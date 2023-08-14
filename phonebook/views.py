from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.db.models import F
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TypesOfContact, Contacts, Persons, Organizations
from .serializer import TypesOfContactSerializer, ContactsSerializer, PersonsSerializer, OrganizationsSerializer

# Create your views here.
@csrf_exempt
def ContactsApi(request):
    if request.method=='GET':
        contacts = Contacts.objects.all().order_by('ID_Contact')
        contacts_serializer=ContactsSerializer(contacts, many=True)
        return JsonResponse(contacts_serializer.data, safe=False)
    elif request.method=='POST':
        contacts_data=JSONParser().parse(request)
        contacts_serializer=ContactsSerializer(data=contacts_data['contact'])
        if contacts_serializer.is_valid():
            contact = contacts_serializer.save()
            type_id=contacts_data['contact']['ID_Type']
            response_data = {
                "message": "Added Successfully",
                "type": "success"}
            if type_id== 1:
                person_data=contacts_data['person']
                person_data['ID_Contact']=contact.ID_Contact
                person_serializer=PersonsSerializer(data=person_data)
                if person_serializer.is_valid():
                    person_serializer.save()
                    return JsonResponse(response_data,safe=False)
                else:
                    contact.delete()
                    return JsonResponse(person_serializer.errors, safe=False)
            if type_id== 2:
                organization_data=contacts_data['organization']
                organization_data['ID_Contact']=contact.ID_Contact
                organization_serializer=OrganizationsSerializer(data=organization_data)
                if organization_serializer.is_valid():
                    organization_serializer.save()
                    return JsonResponse(response_data,safe=False)
                else:
                    contact.delete()
                    return JsonResponse(organization_serializer.errors, safe=False)  
        return JsonResponse(contacts_serializer.errors,safe=False)
    
    elif request.method=='PUT': 
        contacts_data=JSONParser().parse(request)
        contact= Contacts.objects.get(ID_Contact=contacts_data['contact']['ID_Contact'])
        contacts_serializer=ContactsSerializer(contact, data=contacts_data['contact'])
        if contacts_serializer.is_valid():
            type_id=contacts_data['contact']['ID_Type']
            response_data = {
                "message": "Updated Successfully",
                "type": "success"
            }
            if type_id ==1:
                person_data=contacts_data['person']
                person= Persons.objects.get(ID_Contact=person_data['ID_Contact'])
                print('contact:', contact,"person:", person)
                if contacts_data['contact']['ID_Contact']==person_data['ID_Contact']:
                    person_serializer=PersonsSerializer(person,data=person_data)
                    if person_serializer.is_valid():
                        contacts_serializer.save()
                        person_serializer.save()
                        return JsonResponse(response_data,safe=False)
                    else:
                        return JsonResponse(person_serializer.errors, safe=False)
                else:
                    return JsonResponse("the contact id is not the same", safe=False)

            if type_id ==2:
                organization_data=contacts_data['organization']
                organization= Organizations.objects.get(ID_Contact=organization_data['ID_Contact'])
                print('contact:', contact,"organization:", organization)
                if contacts_data['contact']['ID_Contact']==organization_data['ID_Contact']:
                    organization_serializer=OrganizationsSerializer(organization,data=organization_data)
                    if organization_serializer.is_valid():
                        contacts_serializer.save()
                        organization_serializer.save()
                        return JsonResponse(response_data,safe=False)
                    else:
                        return JsonResponse(organization_serializer.errors, safe=False)
                else:
                    return JsonResponse("the contact id is not the same", safe=False)   
                
    elif request.method == 'DELETE':

        contacts_data=JSONParser().parse(request)
        print('contacts_data', contacts_data)
        contact = Contacts.objects.get(ID_Contact=contacts_data['ID_Contact'])
        print('contact', contact)
        contact.delete()
        response_data = {
                "message": "Deleted Successfully",
                "type": "success"
        }
        return JsonResponse(response_data,safe=False)

@csrf_exempt
def TypeofContact(request):
    if request.method=='POST':
        type_data=JSONParser().parse(request)
        type_serializer=TypesOfContactSerializer( data=type_data)
        if type_serializer.is_valid():
            type_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
    elif request.method=='GET':
        typeContact = TypesOfContact.objects.all()
        typeContact_serializer=TypesOfContactSerializer(typeContact, many=True)
        return JsonResponse(typeContact_serializer.data, safe=False)
    return JsonResponse(type_serializer.errors,safe=False)



@csrf_exempt
def PersonApi(request):
    if request.method=='GET':
        persons=Persons.objects.all()
        persons_serializer=PersonsSerializer(persons,many=True)
        return JsonResponse(persons_serializer.data, safe=False)
    


@csrf_exempt
def OrganizationApi(request):
    if request.method=='GET':
        organizations=Organizations.objects.all()
        organizations_serializer=OrganizationsSerializer(organizations,many=True)
        return JsonResponse(organizations_serializer.data, safe=False)
    



        
        







