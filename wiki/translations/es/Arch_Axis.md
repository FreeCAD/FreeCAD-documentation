---
- GuiCommand:/es
   Name:Arch Axis
   Name/es:Ejes de arquitectura
   MenuLocation:Arquitectura → Ejes
   Workbenches:[Arquitectura](Arch_Workbench/es.md)
   Shortcut:**A** **X**
---

# Arch Axis/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta Ejes te permite situar un sistema de ejes en el documento actual. La distancia y ángulo entre ejes es personalizable, así como el estilo de numeración. Los ejes sirven proncipalmente como referencias a las que ajustar objetos, pero se pueden utilizar en conjunto con [estructuras](Arch_Structure/es.md) para crear matrices paramétricas de vigas o columnas.


</div>

<img alt="" src=images/Arch_Axis_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

La imagen de arriba muestra dos objetos de eje diferentes posicionados perpendicularmente entre sí


</div>


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Presiona el botón **<img src="images/Arch_Axis.png" width=16px> [Arch Axis](Arch_Axis/es.md)
**, o pulsa las teclas **A** y **X**
2.  [Mover](Draft_Move/es.md)/[Rotar](Draft_Rotate/es.md) el sistema de ejes a la posición deseada
3.  Entrar en modo de edición haciendo doble clic en el sistema de ejes en la vista de árbol para ajustar sus parámetros como el número de ejes, distancias y ángulos entre ejes.


</div>

## Opciones


<div class="mw-translate-fuzzy">

-   Cada eje en la sucesión tiene su propia distancia y ángulo en relación con el eje previo. Esto permite crear sistemas muy complejos como sistemas no ortogonales, sistemas polares o culquier tipo de sistemas no uniformes.
-   Hacer doble clic en el eje en la vista en árbol permite editar las distancias, los ángulos y las etiquetas de cada eje
-   La longitud de los ejes, el tamaño de los globos y los estilos de numeración se pueden personalizar directamente por medio de las propiedades de los sistemas de ejes
-   Cada eje también puede mostrar una etiqueta, también editable a través del diálogo del panel de tareas


</div>

## Propiedades


<div class="mw-translate-fuzzy">

-    {{PropertyData/es|Length}}: La longitud de los ejes

-    {{PropertyView/es|Bubble Size}}: El tamaño de los globos de los ejes

-    {{PropertyView/es|Numeration style}}: Cómo se numeran los ejes: 1,2,3, A,B,C, etc\...

-    {{PropertyView/es|Bubble Position}}: Donde la burbuja se coloca en el eje: En el punto de inicio, punto final, ambos o ninguno.

-    {{PropertyView/es|Font Name}}: Una fuente para dibujar el número de burbuja y/o las etiquetas

-    {{PropertyView/es|Font Size}}: El tamaño del texto de la etiqueta solamente (el texto de la burbuja está controlado por el tamaño de la burbuja)

-    {{PropertyView/es|Show Labels}}: Activa/desactiva la visualización de los textos de las etiquetas


</div>

## Use as section mark 

By setting the **Bubble Position** property to **Arrow left/right** or **Bar left/right**, the axis will display a filled arrow or bar instead of the bubble, so it can be used as a section mark. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta Ejes se puede utilizar en [macros](macros/es.md) y desde la consola por medio de las siguientes funciones:


</div>


```python
Axes = makeAxis(num=5, size=1000, name="Axes")
```


<div class="mw-translate-fuzzy">


:   crea un sistema de ejes basado en el número dado de ejes y distancia de intervalo


</div>

Ejemplo:


```python
import Draft, Arch

Axes = Arch.makeAxis(5, 1000)

Axes.ViewObject.LineWidth = 3
Axes.ViewObject.BubbleSize = 200
Axes.ViewObject.FontSize = 150

Axes2 = Arch.makeAxis(6, 500)

Axes2.ViewObject.LineWidth = 2
Axes2.ViewObject.BubbleSize = 200
Axes2.ViewObject.FontSize = 150
Axes2.ViewObject.NumberingStyle = "A,B,C"
FreeCAD.ActiveDocument.recompute()

Axes2.Length = 6000
Draft.rotate(Axes2, -90)
Draft.move(Axes2, FreeCAD.Vector(-1000, 2500, 0))
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


</div>


 

[<img src="images/Property.png" style="width:16px"> Arch/es](<img src="images/Property.png" style="width:16px"> Arch/es.md)

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Axis/es
