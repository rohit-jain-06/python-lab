# Q. Write a program to find out whether a given post is talking about ”Simarjeet” or not.

post = input("Enter a post: ")
if (("Simarjeet" in post) or ("simarjeet" in post) or ("SIMARJEET" in post)):
    print("Yes! the post is talking about Simarjeet")
else: 
    print("No! the post is not talking about Simarjeet")


# Output :    Enter a post: Simarjeet
#             Yes! the post is talking about Simarjeet
            
#             Enter a post: harry
#             No! the post is not talking about Simarjeet
