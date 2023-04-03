#first part:

for number in range(45, 210):
    if number == 100:
        continue
    if number == 205:
        break

    print(number)



    # second part:

while int(input("what is the product of 7 * 24 ?")) != 7*24:
    print(" and show the user the question again.")
else:
    print("You answered this Question correctly")
