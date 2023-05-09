userdata = input("Enter name,surname and dates: ")
userdata1 = userdata.split(" ")
lst = list(userdata1)
username = lst[0]
usersurname = lst[1]
date1 = lst[2]
date1 = date1.split("-")
date2 = lst[3]
date2 = date2.split("-")
age = int(date2[0]) - int(date1[0])
print(f"Name: {username} {usersurname} \nAge: {age}")
