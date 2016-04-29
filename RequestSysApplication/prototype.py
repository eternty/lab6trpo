import copy
from RequestSysApplication.models import MyRequest, Department

class Prototype:
    def __init__(self):
        self._objects = {}



    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update inner attributes dictionary"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

    def new (self):
        obj = Request.objects.create()
        obj.save()
        return oj.id