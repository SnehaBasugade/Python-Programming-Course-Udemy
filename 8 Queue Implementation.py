list1 = []

while True:
    oprInput = int(input(''' 
1. Push Element
2. Pop Element
3. Front Element
4. Display Last Element
5. Display All Elements
6. Exit
Choose an option: '''))

    if oprInput == 1:
        userInput = input("Enter a value: ")
        list1.append(userInput)
        print("Pushed Element:", userInput)

    elif oprInput == 2:
        if len(list1) == 0:
            print("Queue Empty")
        else:
            popped = list1[0]
            del list1[0]
            print("Popped element:", popped)

    elif oprInput == 3:
        if len(list1) == 0:
            print("Queue Empty")
        else:
            print("First Element of Queue is:", list1[0])

    elif oprInput == 4:
        if len(list1) == 0:
            print("Queue Empty")
        else:
            print("Last Element:", list1[-1])

    elif oprInput == 5:
        print("Queue Elements:", list1)

    elif oprInput == 6:
        break

    else:
        print("Invalid Operation")
