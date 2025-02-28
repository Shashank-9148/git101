'''def collect_student_data(**data):
    print(data)
    print(type(data))

collect_student_data(Name="Shashank",Age=28,Avg=60.5,Gender="Male")


def collect_student_data(Name,crust,**data):
     print(Name)
     print(data)
     print(crust)
   
     print(type(data))
collect_student_data(Name="Shashank",Age=28,Avg=60.5,Gender="Male",crust=88)


def collect_student_data(Name,**data):
     print(Name)
     print(data)
collect_student_data(Name="surya",Age=27,Avg=78.98,Gender="Male")


def collect_student_data(**data):
     print(data)
     
collect_student_data(Name="rohit",Age = 22,Avg = 67,Gender="m")'''


'''def collect_student_data(Name,crust,**data):
     print(crust)
     print(data)
     print(Name)
collect_student_data("rohith",age = 56, avg = 89,gender = 'm',crust="tiptur")'''



def collect_student_data(Name,crust,**data,):
     print(Name)
     print(data)
     print(crust)
collect_student_data(Name="deepak",Age=23,Avg=79,Place="tiptur",crust="Mahesh")


