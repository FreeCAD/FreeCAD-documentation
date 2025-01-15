# Arch Rebar/es
---
 GuiCommand:   Name: Arch Rebar   Name/es: Arch Rebar   Workbenches: Arch_Workbench/es   Arch---


</div>

---
 GuiCommand:   Name: Arch Rebar   Name/es: Arch Rebar   Workbenches: Arch_Workbench/es   Arch---


</div>



## Descripción


<div class="mw-translate-fuzzy">

La herramienta Rebar le permite colocar [reinforcing bars](http://en.wikipedia.org/wiki/Rebar) dentro de los objetos [Arch Structure](Arch_Structure/es.md). Los objetos de barra de refuerzo se basan en perfiles 2D como [sketches](Sketcher_Workbench/es.md) o [draft objects](Draft_Workbench/es.md), que deben dibujarse en una cara de un objeto de estructura. A continuación, puede ajustar la configuración de las barras de refuerzo, como el número y el diámetro de las barras, o la distancia de desplazamiento entre los dos extremos del elemento estructural.


</div>

Rebar objects are based on 2D profiles such as [Draft objects](Draft_Workbench.md) and [Sketches](Sketcher_Workbench.md), that must be drawn on a face of the structural object. After creation you can adjust the properties of the rebar, including the number and diameter of the bars, and the offset distance between them and the faces of the structural element.

<img alt="" src=images/Arch_Rebar_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

La imagen de arriba muestra un objeto estructural, donde se dibujan dos bocetos, que definen dos diagramas de barras. Estos dos bocetos se convierten en objetos de barras de refuerzo.


</div>




<div class="mw-translate-fuzzy">

## Como utilizar 


</div>


<div class="mw-translate-fuzzy">

1.  Crear un elemento [structure](Arch_Structure/es.md)
2.  Cambiar a [Sketcher Workbench](Sketcher_Workbench/es.md)
3.  Seleccione una cara del elemento estructural
4.  Presione el botón **<img src="images/_Sketcher_NewSketch.png" width=16px> [New Sketch](Sketcher_NewSketch/es.md)** para comenzar un nuevo boceto en la cara seleccionada
5.  Dibuja el diagrama de tu barra
6.  Presione el botón **<img src="images/_Sketcher_LeaveSketch.png" width=16px> [Leave Sketch](Sketcher_LeaveSketch/es.md)** para finalizar
7.  Vuelve al [Arch Workbench](Arch_Workbench/es.md)
8.  Seleccione el boceto que acaba de dibujar
9.  Presione el botón **<img src="images/_Arch_Rebar.png" width=16px> [Arch Rebar](Arch_Rebar/es.md)
**, o presione **R** luego la tecla **B**
10. Ajuste las propiedades deseadas (es posible que su barra de refuerzo no aparezca inmediatamente, si algunas de las propiedades crean una situación imposible, como que el diámetro de la barra sea 0 o que las distancias de compensación sean mayores que la longitud del elemento estructural)


</div>

Although normally a rebar is used inside an Arch Structure, since FreeCAD 0.19 the rebar can be created outside of any host object. To host a rebar inside an object, you just need to set its **Host**.



## Opciones

-   Las barras de refuerzo comparten las propiedades y los comportamientos comunes de todos [Arch Components](Arch_Component/es.md)
-   El valor de redondeo se expresa en veces el diámetro. Si su barra tiene un diámetro de 5 mm, un valor de redondeo de 3 creará redondeo en ángulos con un radio de 15 mm.
-   Los valores predeterminados para nuevas barras de refuerzo se pueden configurar en la configuración de preferencias de Arch.
-   Si no se especifica un vector de dirección, la dirección y la distancia a lo largo de las cuales se extenderán las barras se calcula automáticamente desde el objeto estructural del anfitrión, tomando la dirección normal del boceto base y tomando su intersección con el objeto estructural. Si especifica un vector de dirección, también se tendrá en cuenta la longitud de ese vector.
-   El valor de espaciado se calcula a partir de la cantidad actual de barras, y representa la distancia entre los ejes de cada barra. Por lo tanto, debe restar el diámetro de la barra para obtener el tamaño del espacio libre entre barras.



## Propiedades

-    {{PropertyData/es|Amount}}: La cantidad de barras.

-    {{PropertyData/es|Diameter}}: El diámetro de las barras.

-    {{PropertyData/es|Direction}}: La dirección (y longitud) a lo largo de la cual las barras deben extenderse. Si el valor es (0,0,0), la dirección se calcula automáticamente desde el objeto estructural del host.

-    {{PropertyData/es|Offset Start}}: La distancia de desplazamiento entre el borde del objeto estructural y la primera barra.

-    {{PropertyData/es|Offset End}}: La distancia de desplazamiento entre el borde del objeto estructural y la última barra.

-    {{PropertyData/es|Rounding}}: A rounding value to be applied to the corners of the bars, expressed in times the diameter.

-    {{PropertyData/es|Spacing}}: La distancia entre los ejes de cada barra.




<div class="mw-translate-fuzzy">

## Programación


</div>


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

La herramienta Refuerzo de Barras puede utilizarse en [macros](macros/es.md) y desde la consola de python utilizando la siguiente función:


</div>


```python
Rebar = makeRebar(baseobj=None, sketch=None, diameter=None, amount=1, offset=None, name="Rebar")
```


<div class="mw-translate-fuzzy">

-   Agrega un objeto de barra de refuerzo al objeto estructural dado, usando el boceto dado como perfil.
-   Si no se proporciona ningún diámetro, cantidad o valor de compensación, se aplican los valores predeterminados de las configuraciones de preferencias de Arch.
-   Devuelve el nuevo objeto Rebar.


</div>

Ejemplo:


```python
import FreeCAD, Arch, Part

Structure = Arch.makeStructure(None, length=1000, width=1000, height=3000)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

p1 = FreeCAD.Vector(-400, 400, 0)
p2 = FreeCAD.Vector(400, 400, 0)
Sketch = FreeCAD.ActiveDocument.addObject('Sketcher::SketchObject', 'Sketch')
Sketch.MapMode = "FlatFace"
Sketch.Support = [(Structure, "Face6")]
Sketch.addGeometry(Part.LineSegment(p1, p2))
FreeCAD.ActiveDocument.recompute()

Rebar = Arch.makeRebar(Structure, Sketch, diameter=80, amount=7, offset=50)
Rebar.OffsetStart = 100
Rebar.OffsetEnd = 100
FreeCAD.ActiveDocument.recompute()
```





<div class="mw-translate-fuzzy">


</div>



---
⏵ [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [BIM](Category_BIM.md) > Arch Rebar/es
