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
    peoples = [
        {'name' : "Mayank Kanojia", 'age' : 21},
        {'name' : "Abhijeet Gupta", 'age' : 26},
        {'name' : "Rohan Verma", 'age' : 16},
        {'name' : "John Doe", 'age' : 14},
        {'name' : "Sandeep Sharma", 'age' : 32},
    ]

    for people in peoples:
        if people['age'] > 18:
            print("Yes")

    # for people in peoples:
    #     print(people)

    # text = """
    #     Lorem, ipsum dolor sit amet consectetur adipisicing elit. Vel doloribus voluptatibus doloremque exercitationem nam 
    #     sed incidunt quaerat sapiente maxime dolore, aliquam iusto alias quos veniam repudiandae inventore, 
    #     deleniti animi modi?
    # """

    vegetables = ['Pumpkin', 'Tomato', 'Potato']

    return render(request, "home/index.html", context = {'page' : 'Django Tutorial 2024', 'peoples': peoples, 'vegetables' : vegetables})   # returning html file


def about(request):
    context = {'page' : 'About'}
    return render(request, "home/about.html", context)   # returning html file


def contact(request):
    context = {'page' : 'Contact'}
    return render(request, "home/contact.html", context)   # returning html file

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hey this is success page.<h1>")
