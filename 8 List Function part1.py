list1=[10,100,20,90,30,80,50,70,90]
print("List before updation:",list1)
del list1[4]
print("List after deletion:",list1)
list1.pop()
print(list1)
list1.sort()
print(list1)
list1.remove(10)
print(list1)
list2=[200,7000]
list1.append(list2)
print(list1)
list3=[600,5000]
list1.extend(list3)
print(list1)
