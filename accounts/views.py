from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        remember = request.POST.get('remember')
        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None
        if user is not None:
            login(request, user)
            if not remember:
                request.session.set_expiry(0)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'accounts/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        zip_code = request.POST.get('zip_code', '').strip()
        agree = request.POST.get('agree')

        if not agree:
            messages.error(request, 'You must agree to the Terms and Privacy Policy.')
            return render(request, 'accounts/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'An account with that email already exists.')
            return render(request, 'accounts/register.html')

        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters.')
            return render(request, 'accounts/register.html')

        username = email.split('@')[0]
        base = username
        i = 1
        while User.objects.filter(username=username).exists():
            username = f"{base}{i}"
            i += 1

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=full_name.split(' ')[0] if full_name else '',
            last_name=' '.join(full_name.split(' ')[1:]) if full_name else '',
        )
        user.profile.zip_code = zip_code
        user.profile.save()
        login(request, user)
        return redirect('home')

    return render(request, 'accounts/register.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home_view(request):
    return render(request, 'accounts/home.html')


@login_required
def student_list_view(request):
    query = request.GET.get('q', '').strip()
    selected_pk = request.GET.get('selected')
    students = Student.objects.all()
    if query:
        students = (
            students.filter(last_name__icontains=query)
            | students.filter(first_name__icontains=query)
            | students.filter(student_id__icontains=query)
        )
    selected = None
    if selected_pk:
        try:
            selected = Student.objects.get(pk=selected_pk)
        except Student.DoesNotExist:
            pass
    if selected is None and students.exists():
        selected = students.first()
    return render(request, 'accounts/student_list.html', {
        'students': students,
        'query': query,
        'selected': selected,
    })


@login_required
def student_detail_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'accounts/student_detail.html', {'student': student})
