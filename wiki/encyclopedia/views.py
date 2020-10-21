from django.shortcuts import render
from django import forms

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def test(request):
    return render(request, "encyclopedia/test.html")
    
def title(request, title):
    info = util.get_entry(title)
    if info:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "info": info
    })
    else:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })
        
def search(request):
    search = request.GET.get('q')
    info = util.get_entry(search)
    if info:
        return render(request, "encyclopedia/search.html", {
            "title": search,
            "info": info
    })
    else:
        names = []
        for entry in util.list_entries():
            if entry.lower().find(search.lower()) != -1:
                names.append(entry)
        if names:
            return render(request, "encyclopedia/results.html", {
                        "title": search,
                        "entries": names 
                    })
        else:
            return render(request, "encyclopedia/error.html", {
                "title": search
            })