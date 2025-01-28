from django.contrib import admin

from blog.models import big_Category, small_Category, Doktor, Xizmat , Galery


# Register your models here.
admin.site.register(Doktor)
admin.site.register(Xizmat)
admin.site.register(Galery)
admin.site.register(small_Category)
admin.site.register(big_Category)
