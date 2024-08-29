import datetime
from django.shortcuts import render, get_object_or_404
from . import form
from .models import *
import random

now = datetime.date.today()
counter = 0


def main(request):
    cityresidence = form.City_Residence()
    cityliving = form.City_Living()
    relation = form.Relationship()
    handicap = form.Handicap()
    citizen = form.Citizenship()
    return render(request, 'main.html',
                  {'handicap': handicap, 'citizen': citizen, 'cityliving': cityliving, 'cityresidence': cityresidence,
                   'relation': relation})


def done(request):
    message = 'All Done'
    cityresidence = form.City_Residence()
    cityliving = form.City_Living()
    relation = form.Relationship()
    handicap = form.Handicap()
    citizen = form.Citizenship()
    name = request.POST.get("name")
    surname = request.POST.get("Surname")
    Second_name = request.POST.get("Second_name")
    if name.isalpha() and surname.isalpha() and Second_name.isalpha():
        pass
    else:
        message = 'name/surname/second name error'
        return render(request, 'main.html',
                      {'message': message, 'handicap': handicap, 'citizen': citizen, 'cityliving': cityliving,
                       'cityresidence': cityresidence,
                       'relation': relation})
    birthdate = request.POST.get("birthdate")
    seria = request.POST.get("seria")
    pass_num = request.POST.get("pass_num")
    seria_exists = Client.objects.filter(seria=seria).exists()
    pass_num_exists = Client.objects.filter(pass_num=pass_num).exists()
    if seria_exists and pass_num_exists:
        message = 'This passport is already exists'
        return render(request, 'main.html',
                      {'message': message, 'handicap': handicap, 'citizen': citizen, 'cityliving': cityliving,
                       'cityresidence': cityresidence,
                       'relation': relation})

    kem = request.POST.get("kem")
    date_vidachi = request.POST.get("date_vidachi")
    idnum = request.POST.get("idnum")
    idnum_exists = Client.objects.filter(idnum=idnum).exists()
    if idnum_exists:
        message = 'Passport id is already exists'
        return render(request, 'main.html',
                      {'message': message, 'handicap': handicap, 'citizen': citizen, 'cityliving': cityliving,
                       'cityresidence': cityresidence,
                       'relation': relation})
    birthplace = request.POST.get("birthplace")
    form_city_residence = form.City_Residence(request.POST)
    if form_city_residence.is_valid():
        city_of_residence = form_city_residence.cleaned_data['city_of_residence']
    adress_residence = request.POST.get("adress_residence")
    HomeNum = request.POST.get("HomeNum")
    mobnum = request.POST.get("mobnum")
    print(mobnum)
    if HomeNum != '':
        if not HomeNum[0:].isdigit():
            message = 'Home number should contain only digits'
            return render(request, 'main.html',
                          {'message': message, 'handicap': handicap, 'citizen': citizen, 'cityliving': cityliving,
                           'cityresidence': cityresidence,
                           'relation': relation})
    if mobnum != '':
        if not mobnum.startswith('+'):
            message = 'Number should start with +'
            return render(request, 'main.html',
                          {'message': message, 'handicap': handicap, 'citizen': citizen, 'cityliving': cityliving,
                           'cityresidence': cityresidence,
                           'relation': relation})
        if not mobnum[1:].isdigit():
            message = 'Number should contain only digits'
            return render(request, 'main.html',
                          {'message': message, 'handicap': handicap, 'citizen': citizen, 'cityliving': cityliving,
                           'cityresidence': cityresidence,
                           'relation': relation})
    email = request.POST.get("email")
    form_city_living = form.City_Living(request.POST)
    if form_city_living.is_valid():
        city_of_living = form_city_living.cleaned_data['city_of_living']
    adress_living = request.POST.get("adress_living")
    form_relation = form.Relationship(request.POST)
    if form_relation.is_valid():
        relation = form_relation.cleaned_data['relation']
    form_citizen = form.Citizenship(request.POST)
    if form_citizen.is_valid():
        citizen = form_citizen.cleaned_data['citizen']
    form_handicap = form.Handicap(request.POST)
    if form_handicap.is_valid():
        handicap = form_handicap.cleaned_data['handicap']
    senior_state = request.POST.get("senior")
    if senior_state == 'False':
        senior = 1
    else:
        senior = 0
    print(surname)
    client = Client.objects.create(name=name, surname=surname, second_name=Second_name, birthdate=birthdate,
                                   seria=seria, pass_num=pass_num, kem=kem, date_vidachi=date_vidachi, idnum=idnum,
                                   birthplace=birthplace, city_of_residence=city_of_residence,
                                   city_of_living=city_of_living, citizen=citizen, adress_residence=adress_residence,
                                   adress_living=adress_living, HomeNum=HomeNum, mobnum=mobnum, email=email,
                                   relation=relation, handicap=handicap, senior=senior)
    num = create_schet_number()
    name_s = name + ' ' + surname + ' ' + Second_name
    schet = Schet.objects.create(number=num, state='Active', cod=1000, debet=0, credit=0, saldo=0, name=name_s,
                                 ostatok = 0)
    num_c = random.randint(0, 9999999999999999)
    pin = random.randint(0, 9999)
    card = Card.objects.create(pin=pin, number=num_c, client=client, schet=schet)
    return render(request, 'main.html',
                  {'message': message, 'handicap': handicap, 'citizen': citizen, 'cityliving': cityliving,
                   'cityresidence': cityresidence, 'relation': relation})


