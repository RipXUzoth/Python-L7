string = input("Please enter your own sting")
string2 = ('')
for i in string:
    string2 = i + string2
    print("\nThe Original String", string)
    print("\nThe Reversed String", string2)