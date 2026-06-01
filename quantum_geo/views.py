from django.shortcuts import render

def home(request):          return render(request, 'quantum_geo/home.html')
def hilbert(request):       return render(request, 'quantum_geo/hilbert.html')
def bloch(request):         return render(request, 'quantum_geo/bloch.html')
def gates(request):         return render(request, 'quantum_geo/gates.html')
def entanglement(request):  return render(request, 'quantum_geo/entanglement.html')
def measurement(request):   return render(request, 'quantum_geo/measurement.html')