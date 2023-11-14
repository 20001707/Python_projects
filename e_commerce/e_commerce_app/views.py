from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse  
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request,'index.html')

def slogin(request):
    a=new_register_model.objects.all() 
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
       
        for i in a :
            if (i.username==username and i.password==password):
                request.session['id']=i.id
                return redirect(seller_profile)
        else:
            return HttpResponse("Login Failed")
    return render(request,'slogin.html')





def sregister(request): 
    if request.method=='POST':
        name=request.POST.get('name')
        pimage=request.FILES.get('pimage')
        username=request.POST.get('username')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        
       
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            a=new_register_model(name=name,email=email,pimage=pimage,phone=phone,username=username,password=password)
            a.save()
            return redirect(slogin)
    
    
        else:
            return redirect(sregister)
        
        
        
    return render(request,'sregister.html')




def seller_profile(request):
    id1=request.session['id']
    a=new_register_model.objects.get(id=id1)
    img=str(a.pimage).split('/')[-1]
    return render(request,'seller.html',{'data':a,'img':img})





def upload(request):
    if request.method=='POST':
        categories=request.POST.get('categories')
        prize=request.POST.get('prize')
        age_range=request.POST.get('age_range')
        brand=request.POST.get('brand')
        color=request.POST.get('color')
        productimg=request.FILES.get('productimg')
        
        b=add_prod(categories=categories,prize=prize,age_range=age_range,brand=brand,color=color,productimg=productimg)
        b.save()    #for commit
        return redirect(seller_profile)
    return render(request,'upload.html')


def edit_profile(request,id):
    a=new_register_model.objects.get(id=id)
    
    if request.method=='POST':
        a.name=request.POST.get('name')
       
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        
        a.username=request.POST.get('username')
        
            
        a.save()
        return redirect(seller_profile)
        
    
    return render(request,'edit_profile.html',{'data':a})


    
    

def seller_productview(request,id):

    id=[]
    categories=[]
    prize=[]
    age_range=[]
    brand=[]
    color=[]
    productimg=[]
    
    a=add_prod.objects.all()

    for i in a:

        id1=i.id

        id.append(id1)

        categories1=i.categories

        categories.append(categories1)

        prize1=i.prize

        prize.append(prize1)

        productimg1=str(i.productimg).split('/')[-1]

        productimg.append(productimg1)

        brand1=i.brand

        brand.append(brand1)

        color1=i.color

        color.append(color1)
        
        age_range1=i.age_range

        age_range.append(age_range1)
        
    mylist=zip(id, categories, prize, productimg, brand, color,age_range)

    return render(request,'view_product.html',{'data':mylist})


def userregister(request): 
    if request.method=='POST':
        uname=request.POST.get('uname')
        uusername=request.POST.get('uusername')
        uphone=request.POST.get('uphone')
        uemail=request.POST.get('uemail')
        proimage=request.FILES.get('proimage')       
        upassword=request.POST.get('upassword')
        ucpassword=request.POST.get('ucpassword')
        if upassword==ucpassword:
            aa=user_register_model(uname=uname,uemail=uemail,proimage=proimage,uphone=uphone,uusername=uusername,upassword=upassword)
            aa.save()
            a=user_register_model.objects.all()
            for i in a:
                if(i.uusername==uusername or i.uemail==uemail):
                    return HttpResponse("Allready Registered")
                else:
                    aa.save()
           
            if upassword==ucpassword:
                return redirect(userlogin)
            else:
                return redirect(userregister)
            
        
        
        
    return render(request,'user_reg.html')



def userlogin(request):
    a=user_register_model.objects.all() 
    if request.method=='POST':
        uusername=request.POST.get('uusername')
        upassword=request.POST.get('upassword')
        
       
        for i in a :
            if (uusername==i.uusername and upassword==i.upassword):
                request.session['u_id']=i.id
                return redirect(userindex)
        else:
            return HttpResponse("Login Failed")
    return render(request,'user_login.html')



def user_profile(request):
    id2=request.session['u_id']
    a=user_register_model.objects.get(id=id2)
    img=str(a.proimage).split('/')[-1]
    return render(request,'user_profile.html',{'data':a,'img':img})



