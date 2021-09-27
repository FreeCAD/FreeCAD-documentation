---
- GuiCommand:/es
   Name:Arch MultiMaterial
   Name/es:Arch MultiMaterial
   MenuLocation:Arch → Multi-Material
   Workbenches:[Arch](Arch_Workbench/es.md), [BIM](BIM_Workbench.md)
---

# Arch MultiMaterial/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta Multi-Material define una lista de [materiales](Material/es.md) con un nombre y un valor de espesor, para cada material. Esta lista de materiales múltiples se puede agregar a un objeto [Arch](Arch_Workbench/es.md) en lugar de a un único [Arch Material](Arch_SetMaterial/es.md).


</div>

![](images/Arch_multimaterial_example.png )

No todos los objetos Arch actualmente pueden hacer uso de múltiples materiales, y el uso que hacen de ellos difiere. Actualmente:


<div class="mw-translate-fuzzy">

-   [Muros](Arch_Wall/es.md) con un MultiMaterial utilizará las definiciones y grosores del material para crear un muro multicapa
-   [Ventanas](Arch_Window/es.md) con un MultiMaterial atribuirá materiales con un nombre dado definido dentro del MultiMaterial a componentes de la ventana con el mismo nombre o tipo (ver a continuación). El espesor del material no es considerado.
-   [Paneles](Arch_Panel/es.md) con un MultiMaterial utilizará las definiciones y grosores del material para crear un panel de múltiples capas


</div>

## Como utilizar 


<div class="mw-translate-fuzzy">

1.  Crea primero una serie de [Arch Materials](Arch_SetMaterial/es.md) que necesitarás en tu Multi-Material
2.  Opcionalmente, seleccione un objeto Arch al que desee atribuir el nuevo Multi-Material
3.  Presione el botón {{KEY | <img src="images/_Arch_MultiMaterial.png" width=16px> [Multi-Material](Arch_MultiMaterial/es.md)}}
4.  Establecer las capas de material deseadas


</div>

## Opciones

![](images/Arch_multimaterial_panel.png )

Al crear o editar un material múltiple haciendo doble clic en el árbol, están disponibles las siguientes opciones:


<div class="mw-translate-fuzzy">

-   **Duplicar** otro Multi-Material existente del mismo documento. Esto solo copia los valores y no vincula los dos materiales múltiples de ninguna manera.
-   El campo **Nombre** también establecerá la etiqueta del objeto material
-   La lista **Composición** es la lista de las diferentes capas de material que componen este multi-material. Cada capa tiene un nombre, un material y un valor de espesor.
-   Haga clic en **Añadir** para agregar una nueva capa, **Arriba** para mover una capa seleccionada hacia arriba, **Abajo** para mover una capa seleccionada hacia abajo, o **Del** para eliminar una capa seleccionada.
-   Haga doble clic en el **nombre** de una capa para editarlo, el material le ofrecerá una lista desplegable de [Arch Materials](Arch_SetMaterial/es.md) disponible en el mismo documento, y se puede configurar el grosor a cualquier valor en cualquier unidad
-   Los campos Nombre y Material son obligatorios. El grosor se puede dejar en blanco (luego adoptará un valor de 0).
-   Cuando un multi-material contiene capas con un espesor de cero, ese espesor se considera variable. Los objetos de arco que usan materiales múltiples, como Paredes y Paneles, lo tratarán como corresponda y le otorgarán a esa capa el espacio disponible restante dado su propio ancho o grosor.
-   Si nombra los diferentes componentes de múltiples materiales \"Marco\", \"Panel sólido\", \"Panel de vidrio\" o \"Louvre\", y aplica ese material a una ventana, los materiales dados se aplicarán a los componentes de ventana correspondientes.


</div>

## Relation to IFC 

This roughly corresponds to a combination of [IfcMaterialLayerSet](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmateriallayerset.htm) and [IfcMaterialLayer](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmateriallayer.htm).

## Limitations

## Scripting


<div class="mw-translate-fuzzy">


{{docnav/es|[Material](Arch_SetMaterial.md)|[Schedule](Arch_Schedule.md)|[Arch](Arch_Workbench.md)|IconL=Arch_SetMaterial.png |IconC=Workbench_Arch.svg |IconR=Arch_Schedule.svg}}


</div>

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch MultiMaterial/es
