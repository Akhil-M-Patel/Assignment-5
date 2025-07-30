dict={'Alice':85,'Sam':80,'Dexter':98}
std_name=input("Enter the student's name: ")
if std_name in dict:
    print(f"{std_name}'s marks: {dict[std_name]}")
else:
    print("Student not found.")