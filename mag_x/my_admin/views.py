from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from main.models import ClientProd, Products


def check_login(req):
    if req.user.is_authenticated:
        return True
    else:
        return False


# Create your views here.
def my_admin(request):
    logged = check_login(request)
    pref_prod_list = []
    bas_prod_list = []
    if logged:
        try:
            cl_prod_data = ClientProd.objects.get(client_id=request.user.id)
            if cl_prod_data.client_pref != "":
                cl_prod_data_list = cl_prod_data.client_pref.split(";")
                pref_prod_query = Products.objects.filter(prod_id__in=cl_prod_data_list)
                for rec in pref_prod_query:
                    pref_prod_list.append(rec)
            if cl_prod_data.client_bas != "":
                cl_prod_data_list = cl_prod_data.client_bas.split(";")
                bas_prod_query = Products.objects.filter(prod_id__in=cl_prod_data_list)
                for rec in bas_prod_query:
                    bas_prod_list.append(rec)
        except ClientProd.DoesNotExist:
            pass
        template = loader.get_template('adm.html')
        data_from_db = {'pref_prod_list': pref_prod_list, 'bas_prod_list': bas_prod_list, 'login': logged}
        return HttpResponse(template.render(data_from_db, request))
    else:
        return redirect('/login')


@csrf_protect
def del_pref(request):
    logged = check_login(request)
    alert_msg = ""
    if logged and request.method == "POST" and request.POST["prod_id"] != "":
        pref_to_del = request.POST["prod_id"]
        try:
            rec = ClientProd.objects.get(client_id=request.user.id)
            if rec.client_pref != "":
                pref_list = rec.client_pref.split(";")
                if pref_to_del in pref_list:
                    pref_list.remove(pref_to_del)
                else:
                    alert_msg = "Eroare, Pref. nu este in lista"
                rec.client_pref = ";".join(pref_list)
            else:
                alert_msg = "Eroare, Lista de preferinte este goala"
            if alert_msg == "":
                rec.save()
        except ClientProd.DoesNotExist:
            alert_msg = "Eroare, ClientProd lipseste client_id"
        return HttpResponse(alert_msg)
    else:
        return redirect('/login')


@csrf_protect
def del_cart(request):
    logged = check_login(request)
    alert_msg = ""
    if logged and request.method == "POST" and request.POST["prod_id"] != "":
        cart_to_del = request.POST["prod_id"]
        try:
            rec = ClientProd.objects.get(client_id=request.user.id)
            if rec.client_bas != "":
                cart_list = rec.client_bas.split(";")
                if cart_to_del in cart_list:
                    cart_list.remove(cart_to_del)
                else:
                    alert_msg = "Eroare, Cart. nu este in lista"
                rec.client_bas = ";".join(cart_list)
            else:
                alert_msg = "Eroare, Lista de cumparaturi este goala"
            if alert_msg == "":
                rec.save()
        except ClientProd.DoesNotExist:
            alert_msg = "Eroare, ClientProd lipseste client_id"
        return HttpResponse(alert_msg)
    else:
        return redirect('/login')
