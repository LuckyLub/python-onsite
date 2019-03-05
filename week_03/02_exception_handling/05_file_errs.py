'''
Read in the first number from 'integers.txt' and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

files = ["integers.txt", "blabla"]

for file in files:
    try:
        with open(file, "r") as fin:
            first_num = int(fin.read().split()[0])

    except IOError:
        pass

    except ValueError:
        pass

    else:
        print(file,": ", 3/first_num)

