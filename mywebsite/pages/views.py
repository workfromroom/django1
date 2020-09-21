from django.shortcuts import render
def home(request):
    from pages.namer import namer
    return render(request,"index.html",{"namer":namer})
def about(request):
    my_name = "Halo, nama saya adalah Ragowo"
    return render(request,"about.html",{"my_name":my_name})
