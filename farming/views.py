from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from farming.models import Petani, Panenan, Tanaman, Hama, PestisidaPupuk
from farming.serializers import PetaniSerializer, PanenanSerializer, TanamanSerializer, HamaSerializer, PestisidaPupukSerializer

@csrf_exempt
def petani_list(request):
    
    """
    List all petani, or create a new petani.
    """
    
    if request.method == 'GET':
        petani = Petani.objects.all()
        serializer = PetaniSerializer(petani, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PetaniSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def panenan_list(request):
    
    if request.method == 'GET':
        panenan = Panenan.objects.all()
        serializer = PanenanSerializer(panenan, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        
        data = JSONParser().parse(request)
        serializer = PanenanSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def tanaman_list(request):
    
    if request.method == 'GET':
        # ambil semua tanaman
        tanaman = Tanaman.objects.all() 
        
        # serializerkan data
        serializer = TanamanSerializer(tanaman, many=True)
        
        # kembalikan dalam bentuk json
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        
        # ambil data dari request
        data = JSONParser().parse(request)
        
        # serializerkan data
        serializer = TanamanSerializer(data=data)
        
        # jika valid maka disimpan jika tidak kembalikan HTTP 400
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def hama_list(request):
    
    """
    List all hama, or create a new hama.
    """
    
    if request.method == 'GET':
        hama = Hama.objects.all()
        serializer = HamaSerializer(hama, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HamaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def pupuk_pestisida_list(request):
    
    """
    List all pupuk pestisida, or create a new pupuk pestisida.
    """
    
    if request.method == 'GET':
        pupes = PestisidaPupuk.objects.all()
        serializer = PestisidaPupukSerializer(pupes, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PestisidaPupukSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



    
@csrf_exempt
def petani_detail(request, username):
    """
    Retrieve, update or delete a code petani
    """
    try:
        # coba ambil petani dengan id pk
        petani = Petani.objects.get(username=username)
    except Petani.DoesNotExist:
        
        # jika tidak ada kembalikan HTTP 404
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = PetaniSerializer(petani)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PetaniSerializer(petani, data=data)
        
    elif request.method == 'DELETE':
        petani.delete()
        return HttpResponse(status=204)
    
@csrf_exempt
def tanaman_detail(request, pk):
    
    """
    Retrieve, update or delete a code tanaman
    """
    
    try:
        tanaman = Tanaman.objects.get(pk=pk)
    except Tanaman.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = TanamanSerializer(tanaman)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TanamanSerializer(tanaman, data=data)
        
    elif request.method == 'DELETE':
        tanaman.delete()
        return HttpResponse(status=204)
    
    
@csrf_exempt
def panenan_detail(request, pk):
    
    """
    Retrieve, update or delete a code tanaman
    """
    
    try:
        panenan = Panenan.objects.get(pk=pk)
    except Panenan.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = PanenanSerializer(panenan)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PanenanSerializer(panenan, data=data)
        
    elif request.method == 'DELETE':
        panenan.delete()
        return HttpResponse(status=204)

