# from email.mime import image
from django.db import models

# Create your models here.
class big_Category(models.Model):
    UZ = 'uz'
    RU = 'ru'
    CHOISE_GROUP_lang = {
        (UZ , 'uz'),
        (RU , 'ru'),
    }
    group_lang = models.CharField(max_length=100 , choices=CHOISE_GROUP_lang , default=UZ)
    name = models.CharField('Katta xizmat guruxi' ,max_length=150)
    date = models.DateTimeField('Katta xizmat yuklangan sana' , auto_now_add=True)

    def __str__(self):
        return self.name

class small_Category(models.Model):
    name = models.CharField('Kichik xizmat guruhi' ,max_length=150)
    date = models.DateTimeField('Kichik xizmat yuklangan sana' , auto_now_add=True)
    bc = models.ForeignKey(big_Category , on_delete=models.CASCADE , default = 1)

    def __str__(self):
        return self.name

class Xizmat(models.Model):

    UZ = 'uz'
    RU = 'ru'
    CHOISE_GROUP_lang = {
        (UZ , 'uz'),
        (RU , 'ru'),
    }
    name = models.CharField("Xizmat nomi" , max_length=200)
    price = models.IntegerField("Bir marotabalik xizmat narxi '$ da'" , default=0)
    date = models.DateTimeField('Xizmat yuklangan sana' , auto_now_add=True)
    chiqish = models.BooleanField('Ekranga chiqsinmi?' , default=True)
    max_group = models.ForeignKey(big_Category , on_delete=models.CASCADE , default="yo'q")
    group_lang = models.CharField(max_length=100 , choices=CHOISE_GROUP_lang , default=UZ)
    min_group= models.ForeignKey(small_Category,on_delete=models.CASCADE,default="bor" )
    class Meta:
        verbose_name = "Xizmat"
        verbose_name_plural = 'Xizmatlar'

    def __str__(self) -> str:
        return self.name


# class Doktor_small_category(models.Model):




class Doktor(models.Model):
    STAMATALOGIYA = 'stamatologiya'
    Travmatalogiya = 'travmatalogiya'
    OKULISTIKA = 'okulistika'
    CHOISE_GROUP = {
        (STAMATALOGIYA , 'stamatologiya'),
        (Travmatalogiya , 'travmatalogiya'),
        (OKULISTIKA , 'okulistika'),
    }
    UZ = 'uz'
    RU = 'ru'
    CHOISE_GROUP_lang = {
        (UZ , 'uz'),
        (RU , 'ru'),
    }
    name = models.CharField("Doktorning to'liq ismi" , max_length=200)
    image = models.ImageField('Doktor surati' ,)
    group = models.CharField(max_length=100 , choices=CHOISE_GROUP , default=STAMATALOGIYA)
    group_lang = models.CharField(max_length=100 , choices=CHOISE_GROUP_lang , default=UZ)
    min_skill = models.CharField('Mutahasisligi haqida qisqacha', max_length=255)
    max_skill = models.TextField("Doktor haqida to'liq ma'lumotlar")
    price = models.IntegerField("Bir marotabalik ko'rik narxi '$ da'")
    chiqish = models.BooleanField('Ekranga chiqsinmi?' , default=True)
    # staj = models.IntegerField('Doktorning staji')
    sertificat1 = models.ImageField('1-sertifikat' , null=True)
    sertificat2 = models.ImageField("2-sertifikat (bu va bundan pastdagilarini to'ldirmaslik mumkin)" , null=True, blank=True)
    sertificat3 = models.ImageField('3-sertifikat' , null=True , blank=True)
    sertificat4 = models.ImageField('4-sertifikat' , null=True , blank=True)

    # kategoriya = models.ForeignKey('Doktor kategoriyasi'  ,  on_delete=models.CASCADE)
    date = models.DateTimeField('Doktor yuklangan sana' , auto_now_add=True)
    staj = models.IntegerField('Doktor ish staji' , default=int(1))

    class Meta:
        verbose_name = "Doktor"
        verbose_name_plural = 'Doktorlar'

    def __str__(self) -> str:
        return self.name



class Galery(models.Model):
    title = models.CharField('Bu qayerning surati' , max_length=120 , default='Klinika')
    image = models.ImageField("Surat", upload_to='gallery', null=True, default='static/img/foto-klinika.png')
    date = models.DateTimeField('Rasm yuklangan sana' , auto_now_add=True)

    class Meta:
        verbose_name = "Galereya"
        verbose_name_plural = 'Galereya'

    def __str__(self) -> str:
        return self.title
