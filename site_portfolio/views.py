from django.shortcuts import render

# Create your views here.
def home(request):
    eu = {
        'nome': 'Mayara',
        'altura': 1,65 
        'conhecimentos':['html', 'css','js','python'],
        'endereço':{
            'cidade':'São paulo',
            'pais':'brasil',
            'planeta':'marte'
        }
    }

    return render(request, 'index.html', {'eu':eu})