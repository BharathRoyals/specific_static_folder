from django.shortcuts import render

# Create your views here.
def specific_static_folder(request):
    return render(request,'specific_static_folder.html')

def penvith(request):
    return render(request,'penvith.html')