from django.db import models
from django.utils.timezone import now
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class transaction(models.Model):
	user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
	TYPES=(('Transport','Transport'),('Food','Food'),('Entertainment','Entertainment'),('Sports','Sports'))
	transaction_type=models.CharField(max_length=50,null=True,choices=TYPES)
	amount=models.CharField(max_length=20,null=True)
	today=date.today()
	date=models.DateTimeField(default=today)

class user_info(models.Model):
	username=models.CharField(max_length=30,null=True)
	firstname=models.CharField(max_length=30,null=True)
	lastname=models.CharField(max_length=30,null=True)
	email=models.CharField(max_length=30,null=True)
	phone=models.CharField(max_length=30,null=True)
	monthly_income=models.CharField(max_length=50,null=True)
	monthly_budget=models.CharField(max_length=50,null=True)













	
    
    
    
    
    
    
        



