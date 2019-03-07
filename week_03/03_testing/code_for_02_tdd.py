
# step 1
# def opener(filepath):
#     pass

# step 2
def opener(filepath):
    with open(filepath) as fin:
        content = fin.read()[:100]

    return content

