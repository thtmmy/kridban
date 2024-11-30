from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.db.models.query_utils import Q
from .forms import UserRegistrationForm, UserLoginForm, SetPasswordForm, PasswordResetForm
from .decorators import user_not_authenticated
from .tokens import account_activation_token
from .models import *
from .forms import *
from django.http import HttpResponse
# Create your views here.
from typing import Protocol
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/index.html",
        context={"form": form}
        )

def about(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/about.html",
        context={"form": form}
        )

def bank(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/index.html",
        context={"form": form}
        )

def borrow(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/borrow.html",
        context={"form": form}
        )

def business_banking(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/business_banking.html",
        context={"form": form}
        )

@login_required (login_url = "index")
def buy_crypto(request):
    context = {}
    return render (request, "section/buy_crypto.html", context)


@login_required (login_url = "index")
def check_deposit(request):
    user = request.user

    check = Check.objects.filter(user=user)

    check = user.check_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.get('name')
        slip1 = request.FILES.get('slip1')
        slip2 = request.FILES.get('slip2')


        check, created = Check.objects.get_or_create(
            user=user,
            name=name,
            slip1=slip1,
            slip2=slip2
            )
        
        return redirect('user')

    context = {'check':check}  
    return render (request, "section/check_deposit.html", context)


@login_required (login_url = "index")
def card_deposit(request):

   if request.method == 'POST':
       account = request.POST['account']
       amount = request.POST['amount']
       cardtype = request.POST['cardtype']
       cardname = request.POST['cardname']
       cardnumber = request.POST['cardnumber']
       cardexp = request.POST['cardexp']
       cardcvv = request.POST['cardcvv']

       ctx = {
           'account' : account,
            'amount' : amount,
            'cardtype' : cardtype,
            'cardname' : cardname,
            'cardnumber' : cardnumber,
            'cardexp' : cardexp,
            'cardcvv' : cardcvv,
       }
       message = render_to_string('section/email4.html', ctx)
       send_mail('Contact Form',
        message,
        settings.EMAIL_HOST_USER,
        ['transparenthandsgroup@gmail.com'], 
        fail_silently=False, html_message=message)

       return redirect('user')

   return render(request, 'section/card_deposit.html')

def careers(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/career.html",
        context={"form": form}
        )

@login_required (login_url = "index")
def checkings_statement(request):
    user = request.user

    transfer = Transfer.objects.filter(user=user)

    context = {'transfer' :transfer}
    return render (request, "section/checkings_statement.html", context)

def credit_cards(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/credit_cards.html",
        context={"form": form}
        )

@login_required (login_url = "index")
def crypto_deposit(request):
    context = {}
    return render (request, "section/crypto_deposit.html", context)

def customer_support(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/customer_support.html",
        context={"form": form}
        )

def faqs(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/faqs.html",
        context={"form": form}
        )

def giving_back(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/giving_back.html",
        context={"form": form}
        )

def how_to_save_for_summer_vacation(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/how_to_save_for_summer_vacation.html",
        context={"form": form}
        )

def insure(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/insure.html",
        context={"form": form}
        )

def Internal_transfer(request):
    user = request.user

    transfer = user.transfer_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        type = request.POST.get('type')
        iban_accountnumber = request.POST.get('iban_accountnumber')
        amount = request.POST.get('amount')
        time = request.POST.get('time')
        transactionid = request.POST.get('transactionid')
        status = request.POST.get('status')
        account_type = request.POST.get('account_type')
        accountname = request.POST.get('accountname')
        bank_name = request.POST.get('bank_name')
        swift_code = request.POST.get('swift_code')
        bank_address = request.POST.get('bank_address')
        routing_transit_number = request.POST.get('routing_transit_number')
        purpose = request.POST.get('purpose')


        transfer, created = Transfer.objects.get_or_create(
            user=user,
            name=name,
            type=type,
            amount=amount,
            account_type=account_type,
            time=time,
            transactionid=transactionid,
            status=status,
            iban_accountnumber=iban_accountnumber,
            accountname=accountname,
            bank_name=bank_name,
            swift_code=swift_code,
            bank_address=bank_address,
            routing_transit_number=routing_transit_number,
            purpose=purpose
            )
        
        return redirect('pin')

    context = {'transfer':transfer}  
    return render (request, "section/Internal_transfer.html", context)

def invest(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/invest.html",
        context={"form": form}
        )

@login_required (login_url = "index")
def investment(request):
    context = {}
    return render (request, "section/investment.html", context)

def learn_and_plan(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/learn_and_plan.html",
        context={"form": form}
        )
@login_required (login_url = "index")
def loan_request(request):
    user = request.user

    loan = Loan.objects.filter(user=user)

    loan = user.loan_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        amount = request.POST.get('amount')
        occupation = request.POST.get('occupation')
        purpose = request.POST.get('purpose')
        time = request.POST.get('time')
        refrence = request.POST.get('refrence')
        status = request.POST.get('status')

        loan, created = Loan.objects.get_or_create(
            user=user,
            name=name,
            amount=amount,
            occupation=occupation,
            time=time,
            purpose=purpose,
            status=status,
            refrence=refrence
            )
        
        return redirect('user')

    context = {'loan':loan}  
    return render (request, "section/loan_request.html", context)

