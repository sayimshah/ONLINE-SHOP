from django.urls import path
from ecomapp import views


urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.handlelogin,name='handlelogin'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logouts,name='logouts'),
    path('about', views.about, name="AboutUs"),
    path('contactus',views.contactus,name='contactus'),
    path('tracker', views.tracker, name="TrackingStatus"),
    path('products/<int:myid>', views.productView, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),
    path('activate/<uidb64>/<token>',  views.ActivateAccountview.as_view(), name = "activate" ),
    path('request-reset-email/',  views.RequestResetEmailView.as_view(), name = "request-reset-email" ),
    path('set-new-password/<uidb64>/<token>',  views.SetNewPasswordView.as_view(), name = "set-new-password" ),




]