print("select youe ride:")
print("1.bite")
print("2.car")

#take input of number 1 or 2
#select your ride
choice= int(input("enter your choice"))
#user enterirng option 1
if(choice==1):#cordition 1 outer if statement
    print("what type of bite?")
    print("1.scooty\n")
    print("2.scooter\n")

    #condition for selecting the tye of bite
    choice2=int(input("enter your choice2:"))
    if choice2==1: #inner if statment
        print("you have selected scooty")
    else:
        print("you have selected a scooter")

#user entering option 2
elif(choice==2): #outer elif statement
    print("what type of car?")
    print("1.sedan")
    print("2.XUV")
    choice3=int(input("enter your choice3:"))