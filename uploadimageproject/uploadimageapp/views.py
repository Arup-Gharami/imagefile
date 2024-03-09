from django.shortcuts import render
from uploadimageapp.models import ImageUploadModel
from uploadimageapp.forms import ImageuploadForm
from django.http import HttpResponse

# Create your views here.
def upload_image(request):
    if request.method == 'POST':
        form = ImageuploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Image uploaded successfully...</h2>")
    else:
        form = ImageuploadForm()
        images = ImageUploadModel.objects.all()
    return render(request,'index.html',{'form':form,'images':images})