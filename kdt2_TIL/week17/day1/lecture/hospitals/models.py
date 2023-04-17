'''
from django.db import models


class Doctor(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'
    
    
class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.TextField()
    
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
    

# doctor1 = Doctor.objects.create(name='alice')
# doctor2 = Doctor.objects.create(name='bella')
# patient1 = Patient.objects.create(name='carol', doctor=doctor1)
# patient2 = Patient.objects.create(name='dane', doctor=doctor2)
'''

'''
from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


# 외래키 삭제
class Patient(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# 중개모델 작성
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'


# 코드 예시
doctor1 = Doctor.objects.create(name='alice')
patient1 = Patient.objects.create(name='carol')

Reservation.objects.create(doctor=doctor1, patient=patient1)

doctor1.reservation_set.all()
patient1.reservation_set.all()

patient2 = Patient.objects.create(name='dane')
Reservation.objects.create(doctor=doctor1, patient=patient2)
'''

'''
from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    # ManyToManyField 작성
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# Reservation Class 주석 처리


# 코드 예시
# doctor1 = Doctor.objects.create(name='alice')
# patient1 = Patient.objects.create(name='carol')
# patient2 = Patient.objects.create(name='dane')

# patient1.doctors.add(doctor1)
# patient1.doctors.all()
# doctor1.patient_set.all()

# doctor1.patient_set.add(patient2)
# doctor1.patient_set.all()
# patient2.doctors.all()
# patient1.doctors.all()

# doctor1.patient_set.remove(patient1)
# doctor1.patient_set.all()
# patient1.doctors.all()

# patient2.patient_set.remove(doctor1)
# patient2.doctors.all()
# doctor1.patient_set.all()
'''

from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'


# 코드 예시
# doctor1 = Doctor.objects.create(name='alice')
# patient1 = Patient.objects.create(name='carol')
# patient2 = Patient.objects.create(name='dane')

# # 1. Reservation class를 통한 예약 생성
# reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
# reservation1.save()
# doctor1.patient_set.all()
# patient1.doctors.all()

# # 2. Patient 객체를 통한 예약 생성
# patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})
# doctor1.patient_set.all()
# patient2.doctors.all()

# doctor1.patient_set.remove(patient1)
# patient2.doctors.remove(doctor1)
