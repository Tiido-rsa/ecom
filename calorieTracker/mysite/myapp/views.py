from django.shortcuts import render
from .models import Consume, food

def index(request):
    
    if request.method == 'POST':
        food_consumed   = request.POST.get('food_consumed')
        consume         = food.objects.get(name=food_consumed)    
        user            = request.user
        consume         = Consume(food=consume, user=user)
        consume.save()
        foods           = food.objects.all()
        consumed_food   = Consume.objects.filter(user=user)
        
    else:
        consumed_food = Consume.objects.filter(user=request.user)
        foods = food.objects.all()
    
    context = {
        'foods': foods,
        'consumes': consumed_food
    }
    
    return render(request, 'index.html', context)