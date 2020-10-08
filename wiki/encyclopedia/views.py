from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def test(request):
    return render(request, "encyclopedia/test.html")
    
def title(request, title):
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "info": util.get_entry(title)
    })