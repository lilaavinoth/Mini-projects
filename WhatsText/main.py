import json
import pywhatkit

f = open('PhoneNumbers.json',)
phoneData = json.load(f)
print(phoneData['phoneNo'])
leng = phoneData['phoneNo']

print(len(leng))

for i in range(len(leng)):
    if (leng[i].get("gender")) == 0:
         genderHolder = "Madam"
    else:
         genderHolder = "Sir"
    print(genderHolder)
    pywhatkit.sendwhatmsg(leng[i].get("number"), genderHolder)
