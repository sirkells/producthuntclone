from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.
def home(request):
    products = Product.objects
    return render(request, 'products/home.html', {'products': products})


@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body_text'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            #checks if all field has bee added
            product = Product()
            product.title = request.POST['title'] #add title
            product.body_text = request.POST['body_text'] #add text
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'): #checks if http:// was added to d url
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url'] #adds http to d url
            product.icon = request.FILES['icon']# add icon
            product.image = request.FILES['image']#add image
            product.pub_date = timezone.datetime.now() #time and date
            product.no_of_votes = 1# default no of vootes is 1
            product.hunter = request.user# adds user who added the project
            product.save()#save and add project to db
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html', {'error': 'All fields needs to be added'})
            
    else:
        return render(request, 'products/create.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})


@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.no_of_votes += 1
        product.save()
        return redirect('/products/' + str(product.id))
    
