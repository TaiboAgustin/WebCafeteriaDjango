from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #enviamos el correo y redireccionamos
            email = EmailMessage(
                'La Caffetiera, nuevo Email',
                'De {} <{}>\n\Escribió:\n\n{}'.format(name, email, content),
                'no-contestar@inbox.mailtrap.io',
                ['agusstaibo23@hotmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                print(email)
                #redireccionamos a ok, se mandó el mail correctamente
                return redirect(reverse('contact')+'?ok')
            except:
                #Algo falló, redireccionamos a FAIL
                return redirect(reverse('contact')+'?fail')

            


    return render(request, 'contact/contact.html', {'form': contact_form})
