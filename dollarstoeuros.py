dollar = 1
dollar_amount = float(input("How many dollars do you want to convert to euros?"))
euros = dollar* 0.94540
total_euros = dollar_amount * euros

answer = input("Would you like to convert dollars to euros? yes or no")

while True:
    if answer == "yes":
        print("How many dollars do you want to convert to euros?")
        dollar_amount =input(int("Enter dollar amount to be converted."))
        total_euros = dollar_amount * euros
        print(str(total_euros) + " euros")
        print("Would you like to convert again?")

    else:
        break


print(str(total_euros) + " euros")



5