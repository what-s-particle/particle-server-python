from django.http import HttpResponse

from particle.protos import addressbook_pb2


def index(request):
    # return HttpResponse("Hello world. You're at the the moments index.")
    person = addressbook_pb2.Person()
    person.id = 42
    person.name = "Test Name"
    person.email = "testname@test.com"

    return HttpResponse(person.SerializeToString(), content_type="application/octet-stream")
