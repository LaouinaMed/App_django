from django.db import models
from listing.models import Placement
from home.models import User
# Create your models here.
class Comment(models.Model):
    comment=models.CharField(max_length=500,null=True)
    user_id=models.IntegerField()
    rating=models.FloatField()
    date_comment=models.DateTimeField(auto_now_add=True,null=True)
    placement=models.ForeignKey(Placement,null=True,on_delete=models.CASCADE)
    user_commented = models.ForeignKey(User, null=True, on_delete=models.CASCADE)