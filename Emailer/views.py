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
            seconds = form.cleaned_data['seconds']
            to_whom = form.cleaned_data['to_whom']

            sender = os.environ.get('Email_user')

            recipients = []
            if to_whom:
                recipients.append(to_whom)

            t = threading.Timer(float(seconds), function=send_mail, args=(subject, message, sender, recipients))

            Email.objects.create(subject=subject,
                                 message=message,
                                 seconds=seconds,
                                 to_whom=to_whom
                                 )

            t.start()
            return HttpResponseRedirect(reverse('Emailer:detail'))
    else:
        form = EmailerForm()

    return render(request, 'index.html', {'form': form})


def detail_page(request):
    last_ten = Email.objects.all().order_by('-id')[:10]

    must_be_sent = Email.objects.all().filter(datetime_must_be_send__gt=timezone.now()).order_by('-id')

    already_sent = Email.objects.all().filter(datetime_must_be_send__lt=timezone.now()).order_by('-datetime_must_be_send')

    context = {'last_ten': last_ten, 'must_be_sent': must_be_sent, 'already_sent': already_sent}

    return render(request, 'detail.html', context)


# git add .
# git commit -m "initial commit"
# git push heroku master
# heroku open
#
