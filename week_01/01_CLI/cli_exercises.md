# Fundamentals Exercise 1: CLI

Perform the following tasks using the CLI and copy and paste
the commands and results below.

- Navigate to your home directory\
-->cd ~
- Create a new directory called CodingNomads. We will use this folder
to house materials for the course.\
--> mkdir CodingNomads

- Move into the CodingNomads folder\
--> cd CodingNomads


- Create new folder cli_testing\
-->mkdir cli_testing

- Inside of folder cli_testing,
    a. print the directory path\
    --> pwd
    
    b. create 3 new .txt files all with different names (file1.txt,
    file2.txt, file3.txt)\
    --> touch file1.txt file2.txt file3.txt
    
    c. list the contents of the folder\
    --> ls -al
    
    d. rename one of the files
    --> mv file1.txt file4.txt
    
- Inside of folder cli_testing, create a new folder \
--> mkdir "Folder"

- Copy a file from cli_testing to the new folder \
--> cp File2.txt Folder

- Move a different file from cli_testing to the new folder \
--> cp File4.txt Folder
- Demonstrate removing:
    a. A file\
    --> rm file2.txt 

    b. A folder\
    --> rm -rf Folder


## vim

- Use `$ vim` to write some text inside a file \
--> vim file3.txt
- Use `$ cat` print contents of file \
--> cat file3.txt \
--> Let me write some beautiful text around here.
- Use `$ grep` to search for a word inside file \
-->grep "beautiful" file3.txt 
Let me write some beautiful text around here.


## explore advanced CLI

- What is the difference between the two commands > and >>? \
--> overwrite vs insert 

- Create a file hello.txt with the text "how?!", then append the text
    to another file called my_file.txt \
        --> touch hello.txt \
        --> vim hello.txt \
        --> touch my_file.txt \
        --> cat hello.txt >> my_file.txt
        
- Overwrite the content of my_file.txt with "tell me" \
--> echo "tell me" > my_file.txt 