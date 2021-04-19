from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import generics

from . import models, serializers


class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    def get_queryset(self):
        qs = super(UserListView, self).get_queryset()
        if self.request.user.is_superuser:
            return qs
        return models.CustomUser.objects.filter(id=self.request.user.id)

@login_required
def dashboard(request):
    return render(request,'account/dashboard.html', {'section': 'dashboard'})
