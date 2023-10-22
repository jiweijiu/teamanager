from django.http import HttpResponse
from django.shortcuts import render, redirect

from app.models import Teacher,Student


# Create your views here.
def index(request):
    tea=Teacher.objects.all()
    data={
        "tea":tea,
    }
    return render(request,"app/index.html",data)


def register(request):
    if request.method=="GET":
        return render(request,"app/register.html")
    if request.method=="POST":
        account=request.POST.get("account")
        password=request.POST.get("password")
        name=request.POST.get("name")
        try:
            Teacher.objects.create(account=account,password=password,name=name)
        except Exception as e:
            return redirect("/app/register/")
        return redirect("/app/login/")



def login(request):
    if request.method=="GET":
        return render(request,"app/login.html")
    if request.method=="POST":
        account=request.POST.get("account")
        password=request.POST.get("password")
        try:
            tea=Teacher.objects.get(account=account)
        except Exception as e:
            return redirect("/app/login/")
        if password!=tea.password:
            return redirect("/app/login/")
        request.session["account"]=tea.account
        return redirect("/app/home")




def home(request):
    if request.method=="GET":
        account=request.session.get("account")
        # if account=="未登录":
        #     data={
        #
        #     }
        #     return
        tea=Teacher.objects.get(account=account)
        stbind=tea.student_set.all().filter(isbind=True)
        stno=Student.objects.all().filter(isbind=False)
        data={
            "stbind":stbind,
            "stno":stno,
            "account":account,
        }
        return render(request,"app/home.html",data)



def addstudent(request):
    if request.method=="GET":
        return render(request,"app/addstudent.html")
    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")

        account=request.session.get("account")
        tea=Teacher.objects.get(account=account)
        try:
            Student.objects.create(name=name,age=age,teacher=tea)
        # Student.objects.create(name=name,age=age,teacher=Teacher(tea.id))
        except Exception as e:
            return redirect("/app/addstudent/")
        return redirect("/app/home/")


def delstu(request):
    if request.method=="GET":
        print("11111111111111111")
        id=request.GET.get("id")
        stu=Student.objects.get(id=id)
        stu.isbind=False
        stu.save()
        return redirect("/app/home/")


def bindstu(request):
    # if request.method=="GET":
    if request.method=="GET":
        id=request.GET.get("id")
        stu=Student.objects.get(id=id)

        account=request.session.get("account")
        tea=Teacher.objects.get(account=account)

        stu.isbind=True
        stu.teacher=tea
        # stu.teacher_id=tea.id
        stu.save()
        return redirect("/app/home/")


def quit(request):
    request.session.flush()
    return redirect("/app/index")