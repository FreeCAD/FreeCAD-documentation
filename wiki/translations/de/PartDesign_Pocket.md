---
- GuiCommand   */de
   Name   *PartDesign Pocket
   Name/de   *PartDesign Tasche
   MenuLocation   *PartDesign → Objekte abziehen → Tasche
   Workbenches   *[PartDesign](PartDesign_Workbench/de.md)
   SeeAlso   *[PartDesign Aufpolsterung](PartDesign_Pad/de.md)
---

# PartDesign Pocket/de

## Beschreibung

Das Werkzeug **Tasche** beschneidet einen Volumenkörper, indem es eine Skizze oder eine Fläche eines Volumenkörpers entlang eines geraden Pfades extrudiert.

![](images/PartDesign_Pocket_example.svg ) \'\'Die Skizze mit dem Profil (A) wurde an die obere Fläche des Basis-Volumenkörpers (B) angeheftet; Ergebnis nach dem Taschenschnitt auf der rechten Seite. \'\' \'\'

## Anwendung

1.  Eine Skizze oder Fläche auswählen, die als Tasche extrudiert werden soll. Es können wahlweise auch mehrere Skizzen oder Flächen ausgewählt werden. {{Version/de|0.20}}

2.  Die Schaltfläche **<img src="images/PartDesign_Pocket.svg" width=16px> '''Tasche'''** drücken.

