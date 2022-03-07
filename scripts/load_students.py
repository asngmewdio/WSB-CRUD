from students.models import Student
import csv


def run():
    with open('students/students.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Student.objects.all().delete()

        for row in reader:
            print(row)

            student = Student(first_name=row[0],
                        last_name=row[1],
                        identityNumber=row[2],
                        address=row[3],
                        department=row[4],
                        average_grade=row[5],
            )
            student.save()