import datetime
import os

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse
from django.utils import timezone

from .forms import EmailerForm
import threading

from .models import Email


def index(request):
    if request.method == 'POST':
        form = EmailerForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = os.environ.get('Email_user')
            to_whom = form.cleaned_data['to_whom']
            seconds_ = form.cleaned_data['seconds']

            recipients = []
            if to_whom:
                recipients.append(to_whom)

            # t = threading.Timer(seconds, function=send_mail, args=(subject, message, sender, recipients))

            now = timezone.now()
            then = now + timezone.timedelta(seconds=seconds_)

            Email.objects.create(datetime_created=now,
                                 subject=subject,
                                 message=message,
                                 # seconds=then,
                                 # seconds=now + timezone.timedelta(seconds=seconds),
                                 to_whom=to_whom
                                 )

            # t.start()
            return HttpResponseRedirect(reverse('Emailer:detail'))
    else:
        form = EmailerForm()

    return render(request, 'index.html', {'form': form})


def detail_page(request):
    last_ten = Email.objects.all().order_by('-id')[:10]

    must_be_sent = Email.objects.all().filter(seconds__gt=timezone.now()).order_by('-id')

    already_sent = Email.objects.all().filter(seconds__lt=timezone.now()).order_by('-id')

    context = {'last_ten': last_ten, 'must_be_sent': must_be_sent, 'already_sent': already_sent}

    return render(request, 'detail.html', context)


# git add .
# git commit -m "initial commit"
# git push heroku master
# heroku open
#
