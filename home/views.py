from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("""<h1>Hey I am Django server.<h1>
#         <p>Hey this is coming from Django Server.<p>
#         <hr>
#         <h3 style="color:red">Hope you are loving it.<h3>
                        
#     """)      # not feasible for complex websites

def home(request):
    return render(request, "home/index.html")   # returning html file

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hey this is success page.<h1>")
