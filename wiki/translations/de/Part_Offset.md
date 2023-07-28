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

Das Werkzeug <img alt="" src=images/Part_Offset.svg  style="width:24px;"> **Part Versatz** erstellt parallele Kopien einer ausgewählten Form in einem bestimmten Abstand von der Grundform, wodurch ein neues Objekt entsteht.

<img alt="" src=images/PartOffset0.png  style="width:400" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:400" height="200px;">



## Anwendung

1.  Ein Objekt auswählen, von dem ein Versatz erstellt werden soll.
2.  Die Schaltfläche **<img src="images/Part_Offset.svg" width=16px> [3D-Versatz](Part_Offset.md)** drücken.
3.  Anpassen des Abstands und derParameter, die vom Originalobjekt abhängen sowie der Gültigkeit der resultierenden Objekte.



## Hinweise

-   [App-Link](App_Link/de.md)-Objekte, die auf geeignete Objektarten verweisen und [App-Part](App_Part/de.md)-Container, die geeignete sichtbare Objekte enthalten, können auch als Quellobjekte verwendet werden. {{Version/de|0.20}}



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



## Eigenschaften

-    {{PropertyData/de|Versatz}}: Abstand zum Versetzen der Flächen der Form.

-    {{PropertyData/de|Modus}}: Modus der Erstellung. Oberfläche erzeugt eine neue Form um die Ausgangsform herum. Rohr ( todo ). RectoVerso ( todo ).

-    {{PropertyData/de|Verknüpfungstyp}}: Wie die neuen Ecken aufgebaut werden. Schnitt ergibt scharfe Ecken durch lineare Verlängerung der Kanten. Kreisbogen und Tangente ergeben abgerundete Ecken.

1.  Optionː Schnittː Erlaubt nach innen gerichtete Versätze, um die Lücke zu \"überfließen\", indem die resultierende Form so lange geschnitten wird, bis gegenüberliegende Flächen erreicht sind.
2.  Optionː Selbstdurchdringungː ( todo )
3.  Optionː Versatz füllenː Wenn die Form 2-dimensional war, wird die Lücke zwischen den beiden Formen gefüllt. Die Füllung ist jetzt ein Festkörper, während die Ausgangsform kein Festkörper ist. Dadurch können boolesche Operationen zu seltsamen Ergebnissen führen. (siehe Beispiel unten).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Offset/de
