---
- GuiCommand:
   Name: Arch Structure
   Name/es: Arch Estructura
   Workbenches: [Arquitectura](Arch_Workbench/es.md)
   MenuLocation: Arquitectura - Estructura
   Shortcut: **S** **T**
   SeeAlso: [Arquitectura Muro](Arch_Wall/es.md), [Arquitectura Barra de refuerzo](Arch_Rebar/es.md)
---

# Arch Structure/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta [Architectura Estructura](Arch_Structure/es.md) permite construir elementos estructurales como columnas o vigas, especificando su anchura, longitud y altura, o basándose en un perfil 2D (cara, alambre o croquis).


</div>

Si no se da ningún perfil, se dispone de un conjunto de preajustes para construir rápidamente un elemento estructural a partir de un perfil estándar predefinido.

![](images/Arch_Structure_example.jpg ) 
*Columna basada en un perfil base 2D; una columna y una viga definidas por su altura, longitud y anchura, sin perfil base; una estructura metálica basada en una cara 2D*

## Utilización


<div class="mw-translate-fuzzy">

1.  Seleccionar una forma 2D (objeto bocetado, cara o croquis) (opcional)
2.  Pulse el botón **<img src="images/Arch_Structure.svg" width=16px>  [Estructura](Arch_Structure/es.md)
**, o pulsar las teclas **S** y **T**
3.  Ajusta las propiedades deseadas.


</div>

## Opciones


<div class="mw-translate-fuzzy">

-   Los elementos estructurales comparten las propiedades y comportamientos comunes de todos los [Arch Components](Arch_Component/es.md)
-   Si no se ha seleccionado ningún objeto, se crea un bloque en tres dimensiones
-   El alto, largo y acho de la estructura se puede ajustar después de su creación
-   Presiona **ESC** o el botón **'''Cancelar'''** para cancelar el comando actual.
-   Haciendo doble clic en la estructura en la vista en árbol después de crearla permite entrar en modo edición y acceder y modificar sus adiciones y substracciones
-   En modo edición, también es posible añadir [sistemas de ejes](Arch_Axis/es.md) al elemento estructural. Cuando se añade un sistema de ejes, el elemento estructural se copiará en cada eje del sistema. Cuando se añaden dos sistemas de ejes, el elemento estructural se copiará una vez en cada intersección de los dos sistemas.


</div>

## Propiedades

### Datos


<div class="mw-translate-fuzzy">

-    **Tool**: una trayectoria de extrusión opcional, que puede ser cualquier tipo de hilo. Si esta propiedad está vacía, la extrusión será recta, y ocurrirá en la dirección dada por la propiedad Normal

-    **Normal**: especifica la dirección en la que se extruirá la cara base de esta estructura. Si esta propiedad se mantiene en (0,0,0), la dirección se establecerá automáticamente a la dirección normal de la cara base.

-    **Face Maker**: especifica el tipo de algoritmo de generación de caras que se utilizará para construir el perfil. Las opciones son None, Simple, Cheese y Bullseye.

-    **Length**: especifica la longitud de la estructura. Sólo se utiliza si la estructura no se basa en un perfil.

-    **Width**: especifica la anchura de la estructura. Sólo se utiliza si la estructura no se basa en un perfil.

-    **Height**: especifica la altura de la estructura, o la longitud de la extrusión cuando se basa en un perfil. Si no se da la altura, y la estructura está dentro de un objeto [Arquitectura Piso](Arch_Floor/es.md) con su altura definida, la estructura tomará automáticamente el valor de la altura del piso.

-    **Nodes Offset**: especifica un desplazamiento opcional entre la línea central y la línea de nodos.


</div>

### Vista

-    **Tipo de nodos**: El tipo de nodos estructurales de este objeto, lineal o de área.

-    **Mostrar Nodos**: Muestra u oculta los nodos estructurales.

## Predefinidos

La herramienta Estructura también presenta una serie de elementos predefinidos que permiten construir rápidamente perfiles metálicos estándar o elementos prefabricados de hormigón.

![](images/Arch_presets_example.jpg ) 
*Algunos preajustes para estructuras de acero*

