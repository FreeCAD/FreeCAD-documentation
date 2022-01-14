# Manual:Parametric objects/es
{{Manual:TOC/es}}

FreeCAD está diseñado para el modelado paramétrico. Esto significa que la geometría que creas, en lugar de ser libremente esculpible, es producida por reglas y parámetros. Por ejemplo, un cilindro puede ser producido a partir de un radio y una altura. Con estos dos parámetros, el programa tiene suficiente información para construir el cilindro.

Los objetos paramétricos, en FreeCAD, son en realidad pequeñas piezas de un programa que se ejecutan siempre que uno de los parámetros ha cambiado. Los objetos pueden tener muchos tipos de parámetros: números (enteros como 1, 2, 3 o valores de punto flotante como 3.1416), tamaños del mundo real (1mm, 2.4m, 4.5ft), coordenadas (x,y,z), cadenas de texto (\"¡hola!\") o incluso otro objeto.

Este último tipo permite construir rápidamente complejas cadenas de operaciones, basándose cada nuevo objeto en uno anterior, y añadiendo nuevas características al mismo.

En el siguiente ejemplo, un objeto sólido y cúbico (Pastilla) se basa en una forma 2D rectangular (Croquis) y tiene una distancia de extrusión. Con estas dos propiedades, produce una forma sólida extruyendo la forma base por la distancia dada. A continuación, puede utilizar este objeto como base para otras operaciones, como dibujar una nueva forma 2D en una de sus caras (Sketch001) y luego hacer una sustracción (Cajera), hasta llegar a su objeto final.

Todas las operaciones intermedias (formas 2D, pastilla, cajery, etc.) siguen estando ahí, y puedes seguir cambiando cualquiera de sus parámetros en cualquier momento. Toda la cadena se reconstruirá (se volverá a calcular) siempre que sea necesario.

![](images/Parametric_objects.jpg )

Es necesario saber dos cosas importantes:

1.  El recálculo no siempre es automático. Las operaciones pesadas, que pueden modificar una gran parte de su documento, y que por lo tanto llevan algún tiempo, no se realizan automáticamente. En su lugar, el objeto (y todos los objetos que dependen de él) se marcarán para su recálculo (aparece un pequeño icono azul sobre ellos en la vista de árbol). A continuación, debe pulsar el botón de recálculo (o **Edición->Refrescar**) para que se vuelvan a calcular todos los objetos marcados.
2.  El árbol de dependencias debe fluir siempre en la misma dirección. Los bucles están prohibidos. (Ver [DAG](Glossary/es#Directed_Acyclic_Graph.md), y [Vista del DAG](DAG_view/es.md)) Puedes tener un objeto A que depende de un objeto B que depende de un objeto C. Pero no puedes tener un objeto A que depende de un objeto B que depende de un objeto A. Eso sería una dependencia circular. Sin embargo, puedes tener muchos objetos que dependen del mismo objeto, por ejemplo los objetos B y C dependen ambos de A. El menú **Herramientas -> Gráfico de dependencia** te muestra un diagrama de dependencia como en la imagen de arriba. Puede ser útil para detectar problemas.

No todos los objetos son paramétricos en FreeCAD. A menudo, la geometría que importas de otros archivos no contendrá ningún parámetro, y serán objetos simples, no paramétricos. Sin embargo, a menudo pueden ser utilizados como una base, o punto de partida para los objetos paramétricos recién creados, dependiendo, por supuesto, de lo que el objeto paramétrico requiere y la calidad de la geometría importada.

Todos los objetos, sin embargo, paramétricos o no, tendrán un par de parámetros básicos, como un Nombre, que es único en el documento y no puede ser editado, una Etiqueta, que es un nombre definido por el usuario que puede ser editado, y una [colocación](placement/es.md), que mantiene su posición en el espacio 3D.

Por último, cabe destacar que los objetos paramétricos personalizados son [fácil de programar en python](Scripted_objects/es.md).

**Leer más**

-   [El editor de propiedades](Property_editor/es.md)
-   [Cómo programar objetos paramétricos](Scripted_objects/es.md)
-   [Posicionamiento de objetos en FreeCAD](Placement/es.md)
-   [Habilitar el gráfico de dependencias](Std_DependencyGraph/es.md)




[<img src="images/Property.png" style="width:16px"> Poweruser Documentation](Category_Poweruser_Documentation.md) [<img src="images/Property.png" style="width:16px"> Tutorials](Category_Tutorials.md)

---
[documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Manual:Parametric objects/es
