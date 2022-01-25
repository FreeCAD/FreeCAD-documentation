# FreeCAD GUI Widgets toolkit
## Background

Design456 is an external workbench that aims to provide a Direct Modeling solution within FreeCAD.

## Introduction

### FreeCAD GUI Widgets toolkit 

In the effort of making new tools for direct modeling, a graphical user interface (GUI) is needed. A widget system is required to let the user interact with the [3D view](3D_view.md). Often FreeCAD implemented this interactive part as a [ViewProvider](Viewprovider.md). These ViewProviders are made for each tool and are specific for each tools.

This doesn\'t serve Design456\'s agenda as it would make producing new tools difficult. That is why the necessity to figure out how [Coin3D](https://github.com/coin3d/coin/wiki) works, in other words how drawings directly to the [scenegraph](scenegraph.md) is implemented.

This GUI toolkit will in the beginning try to produce different kind of primitive drawings which then can be adapted by different widgets (i.e square, circle, triangle, ellipse etc\...) For example an arrow that a user can push/pull to get the effect of extruding or pushing a face of a 3D object.

As I am inspired totally by the simplicity of [FLTK GUI Toolkit](https://www.fltk.org/) used for making Windows/macOS/Linux GUI interfaces in cplusplus and other languages. The [Fr Widget](Fr_Widget.md) toolkit will be inspired by FLTK so understanding the toolkit shouldn\'t present much difficulty.

##### Simple example showing a drawing 


```python
from pivy import coin
import fr_draw as d 

sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()
root = d.draw_circle()
sg.addChild(root)
```

##### Another example 


```python
from pivy import coin
import math
import fr_draw as d 
import time
from PySide import QtCore,QtGui
sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()
      #draw_DoubleSidedArrow(_Points=[], _color=FR_COLOR.FR_BLACK, _ArrSize=1.0, _rotation=[0.0, 0.0, 1.0, 0.0]):
root=d.draw_DoubleSidedArrow(App.Vector(0,0,0),(0,1,1),1,[1.0, 0.0, 0.0, 180])
sg.addChild(root)

```

### Installing the GUI toolkit 

The [Design456 Workbench](Design456_Workbench.md) is a prerequisite to be able to use this widget system. There is an option to specifically import the toolkit via python code, but Design456 Workbench is still required

### [Fr\_Widget Basics](Fr_Widget_Basics.md) 

### [Fr\_Widget Common Widgets](Fr_Widget_Common_Widgets.md) 

There are some basic drawings written at the moment. Later I will list down them. But you can look at fr\_draw.py to find them. Some are used for developing direct modeling commands.

To be continued ..



---
![](images/Right_arrow.png) [documentation index](../README.md) > FreeCAD GUI Widgets toolkit
