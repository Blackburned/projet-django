
from django.urls import path

from app.views import homeView, blogSinglesidebar, blogGridsidebar, blogSingle, contactView


urlpatterns = [
    path(route='', view=homeView, name="home"),
    path(route='blog-single-sidebar', view=blogSinglesidebar, name="blogSinglesidebar"),
    path(route='blog-grid-sidebar', view=blogGridsidebar, name="blogGridsidebar"),
    path(route='blog-single', view=blogSingle, name="blogSingle"),
    path(route='contact', view=contactView, name="contact"),


]
