# from os import name
import requests
import json

course=requests.get('https://api.merakilearn.org/courses')
data=json.loads(course.text) 
print(type(data))

with open("courses.json","w") as f:
    json.dump(course.json(),f,indent=2)

# # print(file)

with open("courses.json","r") as fn:
    fil=json.load(fn) 


num=1
course_list=[]
id=[]
course_num=[]
main_dic={}
data={}
for i in fil:
    print(num,":",i["name"],":",i["id"])
    id.append(i["id"])
    course_list.append(i["name"])
    course_num.append(num)
    main_dic.update({i["name"]:i["id"]})
    data.update({num:main_dic})
    num+=1
    # print(id)
# print(data)
# print(id)
course_selection=int(input("which course you want:"))

# print(course_list[course_selection-1])
    # break


course1=requests.get('https://api.merakilearn.org/courses/'+fil[course_selection-1]["id"]+'/exercises')
data1=course1.json()
# print(data1)

with open("courselist.json","w") as f:
    json.dump(data1,f,indent=2)

with open("courselist.json","r") as fn:
    course_file=json.load(fn)

# print(course_file)

p_id=[]
c_id=[]

for i,j in course_file.items():
    for k in j["exercises"]:
        if k["id"]==k["parent_exercise_id"]:
            p_id.append(k)
        elif k["id"]!=k["parent_exercise_id"]:
            c_id.append(k)
        elif k["parent_exercise_id"]=="null":
            p_id.append(k)
            c_id.append(k)
# print(p_id)
# print(c_id)

with open("parents_id.json","w") as f:
    json.dump(p_id,f,indent=4)

with open("parents_id.json","r") as fs:
    p_id1=json.load(fs)


with open("child_id.json","w") as fn:
    json.dump(c_id,fn,indent=4)
with open("child_id.json","r") as fr:
    c_id1=json.load(fr)

# print(p_id1)
# print(c_id1)
s1=1
for items in c_id1:
    for item in c_id1:
        if items["id"]==item["id"]:
            print(s1,items["id"])
    s=1
    for k in items.keys():
        if k=="name" or k=="slug":
            print(s,items[k])
        s+=1
    s1+=1
s=1
for items in p_id1:
    for item in p_id1:
        if items["id"]==item["id"]:
            print(s,items["id"])
    s1=1
    for k in items.keys():
        if k=="name" or k=="slug":
            print(s1,items[k])
        s1+=1
    s+=1

# sec_input=input("which course you want (p/n):")
# if sec_input=="p":
#     course1=requests.get('https://api.merakilearn.org/courses/'+fil[course_selection-2]["id"]+'/exercises')
#     data1=course1.json()
# # print(data1)

#     with open("courselist.json","w") as f:
#         json.dump(data1,f,indent=2)

#     with open("courselist.json","r") as fn:
#         course_file=json.load(fn)

#     # print(course_file)

#     p_id=[]
#     c_id=[]

#     for i,j in course_file.items():
#         for k in j["exercises"]:
#             if k["id"]==k["parent_exercise_id"]:
#                 p_id.append(k)
#             elif k["id"]!=k["parent_exercise_id"]:
#                 c_id.append(k)
#             elif k["parent_exercise_id"]=="null":
#                 p_id.append(k)
#                 c_id.append(k)
#     # print(p_id)
#     # print(c_id)
    


#     with open("parents_id.json","w") as f:
#         json.dump(p_id,f,indent=4)

#     with open("parents_id.json","r") as fs:
#         p_id1=json.load(fs)


#     with open("child_id.json","w") as fn:
#         json.dump(c_id,fn,indent=4)
#     with open("child_id.json","r") as fr:
#         c_id1=json.load(fr)

#     # print(p_id1)
#     # print(c_id1)
#     s=1
#     for items in c_id1:
#         for k in items.keys():
#             if k=="name" or k=="slug":
#                 print(s,items[k])
#             s+=1
#     s=1
#     for items in p_id1:
#         for k in items.keys():
#             if k=="name" or k=="slug":
#                 print(s,items[k])
#         s+=1

# elif sec_input=="n":
#     course1=requests.get('https://api.merakilearn.org/courses/'+fil[course_selection]["id"]+'/exercises')
#     data1=course1.json()
#     # print(data1)

#     with open("courselist.json","w") as f:
#         json.dump(data1,f,indent=2)

#     with open("courselist.json","r") as fn:
#         course_file=json.load(fn)

#     # print(course_file)

#     p_id=[]
#     c_id=[]

#     for i,j in course_file.items():
#         for k in j["exercises"]:
#             if k["id"]==k["parent_exercise_id"]:
#                 p_id.append(k)
#             elif k["id"]!=k["parent_exercise_id"]:
#                 c_id.append(k)
#             elif k["parent_exercise_id"]=="null":
#                 p_id.append(k)
#                 c_id.append(k)
#     # print(p_id)
#     # print(c_id)

#     with open("parents_id.json","w") as f:
#         json.dump(p_id,f,indent=4)

#     with open("parents_id.json","r") as fs:
#         p_id1=json.load(fs)


#     with open("child_id.json","w") as fn:
#         json.dump(c_id,fn,indent=4)
#     with open("child_id.json","r") as fr:
#         c_id1=json.load(fr)

#     # print(p_id1)
#     # print(c_id1)
#     s=1
#     for items in c_id1:
#         for k in items.keys():
#             if k=="name" or k=="slug":
#                 print(s,items[k])
#             s+=1
#     s=1
#     for items in p_id1:
#         for k in items.keys():
#             if k=="name" or k=="slug":
#                 print(s,items[k])
#         s+=1
# else:
#     print("your search is over")













        


    
