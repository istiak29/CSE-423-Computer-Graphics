'''OpenGL extension VERSION.GL_3_1

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_3_1 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VERSION/GL_3_1.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.VERSION.GL_3_1 import *
from OpenGL.raw.GL.VERSION.GL_3_1 import _EXTENSION_NAME

def glInitGl31VERSION():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glDrawElementsInstanced.indices size not checked against 'count,type'
glDrawElementsInstanced=wrapper.wrapper(glDrawElementsInstanced).setInputArraySize(
    'indices', None
)
# INPUT glGetUniformIndices.uniformNames size not checked against 'uniformCount'
glGetUniformIndices=wrapper.wrapper(glGetUniformIndices).setOutput(
    'uniformIndices',size=_glgets._glget_size_mapping,pnameArg='uniformCount',orPassIn=True
).setInputArraySize(
    'uniformNames', None
)
# OUTPUT glGetActiveUniformsiv.params COMPSIZE(uniformCount, pname) 
# INPUT glGetActiveUniformsiv.uniformIndices size not checked against uniformCount
glGetActiveUniformsiv=wrapper.wrapper(glGetActiveUniformsiv).setInputArraySize(
    'uniformIndices', None
)
glGetActiveUniformName=wrapper.wrapper(glGetActiveUniformName).setOutput(
    'length',size=(1,),orPassIn=True
).setOutput(
    'uniformName',size=lambda x:(x,),pnameArg='bufSize',orPassIn=True
)
# INPUT glGetUniformBlockIndex.uniformBlockName size not checked against ''
glGetUniformBlockIndex=wrapper.wrapper(glGetUniformBlockIndex).setInputArraySize(
    'uniformBlockName', None
)
# OUTPUT glGetActiveUniformBlockiv.params COMPSIZE(program, uniformBlockIndex, pname) 
glGetActiveUniformBlockName=wrapper.wrapper(glGetActiveUniformBlockName).setOutput(
    'length',size=(1,),orPassIn=True
).setOutput(
    'uniformBlockName',size=lambda x:(x,),pnameArg='bufSize',orPassIn=True
)
glGetIntegeri_v=wrapper.wrapper(glGetIntegeri_v).setOutput(
    'data',size=_glgets._glget_size_mapping,pnameArg='target',orPassIn=True
)
### END AUTOGENERATED SECTION
