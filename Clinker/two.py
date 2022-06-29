print("im out of function")


def myfuncti(param1, param2):
    print("im inside a function")
    total = param1 + param2
    print(total)
    print(type(total))

b = "this"

a = "Hello World this is a small test"
print(a[::-2])
print(len(a))

if b in a:
    print("its there")
else:
    print("not there")

print(a.upper())
print(a.lower())
print(a.replace("World","Sheeba"))

age = 25
location = "Tuticorin"
name = "im Sheeba im {1} years old. I live in {0}. again {1}".format(age,location)
print(name)
print(type(name))
print(type(age))


myfuncti(5,2)

students = ["Vinoth", "Sheeba" ,"Srivatshan"]

for anyVariableName in students:
    print(anyVariableName)

for x in range(10):
    x += 1
    print("Sheeba {}".format(x))

customerListId = [1,2,7,5,9,5,7,5,6,8]

# for i in customerListId:
#     for g in i:
#         print(i)

thy = 1
while thy <= 50:
    print("Count {}".format(thy))
    thy += 1