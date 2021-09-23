---
- GuiCommand:/es
   Name:Part Box
   Name/es:Part Cubo
   MenuLocation:Pieza → Primitivas → Cubo
   Workbenches:[Part](Part_Workbench/es.md)
   SeeAlso:[Part Crear primitivas](Part_Primitives/es.md)
---

# Part Box/es


</div>

## Descripción

El comando Cubo del [Banco de trabajo Part](Part_Workbench/es.md) inserta un [rectangular cuboid](http://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid), que es una forma primitiva geométrica paramétrica, en el documento activo. Por defecto, el comando Cubo insertará un cubo de 10x10x10 mm, posicionado en el origen, con el nombre \"Cubo\". Estos parámetros pueden ser modificados tras la creación del objeto.

<img alt="Part\_Box" src=images/Part_Box.jpg  style="width:400px;">

## Uso

1.  Ir a <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Banco de trabajo Part](Part_Workbench/es.md)
2.  Hay varias maneras de invocar al comando:
    -   Presionando el botón **<img src="images/Part_Box.svg" width=16px> Cubo** en la barra de herramientas.
    -   Seleccionar **Pieza → Primitivas → <img src="images/Part_Box.svg" width=16px> Cubo** desde la barra de menú.


<div class="mw-translate-fuzzy">

**Resultado:** El resultado por defecto es un cubo de la misma longitud, anchura y altura de 10 mm. Está unido al plano global XY y una arista es coincidente con el eje global Z.


</div>

Las propiedades del Cubo pueden ser editadas posteriormente, bien desde el editor de propiedades, o bien pinchando con doble clic de ratón sobre la pestaña Modelo del árbol de dependencias.

## Propiedades


{{Properties_Title|Base}}

-    {{PropertyData/es|Placement o Emplazamiento}}: Especifica la orientación y la posición del Cubo en el espacio 3D. Ver [Placement](Placement/es.md). El punto de referencia es la esquina frontal inferior izquierda del cubo.

-    {{PropertyData/es|Label o Etiqueta}}: Nombre dado al objeto Cubo. Puede ser cambiado si es conveniente.


{{Properties_Title|Box}}

-    {{PropertyData/es|Length o Longitud}}: Dimensiones del Cubo en la dirección X.

-    {{PropertyData/es|Width o Anchura}}: Dimensiones del Cubo en la dirección Y.

-    {{PropertyData/es|Height o Altura}}: Dimensiones del Cubo en la dirección Z.

![Part\_Box-Properties](images/Part_Box-Properties.jpg )

## Programación

El comando Box (Cubo) puede ser usado en las [macros](Macros.md) y desde la consola de Python usando la siguiente función: 
```python
FreeCAD.ActiveDocument.addObject("Part::Box", "myBox")
```

-   Donde \"myBox\" es el nombre del objeto Cubo.
-   Devuelve un nuevo objeto creado de tipo Cubo.

Se puede acceder y modificar los atributos del objeto Box(Cubo). Por ejemplo, si se desean modificar los atributos de longitud, anchura o altura: 
```python
FreeCAD.ActiveDocument.myBox.Length = 25
FreeCAD.ActiveDocument.myBox.Width = 15
FreeCAD.ActiveDocument.myBox.Height = 30
```

Se puede cambiar su emplazamiento con: 
```python
FreeCAD.ActiveDocument.myBox.Placement = FreeCAD.Placement(FreeCAD.Vector(4, 6, 3), FreeCAD.Rotation(30, 45, 10))
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Box/es
