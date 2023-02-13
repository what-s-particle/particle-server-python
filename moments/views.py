from django.http import HttpResponse

from particle.protos.merge import particle_pb2 as particle


def index(request):
    # return HttpResponse("Hello world. You're at the the moments index.")
    person = particle.Person()
    person.id = 42
    person.name = "Test Name"
    person.email = "testname@test.com"

    return HttpResponse(person.SerializeToString(), content_type="application/octet-stream")
