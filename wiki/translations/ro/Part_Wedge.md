---
- GuiCommand:
   Name:Part Wedge
   MenuLocation:Part → Create primitives → Wedge
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Part Primitives](Part_Primitives.md)
---


</div>

## Description

Creați un obiect parametric Pană/Wedge. Valoarea implicită pentru această reținere este o bază pătratică mai mare și un vârf pătrat mai mic.

## Usage

### Dimensiuni și Plasamente implicite 

**Plasament:** Orientarea implicită plasează baza în planul XZ, iar partea superioară în direcția axei Y. Colțul de bază implicit este originea 0,0,0.

**Fațeta de bază:**

-   X : 10 mm
-   Z : 10 mm

**Înălțimea:**

-   Y : 0-10 mm

**Fațeta Superioară:**

-   X : 2-8 mm
-   Z : 2-8 mm

![](images/PartWedgeProperty.png ) 

### Intrări Parametrice 

+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ![](images/PartWedgeProperty_Inputs.png ) | Utilizând destinația de plasare prestabilită, intrările de mai jos sunt:                                                        |
|                                                                  |                                                                                                                                 |
|                                                                  | -                                                                                                                |
|                                                                  |     **X min/max**                                                                                                  |
|                                                                  |                                                                                                                              |
|                                                                  |     : Base face X axis span                                                                                                     |
|                                                                  |                                                                                                                                 |
|                                                                  | -                                                                                                                |
|                                                                  |     **Y min/max**                                                                                                  |
|                                                                  |                                                                                                                              |
|                                                                  |     : Wedge height span                                                                                                         |
|                                                                  |                                                                                                                                 |
|                                                                  | -                                                                                                                |
|                                                                  |     **Z min/max**                                                                                                  |
|                                                                  |                                                                                                                              |
|                                                                  |     : Base face Z axis span                                                                                                     |
|                                                                  |                                                                                                                                 |
|                                                                  | -                                                                                                                |
|                                                                  |     **X2 min/max**                                                                                                 |
|                                                                  |                                                                                                                              |
|                                                                  |     : Top face X axis span                                                                                                      |
|                                                                  |                                                                                                                                 |
|                                                                  | -                                                                                                                |
|                                                                  |     **Z2 min/max**                                                                                                 |
|                                                                  |                                                                                                                              |
|                                                                  |     : Top face Z axis span                                                                                                      |
|                                                                  |                                                                                                                                 |
|                                                                  | #### Poziția                                                                                                                    |
|                                                                  |                                                                                                                                 |
|                                                                  | Extindeți elementul Poziție pentru a stabili:                                                                                   |
|                                                                  |                                                                                                                                 |
|                                                                  | -   punctul de poziționare în vizualizarea 3D, în mod implicit, colțul din stânga jos al bazei este poziționat în punctul 0,0,0 |
|                                                                  | -   direcția axei wedge, x, y, z sau definite de utilizator.                                                                    |
|                                                                  |                                                                                                                                 |
|                                                                  | Parametrii și poziționarea pot fi modificate prin fila/tab-ul Proprietăți.                                                      |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+

### Proprietăți

+----------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ![](images/PartWedgeProperty_it.png ) | #### Vizualizări                                                                           |
|                                                          |                                                                                            |
|                                                          | Sunt disponibile [Proprietà standard](DraftStandardProperty/it.md) în vizualizare. |
|                                                          |                                                                                            |
|                                                          | #### Date                                                                                  |
|                                                          |                                                                                            |
|                                                          |                                                                             |
|                                                          | {{KEY/it|Base}}                                                                            |
|                                                          |                                                                                         |
|                                                          | \* {{ProprietaDati|Label}}: nume                                             |
|                                                          |                                                                                            |
|                                                          | -                                                                           |
|                                                          |     {{ProprietaDati|Placement}}                                                            |
|                                                          |                                                                                         |
|                                                          |     : [posizionamento](Placement/it.md)                                            |
|                                                          |                                                                                            |
|                                                          |                                                                             |
|                                                          | {{KEY/it|Wedge}}                                                                           |
|                                                          |                                                                                         |
|                                                          | \* {{ProprietaDati|X2 max}} : coordonată (valoarea predefinită este 8 mm).   |
|                                                          |                                                                                            |
|                                                          | -                                                                           |
|                                                          |     {{ProprietaDati|X2 min}}                                                               |
|                                                          |                                                                                         |
|                                                          |     : coordonată (predefinită e 2 mm).                                                     |
|                                                          |                                                                                            |
|                                                          | -                                                                           |
|                                                          |     {{ProprietaDati|X max}}                                                                |
|                                                          |                                                                                         |
|                                                          |     : coordonată (predefinită e 10 mm).                                                    |
|                                                          |                                                                                            |
|                                                          | -                                                                           |
|                                                          |     {{ProprietaDati|X min}}                                                                |
|                                                          |                                                                                         |
|                                                          |     : coordonată (predefinită e 0 mm).                                                     |
|                                                          |                                                                                            |
|                                                          | -                                                                           |
|                                                          |     {{ProprietaDati|Y max}}                                                                |
|                                                          |                                                                                         |
|                                                          |     : coordonată (predefinită e 10 mm).                                                    |
|                                                          |                                                                                            |
|                                                          | -                                                                           |
|                                                          |     {{ProprietaDati|Y min}}                                                                |
|                                                          |                                                                                         |
|                                                          |     : coordonată (predefinită e 2 mm).                                                     |
|                                                          |                                                                                            |
|                                                          | -                                                                           |
|                                                          |     {{ProprietaDati|Z2 max}}                                                               |
|                                                          |                                                                                         |
|                                                          |     : coordonată (predefinită e 8 mm).                                                     |
|                                                          |                                                                                            |
|                                                          | -                                                                           |
|                                                          |     {{ProprietaDati|Z2 min}}                                                               |
|                                                          |                                                                                         |
|                                                          |     : coordonată (predefinită e 2 mm).                                                     |
|                                                          |                                                                                            |
|                                                          | -                                                                           |
|                                                          |     {{ProprietaDati|Z max}}                                                                |
|                                                          |                                                                                         |
|                                                          |     : coordonată (predefinită e 10 mm).                                                    |
|                                                          |                                                                                            |
|                                                          | -                                                                           |
|                                                          |     {{ProprietaDati|Z min}}                                                                |
|                                                          |                                                                                         |
|                                                          |     : coordonată (valoarea predefinită e 0 mm).                                            |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------+

### Mai multe exemple de pene 

![](images/Wedge_examples.png )





 
