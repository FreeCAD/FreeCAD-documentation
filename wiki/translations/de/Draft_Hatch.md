---
 GuiCommand:
   Name: Draft Hatch
   Name/de: Draft Schraffur
   MenuLocation: Zeichnen , Schraffur<br>Anmerkung , Schraffur
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Shortcut: **H** **A**
   Version: 0.20
   SeeAlso: Draft_Pattern/de
---

# Draft Hatch/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Hatch.svg  style="width:24px;"> **Draft Schraffur** erzeugt Schraffuren auf den ebenen Flächen eines ausgewählten Objekts.



## Anwendung

1.  Ein Objekt mit Flächen auswählen. Nur die ebenen Flächen des Objekts werden schraffiert.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Hatch.svg" width=16px> [Schraffur](Draft_Hatch/de.md)** drücken.
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Zeichnen → <img src="images/Draft_Hatch.svg" width=16px> Schraffur** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **Anmerkung → <img src="images/Draft_Hatch.svg" width=16px> Schraffur** auswählen.
    -   Das Tastaturkürzel **H** dann **A**.
3.  Das Aufgaben-Fenster **Schraffur** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
4.  Die Schaltfläche **OK** drücken.



## Optionen

-   Die Schaltfläche **...** drücken und eine **PAT-Datei** auswählen. Siehe [Hinweise](#Hinweise.md).

-    **Muster**aus der Datei wählen. Derzeit ist es ratsam, Muster mit Strichlinien zu vermeiden.

-    **Maßstab**für das Muster angeben.

-    **Drehung**für das Muster angeben.

-    **Esc**oder die Schaltfläche **Cancel** drücken, um den Befehl abzubrechen.



## Schraffur-Ausrichtung 

Wenn das Schraffurmuster für eine Fläche berechnet wird, wird es standardmäßig vorübergehend in die globale XY-Ebene übersetzt. Bei einer Fläche mit geraden Kanten bestimmt die erste gerade Kante, wie dies geschieht. Der erste Punkt dieser Kante wird auf den Ursprung gelegt und die Kante selbst wird an der X-Achse ausgerichtet. Wenn ein [Draft-Linienzug](Draft_Wire/de.md) in diesem Sinne erstellt wird, kann gesteuert werden, wie das Schraffurmuster an der Kontur der Fläche ausgerichtet wird.

Wenn alle Flächen des ausgewählten Objekts auf der globalen XY-Ebene liegen, kann dieses Standardverhalten ausgeschaltet werden, indem die Eigenschaft {{PropertyData/de|Translate}} der Draft-Schraffur auf `False` gesetzt wird. Das Schraffurmuster wird dann mit dem Ursprung und der X-Achse des globalen Koordinatensystems ausgerichtet. Für Flächen auf der XY-Ebene mit geraden Kanten kann die Eigenschaft {{PropertyData/de|Translate}} verwendet werden, um zwischen absoluten (links im Bild) und relativen (rechts im Bild) Mustern zu wechseln.

<img alt="" src=images/Draft_Hatch_alignment.png  style="width:400px;"> 
*
Zwei Draft-Linienzüge mit Schraffur.<br>
Die Linien wurden ausgehend vom unteren linken Punkt gegen den Uhrzeigersinn  erstellt.<br>
Bei der Draft-Schraffur auf der linken Seite ist die Eigenschaft Translate auf false gesetzt.<br>
Bei der Draft-Schraffur auf der rechten Seite ist sie auf true gesetzt.
*



## Hinweise

-   Für den Moment empfiehlt es sich, eine PAT-Datei herunterzuladen. Viele können online gefunden werden. Es kann zum Beispiel eine Websuche nach **acad.pat** oder **acadiso.pat** durchgeführt werden.
-   Eine kleine PAT-Datei wird mit FreeCAD installiert: **<PROGRAMM_ORDNER>/data/Mod/TechDraw/PAT/FCPAT.pat**, wobei der **<PROGRAMM_ORDNER>** der FreeCAD-Programmordner ist:
    -   Unter Linux ist es normalerweise **/usr/share/freecad**.
    -   Unter Windows ist es normalerweise **C:\Program Files\FreeCAD**.
    -   Unter macOS ist es normalerweise **/Applications/FreeCAD**.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

Es handelt sich dabei um die folgenden Einstellungen:

-   PAT-Datei: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Mod → TechDraw → PAT → FilePattern**.
-   Muster: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Mod → TechDraw → PAT → NamePattern**.
-   Maßstab: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Mod → Draft → HatchPatternScale**.
-   Drehung: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Mod → Draft → HatchPatternRotation**.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft-Schraffur-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Hatch}}

-    {{PropertyData/de|Basis|Link}}: gibt das Objekt an, dessen Flächen schraffiert werden.

-    {{PropertyData/de|File|File}}: gibt die PAT-Datei an.

-    {{PropertyData/de|Pattern|String}}: gibt den Namen des Musters an.

-    {{PropertyData/de|Rotation|Angle}}: gibt die Drehung des Musters an.

-    {{PropertyData/de|Scale|Float}}: gibt den Maßstab des Musters an.

-    {{PropertyData/de|Translate|Bool}}: gibt an, ob die Flächen während des Schraffiervorgangs vorübergehend in die globale XY-Ebene übersetzt werden. Die Einstellung `False` kann zu falschen Ergebnissen bei nicht XY-Flächen führen.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen einer Draft-Schraffur wird die Methode `make_hatch` des Draft-Moduls verwendet:


```python
hatch = make_hatch(baseobject, filename, pattern, scale, rotation)
```

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(4000, 1000)
rectangle.MakeFace = True
filename = App.getHomePath() + "data/Mod/TechDraw/PAT/FCPAT.pat"
pattern = "Horizontal5"
hatch = Draft.make_hatch(rectangle, filename, pattern, scale=50, rotation=45)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Hatch/de
