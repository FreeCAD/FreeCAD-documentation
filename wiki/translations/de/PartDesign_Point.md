---
- GuiCommand:/de
   Name:PartDesign Point
   Name/de:PartDesign Bezugspunkt erstellen
   MenuLocation:Part Design → Bezugspunkt erstellen
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign Bezugslinie](PartDesign_Line/de.md), [PartDesign Bezugsebene](PartDesign_Plane/de.md)
---

# PartDesign Point/de


</div>

## Beschreibung

Erstellt einen Bezugspunkt. Dieser kann innerhalb des aktuellen Körpers referenziert werden. Dies gilt ebenfalls für weitere Referenzobjekte.

![](images/DatumPoint.png ) 
*Ein Referenzpunkt, der mit einem Offset von {{Value|2* in Z Richtung die Kugel am Z Scheitelpunkt referenziert.}}

## Anwendung

1.  Klicke auf das **<img src="images/PartDesign_Point.svg" width=24px> '''Erstellen eines neuen Bezugspunkts'''** Icon.
2.  Definiere die Parameter des Punkts. Wähle erst einen Referenzpunkt und dann einen der möglichen Modi
3.  Je nach Referenz gibt es verschiedene Aufhängemodi. Der wahrscheinlichste ist vorselektiert (Fettschrift ) . Der gewählte Modus erscheint als Hinweis in der Ziel über der Referenzauswahl.
4.  Um weitere Referenzen zu wählen, auf das nächste **Reference** Icon klicken und ein Objekt auswählen.
5.  Falls nötig wiederum einen Modus wählen und einen Offset eingeben.
6.  Mit **OK** abschliessen.

## Optionen


<div class="mw-translate-fuzzy">

Doppel-Klicke das Referenzpunkt Label im Modellbaum oder klicke dies einfach und selektiere \"Bezug ändern\" oder wähle ein Referenzobjekt mit der rechten Maustaste im Kontextmenu. Details findet man bei Referenzmodus und Offsets , siehe: [Attachment](Part_Attachment.md).


</div>

## Eigenschaften

-    {{PropertyData/de|MapMode}}: Listet die benutzten Referenzmodi.

-    {{PropertyData/de|Attachment Offset}}: Transformiert ( Verschiebung und Rotation ) das Objekt in Bezug auf seinen Referenzpunkt und seine Richtung.

-    {{PropertyData/de|Label}}: änderbarer Name des Objekts

## Einschränkungen

-   Der Bezugspunkt kann nicht als Referenz für Rohr und Loft Features benutzt werden.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Point/de
