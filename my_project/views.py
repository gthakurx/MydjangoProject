import json
from django.http import HttpRequest,HttpResponse
from .models import User

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
        serialized_users = [ user.name for user in users]
            # return HttpResponse(serialized_users) this still a object not a string 

            #inport jason 
        return HttpResponse(json.dumps(serialized_users))
    if request.method == 'POST':
        body=json.loads(request.body)
        user=User(name=body['name'],email=body['email'],age=body['age'])## just with this ID will not be available since its not saved 
        user.save()
        return HttpResponse(json.dumps({'id':user.id,'name':user.name}))

