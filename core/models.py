from django.db import models
import datetime
from .validators import validate_logo, validate_year_of_formation

class Social_Media_btn(models.Model):
    name = models.CharField(max_length=20)
    link = models.URLField()
    icon = models.FileField(upload_to='static/core/images/socialMediaIcons', validators=[validate_logo])
    def __str__(self):
        return f"{self.name}"

class Formation(models.Model):
    institute = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    start_year = models.IntegerField(validators=[validate_year_of_formation])
    end_year = models.IntegerField(validators=[validate_year_of_formation])
    logo = models.FileField(upload_to='static/core/images', validators=[validate_logo])
    def __str__(self):
        return f"{self.institute} - {self.course}"

class Certificate(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='static/core/images')
    def __str__(self):
        return f"{self.title}"

class Bio_Picture(models.Model):
    picture = models.ImageField(upload_to='static/core/images')
    alt = models.CharField(max_length=100, default='Foto')
    def __str__(self):
        return f"{self.alt}"

class Main_Picture(models.Model):
    picture = models.ImageField(upload_to='static/core/images')
    alt = models.CharField(max_length=100, default='Foto de Leonardo Costa')
    def __str__(self):
        return "Foto Principal"

