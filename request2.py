import requests
import json

course=requests.get('https://api.merakilearn.org/courses')
data=course.json()
# print(data)
with open("maincourse.json","w") as f:
    json.dump(data,f,indent=2)


s_n=1
for i in data:
    print(s_n,i["name"],":",i["id"])
    s_n+=1


user1=int(input("which course you want:"))
no=user1-1
print(data[no]["name"],":",data[no]["id"])
# course1=requests.get('https://api.merakilearn.org/courses/'+data[no]["id"]+'/exercises')
# data1=course1.json()
# print(data1)
# s=1
# s1=1
# for i in data1["course"]["exercises"]:

#     print(s,i["name"],"=",i["id"])
#     # print(s1,i["slug"])
    # s+=1

second_input=input("enter next or previous,(n/p):")
if second_input=="p":
    s_n=1
    for i in data:
        print(s_n,i["name"],":",i["id"])
        s_n+=1
    next_input=int(input("which you want,please enter number;"))
    print(data[next_input-1]["name"],":",data[next_input]["id"])

elif second_input=="n":
    data1=requests.get('https://api.merakilearn.org/courses/'+data[no]["id"]+'/exercises')
    inside_course=data1.json()
    # print(inside_course)

    with open("inside_topic.json","w") as fn:
        json.dump(inside_course,fn,indent=2)

    s_n1=1
    s_n2=1
    list1=[]
    list2=[]
    main_list=[]
    for j in inside_course["course"]["exercises"]:
        if j["parent_exercise_id"]==None:
            print(s_n1,j["name"])
            print(" ",s_n2,j["name"])
            s_n1+=1
            list1.append(j)
            list2.append(j)
            main_list.append(j)
        elif j["parent_exercise_id"]==j["id"]:
            print(s_n1,j["name"])
            s_n1+=1
            list1.append(j)
            main_list.append(j)
            new_n=1
        elif j["parent_exercise_id"]!=j["id"]:
            print(" ",new_n,j["name"])
            new_n+=1
            list2.append(j)
            main_list.append(j)
# print(main_list)
    third_input=int(input("which topic you want to read,enter name:")) 
    for i in list1:
        if i["parent_exercise_id"]==i["id"]:
            print(list1[third_input-1]["name"])
            break
    num=(list1[third_input-1]["id"])
    var=[]
    var3=[]
    new_num=1
    for j in list2:
        if j["parent_exercise_id"]==num:
            print(" ",new_num,j["name"])
            var.append(j["name"])
            var3.append(j["content"])
            new_num+=1
    i=0
    while i<=len(var):
        child=int(input("enter the child exercise you want:"))
        for k in range(len(var)):
            if (third_input-1)==k:
                print(var[k])
                print(var3[k])
        i+=1
#             again_enter_child=int(input("again enter the child exercise you want:"))
#             for m in range(len(var)):
#                 if (again_enter_child-1)==m:
#                     print(var[m])
#                     print(var3[m])
else:
    print("enter the correct input....")

        


with open("list1.json",'w') as f:
    json.dump(list1,f,indent=2)
with open("list2.json","w") as fn:
    json.dump(list2,fn,indent=2)
with open("main_list.json","w") as fs:
    json.dump(main_list,fs,indent=2)











