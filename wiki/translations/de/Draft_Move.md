---
- GuiCommand:/de
   Name:Draft Move
   Name/de:Draft Verschieben
   MenuLocation:Änderung → Verschieben
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:**M****V**
   Version:0.7
   SeeAlso:[Draft UnterelementHervorheben](Draft_SubelementHighlight/de.md)
---

# Draft Move/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Move.svg  style="width:24px;"> **Draft-Verschieben** verschiebt oder kopiert die ausgewählten Objekt von einem Punkt zu einem anderen. Im Unterelemente-Modus verschiebt die Anweisung ausgewählte Punkte und Kanten oder kopiert ausgewählte Kanten von [Draft Linien](Draft_Line/de.md) und [Draft Drähten](Draft_Wire/de.md).

Die Anweisung kann auf 2D-Formen, die mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench/de.md) erstellt wurden, angewendet werden, aber auch auf viele 3D-Objekte, wie jenen, die mit den Arbeitsbereichen [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md) oder [Arch](Arch_Workbench/de.md) erzeugt wurden.

<img alt="" src=images/Draft_Move_example.jpg  style="width:400px;"> 
*Verschieben eines Objekts von einem Punkt zu einem anderen Punkt*



## Anwendung

Siehe auch: [Draft Fangen](Draft_Snap/de.md) and [Draft Beschränken](Draft_Constrain/de.md).

1.  Wahlweise ein oder mehrere Objekte auswählen, oder ein oder mehrere Unterelemente einer [Draft Linie](Draft_Line/de.md) oder eines [Draft Drahtes](Draft_Wire/de.md).
2.  Es gibt mehrere Moglichkeiten die Anweisung auszuführen:
    -   Die Schaltfläche **<img src="images/Draft_Move.svg" width=16px> [Draft Verschieben](Draft_Move/de.md)** drücken.
    -   Den Menüeintrag **Änderung → <img src="images/Draft_Move.svg" width=16px> Verschieben** auswählen.
    -   Die Tastenkombination: **M** dann **V**.
3.  Wenn noch kein Objekt ausgewählt wurde: ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.
4.  Der Aufgabenbereich **Verschieben** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
5.  Wenn Unterelemente ausgewählt wurden: die Check-Box **Unterelemente ändern** aktivieren, um in den Unterelemente-Modus umzuschalten.
6.  Den ersten Punkt, den Basispunkt, in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und auf die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** klicken.
7.  Den zweiten Punkt, den Zielpunkt, in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und auf die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** klicken.



## Optionen

Das jeweilige Verhalten eines Tastaturkürzels, das hier genannt wird kann geändert sein. Siehe [Entwurf Einstellungen](Draft_Preferences/de.md).

-   To manually enter coordinates enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   To use polar coordinates enter a value for the **Length** and a value for the **Angle**, and press **Enter** after each.
-   Check the **Angle** checkbox to constrain the pointer to the specified angle.
-   Press **H** to change the focus from the **X** input box to the **Length** input box and back. Depending on the input box that receives the focus the **Angle** checkbox is checked or unchecked.
-   Press **R** or click the **Relative** checkbox to toggle relative mode. If relative mode is on, the coordinates of the second point are relative to the first point, else they are relative to the coordinate system origin.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **T** or click the **Continue** checkbox to toggle continue mode. If continue mode is on, the command will restart after finishing. This mode really only makes sense if copy mode is switched on. Depending on the **Select base objects after copying** preference, either the original objects are selected for the next command call or the copies that were created last. See [Preferences](#Preferences.md).
-   Press **P** or click the **Copy** checkbox to toggle copy mode. If copy mode is on, the command will create moved copies instead of moving the original objects.
-   Press **D** or click the **Modify subelements** checkbox to toggle subelement mode. If subelement mode is on, the command will use the selected subelements instead of the whole objects. The subelements must belong to [Draft Lines](Draft_Line.md) or [Draft Wires](Draft_Wire.md).
-   If copy mode and subelement mode are both on, and edges of [Draft Wires](Draft_Wire.md) are selected, new wires will be created from those edges.
-   Holding down **Alt** after picking the base point will also toggle copy mode. While **Alt** is held down multiple target points can be picked. Release **Alt** to finish the command and see the created copies.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press **Esc** or the **Close** button to abort the command.



## Hinweise

-   Ein Objekt, das [angehängt](Part_EditAttachment/de.md) ist, kann nicht mit der Draft Verschieben Anweisung verschoben werden. Um es trotzdem zu verschieben, muss sein unterstützendes **Support** Object verschoben werden, oder seine **Attachment Offset** geändert werden.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Entwurf Einstellungen](Draft_Preferences/de.md).

-   Um die Anzahl der Dezimalstellen für die Eingabe der Koordinaten, wie Längen und Winkel zu ändern, ist die Eigenschaft: **Edit → Preferences... → General → Units → Units settings → Number of decimals** einzustellen.
-   Um den Fokus beim Öffnen der Aufgabenansicht auf **Length** zu legen, ist die Eigenschaft: **Edit → Preferences... → Draft → General settings → Draft tools options → Set focus on Length instead of X coordinate** anzupassen. Beachte, dass der Zeiger in der [3D Ansicht](3D_view/de.md) bewegt werden muss, um die Auswirkung sehen zu können.
-   Um die gleiche Kopiermethode über alle Anweisungen zu speichern und wieder zu verwenden, ist die Eigenschaft: **Edit → Preferences... → Draft → General settings → Draft tools options → Global copy mode** einzustellen.
-   Um die Origialobjekte nach dem Kopieren zu markieren, ist die Eigenschaft: **Edit → Preferences... → Draft → General settings → Draft tools options → Select base objects after copying** einzustellen.



## Skripten

Siehe auch: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um Objekte zu verschieben, benutze die `move`-Methode des Entwurfmodules.


```python
moved_list = move(objectslist, vector, copy=False)
```

-    `objectslist`enthält die zu verschiebenden Objekte. Es kann ein einzelnes Objekt oder es können mehrere Objekte sein.

-    `vector`ist der Versatz.

-   Wenn `copy` `True` ist, werden Kopien erstellt, anstatt die Originale der Objekte zu verschieben.

-    `moved_list`gibt die verschobenen Originale oder die neuen Kopien aus. Es ist ein einzelnes Objekt oder eine Liste von Objekten, abhängig von `objectslist`.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)

Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon2, App.Vector(1000, -1000, 0))
Draft.move(polygon3, App.Vector(-500, -500, 0))

list1 = [polygon1, polygon2, polygon3]

vector = App.Vector(-2000, -2000, 0)
list2 = Draft.move(list1, vector, copy=True)
list3 = Draft.move(list1, -2*vector, copy=True)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Move/de
