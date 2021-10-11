# Q. Write a program to create a dictionary of Hindi words with values as their English Translation. Provide user with an option to look it up.

dict = {'Khush' :'Happy', 'Rona' :'Cry', 'Dukhi' :'Sad'}

for key in dict:
    print (key)
print("Enter the hindi word from above list whose english meaning you want : ")
x=input()

print(dict[x])


# Output :    Khush
#             Rona
#             Dukhi
#             Enter the hindi word from above list whose english meaning you want :
#             Happy
#             Cry
#             Sad
