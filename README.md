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
31. Copy template navbar yang ada di web https://getbootstrap.com/docs/4.5/components/navbar/
32. Paste template navbar tsb di bawah tag body di dalam file base.html
33. Beri Tag comment pada <form class="form-inline my-2 my-lg-0"> </form> pada file base.html
34. Beri Tag comment pada <li class="nav-item"></li> pada file base.html
35. Beri Tag comment pada <li class="nav-item dropdown"></li> pada file base.html
36. Beri Tag comment pada <li class="nav-item active"></li> pada file base.html
37. Tambahkan kode sbb di bawah tag </nav>:
    <div class="container">
        {% block content %}
        {% endblock %}
    </div>
38. Update kode sbb di bawah tag <nav class="navbar navbar-expand-lg navbar-light bg-light"> pada file base.html :
    <a class="navbar-brand" href="{% url 'home' %}">Home</a>
39. Update kode sbb di bawah tag <li class="nav-item"> pada file base.html :
    <a class="nav-link" href="{% url 'about' %}">About</a>
40. Hapus tag <a href="{% url 'home' %}">Home</a> | <a href="{% url 'about' %}">About</a> pada file index.html & about.html
41. Tambahkan kode html sbb di atas tag <!-- Optional JavaScript -->
    <br><br><br>
    <center><small>Copyright &copy; Ragowo - All Rights Reserved</small></center>
42. Tambahkan & update kode python pada file views di dalam folder page sbb:
    my_name = "Halo, nama saya adalah Ragowo"
    return render(request,"about.html",{"my_name":my_name}) 
43. Tambahkan kode sbb pada about.html di bawah tag <p>Ini adalah Halaman About </p> di dalam folder templates:
    {{my_name}}
44. Buat file baru di dalam folder pages dengan nama namer.py
45. Tambahkan kode python sbb di dalam file namer.py
    def name():
    return "Ini adalah Website Ragowo"
46. Update kode python sbb pada file views.py di dalam folder pages:
    def home(request):
    from pages.namer import namer
    return render(request,"index.html",{"namer":namer})
47. Tambahkan kode sbb pada index.html di bawah tag <p>Ini adalah Halaman Home </p> di dalam folder templates:
    {{namer}}
48. Buat folder baru bernama static di dalam folder pages
49. Buat folder baru bernama images di dalam folder static
50. Tambahkan foto bertipe jpeg di dalam folder images
51. Tambahkan kode sbb pada file setting.py di posisi paling bawah di dalam folder mywebsite:
    STATICFILES_DIRS = [
        BASE_DIR.joinpath('static')
        ]
52. Copy kode template card dari https://getbootstrap.com/docs/4.5/components/card/
53. Paste kode template card tsb pada pada file index.html di dalam folder templates di bawah {{namer}}:
    <div class="card" style="width: 18rem;">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
54. Update kode template card tsb sbb :
    <div class="card" style="width: 18rem;">
      <img src="{%static 'images/pesawat.jpg'%}" class="card-img-top" alt="About">
      <div class="card-body">
        <h5 class="card-title">About</h5>
        <p class="card-text">About Me</p>
        <a href="{%url 'about'%}" class="btn btn-primary">About Page</a>
      </div>
    </div>

    