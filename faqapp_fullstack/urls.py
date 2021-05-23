from django.contrib import admin
from django.urls import path, include
from faqapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('faq/',include('faqapp.urls')),
]
