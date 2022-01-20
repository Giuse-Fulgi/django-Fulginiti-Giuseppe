from django.shortcuts import render

def view_b(request):
    context={
        'materie' : ['Matematica','Italiano','Inglese','Storia','Geografia']
    }
    return render(request,"view_b.html", context)

def view_c(request):
    context={
        'voti' : {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Storia",7,5,4),("Geografia",5,7)],
            'Antonio Barbera':[("Matematica",7,3),("Italiano",7,3),("Storia",7,5,4),("Geografia",5,7)],
            'Nicola Spina':[("Matematica",9,0),("Italiano",7,3),("Storia",7,5,4),("Geografia",5,7)]},
    }
    return render(request,"view_c.html", context)
