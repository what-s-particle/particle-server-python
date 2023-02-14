from django.http import HttpResponse
from google.protobuf import json_format

from particle.protos.particle import Person, AddressBook


def index(request):
    # return HttpResponse("Hello world. You're at the the moments index.")
    people = [
        Person(id=42, name="Test Name", email="testname@test.com"),
        Person(id=43, name="Test Name 1", email="testname1@test.com")
    ]
    address_book = AddressBook(people=people)

    if request.content_type == "application/octet-stream":
        return HttpResponse(address_book.SerializeToString(), content_type="application/octet-stream")
    else:
        return HttpResponse(json_format.MessageToJson(address_book), content_type="application/json")
