from django.shortcuts import render, get_object_or_404
from blog.models import big_Category, small_Category, Doktor, Xizmat , Galery
from .forms import SearchForm # Qidiruv shaklini import qilamiz

# Ko'rish funksiyalari
# ru
def index(request):
    form = SearchForm()
    query = None
    results_doktor = []
    results_xizmat = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results_doktor = Doktor.objects.filter(name__icontains=query)  # Doktorlarni qidiramiz
            results_xizmat = Xizmat.objects.filter(name__icontains=query)  # Xizmatlarni qidiramiz

            return render(request, 'blog/search.html', {
                'form': form,
                'query': query,
                'results_doktor': results_doktor,
                'results_xizmat': results_xizmat
            })

    doktors = Doktor.objects.order_by("-date")[:10]
    galerylar = Galery.objects.order_by("-date")[:12]
    xizmatlar = Xizmat.objects.order_by("-date")[:4]

    return render(request, 'blog/index.html', {
        'doktors': doktors,
        'xizmatlar': xizmatlar,
        'galerylar': galerylar,
        'form': form
    })

def doktors(request):
    doktors = Doktor.objects.order_by("-date")
    return render(request , 'blog/doktors.html' , {'doktors': doktors})

def contact(request):
    return render(request , 'blog/contact.html' )

def doktor_detail(request, id):
    doktor = get_object_or_404(Doktor, id=id)
    return render(request, 'blog/stranisa-vrachi.html', {"doktor": doktor})

def xizmatlar(request):
    xizmatlar = Xizmat.objects.order_by("-date")
    kichik_kategoriyalar = small_Category.objects.all()
    katta_kategoriyalar = big_Category.objects.all()
    return render(request , 'blog/xizmatlar.html' , {
        'xizmatlar': xizmatlar,
        'kichik_kategoriyalar': kichik_kategoriyalar,
        'katta_kategoriyalar' : katta_kategoriyalar,
    })


def xizmat_detail(request, id):
    xizmat = get_object_or_404(Xizmat, id=id)
    return render(request, 'blog/xizmat_detail.html', {"xizmat": xizmat})

def galereyaru(request):
    rasmlar = Galery.objects.order_by("-date")
    return render(request , 'blog/galereya.html' , {'rasmlar': rasmlar})


# ! uz


def indexuz(request):
    form = SearchForm()
    query = None
    results_doktor = []
    results_xizmat = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results_doktor = Doktor.objects.filter(name__icontains=query)  # Doktorlarni qidiramiz
            results_xizmat = Xizmat.objects.filter(name__icontains=query)  # Xizmatlarni qidiramiz

            return render(request, 'bloguz/search.html', {
                'form': form,
                'query': query,
                'results_doktor': results_doktor,
                'results_xizmat': results_xizmat
            })

    doktors = Doktor.objects.order_by("-date")[:10]
    galerylar = Galery.objects.order_by("-date")[:12]
    xizmatlar = Xizmat.objects.order_by("-date")[:4]

    return render(request, 'bloguz/index.html', {
        'doktors': doktors,
        'xizmatlar': xizmatlar,
        'galerylar': galerylar,
        'form': form
    })

def doktorsuz(request):
    doktors = Doktor.objects.order_by("-date")
    return render(request , 'bloguz/doktors.html' , {'doktors': doktors})

def contactuz(request):
    return render(request , 'bloguz/contact.html' )

def doktor_detailuz(request, id):
    doktor = get_object_or_404(Doktor, id=id)
    return render(request, 'bloguz/doktor_detail.html', {"doktor": doktor})

def xizmatlaruz(request):
    xizmatlar = Xizmat.objects.order_by("-date")
    kichik_kategoriyalar = small_Category.objects.all()
    katta_kategoriyalar = big_Category.objects.all()
    return render(request , 'bloguz/xizmatlar.html' , {
        'xizmatlar': xizmatlar,
        'kichik_kategoriyalar': kichik_kategoriyalar,
        'katta_kategoriyalar' : katta_kategoriyalar,
    })


def xizmat_detailuz(request, id):
    xizmat = get_object_or_404(Xizmat, id=id)
    return render(request, 'bloguz/xizmat_detail.html', {"xizmat": xizmat})

def galereya(request):
    rasmlar = Galery.objects.order_by("-date")
    return render(request , 'bloguz/galereya.html' , {'rasmlar': rasmlar})
