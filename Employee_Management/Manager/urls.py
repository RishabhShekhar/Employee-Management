from django.urls import path,include
from Manager import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
    path('',views.index,name='index'),
    path('siteadmin_login/',views.siteadmin_login,name='siteadmin_login'),
    # path('manager_login/<int:flag>',LoginView.as_view(),name='login'),
    # path('employee_login/<int:flag>',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('dash/',views.home,name='dash'),
    # path('admin_dash/',views.admin_dash,name='admin_dash'),
    path('employees/',views.EmployeeListView.as_view(),name='employee_list'),
    path('employees_detail/<int:pk>',views.EmployeeDetailView.as_view(),name='employee_detail'),
    path('employee/<int:pk>/edit/',views.EmployeeUpdateView.as_view(),name="employee_edit"),
    path('employee/<int:pk>/remove/',views.deleteemployee,name="employee_remove"),
    path('work/<int:pk>/remove/',views.deletework,name="work_remove"),
    path('work/<int:pk>/edit/',views.WorkUpdateView.as_view(),name="work_edit"),
    path('work/',views.WorkListView.as_view(),name='work_list'),
    path('add_employee/',views.AddEmployeeView.as_view(),name='add_employee'),
    path('add_work/',views.AddWorkView.as_view(),name='add_work'),
]
