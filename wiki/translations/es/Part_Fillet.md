---
- GuiCommand:/es
   Name:Part Fillet
   Name/es:Pieza Redondeo
   MenuLocation:Pieza → Redondeo
   Workbenches:[Pieza](Part_Workbench/es.md)
   SeeAlso:[Pieza Chaflán](Part_Chamfer/es.md)
---

# Part Fillet/es


</div>

## Descripción

Esta herramienta crea un redondeo (ronda) sobre las aristas seleccionadas de un objeto. Un diálogo permite seleccionar qué objetos y qué bordes se va a trabajar.

## Utilización


<div class="mw-translate-fuzzy">

-   Inicia la herramienta desde la barra de herramientas de Pieza o desde el menú. Puedes seleccionar los objetos antes o después de iniciar la herramienta.
-   Si la forma no está seleccionada antes de seleccionar la herramienta, la seleccionas en la lista de formas del panel de tareas.
-   Selecciona el tipo de radio, ya sea de radio constante o de radio variable.
-   Selecciona las aristas en la vista del modelo 3D, o escogiéndolas en la lista de aristas del panel de tareas.
-   Establece el valor del radio.
-   Pulsa **OK** para validar.


</div>

![](images/Dialog-fillet.png )


<div class="mw-translate-fuzzy">

## Redondeo de Piezas VS. Redondeo de Diseño de Piezas 

Existe otra herramienta de redondeo en el <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Ambiente de trabajo DiseñoPiezas](PartDesign_Workbench/es.md). Ten en cuenta que sus operaciones son bastante diferente. Comprueba la <img alt="" src=images/PartDesign_Fillet.svg  style="width:24px;"> [Redondeo de DiseñoPiezas](PartDesign_Fillet/es.md) página de referencia para más detalles de sus diferencias.


</div>

## Notes on application of Part Fillet 

Part Fillet might do nothing if the result would touch or cross the next adjacent edge. So if you do not get the expected result, try with a smaller value. This is the same for <img alt="" src=images/Part_Chamfer.svg  style="width:24px;"> [Part Chamfer](Part_Chamfer.md).

The fillet tool sometimes fails when trying to fillet complex objects. A common cause of this may be that the shape being filleted is not geometrically correct. This may be the result of lines/planes etc not being removed after previous operations used to construct the shape ( e.g. Cut/Intersection/Fusion). A number of steps can be used to minimize problems:

-   Where possible leave filleting a part until the part is completely generated. This will minimize interaction of fillets with subsequent Boolean operations;
-   Use the **Part → Check Geometry** to check for any errors in the shape geometry and correct;
-   Use **Part → Refine shape** to remove any artifacts introduced by previous Boolean operations before filleting (and in some cases between filleting operations in sequence);
-   Consider using **Edit → Preferences → PartDesign** to enable automatic checking and refining of the model after Boolean and sketch based operations (performance may be affected if these options are left switched on).

Also note that the part Fillet feature is affected by the [Topological naming problem](Topological_naming_problem.md) when the any change is done to a modeling step earlier in the chain that affects the number of facets or vertices. This could cause unpredictable result. Until that is resolved (possibly with V0.19) it is advised to apply Chamfer and [Fillet](Part_Fillet.md) operations at the last steps in the chain.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Fillet/es
