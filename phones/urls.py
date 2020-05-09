from django.urls import path

from .views import HomePageView, SearchResultsView

from phones import views



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('', views.button_back, name='button_back'),
]