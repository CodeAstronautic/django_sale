from  django.contrib.auth import views as v
from django.urls import path
from . import views 
# from .views import *

urlpatterns = [
    path('',views.index, name='index'),

    path('password-change/',v.PasswordChangeView.as_view(template_name='userprofile.html'),name='change_password'),
 
    path('password-change-done/', v.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done'),

    path('password-reset/', v.PasswordResetView.as_view(template_name='password_reset.html', email_template_name='password_reset_email.html',subject_template_name='password_reset_email_subject.txt'),name='password_reset'),
    path('password-reset-done/', v.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', v.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', v.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    
    path('signup_user/'  , views.signup_user , name='signup_user') ,
    path('login_user/'   , views.login_user  , name='loginuser')   ,
    path('logout_user/'  , views.logout_user , name='logout_user') ,
    path('addproduct/'   , views.addproduct  , name='addproduct')  ,
    path('allproduct/'   , views.allproduct  , name='allproduct')  ,
    path('productdetails/<int:id>'   , views.productdetails  , name='productdetails')  ,
    path('userprofile/'  , views.userprofile , name='userprofile') ,
    path('category/'     , views.category    , name='category')    ,
    path('addprice/<int:id>', views.addprice , name='addprice')    ,
    path('myproduct'     , views.myproduct   , name='myproduct')      ,
    path('pdel'          , views.pdel        , name='pdel')      ,
    # path('topten/'       , views.topten       , name='topten')      ,
     # path('aboutus/', views.aboutus , name= 'aboutus') , 
    #path('handlerequest/',views.handlerequest,name='handlerequest'),
    #path('order/',views.order,name='order'),


    
         
]