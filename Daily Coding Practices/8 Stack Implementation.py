list1 = []

while True:
    oprInput = int(input(''' 
1. Push Element
2. Pop Element
3. Peek Element
4. Display Elements
5. Exit
Choose an option: '''))

    if oprInput == 1:
        userInput = input("Enter a value: ")
        list1.append(userInput)
        print("Pushed Element:", list1)

    elif oprInput == 2:
        if len(list1) == 0:
            print("Stack Empty")
        else:
            popElement = list1.pop()
            print("Popped Element:", popElement)
            print("Stack Now:", list1)

    elif oprInput == 3:
        if len(list1) == 0:
            print("Stack Empty")
        else:
            print("Last Element:", list1[-1])

    elif oprInput == 4:
        print("Stack Elements:", list1)

    elif oprInput == 5:
        break

    else:
        print("Invalid Operation")

            
            