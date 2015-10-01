from django.db import models

# Create your models here.

class Join(models.Model):
    email = models.EmailField(unique=True)
    ip_address = models.CharField(max_length=120, default='ABC')
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __unicode__(self):
        return '%s' % (self.email)

#The guide on using south
#1) Install south: pip install south, add south to settings.py in INSTALLED_APPS
#2) Ensure Model is synced in the database
#3) Convert the model to south with: python manage.py convert_to_south appname
#4) Make changes to model (e.g. add new fields: ip_address = models.CharField(max_length=120, default='ABC') )
#5) Run schemamigration: python manage.py schemamigration appname --auto
#6) Run migrate: python manage.py migrate
#5
