---
 GuiCommand:
   Name: PartDesign Pad
   Name/de: PartDesign Aufpolsterung
   MenuLocation: Part Design , Objekt hinzufügen , Aufpolsterung
   Workbenches: PartDesign_Workbench/de
   SeeAlso: PartDesign_Pocket/de
---

# PartDesign Pad/de



## Beschreibung

Das Werkzeug **Aufpolsterung** extrudiert eine Skizze oder eine Fläche eines Volumenkörpers entlang eines geraden Pfades.

![](images/PartDesign_Pad_example.svg )

*Skizze (A) links und der daraus resultierende Festkörper (B) rechts.*



## Anwendung

1.  Eine einzelne Skizze oder eine oder mehrere Flächen des Körpers auswählen.
2.  Die Schaltfläche **<img src="images/PartDesign_Pad.svg" width=16px> [Aufpolsterung](PartDesign_Pad/de.md)** drücken.
3.  Parameter der Aufpolsterung einstellen, siehe [Optionen](#Optionen.md) unten.
4.  Die Schaltfläche **OK** drücken.



## Optionen

Währen des Extrudierens oder nach einem Doppelklick auf ein bestehenden Block in der[Baumansicht](Tree_view/de.md) wird der Aufgaben-Dialog **Parameter der Aufpolsterung** angezeigt. Er bietet folgende Einstellungen:

![](images/PartDesign_Pad_Taskpanel.png )



### Typ

Typ bietet fünf verschiedene Möglichkeiten zum Festlegen der Länge des Blocks:



#### Bemaßung

Einen numerischen Wert für die **Höhe (Länge)** des Blocks eingeben. Mit der Option **Symmetrisch zu einer Ebene** wird der Block jeweils mit der Hälfte der gegebenen Länge zu beiden Seiten der Skizze oder Fläche ausgeführt.



#### Zur letzten 

Der Block wid bis zur letzten Fläche des Ausgangskörpers (Support) ausgeführt, auf die er entlang seiner Richtung trifft. Ist kein Ausgangskörpers vorhanden ist, wird eine Fehlermeldung angezeigt.



#### Zur ersten 

Der Block wird bis zur ersten Fläche des Ausgangskörpers ausgeführt, auf die er entlang seiner Richtung trifft. Wenn kein Ausgangskörper vorhanden ist, wird eine Fehlermeldung angezeigt.



#### Bis zur Fläche 

Der Block wird bis zu einer Fläche ausgeführt. Die Schaltfläche **Fläche auswählen** drücken und eine Fläche oder [Bezugsebene](PartDesign_Plane/de.md) am Körper auswählen.



#### Zwei Abmessungen 

Dies ermöglicht die Eingabe einer zweiten Länge, mit der der Block in die entgegengesetzte Richtung ausgedehnt werden soll. Die Richtung kann durch Aktivieren der Option **Umgekehrt** geändert werden.

#### Up to shape 


<small>(v1.0)</small> 

: The pad will extend up to the selected shape. Optionally press the **Select shape** button and select a shape. Leave the **Select all faces** checkbox enabled or disable it, press the **Select faces** button and select the faces up to which the pad should be created.



### Versatz zur Fläche 

Abstand zu der Fläche, an der der Block enden soll. Diese Option steht nur zur Verfügung, wenn für **Typ** entweder **Zur Letzten**, **Bis zur dichtesten Objektbegrenzung**, oder **Bis zur Oberfläche** ausgewählt wurde.



### Länge

Legt die Tiefe des Blocks fest. Diese Option steht nur zur Verfügung, wenn für **Typ** entweder **Höhe (Länge)** oder **Zwei Längen** ausgewählt wurde. Die Höhe wird entlang des Richtungsvektors oder entlang der Skizzen- oder Flächennormale gemessen. Negative Werte sind nicht möglich; stattdessen verwendet man dafür die Option **Umgekehrt**.



### Zweite Länge 

Legt die Länge des Blocks in entgegengesetzter Richtung fest. Diese Option steht nur zur Verfügung, wenn für **Typ** **Zwei Längen** ausgewählt wurde.



### Symmetrisch zur Ebene 

Diese Option auswählen, wenn jeweils die Hälfte der angegeben Länge zu beiden Seiten der Skizzenebene oder Fläche ausgeführt werden soll. Diese Option steht nur zur Verfügung, wenn für **Typ** **Abmessung** ausgewählt wurde



### Umgekehrt

Kehrt die Extrusionsrichtung um.



### Richtung



#### Richtung/Kante

Für die Richtung der Extrusion steht Folgendes zur Auswahl:

-   **Skizzennormale** oder **Flächennormale:** Die Skizze oder die Fläche wird entlang ihrer Normale extrudiert. Wurden mehrere Skizzen oder Flächen ausgewählt, wird die Normale der zuerst gewählten verwendet.
-   **Referenz auswählen\...:** Die Skizze oder die Fläche wird in Richtung einer am Körper ausgewählten geraden Kante oder einer [Bezugslinie](PartDesign_Line/de.md) extrudiert.
-   **Benutzerdefinierte Richtung:** Die Skizzeoder die Fläche wird in Richtung des des angegebenen Vektors extrudiert.



### Richtung anzeigen 

Wenn Aktiviert, wird die Richtung des Blocks angezeigt. Falls der Block eine **Benutzerdefinierte Richtung** verwendet, kann diese geändert werden.



#### Länge entlang der Skizzennormalen 

Wenn Aktiviert, wird die Länge des Blocks entlang der Skizzen- oder Flächennormale gemessen, sonst entlang der benutzerdefinierten Richtung.



### Schrägungswinkel

Schrägt die Seiten eines Blocks in Richtung der Extrusion um den gegebenen Winkel an. Ein positiver Winkel stellt die Seitenwände nach außen auf. Man beachte, dass innere Strukturen entgegengesetzt angeschrägt werden. Dies ermöglicht die Konstruktion von Gussformen und (Spritz-) Gussteilen. Diese Option steht nur zur Verfügung, wenn als **Typ** entweder **Höhe (Länge)** oder **Zwei Längen** ausgewählt wurde.



### Zweiter Schrägungswinkel 

Schrägt die Seiten eines Blocks entgegen der Extrusionsrichtung um den gegebenen Winkel an. Siehe **Schrägungswinkel**. Diese Option steht nur zur Verfügung, wenn für **Typ** auf **Zwei Längen** festgelegt wurde.



## Eigenschaften



### Daten


{{TitleProperty|Pad}}

-    **Type|Enumeration**: Art und Weise, wie ein Block extrudiert wird, siehe [Optionen](#Optionen.md).

-    **Length|Length**: legt die Länge eines Blocks fest, siehe [Optionen](#Optionen.md).

-    **Length2|Length**: zweite Länge des Blocks, falls für die {{PropertyData/de|Type}} **Zwei Längen** gewählt wurde, siehe [Optionen](#Optionen.md).

-    **Use Custom Vector|Bool**: Wenn aktiviert, wird als Richtung nicht die Skizzennormale sondern der angegebene Vektor verwendet, siehe [Optionen](#Optionen.md).

-    **Direction|Vector**: VVektor der Extrusionsrichtung, wenn die {{PropertyData/de|Use Custom Vector}} aktiviert ist.

-    **Reference Axis|LinkSub**
    

-    **Along Sketch Normal|Bool**: Wenn *true*, wird die Länge des Blocks entlang der Skizzennormale gemessen. Andernfalls und bei aktivierter {{PropertyData/de|Use Custom Vector}} wird sie entlang der benutzerdefinierten Richtung gemessen.

-    **Up To Face|LinkSub**: Eine Fläche, bis zu der der Block extrudiert wird, siehe [Optionen](#Optionen.md).

-    **Offset|Length**: Abstand zu der Fläche, an der der Block enden wird. Dies wird nur berücksichtigt, wenn als {{PropertyData/de|Type}} **Zur letzten**, **Bis zur dichtesten Objektbegrenzung** oder **Bis zu Oberfläche** ausgewählt wurde.

-    **Taper Angle|Angle**
    

-    **Taper Angle2|Angle**
    


{{TitleProperty|Part Design}}

-    **Refine|Bool**: true oder false. Beseitigt die nach der Operation verbleibenden Ränder. Dieses Verhalten wird zunächst entsprechend den Einstellungen des Benutzers festgelegt (gefunden in **>Einstellungen → Part Design → Allgemein → Modelleinstellungen**).


{{TitleProperty|Sketch Based}}

-    {{PropertyData/de|Profile|LinkSub}}
    

-    {{PropertyData/de|Midplane|Bool}}
    

-    {{PropertyData/de|Reversed|Bool}}
    

-    {{PropertyData/de|Allow Multi Face|Bool}}
    



## Begrenzungen

-   Wie alle PartDesign-Formelemente erzeugt Pad einen Festkörper, daher muss die Skizze ein geschlossenes Profil enthalten, sonst wird es mit einem Fehler \"Failed to validate broken face\" (Gescheitert beim überprüfen der gebrochenen Fläche) scheitern.
-   Skizzen,die [B-Splines](B-Splines/de.md) enthalten können oft nicht richtig abgeschrägt werden. Dies ist eine Einschränkung des [OpenCASCADE](OpenCASCADE/de.md)-Kernels, den FreeCAD einsetzt.
-   Für größere Winkel wird Abschrägen scheitern, wenn die Endfläche weniger Kanten besitzt als die Ausgangsfläche.
-   Der für **Zur ersten** und **Zur letzten** verwendete Algorithmus ist:
    -   Erzeuge eine Linie durch den Schwerpunkt der Skizze
    -   Finden alle Flächen, welche durch diese Linie geschnitten werden
    -   Wähle die Fläche, bei der der Schnittpunkt am nächsten/weitesten von der Skizze entfernt ist.

:   Das bedeutet, dass die gefundene Fläche vielleicht nicht immer das ist, was du erwartet hast. Wenn du auf dieses Problem stößt, verwende stattdessen den Typ **Bis zur Fläche** und greife die gewünschte Fläche.
:   Für den sehr speziellen Fall der Extrusion auf eine konkave Oberfläche, bei der die Skizze größer als diese Oberfläche ist, wird die Extrusion fehlschlagen. Dies ist ein ungelöster Fehler.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pad/de
