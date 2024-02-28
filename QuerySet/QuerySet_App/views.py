from django.shortcuts import render
from .models import Student, Teacher


# Create your views here.


def home(request):
    student_data = Student.objects.all()  # retrive all objects

    stu_filter = Student.objects.filter(marks=88)

    stu_exclude = Student.objects.exclude(marks=32)

    stu_orderby = Student.objects.order_by('-marks')
    # -marks - desc order  # ? - random oder # by default asc

    stu_reverse = Student.objects.order_by('id').reverse()[:5]

    stu_values = Student.objects.values()  # return dictionary
    stu_values_list = Student.objects.values('id', 'name')  # return tuple

    stu_distinct = Student.objects.values('marks').distinct()

    stu_using = Student.objects.using('default')

    stu_none = Student.objects.none()

    # stu_date = Student.objects.dates('pass_date','month') #date ex

    # second table ex of union
    qs1 = Student.objects.values_list('city', 'name', named=True)
    qs2 = Teacher.objects.values_list('city', 'name', named=True)
    result_union = qs2.union(qs1)

    # second table ex of Intersection
    qs1 = Student.objects.values_list('city', 'name', named=True)
    qs2 = Teacher.objects.values_list('city', 'name', named=True)
    result_intersection = qs2.intersection(qs1)  # what is common between two table

    # second table ex of difference - we will not get teacher table data
    qs1 = Student.objects.values_list('city', 'name', named=True)
    qs2 = Teacher.objects.values_list('city', 'name', named=True)
    result_difference = qs2.difference(qs1)

    # print("Return:", student_data)
    print("SQL Query:", stu_using.query)
    return render(request, 'querySet/home.html',
                  {'students': result_difference})
