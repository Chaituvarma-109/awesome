from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def inbox_view(request):
    return render(request, 'a_inbox/inbox.html')