def list(request):
    clients = Client.objects.order_by('surname')
    return render(request, 'list.html', {'clients': clients})


def client_detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    bd = (client.birthdate)
    date_vidachi = client.date_vidachi
    formres = form.City_Residence(initial={'city_of_residence': client.city_of_residence})
    formliv = form.City_Living(initial={'city_of_living': client.city_of_living})
    formhand = form.Handicap(initial={'handicap': client.handicap})
    formrel = form.Relationship(initial={'relation': client.relation})
    formcitizen = form.Citizenship(initial={'citizen': client.citizen})
    if client.senior == '1':
        senior_state = 'False'
    else:
        senior_state = 'None'
    return render(request, 'client_detail.html',
                  {'formres': formres, 'formliv': formliv, 'formhand': formhand, 'formrel': formrel,
                   'formcitizen': formcitizen, 'client': client, 'bd': str(bd), 'date_vidachi': str(date_vidachi),
                   'senior_state': senior_state})


def change(request):
    client = Client.objects.get(id=request.POST.get("id"))
    print(client.birthdate)
    bd = (client.birthdate)
    date_vidachi = client.date_vidachi
    formres = form.City_Residence(initial={'city_of_residence': client.city_of_residence})
    formliv = form.City_Living(initial={'city_of_living': client.city_of_living})
    formhand = form.Handicap(initial={'handicap': client.handicap})
    formrel = form.Relationship(initial={'relation': client.relation})
    formcitizen = form.Citizenship(initial={'citizen': client.citizen})
    client.name = request.POST.get("name")
    client.surname = request.POST.get("Surname")
    client.Second_name = request.POST.get("Second_name")
    client.birthdate = request.POST.get("birthdate")
    client.seria = request.POST.get("seria")
    client.pass_num = request.POST.get("pass_num")
    client.kem = request.POST.get("kem")
    client.date_vidachi = request.POST.get("date_vidachi")
    client.idnum = request.POST.get("idnum")
    client.birthplace = request.POST.get("birthplace")
    form_city_residence = form.City_Residence(request.POST)
    if form_city_residence.is_valid():
        client.city_of_residence = form_city_residence.cleaned_data['city_of_residence']
    client.adress_residence = request.POST.get("adress_residence")
    client.HomeNum = request.POST.get("HomeNum")
    client.mobnum = request.POST.get("mobnum")
    client.email = request.POST.get("email")
    form_city_living = form.City_Living(request.POST)
    if form_city_living.is_valid():
        client.city_of_living = form_city_living.cleaned_data['city_of_living']
    client.adress_living = request.POST.get("adress_living")
    form_relation = form.Relationship(request.POST)
    if form_relation.is_valid():
        client.relation = form_relation.cleaned_data['relation']
    form_citizen = form.Citizenship(request.POST)
    if form_citizen.is_valid():
        client.citizen = form_citizen.cleaned_data['citizen']
    form_handicap = form.Handicap(request.POST)
    if form_handicap.is_valid():
        client.handicap = form_handicap.cleaned_data['handicap']
    senior_state = request.POST.get("senior")
    print(senior_state)
    if senior_state == 'False':
        client.senior = 1
    else:
        client.senior = 0
    client.save()
    return render(request, 'main.html')


