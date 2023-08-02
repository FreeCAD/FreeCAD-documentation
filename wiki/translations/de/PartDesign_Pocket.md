---
- GuiCommand:
   Name: PartDesign Pocket
   Name/de: PartDesign Tasche
   MenuLocation: PartDesign -> Objekte abziehen -> Tasche
   Workbenches: PartDesign_Workbench/de
   SeeAlso: PartDesign_Pad/de
---

# PartDesign Pocket/de



## Beschreibung

Das Werkzeug **Tasche** beschneidet einen Volumenkörper, indem es eine Skizze oder eine Fläche eines Volumenkörpers entlang eines geraden Pfades extrudiert.

![](images/PartDesign_Pocket_example.svg ) *Die Skizze mit dem Profil (A) wurde an die obere Fläche des Basis-Volumenkörpers (B) angeheftet; Ergebnis nach dem Taschenschnitt auf der rechten Seite.* \'\'



## Anwendung

1.  Eine Skizze oder Fläche auswählen, die als Tasche extrudiert werden soll. Es können wahlweise auch mehrere Skizzen oder Flächen ausgewählt werden. {{Version/de|0.20}}

2.  Die Schaltfläche **<img src="images/PartDesign_Pocket.svg" width=16px> '''Tasche'''** drücken.

3.  Parameter der Tasche einstellen, siehe [Optionen](#Optionen.md) unten.

4.  
    **OK**klicken.

Wenn eine einzelne Skizze ausgewählt wird, kann sie mehrere geschlossene Konturen innerhalb einer größeren enthalten, z.B. ein Rechteck mit zwei Kreisen darin. Die Konturen dürfen sich nur nicht überlappen. {{Version/de|0.20}}



## Optionen

Während der Erstellung der Tasche wird der Dialog **Parameter der Tasche** angezeigt. Er bietet folgende Einstellungen:

![](images/pocket_parameters_cropped.png )



### Typ

Typ bietet fünf verschiedene Möglichkeiten zum Festlegen der Länge, auf die die Tasche extrudiert werden soll:



#### Abmessung

Einen numerischen Wert für die Tiefe der Tasche eingeben. Die Vorgaberichtung der Extrusion ist in den Basiskörper hinein, kann aber geändert werden, durch aktivieren der Option **Umgekehrt**. Voreingestellt ist die Richtung der Extrusion [1](http://en.wikipedia.org/wiki/Surface_normalnormal) zur maßgeblichen Skizzenebene. Dies kann durch die Angabe einer anderen **Richtung** {{Version/de|0.20}} geändert werden. Mit der Option **Symmetrisch zu einer Ebene** wird die Tasche jeweils mit der Hälfte der gegebenen Länge auf beiden Seiten der Ebene ausgeführt. Negative Längen sind nicht Möglich; stattdessen wird die Option **Umgekehrt** verwendet.



#### Durch alles 

The pocket will extrude through all objects in the extrusion direction. With the option **Symmetric to plane** the pad will cut through all material in both directions.**Note:** For technical reasons, *Through All* is actually a 10 meter deep pocket. If you need deeper pockets, use the type **Dimension**.



#### Bis zur dichtesten Objektbegrenzung 

The pocket will extrude up to the first face of the support in the extrusion direction. In other words, it will cut through all material until it reaches an empty space.



#### Bis zu Oberfläche 

Die Tasche wird bis zu einer Fläche im Modell extrudiert, die durch Anklicken ausgewählt werden kann.



#### Zwei Längen 

Dies ermöglicht die Eingabe einer zweiten Länge, mit der die Tasche in die entgegengesetzte Richtung (in die Halterung) ausgedehnt werden soll. Die Richtung kann durch Aktivieren der Option **Umgekehrt** geändert werden.



### Länge

Definiert die Tiefe der Tasche. Die Maßeinheiten können unabhängig von den Benutzervorgaben in den Einstellungen angegeben werden (m, cm, mm, nm, ft oder \', in oder \"). Diese Option ist nur verfügbar, wenn als **Typ** entweder **Abmessung** oder **Zwei Längen** gewählt wurde.



### Abstand zur Fläche 

Abstand zu der Fläche, an der die Tasche enden soll. Diese Option ist nur verfügbar, wenn als **Typ** entweder **Durch alles**, **Bis zur dichtesten Objektbegrenzung**, oder **Bis zur Oberfläche** gewählt wurde.



### Richtung


{{Version/de|0.20}}



#### Richtung/Kante

Für die Richtung der Extrusion steht Folgendes zur Auswahl:

-   **Face/Sketch normal** The sketch or face is extruded along its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used. <small>(v0.20)</small> 
-   **Select reference\...** The sketch is extruded along an edge of the 3D model. When this is method selected, you can click on any edge in the 3D model and it becomes the direction vector for the extrusion.
-   **Custom direction** The sketch is extruded along a direction that can be specified via vector values.



#### Richtung anzeigen 

Wenn Aktiviert, wird die Richtung der Tasche angezeigt. Falls die Tasche eine **benutzerdefinierte Richtung** verwendet, kann diese geändert werden.



#### Länge entlang der Skizzennormale 

Wenn Aktiviert, wird die Länge der Tasche entlang der Skizzennormale gemessen, sonst entlang der benutzerdefinierten Richtung.



### Symmetrisch zur Ebene 

Diese Option extrudiert jeweils die halbe Gesamtlänge auf beiden Seiten der Skizze oder Ebene.



### Umgekehrt

Kehrt die Richtung der Tasche um.



### Schrägungswinkel


{{Version/de|0.20}}

Tapers the pocket in the extrusion direction by the given angle. A positive angle means the outer pocket border gets wider. This option is only available if **Type** is either **Dimension** or **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

Limitations:

-   Sketches containing [B-Splines](B-Splines.md) often cannot be properly tapered. This is a limitation of the [OpenCASCADE](OpenCASCADE.md) kernel that FreeCAD uses.
-   For larger angles tapering will fail if the end face of the pocket would have fewer edges than the start face/sketch.



### Zweite Länge 

Defines the length of the pocket in the opposite extrusion direction. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \"). This option is only available if **Type** is **Two dimensions**.



### Zweiter Schrägungswinkel 


{{Version/de|0.20}}

Tapers the pocket in the opposite extrusion direction by the given angle. A positive angle means the outer pocket border gets wider. This option is only available if **Type** is **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.



## Eigenschaften

-    **Type**: Type of ways how the pocket will be extruded, see [Options](#Options.md).

-    **Length**: Defines the length of the pocket, see [Options](#Options.md).

-    **Length2**: Second pocket length in case the **Type** is **TwoLengths**, see [Options](#Options.md).

-    **Use Custom Vector**: <small>(v0.20)</small>  If checked, the pocket direction will not be the normal vector of the sketch but the given vector, see [Options](#Options.md).

-    **Direction**: <small>(v0.20)</small>  Vector of the pocket direction if **Use Custom Vector** is used.

-    **Along Sketch Normal**: <small>(v0.20)</small>  If *true*, the pocket length is measured along the sketch normal. Otherwise and if **Use Custom Vector** is used, it is measured along the custom direction.

-    **Up To Face**: A face the pocket will extrude up to, see [Options](#Options.md).

-    **Refine**: True or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in **Preferences → Part design → General → Model settings**). It can be manually changed afterwards. This property will be saved with the FreeCAD document.



## Einschränkungen

-   Verwende den Typ **Abmessung** oder **Durch alles**, wo immer möglich, da die anderen Typen manchmal Probleme beim Mustern verursachen.
-   Ansonsten hat die Funktion Tasche die gleichen [Einschränkungen](PartDesign_Pad/de#Einschränkungen.md) wie die Funktion Polster.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pocket/de
