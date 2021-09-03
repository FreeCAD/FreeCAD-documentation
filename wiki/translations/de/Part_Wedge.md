---
- GuiCommand:/de
   Name:Part Wedge   Name/de:Part Wedge
   MenuLocation:Part → [Part CreatePrimitives](Part_CreatePrimitives/de.md) → Wedge
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part CreatePrimitives](Part_CreatePrimitives/de.md)
---


</div>

## Description

Erstellt ein parametrisches Keil-Objekt. Der Keil hat standardmäßig eine große quadratische Grundfläche und eine kleinere quadratische Deckfläche.

## Usage

### Start-Größe und Position {#start_größe_und_position}

**Position:** Die Standard-Orientierung platziert die Grundfläche in die XZ-Ebene und die Deckfläche in Richtung der Y-Achse. Der Nullpunkt der Grundfläche liegt in 0/0/0.

**Grundfläche:**

-   X : 10 mm
-   Z : 10 mm

**Höhe:**

-   Y : 0-10 mm

**Deckfläche:**

-   X : 2-8 mm
-   Z : 2-8 mm

![](images/PartWedgeProperty.png ) 

### Parametrische Eingaben {#parametrische_eingaben}

+------------------------------------------------------------------+-----------------------------------------------------------------+
| ![](images/PartWedgeProperty_Inputs.png ) | Zusammen mit der Standard-Orientierung stehen die Eingaben für: |
|                                                                  |                                                                 |
|                                                                  | -                                                |
|                                                                  |     {{PropertyData/de|X min/max}}                               |
|                                                                  |                                                              |
|                                                                  |     : Koordinatenwerte der unteren Fläche in X-Richtung         |
|                                                                  |                                                                 |
|                                                                  | -                                                |
|                                                                  |     {{PropertyData/de|Y min/max}}                               |
|                                                                  |                                                              |
|                                                                  |     : Lage der oberen und unteren Fläche in Y-Richtung          |
|                                                                  |                                                                 |
|                                                                  | -                                                |
|                                                                  |     {{PropertyData/de|Z min/max}}                               |
|                                                                  |                                                              |
|                                                                  |     : Koordinatenwerte der unteren Fläche in Z-Richtung         |
|                                                                  |                                                                 |
|                                                                  | -                                                |
|                                                                  |     {{PropertyData/de|X2 min/max}}                              |
|                                                                  |                                                              |
|                                                                  |     : Koordinatenwerte der oberen Fläche in X-Richtung          |
|                                                                  |                                                                 |
|                                                                  | -                                                |
|                                                                  |     {{PropertyData/de|Z2 min/max}}                              |
|                                                                  |                                                              |
|                                                                  |     : Koordinatenwerte der oberen Fläche in Z-Richtung          |
+------------------------------------------------------------------+-----------------------------------------------------------------+

### Mehr Beispiele für Keile {#mehr_beispiele_für_keile}

![](images/Wedge_examples.png )





 