def delete_client(request, client_id):
    client = Client.objects.get(pk=client_id)
    credit = Credit.objects.get(client_id=client)
    if credit.is_open == 0:
        client.delete()
    return render(request, 'main.html')


def deposit(request, client_id):
    client = Client.objects.get(pk=client_id)
    formtype = form.Deposit_type()
    valut = form.Valut()
    return render(request, 'deposit.html', {'client': client, 'formtype': formtype, 'valut': valut})


def credit(request, client_id):
    client = Client.objects.get(pk=client_id)
    formtype = form.Credit_type()
    valut = form.Valut()
    return render(request, 'credit.html', {'client': client, 'formtype': formtype, 'valut': valut})


def deposit_client(request):
    client_id = request.POST.get('client_id')
    client = Client.objects.get(id=client_id)
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    second_name = request.POST.get('second_name')
    form_type = form.Deposit_type(request.POST)
    if form_type.is_valid():
        type = form_type.cleaned_data['deposit_type']
    number = request.POST.get('number')
    start_date = request.POST.get('start_date')
    finish_date = request.POST.get('finish_date')
    srok = request.POST.get('srok')
    sum = request.POST.get('sum')
    percent = request.POST.get('percent')
    form_valut = form.Valut(request.POST)
    if form_valut.is_valid():
        valut = form_valut.cleaned_data['valut']
    schet1_num = create_schet_number()
    cod1 = 2400
    debet = 0
    credit = 0
    saldo = 0
    name_s1 = surname + ' ' + name + ' ' + second_name
    cass = Schet.objects.get(cod=1010)
    cass.debet += int(sum)
    cass.credit += int(sum)
    state1 = 'Passive'
    schet1 = Schet.objects.create(number=schet1_num, state=state1, cod=cod1, debet=debet, credit=credit, saldo=saldo,
                                  name=name_s1, ostatok=0)
    schet2_num = create_schet_number()
    cod2 = 3014
    state2 = 'Active'
    schet2 = Schet.objects.create(number=schet2_num, state=state2, cod=cod2, debet=sum, credit=sum, saldo=saldo,
                                  name=name_s1, ostatok=0)
    date_to_compare = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    if (date_to_compare) > datetime.date.today():
        status = False
    else:
        status = True

    Deposit.objects.create(type=type, client=client, is_open=status, schetActive=schet2,
                                             schetPassive=schet1, open_time=start_date, close_time=finish_date,
                                             srok=srok, number=number, valute=valut, sum=sum, percent=percent)
    fond = Schet.objects.get(cod=7327)
    fond.credit += int(sum)
    cass.save()
    fond.save()
    bd = (client.birthdate)
    date_vidachi = client.date_vidachi
    formres = form.City_Residence(initial={'city_of_residence': client.city_of_residence})
    formliv = form.City_Living(initial={'city_of_living': client.city_of_living})
    formhand = form.Handicap(initial={'handicap': client.handicap})
    formrel = form.Relationship(initial={'relation': client.relation})
    formcitizen = form.Citizenship(initial={'citizen': client.citizen})
    if client.senior == '1':
        senior_state = 'False'
    else:
        senior_state = 'None'
    return render(request, 'client_detail.html',
                  {'formres': formres, 'formliv': formliv, 'formhand': formhand, 'formrel': formrel,
                   'formcitizen': formcitizen, 'client': client, 'bd': str(bd), 'date_vidachi': str(date_vidachi),
                   'senior_state': senior_state})


