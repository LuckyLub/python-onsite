'''

Building on the example more_APIs/00_slack, make a new database with two tables to model this object:

{
        "link": "the fetched URL",
        "description": "short blurb describing the resource (if available)",
        "date_added": "when was it posted?",
        "read": False  # defaults to False, change to True if you read it
        "rating": 0  # on a scale from 1-10, initially 0
        "comments": [
            "a list of strings",
            "with comments on the resource",
        ]
        "starred": False,  # defaults to False, change to True if you think it's great
}

Think about what tables are required to model this object. Do you need two tables? Three?

Now, instead of saving the list of these objects to a JSON file, persist the data
to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''


import sqlalchemy as sqa
from slackclient import SlackClient
from sqlalchemy.exc import IntegrityError
import datetime
from Documents import postgres_login as plogin
from Documents import slack_token as slogin


DATABASE_URI = f'postgres+psycopg2://{plogin.username}:{plogin.password}@localhost:5432/slack'
engine = sqa.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = sqa.MetaData()

posts = sqa.Table('posts', metadata,
                  sqa.Column('id', sqa.Integer, primary_key=True, autoincrement=True),
                  sqa.Column('link', sqa.VARCHAR()),
                  sqa.Column('description', sqa.VARCHAR()),
                  sqa.Column('date_added', sqa.VARCHAR()),
                  sqa.Column('read', sqa.BOOLEAN(), default=False, nullable=False),
                  sqa.Column('rating', sqa.SmallInteger, default= 0, nullable=False),
                  sqa.Column('starred', sqa.BOOLEAN, default= False, nullable=False),
                  sqa.Column('slack_id', sqa.VARCHAR(), unique=True, default= False, nullable=False)
                  )

comments = sqa.Table('comments', metadata,
                     sqa.Column('id', sqa.Integer(), primary_key=True, autoincrement=True),
                     sqa.Column('comment', sqa.VARCHAR()),
                  )

users = sqa.Table('users', metadata,
                     sqa.Column('id', sqa.Integer(), primary_key=True, autoincrement=True),
                     sqa.Column('user_name', sqa.VARCHAR()),
                  )

posts_comments = sqa.Table('posts_comments', metadata,
                           sqa.Column('id', sqa.Integer(), primary_key=True, autoincrement=True),
                           sqa.Column('postsID', sqa.Integer(), nullable=False),
                           sqa.Column('commentsID', sqa.Integer(), nullable=False))

posts_users = sqa.Table('posts_users', metadata,
                        sqa.Column('id', sqa.Integer(), primary_key=True, autoincrement=True),
                        sqa.Column('postsID', sqa.Integer(), nullable=False),
                        sqa.Column('usersID', sqa.Integer(), nullable=False))

comments_users = sqa.Table('comments_users', metadata,
                           sqa.Column('id', sqa.Integer(), primary_key=True, autoincrement=True),
                           sqa.Column('commentsID', sqa.Integer(), nullable=False),
                           sqa.Column('usersID', sqa.Integer(), nullable=False))

metadata.create_all(engine)

slack_channel = "CGUDWETHR"
sc = SlackClient(slogin.key)

res = sc.api_call("channels.history", channel=slack_channel)

for dict_ in res["messages"]:
    if dict_["type"] == "message" and "attachments" in dict_.keys():
        original_slack_id = str(dict_["client_msg_id"])
        for sub_dict in dict_["attachments"]:
            if "original_url" not in sub_dict.keys():
                link = sub_dict["app_unfurl_url"]
            else:
                link = sub_dict["original_url"]
            description = sub_dict["text"]
            date_added = str(dict_["ts"])
            slack_id = original_slack_id + str(sub_dict["id"])

            insert_query = sqa.insert(posts, {
                "link": link,
                "description": description,
                "date_added": date_added,
                "slack_id": slack_id
            })
            try:
                result_proxy = connection.execute(insert_query)
            except IntegrityError as IE:
                print(f"This post is already recorded: {slack_id}")

