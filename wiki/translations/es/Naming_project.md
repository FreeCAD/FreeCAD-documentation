# Naming project/es




{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}

Esta plantilla es la directriz para un proyecto de desarrollo de FreeCAD. Sigue las reglas de la metodología **GTD** [Getting Things Done (GTD)\|](http://en.wikipedia.org/wiki/Getting_Things_Done#Methodology). Los proyectos se recopilan en el [mapa de desarrollo](Development_roadmap/es.md).

## Propósito y principios 

Se trata de un esfuerzo de desarrollo y diseño para implementar una nomenclatura topológica robusta en FreeCAD.

Más detalles sobre la nomenclatura topológica en **[Problema de nomenclatura topológica](Topological_naming_problem/es.md)**.

## Resultado

1.  **Interfaz** en (Part::TopoShape) para referenciar de forma robusta (nombre) formas y subformas (caras, aristas, vértices) a través de una cadena de texto (nombrar los subelementos como \"Face1\")
    Aquí necesitamos una interfaz que proporcione a \'\'\'Part::TopoShape \'\'\' toda la información necesaria para realizar el nombrado, por ejemplo, NewShape, información adicional de un algoritmo como el borrado de caras, paso de modelado (para 2.) y \...
2.  **Asociación** de los pasos de modelado con las caras/aristas resultantes.
    En el caso de un modelo muy grande el usuario está perdido si tiene cientos de redondeos o taladros. De modo que si las caras/aristas supieran en que paso del modelado se han creado podríamos implementar que el doble clic en las caras/aristas abriera la operación correspondiente!
3.  Un **algoritmo** para mantener el nombrado estable a través de los cambios en el historial del modelo, como la división de aristas/caras y el desplazamiento de vértices
    ![](images/NamingExample.jpg )
4.  (opcional) **estructura de datos optimizada en memoria** para mantener sólo las caras/aristas modificadas en cada operación de modelado. Esto será importante cuando el modelo sea grande. No es eficiente copiar la mayor parte de la forma, sería mucho más eficiente compartir las aristas/caras que no han cambiado entre operaciones y copiar sólo lo que ha cambiado.

## Lluvia de ideas 

Se discutió mucho en el post [\"Referencias robusta\"](http://forum.freecadweb.org/viewtopic.php?f=10&t=2656) de jrheinlaender.

### Otros

-   [Topología y denominación genérica de Catia V5](http://www.maruf.ca/files/caadoc/CAATopTechArticles/JournalMethodology.htm#Definition) y [Objetivos de la denominación genérica de Catia V5](http://www.maruf.ca/files/caadoc/CAAMmrTechArticles/CAAMmrGenericNaming.htm#Objectives%20of%20GN)
-   [Nomenclatura topológica en OCAF (Open CASCADE Application Framework)](https://www.opencascade.com/doc/occt-7.4.0/overview/html/occt_user_guides__ocaf.html#occt_ocaf_5_6)

### Literatura & documentación 

-   J Kripac, \"Un mecanismo para la designación topológica persistente de entidades en modelos sólidos paramétricos basados en historial, Simposio sobre modelado de sólidos y aplicaciones 1995, p.21-30\"

:   Describe para realizar el primero de los tres puntos de la lista. Podría decirse que es el modo de designación utilizado en Catia y OCC. Por lo menos la interfaz parece la misma. El documento no está disponible para descargar. Tuve que comprarlo. Si alguien está interesado se lo puedo enviar por email.

-   [Dago AGBODAN, David MARCHEIX y Guy PIERRA, \"Designación persistente para modelos paramétricos, 2000\"](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.29.2836&rep=rep1&type=pdf)

:   Interesante acercamiento a través de estructuras gráficas, trata el punto cuatro de la lista por la reutilización de caras/aristas no modificadas.

-   [Duhwan Mun and Soonhung Han, \"Identificación de entidades topológicas y mapeado de la designación de los cambios en modelos de CAD paramétricos, INTERNATIONAL JOURNAL OF CAD/CAM, 2005, p 69-82\"](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.106.3087&rep=rep1&type=pdf)

:   Muy buena visión general y ejemplos

-   [Farjana, S.H., Han, S. \"Mechanisms of Persistent Identification of Topological Entities in CAD Systems: A Review\", Alexandria Engineering Journal, Volume 57, Issue 4, December 2018, Pages 2837-2849](https://research-management.mq.edu.au/ws/portalfiles/portal/100931773/Publisher_version_open_access_.pdf).

-   [Assembly Solving for Neutral Re-Imported Product Models Tahir A. Jauhar, Soonhung Han, Soonjo Kwon , p.108-123 , CAD Journal 2020, Volume 17 Number 1](http://www.cad-journal.net/files/vol_17/CAD_17(1)_2020_108-123.pdf)

### Resumen del trabajo hasta la fecha 

A fecha de 13 de junio de 2016, este es un resumen del trabajo que se ha realizado para este proyecto:

-   jrheinlaender produjo una gran cantidad de código en 2012 que se basa en gran medida en el ambiente de trabajo de Sketch para resolver \"Referencias Robustas\"
-   ickby había tomado una puñalada en la incorporación de algunos o el código de jrheinlaender en freecad moderno. [Este post](http://forum.freecadweb.org/viewtopic.php?f=10&t=2656&start=60#p124844) tiene un enlace a su repo de github.
-   En 2016, ezzieyguywuf revivió el hilo de jrheinlaender y posteriormente comenzó el suyo propio. Puedes verlo [aquí](http://forum.freecadweb.org/viewtopic.php?f=10&t=15847)
-   ezzieyguywuf desarrolló un programa \"ligero\" de opencascade para duplicar el problema de la denominación topológica y para probar posibles soluciones. Ver su repo de github [freecadTopoTesting](https://github.com/ezzieyguywuf/freecadTopoTesting) aquí
-   ezzieyguywuf incorporó el kit de herramientas TNaming de opencascade en su código de prueba, y mostró cómo esto podría ayudar a resolver algunos de los problemas de Nomenclatura Topológica. Ver el repo de github
-   [Denominación topológica](https://github.com/realthunder/FreeCAD_assembly3/wiki/Topological-Naming) github repositorio por realthunder
-   [Algoritmo de Nombramiento Topológico](https://github.com/realthunder/FreeCAD_assembly3/wiki/Topological-Naming-Algorithm) github repositorio por realthunder

## Organización

### Información sobre TNaming 

Ver [aquí](https://github.com/ezzieyguywuf/freecadTopoTesting/blob/master/TNaming_Writeup.md) para un escrito decente en el repo de github de ezzieyguywuf. Aquí hay algunos puntos destacados:

-   El TNaming de opencascade se basa en el [marco de datos TDF\_Data](https://dev.opencascade.org/doc/occt-7.5.0/refman/html/class_t_d_f___reference.html#details).
-   TDF\_Data es un componente clave de la cosa OCAF de opencascade, pero puede ser utilizado independientemente de ella
-   TDF\_Data es esencialmente un árbol en el que los datos se añaden y se leen en una fecha posterior.
-   Cada vez que se añade un atributo TNaming\_NamedShape a un nodo del árbol TDF\_Data, se añade un atributo TNaming\_UsedShapes a la raíz del árbol
    -   NOTA: Este atributo TNaming\_UsedShapes es fundamental para la utilidad del kit de herramientas TNaming. Contiene un historial de todas las TopoDS\_Shape utilizadas durante la \"historia\" de la pieza
-   TNaming\_Builder se utiliza para añadir información al árbol TDF\_Data. Añade una TNaming\_NamedShape a un nodo determinado del árbol, además de actualizar la base de datos TNaming\_UsedShapes según sea necesario.
-   Cada vez que se modifica el TopoDS\_Shape, debe registrarse en la estructura TDF\_Data
    -   De nuevo, TNaming\_Builder se utiliza para esto
    -   Ver [aquí](http://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__ocaf.html#occt_ocaf_5_6_1) en la documentación de opencascade para una tabla que lista lo que debe ser almacenado en la base de datos. **NOTA:** esta tabla parece estar incompleta. Es posible que haya que hacer algunas pruebas adicionales
    -   En resumen, cada vez que se modifique la TopoDS\_Shape, cualquier característica modificada/generada/borrada debe ser registrada. En su mayor parte, ya que estamos tratando con sólidos, esto significa que debemos registrar las Caras modificadas/generadas/borradas en el sólido
-   La clase TNaming\_Selector se utiliza para \"seleccionar\" una característica que está siendo rastreada en el árbol TDF\_Data
    -   Una característica \"seleccionada\" es aquella a la que el algoritmo TNaming de opencascade mantendrá una referencia constante, independientemente de los cambios topológicos.

## Siguientes acciones 

-   Definir el alcance
-   Casos de prueba en Python
-   Interfaz en Part::TopoShape (+ vinculación con Python)

### Siguientes pasos (a partir del 13 de junio de 2016) 

1.  Determinar si el kit de herramientas de TNaming de opencascade resuelve completamente el problema de Nomenclatura Topológica en FreeCAD.
    -   ¿Cuáles son todos los casos en los que la Nomenclatura Topológica es un problema?
    -   ¿Cuáles son los escenarios complejos en los que este enfoque deberá funcionar?
2.  Incorporar el código de TNaming en FreeCAD
    1.  Empezar con un enfoque básico, es decir, hacer un cubo y un cilindro, fusionar, filetear, y luego redimensionar el cilindro. El filete no debe moverse
    2.  Añadir gradualmente más funcionalidad
3.  Determine si TNaming será la solución a largo plazo
4.  Tanto si TNaming es la solución a largo plazo como si no lo es, hay que encontrar una forma de \'serializar/deserializar\' los datos que TNaming utiliza para la persistencia entre sesiones




[Category:Roadmap](Category:Roadmap.md)
