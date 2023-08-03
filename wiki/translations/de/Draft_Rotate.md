---
 GuiCommand:
   Name: Draft Rotate
   Name/de: Draft Drehen
   MenuLocation: Änderung , Drehen
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **R****O**
   Version: 0.7
   SeeAlso: Draft_SubelementHighlight/de
---

# Draft Rotate/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Rotate.svg  style="width:24px;"> **Draft Drehen** dreht oder kopiert ausgewählte Objekte um ein Zentrum in einem gegebenen Winkel. Im Unterelemente-Modus dreht die Anweisung ausgewählte Punkte und Kanten oder Kopien von ausgewählten Kanten von [Draft Linien](Draft_Line/de.md) und [Draft Drähte](Draft_Wire/de.md).

Der Befehl kann auf 2D-Formen angewendet werden, die mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench/de.md) erstellt wurden, kann aber auch mit vielen Arten von 3D-Objekten benutzt werden, wie denen, die mit den Arbeitsbereichen [Part](Part_Workbench/de.md) oder [Arch](Arch_Workbench/de.md) erzeugt wurden.

<img alt="" src=images/Draft_Rotate_example.jpg  style="width:400px;"> 
*Drehen eines Objekts um einen Drehpunkt*



## Anwendung

Siehe auch: [Draft Fangen](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Wahlweise ein oder mehrere Objekte auswählen oder Unterelemente von [Draft Linien](Draft_Line/de.md) oder [Draft Drähten](Draft_Wire/de.md).
2.  Es gibt mehrere Möglichkeiten den Befehl auszuführen:
    -   Die Schaltfläche **<img src="images/Draft_Rotate.svg" width=16px> [Drehen](Draft_Rotate/de.md)** klicken.
    -   Den Menüeintrag **Änderung → <img src="images/Draft_Rotate.svg" width=16px> Drehen** wählen.
    -   Das Tastenkürzel **R** dann **O**.
3.  Wenn noch kein Objekt ausgewählt wurde: ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.
4.  Der Aufgabenbereich **Drehen** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
5.  Wenn Unterelemente ausgewählt wurden: die Check-Box **Unterelemente ändern** aktivieren, um in den Unterelemente-Modus umzuschalten.
6.  Den ersten Punkt, das Zentrum der Drehung, in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** anklicken.
7.  Den zweiten Punkt in the [3D-Ansicht](3D_view/de.md) wählen oder einen **Basiswinkel** eingeben.
8.  Den dritten Punkt in der [3D-Ansicht](3D_view/de.md) wählen oder eine **Drehung** eingeben.



## Optionen

Die hier erwähnten Tastenkombinationen für einzelne Zeichen und die Modifikatortaste können geändert werden. Siehe [Entwurf Einstellungen](Draft_Preferences/de.md).

-   Zur manuellen Eingabe der Koordinaten des Zentrums der Drehung die X-, Y- und Z-Komponente eingeben und jeweils **Enter** drücken. Oder die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen**-Schaltfläche betätigen, wenn die gewünschten Werte für den einzufügenden Punkt eingegeben sind. Es ist ratsam, vor der Eingabe der Koordinaten, den Mauszeiger außerhalb der [3D-Ansicht](3D_view/de.md) zu setzen.
-   Drücke **G** oder setze das **Global**-Auswahlkästchen, um in den globalen Modus zu schalten. Ist der globale Modus gesetzt, werden die Koordinaten relativ zum globalen Koordinatensystem verwendet. Umgekehrt werden sie relativ zum Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md) verwendet. {{Version/de|0.20}}
-   Die **T**-Taste betätigen oder das **Continue**-Auswahlkästchen setzen, um in den \"Nächstes-Modus\" zu schalten. Ist der Nächstes_Modus gesetzt, wird die Anweisung nach dem Beenden wieder aufgerufen. Dieser Modus ist nur bei einem aktiven Kopiermodus sinnvoll. Abhängig von der **Select base objects after copying / Wähle grundlegende Objekte nach dem Kopieren**-Einstellung werden entweder die grundlegenden Objekte oder die zuletzt erstellten Kopien für den nächsten Aufruf der Anweisung gewählt. Siehe [Einstellungen](#Preferences.md).
-   Die **P**-Taste betätigen oder das **Copy**-Auswahlkästchen setzen, um in den Kopiermodus zu schalten. Ist der Kopiermodus gesetzt, werden gedrehte Kopien anstelle gedrehter Originalobjekte erstellt.
-   Die **D**-Taste betätigen oder das **Modify subelements / Unterelemente anpassen**-Auswahlkästchen setzen, um in den Unterelementemodus zu schalten. Ist der Modus Einzelelemente gesetzt, werden die gewählten Elemente anstatt des ganzen Objektes verwendet. Die Unterelemente müssen [Linien](Draft_Line/de.md) oder [Drähte](Draft_Wire/de.md) sein.
-   Wenn der Kopiermodus und der Unterelementemodus aktiv sind, werden die [Drähte](Draft_Wire/de.md) ausgewählt. Neue Drähte werden aus diesen Drähten erstellt.
-   Durch Halten der **ALT**-Taste nach der Eingabe des **Base angle / grundlegenden Winkels** wird ebenfalls in den Kopiermodus geschalten. Wenn die **ALT**-Taste gehalten wird, können mehrere Punkte für die **Rotation / Drehung** gewählt werden. Nach dem Lösen der **ALT**-Taste wird die Anweisung abgeschlossen und die erstellten Kopien werden angezeigt.
-   Drücken der **S**-Taste schaltet das [Fangen](Draft_Snap/de.md) ein oder aus.
-   Drücken der **ESC**-Taste oder durch Klicken auf die **Schließen**-Schaltfläche wird die aktuelle Anweisung abgebrochen.



