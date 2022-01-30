from json import dumps
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import JsonResponse

# Models and Forms
from .models import CookEntry
from menu.models import recipeModel

# Create your views here.


def cook(request):
    recipe_name = CookEntry.objects.all()[0].entry
    recipe = recipeModel.objects.get(name=recipe_name)
    context = {
        "recipe": recipe,
    }
    return render(request, 'cook/cook.html', context)


@csrf_exempt
def route_cook(request):
    if request.is_ajax and request.method == "POST":
        recipe_name = request.POST['name']
        CookEntry.objects.all().delete()
        et = CookEntry(entry=recipe_name)
        et.save()
        return JsonResponse({"instance": "instance"}, status=200)
    return JsonResponse({"error": "error"}, status=400)

