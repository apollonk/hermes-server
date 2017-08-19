from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
import networkx as nx
import uuid

class Element:
    """Class for HERMES elements"""

    def __init__(self, name="Unnamed", notes="", etype="element"):
        """Element constructor:
        id (uuid)
        name (description string, string value of object)
        notes (long [rich?] text)
        type (element / superelement / ?)"""

        # Consider creating UUID from name and (?) instead of random
        self.uuid = uuid.uuid4().hex
        self.name = name
        self.notes = notes
        self.type = etype

    def __str__(self):
        return self.name

    def getUUID():
        return self.uuid

    def __hash__(self):
        return hash(self.uuid)

    def set_name(self, name):
        self.name = unicode(name)
        return self.name

class Function:
    """Class for HERMES functions"""

    def __init__(self, source, target, name="Unnamed", 
                       notes="", ftype="undefined"):

        """Element constructor:
        id (uuid)
        name (description string, string value of object)
        notes (long [rich?] text)
        type (useful / harmful / insufficient / excessive)
        source (source element)
        target (target element)"""

        self.uuid = uuid.uuid5(uuid.NAMESPACE_DNS,source.uuid+target.uuid).hex
        self.name = name
        self.notes = notes
        self.type = ftype
        self._source = source
        self.sourceId = source.uuid
        self._target = target
        self.targetId = target.uuid

    def __str__(self):
        return str(self._source) + " -- " + self.name + \
               " --> " + str(self._target)

    def __hash__(self):
        return hash(self.uuid)



#G = nx.Graph()
#
#G.add_nodes_from(['Hair Dryer', 'Air Heating System',
#                  'Power and Control System', 'Blower System',
#                  '(Wet) Hair', 'Mains', 'Air (Ambient)',
#                  'Operator'])
#
#G.add_edges_from([('Air Heating System', '


def test1():
    e1 = Element("Dear Watson")
    e2 = Element("Atomic")
    e3 = Element("Fifth")
    
    f1 = Function(e1, e2, "Elementarifies")
    f2 = Function(e3, e2, "Badabooms", e1, e2)
    
    print(e1)
    print(e2)
    print(e3)
    print(f1)
    print(f2)

def test2():
    e = [ Element('Hair Dryer'),
          Element('Air Heating System'),
          Element('Power and Control System'),
          Element('Blower System'),
          Element('(Wet) Hair'),
          Element('Mains'),
          Element('Air (Ambient)'),
          Element('Operator') ]

    f = [ Function(e[0], e[1], "Heats Air"),
          Function(e[2], e[1]),
          Function(e[2], e[3], "Controls"),
          Function(e[3], e[0], "Blows Air"),
          Function(e[0], e[4], "Dries"),
          Function(e[5], e[0], "Powers"),
          Function(e[6], e[0], "Provides Heating Medium"),
          Function(e[7], e[0], "Controls") ]

    for function in f:
        print(function)

    #import jsonpickle
    #print jsonpickle.encode( { 'elements': e, 'functions': f }, unpicklable=False, max_depth=3 )

if __name__ == '__main__':
    print("Test 1:")
    print
    test1()
    print

    print("Test 2:")
    print
    test2()
    print
