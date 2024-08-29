from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    seria = models.CharField(max_length=8)
    pass_num = models.CharField(max_length=20)
    kem = models.CharField(max_length=255)
    date_vidachi = models.DateField()
    idnum = models.CharField(max_length=255)
    birthplace = models.CharField(max_length=255)
    city_of_residence = models.CharField(max_length=255)
    adress_residence = models.CharField(max_length=255)
    HomeNum = models.CharField(max_length=7)
    mobnum = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    city_of_living = models.CharField(max_length=255)
    adress_living = models.CharField(max_length=255)
    relation = models.CharField(max_length=255)
    citizen = models.CharField(max_length=255)
    handicap = models.CharField(max_length=255)
    senior = models.BooleanField()

    def __str__(self):
        return {self.name}


class Schet(models.Model):
    number = models.BigIntegerField()
    cod = models.IntegerField()
    state = models.CharField(max_length=255)
    debet = models.FloatField()
    credit = models.FloatField()
    saldo = models.FloatField()
    ostatok = models.FloatField()
    name = models.CharField(max_length=512)


class Credit(models.Model):
    type = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    schetActive = models.ForeignKey(Schet, on_delete=models.CASCADE, related_name='schetCA')
    schetPassive = models.ForeignKey(Schet, on_delete=models.CASCADE, related_name='schetCB')
    open_time = models.DateField()
    close_time = models.DateField()
    is_open = models.BooleanField(default=True)
    number = models.BigIntegerField()
    valute = models.CharField(max_length=255)
    srok = models.CharField(max_length=255)
    sum = models.FloatField()
    percent = models.FloatField()


class Card(models.Model):
    number = models.BigIntegerField()
    pin = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    schet = models.ForeignKey(Schet, on_delete=models.CASCADE, related_name='schet')


class Deposit(models.Model):
    type = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    schetActive = models.ForeignKey(Schet, on_delete=models.CASCADE, related_name='schetA')
    schetPassive = models.ForeignKey(Schet, on_delete=models.CASCADE, related_name='schetB')
    open_time = models.DateField()
    close_time = models.DateField()
    is_open = models.BooleanField(default=True)
    number = models.BigIntegerField()
    valute = models.CharField(max_length=255)
    srok = models.CharField(max_length=255)
    sum = models.FloatField()
    percent = models.FloatField()
