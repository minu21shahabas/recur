from django.db import models
from django.contrib.auth.models import User

class company_details(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    contact_number = models.CharField(max_length=100,null=True,blank=True)
    company_name = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    company_email = models.CharField(max_length=255,null=True,blank=True)
    business_name = models.CharField(max_length=255,null=True,blank=True)
    company_type = models.CharField(max_length=255,null=True,blank=True)
    industry_type = models.CharField(max_length=255,null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank = True,upload_to = 'image/patient')




class Sales(models.Model):
    Account_type=models.TextField(max_length=255)
    Account_name=models.TextField(max_length=255)
    Acount_code=models.TextField(max_length=255)
    Account_desc=models.TextField(max_length=255)
    def __str__(self):
        return self.Account_name
    


class Purchase(models.Model):
    Account_type=models.TextField(max_length=255)
    Account_name=models.TextField(max_length=255)
    Acount_code=models.TextField(max_length=255)
    Account_desc=models.TextField(max_length=255)
    def __str__(self):
        return self.Account_name




class Unit(models.Model):
    unit=models.TextField(max_length=255)

    def __str__(self):
        return self.unit

    
    
    
class AddItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    type=models.TextField(max_length=255)
    Name=models.TextField(max_length=255)
    unit=models.ForeignKey(Unit,on_delete=models.CASCADE)
    sales=models.ForeignKey(Sales,on_delete=models.CASCADE)
    purchase=models.ForeignKey(Purchase,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    s_desc=models.TextField(max_length=255)
    p_desc=models.TextField(max_length=255)
    creat=models.CharField(max_length=255)
    s_price=models.CharField(max_length=255)
    p_price=models.TextField(max_length=255)
    satus=models.TextField(default='active')
    interstate=models.CharField(max_length=255,default='')
    intrastate=models.CharField(max_length=255,default='')

class History(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    date=models.DateTimeField(auto_now=True)
    message=models.CharField(max_length=255)
    p=models.ForeignKey(AddItem,on_delete=models.CASCADE)


class vendor_table(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    salutation=models.CharField(max_length=25)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    company_name=models.CharField(max_length=150)
    vendor_display_name=models.CharField(max_length=150)
    vendor_email=models.CharField(max_length=250)
    vendor_wphone=models.CharField(max_length=50)
    vendor_mphone=models.CharField(max_length=50)
    skype_number=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    website=models.CharField(max_length=250)
    gst_treatment=models.CharField(max_length=100)
    gst_number=models.CharField(max_length=50,null=True)
    pan_number=models.CharField(max_length=50,null=True)
    source_supply=models.CharField(max_length=100)
    currency=models.CharField(max_length=50)
    opening_bal=models.CharField(max_length=100)
    payment_terms=models.CharField(max_length=100)
    battention=models.CharField(max_length=100,default='')
    bcountry=models.CharField(max_length=100,default='')
    baddress=models.CharField(max_length=300,default='')
    bcity=models.CharField(max_length=100,default='')
    bstate=models.CharField(max_length=100,default='')
    bzip=models.CharField(max_length=100,default='')
    bphone=models.CharField(max_length=100,default='')
    bfax=models.CharField(max_length=100,default='')
    sattention=models.CharField(max_length=100,default='')
    scountry=models.CharField(max_length=100,default='')
    saddress=models.CharField(max_length=300,default='')
    scity=models.CharField(max_length=100,default='')
    sstate=models.CharField(max_length=100,default='')
    szip=models.CharField(max_length=100,default='')
    sphone=models.CharField(max_length=100,default='')
    sfax=models.CharField(max_length=100,default='')

class comments_table(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,default='')
    vendor=models.ForeignKey(vendor_table,on_delete=models.CASCADE,null=True)
    comment=models.TextField(max_length=500)

class mail_table(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,default='')
    vendor=models.ForeignKey(vendor_table,on_delete=models.CASCADE,null=True)
    mail_from=models.TextField(max_length=300)
    mail_to=models.TextField(max_length=300)
    subject=models.TextField(max_length=250)
    content=models.TextField(max_length=900)
    mail_date=models.DateTimeField(auto_now_add=True)

class doc_upload_table(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,default='')
    vendor=models.ForeignKey(vendor_table,on_delete=models.CASCADE,null=True)
    title=models.TextField(max_length=200)
    document=models.FileField(upload_to='doc/')
    
    
    
 

class customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    customerName= models.CharField(max_length=100,null=True,blank=True)
    customerType= models.CharField(max_length=100,null=True,blank=True)
    companyName= models.CharField(max_length=100,null=True,blank=True)
    customerEmail= models.CharField(max_length=100,null=True,blank=True)
    customerWorkPhone= models.CharField(max_length=100,null=True,blank=True)
    customerMobile= models.CharField(max_length=100,null=True,blank=True)
    skype=models.CharField(max_length=100,null=True,blank=True)
    designation=models.CharField(max_length=100,null=True,blank=True)
    department=models.CharField(max_length=100,null=True,blank=True)
    website=models.CharField(max_length=100,null=True,blank=True)
    GSTTreatment=models.CharField(max_length=100,null=True,blank=True)
    placeofsupply=models.CharField(max_length=100,null=True,blank=True)
    Taxpreference=models.CharField(max_length=100,null=True,blank=True)
    currency=models.CharField(max_length=100,null=True,blank=True)
    OpeningBalance= models.IntegerField(null=True,blank=True)
    PaymentTerms=models.CharField(max_length=100,null=True,blank=True)
    PriceList=models.CharField(max_length=100,null=True,blank=True)

    PortalLanguage=models.CharField(max_length=100,null=True,blank=True)
    Facebook=models.CharField(max_length=100,null=True,blank=True)
    Twitter=models.CharField(max_length=100,null=True,blank=True)
    Attention=models.CharField(max_length=100,null=True,blank=True)
    country=models.CharField(max_length=100,null=True,blank=True)
    Address1=models.CharField(max_length=100,null=True,blank=True)
    Address2=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    zipcode=models.CharField(max_length=100,null=True,blank=True)
    phone1=models.CharField(max_length=100,null=True,blank=True)
    fax=models.CharField(max_length=100,null=True,blank=True)

    CPsalutation=models.CharField(max_length=100,null=True,blank=True)
    Firstname=models.CharField(max_length=100,null=True,blank=True)
    Lastname=models.CharField(max_length=100,null=True,blank=True)
    CPemail=models.CharField(max_length=100,null=True,blank=True)#
    CPphone=models.CharField(max_length=100,null=True,blank=True)
    CPmobile=models.CharField(max_length=100,null=True,blank=True)
    CPskype=models.CharField(max_length=100,null=True,blank=True)
    CPdesignation=models.CharField(max_length=100,null=True,blank=True)
    CPdepartment=models.CharField(max_length=100,null=True,blank=True)

class RetainerInvoice(models.Model):
    customer_name=models.ForeignKey(customer,on_delete=models.CASCADE)
    retainer_invoice_number=models.CharField(max_length=255)
    refrences=models.CharField(max_length=255)
    retainer_invoice_date=models.DateField()
    total_amount=models.CharField(max_length=100)
    customer_notes=models.TextField()
    terms_and_conditions=models.TextField()
    is_draft=models.BooleanField(default=True)
    is_sent=models.BooleanField(default=False)

class Retaineritems(models.Model):
    retainer=models.ForeignKey(RetainerInvoice, on_delete=models.CASCADE)
    description=models.TextField()
    amount=models.CharField(max_length=100)
            
class Estimates(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    customer_name = models.CharField(max_length=100,null=True,blank=True)
    estimate_no = models.CharField(max_length=100,null=True,blank=True)
    reference = models.CharField(max_length=100,null=True,blank=True)
    estimate_date = models.DateField(null=True)
    expiry_date = models.DateField(null=True)
    sub_total = models.FloatField(null=True,blank=True)
    igst = models.FloatField(null=True,blank=True)
    sgst = models.FloatField(null=True,blank=True)
    cgst = models.FloatField(null=True,blank=True)
    tax_amount = models.FloatField(null=True,blank=True)
    shipping_charge = models.FloatField(null=True,blank=True)
    adjustment = models.FloatField(null=True,blank=True)
    total = models.FloatField(null=True,blank=True)
    status = models.CharField(max_length=100,null=True,blank=True)
    customer_notes = models.CharField(max_length=250,null=True,blank=True)
    terms_conditions = models.CharField(max_length=250,null=True,blank=True)
    attachment = models.ImageField(upload_to="image/", null=True)  

class EstimateItems(models.Model):
    estimate = models.ForeignKey(Estimates,on_delete=models.CASCADE,null=True,blank=True)
    item_name = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    rate = models.FloatField(null=True,blank=True)
    discount = models.FloatField(null=True,blank=True)
    tax_percentage = models.IntegerField(null=True,blank=True)
    amount = models.FloatField(null=True,blank=True)

class payment(models.Model):
    term=models.TextField(max_length=255)
    days=models.TextField(max_length=255)
    
class payment_terms(models.Model):
    Terms=models.CharField(max_length=100,null=True,blank=True)
    Days=models.IntegerField(null=True,blank=True)    

class invoice(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    invoice_no=models.TextField(max_length=255)
    terms=models.ForeignKey(payment_terms,on_delete=models.CASCADE)
    order_no=models.IntegerField()
    inv_date=models.DateField()
    due_date=models.DateField()
    igst=models.TextField(max_length=255)
    cgst=models.TextField(max_length=255)
    sgst=models.TextField(max_length=255)
    t_tax=models.FloatField()
    subtotal=models.FloatField()
    grandtotal=models.FloatField()
    cxnote=models.TextField(max_length=255)
    file=models.ImageField(upload_to='documents')
    terms_condition=models.TextField(max_length=255)
    status=models.TextField(max_length=255)
    
    def __str__(self) :
        return self.invoice_no
    
class invoice_item(models.Model):
    product=models.TextField(max_length=255)
    quantity=models.IntegerField()
    hsn=models.TextField(max_length=255)
    tax=models.IntegerField()
    total=models.FloatField()
    desc=models.TextField(max_length=255)
    rate=models.TextField(max_length=255)
    inv=models.ForeignKey(invoice,on_delete=models.CASCADE)


class Pricelist(models.Model):
    itemtable=models.ForeignKey(AddItem,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    types=models.CharField(max_length=255)
    tax=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    mark=models.CharField(max_length=255)
    percentage=models.IntegerField()
    roundoff=models.CharField(max_length=255)
    currency=models.CharField(max_length=255)
    status= models.TextField(default='active')
    
class Sample_table(models.Model):
    item_name=models.CharField(max_length=255)
    price=models.IntegerField()
    cust_rate=models.FloatField()
    pl=models.ForeignKey(Pricelist,on_delete=models.CASCADE)
    
    
class contact_person_table(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    vendor=models.ForeignKey(vendor_table,on_delete=models.CASCADE,null=True)
    salutation=models.CharField(max_length=25)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=200)
    work_phone=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    skype_number=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    department=models.CharField(max_length=50)

class remarks_table(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    vendor=models.ForeignKey(vendor_table,on_delete=models.CASCADE,null=True)
    remarks=models.CharField(max_length=500)