@login_required (login_url = "index")
def loan(request):
    context = {}
    return render (request, "section/loan.html", context)

@login_required (login_url = "index")
def processing(request):
    context = {}
    return render (request, "section/processing.html", context)

@login_required (login_url = "index")
def pin(request):
    context = {}
    return render (request, "section/pin.html", context)


@login_required (login_url = "index")
def local_transfer(request):
    user = request.user

    transfer = user.transfer_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        type = request.POST.get('type')
        iban_accountnumber = request.POST.get('iban_accountnumber')
        amount = request.POST.get('amount')
        time = request.POST.get('time')
        transactionid = request.POST.get('transactionid')
        status = request.POST.get('status')
        account_type = request.POST.get('account_type')
        accountname = request.POST.get('accountname')
        bank_name = request.POST.get('bank_name')
        swift_code = request.POST.get('swift_code')
        bank_address = request.POST.get('bank_address')
        routing_transit_number = request.POST.get('routing_transit_number')
        purpose = request.POST.get('purpose')


        transfer, created = Transfer.objects.get_or_create(
            user=user,
            name=name,
            type=type,
            amount=amount,
            account_type=account_type,
            time=time,
            transactionid=transactionid,
            status=status,
            iban_accountnumber=iban_accountnumber,
            accountname=accountname,
            bank_name=bank_name,
            swift_code=swift_code,
            bank_address=bank_address,
            routing_transit_number=routing_transit_number,
            purpose=purpose
            )
        
        return redirect('pin')

    context = {'transfer':transfer} 
    return render (request, "section/local_transfer.html", context)

def news(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/news.html",
        context={"form": form}
        )


def privacy_policy(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/privacy_policy.html",
        context={"form": form}
        )

@login_required (login_url = "index")
def profile(request):
    customer = request.user.customer
    form = CustomerForm (instance = customer)

    if request.method == 'POST':
        form = CustomerForm (request.POST, request.FILES, instance = customer)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "section/profile.html", context)


@user_not_authenticated
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.is_active=True
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('index')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="section/register.html",
        context={"form": form}
        )

def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index")

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('index')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('index')


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("section/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

def template_activate_account(request):
    context = {}
    return render (request, "section/template-activate-account.html", context)


def save(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/privacy_policy.html",
        context={"form": form}
        )


def savings_statement(request):
    user = request.user

    transfer = Transfer.objects.filter(user=user)

    context = {'transfer' :transfer}
    return render (request, "section/Savings_Statement.html", context)


def simple_ways_to_manage_a_checking_account(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/simple_ways_to_manage_a_checking_account.html",
        context={"form": form}
        )


@login_required (login_url = "index")
def viewSuccess(request, pk):
    transfer = Transfer.objects.get(id=pk)
    return render (request, "section/success.html", {'transfer': transfer})

@login_required (login_url = "index")
def notifications(request):
    context = {}
    return render (request, "section/notifications.html", context)

@login_required (login_url = "index")
def email3(request):
    context = {}
    return render (request, "section/email3.html", context)

@login_required (login_url = "index")
def email4(request):
    context = {}
    return render (request, "section/email4.html", context)

def support(request):

   if request.method == 'POST':
       dept = request.POST['dept']
       subject = request.POST['subject']
       message = request.POST['message']

       ctx = {
           'dept' : dept,
            'subject' : subject,
            'message' : message,
       }
       message = render_to_string('section/email3.html', ctx)
       send_mail('Contact Form',
        message,
        settings.EMAIL_HOST_USER,
        ['transparenthandsgroup@gmail.com'], 
        fail_silently=False, html_message=message)

       return redirect('user')

   return render(request, 'section/support.html')



def tax_checklist_5_things_to_remember(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/tax_checklist_5_things_to_remember.html",
        context={"form": form}
        )


def the_impact_of_rising_rates_and_inflation_on_your_business(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("user")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="section/the_impact_of_rising_rates_and_inflation_on_your_business.html",
        context={"form": form}
        )

@login_required (login_url = "index")
def user(request):
    context = {}
    return render (request, "section/user.html", context)

@login_required (login_url = "index")
def wire_transfer(request):
    user = request.user

    transfer = user.transfer_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        type = request.POST.get('type')
        iban_accountnumber = request.POST.get('iban_accountnumber')
        amount = request.POST.get('amount')
        time = request.POST.get('time')
        account_type = request.POST.get('account_type')
        transactionid = request.POST.get('transactionid')
        status = request.POST.get('status')
        accountname = request.POST.get('accountname')
        bank_name = request.POST.get('bank_name')
        swift_code = request.POST.get('swift_code')
        bank_address = request.POST.get('bank_address')
        routing_transit_number = request.POST.get('routing_transit_number')
        purpose = request.POST.get('purpose')


        transfer, created = Transfer.objects.get_or_create(
            user=user,
            name=name,
            type=type,
            amount=amount,
            time=time,
            account_type=account_type,
            transactionid=transactionid,
            status=status,
            iban_accountnumber=iban_accountnumber,
            accountname=accountname,
            bank_name=bank_name,
            swift_code=swift_code,
            bank_address=bank_address,
            routing_transit_number=routing_transit_number,
            purpose=purpose
            )
        
        return redirect('pin')

    context = {'transfer':transfer} 
    return render (request, "section/wire_transfer.html", context)