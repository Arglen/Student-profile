import os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'enrollment.settings'
import sys; sys.path.insert(0, r'C:\Users\argle\.kiro\crew\workspace\borrowhood_pkgs')
django.setup()

from students.models import Student
from django.contrib.auth.models import User
from datetime import date

# superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin1234')
    print('Created superuser: admin / admin1234')

students = [
    dict(student_id='2024-00268', first_name='Mia',    middle_name='A',       last_name='Bautista',  gender='Female', date_of_birth=date(2008,7,30),  phone='0918 555 6690', email='mia.bautista@example.edu',   address='26 Katipunan Street, Mandaluyong City',    course='BSIT', year_level='2nd Year', section='St. Luke',    school_year='2025-26', guardian_name='Diana Bautista',   guardian_contact='0917 555 6651', status='Enrolled'),
    dict(student_id='2024-00234', first_name='Noah',   middle_name='P',       last_name='Dela Cruz', gender='Male',   date_of_birth=date(2007,3,12),  phone='0917 555 1234', email='noah.delacruz@example.edu',  address='15 Mabini Street, Quezon City',            course='BSIT', year_level='2nd Year', section='St. Matthew', school_year='2025-26', guardian_name='Carlos Dela Cruz', guardian_contact='0917 555 1200', status='Enrolled'),
    dict(student_id='2024-00252', first_name='Lucas',  middle_name='R',       last_name='Garcia',    gender='Male',   date_of_birth=date(2008,1,20),  phone='0916 555 5678', email='lucas.garcia@example.edu',   address='7 Rizal Ave, Pasig City',                  course='BSCS', year_level='1st Year', section='St. Luke',    school_year='2025-26', guardian_name='Rosa Garcia',      guardian_contact='0916 555 5600', status='Pending'),
    dict(student_id='2024-00279', first_name='Caleb',  middle_name='T',       last_name='Lim',       gender='Male',   date_of_birth=date(2007,9,5),   phone='0919 555 9012', email='caleb.lim@example.edu',      address='32 Orchid Street, Marikina City',          course='BSIT', year_level='2nd Year', section='St. Matthew', school_year='2025-26', guardian_name='Joseph Lim',       guardian_contact='0919 555 9000', status='Enrolled'),
    dict(student_id='2024-00341', first_name='Leah',   middle_name='C',       last_name='Navarro',   gender='Female', date_of_birth=date(2008,5,18),  phone='0912 555 3456', email='leah.navarro@example.edu',   address='10 Sampaguita Street, Caloocan City',      course='BSBA', year_level='1st Year', section='St. Luke',    school_year='2025-26', guardian_name='Maria Navarro',    guardian_contact='0912 555 3400', status='Enrolled'),
    dict(student_id='2024-00191', first_name='Ethan',  middle_name='J',       last_name='Reyes',     gender='Male',   date_of_birth=date(2007,11,2),  phone='0920 555 7890', email='ethan.reyes@example.edu',    address='5 Ilang-Ilang Street, Taguig City',        course='BSIT', year_level='3rd Year', section='St. Matthew', school_year='2025-26', guardian_name='Patricia Reyes',   guardian_contact='0920 555 7800', status='For Review'),
    dict(student_id='2024-00182', first_name='Amara',  middle_name='L',       last_name='Santos',    gender='Female', date_of_birth=date(2008,8,25),  phone='0921 555 2345', email='amara.santos@example.edu',   address='22 Acacia Street, Valenzuela City',        course='BSBA', year_level='2nd Year', section='St. Luke',    school_year='2025-26', guardian_name='Grace Santos',     guardian_contact='0921 555 2300', status='Enrolled'),
    dict(student_id='2024-00310', first_name='Sofia',  middle_name='M',       last_name='Torres',    gender='Female', date_of_birth=date(2008,2,14),  phone='0923 555 6789', email='sofia.torres@example.edu',   address='18 Narra Street, Paranaque City',          course='BSCS', year_level='1st Year', section='St. Matthew', school_year='2025-26', guardian_name='Ramon Torres',     guardian_contact='0923 555 6700', status='Enrolled'),
]

for data in students:
    obj, created = Student.objects.get_or_create(student_id=data['student_id'], defaults=data)
    print(f"{'Created' if created else 'Exists '}: {obj}")

print('\nDone. Visit http://127.0.0.1:8000/students/')
