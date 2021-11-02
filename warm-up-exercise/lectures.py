# result = int(input("Choose an index position: "))

# def user_choice():
#     choice = input ("Please enter a number (0-10): ")
#     return int(choice)

## need data type validation
## check inputs is in 

# def user_choice():
#     choice = "WRONG"

#     while choice.isdigit() == False:
#         choice = input ("Please enter a number (0-10): ")

#         if choice.isdigit() == False:
#             print("Sorry that is not a digit!")

#     return int(choice)

# print(user_choice())

def user_choice():

    choice = "WRONG"
    acceptable_range = range(0,10)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input ("Please enter a number (0-10): ")

        # DIGIT CHECK
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")

        #RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Not in range")
                within_range = False

    return int(choice)

print(user_choice())