# Raytracing API example/pl
## Introduction

The `Raytracing` and `RaytracingGui` modules provide several methods to write scene contents as povray or luxrender data.

The most useful commands are `Raytracing.getPartAsPovray()` and `Raytracing.getPartAsLux()` to render a FreeCAD Part object into a povray or luxrender definition, and `RaytracingGui.povViewCamera()` and `RaytracinGui.luxViewCamera()` to get the current point of view of the 3D view window into povray or luxrender format.

## Outputting render files 

Here is how to write a povray file from python, assuming your document contains a \"Box\" object:


```python
import Raytracing,RaytracingGui
OutFile = open('C:/Documents and Settings/jriegel/Desktop/test.pov','w')
OutFile.write(open(App.getResourceDir()+'Mod/Raytracing/Templates/ProjectStd.pov').read())
OutFile.write(RaytracingGui.povViewCamera())
OutFile.write(Raytracing.getPartAsPovray('Box',App.activeDocument().Box.Shape,0.800000,0.800000,0.800000))
OutFile.close()
del OutFile
```

And the same for luxrender:


```python
import Raytracing,RaytracingGui
OutFile = open('C:/Documents and Settings/jriegel/Desktop/test.lxs','w')
OutFile.write(open(App.getResourceDir()+'Mod/Raytracing/Templates/LuxClassic.lxs').read())
OutFile.write(RaytracingGui.luxViewCamera())
OutFile.write(Raytracing.getPartAsLux('Box',App.activeDocument().Box.Shape,0.800000,0.800000,0.800000))
OutFile.close()
del OutFile
```

## Creating a custom render object 

Apart from standard povray and luxrender view objects that provide a view of an existing Part object, and that can be inserted in povray and luxrender projects respectively, a third object exist, called RaySegment, that can be inserted either in povray or luxrender projects. That RaySegment object is not linked to any of the FreeCAD objects, and can contain custom povray or luxrender code, that you might wish to insert into your raytracing project. You can also use it, for example, to output your FreeCAD objects a certain way, if you are not happy with the standard way. You can create and use it like this from the python console:


```python
myRaytracingProject = FreeCAD.ActiveDocument.PovProject
myCustomRenderObject = FreeCAD.ActiveDocument.addObject("Raytracing::RaySegment","myRenderObject")
myRaytracingProject.addObject(myCustomRenderObject)
myCustomRenderObject.Result = "// Hello from python!"
```


 {{Raytracing Tools navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [API](Category_API.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Raytracing](Raytracing_Workbench.md) > Raytracing API example/pl
