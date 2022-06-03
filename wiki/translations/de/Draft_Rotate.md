---
- GuiCommand   */de
   Name   *Draft Rotate
   Name/de   *Entwurf Drehen
   MenuLocation   *Modification → Drehen
   Workbenches   *[Entwurf](Draft_Workbench/de.md), [Architektur](Arch_Workbench/de.md)
   Shortcut   ***R****O**
   Version   *0.7
   SeeAlso   *[Entwurf UnterelementMarkieren](Draft_SubelementHighlight/de.md)
---

# Draft Rotate/de

## Beschreibung

Die <img alt="" src=images/Draft_Rotate.svg  style="width   *24px;"> **Entwurf Drehen** Anweisung dreht oder kopiert die ausgewählten Objekte um ein Zentrum in einem gegebenen Winkel. Im Unterelementemodus dreht die Anweisung ausgewählte Punkte und Kanten oder Kopien von ausgewählten Kanten um [Linien](Draft_Line/de.md) und [Drähte](Draft_Wire/de.md).

Das Anweisung kann auf 2D-Formen angewendet werden, die mit dem [Draft](Draft_Workbench/de.md)- oder [Skizzierer](Sketcher_Workbench/de.md)-Arbeitsbereich erstellt wurden, kann aber auch mit vielen Arten von 3D-Objekten benutzt werden, wie die mit dem [Part](Part_Workbench/de.md)- oder [Arch](Arch_Workbench/de.md)-Arbeitsbereich erzeugten.

<img alt="" src=images/Draft_Rotate_example.jpg  style="width   *400px;"> 
*Drehen eines Objekts um en Zentrum*

## Anwendung

Siehe auch   * [Entwurf Fang](Draft_Snap/de.md) und [Entwurf Beschränken](Draft_Constrain/de.md).

1.  Ein oder mehrere Objekte oder Unterelemente als [Linien](Draft_Line/de.md) oder [Drähte](Draft_Wire/de.md) auswählen.
2.  Es gibt mehrere Wege, die Anweisung auszuführen   *
    -   Auf die Schaltfläche **<img src="images/Draft_Rotate.svg" width=16px> [Entwurf Drehen](Draft_Rotate/de.md)** klicken.
    -   Den Menüpunkt **Modification → <img src="images/Draft_Rotate.svg" width=16px> Drehen** wählen.
    -   Das Tastenkürzel **R** dann **O** verwenden.
3.  Wenn noch kein Objekt gewählt wurde, dann eines in der [3D-Ansicht](3D_view/de.md) wählen.
4.  Die **Drehen**-Ansicht wird geöffnet. Siehe auch [Optionen](#Options.md).
5.  Wenn Unterelemente gewählt wurden   * über das **Modify subelements**-Auswahlkästchen das Unterelementmenü aktivieren.
6.  Den ersten Punkt, das Zentrum der Drehung, in der [3D-Ansicht](3D_view/de.md) wählen oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** anklicken.
7.  Den zweiten Punkt in the [3D-Ansicht](3D_view/de.md) wählen oder einen **Basiswinkel** eingeben.
8.  Den dritten Punkt in der [3D-Ansicht](3D_view/de.md) wählen oder eine **Drehung** eingeben.

## Optionen

Die hier erwähnten Tastenkombinationen für einzelne Zeichen und die Modifikatortaste können geändert werden. Siehe [Entwurf Einstellungen](Draft_Preferences/de.md).


<div class="mw-translate-fuzzy">

-   Zur manuellen Eingabe der Koordinaten des Zentrums der Drehung einfach die X-, Y- und Z-Komponente eingeben und jeweils **Enter** drücken. Oder die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen**-Schaltfläche betätigen, wenn die gewünschten Werte für den einzufügenden Punkt eingegeben sind. Es ist ratsam, vor der Eingabe der Koordinaten, den Mauszeiger außerhalb der [3D-Ansicht](3D_view/de.md) zu setzen.
-   Das **Relative**-Auswahlkästchen hat zu diese Anweisung keine Bedeutung.
-   Drücke **G** oder setze das **Global**-Auswahlkästchen, um in den globalen Modus zu schalten. Ist der globale Modus gesetzt, werden die Koordinaten relativ zum globalen Koordinatensystem verwendet. Umgekehrt werden sie relativ zum Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md) verwendet. <small>(v0.20)</small> 
-   Die **T**-Taste betätigen oder das **Continue**-Auswahlkästchen setzen, um in den \"Nächstes-Modus\" zu schalten. Ist der Nächstes\_Modus gesetzt, wird die Anweisung nach dem Beenden wieder aufgerufen. Dieser Modus ist nur bei einem aktiven Kopiermodus sinnvoll. Abhängig von der **Select base objects after copying / Wähle grundlegende Objekte nach dem Kopieren**-Einstellung werden entweder die grundlegenden Objekte oder die zuletzt erstellten Kopien für den nächsten Aufruf der Anweisung gewählt. Siehe [Einstellungen](#Preferences.md).
-   Die **P**-Taste betätigen oder das **Copy**-Auswahlkästchen setzen, um in den Kopiermodus zu schalten. Ist der Kopiermodus gesetzt, werden gedrehte Kopien anstelle gedrehter Originalobjekte erstellt.
-   Die **D**-Taste betätigen oder das **Modify subelements / Unterelemente anpassen**-Auswahlkästchen setzen, um in den Unterelementemodus zu schalten. Ist der Modus Einzelelemente gesetzt, werden die gewählten Elemente anstatt des ganzen Objektes verwendet. Die Unterelemente müssen [Linien](Draft_Line/de.md) oder [Drähte](Draft_Wire/de.md) sein.
-   Wenn der Kopiermodus und der Unterelementemodus aktiv sind, werden die [Drähte](Draft_Wire/de.md) ausgewählt. Neue Drähte werden aus diesen Drähten erstellt.
-   Durch Halten der **ALT**-Taste nach der Eingabe des **Base angle / grundlegenden Winkels** wird ebenfalls in den Kopiermodus geschalten. Wenn die **ALT**-Taste gehalten wird, können mehrere Punkte für die **Rotation / Drehung** gewählt werden. Nach dem Lösen der **ALT**-Taste wird die Anweisung abgeschlossen und die erstellten Kopien werden angezeigt.
-   Drücken der **S**-Taste schaltet das [Fangen](Draft_Snap/de.md) ein oder aus.
-   Drücken der **ESC**-Taste oder durch Klicken auf die {{button|Schließen}}-Schaltfläche wird die aktuelle Anweisung abgebrochen.


