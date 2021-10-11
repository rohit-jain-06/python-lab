# Q. Replace double spaces with single spaces in previous program

string = input("Enter String: ")
while '  ' in string:
    string = string.replace('  ', ' ')
    print("changed string = " + string)

# Output: Enter String: Rohit  Jain
#         changed string = Rohit Jain
