command=input("Enter command: ")
if(command=="help"):
    print('start-to start the car')
    print('stop-to stop the car')
    print('quit-to exit')
elif(command=="start"):
    print('Car started....Ready to go!')
elif(command=="stop"):
    print('Car stopped.')
elif(command=="quit"):
    break
else:
    print("I don't understand that...")

