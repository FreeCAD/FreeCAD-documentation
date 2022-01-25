# Part Wedge/cs
---
- GuiCommand:/cs   Name:Part Wedge   Name/cs:Díl_Klín   MenuLocation:Díl -> [|Workbenches:[[Part_Workbench/cs   Modul Díl](Part_CreatePrimitives/cs___Díl_Vytváření_zákl.geom.tvarů]] -> Klín.md)|SeeAlso:[Díl Vytváření zákl.geom.tvarů](Part_CreatePrimitives/cs.md)---


</div>

## Description

Vytváří parametrický objekt Klín. Defaultně se za základnu považuje větší plocha a menší je vrchol.

## Usage

### Defaultní rozměr a umístění 

**Umístění:** Defaultně je základna v rovině XY a vrchol vznikne ve směru osy Z. Roh základny je v počátku 0,0,0.

**Plocha základny:**

-   X : 10 mm
-   Z : 10 mm

**Výška:**

-   Y : 0-10 mm

**Plocha vrcholu:**

-   X : 2-8 mm
-   Z : 2-8 mm

![](images/PartWedgeProperty.png ) 

### Vstupní parametry 

+++
| ![](images/PartWedgeProperty_Inputs.png ) | Při využití defaultního umístění jsou vstupní parametry následující: |
|                                                                  |                                                                      |
|                                                                  | -                                                     |
|                                                                  |     **X min/max**                                       |
|                                                                  |                                                                   |
|                                                                  |     : Base face X axis span                                          |
|                                                                  |                                                                      |
|                                                                  | -                                                     |
|                                                                  |     **Y min/max**                                       |
|                                                                  |                                                                   |
|                                                                  |     : Wedge height span                                              |
|                                                                  |                                                                      |
|                                                                  | -                                                     |
|                                                                  |     **Z min/max**                                       |
|                                                                  |                                                                   |
|                                                                  |     : Base face Z axis span                                          |
|                                                                  |                                                                      |
|                                                                  | -                                                     |
|                                                                  |     **X2 min/max**                                      |
|                                                                  |                                                                   |
|                                                                  |     : Top face X axis span                                           |
|                                                                  |                                                                      |
|                                                                  | -                                                     |
|                                                                  |     **Z2 min/max**                                      |
|                                                                  |                                                                   |
|                                                                  |     : Top face Z axis span                                           |
+++

### More examples for wedges 

![](images/Wedge_examples.png )



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Wedge/cs
