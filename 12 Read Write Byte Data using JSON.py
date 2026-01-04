import json
data={"Name":"Jhon","age":33,"Experience":"10+years",
      "Amount":50000}
print(type(data))
jsonString=json.dumps(data,indent=4)
print(type(jsonString))
print("JSON STRING=",jsonString)
pythonObject=json.loads(jsonString)
print(type(pythonObject))
