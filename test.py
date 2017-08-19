from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

from hermesmodel import Element, Function

e1 = Element("Apollon")
e2 = Element("Yiannis")

f1 = Function(e1, e2, "Pisses off")

print(f1)
