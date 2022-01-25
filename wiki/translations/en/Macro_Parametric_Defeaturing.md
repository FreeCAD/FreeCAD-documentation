# Macro Parametric Defeaturing/en
{{Macro
|Name=Macro Parametric Defeaturing
|Icon=parametric_defeaturing.svg
|Description=This macro is similar to the [defeaturing tool](Part_Defeaturing.md) in the [Part Workbench](Part_Workbench.md), but it's parametric and it also works in [PartDesign](PartDesign_Workbench.md). To use: select the faces of the features you wish to remove from the model and run the macro. Faces are used in defeaturing, not edges or vertices. The faces used may be edited later and the object will rebuild itself automatically.<br/>

Parametric is generally a good thing in 3D modeling, but because defeaturing relies upon face names: Face1, Face2, etc. it is vulnerable to topological naming issues and might break if changes are made to the original source object being defeatured when those changes result in the face names getting renumbered. Defeaturing is also a somewhat finicky process, not guaranteed to always succeed.<br/>

Full documentation can be found on github: [https://github.com/mwganson/parametric_defeaturing Parametric Defeaturing].<br/>

|Author=TheMarkster
|Version=0.2021.10.10.rev2
|Date=2021-10-10.rev2
|FCVersion=python 3 versions
|Download=[https://wiki.freecadweb.org/File:parametric_defeaturing.svg ToolBar Icon]
|Links=[https://github.com/mwganson/parametric_defeaturing Full Documentation on Github]
}}

## Description

This macro is similar to the [defeaturing tool](Part_Defeaturing.md) in the [Part Workbench](Part_Workbench.md), but it\'s parametric and it also works in [PartDesign](PartDesign_Workbench.md). To use: select the faces of the features you wish to remove from the model and run the macro. Faces are used in defeaturing, not edges or vertices. The faces used may be edited later and the object will rebuild itself automatically.

Parametric is generally a good thing in 3D modeling, but because defeaturing relies upon face names: Face1, Face2, etc. it is vulnerable to topological naming issues and might break if changes are made to the original source object being defeatured when those changes result in the face names getting renumbered. Defeaturing is also a somewhat finicky process, not guaranteed to always succeed.

Full documentation can be found on github: [Parametric Defeaturing](https://github.com/mwganson/parametric_defeaturing).

<img alt="" src=images/parametric_defeaturing_scr2.png  style="width:600px;"> 
*Macro Parametric Defeaturing screenshot‎*

## Legend


{{Codeextralink|https://gist.github.com/mwganson/0d55a5c51b1d6ff488b7a2f62bf50656/raw/140e9118deb955981a1ea499778cbf2521818e40/parametric_defeaturing.FCMacro|parametric_defeaturing.FCMacro}}

ToolBar Icon ![](images/parametric_defeaturing.svg )

## Script

**Macro parametric\_defeaturing.FCMacro**


{{CodeDownload|https://gist.github.com/mwganson/0d55a5c51b1d6ff488b7a2f62bf50656|parametric_defeaturing.FCMacro}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Parametric Defeaturing/en
