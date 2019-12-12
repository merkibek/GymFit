from django.contrib import admin
from django.urls import path, include
from parts import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Gym Administration Tool"
admin.site.site_title = "GymSystem"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('class.html', views.classes, name='classes'),
    path('contact.html', views.contact, name='contact'),
    path('trainers.html', views.trainers, name='trainers'),
    path('join_class/', views.join_class),
    path('join_us/', views.join_us),
    path('contact_us/', views.contact_us),
    path('api/', include('parts.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

