from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .models import Flight, Passenger

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
        return render(request, "flights/flight.html", {
            "flight": flight,
            "passengers": flight.passengers.all(),
            "non_passengers": Passenger.objects.exclude(flights=flight).all()
        })
    except:
        return HttpResponseBadRequest("Flight not found")

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return redirect("flights:flight", flight_id=flight_id)
