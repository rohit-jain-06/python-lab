# Write a program to fill in a letter template given below with name and date: 
# letter = ''' Dear <|Name|>  You are selected  <|Date|> '''

Name = input("Enter your Name: ")
Date = input("Enter Date: ")
print("''' Dear " + Name + "\n You are selected" + "\n" + Date + "'''") 

# Output: Enter your Name: Rohit Jain
#         Enter Date: 09-10-2021
#         ''' Dear Rohit Jain
#             You are selected
#             09-10-2021'''
