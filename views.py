from django.shortcuts import render,redirect
from movieapp.models import *
import os

from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def foot(request):
	return render(request,'footer.html')
def editpro(request):
	user=UserRegister.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.username=request.POST.get('nm')
		user.password=request.POST.get('pw')
		user.last_name=request.POST.get('ad')
		user.gender=request.POST.get('c')
		user.first_name=request.POST.get('pi')
		
		
		user.DOB=request.POST.get('db')
		user.save()
		return redirect('/myprofile')
	else:
		return render(request,'editpro.html',{'user':user})

	


def myprofile(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	user=UserRegister.objects.get(email=request.session['email'])
	return render(request,'myprofile.html',{'user':user})

def logout(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	del request.session['email']
	return redirect('/login')



def login(request):
	if request.method=="POST":
		e=request.POST.get('em')
		p=request.POST.get('pw')
		data=UserRegister.objects.filter(email=e,password=p)
		k=len(data)
		if k>0:
			request.session['email']=e
			return redirect('/myprofile')
		else:
			return render(request,'login.html',{'msg':"invalid candidate"})
	else:
		return render(request,'login.html')
def PASS(request): 
	return render(request,'PASS.html')
def REGG(request):
	if request.method=="POST":
		em=request.POST.get('em')

		if UserRegister.objects.filter(email=em).exists():
			return render(request,'REGG.html',{'msg' :"Email Id is Already exists"})
		else:
		    x=UserRegister()
		    x.name=request.POST.get('nm')
		    x.email=request.POST.get('em')
		    x.message=request.POST.get('msg')
		    x.first_name=request.POST.get('nmf')
		    x.DOB=request.POST.get('db')
		    x.last_name=request.POST.get('nml')
		    x.password=request.POST.get('pw')
		    x.phone_number=request.POST.get('pnn')
		    x.gender=request.POST.get('gn')
		    if 'img' in request.FILES:
		    	x.Photo=request.FILES['img']
		    x.save()
		    return render(request,'REGG.html',{'msg':'user successfully added'})
	else:
		 return render(request,'REGG.html')



def header(request):
	return render(request,'header.html')

def contact(request):
	if request.method=="POST":
		
		x.name=request.POST.get('nm')
		x.email=request.POST.get('em')
		x.message=request.POST.get('msg')
		x.save()
		return render(request,'contact.html',{'su' :"Data succ Added"})
	else:
		return render(request,'contact.html')
def sidebar(request):
	return render(request,'sidebar.html')
def changepassword(request):
	if request.method=="POST":
		user=UserRegister.objects.get(email=request.session['email'])
		o=request.POST.get('opw')
		n=request.POST.get('npw')
		r=request.POST.get('rpw')
		if n==r:
			p=user.password
			if p==o:
				user.password=n
				user.save()
				return render(request,'changepassword.html',{'msg':"password succ changed"})
			else:
				return render(request,'changepassword.html',{'msg':"Invalid current password"})
		else:
			return render(request, 'changepassword.html',{'msg':'password and c-password does not match'})
	else:
		return render(request,'changepassword.html')


def forgetpass(request):
	if (request.method=='POST'):
		email=request.POST.get('em')
		user=UserRegister.objects.filter(email=email)
		if(len(user)>0):
			pw=user[0].password
			subject="Password"
			message="Welcome! your Password is" +pw
			email_from=settings.EMAIL_HOST_USER
			recipient_list=[email,]
			print(subject,message,email_from,recipient_list)
			send_mail(subject,message,email_from,recipient_list)
			res="your password send to your respective email account"
			return render(request,'forgetpass.html',{'msg':res})
		else:
			rest='This Email Id is not registered'
			return render(request,'forgetpass.html',{'msg':rest})
	else:
		return render(request,'forgetpass.html')

def allmovies(request):
	
	if request.method=='POST':
		sel=request.POST.get('sel')
		lag=Language.objects.all()
		res=Movie.objects.filter(Language=sel)
		return render(request,'allmovies.html',{'data':res, 'Language':lag})
	else:
		lag=Language.objects.all()
		res=Movie.objects.all()
		return render(request,'allmovies.html',{'data':res, 'Language':lag})
def allmovies1(request):
	res=Movie.objects.all()

	return render(request,'allmovies1.html',{'data':res})
def moviedetail(request, id):
	x=Movie.objects.get(id=id)
	if request.method=="POST":
		m_name=request.POST.get('movie_name')
		m_id=request.POST.get('movie_id')
		m_date=request.POST.get('date')
		m_time=request.POST.get('time')
		request.session['movie_name']=m_name
		'''mo=seats.objects.filter(Movie_name=request.session['movie_name'])
		all_booked_seats=""
		for i in mo:
			all_booked_seats+=Seats_number'''
		return render(request,'seats.html',{'m_name' : m_name,'m_id' :m_id,'m_date':m_date,'m_time':m_time })
	else:
		return render(request,'moviedetail.html',{'i':x})

import random
def boo_seats(request):
	user=UserRegister.objects.get(email=request.session['email'])
	'''mo=seats.objects.filter(movie_name=request.session['movie_name'])
	all_booked_seats=""
	for i in mo:
		all_booked_seats+=Seats_number'''
	if request.method=="POST":
		o=str(random.randrange(100000,999999))
		x=seats()
		print(user.username)
		x.User_name=user.username
		x.User_Email=user.email
		x.User_id=user.id
		x.movie_name=request.POST.get('moviename')
		x.movie_id=request.POST.get('movieid')
		x.movie_date=request.POST.get('moviedate')
		x.movie_time=request.POST.get('movietime')
		x.total_number_of_seats=request.POST.get('count')
		x.seat_numbers=request.POST.get('seats')
		x.otp=o
		subject="otp"
		message="Welcome! your otp is" +o
		email_from=settings.EMAIL_HOST_USER
		recipient_list=[user.email,]
		send_mail(subject,message,email_from,recipient_list)
		res="your password send to your respective email account"
		x.save()
		return render(request,'enter_otp.html',{'org_otp':o,'res':res,'seats_count':x.total_number_of_seats})
	else:
		print("else part")
		return render(request,'seats.html',{})


def index(request):
	return render(request,'index.html')

def enter_otp(request):
	if request.method=="POST":
		org_otp=request.POST.get('org_otp')
		enter_otp=request.POST.get('enter_otp')
		seat_count=request.POST.get('seat_count')
		print(seat_count)
		if org_otp==enter_otp:
			import qrcode
			import io 
			upi_id='flash543210@ibl'
			#aa=int(seat_count)
			amount=int(seat_count)*250
			print(amount)
			Your_Name='JAISLEEN KAUR'
			upi_url=f'upi://pay?pa={upi_id}&pn={Your_Name}&am={amount}&cu=INR'
			qr=qrcode.make(upi_url)
			buffer=io.BytesIO()
			qr_file_path=os.path.join('statics','images','new_upi.png')
			

			
			os.makedirs(os.path.dirname(qr_file_path), exist_ok=True)
			qr.save(qr_file_path)
			return render(request,'payment.html',{'name':Your_Name,'upi_id':upi_id,'qr_file_path':qr_file_path})
		else:
			return render(request,'enter_otp.html',{'msg':"Incorrect OTP"})
	else:
		return render(request,'enter_otp.html',{})
		
def payment(request):
	return render(request,'payment.html')
def trailer(request):
		return render(request,'trailer.html')
def booked(request):
	return render(request,'booked.html')
def bookeddetails(request):
	user=UserRegister.objects.get(email=request.session['email'])
	em=user.email
	data=seats.objects.filter(User_Email=em)
	return render(request,'bookeddetails.html',{'data':data})







