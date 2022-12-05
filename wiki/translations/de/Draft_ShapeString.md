---
- GuiCommand:/de
   Name:Draft ShapeString
   Name/de:Draft Textform
   MenuLocation:Entwurf → Form von Text
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:
   Version:0.14
   SeeAlso:[Draft Text](Draft_Text/de.md), [Draft Notiz](Draft_Label/de.md), [Part Extrudieren](Part_Extrude/de.md)
---

# Draft ShapeString/de

## Beschreibung

Der Befehl <img alt="" src=images/Draft_ShapeString.svg  style="width:24px;"> **Draft Textform** erstellt eine Verbundform, die eine Zeichenfolge darstellt. Diese Form kann für die Erstellung von 3D-Buchstaben mit dem Befehl [Part Extrudieren](Part_Extrude/de.md) verwendet werden.

Der Befehl Draft Textform ist nicht für normale Notizen gedacht. Dafür sollten die Befehle [Draft Text](Draft_Text.md) oder [Draft Notiz](Draft_Label.md) verwendet werden.

![](images/Draft_ShapeString_Example400.png ) 
*Ein einzelner Punkt wird zur Positionierung einer Textform benötigt*

## Anwendung

Für Windows-Anwender: Bitte zuerst den Abschnitt [Auswahl der Schriftdatei unter Windows](#Auswahl_der_Schriftdatei_unter_Windows.md) lesen.

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_ShapeString.svg" width=16px> [Form von Text](Draft_ShapeString/de.md)** drücken.
    -   Dem Menüeintrag **Entwurf → <img src="images/Draft_ShapeString.svg" width=16px> Form von Text** auswählen.
2.  Der Aufgabenbereich **Textform** wird geöffnet.
3.  Einen Punkt in der [3D-Ansicht](3D_view/de.md) anklicken, oder die Koordinaten eingeben.
4.  Wahlweise die Schaltfläche **Punkt zurücksetzen** drücken, um den Punkt auf den Ursprung zurückzusetzen.
5.  Eine **Zeichenkette** eingeben.
6.  Die **Höhe** eingeben.
7.  Zur Auswahl einer Schrift hat man folgende Möglichkeiten:
    -   Einen Dateipfad im Eingabefeld **Font file** eintragen.
    -   Die Schaltfläche **...** drücken und eine Datei auswählen.
8.  Die Schaltfläche **OK** drücken, um den Befehl abzuschließen.

## Optionen

-   Die **Esc**-Taste oder die Schaltfläche **Cancel** drücken, um den Befehl abzubrechen.

## Hinweise


<div class="mw-translate-fuzzy">

### Begrenzungen

-   Sehr kleine Texthöhen können durch Detailverlust bei der Skalierung zu verzerrten Zeichenformen führen.
-   Die aktuelle Version ist auf die von Links nach Rechts Schreiben begrenzt.
-   Um kreisförmig angeordneten Text zu erstellen, verwende <img alt="" src=images/FCCircularTextButtom.png  style="width:24px;"> [Macro FCCircularText](Macro_FCCircularText/de.md).


</div>

## Auswahl der Schriftdatei unter Windows 

On Windows access to the default font folder is restricted. This affects the font file selection for ShapeStrings. There are three cases in FreeCAD where a font file for ShapeStrings can be specified: in the ShapeString task panel, when changing the **Font File** property of a ShapeString, and when specifying the default font file in the [Draft Preferences](Draft_Preferences#Texts_and_dimensions.md).

Pressing the **...** button and then selecting a file from the default Windows font folder is not possible when using the native file dialog. There are a number of workarounds:

-   Make sure **DontUseNativeFontDialog** is set to {{True}}, which is the default value for this preference. This will only call a different, non-native, file dialog when pressing the **...** button in the ShapeString task panel. With this file dialog the default Windows font folder can be accessed.
-   Change **DontUseNativeDialog** to {{True}}. This instructs FreeCAD to always use the non-native file dialog.
-   Specify the font file in the input box. You can of course type the full path or copy-paste the path from the Windows File Explorer. But there is also another way to enter the path. If you enter {{Value|C:\}} a dropdown list will appear. Select {{Value|Windows}} from that list and add {{Value|\F}}. Select {{Value|Fonts}} from the new dropdown list. Finally add {{Value|\}} and the first letter(s) of the font file, and then select it from the dropdown list.
-   Create a custom folder for your font files.

See the [Preferences](#Preferences.md) paragraph below for the location of the mentioned preferences.

## Tutorien

-   [Entwurf FormFolge Tutorium](Draft_ShapeString_tutorial/de.md): einen ShapeString extrudieren, im 3D Raum positionieren und eine Gravur in einem anderen Körper erzeugen.
-   [Anwenden von Formfolgen in PartDesign](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623)

## Einstellungen

See also: [Preferences Editor](Preferences_Editor.md), [Draft Preferences](Draft_Preferences.md) and [Std DlgParameter](Std_DlgParameter.md).

-   The default font file can be changed in the preferences: **Edit → Preferences... → Draft → Texts and dimensions → Default ShapeString font file**.
-   For Windows users:
    -   Set **Tools → Edit parameters... → BaseApp → Preferences → Dialog → DontUseNativeFontDialog** to {{True}} to use the non-native file dialog when selecting a font file from the ShapeString task panel.
    -   Alternatively, set **Tools → Edit parameters... → BaseApp → Preferences → Dialog → DontUseNativeDialog** to {{True}} to always use the non-native file dialog.

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft ShapeString-Objekt (Textform-Objekt) wird von einem [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:

### Daten


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    {{PropertyData/de|Position}}: gibt die Position des Basispunktes der verbundenen Form an.

-    {{PropertyData/de|Winkel}}: gibt die Rotation der Grundlinie der Form an.

-    {{PropertyData/de|Achse}}: gibt die Achse an, die für die Rotation verwendet werden soll.

-    {{PropertyData/de|Folge}}: gibt die anzuzeigende Textzeichenfolge an; im Gegensatz zum Werkzeug [Entwurf Text](Draft_Text/de.md) kann das Werkzeug [Entwurf FormFolge](Draft_ShapeString/de.md) nur eine einzelne Zeile anzeigen.

-    {{PropertyData/de|Größe}}: gibt die allgemeine Höhe der Buchstaben an.

-    {{PropertyData/de|Laufweite}}: gibt den zusätzlichen Abstand zwischen den Zeichen in der Zeichenkette an.

-    {{PropertyData/de|Schriftartdatei}}: gibt den vollständigen Pfad der Schriftdatei an, die zum Zeichnen der Zeichenkette verwendet wird.


</div>

### Ansicht


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the faces of the text. This property only works if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Skripten

Siehe auch: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um eine Draft Textform zu erstellen, verwendet man die Methode `make_shapestring` ({{Version/de|0.19}}) des Arbeitsbereiches Draft. Diese Methode ersetzt die veraltete Methode `makeShapeString`.


```python
shapestring = make_shapestring(String, FontFile, Size=100, Tracking=0)
```


<div class="mw-translate-fuzzy">

-   Erzeugt eine `Formfolge` verbundene Form unter Verwendung der angegebenen `Folge` und des vollständigen Pfades einer unterstützten `Schriftartdatei`.

-    `Größe`ist die Höhe des resultierenden Textes in Millimetern.

-    `Laufweite`ist der zusätzliche Zeichenabstand in Millimetern.


</div>

Die Platzierung der FormFolge kann durch Überschreiben seines `Placement` Attributs oder durch individuelles Überschreiben seiner `Placement.Base` und `Placement.Rotation` Attribute geändert werden.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

font1 = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"
font2 = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
font3 = "/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf"

S1 = Draft.make_shapestring("This is a sample text", font1, 200)

S2 = Draft.make_shapestring("Inclined text", font2, 200, 10)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(-1000, 500, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 45))
S2.Placement = place2

S3 = Draft.make_shapestring("Upside-down text", font3, 200, 10)
S3.Placement.Base = App.Vector(0, -1000, 0)
S3.Placement.Rotation = App.Rotation(zaxis, 180)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ShapeString/de
