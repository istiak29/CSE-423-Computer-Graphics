'''OpenGL extension EXT.blend_func_separate

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.blend_func_separate to provide a more 
Python-friendly API

Overview (from the spec)
	
	Blending capability is extended by defining a function that allows
	independent setting of the RGB and alpha blend factors for blend
	operations that require source and destination blend factors.  It
	is not always desired that the blending used for RGB is also applied
	to alpha.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/blend_func_separate.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.blend_func_separate import *
from OpenGL.raw.GL.EXT.blend_func_separate import _EXTENSION_NAME

def glInitBlendFuncSeparateEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION