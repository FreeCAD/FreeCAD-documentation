---
- GuiCommand:/de
   Name:Part Cut
   Name/de:Part Schnitt
   MenuLocation:Formteil → Bool'sche Operationen → Schneiden
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part Boolsche Operation](Part_Boolean/de.md), [Part Verschmelzung](Part_Fuse/de.md), [Part Schnittmenge](Part_Common/de.md)
---


</div>

## Beschreibung

Schneidet (subtrahiert) ausgewählte Teileobjekte, wobei das letzte vom ersten subtrahiert wird. Diese Operation ist voll parametrisch und die Komponenten können modifiziert und das Ergebnis neu berechnet werden.

**Hinweis:** Dieser Befehl ist eine automatisierte Form des <img alt="" src=images/Part_Booleans.svg  style="width:24px;"> [Boolesche Operation](Part_Boolean/de.md).

[480px\|left\|Schneiden](IMAGE:Part_Cut_01.png.md)

## Anwendung

1.  Wähle zwei Formen
2.  Rufe den Part Schneiden Befehl auf verschiedene Weise auf:
    -   Drücke die **![](images/) '''Schneiden'''** Schaltfläche in der Part Werkzeugleiste
    -   Verwende den {{MenuCommand/de|Part → Boolesche operation → Schneiden}} Eintrag aus dem Part Menü

## Unterstützte Eingaben 

Eingabeobjekte müssen [OpenCascade ](OpenCascade/de.md) Formen sein. Beispiele: Sachen, die mit den Arbeitsbereichen Part, PartDesign, Skizzierer erstellt wurden. Keine Polygonnetze (es sei denn, diese wurden in Formen umgewandelt) - für Polygonnetze gibt es spezielle boolesche Werkzeuge im Arbeitsbereich Netzkonstruktion.


<div class="mw-translate-fuzzy">





</div>


  
