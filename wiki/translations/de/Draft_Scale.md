---
 GuiCommand:
   Name: Draft Scale
   Name/de: Draft Skalieren
   MenuLocation: Änderung , Skalieren<br>Bearbeiten , Skalieren
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Shortcut: **S** **C**
   SeeAlso: Draft_SubelementHighlight/de, Draft_Clone/de
---

# Draft Scale/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Draft_Scale.svg  style="width:24px;"> **Draft Skalieren** skaliert oder kopiert ausgewählte Objekte von einem Basispunkt aus. Im Unterelement-Modus skaliert der Befehl ausgewählte Punkte und Kanten von [Draft Linien](Draft_Line/de.md) und [Draft-Drähten](Draft_Wire/de.md).

Der Befehl kann auf 2D-Formen angewendet werden, die mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench/de.md) erstellt wurden, kann aber auch mit vielen Arten von 3D-Objekten benutzt werden, wie denen, die mit den Arbeitsbereichen [Part](Part_Workbench/de.md) oder [BIM](BIM_Workbench/de.md) erzeugt wurden.

<img alt="" src=images/Draft_Scale_example.png  style="width:400px;"> 
*Skalieren eines Objekts von einen Basispunkt aus*



## Anwendung

Siehe auch: [Draft Fangen](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Wähle wahlweise eines oder mehrere Objekte, oder ein oder mehrere Unterelemente von [Draft Linien](Draft_Line/de.md) or [Draft Linienzug](Draft_Wire/de.md).
2.  Es gibt mehrere Möglichkeiten den Befehl zu starten:
    -   Drücke die **<img src="images/Draft_Scale.svg" width=16px> [Skalieren](Draft_Scale/de.md)** Schaltfläche.
    -   [Draft](Draft_Workbench/de.md): Wähle die **Änderung → <img src="images/Draft_Scale.svg" width=16px> Skalieren** Option aus dem Menü.
    -   [BIM](BIM_Workbench/de.md): Wähle die **Modifizieren → <img src="images/Draft_Scale.svg" width=16px> Skalieren** Option aus dem Menü.
    -   Wähle die Abkürzungstaste: **S** dann **C**.
3.  Wenn du kein Objekt ausgewählt hast: wähle ein Objekt in der [3D Ansicht](3D_view/de.md).
4.  Das **Skalieren** Aufgabenfenster öffnet. Siehe [Optionen](#Options.md) für weitere Informationen.
5.  Wenn Unterelemente ausgewählt wurden: überprüfe das **Modifiziere Unterelemente** Optionsfeld um in den Unterelemente Modus zu wechseln.
6.  Wähle den Basispunkt in der [3D Ansicht](3D_view/de.md), oder gib Koordinaten ein und wähle die **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** Schaltfläche.
7.  Gib die X, Y und Z Skalierfaktoren ein.
8.  Drücke **Enter** oder die **OK** Schaltfläche um den Befehl zu beenden.



## Optionen



### Erstes Aufgabenfenster 

Alle im Aufgabenfenster vorhandenen Abkürzungstasten können geändert werden. Siehe [Draft Einstellungen](Draft_Preferences/de.md). Die hier genannten Abkürzungstasten sind die voreingestellten.

-   Um die Koordinaten des Basispunktes von Hand einzugeben, gib die X, Y und Z Komponenten ein und drücke nach jeder **Enter**. Oder du kannst die **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** Schaltfläche betätigen sobald du die gewünschten Werte hast. Es ist ratsam den Zeiger vor der Eingabe der Koordinaten aus der [3D Ansicht](3D_view/de.md) heraus zu bewegen.
-   Drücke **G** oder wähle das **Global** Optionsfeld um den globalen Modus umzuschalten. Wenn der Global Modus aktiv ist, dann sind die Koordinaten relativ zum globalen Koordinatensystem, sonst sind sie relativ zum Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md).
-   Drücke **S** um [Draft Einrasten](Draft_Snap/de.md) ein oder auszuschalten.
-   Drücke die **Abbrechen** Schaltfläche um den Befehl abzubrechen.



### Zweites Aufgabenfenster 

-   Gib um die Skalierung zu definieren die X, Y und Z Faktoren ein. Die Werte müssen größer als Null sein.
-   Markiere das **Einheitliche Skalierung** Optionsfeld um die X, Y und Z Faktoren auf den gleichen Wert einzurasten.
-   Wenn das **Ausrichtung der Arbeitsebene** Optionsfeld gewählt ist dann sind die Skalierungsfaktoren relativ zum Koordinaten System der [Arbeitsebene](Draft_SelectPlane.md), sonst sind sie relativ zum globalen Koordinatensystem.
-   Wenn das **Kopieren** Optionsfeld gewählt ist dann wird eine skalierte Kopie des Originalobjektes erzeugt. Dies funktioniert nur bei Draft Objekten die eine **Punkte** Eigenschaft haben, wie etwa [Draft Linienzug](Draft_Wire/de.md).
-   Wenn das **Unterelemente ändern** Optionsfeld gewählt ist dann verwendet der Befehl die gewählten Unterelemente an Stelle des gesamten Objektes. Die Unterelemente müssen zu [Draft Linien](Draft_Line.md) oder [Draft Linienzug](Draft_Wire/de.md) gehören.
-   Wenn das **Klon erzeugen** Optionsfeld gewählt ist dann werden skalierte [Klone](Draft_Clone/de.md) des original Objektes erzeugt. Dies funktioniert mit allen Objekttypen. Für Objekte die keine Draft Objekte sind, oder für Draft Objekte die keine **Punkte** Eigenschaft haben, **muss** dies gewählt werden.
-   Drücke die **Anfangs- und Endpunkte wählen** Schaltfläche und wähle zwei zusätzliche Punkte in der [3D Ansicht](3D_view/de.md) um die Masstabfaktoren zu berechnen. Dies überprüft automatisch das **Einheitliche Skalierung** Optionsfeld. Die X, Y und Z Skalierungsfaktoren werden daher gleich sein und auf den Abstand zwischen Basispunkt und \'von\' Punkt, dividiert durch den Abstand zwischen Basispunkt und \'bis\' Punkt gesetzt werden.
-   Drücke **Esc** oder die **Abbrechen** Schaltfläche um den Befehl abzubrechen.



## Hinweise

-   Der Befehl kann auch [Bildebenen](Image_CreateImagePlane/de.md) skalieren, aber nicht im Klon-Modus.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   Um die Basisobjekte nach dem Kopieren von Objekten wieder auszuwählen: **Bearbeiten → Einstellungen... → Draft → Allgemein → Wähle ursprüngliche Objekte nach dem Kopieren aus**.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Zum skalieren von Objekten wird die Methode `scale` des Draft-Moduls verwendet.


```python
scaled_list = scale(objectslist, scale=Vector(1,1,1), center=Vector(0,0,0), copy=False)
```

-    `objectslist`enthält die Objekte, die skaliert werden sollen. Das ist entweder ein einzelnes Objekt oder eine Liste von Objekten.

-    `scale`ist der Vektor welcher die X, Y und Z Skalierungsfaktoren definiert.

-    `center`ist der Mittelpunkt der Skalierungsoperation.

-   Falls `copy` auf `True` ist, dann werden Kopien erzeugt,anstatt die originalen Objekte zu skalieren.

-    `scaled_list`wird mit den originalen skalierten Objekten oder mit neuen Kopien zurückgeliefert. Ist abhängig von `objectslist` entweder ein einzelnes Objekt oder eine Liste von Objekten..

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

pts = [App.Vector(0, 0, 0), App.Vector(500, 500, 0), App.Vector(600, 0, 0)]
wire1 = Draft.make_wire(pts, closed=True)
doc.recompute()

scale1 = App.Vector(2.3, 0.75, 0)
wire2 = Draft.scale(wire1, scale1, copy=True)
doc.recompute()

scale2 = App.Vector(-2, -1.5, 0)
wires = Draft.scale([wire1, wire2], scale2, copy=True)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Scale/de