def userindex(request):
    id2=request.session['u_id']
    a=user_register_model.objects.get(id=id2)
    c=add_prod.objects.all()
    ids=[]
    categories=[]
    prize=[]
    age_range=[]
    brand=[]
    color=[]
    productimg=[]
    
   
    for i in c:

        id1=i.id

        ids.append(id1)

        categories1=i.categories

        categories.append(categories1)

        prize1=i.prize

        prize.append(prize1)

        productimg1=str(i.productimg).split('/')[-1]

        productimg.append(productimg1)

        brand1=i.brand

        brand.append(brand1)

        color1=i.color

        color.append(color1)
        
        age_range1=i.age_range

        age_range.append(age_range1)
        
    mylist=zip(ids, categories, prize, productimg, brand, color,age_range)
   
    return render(request,'userindex_all.html',{'name':a,'data':mylist})



def userindex_category(request,category):
    id2=request.session['u_id']
    a=user_register_model.objects.get(id=id2)
    c=add_prod.objects.all()
    idk=[]
    categories=[]
    prize=[]
    age_range=[]
    brand=[]
    color=[]
    productimg=[]
    for i in c:

        id1=i.id

        idk.append(id1)

        categories1=i.categories

        categories.append(categories1)

        prize1=i.prize

        prize.append(prize1)

        productimg1=str(i.productimg).split('/')[-1]

        productimg.append(productimg1)

        brand1=i.brand

        brand.append(brand1)

        color1=i.color

        color.append(color1)
        
        age_range1=i.age_range

        age_range.append(age_range1)
        
    mylist=zip(idk, categories, prize, productimg, brand, color,age_range)
    

    # category=category.replace('_',' ')

   
    
    return render(request,'userindex.html',{'name':a,'data':mylist,'category':category})

    
def wishlist(request,id):
    a=add_prod.objects.get(id=id)
    id1=request.session['u_id']
    c=wishmodel.objects.all()
    for i in c:
        if id ==i.prod_id and id1 == i.userid:
            return HttpResponse("Item already in wishlist")
    else:
        b=wishmodel(prod_id=a.id,userid=id1,categories=a.categories, prize=a.prize, productimg=a.productimg, brand=a.brand)
        b.save()
        return HttpResponse("Item added successfully into wishlist..")
   

def wishlist_view(request):
    id3=request.session['u_id']
    a=wishmodel.objects.all()
    id1=[]
    userid=[]
    prod_id=[]
    categories=[]
    prize=[]
    productimg=[]
    brand=[]
    
    for i in a:
        idw=i.id
        id1.append(idw)
        
        
        userid1=i.userid
        userid.append(userid1)
        prod_id1=i.prod_id
        prod_id.append(prod_id1)
        categories1=i.categories
        categories.append(categories1)
        prize1=i.prize
        prize.append(prize1)
        productimg1=str(i.productimg).split('/')[-1]
        productimg.append(productimg1)
        brand1=i.brand
        brand.append(brand1)
    mylist=zip(id1,prod_id,userid,categories,prize,productimg,brand)
    return render(request,'wishlist_view.html',{'data':mylist,'id':id3})

def delete_wish(request,id):
    a=wishmodel.objects.get(id=id)
    id1 = request.session['u_id']
    a.delete()
    return redirect("http://127.0.0.1:8000/wishview/")





def cart_add(request,id):
    a=add_prod.objects.get(id=id)
    id1=request.session['u_id']
    c=cartmodel.objects.all()
    for i in c:
        if id == i.prod_id and id1 == i.userid:
            i.quantity +=1
            i.prize=a.prize * i.quantity
            i.save()
            return HttpResponse("product incremented")
    else:
        count=1
        b=cartmodel(prod_id=a.id,userid=id1,quantity=count,categories=a.categories, prize=a.prize, brand=a.brand, productimg=a.productimg)
        b.save()
        return HttpResponse("Item added successfully into Cart..")
    
    
