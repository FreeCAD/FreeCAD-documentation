---
- GuiCommand:/de
   Name:Draft Trimex
   Name/de:Draft Trimex
   MenuLocation:Änderung → Trimex
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:**T** **R**
   SeeAlso:[Part Extrudieren](Part_Extrude/de.md)
---

# Draft Trimex/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Draft_Trimex.svg  style="width:24px;"> **Draft Trimex** [beschneidet oder verlängert ](#Beschneiden_oder_verlängern.md) ein ausgewähltes Objekt. Schnittstellen mit einem anderen Objekt können zum Bestimmen neuer Endpunkte verwendet werden. Der Befehl kann auch verwendet werden, um eine Fläche zu [extrudieren](#Extrudieren.md); in so einem Fall erstellt er ein [Part Extrude](Part_Extrude/de.md)-Objekt.

<img alt="" src=images/Draft_trimex_example.jpg  style="width:400px;"> 
*Oben: ein Draft-Draht verlängert und dann beschnitten.<br>
Unten: eine Fläche zu einem Festkörper extrudiert.*



## Beschneiden oder verlängern 



### Anwendung

1.  Wahlweise ein Objekt auswählen. Das Objekt muss eine [Draft-Linie](Draft_Line/de.md), ein [Draft-Draht](Draft_Wire/de.md), ein [Draft-Bogen](Draft_Arc/de.md) oder ein [Draft-Kreis](Draft_Circle/de.md) sein (nur diese lassen sich trimmen). Ist das ausgewählte Objekt geschlossen, muss seine {{PropertyData/de|Make Face}} auf `False` gesetzt werden.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Trimex.svg" width=16px> [Trimex](Draft_Trimex.md)** drücken.
    -   Den Menüeintrag **Änderung → <img src="images/Draft_Trimex.svg" width=16px> Trimex** auswählen.
    -   Das Tastaturkürzel **T** dann **R**.
3.  Wurde noch kein Objekt ausgewählt: Ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.
4.  Der Aufgabenbereich **Trimex** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
5.  Den Mauszeiger in der [3D-Ansicht](3D_view/de.md) bewegen, damit die Vorschau dem gewünschten Ergebnis entspricht. Wenn nötig, die unter [Optionen](#Optionen.md) beschriebenen Auswahltasten verwenden.
6.  Eine der folgenden Möglichkeiten ausführen:
    -   Einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Einen **Abstand** oder einen **Winkel** eingeben. Der Abstand ist ein Delta-Abstand. Diese Option funktioniert nicht wenn Auswahltasten verwendet werden.
    -   Den Mauszeiger über eine Kante, die zu einem anderen Objekt gehört, bewegen und klicken, wenn diese hervorgehoben wird, um das ausgewählte Objekt zu beschneiden bzw. zu verlängern, mit der hervorgehobenen Kante als neuen Endpunkt. Beim Beschneiden wird das standardmäßige Ergebnis von der Projektion des Punktes, an dem die Schnittlinie ausgewählt wurde, auf das zu beschneidende Objekt bestimmt. Dabei ist zu beachten, dass [Draft-Fangfunktionen](Draft_Snap/de.md) hier einen unschönen Einfluss haben können. In einigen Fällen kann es nützlich sein, sie zeitweilig abzuschalten.



### Optionen

The single character keyboard shortcut and the modifier keys mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

-   Hold down **Alt** to invert the default result of the command.
-   Hold down **Shift** to restrict the operation to the current segment of a [Draft Wire](Draft_Wire.md).
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.

Here is an example to explain the modifier keys. The left edge or the bottom edge of the U-shaped wire was extended. All [Draft Snaps](Draft_Snap.md) were turned off.

![](images/Draft_Trimex_example2.png )

1.  Der Bogen wurde nahe der unteren linken Ecke des Drahtes angeklickt. Dies ist das Standardmäßige Ergebnis.

2.  
    **Alt**wurde gedrückt gehalten, während der Bogen nahe der unteren linken Ecke des Drahtes angeklickt wurde.

3.  
    **Y**wurde gedrückt und Während der Mauszeiger über der Linken Kante schwebte, wurde **Shift** gedrückt gehalten und dann der Bogen angeklickt. Das Drücken von **Y** ist nur für Kanten erforderlich, die mehr oder weniger parallel zur Y-Achse sind.



## Extrudieren



### Anwendung 

Siehe auch: [Draft Fangen](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  It can be helpful to first change the [Draft working plane](Draft_SelectPlane.md) so that it is not coplanar with the face you want to extrude.
2.  Optionally select a single face or an object with a single face.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Trimex.svg" width=16px> [Draft Trimex](Draft_Trimex.md)** button.
    -   Select the **Modification → <img src="images/Draft_Trimex.svg" width=16px> Trimex** option from the menu.
    -   Use the keyboard shortcut: **T** then **R**.
4.  If you have not yet selected an object or a face: select an object with a single face in the [3D view](3D_view.md).
5.  The **Trimex** task panel opens. See [Options](#Options_2.md) for more information.
6.  To define the extrusion direction and distance do one of the following:
    -   Pick a point in the [3D view](3D_view.md) that does no lie on the same plane as the face.
    -   Make sure the pointer is on the correct side of the face in the [3D view](3D_view.md) and enter a **Distance**.



### Optionen 

The modifier key mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

-   Hold **Shift** to extrude in a direction that is not parallel to the normal of the face.



## Einstellungen

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of the distance: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Es gibt keine Python-Methode zum Trimmen von Objekten. Um Objekte zu extrudieren, wird die Methode `extrude` des Draft-Moduls verwendet.


```python
extrusion = extrude(obj, vector, solid=False)
```

-    `obj`is the object to be extruded.

-    `vector`is the extrusion direction and distance.

-   If `solid` is `True` a solid is created instead of a shell.

-    `extrusion`is returned with the created object.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(1500, 500)
doc.recompute()

vector = App.Vector(0, 0, 300)
solid = Draft.extrude(rectangle, vector, solid=True)
doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Trimex/de
