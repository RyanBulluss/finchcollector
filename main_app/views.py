from django.shortcuts import render

finches = [
  {'name': 'name1', 'breed': 'breed1', 'description': 'description1', 'age': 1},
  {'name': 'name2', 'breed': 'breed2', 'description': 'description2', 'age': 2},
  {'name': 'name3', 'breed': 'breed3', 'description': 'description3', 'age': 3},
  {'name': 'name3', 'breed': 'breed3', 'description': 'description3', 'age': 3},
  {'name': 'name3', 'breed': 'breed3', 'description': 'description3', 'age': 3},
  {'name': 'name3', 'breed': 'breed3', 'description': 'description3', 'age': 3},
  {'name': 'name3', 'breed': 'breed3', 'description': 'description3', 'age': 3},
  {'name': 'name3', 'breed': 'breed3', 'description': 'description3', 'age': 3},
  {'name': 'name3', 'breed': 'breed3', 'description': 'description3', 'age': 3},
  {'name': 'name3', 'breed': 'breed3', 'description': 'description3', 'age': 3},
  {'name': 'name3', 'breed': 'breed3', 'description': 'description3', 'age': 3},
  {'name': 'name3', 'breed': 'breed3', 'description': 'description3', 'age': 3},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })