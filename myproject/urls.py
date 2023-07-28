
from django.contrib import admin
from django.urls import path
from enroll.views import insertshowview, deleteview, editview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', insertshowview, name='home'),
    path('delete/<int:id>/', deleteview, name='delete'),
    path('edit/<int:id>/', editview, name='edit'),
]
