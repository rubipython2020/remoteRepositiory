from django.contrib import auth, messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from institute.models import courseform, register,feedback,enquariform,entry,Student
from .forms import enquary,entry_student

import datetime
date=datetime.datetime.now()


def home(request):
    return render(request, 'htmlfile/home.html')


def contact(request):
    return render(request, 'htmlfile/contact.html')


def gallery(request):
    return render(request, 'htmlfile/gallery.html')


def Cources(request):
    if request.method == 'GET':
        return render(request, 'htmlfile/cources.html')
    else:
        name = request.POST.get('name1')
        Duration = request.POST.get('duration')
        date = request.POST.get('date')
        time = request.POST.get('time')
        t_name = request.POST.get('name2')
        exp = request.POST.get('exp1')

        data = courseform.objects.create(c_name=name, c_dur=Duration, date=date, time=time, c_trainer=t_name, exp=exp)

        data.save()

        return render(request,'htmlfile/Cources.html')


def courselist(request):
    context = {'courselist': courseform.objects.all()}

    return render(request, 'htmlfile/list.html', context)



def registration(request):
    if request.method == 'POST':
        fname1 = request.POST.get('fname')
        lname1 = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        iname = request.POST.get('iname')
        location = request.POST.get('location')

        data = register(fname=fname1, lname=lname1, username=username, email=email, password=password,  iname=iname, location=location)
        data.save()
        return redirect('register')

    context = {'register': register.objects.all()}

    return render(request, 'htmlfile/register.html', context)

def feed(request):
    if request.method=='POST':
        name=request.POST.get('name')
        rating=request.POST.get('rating')
        feed=request.POST.get('feed')
        date=datetime.datetime.now()
        data=feedback(name=name,rating=rating,feedback=feed,date=date)
        data.save()
        return  redirect('feedback')



    context = {'feed': feedback.objects.all()}
    return render(request, 'htmlfile/feedback.html', context)

def readd(request):
    context = {'feed': feedback.objects.all()}

    return render(request, 'htmlfile/read.html', context)

def enquairy_view(request):
    if request.method=='POST':
        eform = enquary(request.POST)
        if eform.is_valid():
            name=eform.cleaned_data.get('name')
            mobile=eform.cleaned_data.get('mobile')
            email=eform.cleaned_data.get('email')
            course=eform.cleaned_data.get('course')
            trainer=eform.cleaned_data.get('trainer')
            shift=eform.cleaned_data.get('shift')
            location=eform.cleaned_data.get('location')
            gender=eform.cleaned_data.get('gender')
            date = datetime.datetime.now()


            data=enquariform(
                name=name,
                mobiles=mobile,
                email=email,
                cources=course,
                trainer=trainer,
                shift=shift,
                location=location,
                gender=gender,
                date=date

            )

            data.save()
            form = enquary()
            context = {'form': form, 'Enquiry': enquariform.objects.all()}
            return render(request, 'htmlfile/enquaryform.html', context)
    else:
        form=enquary()
        context={'form': form , 'Enquiry' : enquariform.objects.all()}
        return render(request,'htmlfile/enquaryform.html',context)

    #context = {'form': enquariform.objects.all()}
    #return render(request,'htmlfile/enquaryform.html',context)

def Entry(request):
    if request.method=='POST':
        eform = entry_student(request.POST)
        if eform.is_valid():
            fname=request.POST.get('fname')
            lname=request.POST.get('lname')
            company=request.POST.get('company')
            location=request.POST.get('location')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            salary=request.POST.get('salary')
            qualification=request.POST.get('qualification')

            data1=entry(
                fname=fname,
                lname=lname,
                company=company,
                location=location,
                email=email,
                mobile=mobile,
                salary=salary,
                qualification=qualification

            )
            data1.save()
            form=entry_student()
            context={'forms':form , 'Entry' : entry.objects.all()}
            return render(request,'htmlfile/entry.html',context)

    else:
        form = entry_student()
        context = {'forms': form , 'Entry': entry.objects.all()}
        return render(request, 'htmlfile/entry.html', context)


def student(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        cname=request.POST.get('cname')
        sname=request.POST.get('sname')
        mname=request.POST.get('mname')
        email=request.POST.get('email')
        telugu=request.POST.get('telugu')
        hindi=request.POST.get('hindi')
        english=request.POST.get('english')
        math=request.POST.get('math')

        data=Student(
            fname=fname,
            lname=lname,
            cname=cname,
            sname=sname,
            mobile=mname,
            email=email,
            telugu=telugu,
            hindi=hindi,
            english=english,
            math=math

        )
        data.save()
        context = {'Studentdata': Student.objects.all()}
        return render(request,'htmlfile/studentdata.html' ,context)

    context={'Studentdata': Student.objects.all()}
    return render(request,'htmlfile/studentdata.html',context)


def update_form(request,id):
    context =  Student.objects.get(id=id)
    return render(request,'htmlfile/display.html' , {'Studentdata' : context })

def update_form_save(request,id):
    context = Student.objects.get(id=id)
    context.fname=request.POST.get('fname')
    context.lname=request.POST.get('lname')
    context.cname=request.POST.get('cname')
    context.sname=request.POST.get('sname')
    context.mobile=request.POST.get('mobile')
    context.email=request.POST.get('email')
    context.telugu=request.POST.get('telugu')
    context.hindi=request.POST.get('hindi')
    context.english=request.POST.get('english')
    context.math=request.POST.get('math')
    context.save()
    return redirect('/')


def delete(request,id):
    student=Student.objects.get(pk=id)
    student.delete()
    return redirect('/')

