

# Code done By Rahul Sen - Student of University of Engineering and Management, Kolkata, CSE Stream
# Bobble.ai internship challenge 2020

# importing required modules
import sys
from collections import defaultdict


# The below is a function to find longest common sub sequence
def longest_common_sub(var1, var2):
    lenght1 = len(var1)
    lenght2 = len(var2)

    # the below array stores the longest sub sequence
    longest_sub = [[0] * (lenght2 + 1) for num in range(lenght1 + 1)]

    for i in range(1, lenght1 + 1):
        for j in range(1, lenght2 + 1):
            if var1[i - 1] == var2[j - 1]:
                longest_sub[i][j] = longest_sub[i - 1][j - 1] + 1
            else:
                longest_sub[i][j] = max(longest_sub[i - 1][j], longest_sub[i][j - 1])
    return longest_sub[lenght1][lenght2]  # return the longest sub sequence


def fun_find(csvfile, the_word):
    # Storing the longest match
    new_dict = defaultdict(int)

    # Reading the .csv file
    for i in csvfile.readlines():
        new_var = i.split(",")[0]
        new_dict[new_var] = longest_common_sub(new_var.lower(), the_word.lower())

        # Ensuring that we get 5 output as mentioned in the question
        if len(new_dict.keys()) > 5:
            # finding  the smallest matched the_word and its length which will be deleted
            lowest = len(the_word) + 1
            lowest_key = -1
            for j in new_dict.keys():
                if new_dict[j] < lowest:
                    lowest = new_dict[j]
                    lowest_key = j

            new_dict.pop(lowest_key, None)

    # Sort the key value pair based on length
    result = [a for a, b in sorted(new_dict.items(), key=lambda item: item[1])]
    return reversed(result)


# Execution of the program begins from there
if __name__ == "__main__":

    # This line checks
    if len(sys.argv) != 3:
        print("Input format was wrong")
        exit(0)  # force exit

    # Preventing error during the read of the fp
    try:
        fn = sys.argv[1]
        tw = sys.argv[2]
        fp = open(fn, 'r')
        res = fun_find(fp, tw)
        for i in res:
            print(i)
    except FileNotFoundError:
        print("The mentioned file was not found, sorry!")
    except Exception:
        print("Error: ", Exception)

# End of program
