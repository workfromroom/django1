# django1
Langkah2 memulai project django:
1. Buat Repository di github
2. Copy url & paste url github di pycharm
3. Setup VENV di menu setting pycharm
4. Install Django di menu setting pycharm
5. Jalankan code ini di terminal:
   django-admin startproject mywebsite
6. masih di terminal, jalankan code sbb:
   python manage.py runserver
7. masih di terminal, jalankan code sbb:
   python manage.py migrate
8. masih di terminal, jalankan code sbb:
   python manage.py createsuperuser 
9. isikan data sbb:
   username : 
   email :
   password :
10. Ketikkan url ini : http://127.0.0.1:8000/admin
11. Login username & password yang sebelumnya sudah didaftarkan
12. Akses terminal dengan perintah sbb:
    python manage.py startapp pages
13. Menambahkan pages pada setting.py yang ada di dalam folder mywebsite
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
    ]
14. Membuat folder templates di dalam folder pages
15. Buat file index.html & about.html di dalam folder templates
16. Tambahkan kode di bawah ini pada file views di dalam folder pages:
    from django.shortcuts import render
    def home(request):
       return render(request,"index.html",{})
    def about(request):
       return render(request,"about.html",{})
17. Membuat file baru bernama urls di dalam folder pages
18. Tambahkan kode di bawah ini pada file urls di dalam folder mywebsite:
    from django.contrib import admin
    from django.urls import path,include
    urlpatterns = [
            path('admin/', admin.site.urls),
            path('',include('pages.urls')),
        ]
19. Tambahkan kode di bawah ini pada file urls di dalam folder pages:
    from django.urls import path
    from . import views

    urlpatterns = [
            path('',views.home,name='home'),
            path('about/',views.about,name='about'),
        ]
20. Tambahkan kode html di bawah ini di dalam tag body pada file index.html:
    <a href="{% url 'home' %}">Home</a> | <a href="{% url 'about' %}">About</a>
    <h1>Home Page</h1>
    <p>Ini adalah Halaman Home </p>    
21. Tambahkan kode html di bawah ini di dalam tag body pada file about.html:
    <a href="{% url 'home' %}">Home</a> | <a href="{% url 'about' %}">About</a>
    <h1>About Page</h1>
    <p>Ini adalah Halaman About </p>
22. Buat file baru base.html di dalam folder templates
23. Copy starter template bootstrap4 di website https://getbootstrap.com/docs/4.5/getting-started/introduction/
24. Paste starter template booststrap4 di file base.html
25. Tambahkan kode di bawah ini di dalam tag body pada file base.html :
    {% block content %}
    {% endblock %}
26. Tambahkan kode di bawah ini pada file index.html :
    {% extends 'base.html' %}
    {% block content %}
    <!DOCTYPE html>
    <html lang="en">
    </html>
    {% endblock %}
27. Tambahkan kode di bawah ini pada file about.html :
    {% extends 'base.html' %}
    {% block content %}
    <!DOCTYPE html>
    <html lang="en">
    </html>
    {% endblock %}
28. Tambahkan Kode HTML di bawah ini di dalam tag head pada file base.html:
    <title>{% block title %}{% endblock %}</title>
29. Tambahkan Kode HTML di bawah ini di bawah kode {% extends 'base.html' %} pada file index.html:
    {% block title %} My Home Page {% endblock %}
30. Tambahkan Kode HTML di bawah ini di bawah kode {% extends 'base.html' %} pada file about.html:
    {% block title %} About Ragowo {% endblock %}
Stop di video 16