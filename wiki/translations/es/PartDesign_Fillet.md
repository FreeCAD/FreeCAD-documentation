---
- GuiCommand:/es
   Name:PartDesign Fillet
   Name/es:DiseñoPiezas Redondeo
   Workbenches:[DiseñoPiezas](PartDesign_Workbench/es.md)
   MenuLocation:DiseñoPiezas → Redondeo
   SeeAlso:[Chaflán](PartDesign_Chamfer.md),[Piezas Redondeo](Part_Fillet/es.md)
---

# PartDesign Fillet/es


</div>

## Descripción

Esta herramienta crea redondeos en las aristas seleccionadas de un objeto. Se crea una nueva entrada de Redondeo, (seguida por un número de secuencia si ya existen redondeos en el documento) en el árbol del proyecto.

## Utilización

-   Selecciona una o varias aristas o una cara en un objeto, y luego inicia la herramienta haciendo clic en su icono o entrando en el menú. En caso de que hayas seleccionado una cara, todos sus bordes se respetan para el fileteado.
-   En el [Panel de tareas](Task_panel/es.md) que aparece, establezca el radio de fileteado ya sea ingresando el valor, o haciendo clic en las flechas arriba/abajo.
-   Si desea agregar más aristas o caras, haga clic en el botón **Agregar** y seleccione las aristas y/o las caras.
-   Si desea eliminar aristas o caras
    -   o bien seleccione el borde/cara en la lista del diálogo y pulse la tecla **DEL**. *Nota*: Como debe haber al menos un borde para la característica, el último borde o cara restante en la lista no puede ser eliminado.
    -   o pulse el botón **Eliminar**. Todos los bordes y caras que se hayan seleccionado previamente se resaltarán en color púrpura. Seleccione el borde o la cara que desea eliminar.
-   Pulsa **OK** para validar.
-   Para una cadena de aristas tangentes entre sí, se puede seleccionar una única arista; el redondeo se propagará a lo largo de la cadena.
-   Para editar el redondeo después de que la función ha sido validada, haz doble clic en la etiqueta del redondeo en el árbol del proyecto o pulsa con el botón derecho sobre ella y selecciona **Editar Redondeo**.

## Redondeo DiseñoPiezas VS. Redondeo Piezas 

<img alt="" src=images/PartDesign_Fillet.svg  style="width:24px;"> [Redondeo DiseñoPiezas](PartDesign_Fillet/es.md) no debe confundirse con el **<img alt="" src=images/Part_Fillet.svg  style="width:24px;"> [Redondeo Piezas](Part_Fillet/es.md)** de la [Ambiente de trabajo Piezas](Part_Workbench/es.md). Aunque comparten el mismo nombre, no son iguales y no se usan de la misma manera.

Aquí puedes ver las diferencias entre ambos:

-   El Redondeo de DiseñoPiezas es *paramétrico*. Después de aplicar un redondeo, su radio puede editarse; esto no es posible con el RedondeoPiezas.
-   Las aristas deben seleccionarse sobre un objeto antes de activar el redondeo de Diseño de Piezas. Con el redondeo de Piezas, la herramienta puede iniciarse y seleccionar después un sólido y las aristas.
-   El Redondeo de DiseñoPiezas crea una entrada de redondeo separada (seguida por un número de secuencia si ya existen otros redondeos) en el árbol de proyecto. El redondeo de Piezas se convierte en la raíz del objeto al que se ha aplicado.
-   El Redondeo de DiseñoPiezas ofrece una previsualización en tiempo real del redondeo a aplicar a los objetos antes de validar la función.
-   El redondeo de Pieza soporta radios variables (con un de inicio y un radio final). El Redondeo de DiseñoPiezas no.

## Temas conocidos 

Fillets, chamfers, and other features that operate on solid bodies depend on the underlying OpenCASCADE Technology (OCCT) kernel that FreeCAD uses. The OCCT kernel occasionally has difficulty handling coincident sharp edges, where two faces meet. If this is the case FreeCAD may crash without an explanation.

If run from the terminal, FreeCAD may output a log like this one after the crash:


{{code|code=
#1  0x7fff63d660ba in BRep_Tool::Curve(TopoDS_Edge const&, TopLoc_Location&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x2a
#2  0x7fff63d69546 in BRep_Tool::Curve(TopoDS_Edge const&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x46
#3  0x7fff71f4fef5 in ChFi3d_Builder::PerformIntersectionAtEnd(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x3b05
#4  0x7fff71f58307 in ChFi3d_Builder::PerformOneCorner(int, bool) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x1097
#5  0x7fff71ef6218 in ChFi3d_Builder::PerformFilletOnVertex(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x4e8
#6  0x7fff71ef71d1 in ChFi3d_Builder::Compute() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0xe31
#7  0x7fff720ad7c3 in BRepFilletAPI_MakeChamfer::Build() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x33
#8  0x7fff723be48e in PartDesign::Chamfer::execute() from /usr/lib/freecad-daily/lib/_PartDesign.so+0x60e
...
}}

This output references functions located in `libTKBRep.so`, `libTKFillet.so`, etc., which are OCCT libraries. If this type of crashes occurs, the problem may need to be reported and solved in OCCT rather than in FreeCAD.

See the forum threads for more information:

-   [Bug Chamfer bigger than 2mm crashes freecad](https://forum.freecadweb.org/viewtopic.php?p=263818#p263818)
-   [Segfault when using part design fillet](https://forum.freecadweb.org/viewtopic.php?p=264827#p264827)

The user is also responsible for the integrity of his or her own model. Depending on the model, it may be impossible to perform a fillet or chamfer if the body is not big enough to support that operation. For example, it wouldn\'t be possible to create a 10 mm fillet if an edge is separated only 5 mm from the next surface. In that case, the maximum radius for a fillet would be 5 mm; trying to use a larger value may result in a shape that doesn\'t compute, or even a crash. If using the exact limit of 5 mm doesn\'t work, it may be possible to use a very close approximation, like 4.9999 mm, to produce the same visible result.

### Topological naming 


<div class="mw-translate-fuzzy">

### Denominación topológica 

Los números de los bordes no son completamente estables, por lo tanto es aconsejable que termine el trabajo de diseño principal de su cuerpo sólido antes de aplicar características como filetes y chaflanes, de lo contrario los bordes podrían cambiar de nombre y los bordes fileteados probablemente quedarían inválidos.


</div>

Lea más en [problema de denominación topológica](topological_naming_problem/es.md).

## Guión


<div class="mw-translate-fuzzy">

La herramienta **[16px|text-top=Fillet|link=PartDesign_Fillet](File:PartDesign_Fillet.svg.md) [Redondeo](PartDesign_Fillet/es.md)** puede ser usada en una macro, y, desde la consola Python usando la siguiente función :


</div>


```python
Box = Box.makeFillet(3,[Box.Edges[0]]) # 1 Fillet
Box = Box.makeFillet(3,[Box.Edges[1],Box.Edges[2],Box.Edges[3],Box.Edges[4]]) # for several Fillets
```

-   3 = radio
-   Box.Edges\[2\] = Borde con su número


<div class="mw-translate-fuzzy">

Ejemplo:


</div>


```python
import PartDesign
from FreeCAD import Base

Box = Part.makeBox(10,10,10)
Box = Box.makeFillet(3,[Box.Edges[0]]) # pour 1 Fillet
Box = Box.makeFillet(3,[Box.Edges[1],Box.Edges[2],Box.Edges[3],Box.Edges[4]]) # for several Fillets
Part.show(Box)
```


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Fillet/es