</div>

## Hinweise

-   Ein Objekt das [angehängt](Part_EditAttachment/de.md) ist, kann nicht mit der Drehen-Anweisung gedreht werden. Entweder sein {{PropertyData/de|Support}}-Objekt wird gedreht, oder sein {{PropertyData/de|Attachment Offset}} wird geändert, um es zu drehen.

## Einstellungen

Siehe auch   * [Editor Einstellungen](Preferences_Editor/de.md) und [Entwurf Einstellungen](Draft_Preferences/de.md).

-   To change the number of decimals used for the input of coordinates and angles   * **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To store and reuse the same copy mode setting across commands   * **Edit → Preferences... → Draft → General settings → Draft tools options → Global copy mode**.
-   To reselect the base objects after copying objects   * **Edit → Preferences... → Draft → General settings → Draft tools options → Select base objects after copying**.

## Skripten

Siehe auch   * [Autogenerated API documentation](https   *//freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Verwende die `Drehen`-Methode des Entwurfmodules, um Objekte zu drehen.


```python
rotated_list = rotate(objectslist, angle, center=Vector(0,0,0), axis=Vector(0,0,1), copy=False)
```


<div class="mw-translate-fuzzy">

-   Dreht den Basispunkt der Objekte in der angegebenen Liste `objectlist` mit dem angegebenen Winkel `angle` um das Rotationszentrum.
    -   
        `objectlist`
        
        kann ein einzelnes Objekt oder eine Liste von Objekten sein.

    -   Wenn ein Rotationszentrum (`center`) und `axis` gegeben sind, werden sie verwendet, ansonten bezieht sich die Drehung auf den Ursprung und um die Z-Achse.

   *   Der Drehungswinkel bezieht sich auf den Basispunkt des Objektes. Wenn also ein Objekt um 45 Grad gedreht wird und dann ein weiteres Mal um 45 Grad gedreht wird, wird es insgesamt um 90 Grad zu ihrer Ursprungsposition gedreht sein.

-   Wenn `copy` `True` ist, werden Kopien erstellt anstatt die originalen Objekte zu drehen.
-   Eine `rotatedlist` wird mit den gedrehten Originalen oder mit den neuen Kopien gemeldet.
    -   
        `rotatedlist`
        
        ist entweder ein einzelnes Objekt oder eine Liste von Objekten, abhängig von der Eingabe `objectlist`.


</div>

Beispiel   *


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=300)
Draft.move(polygon1, App.Vector(1000, 0, 0))

# Rotation around the origin
angle1 = 45
rot2 = Draft.rotate(polygon1, angle1, copy=True)
rot3 = Draft.rotate(polygon1, 2*angle1, copy=True)
rot4 = Draft.rotate(polygon1, 4*angle1, copy=True)

polygon2 = Draft.make_polygon(3, radius=1000)
polygon3 = Draft.make_polygon(5, radius=500)
Draft.move(polygon2, App.Vector(2000, 0, 0))
Draft.move(polygon3, App.Vector(2000, 0, 0))

# Rotation around another point
angle2 = 60
cen = App.Vector(3100, 0, 0)
list2 = [polygon2, polygon3]
rot_list2 = Draft.rotate(list2, angle2, center=cen, copy=True)
rot_list3 = Draft.rotate(list2, 2*angle2, center=cen, copy=True)
rot_list4 = Draft.rotate(list2, 4*angle2, center=cen, copy=True)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rotate/de
