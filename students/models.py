from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Representative(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model): # If required delete blank=True
    DEPARTMENTS = (
        ('CS','Computer Science'),
        ('ACC','Accounting'),
        ('GF','Games&Fun'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    identityNumber = models.CharField(max_length=10, blank=True) # Can be changed to Float
    address = models.CharField(max_length=200, blank=True)
    department = models.CharField(max_length=3, choices=DEPARTMENTS)
    average_grade = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    representative = models.ForeignKey(Representative, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.identityNumber:
            return f"{self.first_name} ({self.identityNumber})"
        return self.first_name

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))

                if field.verbose_name != 'representative'

                else
                    (field.verbose_name,
                    Representative.objects.get(pk=field.value_from_object(self)).name)

                for field in self.__class__._meta.fields[1:]
            ]