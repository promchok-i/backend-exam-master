from django.core.management.base import BaseCommand
from apis.models import School, Classroom, Teacher, Student
import random


class Command(BaseCommand):
    help = 'Generate sample data for School, Classroom, Teacher, and Student'

    def handle(self, *args, **kwargs):
        # Remove existing records
        self.stdout.write(self.style.NOTICE('Removing existing records...'))
        
        Teacher.objects.all().delete()
        Student.objects.all().delete()
        Classroom.objects.all().delete()
        School.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Successfully removed existing records.'))
        
        # Create 5 schools
        for i in range(5):
            School.objects.create(
                name=f'School {i+1}',
                abbrevation=f'SCH{i+1}',
                address=f'123 Street {i+1}, City, Country, {random.randint(10000, 99999)}'
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created School {i+1}'))

        # Create 10 classrooms
        schools = list(School.objects.all())
        for i in range(10):
            school = random.choice(schools)
            Classroom.objects.create(
                grade=random.choice(['K1', 'K2', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12']),
                room=f'{i+1}',
                school=school
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Classroom {i+1}'))

        # Create 20 teachers
        for i in range(20):
            # Randomly select a school
            school = random.choice(schools)
            
            # Get classrooms belonging to the selected school
            classrooms = list(Classroom.objects.filter(school=school))
            
            if not classrooms:
                self.stdout.write(self.style.WARNING(f'No classrooms available for School {school.name}. Skipping teacher creation.'))
                continue
            
            teacher = Teacher.objects.create(
                first_name=f'First{i+1}',
                last_name=f'Last{i+1}',
                gender=random.choice(['M', 'F']),
                school=school
            )
            
            # Assign 1 to 3 random classrooms from the selected school to the teacher
            random_classrooms = random.sample(classrooms, k=random.randint(1, min(3, len(classrooms))))
            teacher.classroom.set(random_classrooms)
            
            self.stdout.write(self.style.SUCCESS(f'Successfully created Teacher {i+1}'))

        # Create 50 students
        classrooms = list(Classroom.objects.all())
        for i in range(50):
            classroom = random.choice(classrooms)
            Student.objects.create(
                first_name=f'First{i+1}',
                last_name=f'Last{i+1}',
                gender=random.choice(['M', 'F']),
                classroom=classroom,
                school=classroom.school
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Student {i+1}'))
