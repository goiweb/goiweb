
# Create your views here.
from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from goiapp.settings import EMAIL_HOST_USER
from  .models import Product,ContactUs
def home(request):
    products = Product.objects.all()
    for i in products:
        i.imageUrl = str(i.imageUrl).split("/")[5]
    contactInfo = ContactUs.objects.all()
    contactInfo = {"location": contactInfo[0].location, "email": contactInfo[0].email, "ph_num" : contactInfo[0].ph_number}
    params = {"contactInfo": contactInfo, "products" : products}
    return render(request, 'home/index.html', params)



def about(request):
    print("Request about")
    contactInfo = ContactUs.objects.all()
    contactInfo = {"location": contactInfo[0].location, "email": contactInfo[0].email, "ph_num" : contactInfo[0].ph_number}
    params = {"contactInfo": contactInfo}
    return render(request, 'home/about.html', params)


def contact1(request):
    contactInfo = ContactUs.objects.all()
    contactInfo = {"location": contactInfo[0].location, "email": contactInfo[0].email, "ph_num" : contactInfo[0].ph_number}
    params = {"contactInfo" : contactInfo}

    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        subject = request.POST.get('subject')
        company = request.POST.get('company')
        email = request.POST.get('email')
        message = request.POST.get('message')
        send_mail(
            subject,
            f'name : {name} \ncontact : {contact}\nrequest_type : contact request\ncompany : {company}\nmessage : {message}',
            EMAIL_HOST_USER,
            ['gehlothweb@gmail.com'],
            fail_silently=False,
        )
        send_mail(
            'Thanks for contacting us.',
            'Hello our team have received your request, we will get back to you as soon as possible.\n\nThank you\nGOI PVT. LTD.',
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )


    return render(request, 'home/contact1.html', params)



def contactId(request,id):
    print(id)
    product = Product.objects.get(pk=id).imageUrl
    title = Product.objects.get(pk=id).title
    product = str(product).split("/")[5]
    contactInfo = ContactUs.objects.all()
    contactInfo = {"location": contactInfo[0].location, "email": contactInfo[0].email,
                   "ph_num": contactInfo[0].ph_number}
    params = {"product" : dict(imageUrl=product, title=title, id=id), "contactInfo" :contactInfo}
    print("Product", params)
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        subject = request.POST.get('subject')
        company = request.POST.get('company')
        email = request.POST.get('email')
        message = request.POST.get('message')
        send_mail(
            subject,
            f'name : {name} \ncontact : {contact}\nrequest_type : product request\nproduct name : {title}\ncompany : {company}\nmessage : {message}',
            EMAIL_HOST_USER,
            ['gehlothweb@gmail.com'],
            fail_silently=False,
        )
        send_mail(
            'Thanks for contacting us.',
            'Hello our team have received your request, we will get back to you as soon as possible.\n\nThank you\nGOI PVT. LTD.',
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

    return render(request, 'home/contact2.html', params)

def products(request):
    contactInfo = ContactUs.objects.all()
    contactInfo = {"location": contactInfo[0].location, "email": contactInfo[0].email, "ph_num" : contactInfo[0].ph_number}
    products = Product.objects.all()
    for i in products:
        i.imageUrl = str(i.imageUrl).split("/")[5]

    print(products)
    params = {"products" : products, "contactInfo" : contactInfo}
    return render(request, 'home/services.html', params)

def career(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        place = request.POST.get('place')
        experience = request.POST.get('exp')
        email = request.POST.get('email')
        about_himself = request.POST.get('details')
        msg = EmailMessage(
            'Career options request',
            f'name : {name} \ncontact : {contact}\nrequest_type : help request\nplace : {place}\nexperience : {experience}\nabout himself : {about_himself}',
            EMAIL_HOST_USER,
            ['contactus@rapidtechit.com']
        )
        # print(request.FILES.get('upfile'))
        # ['contactus@rapidtechit.com'],
        if request.FILES.get('upfile') :
            print("has files")
            file = request.FILES['upfile']
            msg.attach(file.name, file.read(), file.content_type)

        msg.send(fail_silently=False)
        send_mail(
            'Reply to your career option request',
            f'Hello {name}, our team have received your career option request, we will get back to you as soon as possible',
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
    return render(request, 'home/career.html')