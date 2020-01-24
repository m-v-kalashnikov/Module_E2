import datetime
import os

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse

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
            seconds = form.cleaned_data['seconds']

            recipients = []
            if to_whom:
                recipients.append(to_whom)

            t = threading.Timer(float(seconds), function=send_mail, args=(subject, message, sender, recipients))

            now = datetime.datetime.now()

            Email.objects.create(datetime_created=now,
                                 subject=subject,
                                 message=message,
                                 seconds=now+datetime.timedelta(seconds=float(seconds)),
                                 to_whom=to_whom
                                 )

            t.start()
            return HttpResponseRedirect(reverse('Emailer:detail'))
    else:
        form = EmailerForm()

    return render(request, 'index.html', {'form': form})


def detail_page(request):
    email_queryset = Email.objects.all()

    last_ten = email_queryset.order_by('datetime_created')[9]

    must_be_sent = email_queryset.filter(seconds__gt=datetime.datetime.now())

    already_sent = email_queryset.filter(seconds__lt=datetime.datetime.now())

    context = {'last_ten': last_ten, 'must_be_sent': must_be_sent, 'already_sent': already_sent}

    return render(request, 'detail.html', context)
