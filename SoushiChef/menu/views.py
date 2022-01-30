from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Bringing in models
from signup.models import userprofile
from .models import recipeModel

# Imports
import json
import os
import datetime

#Forms
from .forms import Search

# Create your views here.
def menu(request):
    user = userprofile.objects.get(username = "jlo411")
    u_favorites = user.favorites.all()
    # Handling search
    if request.method == 'POST':
        search_form = Search(data=request.POST)
        if search_form.is_valid():
            search = request.POST['search']
            results = recipeModel.objects.filter(name__icontains = search)
            context = {
                "favorites": u_favorites,
                "search": search,
                "results": results,
                "searchbar": Search
            }
            return render(request, 'menu/search.html', context)
    # Load data
    initalize_recipes()
        
    # Render Page w/ Data
    recipes = recipeModel.objects.all()
    print(u_favorites)
    context = {
        "favorites": u_favorites,
        "user": user,
        "recipes": recipes,
        "searchbar": Search
    }
    return render(request, 'menu/menu.html', context)

@csrf_exempt
def favorite(request):
    if request.is_ajax and request.method == "POST":
        recipe_name = request.POST['name']
        recipe = recipeModel.objects.get(name = recipe_name)
        user = userprofile.objects.get(username = "jlo411")
        user.favorites.add(recipe)
        user.save()
        return JsonResponse({"instance": "instance"}, status=200)
    return JsonResponse({"error": "error"}, status=400)


# Helper Functions
def initalize_recipes():
    # Clearing Dupes
    recipes = recipeModel.objects.all().delete()

    # Openning json and initalizng models
    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_file = open(os.path.join(script_dir, 'data.json'))
    data = json.load(config_file)['data']
    
    for i in data:
        name = i['name']
        recipe = list(i["recipe"].values())
        for j in range(len(recipe)):
            if "," in recipe[j]:
                recipe[j] = recipe[j].replace(',',' |')
        time = datetime.timedelta(minutes=int(i["time"]))
        ingredients = list(i["ingredients"].values())
        for j in range(len(ingredients)):
            if "," in ingredients[j]:
                ingredients[j] = ingredients[j].replace(',',' |')
        description = "No Description Available"
        if len(i["description"]) != 0:
            description = i["description"]
        serving_size = i["serving_size"]
        image = i['image']
        # Models
        recipeObj = recipeModel(name=name, recipe=recipe, time=time, ingredients=ingredients, description=description, serving_size=serving_size, image=image)
        recipeObj.save()
