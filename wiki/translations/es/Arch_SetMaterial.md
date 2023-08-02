---
- GuiCommand:
   Name: Arch SetMaterial
   Name/es: Arch SetMaterial
   MenuLocation: Arch -> Set material...
   Workbenches: Arch_Workbench/es, BIM_Workbench/es
   Shortcut: **M** **T**
---

# Arch SetMaterial/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

Las herramientas Material permiten agregar [materials](Material.md) al documento activo y atribuir un material a un objeto [Arch](Arch_Workbench/es.md). Los materiales pueden tener todas las propiedades de un material determinado y controlar el color del objeto al que está unido. Los materiales se almacenan en una carpeta **Materiales** en el documento activo.


</div>

![](images/Arch_materials_01.jpg )


<div class="mw-translate-fuzzy">

## Como utilizar 


</div>


<div class="mw-translate-fuzzy">

1.  Opcionalmente, seleccione uno o más objetos a los que desee atribuir un nuevo material
2.  Presione el botón **<img src="images/_Arch_SetMaterial.png" width=16px> [Set Material](Arch_SetMaterial/es.md)
**
3.  Cargue un material preestablecido, o cree uno nuevo completando los campos.
4.  Presiona **OK**


</div>

## Opciones

-   Al crear un nuevo material, un panel de tareas le permite establecer diferentes opciones:

![](images/Arch_materials_02.jpg )


<div class="mw-translate-fuzzy">

-   **Elegir predefinido**: elija uno de los materiales preestablecidos, para usarlo tal cual, o para adaptarlo modificando los campos a continuación
-   **Nombre**: elija un nombre para el material
-   **Botón Editar**: Esto abre el material actual en [Material editor](FEM_MaterialEditor.md) de FreeCAD, lo que le permite editar muchas propiedades adicionales y agregar sus propias propiedades personalizadas
-   **Descripción**: Una descripción más detallada del material
-   **Color**: un color de pantalla para el material, que se aplicará a todos los objetos que usen ese material
-   **Código**: un nombre y número de referencia de un sistema de especificación como [Masterformat](https://en.wikipedia.org/wiki/MasterFormat) o [Omniclass](http://www.omniclass.org/) .
-   **Botón del navegador de códigos**: Aún no implementado: permitirá abrir la referencia en un navegador web
-   **URL**: una URL donde se puede encontrar más información sobre el material
-   **Botón URL**: abre la URL en un navegador web


</div>

## Relation to IFC 

This roughly corresponds to [IfcMaterial](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmaterial.htm).


<div class="mw-translate-fuzzy">


{{docnav/es
|[Arch CompSetMaterial/es](Arch_CompSetMaterial/es.md)
|[Multi-Material/es](Arch_MultiMaterial/es.md)
|[Arch](Arch_Workbench/es.md)
|IconL=Arch_CompSetMaterial.png 
|IconC=Workbench_Arch.svg 
|IconR=Arch_MultiMaterial.png
}}


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SetMaterial/es
