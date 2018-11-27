from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.
def servicios(request):
    contact_form=ContactForm()
    if request.method=="POST":
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            content=request.POST.get('content','')
            #enviamos el correo y redireccionamos
            email=EmailMessage(
            'Circulo de Investigacion en Meteorologia y Climatologia',
            'De {} <{}>\n\nEscribió:\n\n{}'.format(name,email,content),
            'no-contestar@inbox.mailtrap.io',
            ["20121061@lamolina.edu.pe"],
            reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('servicios')+'?ok')
            except:
                return redirect(reverse('servicios')+'?fail')


            ####ss#
    return render(request,"servicios/servicios.html",{"form":contact_form})
