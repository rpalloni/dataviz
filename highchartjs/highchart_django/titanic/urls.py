
from django.contrib import admin
from django.urls import path

from passengers import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ticket-class/', views.ticket_class_view, name='ticket-class'),
    path('ticket-class/2/', views.ticket_class_view_2, name='ticket-class-2'),
    path('ticket-class/3/', views.ticket_class_view_3, name='ticket-class-3'),
    path('json-example/', views.json_example, name='json-example'),
    path('json-example/data/', views.chart_data, name='chart-data'),
    path('admin/', admin.site.urls),
]
