---
- GuiCommand   */de
   Name   *PartDesign Pad
   Name/de   *PartDesign Aufpolsterung
   MenuLocation   *Part Design → Objekt hinzufügen → Aufpolsterung
   Workbenches   *[PartDesign](PartDesign_Workbench/de.md)
   SeeAlso   *[PartDesign Tasche](PartDesign_Pocket/de.md)
---

# PartDesign Pad/de

## Beschreibung

Das Werkzeug **Aufpolsterung** extrudiert eine Skizze oder eine Fläche eines Volumenkörpers entlang eines geraden Pfades.

![](images/PartDesign_Pad_example.svg )

*Skizze (A) links und der daraus resultierende Festkörper (B) rechts.*

## Anwendung

1.  Eine Skizze oder Fläche auswählen, die extrudiert werden soll. Es können wahlweise auch mehrere Skizzen oder Flächen ausgewählt werden. {{Version/de|0.20}}

2.  Die Schaltfläche **<img src="images/PartDesign_Pad.svg" width=16px> [Aufpolsterung](PartDesign_Pad/de.md)** drücken.

3.  Parameter der Aufpolsterung einstellen, siehe [Optionen](#Optionen.md) unten.

4.  
    **OK**klicken.

Wenn eine einzelne Skizze ausgewählt wird, kann sie mehrere geschlossene Konturen innerhalb einer größeren enthalten, z.B. ein Rechteck mit zwei Kreisen darin. Die Konturen dürfen sich nur nicht überlappen. {{Version/de|0.20}}

## Optionen

Währen des Extrudierens wird der Dialog **Parameter der Aufpolsterung** angezeigt. Er bietet folgende Einstellungen   *

![](images/pad_parameters_cropped.png )

### Typ

Typ bietet fünf verschiedene Möglichkeiten zum Festlegen der Länge, auf welche extrudiert werden soll   *

#### Bemaßung

Für die Länge der Aufpolsterung gibt man einen numerischen Wert ein. Die Standardrichtung für die Extrusion ist in Richtung der positiven Normale des extrudierten Objekts. Dies kann geändert werden, indem die Option **Umgekehrt** angekreuzt wird. Extrusionen erfolgen standardmäßig [normal](http   *//en.wikipedia.org/wiki/Surface_normal) zur definierenden Skizzenebene. Dies kann durch Angabe einer anderen **Richtung** geändert werden. Mit der Option **Symmetrisch zu Ebene** wird die Fläche mit jeweils der halben gegebenen Länge auf beiden Seiten der Ebene verlängert. Negative Maße sind nicht möglich. Stattdessen verwendet man die Option **Umgekehrt**.

#### Zur letzten 

Das Pad extrudiert bis zur letzten Fläche des Ausgangskörpers in Extrusionsrichtung. Wenn keine solche Fläche vorhanden ist, wird eine Fehlermeldung angezeigt.

#### Zur ersten 

Die Aufpolsterung wird in Extrusionsrichtung bis zur ersten Seite des tragenden Objekts extrudiert. Wenn keine Fläche vorhanden ist, wird eine Fehlermeldung angezeigt.

#### Bis zur Fläche 

Die Aufpolsterung wird zu einer Fläche im Modell extrudiert, die durch Anklicken ausgewählt werden kann.

#### Zwei Abmessungen 

Dies ermöglicht die Eingabe einer zweiten Länge, in der sich die Aufpolsterung in die entgegengesetzte Richtung (in die Halterung) erstrecken soll. Auch hier kann die Länge durch anhaken der **Umgekehrt** Option geändert werden.

### Länge

Definiert die Länge der Extrusion. Die Maßeinheiten können unabhängig von den Benutzervorgaben in den Einstellungen angegeben werden (m, cm, mm, nm, ft oder \', in oder \"). Diese Option ist nur verfügbar, wenn als **Typ** entweder **Abmessung** oder **Zwei Längen** gewählt wurde.

### Versatz zur Fläche 

Versatz von der Fläche, an der die Aufpolsterung enden soll. Diese Option ist nur verfügbar, wenn als **Typ** entweder **Zur letzten**, **Zur ersten** oder **Bis zur Fläche** gewählt wurde.

### Richtung

#### Richtung/Kante

You can select the direction of the extrusion   *

-   **Face/Sketch normal** The sketch or face is extruded along its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used. <small>(v0.20)</small> 
-   **Select reference\...** The sketch is extruded along an edge of the 3D model. When this is method selected, you can click on any edge in the 3D model and it becomes the direction vector for the extrusion. <small>(v0.20)</small> 
-   **Custom direction** The sketch is extruded along a direction that can be specified via vector values. <small>(v0.19)</small> 

### Richtung anzeigen 

Wenn angehakt, wird die Polster Richtung angezeigt. Falls die Aufpolsterung eine **benutzerdefinierte Richtung** verwendet, kann diese geändert werden. {{Version/de|0.20}}

#### Länge entlang der Skizzennormalen 

Wenn angehakt, wird die Länge der Aufpolsterung entlang der Skizzennormalen gemessen, sonst entlang der benutzerdefinierten Richtung. {{Version/de|0.20}}

### Symmetrisch zur Ebene 


<div class="mw-translate-fuzzy">

Diese Option extrudiert die Gesamtlänge exakt hälftig in beide Richtungen.


</div>

### Umgekehrt

Kehrt die Extrusionsrichtung um.

### Taper angle 


<small>(v0.20)</small> 

Tapers the pad in the extrusion direction by the given angle. A positive angle means the outer pad border gets wider. This option is only available if **Type** is either **Dimension** or **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

Limitations   *

-   Sketches containing [B-Splines](B-Splines.md) often cannot be properly tapered. This is a limitation of the [OpenCASCADE](OpenCASCADE.md) kernel that FreeCAD uses.
-   For larger angles tapering will fail if the end face of the pad would have fewer edges than the start face/sketch.

### 2nd length 

Defines the length of the pad in the opposite extrusion direction. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \"). This option is only available if **Type** is **Two dimensions**.

### 2nd taper angle 


<small>(v0.20)</small> 

Tapers the pad in the opposite extrusion direction by the given angle. A positive angle means the outer pad border gets wider. This option is only available if **Type** is **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

## Eigenschaften


<div class="mw-translate-fuzzy">

-    **Typ**   * Art und Weise, wie das Polster extrudiert wird, siehe [Optionen](#Options.md).

-    **Länge**   * Definiert die Länge des Polsters, siehe [Optionen](#Options.md).

-    **Länge2**   * Zweite Polster Länge für den Fall, dass die **Typ** Option **ZweiLängen** verwendet wird, siehe [Optionen](#Options.md).

-    **Verwende benutzerdefinierten Vektor**   * {{Version/de|0.19}} Wenn angehakt, ist die Polster Richtung nicht der Normalenvektor der Skizze, sondern den vorgegebenen Vektor, siehe [Optionen](#Options.md).

-    **Richtung**   * <small>(v0.19)</small>  Vektor der Polster Richtung, wenn der **Verwende benutzerdefinierten Vektor** verwendet wird.

-    **Entlang der Skizzennormalen**   * {{Version/de|0.20}} Wenn *true*, wird die Polsterlänge entlang der Skizzennormalen gemessen. Andernfalls und bei Verwendung von **Benutzerdefinierten Vektor verwenden** wird sie entlang der benutzerdefinierten Richtung gemessen.

-    **Bis zur Fläche**   * Eine Fläche, bis zu der das Polster extrudiert wird, siehe [Optionen](#Options.md).

-    **Versatz**   * Versatz von der Fläche, in der das Polster enden wird. Dies wird nur berücksichtigt, wenn die **Typ** Option **BisZurLetzen**, **BisZurErsten** oder **BisZurFläche** verwendet wird.

-    **Verfeinern**   * {{VersionPlus/de|0.17}} true oder false. Bereingt überflüssige entstandene Kanten nach der Berechnung. Diese Option richtet sich nach den Vorgeben des Benutzers in den Grundeinstellungen (zu finden in *Einstellungen → Part design → Allgemein → Modelleinstellungen*). Sie kann nachträglich manuell geändert werden. Diese Eigenschaft wird mit dem FreeCAD Dokument gespeichert.


</div>

## Begrenzungen


<div class="mw-translate-fuzzy">

-   Wie alle Part Design Formelemente erzeugt Pad einen Volumenkörper, daher muss die Skizze ein geschlossenes Profil enthalten, sonst wird sie mit einem Fehler \"Failed to validate broken face\" (Gescheitert beim überprüfen der gebrochenen Fläche) auftreten. Es können mehrere geschlossene Profile in einem größeren enthalten sein, vorausgesetzt, keines überschneidet sich mit einem anderen (z.B. ein Rechteck mit zwei Kreisen darin).
-   Der für **Zur ersten** und **Zur letzten** verwendete Algorithmus ist   *
    -   Erzeuge eine Linie durch den Schwerpunkt der Skizze
    -   Finden alle Flächen, welche durch diese Linie geschnitten werden
    -   Wähle die Fläche, bei der der Schnittpunkt am nächsten/weitesten von der Skizze entfernt ist.

   *   Das bedeutet, dass die gefundene Fläche vielleicht nicht immer das ist, was du erwartet hast. Wenn du auf dieses Problem stößt, verwende stattdessen den Typ **Bis zur Fläche** und greife die gewünschte Fläche.
   *   Für den sehr speziellen Fall der Extrusion auf eine konkave Oberfläche, bei der die Skizze größer als diese Oberfläche ist, wird die Extrusion fehlschlagen. Dies ist ein ungelöster Fehler.

-    {{VersionMinus|0.16}}Es gibt keine automatische Bereinigung, z.B. benachbarter planarer Oberflächen zu einer Einzeloberfläche.

Du kannst dies manuell in der Datei <img alt="" src=images/Workbench_Part.svg  style="width   *16px;"> korrigieren. [Part Arbeitsbereich](Part_Workbench.md) mit **<img src="images/Part_RefineShape.svg" width=16px> [Part FormVerfeinern](Part_RefineShape/de.md)** (wodurch ein unverknüpfter, nichtparametrischer Körper erzeugt wird) oder mit der **<img src="images/OpenSCAD_RefineShapeFeature.svg" width=16px>  [OpenSCAD FormVerfeinernFormelement](OpenSCAD_RefineShapeFeature/de.md)** aus der Datei <img alt="" src=images/Workbench_OpenSCAD.svg  style="width   *16px;"> [OpenSCAD Arbeitsbereich](OpenSCAD_Workbench/de.md), das ein parametrisches Formelement erzeugt.


</div>





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pad/de
