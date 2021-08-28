import json
def complex_num(object):
    if "complex" in object:
        return complex(object["real"],object["img"])
    return object
complex_object=json.loads('{"complex":true,"real":4,"img":5}',object_hook=complex_num)
simple_object=json.loads('{"real":4,"img":5}',object_hook=complex_num)
print(complex_object)
print(simple_object)
print('_____________________________________________________________________')
import json
def complex_num(object):
    if "complex" in object:
        return complex(object["real"],object["img"])
    return object
complex_object=json.loads('{"complex":true,"real":4,"img":5}')
simple_object=json.loads('{"real":4,"img":5}')
print(complex_object)
print(simple_object)