---
 GuiCommand:
   Name: Draft ShapeString
   Name/de: Draft Textform
   MenuLocation: Entwurf , Form von Text
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: 
   Version: 0.14
   SeeAlso: Draft_Text/de, Draft_Label/de, Part_Extrude/de
---

# Draft ShapeString/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_ShapeString.svg  style="width:24px;"> **Draft Textform** erstellt eine Verbundform, die eine Zeichenfolge darstellt. Diese Form kann für die Erstellung von 3D-Buchstaben mit dem Befehl [Part Extrudieren](Part_Extrude/de.md) verwendet werden.

Der Befehl Draft Textform ist nicht für normale Notizen gedacht. Dafür sollten die Befehle [Draft Text](Draft_Text.md) oder [Draft Notiz](Draft_Label.md) verwendet werden.

![](images/Draft_ShapeString_Example400.png ) 
*Ein einzelner Punkt wird zur Positionierung einer Textform benötigt*



## Anwendung

Für Windows-Anwender: Bitte zuerst den Abschnitt [Auswahl der Schriftdatei unter Windows](#Auswahl_der_Schriftdatei_unter_Windows.md) lesen.

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_ShapeString.svg" width=16px> [Textform](Draft_ShapeString/de.md)** drücken.
    -   Den Menüeintrag **Zeichnen → <img src="images/Draft_ShapeString.svg" width=16px> Textform** auswählen.
2.  Der Aufgabenbereich **Textform** wird geöffnet.
3.  Einen Punkt in der [3D-Ansicht](3D_view/de.md) anklicken, oder die Koordinaten eingeben.
4.  Wahlweise die Schaltfläche **Punkt zurücksetzen** drücken, um den Punkt auf den Ursprung zurückzusetzen.
5.  Eine **Zeichenkette** eingeben.
6.  Die **Höhe** eingeben.
7.  Zur Auswahl einer Schrift hat man folgende Möglichkeiten:
    -   Einen Dateipfad im Eingabefeld **Font file** eintragen.
    -   Die Schaltfläche **...** drücken und eine Datei auswählen.
8.  Die Schaltfläche **OK** drücken, um den Befehl abzuschließen.
9.  Wahlweise die {{PropertyData/de|Justification}} (Ausrichtung) der Textform anpassen. Siehe [Eigenschaften](#Eigenschaften.md).



## Optionen

-   Die **Esc**-Taste oder die Schaltfläche **Cancel** drücken, um den Befehl abzubrechen.



## Hinweise

-   Eine Draft Textform (ShapeString) kann nach einem Doppelklick auf ihr Symbol in der [Baumansicht](Tree_view/de.md) bearbeitet werden. {{Version/de|0.20}}
-   Die unterstützten Schriftarten enthalten TrueType- (**.ttf**), OpenType- (**.otf**) und Type-1-Schriftarten (**.pfb**).
-   Der Befehl unterstützt nur Text mit Schreibrichtung nach rechts. Text mit Schreibrichtung nach links und von oben nach unten wird nicht unterstützt.
-   Sehr kleine Schrifthöhen können zu verformten Zeichenumrissen führen, da beim Skalieren Details verlorengehen.
-   Schriftarten können problematische Geometrien erzeugen. Das liegt daran, dass Schriftkonturen überlappen dürfen und kleine Lücken enthalten dürfen. Diese Merkmale werden bei Linienzügen, die zur Erstellung von Flächen dienen, als Fehler angesehen.
-   Draft Textformen können auch mit dem [Macro Fonts Win10 PYMP](Macro_Fonts_Win10_PYMP.md) erstellt werden.
-   Um Draft Textformen ringförmig anzuordnen kann das [Macro FCCircularText](Macro_FCCircularText.md) verwendet werden.



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

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md), [Draft Einstellungen](Draft_Preferences/de.md) und [Std ParameterDialog](Std_DlgParameter/de.md).

-   Die Standardschrift kann im Voreinstellungseditor angepasst werden: **Bearbeiten → Einstellungen... → Draft → Texte und Bemaßungen → Standardschriftart für Textformen**.
-   Für Windows-Anwender:
    -   
        **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Dialog → DontUseNativeFontDialog**
        
        auf {{True}} setzen, um den non-native Datei-Dialog zu verwenden, wenn eine Schriftart aus dem Aufgaben-Bereich Textform ausgewählt wird.

    -   Alternativ kann **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Dialog → DontUseNativeDialog** auf {{True}} gesetzt werden, um immer den non-native Datei-Dialog zu verwenden.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft ShapeString-Objekt (Textform-Objekt) wird von einem [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Draft}}

