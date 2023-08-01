---
- GuiCommand:
   Name: Arch MultiMaterial   Name/ro: Arch MultiMaterial
   Workbenches: [Arch](Arch_Workbench/ro.md)
   MenuLocation: Arch - Multi-Material
---

# Arch MultiMaterial/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul Multi-Material definește o listă de [ materials](Material.md), cu câte un nume și o valoare a grosimii pentru fiecare material. Această listă de multi-materiale poate fi apoi adăugată la un obiect [ Arch](Arch_Workbench/ro.md) în loc de un singur [Arch Material](Arch_SetMaterial.md) .


</div>

![](images/Arch_multimaterial_example.png )

Nu toate obiectele Arch pot folosi în prezent multi-materiale, iar utilizarea lor diferă. În prezent:


<div class="mw-translate-fuzzy">

-   [Wallscu](Arch_Wall.md) un material MultiMaterial va folosi definițiile materialelor și grosimile pentru a crea un perete multistrat
-   [Windows](Arch_Window.md) with a MultiMaterial will attribute materials with a given name defined inside the MultiMaterial to window components with a same name or type (see below). Material thickness is not considered.
-   [Panels](Arch_Panel.md) cu un material MultiMaterial va utiliza definițiile materialelor și grosimile pentru a crea un panou cu mai multe straturi


</div>

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Creați mai întâi o serie de [Arch Materials](Arch_SetMaterial.md) pe care o veți avea nevoie în materialul Multi-Material
2.  Optionally, select an Arch object you wish to attribute the new Multi-Material to
3.  apăsați butonul **<img src="images/Arch_MultiMaterial.png" width=16px> [Multi-Material](Arch_MultiMaterial.md)
**
4.  Definiții straturile cu materialele dorite


</div>

## Opțiuni

![](images/Arch_multimaterial_panel.png )

La crearea sau editarea unui material multiplu făcând dublu clic pe el în arbore, sunt disponibile următoarele opțiuni:


<div class="mw-translate-fuzzy">

-   **Duplicate** cu mai multe materiale existente din același document. Aceasta copiază numai valorile și nu leagă în nici un fel cele două materiale.
-   The **Name** field will also set the material object\'s Label
-   The **Composition** list is the list of the different material layers that compose this multi-material. Each layer has a name, a material and a thickness value.
-   Click **Add** to add a new layer, **Up** to move a selected layer up, **Down** to move a selected layer down, or **Del** to delete a selected layer.
-   Double-click the **name** of a layer to edit it, the material will offer you a drop-down list of available [Arch Materials](Arch_SetMaterial.md) in the same document, and thickness can be set to any value in any unit
-   Name and Material fields are mandatory. Thickness can be left blank (it will then adopt a value of 0).
-   When a multi-material contains layers with a thickness of zero, that thickness is considered variable. Arch objects that use the multi-material, such as Walls and Panels, will treat that accordingly, and give that layer the remaining space available given their own width or thickness.
-   Dacă numiți diferitele componente ale unui \"cadru\", \"panou solid\", \"panou din sticlă\" sau \"jaluzele\" și aplicați materialul într-o fereastră, materialele respective vor fi aplicate componentelor corespunzătoare ferestrei.


</div>

## Relation to IFC 

This roughly corresponds to a combination of [IfcMaterialLayerSet](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmateriallayerset.htm) and [IfcMaterialLayer](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmateriallayer.htm).

## Limitations

## Scripting


<div class="mw-translate-fuzzy">


{{docnav/ro|[Material](Arch_SetMaterial.md)|[Schedule](Arch_Schedule.md)|[Arch](Arch_Workbench.md)|IconL=Arch_SetMaterial.png |IconC=Workbench_Arch.svg |IconR=Arch_Schedule.svg}}


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch MultiMaterial/ro
