import json
from django.http import HttpRequest,HttpResponse
from .models import User
from django.shortcuts import get_object_or_404


# >>> import json
# >>> li=[1,2,4]
# >>> json.dumps(li) 
# '[1, 2, 4]'
# >>> out =json.dumps(li) 
# >>> type(out) 
# <class 'str'>
# >>> out=json.loads(li) 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "C:\Users\gthakur\AppData\Local\Programs\Python\Python38-32\lib\json\__init__.py", line 341, in loads
#     raise TypeError(f'the JSON object must be str, bytes or bytearray, '
# TypeError: the JSON object must be str, bytes or bytearray, not list
# >>> out=json.loads(out) 
# >>> type(out) 
# <class 'list'>
# >>> out
# [1, 2, 4]
# >>>

def users(request:HttpRequest) -> HttpResponse:

    if request.method == 'GET':
        
        users=User.objects.all()

            #return HttpResponse(users) this will have the Objects not the plain Txt 
            # we need to chnage that so serialize is used 
        serialized_users = [ {
            "id":user.id,
            "name":user.name,
            "email":user.email,
            "age":user.age,
        } for user in users]
            # return HttpResponse(serialized_users) this still a object not a string 

            #inport jason 
        return HttpResponse(json.dumps(serialized_users))
    if request.method == 'POST':
        body=json.loads(request.body)
        user=User(name=body['name'],email=body['email'],age=body['age'])## just with this ID will not be available since its not saved 
        user.save()
        return HttpResponse(json.dumps({'id':user.id,'name':user.name}))
#currently we are converting lots of string to dictionary / json and jsaon to string
#we need a serializer for that , so Django rest framework provides those functionality
def get_update_or_delete(request:HttpRequest,id:int) -> HttpResponse:


    if request.method == 'GET':
        # user=User.objects.get(id=id)
        user=get_object_or_404(User,id=id)
        return HttpResponse(json.dumps({'id':user.id,'name':user.name,'age':user.age,'email':user.email}))

    if request.method=='PUT':
        body=json.loads(request.body)
        # user=User.objects.get(id=id)
        user=get_object_or_404(User,id=id)
        user.name=body['name']
        user.email=body['email']
        user.age=body['age']
        user.save()
        return HttpResponse(json.dumps({'id':user.id,'name':user.name,'age':user.age,'email':user.email}))

    if request.method=='DELETE':
        # user=User.objects.get(id=id)
        user=get_object_or_404(User,id=id)
        user.delete()
        return HttpResponse(json.dumps({'id':user.id,'name':user.name}))



