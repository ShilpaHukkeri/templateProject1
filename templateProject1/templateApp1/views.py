from django.shortcuts import render
def employeeviews(r):
    Ename=input("enter a employee name")
    Eid=int(input("enter the id of employee"))
    Edesignation=input("enter the employee designation")
    Esal=int(input("enter the employee sallary"))
    d={'n':Ename,'id':Eid,'des':Edesignation,'sal':Esal}
    return render(r,'templateApp1/1.html',d)
    


