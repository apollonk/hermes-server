from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
import networkx as nx
import uuid
from pprint import pprint

class Element:
    """Class for HERMES elements"""

    def __init__(self, name="Unnamed", notes="", etype="element", system=None):
        """Element constructor:
        id (uuid)
        name (description string, string value of object)
        notes (long [rich?] text)
        etype (element / superelement / ?)"""

        # Consider creating UUID from name and (?) instead of random
        self.uuid = uuid.uuid4().hex
        self.name = name
        self.notes = notes
        self.etype = etype
        self.system = system

    def __str__(self):
        return self.name if self.system is None else self.system.get_hierarchy_string() + ":" + self.name

    def getUUID():
        return self.uuid

    def __hash__(self):
        return hash(self.uuid)

    def set_name(self, name):
        self.name = unicode(name)
        return self.name

    def set_system(self, system):
        self.system = system
        return self.system

class Function:
    """
    Class for HERMES functions. Functions can only be defined
    between elements, never systems or other functions.
    """

    def __init__(self, source, target, name="Unnamed", 
                       notes="", ftype="undefined"):

        """Element constructor:
        id (uuid)
        name (description string, string value of object)
        notes (long [rich?] text)
        ftype (useful / harmful / insufficient / excessive)
        source (source element)
        target (target element)"""

        self.uuid = uuid.uuid5(uuid.NAMESPACE_DNS,source.uuid+target.uuid).hex
        self.name = name
        self.notes = notes
        self.ftype = ftype
        self._source = source
        self.sourceId = source.uuid
        self._target = target
        self.targetId = target.uuid

    def __str__(self):
        return str(self._source) + " -- " + self.name + \
               " --> " + str(self._target)

    def __hash__(self):
        return hash(self.uuid)

class System:
    """
    Class for HERMES systems.
    Systems in the HERMES model are groups comprising of other
    systems and elements.

    Each HERMES model includes at
    least the following systems:
    1. The System
    2. The Super-system

    These two systems are part of another, top-level
    system which is also created by default and represents
    the entire model.

    Systems are probably a true tree structure.
    """

    def __init__(self, name="Unnamed", parent_system=None,
                       notes=""):

        """System constructor:
        id (uuid)
        name (description string, string value of object)
        notes (long [rich?] text)"""

        # Consider creating UUID from name and (?) instead of random
        self.uuid = uuid.uuid4().hex
        self.name = name
        self.parent_system = parent_system
        self.notes = notes
        self.elements = []
        self.systems = []

        # Maintain index of elements in system?

    def __str__(self):
        return self.name

    def getUUID():
        return self.uuid

    def __hash__(self):
        return hash(self.uuid)

    def set_name(self, name):
        self.name = unicode(name)
        return self.name

    def get_name(self):
        return self.name

    def set_parent_system(self, system):
        """Re-defines the higher level system that this system belongs to"""
        self.parent_system = system
        return system

    def get_parent_system(self):
        """Returns the higher level system that this system belongs to"""
        return self.parent_system

    def add_element(self, element):
        """Adds an element to the diagram, mapped to this system"""
        #TODO: We shouldn't depend on keeping the two properties aligned maybe?
        element.set_system(self)
        self.elements.append(element)
        return element

    def get_elements(self):
        """Returns list of elements in the diagram mapped to this system"""
        return self.elements

    def get_hierarchy(self):
        """Returns list of all parent systems from this system to the top level"""
        # TODO: There must be a better, more pythonic way to do this
        hierarchy = []
        current_system = self
        while current_system is not None:
            # Prepend in order to get the correct order
            hierarchy[:0] = [ current_system ]
            current_system = current_system.get_parent_system()
        return hierarchy

    def get_hierarchy_string(self):
        return ":".join(map(str, self.get_hierarchy()))


    #def get_child_systems(self):
    #    """Returns a list of systems that belong to this system"""

    def add_system(self, system):
        """Adds a sub-system to this system"""
        #TODO: We shouldn't depend on keeping the two properties aligned maybe?
        system.set_parent_system(self)
        self.systems.append(system)
        return system


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

def test3():
    fad = System("Test FAD")
    s = fad.add_system(System("System"))
    ss = fad.add_system(System("Super-System"))

    e = [ s.add_element(Element('Hair Dryer')),
          s.add_element(Element('Air Heating System')),
          s.add_element(Element('Power and Control System')),
          s.add_element(Element('Blower System')),
          ss.add_element(Element('(Wet) Hair')),
          ss.add_element(Element('Mains')),
          ss.add_element(Element('Air (Ambient)')),
          ss.add_element(Element('Operator')) ]

    f = [ Function(e[0], e[1], "Heats Air"),
          Function(e[2], e[1]),
          Function(e[2], e[3], "Controls"),
          Function(e[3], e[0], "Blows Air"),
          Function(e[0], e[4], "Dries"),
          Function(e[5], e[0], "Powers"),
          Function(e[6], e[0], "Provides Heating Medium"),
          Function(e[7], e[0], "Controls") ]

    print(fad.get_hierarchy_string())
    print(s.get_hierarchy_string())
    print(ss.get_hierarchy_string())

    for function in f:
        print(function)


if __name__ == '__main__':
    print("Test 1:")
    print
    test1()
    print

    print("Test 2:")
    print
    test2()
    print

    print("Test 3:")
    print
    test3()
    print
