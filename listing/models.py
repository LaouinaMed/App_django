from django.db import models

# Create your models here.
class Placement(models.Model):
    title=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=500,null=True)
    image=models.CharField(max_length=500,null=True)
    type=models.CharField(max_length=300,null=True)
    details=models.CharField(max_length=500,null=True)
    maplocation=models.CharField(max_length=800,null=True)
    longtitude=models.FloatField()
    latitude=models.FloatField()
    ratings=models.FloatField()
    phone=models.CharField(max_length=50,null=True)
    """
    nature_of_it=(('1', 'Restaurant'),
                  ('2', 'Gas Station'),
                  ('3', 'Hotel'),
                  ('4', 'Shop'))
                  

    city=(('1', 'Rabat'),
          ('2', 'Casablanca'),
          ('3', 'Marrackech'),
          ('4', 'Tangier'))
          
    country=(('1', 'Morroco'),
             ('2', 'United States of America'),
             ('3', 'Spain'),
             ('4', 'France'))
    """
    Placement_Type=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=100,null=True)
    Country=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.title
       