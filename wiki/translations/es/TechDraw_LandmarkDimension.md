---
 GuiCommand:
   Name: TechDraw LandmarkDimension
   MenuLocation: TechDraw , Dimensions , Insert Landmark Dimension - EXPERIMENTAL
   Workbenches: TechDraw_Workbench/es
   Version: 0.19
   SeeAlso: TechDraw_HorizontalDimension/es, TechDraw_VerticalDimension/es
---

# TechDraw LandmarkDimension/es



## Descripción


<div class="mw-translate-fuzzy">

La herramienta **TechDraw LandmarkDimension** agrega una dimensión lineal a una Vista. La dimensión se basa en dos objetos punto (objetos [Draft Point](Draft_Point/es.md) o [Part Point](Part_Point/es.md)) del modelo 3D.


</div>

El propósito de esta herramienta es proporcionar una solución alternativa a la corrupción de dimensiones causada por los problemas de \"[denominación topologica](Topological_naming_problem/es.md)\". Los puntos de origen deben utilizar [Expresiones](Expressions/es.md) u otros mecanismos de contención para establecer su posición. Dado que los puntos son [Objetos de documento](App_DocumentObject/es.md) y no componentes de forma, su nombre no cambia con los nuevos cálculos y, por lo tanto, se encuentran fácilmente.

Vea [TechDraw LengthDimension](TechDraw_LengthDimension/es#Limitation.md) para obtener más información sobre dimensiones y denominación topológica.



## Uso

1.  Seleccione dos objetos punto en la [vista 3D](3D_view/es.md) o la [vista de árbol](Tree_view/es.md).
2.  Agregue la vista TechDraw correcta a la selección seleccionándola en la [vista de árbol](Tree_view/es.md).
3.  Hay varias formas de invocar la herramienta:
    -   Presione el botón **<img src="images/TechDraw_LandmarkDimension.svg" width=16px> [Insertar cota Landmark - EXPERIMENTAL](TechDraw_LandmarkDimension.md)**.
    -   Seleccione la opción **TechDraw → Dimensions → <img src="images/TechDraw_LandmarkDimension.svg" width=16px> Insertat cota Landmark - EXPERIMENTAL** del menú.
4.  Se agrega una dimensión a la Vista.
5.  La dimensión se puede arrastrar a la posición deseada.
6.  Si es necesario, agregue tolerancias como se describe en [esta página](TechDraw_Geometric_dimensioning_and_tolerancing/es#Tolerances.md).



### Cambiar propiedades 

Para cambiar las propiedades de un objeto de dimensión, haga doble clic en él en el dibujo o en la [vista de árbol](Tree_view.md). Esto abrirá el [diálogo de dimensión](TechDraw_LengthDimension/es#Dimension_dialog.md).



## Limitaciones

La herramienta Cota de referencia está inicialmente limitada a cotas de \"Distancia\". Se pueden agregar otros tipos si la demanda lo amerita.



## Notas

Vea [TechDraw LengthDimension](TechDraw_LengthDimension/es#Notes.md).



## Propiedades

Vea [TechDraw LengthDimension](TechDraw_LengthDimension/es#Properties.md).



## Programación

Ver también: [Documentación de la API autogenerada](https://freecad.github.io/SourceDoc/) y [Fundamentos de FreeCAD Guión](FreeCAD_Scripting_Basics/es.md).

La herramienta Cota de referencia se puede utilizar en [macros](Macros/es.md) y desde la consola de [Python](Python/es.md) utilizando las siguientes funciones:


```python
dim1 = FreeCAD.ActiveDocument.addObject("TechDraw::LandmarkDimension", "Landmark")
dim1.Type = "Distance"
dim1.References2D = [(TDView, "Vertex1")]
dim1.References3D = [(Point3d1, "Vertex1")]
dim1.References3D = [(Point3d2, "Vertex1")]
page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LandmarkDimension/es
