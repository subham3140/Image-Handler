from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ImagePro

# Create your views here.

def home(request):
    if request.method == "POST":
        
        img = ImagePro(image=request.FILES.get("image"))
 
        img.save()
        redirect_to = f'/media/{img.image}'
      
        # resizing 
        img.resize(int(request.POST.get("width")),int(request.POST.get("height")))

      #   # quality
        img.quality(int(request.POST.get("quality")))


        # image rotate
        if request.POST.get("rotate") != None:
           img.rotate(int(request.POST.get("rotate")))
        elif request.POST.get("rotate-custom") != "":
           img.rotate(int(request.POST.get("rotate-custom")))

        #image flip
        if request.POST.get("flip") != None:
           img.flip(request.POST.get("flip"))
       
      #   #image convert to 'L', 'RBG', 'CMYK'(CMYK refers to the four ink plates used in some color printing: cyan, magenta, yellow, and key (black))
        img.colorTransform(request.POST.get("colortransform"))

        #image enhance
        img.enhance(int(request.POST.get("enhance")))
        return redirect(redirect_to)  

    return render(request, 'home.html')
