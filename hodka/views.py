from django.shortcuts import render
from hodka.models import slider, extraData, CEO, Satisfaction, Product, contactUs
from django.contrib import messages
from captcha.fields import CaptchaField

# Create your views here.
def HomePage(request):
    if request.method == "POST":
        form = ContactForm2(request.POST)
        print(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'اطلاعات شما با موفقیت دریافت شد')
            form.save()
        else:
            messages.add_message(request, messages.ERROR, 'متاسفانه اطلاعات شما دریافت نشد')
    form = ContactForm2()
    sliders = slider.objects.filter(active=True)
    exdata = extraData.objects.filter(active=True).first()
    ceo = CEO.objects.all()
    statisfaction = Satisfaction.objects.all()
    product = Product.objects.filter(active=True)
    return render(request, 'index.html', context={
        'sliders': sliders,
        "exdata":exdata,
        "ceo": ceo,
        "statisfaction":statisfaction,
        "product":product,
        'form':form
    })


from django import forms
class ContactForm2(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = contactUs
        fields = ['name', 'email', 'message'] 
        