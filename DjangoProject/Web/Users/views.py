from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect


class MyView(View):
    def get(self, request):
        if not  User.objects.filter(username='admin',).exists():
            User.objects.create_superuser(username='admin', password='django777', email='admin@admin.com')
        return redirect('admin/')