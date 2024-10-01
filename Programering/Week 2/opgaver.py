name="Josefine"
age=17

#print(name, age)
#print(type(name), type(age))

question="How old is "+name+"?"
answer=name+" is "+str(age)+ " years old."

#print(question)
#print(answer)


is_adult=age>=18

#print(is_adult)

is_student=True
student_campus="Ballerup"

is_dtu_student=is_student and (student_campus=="Lyngby" or student_campus=="Ballerup")
#print(is_dtu_student)


current_record=5.24
new_record_attempt=5.8
#print(current_record)

current_record=max(current_record,new_record_attempt)

#print(current_record)

drot=1740
full=360
remain=drot//full
remainD=drot-remain*full

#print(remain)
#print(remainD)


