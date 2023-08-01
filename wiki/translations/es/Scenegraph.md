# Scenegraph/es
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

La geometría que aparece en las vistas 3D de FreeCAD son renderizadas por la biblioteca Coin3D. Coin3D es una implementación del estandard [OpenInventor](http://en.wikipedia.org/wiki/Open_Inventor). El software OpenCascade también proporciona la misma funcionalidad, pero se decidió, al comenzar el desarrollo de FreeCAD, no utilizar el visor de OpenCascade, sino cambiar al software Coin3D, por tener mejor rendimiento. Un buen modo de aprender sobre esa librería es el libro [Open Inventor Mentor](http://www-evasion.imag.fr/Membres/Francois.Faure/doc/inventorMentor/sgi_html/).


</div>

## Description


<div class="mw-translate-fuzzy">

[OpenInventor](http://en.wikipedia.org/wiki/Open_Inventor) es en realidad un lenguaje de descripción de escena 3D. La escena descrita en openInventor es seguidamente renderizada en la pantalla con OpenGL. Coin3d se encarga de hacer esto, por lo que el programador no tiene que lidiar con complejas llamadas a OpenGL, bastará con que le proporcione código OpenInventor válido. La gran ventaja es que openInventor es un estándard muy bien conocido y bien documentado.


</div>


<div class="mw-translate-fuzzy">

Uno de los trabajos mas inportantes que FreeCAD hace por ti es, básicamente, traducir la información de geometría OpenCascade al idioma de openInventor.


</div>


<div class="mw-translate-fuzzy">

OpenInventor describe una escena 3D en forma de una [escena gráfica](http://en.wikipedia.org/wiki/Scene_graph) (scenegraph), como la siguiente:


</div>

![](images/Scenegraph.gif )


<div class="mw-translate-fuzzy">

![](images/Scenegraph.gif ) image from [Inventor mentor](http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html)


</div>


<div class="mw-translate-fuzzy">

Una escena gráfica de openInventor describe todo lo que es parte de una escena 3D, como la geometría, colores, materiales, luces, etc, y organiza todos los datos en una estructura cómoda y clara. Todo puede agruparse en sub-estructuras, lo que te permite organizar los contenidos de tu escena más o menos de la forma que quiera. He aquí un ejemplo de un archivo de openInventor:


</div>


{{Code|lang=bash|code=
#Inventor V2.0 ascii
 
Separator { 
    RotationXYZ {   
       axis Z
       angle 0
    }
    Transform {
       translation 0 0 0.5
    }
    Separator { 
       Material {
          diffuseColor 0.05 0.05 0.05
       }
       Transform {
          rotation 1 0 0 1.5708
          scaleFactor 0.2 0.5 0.2
       }
       Cylinder {
       }
    }
}
}}


<div class="mw-translate-fuzzy">

Como puedes ver, la estructura es muy simple. Utiliza separadores para organizar los datos en bloques, parecido a como harías al organizar tus archivos en carpetas. Cada declaración afecta a lo que viene después, por ejemplo los dos primeros puntos de nuestro separador raíz son una rotación y una traslación, todo ello afectará al siguiente elemento, que es un separador. En ese separador, se define un material y otra transformación. Nuestro cilindro por lo tanto se verá afectado por las dos transformaciones, la que le fue aplicada directamente, y la que se aplicó al separador que le contiene.


</div>


<div class="mw-translate-fuzzy">

También tenemos muchos otros tipos de elementos para organizar nuestra escena, como los grupos, conmutadores o anotaciones. Podemos definir materiales muy complejos para nuestros objetos, con el color, las texturas, los modos de sombreado y transparencia. También podemos definir las luces, cámaras, e incluso movimiento. También es posible integrar pedazos de secuencias de comandos en los archivos de openInventor, para definir comportamientos más complejos.


</div>


<div class="mw-translate-fuzzy">

Si estás interesado en aprender más sobre openInventor, vete directamente a su referencia más famosa, [Inventor mentor](http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html).


</div>


<div class="mw-translate-fuzzy">

En FreeCAD, normalmente, no es necesario interactuar directamente con la escena gráfica (scenegraph) de openInventor. Cada objeto en un documento de FreeCAD, ya sea una malla, una forma de pieza o cualquier otra cosa, se convierte automáticamente en código de openInventor y se inserta en la escena gráfica (scenegraph) principal que aparecen en una vista 3D. Esa escena gráfica se actualiza continuamente cuando se hacen modificaciones, se añaden o eliminan objetos en el documento. De hecho, cada objeto (en el espacio App) tiene un proveedor de vista (un objeto correspondiente en el espacio de la interfaz gráfica del usuario GUI), responsable de la expedición de código de openInventor.


</div>


<div class="mw-translate-fuzzy">

Pero poder acceder a la escena gráfica directamente tiene muchas ventajas. Por ejemplo, puedes cambiar temporalmente la apariencia de un objeto, o podemos agregar objetos a la escena que no tienen existencia real en el documento de FreeCAD, como la geometría constructiva, ayudantes, sugerencias o herramientas gráficas como manipuladores o información en pantalla.


</div>


<div class="mw-translate-fuzzy">

FreeCAD cuenta con varias herramientas para ver o modificar código de openInventor. Por ejemplo, el código de Python siguiente muestra la representación en openInventor de un objeto seleccionado:


</div>


```python
obj = FreeCAD.ActiveDocument.ActiveObject
viewprovider = obj.ViewObject
print viewprovider.toString()

```


<div class="mw-translate-fuzzy">

Pero también tenemos un módulo de Python que permite un acceso completo a todo lo controlado por Coin3d, como la escena gráfica (scenegraph) de FreeCAD. Sigue leyendo en [Pivy](Pivy/es.md).


</div>

## Coding examples 

See [Coin3d snippets](Coin3d_snippets.md) courtesy of MariwanJ\'s research for the [Design456 Workbench](Design456_Workbench.md). The code repository can be found at <https://github.com/MariwanJ/COIN3D_Snippet>. {{Top}}


<div class="mw-translate-fuzzy">


{{docnav/es|Mesh to Part/es|Pivy/es}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Scenegraph/es
