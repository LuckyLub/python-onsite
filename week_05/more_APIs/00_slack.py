'''
Create a slack API token for the codingnomads workspace.

Using the slackclient package, fetch all comments that include links
from the python-resources channel.

Store the links in a JSON file that has the following form:
[
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
    },
    # next link item
]

We will continue to work with this data throughout the week, so make sure to complete it!

'''

from slackclient import SlackClient
from pprint import pprint
from datetime import datetime
import json

token_path = "Documents/slack_token"
with open(token_path, "r") as fin:
    token = fin.read()

slack_channel = "CGUDWETHR"
sc = SlackClient(token)

res = sc.api_call("channels.history", channel=slack_channel)
pprint(res["messages"])

output_list = []

for dict_ in res["messages"]:
    if dict_["type"] == "message" and "attachments" in dict_.keys():
        for sub_dict in dict_["attachments"]:
            output_dict = {}
            if "original_url" not in sub_dict.keys():
                output_dict["link"] = sub_dict["app_unfurl_url"]
            else:
                output_dict["link"] = sub_dict["original_url"]
            output_dict["description"] = sub_dict["text"]
            output_dict["date_added"] = dict_["ts"]
            output_dict["read"] = False
            output_dict["rating"] = 0
            output_dict["comments"] = []
            output_dict["starred"] = False

            output_list.append(output_dict)

output_file_path = "Documents/slack_output.json"

with open(output_file_path, "w") as fout:
    json.dump(output_list, fout)

