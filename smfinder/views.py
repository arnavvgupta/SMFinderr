from django.shortcuts import render

from smfinder.find_socials import find_socials

def index(request):
    return render(request, 'home.html')

def serach(request):
    name = request.GET["name"]
    
    socials = find_socials(name)
    
    for user in socials['twitter']:
        user["det"][2] = "https://www.twitter.com/" + user["det"][1].replace("@", "")

    return render(request, 'search.html', {'name': name, "socials": socials})


def loading(request):
    name = request.GET["name"]
    return render(request, "loading.html", {"name": name})

def get_socials(request):
    name = request.GET["name"]
    socials = find_socials(name)
