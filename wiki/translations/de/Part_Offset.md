---
 GuiCommand:
   Name: Part Offset
   Name/de: Part Versatz
   MenuLocation: Part , 3D-Versatz...
   Workbenches: Part_Workbench/de
   SeeAlso: Part_Thickness/de, Part_Offset2D/de
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

<img alt="" src=images/PartOffset0.png  style="width:" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:" height="200px;">

Objekt mit kleinem Versatz und abgerundeten (Bogen-) Ecken.

<img alt="" src=images/PartOffset3.png  style="width:" height="200px;">

Dasselbe Objekt mit scharfen (Schnittpunkt-) Ecken.

<img alt="" src=images/PartOffset2.png  style="width:" height="200px;">

Dasselbe Objekt mit großem Versatz, der die vordere linke Lücke überfüllt, und aktivierter Schnitt-Option.

<img alt="" src=images/PartOffset4.png  style="width:" height="200px;">

Beliebige Form ([Draft Wire](Draft_Wire/de.md)) mit einem 3D-Versatz (ignoriert MODUS-Parameter)

<img alt="" src=images/PartOffset5.png  style="width:" height="200px;">

Dieselbe Form mit einem 3D-Versatz als SKIN und *gefülltem* Versatz

<img alt="" src=images/PartOffset6.png  style="width:" height="200px;">

*gefüllter* Versatz mit 2 Zylindern, die boolesche Ausschnitte (Differenz) erstellen. Zylinder A geht durch den FÜLL-Körper, während Zylinder B auch durch den FÜLL-Körper geht aber NICHT durch die 2D-Ausgangsform.



## Eigenschaften

-    {{PropertyData/de|Offset}}: Abstand zum Versetzen der Flächen der Form.

-    {{PropertyData/de|Mode}}: Modus der Erstellung. *Oberfläche* erzeugt eine neue Form um die Ausgangsform herum. *Rohr* (in Arbeit). *RectoVerso* (in Arbeit).

-    {{PropertyData/de|Join type}}: Wie die neuen Ecken aufgebaut werden. *Schnitt* ergibt scharfe Ecken durch lineare Verlängerung der Kanten. *Kreisbogen* und *Tangente* ergeben abgerundete Ecken.

1.  Optionː Schnittː Erlaubt nach innen gerichtete Versätze, um die Lücke zu \"überfließen\", indem die resultierende Form so lange geschnitten wird, bis gegenüberliegende Flächen erreicht sind.
2.  Optionː Selbstdurchdringungː ( todo )
3.  Optionː Versatz füllenː Wenn die Form 2-dimensional war, wird die Lücke zwischen den beiden Formen gefüllt. Die Füllung ist jetzt ein Festkörper, während die Ausgangsform kein Festkörper ist. Dadurch können boolesche Operationen zu seltsamen Ergebnissen führen. (siehe Beispiel unten).





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Offset/de
