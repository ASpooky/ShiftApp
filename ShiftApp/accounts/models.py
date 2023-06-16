from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser,PermissionsMixin,BaseUserManager
)
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError(" Enter Email ")
        
        user=self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects=UserManager()

    class Meta:
        db_table="users"

class ShiftDaily(models.Model):
    choices=(("6:00~9:00","6:00~9:00"),
            ("9:00~14:00","9:00~14:00"),
            ("14:00~17:00","14:00~17:00"),
            ("17:00~22:00","17:00~22:00"),
            ("22:00~01:00","22:00~01:00"),
            ("01:00~","01:00~"))
    shift_time = models.CharField(max_length=100)
    
    date=models.DateField()

    user=models.ForeignKey(Users,on_delete=models.CASCADE)

    class Meta:
        db_table="ShiftDaily"

#class ShiftWeekly(models.Model):
#    user=models.ForeignKey(Users,on_delete=models.CASCADE)
#    start_date=models.DateField()
#    shift=models.Aggregate
#
#class WeeklyCalendar(models.Model):
    


