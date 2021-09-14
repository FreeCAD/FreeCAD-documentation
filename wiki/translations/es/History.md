# History/es

 \_\_FORCETOC\_\_

## Historia

<img alt="Primera versión de FreeCAD, desconocida" src=images/Screenshot_mesh.jpg  style="width:300px;"> <img alt="FreeCAD versión 0.7 de 2009" src=images/Part_BooleanOperations.png  style="width:300px;">

### Cómo empezó todo 

FreeCAD comenzó en enero de 2001 cuando [Jürgen Riegel](User:Jriegel.md) empezó a trabajar en el proyecto Cas.CADE. Cas.CADE era un marco de desarrollo de software comercial que incluía un [núcleo de modelado geométrico](Glossary#Geometric_modeling_kernel.md) (o kernel CAD): fue publicado bajo una licencia de código abierto en el año 2000 y rebautizado como [OpenCASCADE](OpenCASCADE/es.md). Esto hizo posible la realización de un programa de CAD 3D de código abierto, ya que tener que programar un núcleo de CAD desde cero habría requerido una enorme cantidad de trabajo.

En las palabras propio del Jürgen:


{{Quote|text=''El proyecto FreeCAD fue iniciado por mí en enero de 2001, como un llamado GOM (Modelador gráfico de objetos), con la idea de usar Qt, Python y Cas.CADE, un CAD Kernel comercial que en ese momento usaba en los proyectos de Daimler. Cas.CADE se convirtió en código abierto poco antes, por lo que parecía el momento adecuado para intentar un movimiento en el, en ese momento, espacio vacío de CAD de código abierto. Tuve una experiencia de dos años con OpenCascade en un proyecto llamado QSpect en el que, al final, fui el principal diseñador de software. Aprendí mucho sobre 3D y programación CAD. También me influyó Catia V5 y su muy especial interfaz de usuario y programación... En el 17 de marzo de 2002, dentro del proyecto OpenCascade, registré el software como FreeCAD. No se me ocurrió un nombre mejor, soy muy malo con los nombres... En abril de 2003, Werner Meyer, uno de los compañeros del proyecto QSpect, se pasó a una empresa llamada Imetric. El contacto con Imetric resultó muy prometedor ya que buscaban una nueva plataforma de software 3D para sus sensores 3D. En 2005, Imetric donó la mayor parte de su módulo de malla a FreeCAD y a la comunidad de código abierto, y desde entonces utilizaron FreeCAD como base para el software de su sistema de sensores. Desde entonces, Werner Meyer es un desarrollador muy activo de FreeCAD. En 2005, después de un año de lucha, decidí arrancar el marco documental de OpenCascade y sustituirlo por una implementación propia. Así que, al final, sólo utilizamos el núcleo CAD de OpenCascade y no el resto de su Framework. 2007 fue otro hito interesante. Cambiamos a QT4 y, por tanto, a la LGPL. En ese momento hicimos mucho trabajo, principalmente Werner''.
|sign=[Jürgen Riegel](User:Jriegel.md)|source=''[http://forum.freecadweb.org/viewtopic.php?f=8&t=295 ¿Quién está detrás de FreeCad?]''}}

El proyecto se anunció al público en general en el [OpenCascade Forum](https://dev.opencascade.org/forums) en 2003:


{{Quote|text=''Hola a todos, mi nombre es Juergen Riegel y hoy quiero anunciar un proyecto OpenCasCade, FreeCAD. Es un RAD CAx de código abierto basado en OpenCasCade, QT y Python. Presenta algunos conceptos clave como la grabación de macros, los bancos de trabajo, la capacidad de ejecutarse como servidor y como extensión de aplicaciones cargables dinámicamente, y está diseñado para ser independiente de la plataforma... Aunque se encuentra en una fase temprana y no es utilizable por los usuarios ni por los desarrolladores -la primera versión para usuarios está prevista para finales de 2003-, me gustaría recibir algunos comentarios sobre la dirección y el diseño de FreeCAD. La interfaz gráfica de usuario está casi terminada y ahora nosotros, mi co-desarrollador Werner Mayer y yo, hemos empezado a añadir las primeras funciones CAD. FreeCAD puede ser visto como un sistema de CAD mecánico de propósito general, pero su primera audiencia, creo, serán los desarrolladores de CAx que necesitan un trabajo de base para su propio desarrollo''.
|sign=[Jürgen Riegel](User:Jriegel.md)|source=''[https://dev.opencascade.org/content/announcing-freecad-project Announcing FreeCAD Project on Sun, 08/17/2003 - 19:23]''}}

### Werner Mayer 

Werner Mayer se unió al proyecto tan pronto como se anunció como proyecto de código abierto (antes del anuncio el proyecto era un proyecto privado de Jürgen). Véase este mensaje de Werner en el foro en alemán: <https://forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>

Con el tiempo, el proyecto fue ganando adeptos y se incorporaron nuevos colaboradores clave en la comunidad.

-   **Inicio de Linux**


{{Quote|text=''Un hecho divertido es que quería tener un software CAD de código abierto principalmente para Linux porque en ese momento no existía nada para esta plataforma. Sin embargo, desde el principio desarrollamos exclusivamente en Windows durante los siguientes 1,5 años. Entonces un checo hizo una contribución para hacer el código del núcleo en Linux: https://github.com/berndhahnebach/All_FreeCAD/commit/9fd2e27c95ba3dc84778d92e2564cd094793ce2f#diff-480477e89f9b6ddafb30c4383dcdd705''}}


{{Quote|text=''Medio año más tarde continué la construcción de Linux: https://github.com/berndhahnebach/All_FreeCAD/commit/35b962d7d751dd80f7c7781df60f93bc9a3da992''}}

**P:** ¿Podría compartir cómo fue ese primer año y medio? ¿Se conocieron en persona o en línea?


{{Quote|text=''Bueno, en aquella época éramos colegas (hasta 2005), así que podíamos discutir las cosas cara a cara. Después de esa época, seguimos teniendo algunos encuentros personales, pero discutimos la mayoría de las cosas por correo electrónico o por teléfono.''}}


{{Quote|text=''Como tercer desarrollador del núcleo, Yorik se unió a finales de 2007, pero pasaron otros 3 o 4 años hasta que la comunidad y el número de colaboradores empezaron a crecer significativamente.''}}

**P:** ¿Dividieron las tareas o trabajaron en implementaciones que competían entre sí?


{{Quote|text=''Sí. Jürgen diseñaba e implementaba la mayor parte de la aplicación y la lógica del documento y yo hacía lo básico de la interfaz gráfica de usuario.

''}}


{{Quote|text=''Sin embargo, no ha sido un proceso gradual, sino que hemos experimentado con muchas cosas al principio. Por ejemplo, en la versión inicial utilizamos el marco documental de OCC, OCAF, y su visor, pero al cabo de uno o dos años nos metimos en un callejón sin salida porque la documentación sobre OCC era muy pobre y no conseguimos que funcionara para ampliar OCAF con nuestros propios tipos de características. Así que decidimos utilizar únicamente las capacidades de modelado de OCC pero desarrollar nuestro propio marco de aplicación/documento.''}}

**P:** En aquel momento, ¿pensabas que FreeCAD estaría donde está hoy?


{{Quote|text=''No lo sabíamos pero lo esperábamos. Por supuesto, no podíamos anticipar cómo se vería exactamente FreeCAD hoy en día.<br>Las decisiones de diseño más importantes fueron hacer que estuviera disponible en todas las plataformas principales y hacer que todo el SW fuera lo más accesible posible, es decir, imponer todas las funciones importantes a Python para que los usuarios (avanzados) pudieran extender FreeCAD con sus propias funciones. De esta manera esperábamos conseguir una amplia audiencia.''}}

(Ver este post del foro de Werner [Re: Historia de FreeCAD](https://forum.freecadweb.org/viewtopic.php?f=8&t=47703#p411612))

### Yorik se une al proyecto 

[Yorik van Havre](User:Yorik.md) se unió al proyecto en 2008 y comenzó a trabajar en el [Módulo de Borrador](Draft_Workbench.md). Antes de ese momento, no había forma de crear geometría 2D a través de la [GUI](Glossary#GUI.md). Este módulo fue programado completamente en Python en lugar de en C++ (el lenguaje de programación principal utilizado en FreeCAD). El nuevo banco de trabajo de Borrador demostró que la integración de Python era un éxito y que podía utilizarse para ampliar o personalizar las capacidades de FreeCAD. Además de su trabajo en el módulo Draft, Yorik trabajó en la expansión de la documentación de FreeCAD, y se convirtió en el \"director de arte\" de facto de FreeCAD, creando muchos iconos para la interfaz gráfica de FreeCAD y [definiendo su estilo](Artwork/es.md).

La versión 0.7 de FreeCAD lanzada en abril de 2009 fue la primera en incluir el módulo Borrador. El módulo Pieza proporcionaba un simple flujo de trabajo de [CSG](Glossary#Geometría_Sólida_Constructiva.md) con la creación de formas primitivas y operaciones booleanas accesibles a través del menú Pieza. También era posible la extrusión de perfiles 2D y el Redondeado.

La versión 0.8, lanzada en julio de 2009, incluyó más trabajo en el módulo de Borrador, incluyendo una nueva herramienta de Dimensión. El módulo de Pieza se benefició de una nueva barra de herramientas junto con nuevas herramientas, Revolver y Sección.

A finales de 2009, FreeCAD fue aceptado como paquete Debian en los repositorios de Debian. FreeCAD se añadió a los repositorios de Ubuntu 10.04 en 2010.

### El proyecto continúa 

La versión 0.10 fue lanzada en julio de 2010 e introdujo el [Ambiente de trabajo Croquizador](Sketcher_Workbench/es.md), basado en Sketchsolve, un solucionador basado en restricciones para crear geometría 2D. La primera versión estaba limitada a la creación de rectángulos y líneas.

A principios de 2011, aprovechando la oportunidad que ofrecía la plataforma online [Launchpad](https://launchpad.net), se creó el [FreeCAD Equipo de mantenimiento](https://launchpad.net/~freecad-maintainers) para proporcionar nuevas versiones estables junto con paquetes de construcción diarios de FreeCAD a los usuarios del sistema operativo Ubuntu.

La versión 0.11 fue lanzada en mayo de 2011 e introdujo el nuevo ambiente de trabajo DiseñoPieza que incluía herramientas como Pastilla, Cajera, Redondeado y Chaflán. El ambiente de trabajo de Borrador recibió mejoras y nuevas herramientas, como BSpline. El ambiente de trabajo de Robot presentó más herramientas de la interfaz gráfica de usuario.

La versión 0.12 se publicó en enero de 2012 y ofrecía un ambiente de trabajo de Coquizador más completo. Incluía un solucionador totalmente reescrito, FreeGCS. Fue el resultado de meses de trabajo de los principales desarrolladores de FreeCAD junto con los recién llegados logari81 (que programó el solucionador) y mrlukeparry. Se añadieron más herramientas al ambiente de trabajo de DiseñoPieza.

### Ampliación del equipo de desarrolladores del núcleo 

En abril de 2019 se amplió el equipo de desarrolladores del núcleo: A Jürgen, Werner y Yorik se unieron Abdullah, Bernd, sliptonic y WandererFan

## Mensajes interesantes en el foro 

-   sobre PartDesignNext y otras decisiones de diseño: <https://forum.freecadweb.org/viewtopic.php?f=8&t=34923&start=130#p297074>
-   sobre la historia del foro: <https://forum.freecadweb.org/viewtopic.php?f=8&t=7448&start=200#p287106>
-   sobre la historia del proyecto: <https://forum.freecadweb.org/viewtopic.php?f=8&t=47703>
-   sobre la historia del código: <https://forum.freecadweb.org/viewtopic.php?f=10&t=46733&start=10#p405068> BTW: el checkin inicial del código fue el 18 de marzo de 2002 (¿puede ser el cumpleaños?)
-   Sobre el proyecto que será de código abierto: <https://forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>
-   sobre el historial de commits de la versión: <https://forum.freecadweb.org/viewtopic.php?f=8&t=23695#p184940>
-   sobre quién está detrás de FreeCAD: <http://forum.freecadweb.org/viewtopic.php?f=8&t=295>
-   sobre la historia MEF: <https://forum.freecadweb.org/viewtopic.php?f=18&t=48646#p416389>
-   sobre la historia MEF Mesher: <https://forum.freecadweb.org/viewtopic.php?f=18&t=48733#p417627>

## Historia del lanzamiento 

#### Overview

  Versión   Nombre del lanzamiento   Fecha de lanzamiento   Notas de lanzamiento                                             Compromiso de lanzamiento                                                                 Rama de lanzamiento
  --------- ------------------------ ---------------------- ---------------------------------------------------------------- ----------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------
  0.20      ?                        en desarrollo          [Notas del lanzamiento 0.20](Release_notes_0.20/es.md)   [head master](https://github.com/FreeCAD/FreeCAD/commits/master)                          
  0.19      \-                       2021-03-20             [Notas del lanzamiento 0.19](Release_notes_0.19/es.md)   [release commit 0.19](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-19)   [branch bugfixes 0.19](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-19)
  0.18      \-                       2019-03-12             [Release notes 0.18](Release_notes_0.18.md)              [release commit 0.18](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-18)   [branch bugfixes 0.18](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-18)
  0.17      Roland                   2018-04-06             [Release notes 0.17](Release_notes_0.17.md)              [release commit 0.17](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-17)   [branch bugfixes 0.17](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-17)
  0.16      \-                       2016-04-18             [Release notes 0.16](Release_notes_0.16.md)              [release commit 0.16](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-16)   [branch bugfixes 0.16](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-16)
  0.15      \-                       2015-04-08             [Release notes 0.15](Release_notes_0.15.md)              [release commit 0.15](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-15)   [branch bugfixes 0.15](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-15)
  0.14      \-                       2014-07-01             [Release notes 0.14](Release_notes_0.14.md)              [release commit 0.14](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-14)   [branch bugfixes 0.14](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-14)
  0.13      \-                       2013-01-29             [Release notes 0.13](Release_notes_0.13.md)              [release commit 0.13](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-13)   [branch bugfixes 0.13](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-13)
  0.12      \-                       2011-12-20             [Release notes 0.12](Release_notes_0.12.md)                                                                                                        
  0.11      \-                       2011-05-03             [Release notes 0.11](Release_notes_0.11.md)                                                                                                        
  0.10      \-                       2010-07-24                                                                                                                                                                        
  0.9       \-                       2010-01-16                                                                                                                                                                        
  0.8       \-                       2009-07-10                                                                                                                                                                        
  0.7       \-                       2009-04-24                                                                                                                                                                        
  0.6       \-                       2007-02-27                                                                                                                                                                        
  0.5       \-                       2006-10-05                                                                                                                                                                        
  0.4       \-                       2006-01-15                                                                                                                                                                        
  0.3       \-                       2005-10-31                                                                                                                                                                        
  0.2       \-                       2005-08-09                                                                                                                                                                        
  0.1       \-                       2003-01-27                                                                                                                                                                        
  0.0.1     \-                       2002-10-29             Initial Upload of a version                                                                                                                                

#### Leyenda

  Color   Version Type
  ------- --------------------------------
          Future release
          Latest preview version
          **Latest version**
          Older version, still supported
          Old version
          

## Enlaces externos 

-   [Sección de archivos de SourceForge](http://sourceforge.net/projects/free-cad/files/)
-   [Sección de archivos antiguos de SourceForge](http://sourceforge.net/projects/free-cad/files/OldFiles/)
-   [Anunciando el proyecto FreeCAD](http://www.opencascade.org/org/forum/thread_6572/?forum=11) en el foro de OpenCascade

[Category:News](Category:News.md)
