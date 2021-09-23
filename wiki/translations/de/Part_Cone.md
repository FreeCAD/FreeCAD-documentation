---
- GuiCommand:/de
   Name:Part Cone
   Name/de:Part Kegel
   MenuLocation:Formteil → Grundkörper → Kegel
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part Grundkörper](Part_Primitives/de.md)
---

# Part Cone/de

## Beschreibung

Ein parametrischer abgeschnittener Part Kegelgrundkörper ist im Part Arbeitsbereich über die Part Werkzeugleiste, das Part Menü (Untermenü Grundkörper) und das Grundkörper erstellen Dialogfeld verfügbar.

<img alt="" src=images/Otherwisedefault270degree_Part_Cone.png  style="width:300px;"> 
*Ein Formteilkegel, bei dem der Parameter "Winkel" auf 270 Grad eingestellt ist und alle anderen Parameter auf ihre Standardwerte gesetzt sind.*

## Anwendung

1.  Wechsle zum <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part](Part_Workbench.md)-Arbeitsbereich.
2.  Es gibt zwei Wege, den Befehl aufzurufen:
    -   Drücke die **<img src="images/Part_Cone.svg" width=16px> [Part Kegel](Part_Cone/de.md)**-Schaltfläche
    -   Verwende den {{MenuCommand/de|Formteil → Grundkörper → <img src="images/Part_Cone.svg" width=16px> Kegel}}-Eintrag aus dem oberen Menü.

**Ergebnis:** Die Standardwerte erzeugen einen abgeschnittenen parametrischen Kegel, der am Ursprung (Punkt 0,0,0) positioniert ist und auf der xy-Ebene steht. Die Höhe von 10mm ist entlang der z-Achse . Der untere **Radius1** ist 2mm, der obere **Radius2**, ist 4mm.

Die Kegeleigenschaften können später geändert werden, entweder im [Eigenschaftseditor](Property_editor/de.md) oder durch doppelklicken des Kegels in der [Baumansicht](Tree_view/de.md).

## Eigenschaften

-    **Radius 1**: Radius des Bogens oder Kreises, der die untere Fläche definiert

-    **Radius 2**: Radius des Bogens oder Kreises, der die obere Fläche definiert

-    **Höhe**: die Höhe des Teilkegels

-    **Winkel**: die Anzahl der Grad des Bogens oder der Kreise, die die obere und untere Fläche des Kegelstumpfes definieren. Der Standardwert 360 erzeugt kreisförmige Flächen, ein niedrigerer Wert erzeugt einen Teil eines Kegels, der durch obere und untere Flächen definiert ist, deren Kanten jeweils durch einen Bogen mit der Anzahl der Grad und zwei Radien definiert sind.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cone/de