Los elementos predefinidos se obtienen al elegir una **Categoría** del panel de opciones de estructura. Las categorías disponibles son **Prefabricados de hormigón** o cualquiera de los perfiles metálicos estándar de la industria, tales como **HEA**, **HEB** o **INP**. Para cada una de estas categorías, hay una cantidad de predefinidos disponibles. Una vez que se selecciona un predefinido, se pueden ajustar sus parámetros individuales tales como **Longitud**, **Ancho** o **Altura**. Sin embargo, para perfiles metálicos, el tamaño del perfil está establecido por el elemento predefinido y no se puede cambiar.

El botón **Switch L/H** se puede usar para cambiar los valores de Longitud y Altura y, por lo tanto, construir una viga horizontal en lugar de una columna vertical.

<img alt="" src=images/Arch_precast_example.jpg  style="width:960px;"> 
*Algunos preajustes para estructuras prefabricadas de hormigón*

## Nodos estructurales 

Los objetos estructurales también tienen la capacidad de mostrar nodos estructurales. Los nodos estructurales son una secuencia de puntos 3D almacenados en una propiedad \"Nodos\". Al activar o desactivar la propiedad de vista \"Mostrar nodos\", se pueden ver los nodos estructurales de un elemento estructural:

<img alt="" src=images/Arch_structural_nodes.jpg  style="width:960px;"> 
*Nodos estructurales visibles para un conjunto de estructuras*


<div class="mw-translate-fuzzy">

-   Los nodos se calculan y actualizan automáticamente, siempre que no los modifiques manualmente. Si lo hizo, no se actualizarán si la forma del objeto estructural cambia, a menos que use la herramienta \"Restablecer nodos\" a continuación.
-   Las estructuras de arco pueden tener nodos lineales, sino también nodos planos. Para esto, 1- Debe haber al menos 3 vectores en la propiedad \"Nodes\" del objeto, 2- la propiedad \"NodesType\" de su ViewObject se debe establecer en \"Área\".
-   Cuando el cálculo de nodos es automático (es decir, si nunca los tocó manualmente), al establecer la propiedad Rol de una estructura a \"Slab\", se convertirá automáticamente en un nodo plano (habrá más de 3 vectores y el NodesType se establecerá en \"Área\").
-   Al editar un objeto de estructura (hacer doble clic), hay un par de herramientas de nodo disponibles en la vista de tareas:
    -   Restablezca los nodos al cálculo automático, en caso de que los haya modificado manualmente
    -   Edite los nodos gráficamente, funciona de la misma manera que [Draft Edit](Draft_Edit/es.md)
    -   Extiende los nodos del objeto editado hasta que toque el nodo de otro objeto
    -   Hacer el nodo de este objeto y otro coincidente
    -   Activa/desactiva la visualización de todos los nodos de todos los objetos estructurales del documento


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Guion


**Ver también:**

[Arch_API/es](Arch_API/es.md) y [FreeCAD_Scripting_Basics/es](FreeCAD_Scripting_Basics/es.md).


</div>


<div class="mw-translate-fuzzy">

La herramienta Estructura se puede utilizar en [macros](macros/es.md) y desde la consola de [Python](Python/es.md) utilizando las siguientes funciones:


</div>


```python
Structure = makeStructure(baseobj=None, height=None)
Structure = makeStructure(baseobj=None, length=None, width=None, height=None, name="Structure")
```

-   Crea un objeto `Structure` a partir del `baseobj` dado, que es un perfil cerrado, y la extrusión `height` dada.
    -   Si no se da el `baseobj`, puede proporcionar los valores numéricos para el `length`, `width`, y `height` para crear una estructura de bloques.
    -   El `baseobj` también puede ser cualquier objeto sólido existente.

Ejemplo: 
```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(200, 300)
Structure1 = Arch.makeStructure(Rect, height=2000)
FreeCAD.ActiveDocument.recompute()

Structure2 = Arch.makeStructure(None, length=500, width=1000, height=3000)
Draft.move(Structure2, FreeCAD.Vector(2000, 0, 0))
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Structure/es
