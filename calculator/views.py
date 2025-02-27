from django.shortcuts import render
from django.shortcuts import render

from . import models

def kalkulacka(request):
    error_msg = None
    vysledek = None
    if request.method == "POST":
        try:
            float(request.POST["a"])
            float(request.POST["b"])
        except:
            error_msg = "A nebo B není číslo!"
            return render(request, "calculator/kalkulacka.html", dict(error_msg=error_msg, vysledek=vysledek))

        if request.POST["operator"] == "/" and float(request.POST["b"]) == 0:
            error_msg = "Chyba dělení nulou"
            return render(request, "calculator/kalkulacka.html", dict(error_msg=error_msg, vysledek=vysledek))
        if request.POST["operator"] == "+":
            vysledek = models.secti(request.POST["a"], request.POST["b"])
        elif request.POST["operator"] == "-":
            vysledek = models.odecti(request.POST["a"], request.POST["b"])
        elif request.POST["operator"] == "/":
            vysledek = models.vydel(request.POST["a"], request.POST["b"])
        elif request.POST["operator"] == "*":
            vysledek = models.vynasob(request.POST["a"], request.POST["b"])
        else:
            error_msg = "Něco se pokazilo :("
            return render(request, "calculator/kalkulacka.html", dict(error_msg=error_msg, vysledek=vysledek))
    return render(request, "calculator/kalkulacka.html", dict(error_msg=error_msg, vysledek=vysledek))
