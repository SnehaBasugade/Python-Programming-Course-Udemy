import json

data={"Name":"John","age":30,"City":"New Youd"}
file=open("json-data.json","w")
json.dump(data,file,indent=4)
print("JSON data has been written to json-data.json file")
myfile=open("json-data.json","r")
with("json-data.json","r") as file:
    loadData=json.load(myfile)
    print(loadData)