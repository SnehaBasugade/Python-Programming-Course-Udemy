import pickle

data={"Name":"John",
      "age":30,
      "profession":"Software Engineer",
      "Salary":"$50000",
      "Experience":"10+years"}

writeData=open("mydata.txt","wb")
pickle.dump(data,writeData)
writeData.close()

myfile=open("mydata.txt","rb")
loadData=pickle.load(myfile)
print(loadData)