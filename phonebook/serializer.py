from rest_framework import serializers
from .models import TypesOfContact, Contacts, Persons, Organizations

class TypesOfContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypesOfContact
        fields = '__all__'

class ContactsSerializer(serializers.ModelSerializer):
    ContactType = serializers.SerializerMethodField()
    class Meta:
        model = Contacts
        fields = ['ID_Contact', 'Name', 'ContactType', 'Phone', 'Email','Comment','ID_Type']
    def get_ContactType(self, obj):
        return obj.ID_Type.TypeName 
        

class PersonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = '__all__'

class OrganizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = '__all__'
