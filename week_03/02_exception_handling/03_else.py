'''
Write a script that demonstrates a try/except/else.

'''

list1 = [1,2,3,4,5,6,7,8,9]
list2 = ["a","b","c","d","e","f","g","h", "i", "j"]
lists = [list1, list2]

def trying_if_out(a_list):

    try:
        a = a_list[9]

    except IndexError:
        print(a_list[0])

    else:
        print(a)



for l in lists:
    trying_if_out(l)

