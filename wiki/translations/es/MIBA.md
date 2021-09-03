

## Introduction


<div class="mw-translate-fuzzy">

## Introducción

Miba es un modo de embeber información sobre el espacio 3D en una imagen 2D. Esto hace que a menudo sea posible utilizar la imagen 2D en lugar de un visor 3D. Por la información de Miba eres capaz de calcular la posición de una ubicación 3D en la imagen 2D. Esto te permite decorar la imagen después con información 3D arbitraria. Puedes coger una imagen en un estado inicial (de diseño) y utilizarla después (en producción). No necesitas conocer la clase de datos 3D o la posición cuando tomas la imagen. Así la imagen está completamente separada de los datos 3D.


</div>

Una especificación detallada puedes encontrarla aquí: <http://miba.juergen-riegel.net/>

## Miba in FreeCAD 


<div class="mw-translate-fuzzy">

## Miba en FreeCAD 

Si seleccionas un formato de archivo que tenga esta capacidad que hemos comentado (JPG y PNG) puedes escoger escribir un comentario o insertar la información MIBA en los campos de comentarios (por defecto):


</div>

<img alt="" src=images/Save_picture.png  style="width:600px;">

## Creación de imágenes Miba pictures por archivos de guión 


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
