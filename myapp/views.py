from django.shortcuts import render

def home(request):
    return render(request, "myapp/homepage.html")

def hrc_detail(request):
    
    return render(request, "myapp/hrc.html")
def catalog(request):
    
    return render(request, "myapp/catalog.html")
def ms_sheets(request):
    
    return render(request, "myapp/ms_sheets.html")
def ppgl(request):
    
    return render(request, "myapp/ppl.html")
def  abrasive_discs(request):
    
    return render(request, "myapp/abrasive_discs.html")
def  welding_wire(request):
    
    return render(request, "myapp/awelding_wire.html")

def  electrodes(request):
    
    return render(request, "myapp/electrodes.html")
def  bolts(request):
    
    return render(request, "myapp/bolts.html")
def  grinding(request):
    
    return render(request, "myapp/grinding.html")



