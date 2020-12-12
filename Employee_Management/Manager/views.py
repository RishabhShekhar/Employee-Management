from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,CreateView
from Manager.forms import EmployeeForm,WorkForm
from Manager.models import Employee,Work
from django.http import HttpResponse
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here.

class AddEmployeeView(LoginRequiredMixin,CreateView):
    model=Employee
    form_class=EmployeeForm
    template_name='Manager/add_employee.html'

class AddManagerView(LoginRequiredMixin,CreateView):
    model=Employee
    form_class=EmployeeForm
    template_name='site_admin/add_employee.html'

class AddWorkView(LoginRequiredMixin,TemplateView):
    login_url='/login/'
    template_name='Manager/add_work.html'

    def get(self,request):
        form=WorkForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=WorkForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('work_list')

        return render(request,self.template_name,{'form':form})

class EmployeeListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    model=Employee

    def get_queryset(self):
        return Employee.objects.order_by('emid')

class ManagerListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    model=Employee

    def get_queryset(self):
        return Employee.objects.order_by('emid')

class WorkListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    model=Work

    def get_queryset(self):
        return Work.objects.order_by('jobid')

class EmployeeDetailView(LoginRequiredMixin,DetailView):
    login_url='/login/'
    model=Employee

class EmployeeUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name = 'Manager/employee_detail.html'
    form_class= EmployeeForm
    model=Employee

class WorkUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name = 'Manager/work_list.html'
    form_class= WorkForm
    model=Work

def siteadmin_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user= authenticate(username=username,password=password)

        if user:
            login(request,user)
            return render(request,"site_admin/dash.html")
        else:
            return HttpResponse("Invalid Login details")
    else:
        return render(request,"site_admin/login.html")

def index(request):
    return render(request,"index/index.html")

@login_required
def deletework(request,pk):
    a=Work.objects.get(pk=pk)
    a.delete()
    return redirect('work_list')

@login_required
def deleteemployee(request,pk):
    a=Employee.objects.get(pk=pk)
    a.delete()
    return redirect('employee_list')

@login_required
def home(request):
    countem= Employee.objects.all().count()
    countwo= Work.objects.all().count()
    context= {'countem': countem,'countwo': countwo}
    return render(request,"Manager/dash.html",context)

@login_required
def jobs(request):
    return render(request,"Manager/jobs-list.html")
