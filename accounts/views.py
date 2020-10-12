from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from datetime import date
from django.views.generic import TemplateView


@login_required(login_url='login')
def home(request):
	today=date.today()
	expenses=transaction.objects.filter(date__date=today).filter(user=request.user)
	monthly_expense=transaction.objects.filter(date__month=today.month).filter(user=request.user)
	total=0
	for i in monthly_expense :
		a=float(i.amount)
		total+=a
	user_count = user_info.objects.filter(username = request.user).count()
	if(user_count !=0):
		user1=user_info.objects.filter(username=request.user)
		budget="₹"+user1[0].monthly_budget+".0"
		income="₹"+user1[0].monthly_income+".0"
	else:
		budget="set your budget in profile"
		income="set your income in profile"



	return render(request,'accounts/dashboard.html',{'expenses':expenses,'total':total,'budget':budget,'income':income})

def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form=CreateUserForm()
		if request.method == 'POST':
			form=CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user=form.cleaned_data.get('username')
				messages.success(request,'Account was created for '+user)
				return redirect('login')

		context={'form':form}
		return render(request,'accounts/registration.html',context)
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username=request.POST.get('username')
			password=request.POST.get('password')

			user=authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('home')
			else:
				messages.info(request,'username or password is incorrect')
		context={}
		return render(request,'accounts/login.html',context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def addExpense(request):
	if(request.method=='POST'):
		user=request.user
		transaction_type=request.POST['transactionType']
		amount=request.POST['amount']
		expense=transaction(user=user,transaction_type=transaction_type,amount=amount)
		expense.save();
		return redirect('home')
	return render(request,'accounts/addExpense.html')

@login_required(login_url='login')
def expenseReport(request):
	expenses=transaction.objects.filter(user=request.user)

	return render(request,'accounts/ExpenseReport.html',{'expenses':expenses})

@login_required(login_url='login')
def profile(request):
	if request.method=="POST":
		data=user_info.objects.filter(username=request.user)
		data1=User.objects.filter(username=request.user)
		fname1=request.POST['fnamea']
		lname1=request.POST['lnamea']
		phone=request.POST['phone']
		monthly_income=request.POST['monthly_income']
		monthly_budget=request.POST['monthly_budget']
		username=request.user
		user_count = user_info.objects.filter(username = request.user).count()

		if(user_count==0):
			new_data=user_info(username=username,firstname=fname1,lastname=lname1,phone=phone,monthly_income=monthly_income,monthly_budget=monthly_budget)
			new_data.save()
		else:
			data.update(firstname=fname1,lastname=lname1,phone=phone,monthly_income=monthly_income,monthly_budget=monthly_budget)
			data1.update(first_name=fname1, last_name=lname1)
		messages.success(request, "Successfully Updated Profile!")
	data=User.objects.filter(username=request.user)
	params={'data':data}
	return render(request,'accounts/profile.html',params)


@login_required(login_url='login')
def viewProfile(request,slug):
	user1 = Userinfo.objects.filter(username=slug)
	params={'users':user1}
	return render(request, 'accounts/viewProfile.html',params)






    
# Create your views here.
