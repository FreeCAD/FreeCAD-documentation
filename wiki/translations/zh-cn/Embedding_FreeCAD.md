# Embedding FreeCAD/zh-cn
{{TOCright}}

## Introduction

FreeCAD can be imported as a [Python](Python.md) module in other programs or in a standalone Python console, together with all its modules and components. It\'s even possible to import the FreeCAD user interface as a python module but with some restrictions indicated in [Caveats](#Caveats.md).

## Using FreeCAD without GUI 

The first, direct, easy, and useful application you can make of this is to import FreeCAD documents into your program. In the following example, we\'ll import the Part geometry of a FreeCAD document into [blender](http://www.blender.org). Here is the complete script. I hope you\'ll be impressed by its simplicity: {{Code|lang=python|code=
<nowiki>
FREECADPATH = '/opt/FreeCAD/lib' # path to your FreeCAD.so or FreeCAD.dll file
import Blender, sys
sys.path.append(FREECADPATH)
 
def import_fcstd(filename):
   try:
       import FreeCAD
   except ValueError:
       Blender.Draw.PupMenu('Error%t|FreeCAD library not found. Please check the FREECADPATH variable in the import script is correct')
   else:
       scene = Blender.Scene.GetCurrent()
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()

def main():
   Blender.Window.FileSelector(import_fcstd, 'IMPORT FCSTD', 
                        Blender.sys.makename(ext='.fcstd'))    
 
# This lets you import the script without running it
if __name__=='__main__':
   main()
</nowiki>
}}

The first and important part is to make sure python will find our FreeCAD library. Once it finds it, all FreeCAD modules such as Part (that we\'ll use as well) will be available automatically. So we simply take the `sys.path` variable, which is where python searches for modules, and we append the FreeCAD library path. This modification is only temporary, and will be lost when we\'ll close our python interpreter. An alternate way could be: making a link to your FreeCAD library in one of the python search paths. I stored the path in a constant (`FREECADPATH`) so it\'ll be easier for another user of the script to configure it to their own system.


{{Code|lang=python|code=
FREECADPATH = '/opt/FreeCAD/lib' # path to your FreeCAD.so or FreeCAD.dll file
import Blender, sys
sys.path.append(FREECADPATH)
}}

Once we are sure the library is loaded (the `try`/`except` sequence), we can now work with FreeCAD, the same way as we would inside FreeCAD\'s own python interpreter. We open the FreeCAD document that is passed to us by the `main()` function, and we make a list of its objects. Then, as we chose only to care about Part geometry, we check if the Type property of each object contains \"`Part`\", then we tesselate it.


{{Code|lang=python|code=
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
}}

The tesselation produce a list of vertices and a list of faces defined by vertices indexes. This is perfect, since it is exactly the same way as blender defines meshes. So, our task is ridiculously simple, we just add both lists contents to the verts and faces of a blender mesh. When everything is done, we just redraw the screen, and that\'s it!


{{Code|lang=python|code=
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()
}}

Of course this script is very simple (in fact I made a more advanced [FreeCAD to Blender importer](https://yorik.orgfree.com/scripts/import_freecad.py)), you might want to extend it, for example importing mesh objects too, or importing Part geometry that has no faces, or import other file formats that FreeCAD can read. You might also want to export geometry to a FreeCAD document, which can be done the same way. You might also want to build a dialog, so the user can choose what to import, etc\... The beauty of all this actually lies in the fact that you let FreeCAD do the ground work while presenting its results in the program of your choice.


**Note:**

checkout [Headless FreeCAD](Headless_FreeCAD.md) for running FreeCAD without the GUI.

## Using FreeCAD with GUI 

From version 4.2 on Qt has the intriguing ability to embed Qt-GUI-dependent plugins into non-Qt host applications and share the host\'s event loop.

Especially, for FreeCAD this means that it can be imported from within another application with its whole user interface where the host application has full control over FreeCAD, then.

The whole python code to achieve that has only two lines


```python
import FreeCADGui 
FreeCADGui.showMainWindow()
```

If the host application is based on Qt then this solution should work on all platforms which Qt supports. However, the host should link the same Qt version as FreeCAD because otherwise you could run into unexpected runtime errors.

For non-Qt applications, however, there are a few limitations you must be aware of. This solution probably doesn\'t work together with all other toolkits. For Windows it works as long as the host application is directly based on Win32 or any other toolkit that internally uses the Win32 API such as wxWidgets, MFC or WinForms. In order to get it working under X11 the host application must link the \"glib\" library.

Note, for any console application this solution of course doesn\'t work because there is no event loop running.

## Caveats

Although it is possible to import FreeCAD to an external Python interpreter, this is not a common usage scenario and requires some care. Generally, it is better to use the Python included with FreeCAD, run FreeCAD via command line, or as a subprocess. See [Start up and Configuration](Start_up_and_Configuration.md) for more on the last two options.

Since the FreeCAD Python module is compiled from C++ (rather than being a pure Python module), it can only be imported from a compatible Python interpreter. Generally this means that the Python interpreter must be compiled with the same C compiler as was used to build FreeCAD. Information about the compiler used to build a Python interpreter (including the one built with FreeCAD) can be found as follows: 
```python
>>> import sys
>>> sys.version
'2.7.13 (default, Dec 17 2016, 23:03:43) \n[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)]'
```

## Related

-   [Headless FreeCAD](Headless_FreeCAD.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Embedding FreeCAD/zh-cn
