from django.shortcuts import render
from registeruser.models import Userreg
from django.contrib import messages

def Userregistraion(request):
	if request.method=="POST":
		if request.POST.get('uname') and request.POST.get('umail') and request.POST.get('pnum') and request.POST.get('mtstatus') and request.POST.get('gender'):
			saverecorde=Userreg()
			saverecorde.uname=request.POST.get('uname')
			saverecorde.umail=request.POST.get('umail')
			saverecorde.pnum=request.POST.get('pnum')
			saverecorde.mtstatus=request.POST.get('mtstatus')
			saverecorde.gender=request.POST.get('gender')
			saverecorde.save()
			messages.success(request,"New User Registration Details Saved Successfully..!")
			return render(request,'Index.html')
	else:
		return render(request,"Index.html")