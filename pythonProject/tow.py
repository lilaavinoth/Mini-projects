ty = 'string is {0}'.format("test")

print(ty)

alist = [10,20,30,40,50,60,70,80]
print(alist[3:])

mylist = [1,'string',3]
print(len(mylist))

print(mylist[1])

print(mylist[:2])

add_list = ['add', 455]

print(mylist+add_list)
new_list = mylist+add_list
new_list[0] = "one"
print(new_list)
new_list.append("appended")
print(new_list)
new_list.pop(1)
print(new_list)
namelist = ["lilaa", "vinoth", "hari"]
namelist.sort()
print(namelist)
namelist.reverse()
print(namelist)
stringing = "samsung"
var = stringing[::-1]
print(var)