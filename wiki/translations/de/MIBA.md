# MIBA/de
## Einführung

Miba ist ein Weg, in ein 2D-Bild Informationen über den 3D-Raum einzubetten. Dies erlaubt es oft, das Bild in einem 3D-Betrachter zu verwenden. Durch die Miba-Informationen ist es möglich, die Position eines 3D-Ortes im 2D-Bild zu berechnen. Das erlaubt dir, das Bild später mit beliebigen 3D-Informationen zu versehen. Du kannst das Bild in einem frühen Stadium aufnehmen (Entwurf) und es später benutzen (z.B. Produktion). Du musst nicht die Art der 3D-Daten oder die Position, wo das das Foto aufgenommen wird. So ist das Bild völlig getrennt von den 3D-Daten.

Eine detaillierte Beschreibung findest du hier: <http://miba.juergen-riegel.net/>

## Miba in FreeCAD 

Wenn du ein Dateiformat wählst, das eine Kommentarfähigkeit hat (JPG und PNG), kannst du wählen, ob du einen Kommentar schreiben oder die MIBA-Informationen in die Kommentarfelder (Vorgabewert) einfügen möchtest:

<img alt="" src=images/Save_picture.png  style="width:600px;">

## Per Skript Miba-Bilder erstellen 


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



---
![](images/Button_right.svg) [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > MIBA/de
