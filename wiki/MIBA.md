 

## Introduction

Miba is a way to embed information about the 3D space into a 2D image. This makes it often possible to use the 2D picture instead of a 3D viewer. By the Miba information you\'re able to calculate the position of a 3D location in the 2D image. That allows you to decorate the image later with arbitrary 3D information. You can take the picture in an early state (design) and use it later (e.g. Production). You do not need to know the kind of 3D data or the positions when you take the picture. So the picture is completely separated from the 3D data.

A detailed specification you can find here: <http://miba.juergen-riegel.net/>

## Miba in FreeCAD {#miba_in_freecad}

If you choose a file format which has an comment ability ( JPG and PNG) you can choose to write a comment or insert the MIBA information in the comment fileds (default):

 <img alt="" src=images/Save_picture.png  style="width:600px;"> 

## Making Miba pictures by script {#making_miba_pictures_by_script}

 
```python
import Part,PartGui

# loading test part
Part.open("C:/Documents and Settings/jriegel/My Documents/Projects/FreeCAD/data/Blade.stp")

OutDir = "c:/temp/"
Gui.ActiveDocument.ActiveView.setAnimationEnabled(False)

# creating images with different Views, Cameras and sizes
for p in ["PerspectiveCamera", "OrthographicCamera"]:
    Gui.SendMsgToActiveView(p)
    for f in ["ViewAxo", "ViewFront", "ViewTop"]:
        Gui.SendMsgToActiveView(f)
        for x, y in [[500, 500], [1000, 3000], [3000, 1000], [3000, 3000], [8000, 8000]]:
            Gui.ActiveDocument.ActiveView.saveImage(OutDir + "Blade_" + p + "_" + f + "_" + str(x) + "_" + str(y) + ".jpg", x, y, "White")
            Gui.ActiveDocument.ActiveView.saveImage(OutDir + "Blade_" + p + "_" + f + "_" + str(x) + "_" + str(y) + ".png", x, y, "Transparent")

# close active document
App.closeDocument(App.ActiveDocument.Name)
```



[Category:User\_Documentation{{\#translation:}}](Category:User_Documentation.md)
