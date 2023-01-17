from django.db import models

City_CHOICE =(
    ("Purnea","Purnea"),
    ("jalandher","jalandher"),
    ("Patna","Patna"),
)
class Student(models.Model):
    name=models.CharField(max_length=150)
    father_name=models.CharField(max_length=150)
    mother_name=models.CharField(max_length=150)
    user_name=models.CharField(max_length=150)
    city=models.CharField(max_length=150,choices=City_CHOICE)
    contect=models.CharField(max_length=150)
    image=models.ImageField(upload_to="photo/",null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    