def credit_client(request):
    client_id = request.POST.get('client_id')
    client = Client.objects.get(id=client_id)
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    second_name = request.POST.get('second_name')
    form_type = form.Credit_type(request.POST)
    if form_type.is_valid():
        type = form_type.cleaned_data['credit_type']
    number = request.POST.get('number')
    start_date = request.POST.get('start_date')
    finish_date = request.POST.get('finish_date')
    srok = request.POST.get('srok')
    sum = request.POST.get('sum')
    percent = request.POST.get('percent')
    form_valut = form.Valut(request.POST)
    if form_valut.is_valid():
        valut = form_valut.cleaned_data['valut']
    schet1_num = create_schet_number()
    cod1 = 2401
    debet = 0
    credit = 0
    saldo = 0
    name_s1 = surname + ' ' + name + ' ' + second_name
    cass = Schet.objects.get(cod=1010)
    fond = Schet.objects.get(cod=7327)
    fond.debet += int(sum)
    state1 = 'CreditPassive'
    schet1 = Schet.objects.create(number=schet1_num, state=state1, cod=cod1, debet=debet, ostatok=0, credit=credit,
                                  saldo=saldo, name=name_s1)
    schet2_num = create_schet_number()
    cod2 = 3015
    state2 = 'CreditActive'
    if type == 'Annuitet':
        schet2 = Schet.objects.create(number=schet2_num, state=state2, cod=cod2, debet=sum, credit=sum, saldo=saldo,
                                      name=name_s1, ostatok=sum)
    else:
        schet2 = Schet.objects.create(number=schet2_num, state=state2, cod=cod2, debet=sum, credit=sum, saldo=saldo,
                                      name=name_s1, ostatok=0)
    cass.debet += int(sum)
    cass.credit += int(sum)
    date_to_compare = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    if (date_to_compare) > datetime.date.today():
        status = False
    else:
        status = True

    credit_client1 = Credit.objects.create(type=type, client=client, is_open=status, schetActive=schet2,
                                           schetPassive=schet1, open_time=start_date, close_time=finish_date, srok=srok,
                                           number=number, valute=valut, sum=sum, percent=percent)

    cass.save()
    fond.save()
    bd = (client.birthdate)
    date_vidachi = client.date_vidachi
    formres = form.City_Residence(initial={'city_of_residence': client.city_of_residence})
    formliv = form.City_Living(initial={'city_of_living': client.city_of_living})
    formhand = form.Handicap(initial={'handicap': client.handicap})
    formrel = form.Relationship(initial={'relation': client.relation})
    formcitizen = form.Citizenship(initial={'citizen': client.citizen})
    if client.senior == '1':
        senior_state = 'False'
    else:
        senior_state = 'None'
    return render(request, 'client_detail.html',
                  {'formres': formres, 'formliv': formliv, 'formhand': formhand, 'formrel': formrel,
                   'formcitizen': formcitizen, 'client': client, 'bd': str(bd), 'date_vidachi': str(date_vidachi),
                   'senior_state': senior_state})


def create_schet_number():
    rand_first = '3012'
    random_number = random.randint(10000000, 99999999)
    number_str = rand_first + str(random_number)

    random_number = int(number_str)


    odd_sum = 0
    even_sum = 0
    for i in range(len(number_str)):
        digit = int(number_str[i])
        if i % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    result = odd_sum * 3 + even_sum
    last_digit = result % 10
    if last_digit == 0:
        random_number *= 10
    else:
        random_number = random_number * 10 + (10 - last_digit)
    return random_number


