from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from my_extra.pas_gen import pas_gen

from my_extra.gen_logs import Logs


@csrf_protect
def generate_pas(request):
    if request.method == "POST":
        return HttpResponse(pas_gen(12))


def create_user(name, email, password):
    user = User.objects.create_user(name, email, password)
    user.save()


@csrf_protect
def user_login(request):
    data = {"alert_msg": ""}
    user_log = Logs(log_name="user_login.log",
                    log_location="",
                    log_dir="user_logs")
    if request.method == "POST":
        print(request.POST)
        if request.POST["form"] == "Login":
            if "user_name" in request.POST and "user_pas" in request.POST:
                user_name = request.POST["user_name"]
                user_pas = request.POST["user_pas"]
                user = authenticate(request, username=user_name, password=user_pas)
                if user is not None:
                    login(request, user=user)
                    user_log.write(f"Login user:  {user_name}")
                    return redirect('/adm')
                else:
                    data["alert_msg"] = "Atentie! Datele au fost incorecte"
        if request.POST["form"] == "Creaza Cont":
            user_name = request.POST["user_name"]
            user_email = request.POST["user_email"]
            user_pas_1 = request.POST["user_pas_1"]
            user_pas_2 = request.POST["user_pas_2"]
            if user_name == "" or user_email == "" or user_pas_1 == "" or user_pas_2 == "":
                data["alert_msg"] = "Lipsesc informatii, nu ati fost inregistrat"
            else:
                if user_pas_1 == user_pas_2:
                    create_user(user_name, user_email, user_pas_1)
                    data["alert_msg"] = "Ati fost inregistrat cu succes"
    template = loader.get_template('login.html')
    return HttpResponse(template.render(data, request))
