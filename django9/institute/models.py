from django.db import models
from multiselectfield import MultiSelectField

class courseform(models.Model):
    c_name = models.CharField(max_length=100)
    c_dur = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    c_trainer = models.CharField(max_length=100)
    exp = models.CharField(max_length=50)


class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=30)


class register(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    iname = models.CharField(max_length=100)
    location = models.CharField(max_length=100)



class feedback(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    date = models.DateTimeField()
    feedback = models.CharField(max_length=500)



class enquariform(models.Model):
    name=models.CharField(max_length=100)
    mobiles=models.BigIntegerField()
    email=models.EmailField(max_length=100)

    COURCES_CHOICE = (
        ('python', 'PYTHON'),
        ('django', 'DJANGO'),
        ('ui', 'UI'),
        ('flask', 'FLASK'),
        ('java', 'JAVA')

    )
    cources=MultiSelectField(choices=COURCES_CHOICE)

    TRAINER_CHOICE = (
        ('narayana', 'NARAYANA'),
        ('srinivas', 'SRINIVAS'),
        ('rubi', 'RUBI'),
        ('rachna', 'RACHNA'),
        ('mohit', 'MOHIT')

    )
    trainer = MultiSelectField(choices=TRAINER_CHOICE)

    SHIFT_CHOICE = (
        ('morning', 'MORNING'),
        ('evening', 'EVENING'),
        ('night', 'NIGHT')
    )
    shift = MultiSelectField(choices=SHIFT_CHOICE)

    LOCATION = (
        ('ameerpet', 'AMEERPET'),
        ('secundrabaad', 'SECANDRABAAD'),
        ('hyd', 'HYD'),
        ('begumpet', 'BEGUMPET')

    )
    location = MultiSelectField(choices=LOCATION)

    date=models.DateField()

    gender=models.CharField(max_length=100)

class entry(models.Model):
    fname=models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    salary=models.IntegerField()

    QUALIFICATION = (
            ('ba', 'BA'),
            ('be', 'BE'),
            ('bsc', 'BSC'),
            ('bcom', 'BCOM'),
            ('c-cat', 'C-CAT'),

        )
    qualification = MultiSelectField(choices=QUALIFICATION)

class Student(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    cname=models.CharField(max_length=20)
    sname=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    telugu=models.IntegerField()
    hindi=models.IntegerField()
    english=models.IntegerField()
    math=models.IntegerField()