def cart_view(request):
    id3=request.session['u_id']
    a=cartmodel.objects.all()
    id1=[]
    userid=[]
    prod_id=[]
    quantity=[]
    categories=[]
    prize=[]
    productimg=[]
    brand=[]
    
    for i in a:
        idw=i.id
        id1.append(idw)
        userid1=i.userid
        userid.append(userid1)
        prod_id1=i.prod_id
        prod_id.append(prod_id1)
        categories1=i.categories
        categories.append(categories1)
        prize1=i.prize
        prize.append(prize1)
        productimg1=str(i.productimg).split('/')[-1]
        productimg.append(productimg1)
        brand1=i.brand
        brand.append(brand1)
        quantity1=i.quantity
        quantity.append(quantity1)
        
    tp1=[]
    tp2=[]
    d=cartmodel.objects.filter(userid=id3)
    for i in d:
        tp1.append(i.prize)
    for i in tp1:
        tp2.append(int(i))
    total_prize=sum(tp2)
    
        
    mylist=zip(id1,prod_id,userid,quantity,categories,prize,brand,productimg)
    return render(request,'cart.html',{'data':mylist,'id':id3,'prize':total_prize})

def cartinc(request,id):
    a=cartmodel.objects.get(id=id)
    b=add_prod.objects.get(id=a.prod_id)
    a.quantity += 1
    a.prize=b.prize * a.quantity
    a.save() 
    return redirect(cart_view)

def cartdec(request,id):
    a=cartmodel.objects.get(id=id)
    b=add_prod.objects.get(id=a.prod_id)
    a.quantity -=1
    a.prize=b.prize * a.quantity
    a.save()
    return redirect(cart_view)

def cart_delete(request,id):
    a=cartmodel.objects.get(id=id)
    id1 = request.session['u_id']
    a.delete()
    return redirect("http://127.0.0.1:8000/cart_view/")

def user_address(request):
    try:
        id2=request.session['u_id']
        b=addressmodel.objects.get(userid=id2)
        if b.address:
            return redirect(edit_useraddress)
    except:
        if request.method =='POST':
            fname=request.POST.get('fname')
            lname=request.POST.get('lname')
            phone=request.POST.get('phone')
            email=request.POST.get('email')
            state=request.POST.get('state')
            city=request.POST.get('city')
            address=request.POST.get('address')
            pincode=request.POST.get('pincode')
            a=addressmodel(userid=id2,fname=fname,lname=lname,phone=phone,address=address,email=email,state=state,city=city,pincode=pincode)
            a.save()
            return redirect(cart_view)
    return render(request,'address.html')
            
            
            
        
        
def edit_useraddress(request):
    id1=request.session['u_id']
    a=addressmodel.objects.get(userid=id1)
    if request.method =='POST':
        a.fname = request.POST.get('fname')
        a.lname=request.POST.get('lname')
        a.phone = request.POST.get('phone')
        a.email = request.POST.get('email')
        a.state = request.POST.get('state')
        a.city = request.POST.get('city')
        a.address = request.POST.get('address')
        a.pincode = request.POST.get('pincode')
        a.save()
        return redirect(cart_view)
    
    
    return render(request,'edit_address.html',{'data':a})


def payment(request):
    
    return render(request,'payment.html')
    
    
def order_details(request):
    id2 = request.session['u_id']
    uname = request.session['uname']
    total_prize = request.session['total_prize']
    productimg = []
    categories = []
    brand = []
    quantity = []
    prize = []
    # ord_date = []
    # del_date = []
    a = cartmodel.objects.all()
    for i in a:
        if i.u_id == id2:
            productimg.append(str(i.productimg).split('/')[-1])
            categories.append(i.categories1)
            brand.append(i.brand1)
            quantity.append(i.quantity1)
            prize.append(i.prize)
            # ord_date.append(i.order_date)
            # del_date.append(i.est_del_date)
    print(productimg)
    print(categories)

    mylist = zip(productimg,categories,brand,quantity,prize)
    d = cartmodel.objects.all()
    d.delete()
    return render(request,'ordered_products.html',{'data':mylist,'total_prize':total_prize,'uname':uname})   




       




        
# def user_logout(request):
#     logout(request)
#     return redirect(userlogin)  



        
    
    
    