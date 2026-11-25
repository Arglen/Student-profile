from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student


@login_required
def student_list(request):
    query = request.GET.get('q', '').strip()
    selected_pk = request.GET.get('selected')
    qs = Student.objects.all()
    if query:
        qs = qs.filter(last_name__icontains=query) | qs.filter(first_name__icontains=query) | qs.filter(student_id__icontains=query)
    selected = None
    if selected_pk:
        try:
            selected = Student.objects.get(pk=selected_pk)
        except Student.DoesNotExist:
            pass
    if selected is None and qs.exists():
        selected = qs.first()
    return render(request, 'students/list.html', {
        'students': qs,
        'query': query,
        'selected': selected,
    })


@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/detail.html', {'student': student})
