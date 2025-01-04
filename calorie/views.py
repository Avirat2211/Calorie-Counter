from django.shortcuts import render,redirect
from .models import Food, Consume
# Create your views here.


def index(request):
    if request.method == 'POST':
        inp = request.POST.get('food_consumed')
        f = Food.objects.get(name=inp)
        user = request.user
        cons = Consume(user = user,food_consumed = f)
        cons.save()
    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user= request.user)
    return render(request,'calorie/index.html',{'foods':foods,'consumed_food':consumed_food})


def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == "POST":
        consumed_food.delete()
        return redirect('/')
    return render(request,'calorie/delete.html')