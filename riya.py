import requests
import json
x = requests.get('http://saral.navgurukul.org/api/courses')
a=x.json()
# print(a)
with open("request.json","w")as file:
    c=json.dump(a,file,indent=4)
def course():
    index=1
    for i in a["availableCourses"]:
        print(index,i["name"],i["id"])
        index=index+1
    for c in a["availableCourses"]:
        course=int(input("selectyour courses"))
        select=a["availableCourses"][course-1]["id"]
        var=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercises/get")
        for c in a["availableCourses"]:
            course=int(input("selectyour courses"))
            select=a["availableCourses"][course-1]["id"]
            var=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercises")
            data2=var.json()
            print(data2)
            data2=var.json()
            print(data2)
course()