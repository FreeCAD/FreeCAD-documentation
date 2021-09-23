# OpenCASCADE/es
{{TOCright}}

## Descripción

[OpenCASCADE Tecnología](OpenCASCADE/es.md), La *OCC* o *OCCT*, para abreviar, es una colección de bibliotecas C++ que juntas constituyen un núcleo de diseño asistido por ordenador (CAD) profesional para modelar objetos 2D y 3D, y construir herramientas especializadas para la fabricación, simulación o visualización. OpenCASCADE es el corazón de las capacidades geométricas de FreeCAD.

Las clases geométricas de OCCT están en su mayoría implementadas y disponibles en FreeCAD a través del módulo [Pieza](Part_Workbench/es.md), del que dependen la mayoría de los otros [Ambiente de trabajo](Workbench/es.md). También proporciona funciones internas para leer y escribir diferentes formatos de archivo como STEP e IGES, y para realizar proyecciones 2D, que pueden ser utilizadas para crear dibujos técnicos en [TechDraw](TechDraw_Workbench/es.md).

<img alt="" src=images/Part_Workbench_relationships.svg  style="width:600px;">


*OpenCASCADE proporciona las clases geométricas básicas y las funciones de dibujo al módulo [Pieza](Part_Workbench.md), que luego son utilizadas por todos los ambientes de trabajo en FreeCAD.*

