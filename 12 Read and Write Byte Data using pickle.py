import pickle
data={"Name":"John",
      "age":30,
      "profession":"Software Engineer",
      "Salary":"$50000",
      "Experience":"10+years"}

myData=pickle.dumps(data)
print(pickle.loads(myData))