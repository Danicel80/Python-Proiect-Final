Mag-X

Un mic proiect de magazin online.

Este facut cu Python 3.11 si Django.

IDE PyCharm

Librarii necesare pentru functionare:
Django 5.0.3

Structura
Proiectul conține trei Django Apps
- Login cu template-ul login.html
- My-admin cu adm.html.
- Main cu cele trei template-uri principale: cu
Template-ul base.html, un fisier baza în care includem
home.html, despre.html și contact.htm. Pe lângă 
aceste template-uri mai sunt și template-uri mai mici,
 sa zicem fragmente, ce se includ în template-urile 
principale.

- Tot în Main avem și fișierul models.py ce conține structura bazei de date și directorul Static ce conține imaginile afisate în site și fișierul style.css ce conține stitul de afisare a etichetelor HTML din template-uri.