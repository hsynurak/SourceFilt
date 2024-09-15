from django.shortcuts import render, get_object_or_404
from .models import Kitap
from django.db.models import Q

def homepage(request):
    return render(request, "homepage.html")

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def sources(request):
    tyt_kitaplar = Kitap.objects.filter(sinav_turu="TYT").values('ders').distinct()
    ayt_kitaplar = Kitap.objects.filter(sinav_turu="AYT").values('ders').distinct()
    all_kitaplar = Kitap.objects.filter(Q(sinav_turu="AYT") | Q(sinav_turu="TYT")).values('ders').distinct()

    ders = request.GET.get('ders')
    sinav_turu = request.GET.get('sinav_turu')
    
    if ders:
        kitaplar = Kitap.objects.filter(ders=ders)
    else:
        kitaplar = Kitap.objects.all()
    
    if sinav_turu:
        kitaplar = kitaplar.filter(sinav_turu=sinav_turu)

    # Handle sorting
    sort_by = request.GET.get('sort_by', 'most_preferred')  
    if sort_by == 'most_preferred':
        kitaplar = kitaplar.order_by('-puan')  
    elif sort_by == 'least_preferred':
        kitaplar = kitaplar.order_by('puan') 
    elif sort_by == 'cheapest':
        kitaplar = kitaplar.order_by('fiyat') 
    elif sort_by == 'most_expensive':
        kitaplar = kitaplar.order_by('-fiyat') 

    # Pagination
    paginator = Paginator(kitaplar, 20)
    page = request.GET.get('page')
    try:
        kitaplar_page = paginator.page(page)
    except PageNotAnInteger:
        kitaplar_page = paginator.page(1)
    except EmptyPage:
        kitaplar_page = paginator.page(paginator.num_pages)

    return render(request, 'sourcepage.html', {
        'kitaplar': kitaplar_page,
        'all_kitaplar': all_kitaplar,
        'tyt_kitaplar': tyt_kitaplar,
        'ayt_kitaplar': ayt_kitaplar,
        'selected_ders': ders,
        'selected_sinav_turu': sinav_turu,
    })

def SpesificSource(request, tur):
    kitaplar = Kitap.objects.filter(ders=tur)
    return render(request, 'sourcepage.html', {'kitaplar': kitaplar})

def productdetail(request, id):
    kitap = get_object_or_404(Kitap, id=id)
    return render(request, 'productdetail.html', {'kitap': kitap})