-    {{PropertyData/de|Font File|File}}: Name der Schriftdatei.

-    {{PropertyData/de|Fuse|Bool}}: Vereinigt Flächen, wenn sie überlappen. Ist normalerweise nicht erforderlich (kann sehr langsam sein). Wird ignoriert, wenn die {{PropertyData/de|Make Face}} auf `False` gesetzt ist. {{Version/de|0.22}}

-    {{PropertyData/de|Justification|Enumeration}}: Horizontales und vertikales Ausrichten. Optionen: {{value|Top-Left}} (oben links), {{value|Top-Center}} (oben mittig), {{value|Top-Right}} (oben rechts), {{value|Middle-Left}} (Mitte links), {{value|Middle-Center}} (Mitte mittig), {{value|Middle-Right}} (Mitte rechts), {{value|Bottom-Left}} (unten links), {{value|Bottom-Center}} (unten mittig), {{value|Bottom-Right}} (unten rechts). {{Version/de|0.22}}

-    {{PropertyData/de|Justification Reference|Enumeration}}: Hohenreferenz, die zum Ausrichten verwendet wird. Optionen: {{value|Cap Height}} (Versalhöhe = Mittel- + Oberlänge), {{value|Shape Height}} (Mittel- + Unterlänge). Shape-Height hängt von den Zeichen in der {{PropertyData/de|String}} ab. {{Version/de|0.22}}

-    {{PropertyData/de|Keep Left Margin|Bool}}: Behält den linken Rand und führende Leerzeichen bei, wenn linksbündig ausgerichtet wird. {{Version/de|0.22}}

-    {{PropertyData/de|Make Face|Bool}}: Erstellt Flächen aus den Konturen der Schriftzeichen.

-    {{PropertyData/de|Oblique Angle|Angle}}: Neigungswinkel. Kann Werte zwischen -80° und +80° annehmen. {{Version/de|0.22}}

-    {{PropertyData/de|Scale To Size|Bool}}: Skaliert die Versalhöhe, damit sie der Schrifthöhe gleicht. Wenn auf `False` gesetzt, wird die Versalhöhe, abhängig von der Schriftart, nicht exakt der {{PropertyData/de|Size}} entsprechen. {{Version/de|0.22}}

-    {{PropertyData/de|Size|Length}}: Schrifthöhe.

-    {{PropertyData/de|String|String}}: Zeichenkette. Eine Textform kann nur eine einzelne Textzeile anzeigen.

-    {{PropertyData/de|Tracking|Distance}}: Zeichenzwischenraum. Die Art der Eigenschaft wurde aktualisiert ({{Version/de|0.22}}).

<img alt="" src=images/Draft_ShapeString_Justification.png  style="width:200px;"> 
*Die Höhe des roten Rechtecks (Vollinie) gleicht der Versalhöhe.<br>
Höhe des grünen Rechtecks (Strichlinie) gleicht der Mittel- + Unterlänge (shape height).<br>
Die Eckpunkte, die Mittelpunkte der Kanten und die Mittelpunkte der Rechtecke<br>
entsprechen den 9 Ausrichtungsoptionen von oben links bis unten rechts.*



## Skripten

Siehe auch: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um eine Draft Textform zu erstellen, verwendet man die Methode `make_shapestring` ({{Version/de|0.19}}) des Arbeitsbereiches Draft. Diese Methode ersetzt die veraltete Methode `makeShapeString`.


```python
shapestring = make_shapestring(String, FontFile, Size=100, Tracking=0)
```

-   Erzeugt eine `shapestring`-Verbund-Form unter Verwendung der angegebenen Zeichenfolge `String` und des vollständigen Pfades einer unterstützten Schriftartdatei `FontFile`.

-    `Size`ist die Höhe des resultierenden Textes in Millimetern.

-    `Tracking`ist der Zeichenabstand (Laufweite) in Millimetern.

Die Positionierung der Textform kann durch Überschreiben ihres Attributs `Placement` oder durch individuelles Überschreiben ihrer Attribute `Placement.Base` und `Placement.Rotation` geändert werden.

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
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ShapeString/de
