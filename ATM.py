print("Enter cash you want to withdraw:")
cash = float(input())
print("Enter initial ammount in you account:")
initial = float(input())

if 0 < initial <= 2000:
    if 0 < cash <= 2000:
        if cash <= (initial - 0.50):
            if cash % 5 ==0:
                print("Transaction Sucessfull.")
                print("Left Balance: ",initial-(cash + 0.50))
            else:
                print("Please enter cash ammount in the multiple of 5.")
        else:
            print("Insufficient Balance.")
    else:
        print("Entered cash ammount is out of range.")
else:
    print("Entered initial ammount is out of range.")