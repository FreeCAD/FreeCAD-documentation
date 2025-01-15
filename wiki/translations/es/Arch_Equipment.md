---
 GuiCommand:
   Name: Arch Equipment
   Name/es: Arch Equipment
   Workbenches: Arch_Workbench/es
   MenuLocation: Arch , Equipment
   Shortcut: E Q
   SeeAlso: Arch_3Views/es
---

# Arch Equipment/es


</div>

---
 GuiCommand:
   Name: Arch Equipment
   Name/es: Arch Equipment
   Workbenches: Arch_Workbench/es
   MenuLocation: Arch , Equipment
   Shortcut: E Q
   SeeAlso: Arch_3Views/es
---

# Arch Equipment/es



## Descripción


<div class="mw-translate-fuzzy">

La herramienta de equipamiento le ofrece una manera simple y conveniente de insertar elementos independientes no estructurales, como muebles, equipos hidro-sanitarios o electrodomésticos para sus proyectos. Los equipos se basan en [Part shapes](Part_Workbench/es.md), lo que les permite beneficiarse de la solidez y las posibilidades de la geometría BRep, y generar buenas vistas cuando se representan en vistas de planos y secciones.


</div>

<img alt="" src=images/Arch_equipment_example.jpg  style="width:600px;"> 
*Furniture objects enclosed in an [Arch Equipment](Arch_Equipment.md) object. The flat projections can be obtained by the [Draft Shape2DView](Draft_Shape2DView.md) tool*


<div class="mw-translate-fuzzy">

A partir de la versión 0.17, los objetos de equipamiento también tienen una propiedad **HiRes** donde se puede conectar un objeto [Mesh](Mesh_Workbench/es.md). Los objetos del equipamiento se pueden hacer para mostrar esa malla en la vista 3D en lugar de su forma, lo que permite usar cualquier objeto de malla de alta resolución, como muebles detallados que se encuentran comúnmente en los sitios web.


</div>

<img alt="" src=images/Arch_equipment_mesh.jpg  style="width:600px;"> 
*Furniture objects enclosed in an [Arch Equipment](Arch_Equipment.md) object, with a high resolution mesh attached*


<div class="mw-translate-fuzzy">

Cuando se utiliza el exportador Arch OBJ, todos los equipos que están en el modo de visualización Mesh se exportarán como su malla en lugar de su forma.


</div>




<div class="mw-translate-fuzzy">

## Como utilizar 


</div>


<div class="mw-translate-fuzzy">

1.  Seleccione una forma de [Part](Part_Workbench/es.md), y opcionalmente un objeto [Mesh](Mesh_Workbench/es.md)
2.  Presione el botón **<img src="images/_Arch_Equipment.png" width=16px> [Arch Equipment](Arch_Equipment/es.md)
**, o presione **E** y luego **Q**


</div>



## Opciones

-   Los equipamientos comparten las propiedades y comportamientos comunes de todos [Arch Components](Arch_Component/es.md)



## Propiedades

-    {{PropertyData/es|Model}}: una descripción del modelo de este equipamiento.

-    {{PropertyData/es|Url}}: una URL de la página del producto donde se puede encontrar más información sobre este equipamiento.

-    {{PropertyData/es|Mesh}}: una representación de [Mesh](Mesh_Workbench/es.md) para usar con este equipo. Cuando se establece, el modo de visualización **Mesh** está disponible.




<div class="mw-translate-fuzzy">

## Programación


</div>


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

La herramienta Equipamiento puede utilizarse en [macros](macros/es.md) y desde la consola de Python utilizando la siguiente función:


</div>


```python
Equipment = makeEquipment(baseobj=None, placement=None, name="Equipment")
```


<div class="mw-translate-fuzzy">

-   Crea un objeto de equipo a partir de un objeto base (Malla o Pieza)
-   Devuelve el nuevo objeto del equipamiento, o ninguno si la operación falló.


</div>

Ejemplo: 
```python
import FreeCAD, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 500
Box.Width = 2000
Box.Height = 600

Equip = Arch.makeEquipment(Box)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav|[Fence](Arch_Fence.md)|[Arch CompPipe](Arch_CompPipe.md)|[Arch](Arch_Workbench.md)|IconL=Arch_Fence.svg |IconC=Workbench_Arch.svg |IconR=Arch_CompPipe.png}}


</div>



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Equipment/es
