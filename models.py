from django.db import models




class FAQ(models.Model):
	qu=models.CharField(max_length=300)
	an=models.CharField(max_length=300)




	
class contactus(models.Model):
	name=models.CharField(max_length=300)
	email=models.EmailField()
	password=models.CharField(max_length=300)
	
class UserRegister(models.Model):
	username=models.CharField(max_length=300)
	email=models.EmailField()
	
	first_name=models.CharField(max_length=300)
	#pincode=models.CharField(max_length=300,blank=True,null=True)
#	course=models.CharField(max_length=300,blank=True,null=True)
#	address=models.CharField(max_length=300,blank=True,null=True)
#	age=models.CharField(max_length=300,blank=True,null=True)
#	gender=models.CharField(max_length=300,blank=True,null=True)

	
	last_name=models.CharField(max_length=300,blank=True,null=True)
	mothername=models.CharField(max_length=300,blank=True,null=True)
	fathername=models.CharField(max_length=300,blank=True,null=True)
	gender=models.CharField(max_length=300,blank=True,null=True)
	password=models.CharField(max_length=300,blank=True,null=True)
	
	DOB=models.CharField(max_length=300,blank=True,null=True)


class Language(models.Model):
	Language_name=models.CharField(max_length=1000,primary_key=True)
	Description=models.TextField()
	def __str__(self):
		return self.Language_name


class Movie_type(models.Model):
		Type_name=models.CharField(max_length=300,primary_key=True)
		Description=models.TextField()
		def __str__(self):
			return self.Type_name   
		       



class Certificate(models.Model):
		Certificate_name=models.CharField(max_length=300,primary_key=True)
		Description=models.TextField()
		def __str__(self):
			return self.Certificate_name   
		       
class Movie(models.Model):
		movie_name=models.CharField(max_length=300)
		Certificate=models.ForeignKey(Certificate,on_delete=models.CASCADE)
		Movie_type=models.ForeignKey(Movie_type,on_delete=models.CASCADE)
		Language=models.ForeignKey(Language,on_delete=models.CASCADE)
		Duration=models.CharField(max_length=300)
		Director=models.CharField(max_length=300)
		Casting=models.CharField(max_length=300)
		Trailer_Embed=models.TextField()
		Release_Date=models.CharField(max_length=300)
		Description=models.TextField()
		Photo=models.ImageField(upload_to="Data",blank=True,null=True)
		def __str__(self):
			return self.movie_name

class seats(models.Model):
	User_name=models.CharField(max_length=300)
	User_Email=models.CharField(max_length=300)
	user_id=models.CharField(max_length=300)
	movie_name=models.CharField(max_length=300)
	movie_id=models.CharField(max_length=300)
	movie_date=models.CharField(max_length=300)
	movie_time=models.CharField(max_length=300)
	total_number_of_seats=models.TextField()
	seat_numbers=models.CharField(max_length=300)
	otp=models.CharField(max_length=300)


		


	


