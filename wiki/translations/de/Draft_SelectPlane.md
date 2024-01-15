---
 GuiCommand:
   Name: Draft SelectPlane
   Name/de: Draft EbeneAuswählen
   MenuLocation: Dienstprogramme , Ebene wählen
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **W** **P**
   SeeAlso: Draft_WorkingPlaneProxy/de
---

# Draft SelectPlane/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_SelectPlane.svg  style="width:24px;"> **Draft EbeneAuswählen** legt die aktuelle Arbeitsebene fest. Dies ist die Ebene in der [3D-Ansicht](3D_view/de.md) auf der neue [Draft](Draft_Workbench.md)-Objekte erstellt werden. Eine Arbeitsebene kann auf einer oder mehreren [Voreinstellungen](#Anwendung_mit_Voreinstellungen.md) basieren oder auf einer Auswahl. Die Auswahl kann vor dem Aufruf des Befehls erfolgen ([Vorauswahl](#Anwendung_mit_Vorauswahl.md)) oder danach ([nachträgliche Auswahl](#Anwendung_mit_nahträglicher_Auswahl.md)).


{{Version/de|0.22}}

: Zu jeder 3D-Ansicht wird eine eigene Arbeitebene gespeichert.

Die Schaltfläche ![](images/Draft_tray_button_plane.png ) im [Draft Tray](Draft_Tray.md) ändert sich abhängig von der aktuellen Arbeitsebene. {{Version/de|0.22}}: Ist die Arbeitsebene nicht auf **Auto** gesetzt, wird der Benennung der Schaltfläche ein Stern (*****) vorangestellt, wenn der Ursprung der Arbeitsebene nicht dem globalen Ursprung entspricht.

<img alt="" src=images/WorkingPlane_example.png  style="width:400px;"> 
*Formen die auf unterschiedlichen Arbeitsebenen erstellt wurden*



## Anwendung mit Vorauswahl 

1.  Eine der folgenden Möglichkeiten ausführen:
    -   Ein einzelnes Objekt auswählen. Die folgenden Objekte werden unterstützt:
        -   [Draft ArbeitsebenenProxies](Draft_WorkingPlaneProxy/de.md): Die {{PropertyView/de|View Data}} (die Kameraposition) und die {{PropertyView/de|Visibility Map}} (die gespeicherten Sichtbarkeitseinstellungen von Objekten) des Arbeitseben-Proxys werden ebenfalls wiederhergestellt.
        -   [Arch Achsen](Arch_Axis/de.md) ({{Version/de|0.22}})
        -   [Arch Achsensysteme](Arch_AxisSystem/de.md) ({{Version/de|0.22}})
        -   [Arch Gebäudeteile](Arch_BuildingPart/de.md)
        -   [Arch Schnittebenen](Arch_SectionPlane/de.md)
        -   [Std Teile](Std_Part/de.md): Sollen nicht nur die angeklickten Subelemente ausgewählt werden, wird empfohlen Std-Teile in der [Baumansicht](Tree_view/de.md) auszuwählen.
        -   Nicht-Festkörper-Objekte, die aus einer einzelnen ebenen Fläche oder einer einzelnen gekrümmten Kante bestehen oder ({{Version/de|0.22}}) die mindestens drei Knoten enthalten.
        -   Festkörper-Objekte oder Objekte ohne eine Form, die eine {{PropertyData/de|Placement}} besitzen. ({{Version/de|0.22}})
    -   Ein oder mehrere Unterelemente auswählen. Zur Wahl stehen:
        -   Eine ebene Fläche.
        -   Eine gekrümmte Kante.
        -   Drei Knotenpunkte.
        -   Eine Kante und ein Knoten oder zwei Kanten. Die Knoten müssen zusammen eine Ebene definieren. ({{Version/de|0.22}})
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche ![](images/Draft_tray_button_plane.png ) im [Draft Tray](Draft_Tray/de.md) drücken.
    -   Den Menüeintrag **Dienstprogramme → <img src="images/Draft_SelectPlane.svg" width=16px> Ebene wählen** auswählen.
    -   Das Tastaturkürzel **W** dann **P**.
3.  Die Arbeitsebene und die Schaltfläche in der [Draft Tray](Draft_Tray/de.md) werden aktualisiert.



