# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_libsikuli', [dirname(__file__)])
        except ImportError:
            import _libsikuli
            return _libsikuli
        if fp is not None:
            try:
                _mod = imp.load_module('_libsikuli', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _libsikuli = swig_import_helper()
    del swig_import_helper
else:
    import _libsikuli
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


_type = type
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
   if (name == "thisown"): return self.this.own(value)
   if (name == "this"):
      if _type(value).__name__ == 'SwigPyObject':
         self.__dict__[name] = value
         return
   method = class_type.__swig_setmethods__.get(name,None)
   if method: return method(self,value)
   if (not static) or hasattr(self,name):
      self.__dict__[name] = value
   else:
      raise AttributeError("You cannot add attributes to %s" % self)   

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _libsikuli.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _libsikuli.SwigPyIterator_value(self)
    def incr(self, n = 1): return _libsikuli.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _libsikuli.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _libsikuli.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _libsikuli.SwigPyIterator_equal(self, *args)
    def copy(self): return _libsikuli.SwigPyIterator_copy(self)
    def next(self): return _libsikuli.SwigPyIterator_next(self)
    def __next__(self): return _libsikuli.SwigPyIterator___next__(self)
    def previous(self): return _libsikuli.SwigPyIterator_previous(self)
    def advance(self, *args): return _libsikuli.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _libsikuli.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _libsikuli.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _libsikuli.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _libsikuli.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _libsikuli.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _libsikuli.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _libsikuli.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class Matches(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Matches, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Matches, name)
    __repr__ = _swig_repr
    def iterator(self): return _libsikuli.Matches_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _libsikuli.Matches___nonzero__(self)
    def __bool__(self): return _libsikuli.Matches___bool__(self)
    def __len__(self): return _libsikuli.Matches___len__(self)
    def pop(self): return _libsikuli.Matches_pop(self)
    def __getslice__(self, *args): return _libsikuli.Matches___getslice__(self, *args)
    def __setslice__(self, *args): return _libsikuli.Matches___setslice__(self, *args)
    def __delslice__(self, *args): return _libsikuli.Matches___delslice__(self, *args)
    def __delitem__(self, *args): return _libsikuli.Matches___delitem__(self, *args)
    def __getitem__(self, *args): return _libsikuli.Matches___getitem__(self, *args)
    def __setitem__(self, *args): return _libsikuli.Matches___setitem__(self, *args)
    def append(self, *args): return _libsikuli.Matches_append(self, *args)
    def empty(self): return _libsikuli.Matches_empty(self)
    def size(self): return _libsikuli.Matches_size(self)
    def clear(self): return _libsikuli.Matches_clear(self)
    def swap(self, *args): return _libsikuli.Matches_swap(self, *args)
    def get_allocator(self): return _libsikuli.Matches_get_allocator(self)
    def begin(self): return _libsikuli.Matches_begin(self)
    def end(self): return _libsikuli.Matches_end(self)
    def rbegin(self): return _libsikuli.Matches_rbegin(self)
    def rend(self): return _libsikuli.Matches_rend(self)
    def pop_back(self): return _libsikuli.Matches_pop_back(self)
    def erase(self, *args): return _libsikuli.Matches_erase(self, *args)
    def __init__(self, *args): 
        this = _libsikuli.new_Matches(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _libsikuli.Matches_push_back(self, *args)
    def front(self): return _libsikuli.Matches_front(self)
    def back(self): return _libsikuli.Matches_back(self)
    def assign(self, *args): return _libsikuli.Matches_assign(self, *args)
    def resize(self, *args): return _libsikuli.Matches_resize(self, *args)
    def insert(self, *args): return _libsikuli.Matches_insert(self, *args)
    def reserve(self, *args): return _libsikuli.Matches_reserve(self, *args)
    def capacity(self): return _libsikuli.Matches_capacity(self)
    __swig_destroy__ = _libsikuli.delete_Matches
    __del__ = lambda self : None;
Matches_swigregister = _libsikuli.Matches_swigregister
Matches_swigregister(Matches)


def initOCR(*args):
  return _libsikuli.initOCR(*args)
initOCR = _libsikuli.initOCR

def switchApp(*args):
  return _libsikuli.switchApp(*args)
switchApp = _libsikuli.switchApp

def addImagePath(*args):
  return _libsikuli.addImagePath(*args)
addImagePath = _libsikuli.addImagePath

def wait(*args):
  return _libsikuli.wait(*args)
wait = _libsikuli.wait
ALT = _libsikuli.ALT
CMD = _libsikuli.CMD
CTRL = _libsikuli.CTRL
META = _libsikuli.META
SHIFT = _libsikuli.SHIFT
WIN = _libsikuli.WIN
ENTER = _libsikuli.ENTER
TAB = _libsikuli.TAB
ESC = _libsikuli.ESC
INSERT = _libsikuli.INSERT
BACKSPACE = _libsikuli.BACKSPACE
DELETE = _libsikuli.DELETE
CAPSLOCK = _libsikuli.CAPSLOCK
SPACE = _libsikuli.SPACE
F1 = _libsikuli.F1
F2 = _libsikuli.F2
F3 = _libsikuli.F3
F4 = _libsikuli.F4
F5 = _libsikuli.F5
F6 = _libsikuli.F6
F7 = _libsikuli.F7
F8 = _libsikuli.F8
F9 = _libsikuli.F9
F10 = _libsikuli.F10
F11 = _libsikuli.F11
F12 = _libsikuli.F12
F13 = _libsikuli.F13
F14 = _libsikuli.F14
F15 = _libsikuli.F15
HOME = _libsikuli.HOME
END = _libsikuli.END
LEFT = _libsikuli.LEFT
RIGHT = _libsikuli.RIGHT
DOWN = _libsikuli.DOWN
UP = _libsikuli.UP
PAGE_DOWN = _libsikuli.PAGE_DOWN
PAGE_UP = _libsikuli.PAGE_UP
ANYWHERE = _libsikuli.ANYWHERE
TOPMOST = _libsikuli.TOPMOST
BOTTOMMOST = _libsikuli.BOTTOMMOST
LEFTMOST = _libsikuli.LEFTMOST
RIGHTMOST = _libsikuli.RIGHTMOST
SCORE = _libsikuli.SCORE
TOPDOWN = _libsikuli.TOPDOWN
BOTTOMUP = _libsikuli.BOTTOMUP
LEFTRIGHT = _libsikuli.LEFTRIGHT
RIGHTLEFT = _libsikuli.RIGHTLEFT
class Pattern(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Pattern, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Pattern, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _libsikuli.new_Pattern(*args)
        try: self.this.append(this)
        except: self.this = this
    def all(self): return _libsikuli.Pattern_all(self)
    def one(self): return _libsikuli.Pattern_one(self)
    def similar(self, *args): return _libsikuli.Pattern_similar(self, *args)
    def exact(self): return _libsikuli.Pattern_exact(self)
    def targetOffset(self, *args): return _libsikuli.Pattern_targetOffset(self, *args)
    def getTargetOffset(self): return _libsikuli.Pattern_getTargetOffset(self)
    def getSimilarity(self): return _libsikuli.Pattern_getSimilarity(self)
    def topMost(self): return _libsikuli.Pattern_topMost(self)
    def bottomMost(self): return _libsikuli.Pattern_bottomMost(self)
    def leftMost(self): return _libsikuli.Pattern_leftMost(self)
    def rightMost(self): return _libsikuli.Pattern_rightMost(self)
    def limit(self, *args): return _libsikuli.Pattern_limit(self, *args)
    def order(self, *args): return _libsikuli.Pattern_order(self, *args)
    def toString(self): return _libsikuli.Pattern_toString(self)
    def getText(self): return _libsikuli.Pattern_getText(self)
    def getImageURL(self): return _libsikuli.Pattern_getImageURL(self)
    def isImageURL(self): return _libsikuli.Pattern_isImageURL(self)
    def isText(self): return _libsikuli.Pattern_isText(self)
    def bAll(self): return _libsikuli.Pattern_bAll(self)
    def bOne(self): return _libsikuli.Pattern_bOne(self)
    def where(self): return _libsikuli.Pattern_where(self)
    def getOrdering(self): return _libsikuli.Pattern_getOrdering(self)
    def getLimit(self): return _libsikuli.Pattern_getLimit(self)
    __swig_destroy__ = _libsikuli.delete_Pattern
    __del__ = lambda self : None;
Pattern_swigregister = _libsikuli.Pattern_swigregister
Pattern_swigregister(Pattern)

class Location(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Location, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Location, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _libsikuli.new_Location(*args)
        try: self.this.append(this)
        except: self.this = this
    def offset(self, *args): return _libsikuli.Location_offset(self, *args)
    def left(self, *args): return _libsikuli.Location_left(self, *args)
    def right(self, *args): return _libsikuli.Location_right(self, *args)
    def above(self, *args): return _libsikuli.Location_above(self, *args)
    def below(self, *args): return _libsikuli.Location_below(self, *args)
    __swig_setmethods__["x"] = _libsikuli.Location_x_set
    __swig_getmethods__["x"] = _libsikuli.Location_x_get
    if _newclass:x = _swig_property(_libsikuli.Location_x_get, _libsikuli.Location_x_set)
    __swig_setmethods__["y"] = _libsikuli.Location_y_set
    __swig_getmethods__["y"] = _libsikuli.Location_y_get
    if _newclass:y = _swig_property(_libsikuli.Location_y_get, _libsikuli.Location_y_set)
    __swig_setmethods__["screen"] = _libsikuli.Location_screen_set
    __swig_getmethods__["screen"] = _libsikuli.Location_screen_get
    if _newclass:screen = _swig_property(_libsikuli.Location_screen_get, _libsikuli.Location_screen_set)
    __swig_destroy__ = _libsikuli.delete_Location
    __del__ = lambda self : None;
Location_swigregister = _libsikuli.Location_swigregister
Location_swigregister(Location)

class Rectangle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Rectangle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Rectangle, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _libsikuli.new_Rectangle(*args)
        try: self.this.append(this)
        except: self.this = this
    def intersection(self, *args): return _libsikuli.Rectangle_intersection(self, *args)
    def toString(self): return _libsikuli.Rectangle_toString(self)
    __swig_setmethods__["x"] = _libsikuli.Rectangle_x_set
    __swig_getmethods__["x"] = _libsikuli.Rectangle_x_get
    if _newclass:x = _swig_property(_libsikuli.Rectangle_x_get, _libsikuli.Rectangle_x_set)
    __swig_setmethods__["y"] = _libsikuli.Rectangle_y_set
    __swig_getmethods__["y"] = _libsikuli.Rectangle_y_get
    if _newclass:y = _swig_property(_libsikuli.Rectangle_y_get, _libsikuli.Rectangle_y_set)
    __swig_setmethods__["w"] = _libsikuli.Rectangle_w_set
    __swig_getmethods__["w"] = _libsikuli.Rectangle_w_get
    if _newclass:w = _swig_property(_libsikuli.Rectangle_w_get, _libsikuli.Rectangle_w_set)
    __swig_setmethods__["h"] = _libsikuli.Rectangle_h_set
    __swig_getmethods__["h"] = _libsikuli.Rectangle_h_get
    if _newclass:h = _swig_property(_libsikuli.Rectangle_h_get, _libsikuli.Rectangle_h_set)
    __swig_destroy__ = _libsikuli.delete_Rectangle
    __del__ = lambda self : None;
Rectangle_swigregister = _libsikuli.Rectangle_swigregister
Rectangle_swigregister(Rectangle)

class ScreenImage(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ScreenImage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ScreenImage, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _libsikuli.new_ScreenImage(*args)
        try: self.this.append(this)
        except: self.this = this
    def getROI(self): return _libsikuli.ScreenImage_getROI(self)
    def getFilename(self): return _libsikuli.ScreenImage_getFilename(self)
    def getMat(self): return _libsikuli.ScreenImage_getMat(self)
    __swig_destroy__ = _libsikuli.delete_ScreenImage
    __del__ = lambda self : None;
ScreenImage_swigregister = _libsikuli.ScreenImage_swigregister
ScreenImage_swigregister(ScreenImage)

PADDING = _libsikuli.PADDING
class Region(Rectangle):
    __swig_setmethods__ = {}
    for _s in [Rectangle]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Region, name, value)
    __swig_getmethods__ = {}
    for _s in [Rectangle]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Region, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _libsikuli.new_Region(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsikuli.delete_Region
    __del__ = lambda self : None;
    def getX(self): return _libsikuli.Region_getX(self)
    def getY(self): return _libsikuli.Region_getY(self)
    def getW(self): return _libsikuli.Region_getW(self)
    def getH(self): return _libsikuli.Region_getH(self)
    def setX(self, *args): return _libsikuli.Region_setX(self, *args)
    def setY(self, *args): return _libsikuli.Region_setY(self, *args)
    def setW(self, *args): return _libsikuli.Region_setW(self, *args)
    def setH(self, *args): return _libsikuli.Region_setH(self, *args)
    def __eq__(self, *args): return _libsikuli.Region___eq__(self, *args)
    def getCenter(self): return _libsikuli.Region_getCenter(self)
    def getLastMatch(self): return _libsikuli.Region_getLastMatch(self)
    def getLastMatches(self): return _libsikuli.Region_getLastMatches(self)
    def setLastMatch(self, *args): return _libsikuli.Region_setLastMatch(self, *args)
    def setLastMatches(self, *args): return _libsikuli.Region_setLastMatches(self, *args)
    def find(self, *args): return _libsikuli.Region_find(self, *args)
    def findAll(self, *args): return _libsikuli.Region_findAll(self, *args)
    def wait(self, *args): return _libsikuli.Region_wait(self, *args)
    def exists(self, *args): return _libsikuli.Region_exists(self, *args)
    def waitVanish(self, *args): return _libsikuli.Region_waitVanish(self, *args)
    def findNow(self, *args): return _libsikuli.Region_findNow(self, *args)
    def findAllNow(self, *args): return _libsikuli.Region_findAllNow(self, *args)
    def waitAll(self, *args): return _libsikuli.Region_waitAll(self, *args)
    def click(self, *args): return _libsikuli.Region_click(self, *args)
    def doubleClick(self, *args): return _libsikuli.Region_doubleClick(self, *args)
    def rightClick(self, *args): return _libsikuli.Region_rightClick(self, *args)
    def hover(self, *args): return _libsikuli.Region_hover(self, *args)
    def dragDrop(self, *args): return _libsikuli.Region_dragDrop(self, *args)
    def drag(self, *args): return _libsikuli.Region_drag(self, *args)
    def dropAt(self, *args): return _libsikuli.Region_dropAt(self, *args)
    def type(self, *args): return _libsikuli.Region_type(self, *args)
    def press(self, *args): return _libsikuli.Region_press(self, *args)
    def paste(self, *args): return _libsikuli.Region_paste(self, *args)
    def mouseDown(self, *args): return _libsikuli.Region_mouseDown(self, *args)
    def mouseUp(self, *args): return _libsikuli.Region_mouseUp(self, *args)
    def keyDown(self, *args): return _libsikuli.Region_keyDown(self, *args)
    def keyUp(self, *args): return _libsikuli.Region_keyUp(self, *args)
    def capture(self): return _libsikuli.Region_capture(self)
    def nearby(self, *args): return _libsikuli.Region_nearby(self, *args)
    def right(self, *args): return _libsikuli.Region_right(self, *args)
    def left(self, *args): return _libsikuli.Region_left(self, *args)
    def above(self, *args): return _libsikuli.Region_above(self, *args)
    def below(self, *args): return _libsikuli.Region_below(self, *args)
    def wider(self, range = 9999999): return _libsikuli.Region_wider(self, range)
    def taller(self, range = 9999999): return _libsikuli.Region_taller(self, range)
    def inside(self): return _libsikuli.Region_inside(self)
    def inner(self, *args): return _libsikuli.Region_inner(self, *args)
    def onAppear(self, *args): return _libsikuli.Region_onAppear(self, *args)
    def onVanish(self, *args): return _libsikuli.Region_onVanish(self, *args)
    def onChange(self, *args): return _libsikuli.Region_onChange(self, *args)
Region_swigregister = _libsikuli.Region_swigregister
Region_swigregister(Region)

class Match(Region):
    __swig_setmethods__ = {}
    for _s in [Region]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Match, name, value)
    __swig_getmethods__ = {}
    for _s in [Region]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Match, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _libsikuli.delete_Match
    __del__ = lambda self : None;
    def __init__(self, *args): 
        this = _libsikuli.new_Match(*args)
        try: self.this.append(this)
        except: self.this = this
    def compareTo(self, *args): return _libsikuli.Match_compareTo(self, *args)
    def getTarget(self): return _libsikuli.Match_getTarget(self)
    def getScore(self): return _libsikuli.Match_getScore(self)
    def setTargetOffset(self, *args): return _libsikuli.Match_setTargetOffset(self, *args)
Match_swigregister = _libsikuli.Match_swigregister
Match_swigregister(Match)

class Screen(Region):
    __swig_setmethods__ = {}
    for _s in [Region]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Screen, name, value)
    __swig_getmethods__ = {}
    for _s in [Region]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Screen, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _libsikuli.new_Screen(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsikuli.delete_Screen
    __del__ = lambda self : None;
Screen_swigregister = _libsikuli.Screen_swigregister
Screen_swigregister(Screen)

class Settings(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Settings, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Settings, name)
    __repr__ = _swig_repr
    __swig_setmethods__["DelayAfterDrag"] = _libsikuli.Settings_DelayAfterDrag_set
    __swig_getmethods__["DelayAfterDrag"] = _libsikuli.Settings_DelayAfterDrag_get
    if _newclass:DelayAfterDrag = _swig_property(_libsikuli.Settings_DelayAfterDrag_get, _libsikuli.Settings_DelayAfterDrag_set)
    __swig_setmethods__["DelayBeforeDrop"] = _libsikuli.Settings_DelayBeforeDrop_set
    __swig_getmethods__["DelayBeforeDrop"] = _libsikuli.Settings_DelayBeforeDrop_get
    if _newclass:DelayBeforeDrop = _swig_property(_libsikuli.Settings_DelayBeforeDrop_get, _libsikuli.Settings_DelayBeforeDrop_set)
    __swig_setmethods__["WaitScanRate"] = _libsikuli.Settings_WaitScanRate_set
    __swig_getmethods__["WaitScanRate"] = _libsikuli.Settings_WaitScanRate_get
    if _newclass:WaitScanRate = _swig_property(_libsikuli.Settings_WaitScanRate_get, _libsikuli.Settings_WaitScanRate_set)
    __swig_setmethods__["ThrowException"] = _libsikuli.Settings_ThrowException_set
    __swig_getmethods__["ThrowException"] = _libsikuli.Settings_ThrowException_get
    if _newclass:ThrowException = _swig_property(_libsikuli.Settings_ThrowException_get, _libsikuli.Settings_ThrowException_set)
    __swig_setmethods__["AutoWaitTimeout"] = _libsikuli.Settings_AutoWaitTimeout_set
    __swig_getmethods__["AutoWaitTimeout"] = _libsikuli.Settings_AutoWaitTimeout_get
    if _newclass:AutoWaitTimeout = _swig_property(_libsikuli.Settings_AutoWaitTimeout_get, _libsikuli.Settings_AutoWaitTimeout_set)
    __swig_getmethods__["addImagePath"] = lambda x: _libsikuli.Settings_addImagePath
    if _newclass:addImagePath = staticmethod(_libsikuli.Settings_addImagePath)
    __swig_getmethods__["getImagePaths"] = lambda x: _libsikuli.Settings_getImagePaths
    if _newclass:getImagePaths = staticmethod(_libsikuli.Settings_getImagePaths)
    __swig_getmethods__["resetImagePaths"] = lambda x: _libsikuli.Settings_resetImagePaths
    if _newclass:resetImagePaths = staticmethod(_libsikuli.Settings_resetImagePaths)
    def __init__(self): 
        this = _libsikuli.new_Settings()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsikuli.delete_Settings
    __del__ = lambda self : None;
Settings_swigregister = _libsikuli.Settings_swigregister
Settings_swigregister(Settings)
cvar = _libsikuli.cvar

def Settings_addImagePath(*args):
  return _libsikuli.Settings_addImagePath(*args)
Settings_addImagePath = _libsikuli.Settings_addImagePath

def Settings_getImagePaths():
  return _libsikuli.Settings_getImagePaths()
Settings_getImagePaths = _libsikuli.Settings_getImagePaths

def Settings_resetImagePaths():
  return _libsikuli.Settings_resetImagePaths()
Settings_resetImagePaths = _libsikuli.Settings_resetImagePaths

class FindFailed(Exception):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FindFailed, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FindFailed, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _libsikuli.new_FindFailed(*args)
        try: self.this.append(this)
        except: self.this = this
    def what(self): return _libsikuli.FindFailed_what(self)
    __swig_destroy__ = _libsikuli.delete_FindFailed
    __del__ = lambda self : None;
FindFailed_swigregister = _libsikuli.FindFailed_swigregister
FindFailed_swigregister(FindFailed)

class FileNotFound(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FileNotFound, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FileNotFound, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _libsikuli.new_FileNotFound(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsikuli.delete_FileNotFound
    __del__ = lambda self : None;
    def what(self): return _libsikuli.FileNotFound_what(self)
FileNotFound_swigregister = _libsikuli.FileNotFound_swigregister
FileNotFound_swigregister(FileNotFound)

class Event(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Event, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Event, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _libsikuli.Event_type_set
    __swig_getmethods__["type"] = _libsikuli.Event_type_get
    if _newclass:type = _swig_property(_libsikuli.Event_type_get, _libsikuli.Event_type_set)
    __swig_setmethods__["pattern"] = _libsikuli.Event_pattern_set
    __swig_getmethods__["pattern"] = _libsikuli.Event_pattern_get
    if _newclass:pattern = _swig_property(_libsikuli.Event_pattern_get, _libsikuli.Event_pattern_set)
    __swig_setmethods__["match"] = _libsikuli.Event_match_set
    __swig_getmethods__["match"] = _libsikuli.Event_match_get
    if _newclass:match = _swig_property(_libsikuli.Event_match_get, _libsikuli.Event_match_set)
    __swig_setmethods__["region"] = _libsikuli.Event_region_set
    __swig_getmethods__["region"] = _libsikuli.Event_region_get
    if _newclass:region = _swig_property(_libsikuli.Event_region_get, _libsikuli.Event_region_set)
    def __init__(self): 
        this = _libsikuli.new_Event()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsikuli.delete_Event
    __del__ = lambda self : None;
Event_swigregister = _libsikuli.Event_swigregister
Event_swigregister(Event)

APPEAR = _libsikuli.APPEAR
VANISH = _libsikuli.VANISH
CHANGE = _libsikuli.CHANGE
class SikuliEventHandler(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SikuliEventHandler, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SikuliEventHandler, name)
    __repr__ = _swig_repr
    def __init__(self): 
        if self.__class__ == SikuliEventHandler:
            _self = None
        else:
            _self = self
        this = _libsikuli.new_SikuliEventHandler(_self, )
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsikuli.delete_SikuliEventHandler
    __del__ = lambda self : None;
    def handle(self, *args): return _libsikuli.SikuliEventHandler_handle(self, *args)
    def __disown__(self):
        self.this.disown()
        _libsikuli.disown_SikuliEventHandler(self)
        return weakref_proxy(self)
SikuliEventHandler_swigregister = _libsikuli.SikuliEventHandler_swigregister
SikuliEventHandler_swigregister(SikuliEventHandler)

class Observer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Observer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Observer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _libsikuli.new_Observer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsikuli.delete_Observer
    __del__ = lambda self : None;
    __swig_setmethods__["event_type"] = _libsikuli.Observer_event_type_set
    __swig_getmethods__["event_type"] = _libsikuli.Observer_event_type_get
    if _newclass:event_type = _swig_property(_libsikuli.Observer_event_type_get, _libsikuli.Observer_event_type_set)
    __swig_setmethods__["pattern"] = _libsikuli.Observer_pattern_set
    __swig_getmethods__["pattern"] = _libsikuli.Observer_pattern_get
    if _newclass:pattern = _swig_property(_libsikuli.Observer_pattern_get, _libsikuli.Observer_pattern_set)
    __swig_setmethods__["callback"] = _libsikuli.Observer_callback_set
    __swig_getmethods__["callback"] = _libsikuli.Observer_callback_get
    if _newclass:callback = _swig_property(_libsikuli.Observer_callback_get, _libsikuli.Observer_callback_set)
    __swig_setmethods__["event_handler"] = _libsikuli.Observer_event_handler_set
    __swig_getmethods__["event_handler"] = _libsikuli.Observer_event_handler_get
    if _newclass:event_handler = _swig_property(_libsikuli.Observer_event_handler_get, _libsikuli.Observer_event_handler_set)
    __swig_setmethods__["active"] = _libsikuli.Observer_active_set
    __swig_getmethods__["active"] = _libsikuli.Observer_active_get
    if _newclass:active = _swig_property(_libsikuli.Observer_active_get, _libsikuli.Observer_active_set)
Observer_swigregister = _libsikuli.Observer_swigregister
Observer_swigregister(Observer)

class RegionObserver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RegionObserver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RegionObserver, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _libsikuli.new_RegionObserver(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsikuli.delete_RegionObserver
    __del__ = lambda self : None;
    def addObserver(self, *args): return _libsikuli.RegionObserver_addObserver(self, *args)
    def observe(self): return _libsikuli.RegionObserver_observe(self)
    def getRegion(self): return _libsikuli.RegionObserver_getRegion(self)
RegionObserver_swigregister = _libsikuli.RegionObserver_swigregister
RegionObserver_swigregister(RegionObserver)

class EventManager(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, EventManager, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, EventManager, name)
    __repr__ = _swig_repr
    __swig_getmethods__["addObserver"] = lambda x: _libsikuli.EventManager_addObserver
    if _newclass:addObserver = staticmethod(_libsikuli.EventManager_addObserver)
    __swig_getmethods__["observe"] = lambda x: _libsikuli.EventManager_observe
    if _newclass:observe = staticmethod(_libsikuli.EventManager_observe)
    __swig_getmethods__["stop"] = lambda x: _libsikuli.EventManager_stop
    if _newclass:stop = staticmethod(_libsikuli.EventManager_stop)
    def __init__(self): 
        this = _libsikuli.new_EventManager()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsikuli.delete_EventManager
    __del__ = lambda self : None;
EventManager_swigregister = _libsikuli.EventManager_swigregister
EventManager_swigregister(EventManager)

def EventManager_addObserver(*args):
  return _libsikuli.EventManager_addObserver(*args)
EventManager_addObserver = _libsikuli.EventManager_addObserver

def EventManager_observe(*args):
  return _libsikuli.EventManager_observe(*args)
EventManager_observe = _libsikuli.EventManager_observe

def EventManager_stop():
  return _libsikuli.EventManager_stop()
EventManager_stop = _libsikuli.EventManager_stop

SKIP = _libsikuli.SKIP
RETRY = _libsikuli.RETRY
ABORT = _libsikuli.ABORT
class SikuliUI(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SikuliUI, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SikuliUI, name)
    __repr__ = _swig_repr
    def __init__(self): 
        if self.__class__ == SikuliUI:
            _self = None
        else:
            _self = self
        this = _libsikuli.new_SikuliUI(_self, )
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsikuli.delete_SikuliUI
    __del__ = lambda self : None;
    def handleFindFailedException(self, *args): return _libsikuli.SikuliUI_handleFindFailedException(self, *args)
    def handleMatchFound(self, *args): return _libsikuli.SikuliUI_handleMatchFound(self, *args)
    __swig_getmethods__["set"] = lambda x: _libsikuli.SikuliUI_set
    if _newclass:set = staticmethod(_libsikuli.SikuliUI_set)
    __swig_setmethods__["sikuliUI"] = _libsikuli.SikuliUI_sikuliUI_set
    __swig_getmethods__["sikuliUI"] = _libsikuli.SikuliUI_sikuliUI_get
    if _newclass:sikuliUI = _swig_property(_libsikuli.SikuliUI_sikuliUI_get, _libsikuli.SikuliUI_sikuliUI_set)
    def __disown__(self):
        self.this.disown()
        _libsikuli.disown_SikuliUI(self)
        return weakref_proxy(self)
SikuliUI_swigregister = _libsikuli.SikuliUI_swigregister
SikuliUI_swigregister(SikuliUI)

def SikuliUI_set(*args):
  return _libsikuli.SikuliUI_set(*args)
SikuliUI_set = _libsikuli.SikuliUI_set

class ImageReadHelper(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ImageReadHelper, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ImageReadHelper, name)
    __repr__ = _swig_repr
    def __init__(self): 
        if self.__class__ == ImageReadHelper:
            _self = None
        else:
            _self = self
        this = _libsikuli.new_ImageReadHelper(_self, )
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsikuli.delete_ImageReadHelper
    __del__ = lambda self : None;
    def resolveImageFilename(self, *args): return _libsikuli.ImageReadHelper_resolveImageFilename(self, *args)
    __swig_getmethods__["instance"] = lambda x: _libsikuli.ImageReadHelper_instance
    if _newclass:instance = staticmethod(_libsikuli.ImageReadHelper_instance)
    __swig_getmethods__["set"] = lambda x: _libsikuli.ImageReadHelper_set
    if _newclass:set = staticmethod(_libsikuli.ImageReadHelper_set)
    def __disown__(self):
        self.this.disown()
        _libsikuli.disown_ImageReadHelper(self)
        return weakref_proxy(self)
ImageReadHelper_swigregister = _libsikuli.ImageReadHelper_swigregister
ImageReadHelper_swigregister(ImageReadHelper)

def ImageReadHelper_instance():
  return _libsikuli.ImageReadHelper_instance()
ImageReadHelper_instance = _libsikuli.ImageReadHelper_instance

def ImageReadHelper_set(*args):
  return _libsikuli.ImageReadHelper_set(*args)
ImageReadHelper_set = _libsikuli.ImageReadHelper_set


