from django.db import models

GENDER_CHOICES = [('Male','Male'),('Female','Female'),('Other','Other')]
YEAR_CHOICES   = [('1st Year','1st Year'),('2nd Year','2nd Year'),('3rd Year','3rd Year'),('4th Year','4th Year')]
CIVIL_CHOICES  = [('Single','Single'),('Married','Married'),('Other','Other')]
STATUS_CHOICES = [('Enrolled','Enrolled'),('Pending','Pending'),('For Review','For Review'),('Inactive','Inactive')]


class Student(models.Model):
    # Personal
    student_id   = models.CharField(max_length=20, unique=True)
    first_name   = models.CharField(max_length=100)
    middle_name  = models.CharField(max_length=100, blank=True)
    last_name    = models.CharField(max_length=100)
    gender       = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    date_of_birth= models.DateField(null=True, blank=True)
    civil_status = models.CharField(max_length=15, choices=CIVIL_CHOICES, blank=True)
    phone        = models.CharField(max_length=20, blank=True)
    email        = models.EmailField(blank=True)
    address      = models.TextField(blank=True)

    # Academic
    course       = models.CharField(max_length=100, blank=True)
    year_level   = models.CharField(max_length=20, choices=YEAR_CHOICES, blank=True)
    section      = models.CharField(max_length=30, blank=True)
    school_year  = models.CharField(max_length=20, blank=True)
    previous_school = models.CharField(max_length=200, blank=True)
    date_enrolled= models.DateField(null=True, blank=True)
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Enrolled')

    # Guardian
    guardian_name    = models.CharField(max_length=150, blank=True)
    guardian_contact = models.CharField(max_length=30, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name}, {self.first_name} ({self.student_id})"

    @property
    def full_name(self):
        parts = [self.first_name]
        if self.middle_name:
            parts.append(self.middle_name[0] + '.')
        parts.append(self.last_name)
        return ' '.join(parts)

    @property
    def initials(self):
        return (self.first_name[:1] + self.last_name[:1]).upper()
