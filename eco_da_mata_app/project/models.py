from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    desctiption = models.CharField(max_length=800)
    social_network_link = models.URLField(max_length=200)
    telephone_number = models.CharField(max_length=20) # perhaps we can use 'django-phonenumber-field' extension.
    email = models.EmailField(max_length=254)
    #community_key = models.ForeignKey("app.Model", on_delete=models.CASCADE) # has to be implemented after those models been created
    #event_key = models.ForeignKey("app.Model", on_delete=models.CASCADE) # has to be implemented after those models been created

    def __str__(self):
        return self.name + '\n' + self.desctiption
    
class Management(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    #people = models.ForeignKey("app.Model", on_delete=models.CASCADE) # has to be implemented after those models been created


    


class Review(models.Model):
    person_name = models.CharField(max_length=80);
    phrase = models.CharField(max_length=100);
    class Grade(models.IntegerChoices):
        pass
