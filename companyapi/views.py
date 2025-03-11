from django.http import HttpResponse ,JsonResponse

def home_page(request):
    friend = [
        'aniket',
        'pankaj',
        'pratik'
    ]
    return JsonResponse(friend,safe=False)  

