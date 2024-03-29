### **Mag-X**

Un mic proiect de magazin online.

Este facut cu Python 3.11 si Django.

IDE PyCharm

Librarii necesare pentru functionare:
Django 5.0.3

### **Instructiuni:**

Dupa ce ati descarcat aplicatia o puteti rula in doua moduri:
1) Direct din linia de comanda cu comanda:


	python locatie\Python-Proiect-Final-main\mag_x\manage.py runserver

unde in loc de "locatie" veti pune calea catre directorul in care se afla proiectul.
Aceasta aplicatie necesita modulul Django 5.0.3, daca nu este instalat si aveti eroarea:

	ModuleNotFoundError: No module named 'django'

va fi nevoie sa instalati modulul cu comanda:

	pip install django

dupa ce a fost instalat modulul, repetati comanda:

	python locatie\Python-Proiect-Final-main\mag_x\manage.py runserver

Dupa ce porneste aplicatia veti vedea urmatorul text:

	Django version 5.0.3, using settings 'mag_x.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CTRL-BREAK.

Copiati si introduceti adresa "http://127.0.0.1:8000/" intr-un browser web



2) Din PyCharm. Deschideti proiectul si mergeti in Python Packages pentru a va asigura ca este instalat modulul Django 5.0.3. Daca nu este, va fi nevoie sa instalati pachetul, din terminal cu comanda:


	pip install django

Tot in terminal, unde prin comanda "cd mag_x" intrati in directorul unde se afla fisierele principale si dati comanda:

	"py manage.py runserver".

In terminal veti vedea textul:

	Django version 5.0.3, using settings 'mag_x.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CTRL-BREAK.

Puteti da click direct pe adresa pentru a accesa pagina web


### **Structura**

Proiectul conține trei Django Apps
- Login cu template-ul login.html
- My-admin cu adm.html.
- Main cu cele trei template-uri principale: cu
Template-ul base.html, un fisier baza în care includem
home.html, despre.html și contact.htm. Pe lângă 
aceste template-uri mai sunt și template-uri mai mici,
 sa zicem fragmente, ce se includ în template-urile 
principale.

- Tot în Main avem și fișierul models.py ce conține structura bazei de date și directorul Static ce conține imaginile afisate în site și fișierul style.css ce conține stilul de afisare a etichetelor HTML din template-uri.
