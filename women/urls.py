from django.urls import path
from women.views.homepage_view import homepage
from women.views.list_view import women_list_view
from women.views.show_post_view import show_post
from women.views.category_list_view import show_category
from women.views.serach_view import search


app_name = "women"


urlpatterns = [
    path('', homepage, name='women_homepage'),
    path('women_list/', women_list_view, name='women_list'),
    path('single_post/<slug:post_slug>/', show_post, name='women_single_post'),
    path('single_category/<slug:cat_slug>/', show_category, name='women_single_category'),
    path('search/', search, name='search')
]