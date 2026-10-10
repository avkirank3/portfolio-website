from django.http import JsonResponse
from django.urls import path
from .data import portfolio_data


def profile(request):
    return JsonResponse(portfolio_data)


urlpatterns = [
    path("profile/", profile, name="profile"),
]
