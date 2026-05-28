#take input for the statement that he can attend the exam or not
medical_cause = input("did you have any medical cause?(Y/N):").strip().upper()

#checking the user input and predecting output accordingly
if medical_cause=='Y': # Condition 1
    print("You are allowed")
else:
    #take input of the attendence
    atten= int(input("enter the attendance of the student"))

    if atten>=75: #Condition 2
        print("Allowed")
    else:
        print("not allowed")