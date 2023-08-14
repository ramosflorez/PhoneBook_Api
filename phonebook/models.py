from django.db import models

class TypesOfContact(models.Model):
    ID_Type = models.AutoField(primary_key=True)
    TypeName = models.CharField(max_length=100)

class Contacts(models.Model):
    ID_Contact = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Phone = models.BigIntegerField(blank=True)
    Email = models.TextField(blank=True)
    Comment = models.TextField(blank=True)
    ID_Type = models.ForeignKey(TypesOfContact, on_delete=models.CASCADE)

class Persons(models.Model):
    ID_Person = models.AutoField(primary_key=True)
    ID_Contact = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    Lastname = models.CharField(max_length=100, blank=True)
    BirthDate = models.DateField(blank=True)

class Organizations(models.Model):
    ID_Organization = models.AutoField(primary_key=True)
    ID_Contact = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    OrganizationType = models.CharField(max_length=100, blank=True)
    Address = models.CharField(max_length=100, blank=True)
    FoundationDate = models.DateField(blank=True)


