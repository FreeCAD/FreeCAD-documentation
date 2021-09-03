


<div class="mw-translate-fuzzy">


{{Macro/de
|Name=Macro Texture
|Translate=Macro Texture
|Icon=FCTexture.png
|Description=Erzeugt ein 3D-Bild aus einem BMP-Bild.
|Author=Mario52
|Version=0.14c
|Date=2021/01/16
|FCVersion=0.18 and more
|Download=[https://www.freecadweb.org/wiki/images/9/90/FCTexture.png ToolBar Icon], [https://www.freecadweb.org/wiki/Macro_Loft Macro Loft] [16px|FCCreaLoft](File:FCCreaLoft.png.md)
|SeeAlso=[32px|FCCreaLoft](File:FCCreaLoft.png.md) [Macro Loft](Macro_Loft/de.md)
}}


</div>


<div class="mw-translate-fuzzy">

## Beschreibung

Mit diesem kleinen Makro können Sie aus einem Bitmap-Bild mit 256 Graustufen sehr einfach ein 3D-Projekt erstellen.


</div>


<div class="mw-translate-fuzzy">

Ich hoffe, dass dieses Makro die Denkweise von CAD und CNC jedes Bild revolutionieren wird, wenn das, was ohne Eingriff in Objekt 3D konvertiert werden kann.


</div>


<div class="mw-translate-fuzzy">

Alles wird möglich, unabhängig von der Komplexität des Bildes!


</div>


<div class="mw-translate-fuzzy">

Das Makro <img alt="FCCreaLoft" src=images/FCCreaLoft.png  style="width:32px;"> [Macro Loft](Macro_Loft/de.md) zum Automatisieren des Multi Loft


</div>


{{Codeextralink|https://gist.githubusercontent.com/mario52a/262317bc7d8555885b0e/raw/3ec2ab127d8ad01a6b657aa5df9a6127ff07c7c0/Macro%2520FCTexture.FCMacro}}

<img alt="" src=images/Texture_004_Honda.png  style="width:480px;"> 
*Texture 004 Honda*


<div class="mw-translate-fuzzy">

## Verwenden Sie {#verwenden_sie}

Dieses Makro benötigt ein Bild mit 256 Graustufen (0-255), bevor Sie das Makro verwenden, konvertieren Sie Ihr Bild in Graustufen (Schwarzweiß), Lowe. Die Anzahl der Farben wird automatisch erkannt, wenn das Bild mehr als 256 Farben enthält, wird erwartet, dass eine andere Funktion erwartet wird. Jede Farbe (Graustufe) wird als tiefes, weißes (255) als hoch und schwarz (0) als niedrigster Pegel (tief) angesehen.


</div>

Die Konfiguration erfolgt vor dem Öffnen der Datei. Die Standardwerte sind die Einstellungen, um die Dimensionen eines Projekts zu ermitteln:

-   Breite des Bildes in Punkten in der Koordinate **X**,
-   Höhe des Bildes in Punkten in der Koordinate **Y**,
-   Tiefe oder Dicke des Projekts 10 mm (im Rohmodus auf 256 mm) in der Koordinate **Z**.

Die Bilddatei wird wie ein Scanner x1 x2 x3 \... in 1-mm-Schritten in FreeCAD ähnlich dem Wert y von jeweils 1 mm aufgefächert. Der Wert von z ergibt sich aus dem Wert der Farbe. Diese Werte sind im Makro konfigurierbar.


<div class="mw-translate-fuzzy">

Achtung: Je nach Größe des Bildes kann das Projekt sehr groß werden! Für die Aufzeichnung ergibt ein Bild mit einer Breite von 100 px und einer Höhe von 100 px **100 x 100 = 10000 Punkte** \'und da jeder Punkt einer Koordinate entspricht,\'\'\' 10000 Koordinaten XYZ dort \'\'\'.


</div>


<div class="mw-translate-fuzzy">

### Die Schnittstelle {#die_schnittstelle}


</div>

<img alt="Texture 002" src=images/Texture_002.png  style="width:300px;">





<div class="mw-translate-fuzzy">

#### Coordinate

-   Coordinate X <img alt="" src=images/Std_CoordinateSystem.svg  style="width:24px;"> {{SpinBox|0,00 mm}} : X-Koordinate der Position des Objekts, Standard: 0.
-   Coordinate Y <img alt="" src=images/Std_CoordinateSystem.svg  style="width:24px;"> {{SpinBox|0,00 mm}} : Y-Koordinate der Position des Objekts, Standard: 0.
-   Coordinate Z <img alt="" src=images/Std_CoordinateSystem.svg  style="width:24px;"> {{SpinBox|0,00 mm}} : Koordinate Z-Position des Objekts, Standard: 0.


</div>


<div class="mw-translate-fuzzy">

#### Stetching

-   Stetching X {{SpinBox|0,00 mm}} : Verengung oder Vergrößerung der Objektlänge, Standard: 0.
-   Stetching Y {{SpinBox|0,00 mm}} : Verkleinerung oder Vergrößerung der Höhe des Objekts, Standardeinstellung: 0.
-   Stetching Z {{SpinBox|0,00 mm}} : Verkleinerung oder Vergrößerung der Objekttiefe, Standard: 0.


</div>


<div class="mw-translate-fuzzy">

#### Inversion

-    {{CheckBox|Axis X}}: Umkehrkoordinaten **X** Bild.

-    {{CheckBox|Axis Y}}: Umkehrkoordinaten **Y** Bild.

-    {{CheckBox|Axis Z}}: Umkehrkoordinaten **Z** Bild.


</div>


<div class="mw-translate-fuzzy">

#### Modus 8 Bits {#modus_8_bits}

Der Anfangswert des Bedienungswerts passt sich automatisch an die ausgewählte Funktion an: 0, wenn die Einstellung auf Schwarz (**Schwarz**) 255 oder 20 steht, wenn die Einstellung Weiß ist (**Weiß**).


</div>


<div class="mw-translate-fuzzy">

-    {{RadioButton|TRUE|<img src="images/Draft_Wire.svg" width=24px> Wire}}: Bauen Sie Ihre Linie (Vektor) in der Form von Wire.

-    {{RadioButton|<img src="images/Draft_BSpline.svg" width=24px> Bspline}}: Bauen Sie Ihre Linie (Vektor) in Form von Bspline.

-    {{RadioButton|<img src="images/Workbench_Points.svg" width=24px> Cloud}}: bildet die Punktvektoren in der Punktewolke.

-    {{RadioButton|<img src="images/Draft_Point.svg" width=24px> Point}}: erstellt an jedem Pixel (Vektor) einen Punkt. (die Prozedur kann lang sein)

-    {{CheckBox|Nuance}}: Wenn die Option Farbton aktiviert ist, wird die Farbe des Punktes als Bild dargestellt.


</div>


<div class="mw-translate-fuzzy">

#### Mode 32 Bits {#mode_32_bits}

-    {{RadioButton|TRUE|Photo}}: Der Fotomodus wird automatisch aktiviert, wenn ein 32-Bit-Bild erkannt wird. (die Prozedur kann lang sein)

-    {{RadioButton|Plan}}: Mit dem Plan können Sie ein **\'32-Bit-Bild** importieren und den Hintergrund des Plans ignorieren. Standardmäßig ist der Kartenhintergrund schwarz, um zu ignorieren, dass Farben mit dem Befehl **Capping** eingestellt werden können. Wenn Weiß markiert ist, wird der untere Bereich weiß angezeigt. (die Prozedur kann lang sein)


</div>


<div class="mw-translate-fuzzy">

#### File

-    {{CheckBox|.pcd}}: Wenn eine Datei markiert ist, wird originalName.bmp.pcd im selben Verzeichnis der Datei (pcd v0.7) gespeichert.

-    {{CheckBox|.asc}}: Wenn eine Datei markiert ist, wird originalName.bmp.asc im selben Verzeichnis der Datei gespeichert. Diese Datei kann als Cloud-Punkt verwendet werden (Format: X Y Z).


</div>


<div class="mw-translate-fuzzy">

#### Verschließen (10mm) {#verschließen_10mm}

-   Slider : gibt die Höhe des Formulars an, die auf dem Titelrahmen angezeigt wird.

-    {{SpinBox|0 height}}: gibt die Höhe des Formulars an, die auf dem Titelrahmen angezeigt wird.

-   Raw mode {{CheckBox|20}} : zum Einstellen der Anzahl der Farben (Tiefe). Der Standardmodus ist 0-20 (was ein Filter darstellt und weitere Details entsprechend der Komplexität des Bildes erhalten), sobald der Modus 0 bis 255 (der gesamte Farbbereich) markiert ist.

-    {{CheckBox}}: Diese CheckBox hat die Spinbox aktiviert.

-    {{SpinBox|0/2 Contour}}: Diese Spinbox gibt die Konturlinie nicht an (zB: 0 für die Basis).

-   Capping {{CheckBox|White}} : Die Capping-Funktion kann auf der Farbauswahl (Weiß (Standard) oder Schwarz) festgelegt werden. Der Grad der Verkappung der Regel 20 auf 0 (oder 255 auf 0), wenn das Kontrollkästchen auf **W** (nicht markiert) oder 0 bis 20 (oder 0 bis 255) gesetzt ist, wenn das Kontrollkästchen auf \'\'\'B gesetzt ist \'\'\'(geprüft).

-    {{SpinBox|20 Capping}}: Diese Spinbox gibt den Grad der Verkappung an.


</div>

#### Befehl

-    **Datei und Start**: Öffnet die Image-Datei und startet die Konvertierung.

-    **Help**: Zeigt die Wiki-Seite im FreeCAD-Browser

    -   Zeigt die Wiki-Seite im FreeCAD-Browser an
    -   Um den Parameter zu ändern, gehen Sie zu \'\' \'Extras → Parameter bearbeiten \...\' \'\'
    -   \_\_Der globale Schritt auf spinBox: \_
    -   User parameter:**BaseApp/Preferences/Macros/FCMmacros/FCTexture → SingleStep**
    -   Passen Sie den gewünschten Wert an (standardmäßig 1,0).
    -   \_\_Für die Suche, ob das Makro aktualisiert wurde:\_\_
    -   User parameter:**BaseApp/Preferences/Macros/FCMmacros/FCTexture → switchVesionMacroSearch**
    -   Passen Sie die switchVesionMacroSearch auf `True` an (standardmäßig `False`).

-    **Quit**: beendet die Funktion.

## Skript

The icons .png <img alt="" src=images/FCTexture.png  style="width:64px;"> and .svg<img alt="" src=images/FCTexture.svg  style="width:64px;">

**Macro\_Texture.FCMacro**

Laden Sie das Makro in Gist herunter [Macro FCTexture.FCMacro](https://gist.github.com/mario52a/262317bc7d8555885b0e)

## Beispiel

The images were inclined to enhance the 3D effect.


<center>

<File:FCTexture_008.png%7CHonda>


</center>


<center>

<File:Macro_FCTexture_008b.png%7CHere> with option contour


</center>


<center>

<File:Texture> Nano Photo.png\|Here an example of a bmp image converted to points and restoring picture the width of the image is 6.5 nm
[thanks for the permission of Yorik](http://forum.freecadweb.org/viewtopic.php?f=24&t=5893#p47075) Image:Texture NanoDesign.png\|Here an example of a bmp image converted to object 3D of 6.7 nm width.
[thanks for the permission of Yorik](http://forum.freecadweb.org/viewtopic.php?f=24&t=5893#p47075)


</center>



<center>

Image:Texture 001 Logo.png\|The logo of FreeCAD. Image:Texture 002 Fe FC.png\|A portion of the screen FreeCAD. The [file](http://forum.freecadweb.org/viewtopic.php?f=3&t=4708&start=10#p46353).


</center>



<center>

Image:Texture\_003\_napperon.png\|A portion of a tablecloth. Image:Texture\_005\_larme.png\|A diamond plate.


</center>



<center>

<File:FCTexture> 006.png\|Mode Plan: the image on the left the white background has been ignored in the right image the colour black has been ignored (an [example](http://forum.freecadweb.org/viewtopic.php?f=3&t=6123&hilit=teobo&start=10#p49024) on the forum)


</center>



<center>

<File:Texture> Topographie.png\|Topography from a drawing or each level is represented with a degrees of different color.


</center>



<center>

<File:FCTexture_007_FreeCAD_ASCII_00.png%7CImage> converted in ASCII caracter.


</center>



<center>

<File:FCTexture_Example.gif%7CProcedure> for create solid:
**1:** Create loft with the <img alt="" src=images/Part_RuledSurface.svg  style="width:24px;"> tools or with the <img alt="FCCreaLoft" src=images/FCCreaLoft.png  style="width:32px;"> [Macro Loft](Macro_Loft/de.md)
**2:** Select all and extrude with the tools <img alt="" src=images/Part_Extrude.svg  style="width:24px;">
**3A:** For Linux Download [GMSHMesh](https://github.com/psicofil/Macros_FreeCAD) (author psicofil) [Macro\_GMSH Wiki page](Macro_GMSH.md)
**3B:** For Windows Download [GmshMesh2.zip](http://forum.freecadweb.org/download/file.php?id=15220) unzip the file and install it in your Mod directory (author ulrich1a)
**4:** Create your Mesh file and use it


</center>



<center>

<File:FCTexture> Example Mesh.png\|Convert solid in mesh with [GmshMesh.](Macro_GMSH.md)


</center>


## Links

Die Diskussion über [the forum](http://forum.freecadweb.org/viewtopic.php?f=24&t=5893) Um Ihre Eindrücke zu vermitteln oder kontaktieren Sie mich.

Das Makro <img alt="FCCreaLoft" src=images/FCCreaLoft.png  style="width:32px;"> [Macro Loft](Macro_Loft/de.md) für die automatisierung des multi loft

[apply hair cell texture](http://forum.freecadweb.org/viewtopic.php?f=3&t=4708&start=10#p46353)

[How to handle pdf import properly and feasibly?](http://forum.freecadweb.org/viewtopic.php?f=3&t=6123&hilit=teobo&start=10#p49024)

## Revision

-   Ver 0.14c : 15-01-2021 include **Gui.SendMsgToActiveView(\"ViewFit\")**

-   Ver 0.14b : 15-01-2021 Create Tab Coordinate and Tab Stretching for diminish the height of the macro and accepted in 15\" screen

-   ver 0.14 : 06/01/2021 change the search path procedure and adding preference option: search the new macro upgraded


```python
                ####new2
                pathFile      = os.path.dirname(SaveName) + "/"  #= C:/Provisoire400/
                formatFichier = os.path.splitext(SaveName)[1]    #= .png
                SaveName      = os.path.splitext(SaveName)[0]    #= /home/kubuntu/.FreeCAD/Macro/Texture_007_H #= C:/Provisoire400/image3D
                SaveNameformatFichier = SaveName + formatFichier #= C:/Provisoire400/image3D.png
                ####new2
                FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macros/FCMmacros/FCTexture").SetString("Path",pathFile)
                ####new
```

-   ver 0.13b: 30/12/2020 add try for **time.clock()** and **time.process\_time()** for Python 3xyz\...
-   ver 0.13 : 17/04/2020 Layout and PySide2 Qt5
-   ver 0.12 : 04/08/2019 add spinbox button for height
-   ver 0.11 :03/07/2019 adapt to Python 3
-   ver 0.10 : 28/12/2016 add save point in .pcd, .asc display a points cloud, height form, contour
-   ver 0.9 : 12/12/2016 adding save file .asc for cloud point
-   ver 0.8 : 16/03/2016 adding progressBar
-   ver 0.7 : 03/09/2014 Delete \"**translate**\" forgotten and bug fix discovered by the passage of PyQt to Pyside !
-   ver 0.6 : 26/08/2014 Delete all \"**\_translate**\"
-   ver 0.5 : 25/08/2014 Delete \"**\_translate (\" MainWindow \",**\" Stretching X \"**, None)**\" that prevented the display of tooltip with PySide (Windows Vista)

-   ver 0.4 : 08/08/2014 PyQt4 PySide

-   ver 0.3 : 28/03/2014 :comment out the line \"**\# self.checkBox\_5.setAccessibleName(\_fromUtf8(\"\"))**\"

that causes an error with the version FreeCAD : Version: 0.14.3343 (Git), Python version: 2.7.6, Qt version: 4.8.5




