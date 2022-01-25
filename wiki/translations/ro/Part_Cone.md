---
- GuiCommand:/ro
   Name:Part Cone
   Name/ro:Part Cone
   MenuLocation:Part -> Cone
|
   Workbenches:[Part](Part_Workbench/ro.md), Complete
   SeeAlso:[Part CreatePrimitives](Part_CreatePrimitives/ro.md)
---

# Part Cone/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Un con parametric trunchiat este un element tip primitivă geometrică disponibil pe bara de instrumente Part sau în meniu (submeniul primitives) se deschide o casetă de dialog Create Primitives .


</div>

<img alt="" src=images/Otherwisedefault270degree_Part_Cone.png  style="width:300px;">


<div class="mw-translate-fuzzy">

Imaginea de mai jos prezintă un Cone Part cu parametrul \"Unghi\" setat la 270 de grade și toți ceilalți parametri sunt la valorile lor implicite.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

În atelierul Part click pe iconița <img alt="" src=images/Part_Cone.png  style="width:32px;">.


</div>


<div class="mw-translate-fuzzy">

Valorile implicite creează un con parametric trunchiat, definit de parametrii: raza1, raza2 înălțime și unghi. La creare Conul implicit va fi poziționat la origine (punctul 0,0,0). Parametrul unghi permite crearea unei porțiuni de con (este setată implicit la 360 °), iar raza 1 și 2 corespund razei de bază și respectiv razei vârfului conului trunchiat.

### Prima metodă 

Faceți clic direct pe butonul {{KEY/it|<img src="images/Part_Cone.png" width=16px>Cono}} din bara de instrumente. Creează un con standard cu raza bazei de 2 mm, raza superioară de 4 mm, înălțimea de 10 mm și centrul cercului inferior poziționat la origine (punctul 0,0,0). Parametrii pot fi modificați în fila Date din vizualizarea combinată.

### A doua metodă 

Această a doua modalitate este disponibilă și în [OpenSCAD](OpenSCAD_Workbench/it.md) Utilizați meniul {{KEY/it|<img src="images/Part_CreatePrimitives.png" width=16px> Creați primitive ... → Cone}}. Se deschide un dialog care vă permite să setați:


</div>

The cone properties can later be edited, either in the [Property editor](Property_editor.md) or by double-clicking the cone in the [Tree view](Tree_view.md).


<div class="mw-translate-fuzzy">

### Primitive Geometriche 

+++
| ![](images/PartConePrimitivesOptions_it.png ) | Cono                                                                                                                                               |
|                                                                          |                                                                                                                                                    |
|                                                                          | #### Parametri                                                                                                                                     |
|                                                                          |                                                                                                                                                    |
|                                                                          | -   raggio 1,                                                                                                                                      |
|                                                                          | -   raggio 2,                                                                                                                                      |
|                                                                          | -   altezza,                                                                                                                                       |
|                                                                          | -   angolo                                                                                                                                         |
|                                                                          |                                                                                                                                                    |
|                                                                          | #### Posizione                                                                                                                                     |
|                                                                          |                                                                                                                                                    |
|                                                                          | Espandere la voce Posizione per stabilire:                                                                                                         |
|                                                                          |                                                                                                                                                    |
|                                                                          | -   punto di posizionamento nella vista 3D,                                                                                                        |
|                                                                          | -   direzione dell\'asse del cono, x, y, z o definita dall\'utente.                                                                                |
|                                                                          |                                                                                                                                                    |
|                                                                          | Anche le dimensioni e il posizionamento del cono prodotto utilizzando le opzioni di creazione sono modificabili tramite la scheda delle proprietà. |
+++

## Opțiuni

+++
| ![](images/PartConeProperty_en.png ) |                                                                                                                                                                                                                                                                                                                                                  |
|                                                        | **Cone**                                                                                                                                                                                                                                                                                                                                                    |
|                                                        |                                                                                                                                                                                                                                                                                                                                                              |
|                                                        | -   Radius 1 - raza cercului sau arcului de cer definit de fațeta inferioară                                                                                                                                                                                                                                                                                    |
|                                                        | -   Radius 2 - raza cercului sau arcului de cerc definită de fațeta suprioară                                                                                                                                                                                                                                                                                   |
|                                                        | -   Height - înălțimea Part Cone                                                                                                                                                                                                                                                                                                                                |
|                                                        | -   Angle - numărul de grade ale arcului sau cercurilor care definesc fațeta superioară și pe cea inferioară ale conului trunchiat. Implicit 360 crează fațete circulare, o valoare mai mică va crea o porțiune a unui con, așa cum este definită de fețele superioare și inferioare, fiecare cu marginile definite de un arc cu numărul de grade și două raze. |
+++


</div>

-    **Radius 1**: Radius of the arc or circle defining the lower face

-    **Radius 2**: Radius of the arc or circle defining the upper face

-    **Height**: Height of the Part Cone

-    **Angle**: Number of degrees of the arc or circles defining the upper and lower faces of the truncated cone. The default 360° creates circular faces, a lower value will create a portion of a cone as defined by upper and lower faces each with edges defined by an arc of the number of degrees and two radii.

## Scripting

A Part Cone can be created using the following function:


```python
cone = FreeCAD.ActiveDocument.addObject("Part::Cone", "myCone")
```

-   Where {{Incode|"myCone"}} is the name for the object.
-   The function returns the newly created object.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cone/ro
