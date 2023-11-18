from django.shortcuts import render
from .models import TexTak ,menuItem ,Photo

# Create your views here.
# textt = 'shayannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
def index(request):
    return render(request, 'Terminal/Terminal.html')


def HakingMusic(request):
    return render(request, 'Haking/music.html')



def nav(request):
    sh =TexTak.objects.all()
    menu = menuItem.objects.all()
    image_mn = Photo.objects.all()

    for img in image_mn:
        s2 = str(img.image)
        img.image = s2.replace('BlogPegasus/static/','')


    for x in sh:
        y = x.mtn1
        mtn2 =x.mtn2
        mtn3 =x.mtn3

    # for z in menu:
    #     name = z.name
    #     mtn_kol = z.mtn_kol
    #     lnk_a = z.lnk_a


    return render(request,"blog/home.html", {
        'textt':y,
        'mtn2':mtn2,
        'mtn3':mtn3,
        'menuItem':menu,
        'img_mno':image_mn

    })
