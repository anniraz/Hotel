import datetime
from django.db import models
from apps.rooms.models import Rooms
from django.core.exceptions import ValidationError


class HotelBooking(models.Model):

    CHOICE=(
        (0,0),
        (1,1),
        (2,2),
        (3,3),
        (4,4),
    )
    full_name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(blank=True ,null=True)
    check_in=models.DateField()
    check_out=models.DateField()
    adults=models.IntegerField(choices=CHOICE)
    children=models.IntegerField(choices=CHOICE,default=0)
    room=models.ForeignKey(Rooms,on_delete=models.CASCADE)



    def __str__(self):
        return f'id:{self.id} room:{self.room} check_in :{self.check_in}: {self.check_out} '


    class Meta:
        unique_together = ('check_in', 'check_out','room',)


    def validate_unique(self, exclude=None):
     
        for i in HotelBooking.objects.all():
            dates=i.check_out-i.check_in
            room=i.room

            for d in range(dates.days +1):
                res=i.check_in+datetime.timedelta(days=d)
                if self.check_in ==res and self.room==room :
                    raise ValidationError("I'm sorry but you can't book this room these days")

        super(HotelBooking, self).validate_unique(exclude=exclude)


    def save(self,*args,**kwargs):
        self.validate_unique()
        return super(HotelBooking,self).save(*args,**kwargs)









