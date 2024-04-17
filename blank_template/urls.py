from django.urls import path, include

urlpatterns = [
    path('', include('blank.urls')),  # This includes all URLs from the blank app
]
