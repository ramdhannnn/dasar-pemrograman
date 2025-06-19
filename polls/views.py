from django.http import HttpResponse

def alamat_view(request):
    return HttpResponse("Alamat: JL.Pemandian Cigunung NO.03 Cisaat")

def telepon_view(request):
    return HttpResponse("Telepon: +62 813-8493-8647")