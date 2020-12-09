from django.shortcuts import redirect, render
from .models import Dojo, Ninja
 
def index(request):
  print('\n==== index ====')
  all_the_dojos = Dojo.objects.all()
  
  first = "Dojo.objects.get(id="
  last = ").ninjas.count()"
  # Dojo.objects.get(id=dojo.id).ninjas.count()  
  
  context = {
    "all_the_dojos" : all_the_dojos,
    'first': first,
    'last' : last,
  }
  return render(request, 'index.html', context)



def add_dojo(request):
  print('\n------- inside form DOJO -----')
  if request.method == "POST":
    print('=== GOT POST ===')
    # check if all fields are filled before db enter:
    if request.POST.get('name') and request.POST.get('city') and request.POST.get('state'):
      print('✅ all POST fields ok')
        
      print(request.POST,'\n')
      
      form_name = request.POST['name']
      form_city = request.POST['city']
      form_state = request.POST['state']
      
      Dojo.objects.create(name=form_name, city=form_city, state=form_state)
      print('✍ DOJO writen in DB')
  return redirect('/')


def add_ninja(request):
  print('\n------- inside form NINJA -----')
  if request.method == "POST":
    print('=== POST OK ===')
    print(request.POST,'\n')
    
    form_first_name = request.POST['first_name']
    form_last_name = request.POST['last_name']
    form_dojo_id = request.POST['dojo_id']
    
    # Dojo.objects.get(id=2)
    # Ninja.objects.create(first_name="Mario", last_name="Bro", dojo=Dojo.objects.get(id=3))
    
    Ninja.objects.create(first_name=form_first_name, last_name=form_last_name, dojo=Dojo.objects.get(id=form_dojo_id))
  return redirect('/')

def delete_dojo(request, url_id):
  print(f"---- DELETING dojo url {url_id}")
  
  Dojo.objects.get(id=url_id).delete()
  
  return redirect('/')