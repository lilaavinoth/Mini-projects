import json

myjson = open("Honda_Data.json",'r')
jsondata = myjson.read()

#Parse
obje = json.loads(jsondata)

print(str(obje['firstName']))
print(str(obje['lastName']))


list = obje['address']
print(list[0])
print('the second list is',(list[1]))

for i in range(len(list)):
    # to get all
    print(list[i].get('street'))

# to get specific data
print(list[0].get('street'))


