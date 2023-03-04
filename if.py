name=input("Enter your name ")
length=len(name)
if(length<3):
    print("name must be at least three characters")
elif(length>50):
    print("name can be a maximum of 50 characters")
else:
    print("Name is perfect")
