from django.db import models
from ckeditor.fields import RichTextField
from .validators import validate_number
# Create your models here.
class Portfolio1(models.Model):
    is_active = models.BooleanField(default=True, unique=True, null=True)
    name = models.CharField(max_length=100)
    animated_desc = models.CharField(max_length=100)
    button_name = models.CharField(max_length=100)

    sec1_heading = models.CharField(max_length=100)
    Icon_choice = (
        ('laptop', "laptop"),
        ('link', "link"),
        ('paper-plane', "paper-plane"),
    )

    sec1_inner1_icon = models.CharField(max_length=15, choices=Icon_choice)
    sec1_inner1_title = models.CharField(max_length=100)
    sec1_inner1_desc = RichTextField()

    sec1_inner2_icon = models.CharField(max_length=11, choices=Icon_choice)
    sec1_inner2_title = models.CharField(max_length=100)
    sec1_inner2_desc = RichTextField()

    sec1_inner3_icon = models.CharField(max_length=11, choices=Icon_choice)
    sec1_inner3_title = models.CharField(max_length=100)
    sec1_inner3_desc = RichTextField()



    sec2_heading = models.CharField(max_length=100)
    sec2_title = models.CharField(max_length=100)
    sec2_desc = RichTextField()



    sec3_heading = models.CharField(max_length=100)

    sec4_heading = models.CharField(max_length=100)
    sec4_ph_num = models.IntegerField()
    sec4_email = models.EmailField()
    sec4_address = models.CharField(max_length=100)
    sec4_button = models.CharField(max_length=100)

    sec5_fb = models.CharField(max_length=100)
    sec5_ld = models.CharField(max_length=100)
    sec5_gh = models.CharField(max_length=100)
    sec5_ig = models.CharField(max_length=100)

    def __str__(self):
        return "Data is for one time - {}".format(self.name)

class Portfolio2(models.Model):
    sec2_inner_title = models.CharField(max_length=100)
    sec2_inner_percentage = models.IntegerField()


    sec3_inner_image = models.ImageField(upload_to="Images/")
    sec3_inner_title = models.CharField(max_length=100)
    

    def __str__(self):
        return "Data for showing dynamic topic - {}".format(self.sec2_inner_title)


class ContactInfo(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField()
    phone=  models.CharField(max_length=10, validators=[validate_number])
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name