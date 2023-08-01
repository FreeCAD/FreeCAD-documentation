---
- GuiCommand:/de
   Name:Part XOR
   Name/de:Part XOdeR
   MenuLocation:Formteil → Teilen → BooleanXOR
   Workbenches:[Part](Part_Workbench/de.md)
   Version:0.17
   SeeAlso:[Part BoolescheFragmente](Part_BooleanFragments/de.md), [Part Zerschneiden](Part_Slice/de.md), [Part AuswahlVerbindungsmethoden](Part_CompJoinFeatures/de.md), [Part Boolesche Operationen](Part_Boolean/de.md)
---

# Part XOR/de

## Beschreibung

Der Befehl <img alt="" src=images/Part_XOR.svg  style="width:24px;"> **Part XOdeR** entfernt Geometrie, die von einer geraden Anzahl von objekten geteilt wird und hinterlässt leeren Raum zwischen den beteiligten Objekten. Für zwei Objekte stellt dies eine symmetrische Version von [Part Differenz](Part_Cut/de.md) dar.

<img alt="" src=images/Part_XOR-01.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Part_XOR-02.png  style="width:300px;"> 
*Drei überlappende Objekte → Resultierendes Objekt*

## Anwendung

1.  Zwei oder mehr Objekte auswählen. Es is auch möglich einen [Part Verbund](Part_Compound/de.md) auszuwählen, der zwei oder mehr Objekte enthält.
2.  Es gibt mehrere Möglichkeiten den Befehl zu aktivieren:
    -   Den Menüeintrag **Formteil → Teilen → <img src="images/Part_XOR.svg" width=16px> Boolean XOR** auswählen.
    -   Die Schaltfläche **<img src="images/Part_XOR.svg" width=16px> [Boolean XOR](Part_XOR/de.md)** drücken.

## Hinweise

-   Leere Räume sind schwer zu finden, wenn die ausgewählten Objekte keine komplanaren Deckflächen haben. Das XOdeR-Ergebnis kann mit [Std Schnittebene](Std_ToggleClipPlane/de.md) überprüft werden.

## Eigenschaften

## Skripten



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part XOR/de