## Hinweise

-   Ein Objekt das [angehängt](Part_EditAttachment/de.md) ist, kann nicht mit der Drehen-Anweisung gedreht werden. Entweder sein {{PropertyData/de|Support}}-Objekt wird gedreht, oder sein {{PropertyData/de|Attachment Offset}} wird geändert, um es zu drehen.



## Einstellungen

Siehe auch: [Editor Einstellungen](Preferences_Editor/de.md) und [Entwurf Einstellungen](Draft_Preferences/de.md).

-   Ändern der Anzahl der Nachkommastellen für die Eingabe der Koordinaten und Winkel: **Bearbeiten → Einstellungen... → Allgemein → Einheiten → Anzahl der Nachkommastellen**.
-   Speichern und Wiederverwenden der gleichen Kopiermoduseinstellungen in den Anweisungen: **Bearbeiten → Einstellungen... → Draft → Allgemeine Einstellungen → Entwurfswerkzeuge Optionen → Globaler Kopiermodus**.
-   Auswählen der Originalobjekte nach dem Kopieren: **Bearbeiten → Einstellungen... → Draft → Allgemeine Einstellungen → Entwurfswerkzeuge Optionen → Wähle ursprüngliche Objekte nach dem Kopieren aus**.



## Skripten

Siehe auch: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Verwende die `Drehen`-Methode des Entwurfmodules, um Objekte zu drehen.


```python
rotated_list = rotate(objectslist, angle, center=Vector(0,0,0), axis=Vector(0,0,1), copy=False)
```

-    `objectlist`enthält die zu drehenden Objekte. Dies ist entweder ein einzelnes Objekt oder es sind mehrere Objekte.

-    `angle`is der Winkel der Drehung in Grad.

-    `center`ist das Zentrum der Drehung.

-    `axis`ist die Richtung der Drehachse.

-   Wenn `copy` `True` ist, werden Kopien erstellt anstatt die originalen Objekte zu drehen.

-   Eine `rotatedlist` wird mit den gedrehten Originalen oder mit den neuen Kopien gemeldet. Dies ist entweder ein einzelnes Objekt oder es sind mehrere Objekte, abhängig von `objectlist`.

Beispiel:


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
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rotate/de
