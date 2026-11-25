from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    zip_code = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.user.username} profile"


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()


YEAR_LEVEL_CHOICES = [
    ('1st Year', '1st Year'),
    ('2nd Year', '2nd Year'),
    ('3rd Year', '3rd Year'),
    ('4th Year', '4th Year'),
]

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

CIVIL_STATUS_CHOICES = [
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Other', 'Other'),
]


class Student(models.Model):
    # Personal Info
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    civil_status = models.CharField(max_length=10, choices=CIVIL_STATUS_CHOICES, blank=True)
    address = models.TextField(blank=True)
    photo = models.ImageField(upload_to='students/', null=True, blank=True)

    # Background / Academic Info
    course = models.CharField(max_length=100, blank=True)
    year_level = models.CharField(max_length=20, choices=YEAR_LEVEL_CHOICES, blank=True)
    section = models.CharField(max_length=20, blank=True)
    school_year = models.CharField(max_length=20, blank=True)
    guardian_name = models.CharField(max_length=150, blank=True)
    guardian_contact = models.CharField(max_length=30, blank=True)
    previous_school = models.CharField(max_length=200, blank=True)
    date_enrolled = models.DateField(null=True, blank=True)

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
