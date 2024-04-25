from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Image
from PIL import Image as im
from .forms import *
from .stegno import  encode as e
from .stegno import  decode as d

def home(request):

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            i = Image.objects.latest('id')

            return redirect('encode_decode')

    else:
        form = UploadForm()
        return render(request, 'home.html', {'form' : form})

def encode_decode(request):
    decoded = None  # Initialize the variable

    if request.method == 'POST':
        imageobj = Image.objects.latest('id')
        imageobj.img.open()
        image = im.open(imageobj.img)

        if request.POST.get('action') == 'encode':
            inputtext = request.POST['inputtext']
            e(image, inputtext)
        elif request.POST.get('action') == 'decode':
            decoded = d(image)

    return render(request, 'encode_decode.html', {'decoded': decoded })