def month(request):
    global now
    now = now.replace(month=now.month + 1)
    if now.month >= 12:
        now = now.replace(month=1)
        now = now.replace(year=now.year + 1)

    add_Deposit(now)
    add_Credit(now)
    cityresidence = form.City_Residence()
    cityliving = form.City_Living()
    relation = form.Relationship()
    handicap = form.Handicap()
    citizen = form.Citizenship()
    return render(request, 'main.html',
                  {'handicap': handicap, 'citizen': citizen, 'cityliving': cityliving,
                   'cityresidence': cityresidence,
                   'relation': relation})


def add_Deposit(now):
    deposits = Deposit.objects.all()
    fond = Schet.objects.get(cod=7327)
    cass = Schet.objects.get(cod=1010)
    print(now)
    for deposit in deposits:
        if (deposit.close_time) >= now and deposit.open_time < now:
            deposit.is_open = 1
        deposit.save()
    deposits = Deposit.objects.filter(is_open=1)
    for deposit in deposits:
        schetA = (deposit.schetActive)
        schetP = (deposit.schetPassive)
        fond.debet += deposit.sum * ((deposit.percent / 100) / 12)
        schetP.credit += deposit.sum * ((deposit.percent / 100) / 12)
        if deposit.close_time <= now or deposit.open_time >= now:
            deposit.is_open = 0
        if deposit.close_time <= now:
            fond.debet += deposit.sum
            schetA.credit += deposit.sum
            schetA.debet += deposit.sum
            cass.debet += deposit.sum
            cass.credit += deposit.sum
            schetP.debet += schetP.credit
            cass.credit += schetP.debet
            cass.debet += schetP.debet

        deposit.save()
        schetA.save()
        schetP.save()

    fond.save()
    cass.save()



