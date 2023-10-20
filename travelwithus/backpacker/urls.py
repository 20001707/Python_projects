from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.user_signup,name='signup'),
    path('login/',views.login_page,name='login'),
    path('agent_signup/',views.agent_signup,name='agent_signup'),
    path('logout/',views.logoutUser,name='logout'),
    path('package/',views.package,name='package'),
    path('agent_packages',views.agent_packages,name='agent_packages'),
    path('create/',views.create_package,name='create'),
    path('package-det/<str:pk>/',views.package_details,name='package-det'),
    path('booking_success/',views.booking_success,name='booking_success'),
    path('bookinglist/',views.bookinglist,name='bookinglist'),
    path('bookinglist_agent/',views.bookinglist_agent,name='bookinglist_agent'),
    path('package-edit/<str:pk>/',views.package_edit,name='package-edit'),
    path('bookind-del/<str:pk>/',views.cancel_booking,name='booking-del'),
    path('package-status/<str:pk>/',views.package_status,name='package-status'),
    path('package-detail/<str:uname>/',views.user_detail,name='user-detail'),
    path('package-detail/<str:uname>/',views.Agentdetails,name='Agentdetails'),
   
   
]