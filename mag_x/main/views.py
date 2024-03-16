from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.views.decorators.csrf import csrf_protect

from .models import Products, Contact, About, ClientProd


def check_login(req):
    if req.user.is_authenticated:
        return True
    else:
        return False


# Create your views here.
def home(request):
    logged = check_login(request)
    template = loader.get_template('home.html')
    q_set = Products.objects.all().values()
    prod_list = []
    for rec in q_set:
        prod_list.append(rec)
    data_from_db = {"prod_list": prod_list, "login": logged}
    return HttpResponse(template.render(data_from_db, request))


def user_logout(request):
    if check_login(request):
        logout(request)
    return redirect('/')


@csrf_protect
def record_pref(request):
    logged = check_login(request)
    alert_msg = ""
    if logged and request.method == "POST" and request.POST["prod_id"] != "":
        new_pref = request.POST["prod_id"]
        try:
            rec = ClientProd.objects.get(client_id=request.user.id)
            if rec.client_pref != "":
                pref_list = rec.client_pref.split(";")
                if new_pref not in pref_list:
                    pref_list.append(new_pref)
                rec.client_pref = ";".join(pref_list)
            else:
                rec.client_pref = new_pref
            rec.save()
        except ClientProd.DoesNotExist:
            rec = ClientProd(client_id=request.user.id, client_pref=new_pref, client_bas="")
            rec.save()
        return HttpResponse(alert_msg)
    else:
        return redirect('/login')


@csrf_protect
def add_to_cart(request):
    logged = check_login(request)
    alert_msg = ""
    if logged and request.method == "POST" and request.POST["prod_id"] != "":
        new_cart = request.POST["prod_id"]
        try:
            rec = ClientProd.objects.get(client_id=request.user.id)
            if rec.client_bas != "":
                cart_list = rec.client_bas.split(";")
                if new_cart not in cart_list:
                    cart_list.append(new_cart)
                rec.client_bas = ";".join(cart_list)
            else:
                rec.client_bas = new_cart
            rec.save()
        except ClientProd.DoesNotExist:
            rec = ClientProd(client_id=request.user.id, client_pref="", client_bas=new_cart)
            rec.save()
        return HttpResponse(alert_msg)
    else:
        return redirect('/login')


def prod_detail(request):
    logged = check_login(request)
    if logged:
        template = loader.get_template('prod_detail_login.html')
    else:
        template = loader.get_template('prod_detail.html')
    if request.method == "GET":
        prod_id = request.GET["p"]
        rec = Products.objects.get(prod_id=prod_id)
        data_from_db = {"prod": rec, "login": logged}
        return HttpResponse(template.render(data_from_db))
    return redirect('/')


def despre(request):
    logged = check_login(request)
    template = loader.get_template('despre.html')
    q_set = About.objects.all().values()
    data_from_db = {}
    for rec in q_set:
        data_from_db[rec['about_text_name']] = rec['about_text_txt']
    data_from_db['login'] = logged
    return HttpResponse(template.render(data_from_db, request))


@csrf_protect
def contact(request):
    logged = check_login(request)
    alert_msg = ""
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        msg = request.POST["message"]
        if name == "" or email == "" or phone == "" or msg == "":
            alert_msg = "Lipsesc informatii, email-ul nu a fost trimis"
        else:
            # afisaza un mesaj pentru teste
            alert_msg = "Email-ul a fost trimis"
    template = loader.get_template('contact.html')
    q_set = Contact.objects.all().values()
    data_from_db = {}
    for rec in q_set:
        data_from_db[rec['contact_text_name']] = rec['contact_text_txt']
    data_from_db['login'] = logged
    data_from_db['alert_msg'] = alert_msg
    return HttpResponse(template.render(data_from_db, request))