OpenCASCADE no debe confundirse con [OpenSCAD](https://www.openscad.org/), que es un proyecto de código abierto diferente para construir modelos 3D, y que es accesible a través del [Ambiente de trabajo OpenSCAD](OpenSCAD_Workbench/es.md).

OpenCASCADE es un software libre que se rige por los términos de la Licencia Pública General Reducida de GNU (LGPL) versión 2.1 con una excepción adicional.

## Instalación

OpenCASCADE es un componente básico de FreeCAD, por lo que si obtiene FreeCAD de uno de los enlaces de la página [Descarga](Download/es.md), lo tendrá instalado, y no será necesaria ninguna otra instalación.

Sin embargo, si quieres desarrollar aplicaciones que utilicen OCCT, o quieres contribuir con código C++ a FreeCAD, entonces necesitas instalar los archivos de desarrollo de OCCT. En este caso, el procedimiento se explica en [Compilación](Compiling/es.md) para cada uno de los sistemas principales, Linux, Windows y MacOS.

## Edición comunitaria 

En 2011 se publicó una \"edición comunitaria\" de OpenCASCADE, abreviada OCE, basada en las fuentes oficiales de OpenCASCADE (OCCT) de la versión 6.5. En teoría, la edición comunitaria OCE debería ser compatible con la versión principal OCCT en la mayoría de los aspectos, al tiempo que cuenta con algún código adicional aportado por la comunidad.

Sin embargo, esta distribución alternativa dejó de desarrollarse activamente alrededor de 2017, y se quedó atrás con respecto a la versión principal en términos de características y correcciones de errores. Por esta razón, desde FreeCAD v0.17, FreeCAD se compila exclusivamente con OCCT, y OCE no se prueba.

En algunas distribuciones antiguas de Linux, FreeCAD se compila contra OCE 0.18, equivalente a OCCT 6.9.x, causando varios problemas que ya han sido resueltos en las versiones principales de OCCT 7.x. Si este es el caso, intenta eliminar OCE, e instalar OCCT en su lugar. Si esto no es posible, utiliza la [AppImagen](AppImage/es.md) para obtener un FreeCAD moderno con una versión actualizada de OCCT.

## Historia

El núcleo geométrico Cas.CADE era originalmente de código cerrado, pero se convirtió en código abierto con su nombre actual alrededor del año 2000. Poco después, se inició el proyecto FreeCAD, cuyos archivos más antiguos datan de enero de 2001. Lea más en [Historia](History/es.md).

La versión 6.6 de OpenCASCADE y las anteriores se regían por su propia \"licencia pública OCCT\", lo que hacía que no fuera del todo \"software libre\". Esto se solucionó con el lanzamiento de OCCT 6.7 (2013), cuando adoptó la licencia LGPL2.

## OCCT Conceptos geométricos 

En la terminología de OpenCascade, distinguimos entre primitivas geométricas y formas topológicas. Una primitiva geométrica puede ser un punto, una línea, un círculo, un plano, etc. o incluso algunos tipos más complejos como una curva B-Spline o una superficie. Una forma puede ser un vértice, una arista, un hilo, una cara, un sólido o un compuesto de otras formas. Las primitivas geométricas no están hechas para ser mostradas directamente en la escena 3D, sino para ser utilizadas como geometría de construcción para las formas. Por ejemplo, una arista puede construirse a partir de una línea o de una porción de un círculo.

En resumen, las primitivas de geometría son bloques de construcción \"sin forma\", mientras que [formas topológicas](Part_TopoShape/es.md) son los objetos reales construidos sobre ellas.

La lista completa de todas las primitivas y formas se puede consultar en la [OCC documentation](http://www.opencascade.org/org/doc/) (Alternative: [sourcearchive.com](https://www.opencascade.com/doc/occt-7.4.0/refman/html/)) y busque **Geom\_\*** (para primitivas geométricas) y **TopoDS\_\*** (para formas). Allí también puedes leer más sobre las diferencias entre ellos. Tenga en cuenta que la documentación oficial de OCC no está disponible en línea (debe descargar un archivo) y está dirigida principalmente a los programadores, no a los usuarios finales. Pero esperamos que encuentre suficiente información para empezar. Consulte también [Guía del usuario de datos de modelado](https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__modeling_data.html).

> \'\'En un nivel muy alto, la topología indica de qué piezas está hecho un objeto y las relaciones lógicas entre ellas. Una forma está formada por un determinado conjunto de caras. Una cara está delimitada por un determinado conjunto de aristas. Dos caras son adyacentes si comparten una arista común\".

> \'\'La topología por sí sola no indica el tamaño, la curvatura o la ubicación en 3D de ninguna de esas piezas. Sin embargo, cada pieza de la topología sabe sobre su geometría subyacente. Una cara sabe en qué superficie se encuentra. Una arista sabe en qué curva se encuentra. La geometría conoce la curvatura y la ubicación en el espacio\". - [Fuente](https://www.opencascade.com/content/geometry-and-topology)


<hr />

> \'\'Por lo tanto, la topología define la relación entre entidades geométricas simples, que pueden vincularse entre sí para representar formas complejas\". - [Guía del usuario de datos de modelado](https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__modeling_data.html)

![](images/ClassTopoDS_Shape_inherit_graph.png )

**Nota:** Sólo 3 tipos de objetos topológicos tienen representaciones geométricas - vértice, arista y cara ([Fuente](https://opencascade.blogspot.com/2009/02/topology-and-geometry-in-open-cascade.html)).

Los tipos geométricos pueden dividirse en dos grandes grupos: curvas y superficies. De las curvas (línea, círculo, \...) se puede construir directamente una arista, de las superficies (plano, cilindro, \...) se puede construir una cara. Por ejemplo, la línea primitiva geométrica es ilimitada, es decir, está definida por un vector base y un vector de dirección, mientras que su representación de forma debe ser algo limitado por un punto inicial y otro final. Y una caja -un sólido- puede crearse mediante seis planos limitados.

A partir de una arista o cara también se puede volver a su contrapartida geométrica primitiva.

Así, a partir de las formas se pueden construir piezas muy complejas o, al revés, extraer todas las subformas de las que está hecha una forma más compleja.

<img alt="" src=images/Part_TopoShape_relationships.svg  style="width:600px;">


*La clase `Part::TopoShape* es el objeto geométrico que se ve en pantalla. Esencialmente todos los ambientes de trabajo utilizan estos [TopoFormas](Part_TopoShape/es.md) internamente para construir y mostrar aristas, caras y sólidos.`

## Relacionados

-   Tecnología OpenCASCADE (OCCT) [sitio web principal](http://www.opencascade.com)
-   OCCT [portal de desarrollo](https://dev.opencascade.org/)
-   OCCT [última versión](https://www.opencascade.com/content/latest-release)
-   OCCT [repositorio git](https://git.dev.opencascade.org/gitweb/?p=occt.git)
-   OpenCASCADE Community Edition (OCE) [repositorio git](https://github.com/tpaviot/oce)
-   [Open Cascade Technology OCCT](http://en.wikipedia.org/wiki/Open_Cascade_Technology) en Wikipedia
-   Glosario, [Open CASCADE](Glossary#Open_CASCADE.md)
-   Seguimiento de los errores de OCCT en el bugtracker de FreeCAD [(hilo)](https://forum.freecadweb.org/viewtopic.php?f=10&t=20264)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > OpenCASCADE/es
