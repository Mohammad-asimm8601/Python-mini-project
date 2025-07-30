# Create an Indian Kirana Store Calculator And bill generator.
x = list()
sum = 0
while(True):
    userInput = input("Enter the item price or press q to quite:")
    if (userInput != 'q'):
        sum += int(userInput)
        print(f"Order total so far: {sum}")
    else:
        print(f"Your Bill total is {sum}. Thanks for shopping  us.")
        break