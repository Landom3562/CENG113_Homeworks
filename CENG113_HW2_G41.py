print("Welcome to Full adder!") #Printing the required lines and taking input one time before the loop to not use break in the while loop.
print("(1) Compute and Display the Outputs")
print("(2) Quit")

run_option = "0"
while run_option != "1" and run_option !="2":
    run_option = input("You choose: ")
print(f"You have chosen option {run_option}")

if run_option == "1": #Set a flag to decide whether to start to loop again or not.
    running = True
else:
    running = False

while running:
    base_option = input("Which base will you use to enter input (base 16/8/2)? ")
    while base_option != "2" and base_option != "8" and base_option != "16": #Taking an input again in case of an invalid input.
        base_option = input("Please enter a valid base option: ")
    if base_option == "2":
        abc = input("Please enter input in three digit form: ")
        while len(abc) != 3 or (abc[0] != "0" and abc[0] != "1") or (abc[1] != "0" and abc[1] != "1") or (abc[2] != "0" and abc[2] != "1"): #Taking an input again in case of invalid input
            abc = input("Please enter a valid input: ")
        A = int(abc[0]) #Assigning the first,second and the third digits of binary input to the variables which we will use to calculate the sum and C_out
        B = int(abc[1])
        C_in = int(abc[2])
    elif base_option == "8" or base_option == "16":
        abc = input("Please enter input: ")
        while not(abc == "0" or abc == "1" or abc == "2" or abc == "3" or abc == "4" or abc == "5" or abc == "6" or abc == "7"):
            abc = input("Not possible to convert it to 3-digit binary number. Please enter a positive value that is less than or equal to 7: ")
        A = (int(abc) // 4) % 2 #Dividing the number entered to 2 and assigning the remaining to the variables starting from C_in to A.
        B = (int(abc) // 2) % 2
        C_in = int(abc) % 2

    Sum = int((not bool(C_in) or ((not bool(A) or bool(B)) and (not bool(B) or bool(A)))) and (not ((not bool(A) or bool(B)) and (not bool(B) or bool(A))) or bool(C_in))) #Simplified version of C_in xor (A xor B) according to predicate logic laws.
    C_out = int((bool(A) and bool(B)) or (bool(C_in) and (not bool(A) or not bool(B)) and (bool(B) or bool(A)))) #Simplified version of (A and B) or (C_in and (A xor B)) according to predicate logic laws.
    print(f"Sum is {Sum} C_out is {C_out}") 
    print("Welcome to full adder!") #Computing the start of the next round in the loop in order not to compute all the loop when the user selects quit option.
    print("(1) Compute and Display the Outputs")
    print("(2) Quit")

    run_option = 0
    while run_option != "1" and run_option !="2":
        run_option = input("You choose: ")

    if run_option == "1":
        running = True
    else:
        running = False

print("Byee!!")