def add_Credit(now):
    credits = Credit.objects.all()
    fond = Schet.objects.get(cod=7327)
    cass = Schet.objects.get(cod=1010)
    print(now)
    for credit in credits:
        if (credit.close_time) >= now and credit.open_time < now:
            credit.is_open = 1
        credit.save()
    credits = Credit.objects.filter(is_open=1)
    for credit in credits:
        schetA = (credit.schetActive)
        schetP = (credit.schetPassive)
        if credit.close_time <= now or credit.open_time >= now:
            credit.is_open = 0
        if credit.close_time >= now:
            if credit.type == 'Konec':
                percent = ((credit.percent / 100) / 12)
                new_passive_credit = credit.sum * percent
                schetP.credit += new_passive_credit
                fond.credit += new_passive_credit
                cass.debet += new_passive_credit
                cass.credit += new_passive_credit
                schetP.debet += new_passive_credit
            if credit.type == 'Annuitet':
                percent = ((credit.percent / 100) / 12)
                part_credit = credit.sum / (int(str(credit.close_time - credit.open_time).split()[0]) // 30)
                new_passive_credit = schetA.ostatok * percent + part_credit
                schetP.credit += schetA.ostatok * percent
                fond.credit += schetA.ostatok * percent
                cass.debet += new_passive_credit
                cass.credit += new_passive_credit
                schetP.debet += schetA.ostatok * percent
                fond.credit += part_credit
                schetA.credit += part_credit
                schetA.debet += part_credit
                schetA.ostatok -= part_credit
        if credit.is_open == 0:
            if credit.type == 'Konec':
                cass.debet += credit.sum
                cass.credit += credit.sum
                schetA.debet += credit.sum
                schetA.credit += credit.sum
                fond.credit += credit.sum
        credit.save()
        schetA.save()
        schetP.save()
    fond.save()
    cass.save()


def graph(request):
    global now
    strings = []
    credits = Credit.objects.all().order_by('open_time')

    # percent = ((credit.percent / 100) / 12)
    # part_credit = credit.sum / (int(str(credit.close_time - credit.open_time).split()[0]) // 30)
    # new_passive_credit = schetA.ostatok * percent + part_credit
    ostat = 0
    for credit in credits:
        time = credit.open_time
        if credit.type == 'Annuitet':
            ostat = credit.sum

        # if now.month >= 12:
        #     now = now.replace(month=1)
        #     now = now.replace(year=now.year + 1)

        time = time.replace(month=time.month + 1)
        while time <= credit.close_time:
            if time != credit.close_time:
                if credit.type == 'Konec':
                    percent = ((credit.percent / 100) / 12)
                    viplata = percent * credit.sum
                    string = str(
                        time) + ' - ' + credit.client.surname + ' ' + credit.client.name + ' ' + credit.client.second_name + ' выплатит ' + str(
                        viplata)
                    strings.append(string)
                if credit.type == 'Annuitet':
                    percent = ((credit.percent / 100) / 12)
                    part_credit = credit.sum / (int(str(credit.close_time - credit.open_time).split()[0]) // 30)
                    new_passive_credit = ostat * percent + part_credit
                    ostat -= part_credit
                    string = str(
                        time) + ' - ' + credit.client.surname + ' ' + credit.client.name + ' ' + credit.client.second_name + ' выплатит ' + str(
                        new_passive_credit)
                    strings.append(string)
            if time == credit.close_time:
                if credit.type == 'Annuitet':
                    percent = ((credit.percent / 100) / 12)
                    part_credit = credit.sum / (int(str(credit.close_time - credit.open_time).split()[0]) // 30)
                    new_passive_credit = ostat * percent + part_credit
                    ostat -= part_credit
                    string = str(
                        time) + ' - ' + credit.client.surname + ' ' + credit.client.name + ' ' + credit.client.second_name + ' выплатит ' + str(
                        new_passive_credit)
                    strings.append(string)
                if credit.type == 'Konec':
                    percent = ((credit.percent / 100) / 12)
                    viplata = percent * credit.sum + credit.sum
                    string = str(
                        time) + ' - ' + credit.client.surname + ' ' + credit.client.name + ' ' + credit.client.second_name + ' выплатит ' + str(
                        viplata)
                    strings.append(string)

            if time.month >= 12:
                time = time.replace(month=1)
                time = time.replace(year=now.year + 1)
            time = time.replace(month=time.month + 1)
            print(str(time))

    return render(request, 'graph.html', {'strings': strings})


def atm(request):
    global counter
    counter = 0
    return render(request, 'ATM.html', {'counter': counter})


def pin_check(request):
    global counter
    card_num = request.POST.get('card_num')
    pin = request.POST.get('PIN')
    cards = Card.objects.all()
    for card in cards:
        print(card.number, ' ', card_num, '+', card.pin, ' ', pin)

        if card.number == int(card_num) and card.pin == int(pin):
            cc = card.client
            m = 'Welcome!'
            counter = 0
            print(card.client.id)
            return render(request, 'pinchecked.html', {'client_id': card.client.id, 'mess': m, })
        else:
            message = 'Номер карты или пин введены неверно'
            counter += 1
            if counter == 3:
                cityresidence = form.City_Residence()
                cityliving = form.City_Living()
                relation = form.Relationship()
                handicap = form.Handicap()
                citizen = form.Citizenship()
                counter = 0
                return render(request, 'main.html',
                              {'handicap': handicap, 'citizen': citizen, 'cityliving': cityliving,
                               'cityresidence': cityresidence,
                               'relation': relation, 'message': message})
            else:
                return render(request, 'ATM.html', {'counter': counter, 'message': message})


def ostatok_scheta(request, client_id):
    card = Card.objects.get(client=client_id)
    sum = card.schet.saldo
    m = str(sum)
    flag = 1
    s = sum
    return render(request, 'pinchecked.html', {'client_id': client_id, 'mess': m, 'flag': flag, 'sum': sum})


def snyatie(request, client_id):
    f = form.Sum()
    m = 'Введите сумму снятия'
    value = 'snyatie'
    return render(request, 'pinchecked.html', {'client_id': client_id, 'mess': m, 'form': f, 'value': value})


def popolnenie(request, client_id):
    f = form.Sum()
    m = 'Введите сумму пополнения'
    value = 'popolnenie'
    return render(request, 'pinchecked.html', {'client_id': client_id, 'mess': m, 'form': f, 'value': value})


def transaction(request):
    f = form.Sum(request.POST)
    value = request.POST.get('value')
    client_id = request.POST.get('client_id')
    if f.is_valid():
        sum_value = f.cleaned_data['sum']
    sum = int(sum_value)
    if value == 'snyatie':
        if sum < 0:
            m = 'Сумма отрицательна, попробуйте положительную'
            f = form.Sum()
            value = 'snyatie'
            return render(request, 'pinchecked.html', {'client_id': client_id, 'mess': m, 'form': f, 'value': value})
        card = Card.objects.get(client=client_id)
        if sum > card.schet.saldo:
            m = 'Сумма больше остатка на счету'
            f = form.Sum()
            value = 'snyatie'
            return render(request, 'pinchecked.html', {'client_id': client_id, 'mess': m, 'form': f, 'value': value})
        if sum < card.schet.saldo and sum >= 0:
            card.schet.credit += sum
            flag = 3
            card.save()
            card.schet.save()
            m = 'Снятие выполнено'
            return render(request, 'pinchecked.html', {'client_id': client_id, 'mess': m, 'flag': flag, 'sum': sum})
    if value == 'popolnenie':
        if sum < 0:
            m = 'Сумма отрицательна, попробуйте положительную'
            f = form.Sum()
            value = 'popolnenie'
            return render(request, 'pinchecked.html', {'client_id': client_id, 'mess': m, 'form': f, 'value': value})
        card = Card.objects.get(client=client_id)
        if sum >= 0:
            card.schet.debet += sum
            flag = 2

            card.save()
            card.schet.save()
            m = 'Пополнение выполнено'
            return render(request, 'pinchecked.html', {'client_id': client_id, 'mess': m, 'flag': flag, 'sum': sum})


def pechat(request):
    m = 'Печать чека'
    now = datetime.datetime.now().strftime("%H:%M %d.%m.%Y ")
    client_id = request.POST.get('client_id1')
    flag = request.POST.get('flag')
    sum = request.POST.get('sum')
    if int(flag) == 1:
        m = str(now) + ' Сумма счета - ' + str(sum)
    if int(flag) == 2:
        m = str(now) + ' Пополнение счета на ' + str(sum)
    if int(flag) == 3:
        m = str(now) + ' нятие со счета ' + str(sum)
    return render(request, 'pinchecked.html', {'mess': m, 'client_id': client_id})


def backDeposit(request):
    print("Back deposit")
    print(request)


    deposits = Deposit.objects.all()
    fond = Schet.objects.get(cod=7327)
    cass = Schet.objects.get(cod=1010)
    print(now)


    for deposit in deposits:
        if (deposit.close_time) >= now and deposit.open_time < now:
            deposit.is_open = 1
        deposit.save()

    deposits = Deposit.objects.filter(is_open=1)

    otziv_deposit = []

    for deposit in deposits:
        if deposit.type == 'Otziv':
            otziv_deposit.append(deposit)

    for deposit in otziv_deposit:
        schetA = (deposit.schetActive)
        schetP = (deposit.schetPassive)
        fond.debet += deposit.sum * ((deposit.percent / 100) / 12)
        schetP.credit += deposit.sum * ((deposit.percent / 100) / 12)

        fond.debet += deposit.sum
        schetA.credit += deposit.sum
        schetA.debet += deposit.sum
        cass.debet += deposit.sum
        cass.credit += deposit.sum
        schetP.debet += schetP.credit
        cass.credit += schetP.debet
        cass.debet += schetP.debet

        deposit.save()
        schetA.save()
        schetP.save()

    fond.save()
    cass.save()

    cityresidence = form.City_Residence()
    cityliving = form.City_Living()
    relation = form.Relationship()
    handicap = form.Handicap()
    citizen = form.Citizenship()

    return render(request, 'main.html',
                  {'handicap': handicap, 'citizen': citizen, 'cityliving': cityliving,
                   'cityresidence': cityresidence,
                   'relation': relation})
