---
- GuiCommand:/de
   Name:Part Offset
   Name/de:Part Versatz
   MenuLocation:Formteil → 3D-Versatz...
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part Dicke](Part_Thickness/de.md), [Part 2D-Versatz](Part_Offset2D/de.md)
---

# Part Offset/de

## Beschreibung

Das Werkzeug Teil 3D Versatz erzeugt parallele Kopien einer ausgewählten Form in einem bestimmten Abstand von der Grundform, wodurch ein neues Objekt entsteht.

<img alt="" src=images/PartOffset0.png  style="width:400" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:400" height="200px;">

## Anwendung

1.  Wähle das Objekt, von dem du den Versatz erstellen möchtest.
2.  Drücke die **<img src="images/Part_Offset.svg" width=16px> '''3D Versatz'''** Schaltfläche
3.  Passe Abstand und Parameter in Abhängigkeit vom Originalobjekt und der Gültigkeit der resultierenden Objekte an.

## Eigenschaften

-    {{PropertyData/de|Versatz}}: Abstand zum Versetzen der Flächen der Form

-    {{PropertyData/de|Modus}}: Modus der Erstellung . Hülle erzeugt eine neue Form um die Ausgangsform herum. Rohr ( todo ) . RectoVerso ( todo )

-    {{PropertyData/de|Verbinde Typ}}: Wie die neuen Ecken aufgebaut werden. Schnittpunkt ergibt scharfe Ecken durch lineare Verlängerung der Kanten. Bogen und Tangente ergeben abgerundete Ecken.

1.  Option ː Schnittpunkt ː Erlaubt nach innen gerichtete Versätze, um die Lücke zu \"überfluten\", indem die resultierende Form so lange geschnitten wird, bis gegenüberliegende Flächen erreicht sind.
2.  Option ː Selbstüberschneidung ː ( todo )
3.  Option ː Fülle Versatz ː Wenn die Form 2 dimensional war, wird die Lücke zwischen den beiden Formen gefüllt. Die Füllung ist jetzt ein Festkörper, daher ist die Ausgangsform kein Festkörper, so dass boolesche Operationen zu seltsamen Ergebnissen führen können. (siehe Beispiel unten) .

## Beispiele

Objekt mit kleinem Versatz und abgerundeten ( Bogen ) Ecken.

<img alt="" src=images/PartOffset0.png  style="width:400" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:400" height="200px;"> 

Gleiches Objekt mit scharfen ( Schnittpunkt ) Ecken.

<img alt="" src=images/PartOffset3.png  style="width:400" height="200px;"> 

Gleiches Objekt mit dickem Abstand, der die vordere linke Lücke überfüllt und Schnittpunkte zulässt.

<img alt="" src=images/PartOffset2.png  style="width:400" height="200px;"> 

Willkürliche Form ( Entwurf Poly als Draht ) mit einem 3D Versatz ( ignoriert MODE param )

<img alt="" src=images/PartOffset4.png  style="width:400" height="200px;"> 

dieselbe Form mit einem 3D Versatz als SKIN und *gefülltem* Versatz

<img alt="" src=images/PartOffset5.png  style="width:400" height="200px;"> 

*gefüllter* Versatz mit 2 Zylindern, die boolesche Schnitte erzeugen. Zylinder A geht durch die FÜLLUNG, während Zylinder B nur durch die FÜLLUNG geht und NICHT durch die 2D Ausgangsform.

<img alt="" src=images/PartOffset6.png  style="width:400" height="200px;">



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Offset/de
