---
 GuiCommand:
   Name: PartDesign Pocket
   Name/de: PartDesign Tasche
   MenuLocation: PartDesign , Objekte abziehen , Tasche
   Workbenches: PartDesign_Workbench/de
   SeeAlso: PartDesign_Pad/de
---

# PartDesign Pocket/de



## Beschreibung

Das Werkzeug **Tasche** beschneidet einen Volumenkörper, indem es eine Skizze oder eine Fläche eines Volumenkörpers entlang eines geraden Pfades extrudiert.

![](images/PartDesign_Pocket_example.svg ) *Die Skizze mit dem Profil (A) wurde an die obere Fläche des Basis-Volumenkörpers (B) angeheftet; Ergebnis nach dem Taschenschnitt auf der rechten Seite.* \'\'



## Anwendung

1.  Eine einzelne Skizze oder eine oder mehrere Flächen des Körpers auswählen.
2.  Die Schaltfläche **<img src="images/PartDesign_Pocket.svg" width=16px> [Tasche](PartDesign_Pocket/de.md)** drücken.
3.  Parameter der Tasche einstellen, siehe [Optionen](#Optionen.md) unten.
4.  Die Schaltfläche **OK** drücken.



## Optionen

Während der Erstellung der Tasche oder nach einem Doppelklick auf eine bestehende Tasche in der [Baumansicht](Tree_view/de.md) wird der Aufgaben-Dialog **Parameter der Tasche** angezeigt. Er bietet folgende Einstellungen:

![](images/PartDesign_Pocket_Taskpanel.png )



### Typ

Typ bietet fünf verschiedene Möglichkeiten zum Festlegen der Länge der Tasche:



#### Abmessung

Einen numerischen Wert für das **Tiefenmaß** der Tasche eingeben. Mit der Option **Symmetrisch zu einer Ebene** wird die Tasche jeweils mit der Hälfte der gegebenen Länge zu beiden Seiten der Skizze oder Fläche ausgeführt.



#### Durch alles 

The pocket will extend up to the last face of the support it encounters in its direction. With the option **Symmetric to plane** the pocket will cut through all material in both directions. Note that for technical reasons, *Through All* is actually a 10 meter deep pocket. If you need deeper pockets, use the type **Dimension**.



#### Bis zur dichtesten Objektbegrenzung 

The pocket will extend up to the first face of the support it encounters in its direction.



#### Bis zu Oberfläche 

Die Tasche wird bis zu einer Fläche ausgeführt. Die Schaltfläche **Fläche auswählen** drücken und eine Fläche oder [Bezugsebene](PartDesign_Plane/de.md) am Körper auswählen.



#### Zwei Längen 

Dies ermöglicht die Eingabe einer zweiten Länge, mit der die Tasche in die entgegengesetzte Richtung ausgedehnt werden soll. Die Richtung kann durch Aktivieren der Option **Umgekehrt** geändert werden.

#### Up to shape 


<small>(v1.0)</small> 

: The pocket will extend up to the selected shape. Optionally press the **Select shape** button and select a shape. Leave the **Select all faces** checkbox enabled or disable it, press the **Select** button and select the faces up to which the pocket should be created.



### Abstand zur Fläche 

Abstand zu der Fläche, an der die Tasche enden soll. Diese Option steht nur zur Verfügung, wenn für **Typ** entweder **Durch alles**, **Bis zur dichtesten Objektbegrenzung**, oder **Bis zur Oberfläche** ausgewählt wurde.



### Länge

Legt die Tiefe der Tasche fest. Diese Option steht nur zur Verfügung, wenn für **Typ** entweder **Tiefenmaß** oder **Zwei Längen** ausgewählt wurde. Die Tiefe wird entlang des Richtungsvektors oder entlang der Skizzen- oder Flächennormale gemessen. Negative Werte sind nicht möglich; stattdessen verwendet man dafür die Option **Umgekehrt**.



### Zweite Länge 

Defines the length of the pocket in the opposite direction. This option is only available if **Type** is **Two dimensions**.



### Symmetrisch zur Ebene 

Diese Option aktivieren, um jeweils die Hälfte der angegebenen Länge zu beiden Seiten der Skizze oder Fläche auszuführen, wenn für **Typ** entweder **Tiefe**, oder **Durch alles** ausgewählt wurde.



### Umgekehrt

Kehrt die Richtung der Tasche um.



### Richtung



#### Richtung/Kante

Für die Richtung der Extrusion steht Folgendes zur Auswahl:

-   **Sketch normal** or **Face normal:** The sketch or face is extruded in the opposite direction of its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used.
-   **Select reference\...:** The sketch or face is extruded in the opposite direction of a straight edge or a [datum line](PartDesign_Line.md) selected from the Body.
-   **Custom direction:** The sketch or face is extruded in the direction of the specified vector.



#### Richtung anzeigen 

Wenn Aktiviert, wird die Richtung der Tasche angezeigt. Falls die Tasche eine **benutzerdefinierte Richtung** verwendet, kann diese geändert werden.



#### Länge entlang der Skizzennormale 

Wenn Aktiviert, wird die Länge der Tasche entlang der Skizzen- oder Flächennormale gemessen, sonst entlang der benutzerdefinierten Richtung.



### Schrägungswinkel

Tapers the pocket in the extrusion direction by the given angle. A positive angle means the outer pocket border gets wider. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts. This option is only available if **Type** is **Dimension** or **Two dimensions**.



### Zweiter Schrägungswinkel 

Tapers the pocket in the opposite extrusion direction by the given angle. See **Taper angle**. This option is only available if **Type** is **Two dimensions**.



## Eigenschaften

### Data


{{TitleProperty|Part Design}}

-    **Refine|Bool**: True or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in **Preferences → Part Design → General → Model settings**).


{{TitleProperty|Pocket}}

-    **Type|Enumeration**: Defines how the pocket will be extruded, see [Options](#Options.md).

-    **Length|Length**: Defines the length of the pocket, see [Options](#Options.md).

-    **Length2|Length**: Second pocket length in case the **Type** is **TwoLengths**, see [Options](#Options.md).

-    **Use Custom Vector|Bool**: If checked, the pocket direction will not be the normal vector of the sketch but the given vector, see [Options](#Options.md).

-    **Direction|Vector**: Vector of the pocket direction if **Use Custom Vector** is used.

-    **Reference Axis|LinkSub**
    

-    **Along Sketch Normal|Bool**: If *true*, the pocket length is measured along the sketch normal. Otherwise and if **Use Custom Vector** is used, it is measured along the custom direction.

-    **Up To Face|LinkSub**: A face the pocket will extrude up to, see [Options](#Options.md).

-    **Offset|Length**
    

-    **Taper Angle|Angle**
    

-    **Taper Angle2|Angle**
    


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**
    

-    **Midplane|Bool**
    

-    **Reversed|Bool**
    

-    **Allow Multi Face|Bool**
    



## Einschränkungen

-   Verwende den Typ **Abmessung** oder **Durch alles**, wo immer möglich, da die anderen Typen manchmal Probleme beim Mustern verursachen.
-   Ansonsten hat die Funktion Tasche die gleichen [Einschränkungen](PartDesign_Pad/de#Einschränkungen.md) wie die Funktion Polster.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pocket/de