## Anwendung mit nachträglicher Auswahl 

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche ![](images/_Draft_tray_button_plane.png ) im [Draft Tray](Draft_Tray/de.md) drücken.
    -   Den Menüeintrag **Dienstprogramme → <img src="images/Draft_SelectPlane.svg" width=16px> Ebene wählen** auswählen.
    -   Das Tastaturkürzel **W** dann **P**.
2.  Der Aufgaben-Bereich **Arbeitsebene einrichten** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Eine der folgenden Möglichkeiten ausführen:
    -   Ein einzelnes Objekt auswählen. Siehe den [vorherigen Absatz](#Anwendung_mit_Vorauswahl.md).
    -   Ein oder mehrere Unterelemente auswählen. Siehe den [vorherigen Absatz](#Anwendung_mit_Vorauswahl.md).
4.  An eine beliebige Stelle in der [3D-Ansicht](3D_view/de.md) klicken, um die Auswahl zu bestätigen und den Befehl zu beenden.
5.  Die Arbeitsebene und die Schaltfläche im [Draft Tray](Draft_Tray/de.md) werden aktualisiert.



## Anwendung mit Voreinstellungen 

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche ![](images/Draft_tray_button_plane.png ) im [Draft Tray](Draft_Tray/de.md) drücken.
    -   Den Menüeintrag **Dienstprogramme → <img src="images/Draft_SelectPlane.svg" width=16px> Ebene wählen** auswählen.
    -   Das Tastaturkürzel **W** dann **P**.
2.  Der Aufgaben-Bereich **Arbeitsebene einrichten** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Eine der Schaltflächen drücken, um den Befehl zu beenden.
4.  Die Arbeitsebene und die Schaltfläche im [Draft Tray](Draft_Tray/de.md) werden aktualisiert.



## Optionen

-   Die Schaltfläche **<img src="images/View-top.svg" width=16px> Oben (XY)** drücken, um die Arbeitsebene zur XY-Ebene des globalen Koordinatensystems auszurichten.

-   Die Schaltfläche **<img src="images/View-front.svg" width=16px> Front (XZ)** drücken, um die Arbeitsebene zur XZ-Ebene des globalen Koordinatensystems auszurichten.

-   Die Schaltfläche **<img src="images/View-right.svg" width=16px> Seite (YZ)** drücken, um die Arbeitsebene zur YZ-Ebene des globalen Koordinatensystems auszurichten.

-   Die Schaltfläche **<img src="images/View-isometric.svg" width=16px> Zur Ansicht ausrichten** drücken, um die Arbeitsebene zur aktuellen [3D-Ansicht](3D_view/de.md) auszurichten. Ist die Checkbox **Ebene in Ansicht zentrieren** nicht aktiviert, ist der Ursprung der Arbeitsebene deckungsgleich mit dem Ursprung des globalen Koordinatensystems, andernfalls ist er deckungsgleich mit der Mitte der aktuellen [3D-Ansicht](3D_view/de.md).

-   Die Schaltfläche **<img src="images/View-axonometric.svg" width=16px> Automatisch** drücken, um die Arbeitsebene auf **Auto** zu setzen. Eine auf **Auto** gesetzte Arbeitsebene wird automatisch zur aktuellen [3D-Ansicht](3D_view/de.md) ausgerichtet, wann immer ein Draft- oder [Arch](Arch_Workbench/de.md)-Befehl gestartet wird, der eine Punkteingabe erfordert. Dies ist entspricht dem Drücken der Schaltfläche **<img src="images/View-isometric.svg" width=16px> Zur Ansicht ausrichten**, bevor der Befehl verwendet wird. Außerdem richtet sich die Arbeitsebene zu ebenen Flächen aus, die vor dem Start des Befehls ausgewählt wurden, oder wenn während der Ausführung des Befehls Punkte auf ebenen Flächen ausgewählt werden.

-    **Versetzen**legt den senkrechten Abstand zwischen der berechneten Ebene und der tatsächlichen Arbeitsebene fest.

-   Die Checkbox **Center plane on view** aktivieren, um den Ursprung der Arbeitsebene auf den Mittelpunkt der aktuellen [3D-Ansicht](3D_view/de.md) zu setzen. Diese Option kann in Kombination mit der Schaltfläche **<img src="images/View-isometric.svg" width=16px> Zur Ansicht ausrichten** nützlich sein.

-   Einen Knoten in der [3D-Ansicht](3D_view/de.md) auswählen und die Schaltfläche **<img src="images/Draft_Move.svg" width=16px> Move working plane** drücken, um die die Arbeitsebene so zu versetzen, dass ihr Ursprung auf dem ausgewählten Knoten liegt.

-    **Rasterabstand**legt den Abstand zwischen den Rasterlinien fest.

-   Der Wert **Hauptlinien alle** legt fest, wo Hauptrasterlinien gezeichnet werden. Hauptrasterlinien sind geringfügig dicker, als normale Rasterlinen. Ist z.B. der Rasterabstand {{Value|0.5 m}} und es gibt eine Hauptlinie alle {{Value|10}} Linien, treten die Hauptlinien alle {{Value|5 m}} auf.

-   Der Wert **Grid extension** legt die Anzahl der Rasterlinien in X- und Y-Richtung des Rasters fest.

-   Der **Einrast-Radius** ist der maximale Abstand, den [Draft EinrastenAufRaster](Draft_Snap_Grid/de.md) berücksichtigt, um die Schnittstellen der Rasterlinien zu finden.

-   Die Schaltfläche **<img src="images/view-fullscreen.svg" width=16px> Ansicht zentrieren** drücken, um die [3D-Ansicht](3D_view/de.md) zur aktuellen Arbeitsebene auszurichten.

-   Die Schaltfläche **<img src="images/sel-back.svg" width=16px> Vorherige** drücken, um die Arbeitsebene auf ihre vorherige Position zurückzusetzen.

-   Die Schaltfläche **Next <img src="images/sel-forward.svg" width=16px>** drücken, um die Arbeitsebene auf ihre nachfolgende Position zu setzen. {{Version/de|0.22}}

-    **Esc**oder die Schaltfläche **Close** drücken, um den Befehl abzubrechen.



## Hinweise

-   Es kann sinnvoll sein, die [3D-Ansicht](3D_view/de.md) zur ausgewählten Arbeitsebene auszurichten. Beispielsweise stellt man nach dem setzen der Arbeitsebene auf Front auch für die Ansicht auf die [Vorderansicht](Std_ViewFront.md) um.
-   Das Raster kann mit dem Befehl [Raster ein-/ausblenden](Draft_ToggleGrid/de.md) umgeschaltet werden.
-   Durch Doppelklicken auf [Draft Arbeitsebenen-Proxies](Draft_WorkingPlaneProxy/de.md) in der [Baumansicht](Tree_view/de.md) kann schnell zwischen Arbeitsebenen gewechselt werden.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   Die Rastereinstellungen im Aufgaben-Bereich und auch einige andere Rastereinstellungen stehen als Voreinstellungen zur Verfügung: **Bearbeiten → Einstellungen... → Draft → Raster und Einrasten**.
-   Der Einrastradius kann auch \"on-the-fly\" geändert werden (see [Draft Einrasten](Draft_Snap/de#Einstellungen.md)) oder durch **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Mod → Draft → snapRange**.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


{{Version/de|0.22}}

Das Modul WorkingPlane (Arbeitsebene) enthält zwei Klassen zur Erstellung von Arbeitsebenen (working plane objects): Die Klasse `PlaneBase` und die Klasse `PlaneGui`. Die zweite Klasse ist von der ersten abgeleitet. Objekte der Klasse `PlaneGui` arbeiten mit der GUI (Schaltfläche im [Draft Tray](Draft_Tray/de.md)), der [3D-Ansicht](3D_view.md) und dem [Raster](Draft_Snap_Grid/de.md) zusammen. `PlaneBase`-Objekte tun dies nicht.

Die Methode `get_working_plane()` der Arbeitsebene wird verwendet, um eine Instanz der Klasse `PlaneGui` zu erhalten, die mit der 3D-Ansicht verknüpft ist. Die Methode gibt entweder die vorhandene Arbeitsebene zurück, die mit der Ansicht verknüpft ist, oder erstellt eine neue Arbeitsebene, fallls erforderlich.


```python
import FreeCAD as App
import WorkingPlane

wp = WorkingPlane.get_working_plane()

origin = App.Vector(0, 0, 0)
normal = App.Vector(1, 1, 1).normalize()
offset = 17
wp.align_to_point_and_axis(origin, normal, offset)

point = App.Vector(10, 15, 2)
projection = wp.project_point(point)
print(projection)
```

Die Klasse `PlaneBase` kann verwendet werden, um Arbeitsebenen unabhängig von der GUI zuerstellen:


```python
import WorkingPlane

wp = WorkingPlane.PlaneBase()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SelectPlane/de
