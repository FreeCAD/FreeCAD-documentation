---
- GuiCommand:/de
   Name:PartDesign Pad
   Name/de:PartDesign Aufpolsterung
   MenuLocation:Part Design → Objekt hinzufügen → Aufpolsterung
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   SeeAlso:[PartDesign Tasche](PartDesign_Pocket/de.md)
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

Währen des Extrudierens wird der Dialog **Parameter der Aufpolsterung** angezeigt. Er bietet folgende Einstellungen:

![](images/pad_parameters_cropped.png )



### Typ

Typ bietet fünf verschiedene Möglichkeiten zum Festlegen der Länge, auf welche extrudiert werden soll:



#### Bemaßung

Für die Länge der Aufpolsterung gibt man einen numerischen Wert ein. Die Standardrichtung für die Extrusion ist in Richtung der positiven Normale des extrudierten Objekts. Dies kann geändert werden, indem die Option **Umgekehrt** angekreuzt wird. Extrusionen erfolgen standardmäßig [normal](http://en.wikipedia.org/wiki/Surface_normal) zur definierenden Skizzenebene. Dies kann durch Angabe einer anderen **Richtung** geändert werden. Mit der Option **Symmetrisch zu Ebene** wird die Fläche mit jeweils der halben gegebenen Länge auf beiden Seiten der Ebene verlängert. Negative Maße sind nicht möglich. Stattdessen verwendet man die Option **Umgekehrt**.



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

Für die Richtung der Extrusion steht Folgendes zur Auswahl:

-   **Flächennormale:** Die Skizze oder die Fläche wird entlang ihrer Normale extrudiert. Wurden mehrere Skizzen oder Flächen ausgewählt, wird die Normale der zuerst gewählten verwendet. {{Version/de|0.20}}
-   **Referenz auswählen\...:** Die Skizze wird entlang einer Kante des 3D-Modells extrudiert. Ist diese Methode ausgewählt, kann man auf irgendeine Kante des 3D-Modells klicken und diese wird zum Richtungsvektor der Extrusion. {{Version/de|0.20}}
-   **Benutzerdefinierte Richtung:** Die Skizze wird entlang einer Richtung extrudiert, die durch Vektorkoordinaten bestimmt wird.



### Richtung anzeigen 

Wenn angehakt, wird die Polster Richtung angezeigt. Falls die Aufpolsterung eine **benutzerdefinierte Richtung** verwendet, kann diese geändert werden. {{Version/de|0.20}}



#### Länge entlang der Skizzennormalen 

Wenn angehakt, wird die Länge der Aufpolsterung entlang der Skizzennormalen gemessen, sonst entlang der benutzerdefinierten Richtung. {{Version/de|0.20}}



### Symmetrisch zur Ebene 

Diese Option extrudiert jeweils die halbe Gesamtlänge auf beiden Seiten der Skizze oder Ebene.



### Umgekehrt

Kehrt die Extrusionsrichtung um.



### Schrägungswinkel


{{Version/de|0.20}}

Schrägt die Seiten eines Blocks in Richtung der Extrusion um den gegebenen Winkel an. Ein positiver Winkel stellt die Seitenwände nach außen auf. Diese Option steht nur zur Verfügung, wenn als **Typ** entweder **Abmessung** oder **Zwei Längen** ausgewählt wurde. Man beachte, dass innere Strukturen entgegengesetzt angeschrägt werden. Dies ermöglicht die Konstruktion von Gussformen und (Spritz-) Gussteilen.

Einschränkungen:

-   Skizzen die [B-Splines](B-Splines/de.md) enthalten, können meistens nicht richtig angeschrägt werden. Dies ist eine Einschränkung des [OpenCASCADE](OpenCASCADE/de.md)-Kernels, den FreeCAD verwendet.
-   Bei größeren Winkeln versagt das Anschrägen, wenn dadurch die Endfläche des Blocks weniger Kanten besäße als die Startfläche bzw. Skizze.



### Zweite Länge 

Legt die Länge des Blocks entgegen der Extrusionsrichtung fest. Maßeinheiten können unabhängig von den Benutzervorgaben in den Einstellungen angegeben werden (m, cm, mm, nm, ft or \', in oder \"). Diese Option steht nur zur Verfügung, wenn als **Typ** entweder **Abmessung** oder **Zwei Längen** ausgewählt wurde.



### Zweiter Schrägungswinkel 


{{Version/de|0.20}}

Schrägt die Seiten eines Blocks entgegen der Extrusionsrichtung um den gegebenen Winkel an. Ein positiver Winkel stellt die Seitenwände nach außen auf. Diese Option steht nur zur Verfügung, wenn der **Typ** auf **Zwei Längen** festgelegt wurde. Man beachte, dass innere Strukturen entgegengesetzt angeschrägt werden. Dies ermöglicht die Konstruktion von Gussformen und (Spritz-) Gussteilen.



## Eigenschaften

-    {{PropertyData/de|Type}}: Art und Weise, wie ein Block extrudiert wird, siehe [Optionen](#Optionen.md).

-    {{PropertyData/de|Length}}: legt die Länge eines Blocks fest, siehe [Optionen](#Optionen.md).

-    {{PropertyData/de|Length2}}: zweite Länge des Blocks, falls für die {{PropertyData/de|Type}} **TwoLengths** gewählt wurde, siehe [Optionen](#Optionen.md).

-    {{PropertyData/de|Use Custom Vector}}: Wenn aktiviert, wird als Richtung nicht die Skizzennormale sondern der angegebene Vektor verwendet, siehe [Optionen](#Optionen.md).

-    {{PropertyData/de|Direction}}: Vektor der Extrusionsrichtung, wenn die {{PropertyData/de|Use Custom Vector}} aktiviert ist.

-    {{PropertyData/de|Along Sketch Normal}}: Wenn *true*, wird die Länge des Blocks entlang der Skizzennormale gemessen. Andernfalls und bei aktivierter {{PropertyData/de|Use Custom Vector}} wird sie entlang der benutzerdefinierten Richtung gemessen. {{Version/de|0.20}}

-    {{PropertyData/de|Up To Face}}: Eine Fläche, bis zu der der Block extrudiert wird, siehe [Optionen](#Optionen.md).

-    {{PropertyData/de|Offset}}: Abstand zu der Fläche, an der der Block enden wird. Dies wird nur berücksichtigt, wenn als {{PropertyData/de|Type}} **Zur letzten**, **Bis zur dichtesten Objektbegrenzung** oder **Bis zu Oberfläche** ausgewählt wurde.

-    {{PropertyData/de|Refine}}: True or false. Bereinigt die nach dem Vorgang verbleibenden Kanten. Diese Eigenschaft wird anfangs den Benutzervorgaben entsprechend festgelegt (zu finden unter **Einstellungen → Part/Part Design → Allgemein → Modelleinstellungen**). Sie kann nachträglich manuell geändert werden. Diese Eigenschaft wird mit dem FreeCAD-Dokument gespeichert.



## Begrenzungen

-   Wie alle Part Design Formelemente erzeugt Pad einen Volumenkörper, daher muss die Skizze ein geschlossenes Profil enthalten, sonst wird sie mit einem Fehler \"Failed to validate broken face\" (Gescheitert beim überprüfen der gebrochenen Fläche) auftreten.
-   Der für **Zur ersten** und **Zur letzten** verwendete Algorithmus ist:
    -   Erzeuge eine Linie durch den Schwerpunkt der Skizze
    -   Finden alle Flächen, welche durch diese Linie geschnitten werden
    -   Wähle die Fläche, bei der der Schnittpunkt am nächsten/weitesten von der Skizze entfernt ist.

:   Das bedeutet, dass die gefundene Fläche vielleicht nicht immer das ist, was du erwartet hast. Wenn du auf dieses Problem stößt, verwende stattdessen den Typ **Bis zur Fläche** und greife die gewünschte Fläche.
:   Für den sehr speziellen Fall der Extrusion auf eine konkave Oberfläche, bei der die Skizze größer als diese Oberfläche ist, wird die Extrusion fehlschlagen. Dies ist ein ungelöster Fehler.





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pad/de
