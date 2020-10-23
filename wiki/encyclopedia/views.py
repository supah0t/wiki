import os

from django.shortcuts import redirect

from django.urls import reverse

from django.core.files.base import ContentFile

from django.shortcuts import render
from django import forms

from .forms import EntryForm

from .models import Entry

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
            
def newpage(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            textBody = form.cleaned_data['textBody']
            full_filename=os.path.join('entries', title+'.md')
            fout = open(full_filename, 'wt')
            fout.write(textBody)
            fout.close()
            return redirect('title', title=title)
            #return render(request, "encyclopedia/entry.html", {
            #    "title": title,
            #    "info": textBody
            #})
    else:
        return render(request, "encyclopedia/newpage.html", {
            'form': EntryForm()
        })