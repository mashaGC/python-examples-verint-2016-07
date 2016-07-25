_author_ = 'mariag'

class Widget(object):
    _built = False
    def __init__(self, _widName):
        self._widName = _widName
        self._dependencies = []

    def add_dependency(self, *widgets):
        for w in widgets:
            self._dependencies.append(w)

    def build(self):
        if self._built == False:
            print "{}, ".format(self._widName),
            self._built = True
            for i in self._dependencies:
                i.build()
                
                
luke    = Widget("Luke")
hansolo = Widget("Han Solo")
leia    = Widget("Leia")
yoda    = Widget("Yoda")
padme   = Widget("Padme Amidala")
anakin  = Widget("Anakin Skywalker")
obi     = Widget("Obi-Wan")
darth   = Widget("Darth Vader")
_all    = Widget("All")


luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
_all.build()
# code should print: Han Solo, Padme Amidala, Anakin Skywalker, Leia, Yoda, Luke, Obi-Wan, Darth Vader
# (can print with newlines in between modules)