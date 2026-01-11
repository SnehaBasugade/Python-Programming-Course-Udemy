students={ 'john': {'age': 34, 'education': 'CSE', 'Roll No': 2024, 'Semister': 'first'},
           'vick':{'age': 40, 'education': 'EE', 'Roll No': 2023, 'Semister': 'first'},
           'Rohan':{'age': 50, 'education': 'CSBT', 'Roll No': 2022, 'Semister': 'first'},
           'Mark': {'age': 60, 'education': 'AIDS', 'Roll No': 2021, 'Semister': 'first'}
          }
print(students)
for k,v in students.items():
    print(k,v)
    
    for k,v in students.items():
        print(k,v['age'],v['Semister'])
        
        students['john']['age']=60
        print(k,v)