list1=[]
for n in range(1,51):
    list1.append(n)
    print(list1)
    
    list2=[n for n in range(1,51) if n%2 == 1]     #n%2 == 1 mean odd numbers
    print(list2)
    
    list3=[n for n in range(1,51) if n%2 == 0]      #n%2 == 0 mean even numbers
    print(list3)