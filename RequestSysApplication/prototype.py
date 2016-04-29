import copy
from RequestSysApplication.models import MyRequest, Department

class Prototype:
    def __init__(self):
        self._objects = {}
        self.igor_was_here = True

    def clone(self, name, **attr):
        """Clone a registered object and update inner attributes dictionary"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

    def clon_master(self):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

    def was_igor_here():
        return hasattr(self, 'igor_was_here') and self.igor_was_here


if __name__ == "__main__":
    p = Prototype()
    print(p.was_igor_here())
