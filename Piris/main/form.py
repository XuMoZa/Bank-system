from django import forms


class City_Residence(forms.Form):
    City_choises = [
        ('Minsk','Минск'),
        ('Vitebsk','Витебск'),
        ('Grodno', 'Гродно'),
        ('Mogilev','Могилёв'),
        ('Brest','Брест'),
        ('Gomel','Гомель'),
    ]
    city_of_residence = forms.CharField(widget=forms.Select(choices=City_choises))

class City_Living(forms.Form):
    City_choises = [
        ('Minsk', 'Минск'),
        ('Vitebsk', 'Витебск'),
        ('Grodno', 'Гродно'),
        ('Mogilev', 'Могилёв'),
        ('Brest', 'Брест'),
        ('Gomel', 'Гомель'),
    ]
    city_of_living = forms.CharField(widget=forms.Select(choices=City_choises))

class Relationship(forms.Form):
    Choises = [
        ('Free','Свободен/а'),
        ('almoust','Помолвлен/а'),
        ('married','Женат/а'),
        ('exmarried','Разведен/а'),
    ]
    relation = forms.CharField(widget=forms.Select(choices=Choises))

class Citizenship(forms.Form):
    Choises = [
        ('Belarus','Беларусь'),
        ('Russia','Россия'),
        ('Ukrain','Украина')
    ]
    citizen = forms.CharField(widget=forms.Select(choices=Choises))

class Handicap(forms.Form):
    Choises = [
        ('No','Нет'),
        ('First','Первая'),
        ('Second','Вторая'),
        ('Third','Третья'),
    ]
    handicap = forms.CharField(widget=forms.Select(choices=Choises))

class Deposit_type(forms.Form):
    Choises = [
        ('Otziv','Отзывной'),
        ('NeOtziv','Безотзывной')
    ]
    deposit_type = forms.CharField(widget=forms.Select(choices=Choises))
class Credit_type(forms.Form):
    Choises = [
        ('Annuitet','Аннуитетный'),
        ('Konec','С оплатой в конце')
    ]
    credit_type = forms.CharField(widget=forms.Select(choices=Choises))
class Sum(forms.Form):
    sum = forms.CharField(max_length=6, required=True)
class Valut(forms.Form):
    Choices = [
        ('Rub','Рубли'),
        ('Dollars','Доллары'),
        ('Euro','Евро')
    ]
    valut = forms.CharField(widget=forms.Select(choices=Choices))