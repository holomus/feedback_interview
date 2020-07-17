import os

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.utils import timezone
from Feedback_project.settings import MANAGERS, MEDIA_ROOT
from feedback.forms import FeedbackForm
from feedback.models import Feedback


# Create your views here.

@login_required
def success(request):
    return render(request, "feedback/success.html")


@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        yesterday = timezone.now() - timezone.timedelta(minutes=1)
        if Feedback.objects.filter(user=request.user, creation_time__gt=yesterday).exists():
            raise PermissionDenied()
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            email = EmailMessage(
                subject=feedback.title,
                body=feedback.description,
                to=[a[1] for a in MANAGERS],
                reply_to=[feedback.user.email]
            )
            if request.FILES:
                path_to_file = os.path.join(MEDIA_ROOT, feedback.attachment.name)
                email.attach_file(path_to_file)
            email.send()
            return redirect('success')
        else:
            error = 'Incorrect form!!'

    else:
        form = FeedbackForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, "feedback/create.html", context)
