from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main/', views.main),
    path('month/', views.month, name='month'),
    path('atm/', views.atm, name='ATM'),
    path('graph/', views.graph, name='graph'),
    path('list/', views.list, name='list'),
    path('done/', views.done),
    path('transaction/', views.transaction, name='transaction'),
    path('pin_check/',views.pin_check,name='pin_check'),
    path('change/', views.change),
    path('delete_client/<int:client_id>/', views.delete_client, name='delete_client'),
    path('deposit/<int:client_id>/', views.deposit, name='deposit'),
    path('credit/<int:client_id>/', views.credit, name='credit'),
    path('ostatok_scheta/<int:client_id>/', views.ostatok_scheta, name='ostatok_scheta'),
    path('snyatie/<int:client_id>/', views.snyatie, name='snyatie'),
    path('pechat/', views.pechat, name='pechat'),
    path('popolnenie/<int:client_id>/', views.popolnenie, name='popolnenie'),
    path('deposit_client/',views.deposit_client,name='deposit_client'),
    path('credit_client/', views.credit_client, name='credit_client'),
    path('client_detail/<int:client_id>/', views.client_detail, name='client_detail'),

    # path('client_detail/<int:client_id>/deposit_otozvat/', views.backDeposit, name='back_Deposit'),
    path('deposit_client/deposit_otozvat/', views.backDeposit, name='back_Deposit'),
    path('client_detail/11/deposit_otozvat/', views.backDeposit, name='back_Deposit'),
]
