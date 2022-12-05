---
- GuiCommand:/ro
   Name/ro:Arch Component
   Icon:Arch Component.svg‏‎
‏   MenuLocation:Arch → Utilities → Component‎‏‎
   Workbenches:[Arch](Arch_Workbench/ro.md)
   Shortcut:**C** **M**
---

# Arch Component/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Creează o componentă non-parametrică [ Arch](Arch_Workbench.md) din orice obiect [ Part](Part_Workbench.md). Aceasta oferă obiectului bazat pe Atelierul Part/Piesă aceleași atribute și proprietăți ca și alte obiecte Arch și permite specificarea modului în care ar trebui exportat la IFC prin setarea proprietății**Role**.


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Selectați un obiect bazat pe Atelierul [Part](Part_Workbench.md)-
2.  Selectați meniul Arch → Utilities → **<img src="images/Arch_Component.png" width=16px> [Component](Arch_Component.md)
**


</div>

## Proprietățile obișnuite ale componentei Arch 


<div class="mw-translate-fuzzy">

Obiectul componentă Arch este, de asemenea, o bază partajată de toate celelalte obiecte Arch ([ Wall](Arch_Wall.md), [ Structure](Arch_Structure.md) etc). Prin urmare, unele dintre proprietățile și comportamentele sale sunt comune tuturor obiectelor Arch (cu excepția instrumentelor care nu produc obiecte solide, cum ar fi [Section Plane](Arch_SectionPlane.md) sau [Axis](Arch_Axis.md)):


</div>


<div class="mw-translate-fuzzy">

-   **Forma de bază**: Componentele Arc sunt întotdeauna bazate pe un obiect de bază bazat pe [Formă](Part_Workbench.md). Unele tipuri de obiecte Arch vor utiliza doar forma de bază așa cum este, altele (de exemplu[Wall](Arch_Wall.md)) vor face unele operații suplimentare, cum ar fi o extrudare. Pentru unele tipuri, având un obiect de bază nu este obligatoriu ([ Structure](Arch_Structure.md))


</div>


<div class="mw-translate-fuzzy">

-   **Additions**: Componentele Arch au o proprietate aditionala, care poate tine referinta la orice alt obiect [ Shape](Part_Workbench.md). Forma acestor adăugiri va fi unită cu forma de bază a componentei, pentru a produce forma finală.


</div>


<div class="mw-translate-fuzzy">

-   **Subtractions**: Componentele arhitecturale au o proprietate de substracție/scădere, care poate deține referință la orice număr de obiecte bazate pe [Formă](Part_Workbench.md). Forma acestor obiecte va fi scăzută din forma de bază a componentei, pentru a produce forma finală.


</div>


<div class="mw-translate-fuzzy">

-   The Placement of the Arch Component is applied after the additions and subtractions are done, so these are performed against the base object at its base location. Then the result is moved to the location of the Placement


</div>


<div class="mw-translate-fuzzy">

-   Objects can be added or removed to/from a Component\'s Additions and Subtractions lists by selecting both the object and the component, and using the [Arch Add](Arch_Add.md) or [Arch Remove](Arch_Remove.md) commands, or from the task panel by double-clicking the Component in the Tree view. The task panel also allows to check which object is currently part of these lists.


</div>


<div class="mw-translate-fuzzy">

-   **Role**: Each Arch Component, besides the function defined by its type (wall, window, etc), also has a Role property, that can define further which kind of function it performs. For example, an [Structure](Arch_Structure.md) can have a beam o column role. Generic Arch Components (as produced by this command) can have any role available in the whole Arch workbench. The role is what is used to define the type of IFC object to export to when [exporting to IFC](Arch_IFC.md).


</div>


<div class="mw-translate-fuzzy">

-   **Clone Of**: Any Arch Component can be a clone of another Arch Component of the same type (A Wall can only be a clone of another Wall, etc.). The only exception is the generic Arch Component (as produced by this command), that can be clone of any other type (Wall, structure, window, etc). This allows to use a generic Arch Component to override the type of another one.


</div>


<div class="mw-translate-fuzzy">

-   **Description**: All Arch Components have a Description field, that can contain any text. This is used when [exporting to IFC](Arch_IFC.md).


</div>

-   **Tag**: The Tag property is another text field, which can be used to give an additional custom identity to objects.


<div class="mw-translate-fuzzy">

-   **Material**: toate componentele arcului au un slot material, care poate conține fie [Material](Arch_SetMaterial.md) sau un [MultiMaterial](Arch_MultiMaterial.md) (nu toate tipurile de obiecte Arch suportă utilizarea de MutiMaterials). Proprietățile DiffuseColor și Transparența materialului atașat vor defini culoarea Shape și transparența componentei Arch. Materialul va fi importat și exportat în [IFC](Arch_IFC.md), [OBJ](Arch_OBJ.md) and [DAE](Arch_DAE.md)..


</div>


<div class="mw-translate-fuzzy">

-   **Move with Host**: Atunci când o componentă este încorporată în interiorul alteia (de exemplu, o fereastră în interiorul unui perete), setarea acestei proprietăți la True va face ca obiectul să se miște și să se rotească împreună cu obiectul gazdă, atunci când obiectul gazdă este mutat sau rotit folosind comenzile [Draft Move](Draft_Move.md) sau [Draft Rotate](Draft_Rotate.md).


</div>


<div class="mw-translate-fuzzy">

-   **Hi Res**: Componentele Arch pot folosi forma unui alt obiect ca o versiune de înaltă rezoluție a acestora. Pentru aceasta, trebuie să fie setată atât proprietatea Hi Res, cât și modul de afișare Hi Res. Acest lucru permite, de exemplu, crearea unui perete simplu și apoi modelarea fiecărei cărămizi care compune zidul, de exemplu cu [ Part Box](Part_Box.md). Apoi, utilizați o combinație a acestor cărămizi ca o versiune de înaltă rezoluție a peretelui. Forma peretelui nu este modificată prin adăugarea unui obiect Hi-Res. Numai reprezentarea sa în vizualizarea 3D se va schimba prin adoptarea reprezentării versiunii de înaltă rezoluție în locul propriei sale vizualizări low resolution.


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Component/ro
