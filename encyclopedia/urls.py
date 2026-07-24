from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/new", views.add_wiki, name="add_wiki"),
    path("wiki/random", views.random_wiki, name="random_wiki"),
    path("wiki/search", views.search_wiki, name="search_wiki"),
    path("wiki/not_found_error", views.wiki_not_found, name="wiki_not_found"),
    path("wiki/edit/<str:wiki_name>", views.update_wiki, name ="update_wiki"),
    path("wiki/<str:wiki_name>", views.get_wiki, name="get_wiki")
]