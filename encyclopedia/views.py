from random import randrange
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from . import util
import markdown2

class NewWikiForm(forms.Form):
    title = forms.CharField(label="Wiki title", min_length=2, widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the title"
        }))

    content = forms.CharField(label="Wiki content", min_length=10, widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 8,
            "placeholder": "Enter the content"
        }))

def index(request):
    wikis = util.list_entries()
    destination_paths = []

    for wiki in wikis:
        destination_paths.append(
            "wiki/" + wiki
            )

    items = zip(wikis, destination_paths)

    return render(request, "encyclopedia/index.html", {
        "items": items
    })

def get_wiki(request, wiki_name):
    wiki = util.get_entry(wiki_name)
    
    if wiki is None:
        return HttpResponseRedirect(reverse("wiki_not_found"))
    
    return render(request, "encyclopedia/get_wiki.html", {
        "wiki_name": wiki_name,
        "wiki": markdown2.markdown(util.get_entry(wiki_name)),
        "upd_link": f"/wiki/edit/{wiki_name}"
    })

def add_wiki(request):
    if request.method == "POST":
        form = NewWikiForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            title = data["title"]
            content = data["content"]

            if util.get_entry(title):
                return render(request, "encyclopedia/add_wiki.html", {
                    "form": form,
                    "error": "Entry already exists!"
                })

            util.save_entry(title, content)
            
            return HttpResponseRedirect(f"/wiki/{title}")
        
        else:
            return render(request, "encyclopedia/add_wiki.html", {
                "form": form,
                "error": "Invalid input"
            })
    return render(request, "encyclopedia/add_wiki.html", {
            "form": NewWikiForm(),
    })

def update_wiki(request, wiki_name):
    if request.method == "POST":
        print("1")
        upd_form = NewWikiForm(request.POST)
        if upd_form.is_valid():
            print("2")
            data = upd_form.cleaned_data
            title = data["title"]
            content = data["content"]

            util.save_entry(title, content)

            return HttpResponseRedirect(f"/wiki/{title}")
        else:
            print("3")
            return render(request, "encyclopedia/update_wiki.html", {
                "form": upd_form,
                "error": "Invalid input"
            })

    if util.get_entry(wiki_name):
        print("4")
        content_old = util.get_entry(wiki_name)
        title_old = wiki_name

        upd_form = NewWikiForm()
        upd_form.fields["title"].initial = title_old
        upd_form.fields["content"].initial = content_old

        return render(request, "encyclopedia/update_wiki.html", {
            "form": upd_form
        })
    print("5")
    return HttpResponseRedirect(reverse("wiki_not_found"))

def search_wiki(request):
    if request.method == "GET" and request.GET.get("q"):
        q = request.GET.get("q")

        wikis = util.list_entries()
        results = []

        for wiki in wikis:
            if q == wiki:
                return HttpResponseRedirect(f"/wiki/{wiki}")
            if q.lower() in wiki.lower():
                results.append({
                    "destination": f"/wiki/{wiki}",
                    "title": wiki
                })
        return render(request, "encyclopedia/search_wiki.html", {
            "results": results,
            "q": q
        })
    else:
        return HttpResponseRedirect(reverse("index"))


def random_wiki(request):
    wikis = util.list_entries()
    if len(wikis) == 0:
        return HttpResponseRedirect(reverse("index"))
    index = randrange(len(wikis))
    return HttpResponseRedirect(f"/wiki/{wikis[index]}")

def wiki_not_found(request):
    return render(request, "encyclopedia/wiki_not_found.html")
