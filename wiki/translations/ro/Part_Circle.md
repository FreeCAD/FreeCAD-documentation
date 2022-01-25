# Part Circle/ro
---
- GuiCommand:   Name:Part Circle   MenuLocation:Part → [Workbenches:[[Part Workbench   Part](Part_CreatePrimitives___Create_Primitives]]_→_Circle.md),  [OpenSCAD](OpenSCAD_Workbench.md)|SeeAlso:..---


</div>


<div class="mw-translate-fuzzy">

## Descriere

Un element primitiv geometric este Circle care este disponibil din dialogul Create Primitives în Atelierul de lucru Part.


</div>

Această comandă va crea o muchie curbată circulară. Cu valorile implicite, muchia curbată circulară va fi închisă și, prin urmare, va fi un cerc. Dacă proprietățile Unghi 0 sau Unghi 1 sunt modificate din valorile implicite (0 și 360) marginea va fi o curbă deschisă, un arc de cerc.

Alternativ, un Cerc din Atelierul Part poate fi definit inițial din trei puncte. Odată creat, cercul va conține numai proprietățile standard ale cercului Part și nu va mai conține o referință la punctele de creare.

## Usage


<div class="mw-translate-fuzzy">

Dialogul Create Primitives pote fi accesat via iconiței [CreatePrimitives](Part_CreatePrimitives.md) <img alt="" src=images/Part_CreatePrimitives.png  style="width:32px;"> localizată în meniul Part sau Part toolbar, în Atelierul Part(Workbench).


</div>


<div class="mw-translate-fuzzy">

### Proprietăți

Crearea unui cerc sau a unui arc de cerc parametric.

Utilizăm meniul {{KEY/it|<img src="images/Part_CreatePrimitives.png" width=16px> Crea primitive... → Cerchio}}. Și apare o fereastră de dialog. Se deschide un dialog care vă permite să setați:

### Primitive Geometrice 

+++
| ![](images/PartCirclePrimitivesOptions_it.png ) | Cercul                                         |
|                                                                              |                                                |
|                                                                              | #### Parametri                                 |
|                                                                              |                                                |
|                                                                              | -                               |
|                                                                              |     {{Parameter|Raza}}                         |
|                                                                              |                                             |
|                                                                              |                                                |
|                                                                              | -                               |
|                                                                              |     {{Parameter|Unghiul 1}}                    |
|                                                                              |                                             |
|                                                                              |                                                |
|                                                                              | -                               |
|                                                                              |     {{Parameter|Unghiul 2}}                    |
|                                                                              |                                             |
|                                                                              |                                                |
|                                                                              | -                               |
|                                                                              |     {{Parameter|Cerc definit din trei puncte}} |
|                                                                              |                                             |
+++


</div>

-    {{Parameter|Radius}}: raza muchiei curbate (arc or circle)

-    {{Parameter|Angle 0}}: Unghiul de pornire a muchiei curbate, (degrees anti-clockwise), valoara implictă este 0

-    {{Parameter|Angle 1}}: Unghiul de capăt al muchiei curbate, (degrees sens antiorar/trigonometric), valoarea implictă este 360



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Circle/ro
