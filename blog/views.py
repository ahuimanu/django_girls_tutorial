from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_list(request):
    # return HttpResponse("HI, this is from the Django Girls Tutorial")
    return render(request, 'blog/post_list.html', {})    
