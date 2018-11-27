from django.shortcuts import render,HttpResponse


# Create your views here.

def inicio(request):
    return render(request,"inicio/Inicio/prueba.html")
def nosotros(request):
    return render(request,"inicio/Nosotros/Nosotros.html")
def teach(request):
    return render(request,"inicio/TeachC/Teach.html")
def goesir(request):
    return render(request,"inicio/Goes/ir/ir.html")
def goesvis(request):
    return render(request,"inicio/Goes/vis/vis.html")
def goesvw(request):
    return render(request,"inicio/Goes/vw/vw.html")
def model_cli_cho(request):
    return render(request,"inicio/Modelos/climato/cho/cho.html")
def model_cli_pres(request):
    return render(request,"inicio/Modelos/climato/pres/pres.html")
def model_cli_tmn(request):
    return render(request,"inicio/Modelos/climato/tmn/tmn.html")
def model_cli_tmx(request):
    return render(request,"inicio/Modelos/climato/tmx/tmx.html")
def model_pro_advt(request):
    return render(request,"inicio/Modelos/pronos/advt/advt.html")
def model_pro_l250(request):
    return render(request,"inicio/Modelos/pronos/l250/l250.html")
def model_pro_l500(request):
    return render(request,"inicio/Modelos/pronos/l500/l500.html")
def model_pro_l850(request):
    return render(request,"inicio/Modelos/pronos/l850/l850.html")
def model_pro_mgp(request):
    return render(request,"inicio/Modelos/pronos/mgp/mgp.html")
def model_pro_pres(request):
    return render(request,"inicio/Modelos/pronos/pres/pres.html")
def estaciones(request):
    return render("estaciones")
def cambioc(request):
    return render("cambioc")
