from django.shortcuts import render
from django.shortcuts import render
# from .models import ContactMessage


def contact_us(request):
    # sent = False

    # if request.method == 'POST':
    #     username = request.POST.get('username', '').strip()
    #     email = request.POST.get('email', '').strip()
    #     message = request.POST.get('message', '').strip()
    #
    #     if username and email and message:
    #         ContactMessage.objects.create(username=username, email=email, message=message)
    #         sent = True

    return render(request, 'page/contact_us.html',context={})


# Create your views here.
