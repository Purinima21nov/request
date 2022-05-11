import requests
import json
def request(url):
    resp=requests.get(url)
    return resp.json()

url=("https://saral.navgurukul.org/api/courses")
response=requests.get(url)
course=json.loads(response.text)
print(course)

id_list=[]
index=0
while index<len(course["availableCourses"]):
    course_id=course["availableCourses"][index]["id"]
    course_name=course["availableCourses"][index]["name"]
    print(index," ",course_name,course_id)
    id_list.append(course_id)
    index=index+1
    
j=int(input('enter:'))
print("index name : ",course["availableCourses"][j]["name"])
a=course["availableCourses"][j]["id"]
print(a)