3.  Parameter der Tasche einstellen, siehe [Optionen](#Optionen.md) unten.

4.  
    **OK**klicken.

When selecting a single sketch, it can have multiple enclosed profiles inside a larger one, for example a rectangle with two circles inside it. But the profiles may not intersect each other. <small>(v0.20)</small> 

## Optionen

When creating a pocket, the the **Pocket parameters** dialog will be shown. It offers the following settings   *

![](images/pocket_parameters_cropped.png )

### Type

Type offers four different ways of specifying the length to which the pocket will be extruded   *

#### Dimension


<div class="mw-translate-fuzzy">

Beim Erzeugen einer Tasche bietet der Dialog **Taschenparameter** fünf verschiedene Möglichkeiten, die Länge (Tiefe) festzulegen, bis zu der die Tasche extrudiert werden soll   *

### Abmessung

Gib einen numerischen Wert für die Tiefe der Tasche ein. Die Standardrichtung für die Extrusion ist in die Auflage. Extrusionen erfolgen [normal](http   *//en.wikipedia.org/wiki/Surface_normal) zur definierenden Skizzierebene. Negative Bemaßungen sind nicht möglich. Verwende stattdessen die Option **Umgekehrt**.

### Zuerst

Die Tasche wird bis zur ersten Fläche des Trägers in Extrusionsrichtung extrudiert. Mit anderen Worten, sie wird durch das gesamte Material schneiden, bis sie eine leere Fläche erreicht.

### Durch alles 

Die Tasche schneidet durch das gesamte Material in Extrusionsrichtung. Mit der Option **Symmetrisch zur Ebene** schneidet die Tasche durch das gesamte Material in beiden Richtungen.**Hinweis   *** Aus technischen Gründen ist **Durch alles** eigentlich eine 10 Meter tiefe Tasche. Wenn Sie tiefere Taschen benötigen, verwende *Abmessung*.


</div>

#### Through all 

The pocket will extrude through all objects in the extrusion direction. With the option **Symmetric to plane** the pad will cut through all material in both directions.**Note   *** For technical reasons, *Through All* is actually a 10 meter deep pocket. If you need deeper pockets, use the type **Dimension**.

#### To first 

The pocket will extrude up to the first face of the support in the extrusion direction. In other words, it will cut through all material until it reaches an empty space.

#### Up to face 


<div class="mw-translate-fuzzy">

### Bis zur Fläche 

Die Tasche wird bis zu einer Fläche im Auflager extrudiert, die durch Anklicken ausgewählt werden kann.

### Zwei Abmessungen 

Hier kann eine zweite Länge eingegeben werden, in der die Tasche in die entgegengesetzte Richtung (in das Auflager) ausfahren soll. Auch dies kann durch Anklicken der Option **Umgekehrt** geändert werden. <small>(v0.17)</small> 


</div>

#### Two dimensions 

This allows to enter a second length in which the pocket should extend in the opposite direction (into the support). The directions can be switched by ticking the **Reversed** option.

### Length

Defines the length of the pocket. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \"). This option is only available when **Type** is either **Dimension** or **Two dimensions**.

### Offset to face 

Offset from face at which the pocket will end. This option is only available when **Type** is either **Through all**, **To first** or **Up to face**.

### Direction


<small>(v0.20)</small> 

#### Direction/edge

You can select the direction of the extrusion   *

-   **Face/Sketch normal** The sketch or face is extruded along its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used. <small>(v0.20)</small> 
-   **Select reference\...** The sketch is extruded along an edge of the 3D model. When this is method selected, you can click on any edge in the 3D model and it becomes the direction vector for the extrusion.
-   **Custom direction** The sketch is extruded along a direction that can be specified via vector values.

#### Show direction 

If checked, the pocket direction will be shown. In case the pocket uses a **Custom direction**, it can be changed.

#### Length along sketch normal 

If checked, the pocket length is measured along the sketch normal, otherwise along the custom direction.

### Symmetric to plane 

Tick the checkbox to extrude half of the given length to either side of the sketch or plane.

### Reversed

Reverses the direction of the pocket.

### Taper angle 


<small>(v0.20)</small> 

Tapers the pocket in the extrusion direction by the given angle. A positive angle means the outer pocket border gets wider. This option is only available if **Type** is either **Dimension** or **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

Limitations   *

-   Sketches containing [B-Splines](B-Splines.md) often cannot be properly tapered. This is a limitation of the [OpenCASCADE](OpenCASCADE.md) kernel that FreeCAD uses.
-   For larger angles tapering will fail if the end face of the pocket would have fewer edges than the start face/sketch.

### 2nd length 

Defines the length of the pocket in the opposite extrusion direction. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \"). This option is only available if **Type** is **Two dimensions**.

### 2nd taper angle 


<small>(v0.20)</small> 

Tapers the pocket in the opposite extrusion direction by the given angle. A positive angle means the outer pocket border gets wider. This option is only available if **Type** is **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

## Properties

-    **Type**   * Type of ways how the pocket will be extruded, see [Options](#Options.md).

-    **Length**   * Defines the length of the pocket, see [Options](#Options.md).

-    **Length2**   * Second pocket length in case the **Type** is **TwoLengths**, see [Options](#Options.md).

-    **Use Custom Vector**   * <small>(v0.20)</small>  If checked, the pocket direction will not be the normal vector of the sketch but the given vector, see [Options](#Options.md).

-    **Direction**   * <small>(v0.20)</small>  Vector of the pocket direction if **Use Custom Vector** is used.

-    **Along Sketch Normal**   * <small>(v0.20)</small>  If *true*, the pocket length is measured along the sketch normal. Otherwise and if **Use Custom Vector** is used, it is measured along the custom direction.

-    **Up To Face**   * A face the pocket will extrude up to, see [Options](#Options.md).

-    **Refine**   * True or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in **Preferences → Part design → General → Model settings**). It can be manually changed afterwards. This property will be saved with the FreeCAD document.

## Limitations


<div class="mw-translate-fuzzy">

## Begrenzungen

-   Verwende den Typ **Abmessung** oder **Durch alles**, wo immer möglich, da die anderen Typen manchmal Probleme beim Mustern verursachen.
-   Ansonsten hat die Taschen Funktion die gleichen [Begrenzungen](PartDesign_Pad/de#Begrenzungen.md) wie die Polster Funktion.


</div>





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pocket/de
