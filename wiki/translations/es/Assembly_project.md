# Assembly project/es



**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}


<div class="mw-translate-fuzzy">

Aquí está la planificación del proyecto para el módulo de **Ensamblaje** como parte del [Mapa de desarrollo](Development_roadmap/es.md)


</div>


<div class="mw-translate-fuzzy">

## Propósito y principios 

Este es un proyecto de desarrollo de software cuya intención es implementar capacidades para la creación de ensamblajes y productos. Trata de la implementación de algunas **características principales** en los módulos de CAD de FeeCAD, **Piezas y Ensamblaje**.


</div>


<div class="mw-translate-fuzzy">

Los pasos del desarrollo se planifican aquí y se siguen en el sistema de gestión de incidencias para conseguir un histórico de cambios bien definido: [Sistema de gestión de incidencias](http://apps.sourceforge.net/mantisbt/free-cad/my_view_page.php)


</div>

You may want to check out current developments in [External Workbenches](External_Workbenches.md), section [Assembly](External_workbenches#Assembly.md).


<div class="mw-translate-fuzzy">

## Resultado

La intención del proyecto es permitir a FreeCAD lograr una tarea de diseño como está:


</div>

<img alt="" src=images/Gripper.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

Esto se logrará utilizando el **Ensamblaje** para poner todos los diferentes tipos de piezas juntas con restricciones y permanecer lo más cerca que se pueda de la especificación ISO 10303 para permitir un intercambio de modelos sencillo.


</div>

Otro objetivo es utilizar [ODE](http://en.wikipedia.org/wiki/Open_Dynamics_Engine) para la cinemática.

## Tormenta de ideas 


<div class="mw-translate-fuzzy">

### Modelo múltiple 

<img alt="" src=images/MultiModel.png  style="width:600px;"> Una característica importante para los diseños del mundo real es la habilidad de dividir un diseño en partes más manejables. Es imposible trabajar en todos los aspectos de un diseño al mismo tiempo o por separado. Esto es cierto para la geometría y también para las tareas de ingeniería como CAE o CAM. Por eso FreeCAD necesita la posibilidad de dividir los modelos. Esto abre algunas posibilidades:

-   **Carga retardada** - Sólo se necesitan recursos como los gráficos y la memoria principal para la pieza en la que se está trabajando.
-   [**Ingeniería concurrente**](http://en.wikipedia.org/wiki/Concurrent_engineering) - Permite a varias personas trabajar en el mismo diseño
-   [**Control de versiones**](http://es.wikipedia.org/wiki/Control_de_versiones) - Mejorar el control sobre diversos aspectos del diseño
-   y muchas otras\....


</div>


<div class="mw-translate-fuzzy">

Un diseño de modelo múltiple podría parecerse a este:


</div>


<div class="mw-translate-fuzzy">

### Gestor de proyecto 

Modelo múltiple significa un montón de archivos que pertenecen a un proyecto, normalmente bajo un directorio común. Un archivo de proyecto y un explorador de proyecto (project browser) pueden ayudar a organizar los archivos. También pueden guardar información adicional sobre el proyecto o una website del proyecto.


</div>

1\. Dos modos, el modo \"Simple\" y el modo \"Proyecto\". \"Simple\" significa que sólo hay un documento, y todos los ensamblajes y piezas van en ese documento. Si se crea o abre un Proyecto, FreeCAD está en modo \"Proyecto\".


<div class="mw-translate-fuzzy">

2\. Proyectos. La posición del archivo FCPrj en el disco define un directorio raíz. Todos los archivos contenidos en este directorio están definidos con rutas relativas al directorio raíz. Una vista adicional a la izquierda contendrá el ProjectExplorer que mostrará el árbol de directorios con los archivos manejados.

Este directorio raíz se utiliza también como raíz para un entorno de pruebas SVN, que permitirá después facilitar el compartir y el control de versiones.

Las referencias externas (a un directorio fuera del directorio raíz, un servidor compartido o un recurso web) se manejarán y mostrarán de forma separada en el ProjectExplorer (un pseudo directorio para cada archivo de servidor o servidor web). Esto hace posible conseguir un rápido resumen sobre las referencias externas y redefinir sus rutas.


</div>


<div class="mw-translate-fuzzy">

### Derechos de autor 

Ahora los derechos de autor de los modelos de 3D son un campo interesante. Los modelos 3D realmente tienen derechos de autor. Los derechos de autor son del creador del modelo. Sólo es posible proteger la forma, que es representada por el modelo, por una patente o una patente de diseño (EE.UU). Pero las patentes cubren sólo la creación de una pieza física para ganar dinero. Como ejemplo el [Patente del diseño del ratón de Microsoft](http://patft1.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1=D464,651.PN.&OS=PN/D464,651&RS=PN/D464,651).


</div>

De modo que tenemos que recordar al creador (titular de los derechos de autor) y cualquier clase de licencia para cada modelo/producto/archivo de un diseño. Para la licencia yo utilizaría las licencias de tipo de CC. <http://creativecommons.org/>

Claves abreviadas para licencias CC:

-   BY = Sólo atribución
-   BY-ND = Atribución - No derivativos
-   BY-NC-ND = Atribución - No comercial - No derivativos
-   BY-NC = Atribución - No comercial
-   BY-NC-SA = Atribución - No comercial - como Share
-   BY-SA = Atribución - Como Share
-   PD = Dedicado o marcado para ser de dominio público por una vía de nuestras herramientas de dominio público, o otro treabajo de dominio público; adaptaciones de trabajo en el dominio público pueden crearse y licenciarse por el creador bajo cualquier término de licencia deseado


<div class="mw-translate-fuzzy">

Añadir un enlace URL al documento de licencia completo (en caso de licencias de clientes)


</div>


<div class="mw-translate-fuzzy">

### ISO 10303 

La ISO 10303 (STEP) es muy importante en este campo. Es la única definición de estructuras de producto que conozco que está bien estandarizada y ampliamente discutida y reconocida. <img alt="" src=images/Product_structure_modeling_Process-Data_diagram.gif  style="width:500px;">


</div>


<div class="mw-translate-fuzzy">

Aquí algunos vínculos con información:

-   [ISO 10303 en Wikipedia](http://es.wikipedia.org/wiki/ISO_10303)
-   [WikiStep.org](http://www.wikistep.org/index.php/Main_Page) con un montón de información básica pero principalmente centrada en STEP-NC
-   La [Estructura de producto](http://www.wikistep.org/index.php/Product_Basics) en STEP
-   Algunos [ejemplos](http://www.wikistep.org/index.php/STEP_Tutorial) sobre STEP
-   [ISO 10303-11](http://en.wikipedia.org/wiki/ISO_10303-11) sobre el lenguaje de modelado (EXPRESS)
-   [Un artículo de Wikipedia](http://en.wikipedia.org/wiki/Product_Structure_Modeling) sobre modelado de producto
-   [Visión general de la Parte 41 \-- Fundamentos de Descripción de producto y soporte](http://www.steptools.com/support/stdev_docs/express/step_irs/index.html#part41)
-   [Visión general de la Parte 44 (edición 2) \-- Configuración de la estructura de producto](http://www.steptools.com/support/stdev_docs/express/step_irs/index.html#part44)
-   [Ejemplos de pequeños archivos de AP 214](http://www.steptools.com/support/stdev_docs/express/ap214/index.html)


</div>


<div class="mw-translate-fuzzy">

### Restricciones de ensamblaje 

Una función importante en la construcción de modelos grandes y productos son las restricciones de ensamblaje, que formulan ciertas reglas sobre como se ensamblan las piezas en un producto. Las restricciones más relevantes son del tipo: Fijo, Cara a cara, Ángulo, Equidistancia y algún tipo de patrón de repetición (para producir múltiples instancias). Estas restricciones necesitan un solucionador especializado que las actualice cuando se produzcan cambios en las piezas. Este solucionador es fundamentalmente diferente al solucionador de croquis. Creo que tenemos que ir hacia un acercamiento basado en gráficos en este\...


</div>


<div class="mw-translate-fuzzy">

### Cinemáticas

Un paso más sería utilizar [ODE](http://ode.org/) para poner las restricciones de piezas y ensamblajes juntas para hacer una simulación de la cinemática de las máquinas. Eso permitiría comprobar si existen colisiones y explorar las condiciones de un sistema mecánico.


</div>


<div class="mw-translate-fuzzy">

### Control de revisiones 

Un importante punto es el control de versión y desarrollo distribuido. Con diseño multi modelo podremos dividir los diseños en piezas menores y podemos distribuir el trabajo entre un equipo. A un desarrollador de software \"distribuido\" y \"Versión\" le sonará familiar, así que por que no utilizar un [DVCS](http://en.wikipedia.org/wiki/Distributed_Version_Control_System). Una buena comparación está [aquí](http://en.wikipedia.org/wiki/Comparison_of_revision_control_software#Technical_information).


</div>


<div class="mw-translate-fuzzy">

Ya que manejamos datos grandes, y datos que no pueden diferenciarse fácilmente, estamos limitados a aquellos que utilizan el modelo de captura persistente. Cualquier sistema de almacenamiento diferente nos dará problemas con los datos (probado personalmente con archivos de Mercurial y Catia). Después de separar los comerciales y no-libres, básicamente sólo quedan [Git](http://en.wikipedia.org/wiki/Git_%28software%29) y [SVN](http://subversion.apache.org/) .


</div>


<div class="mw-translate-fuzzy">

Utilizando Git para la tarea nos deja a nosotros con dos grandes fronteras:

-   Git es muy complicado; El ramificado, el fusionado y etiquetado a lo largo de una ruta de desarrollo no lineal deja sólo el fusionado con repositorios remotos (push, pull) traerá un montón de complejidad en al asunto. Ocultarlo del usuario será un complicado.
-   Git permite manejadores de Fusión y Diferencia para ciertos tipos de archivos; Necesitamos uno para .fcstd. Este manejador tiene que examinar dos documentos de FreeCAD y mostrar y fusionar diferencias en los objetos, operaciones y parámetros. Tampoco es fácil


</div>


<div class="mw-translate-fuzzy">

Pero utilizando Git podrían abrirse un montón de posibilidades incluso podríamos soñar con un sistema PLM de primera clase\...


</div>

## Organización

Aquí están algunas tareas de desarrollo necesarias para un diseño decente de Ensamblaje/Productos:

### Infraestructura

El ensamblaje demandará algunos cambios en e sistema base y capa de infraestructura de FreeCAD.


<div class="mw-translate-fuzzy">

#### Modelos múltiples 

Los modelos múltiples estaban en mente desde el principio del diseño de FreeCAD. Por tanto tenemos una interfaz de múltiples documentos y podemos cargar ilimitados documentos. Pero necesitamos promocionar especialmente el visor 3D para manejar el mostrar más de un documento en su vista (Part-Trees).


</div>


<div class="mw-translate-fuzzy">

#### Part-Trees 

La combinación de piezas y subensamblajes es la actividad principal durante los ensamblajes. Por ello, hay que tener herramientas adecuadas para agrupar ordenadamente las piezas en una estructura de arbol. Esas herramientas hay que implementarlas. A diferencia de un DocumentObjectGroup el grupo de Ensamblaje tiene que manejar visibilidad y ubicación de sus hijos. Mejor hacerlo por apilado ViewProvider en cada otro. Eso necesita un tipo de ClaimChildren() interfaz para el ViewProviders.


</div>


<div class="mw-translate-fuzzy">

#### Interfaces unificados de Arrastrar/Soltar/Copiar/Pegar 

El interfaz debe ser adecuado para facilitar que tanto desde ViewProvider como desde los diversos entornos se tenga un control total sobre las operaciones de Arrastrar/Soltar/Copiar/Pegar y además sea operativo tanto en la vista en árbol como en la vista 3D.


</div>


<div class="mw-translate-fuzzy">

#### Recursos externos 

Manejar enlaces (de navegadores internos o externos). Significa recursos cargando sobre (potencialmente) conexiones lentas (http).


</div>

### Material

La descripción del material y sus propiedades es una parte vital de un sistema CAD/CAE. Un material tiene un montón de propiedades y nombres altamente dependientes del campo en el que se utilizan. Por ejemplo, FEM y la ingeniería mecánica tienen diferentes entornos y estándares para describir el material.

Para la descripción del material se ha creado un artículo específico: [Material](Material/es.md)

### Modelo de objetos 

Una Clase árbol para manejar conceptos necesarios. Referencias, interfaces, enlaces de documentos, vistas, compuestos, restricciones, configuraciones, y mucho más\...

## STEP check loop 

Implementing a first STEP importer for more than geometry and color to check if the object model holds for a wider usage.


<div class="mw-translate-fuzzy">

### Solucionador de restricciones de ensamblaje 

Definir un interfaz para un Solucionador de restricciones de ensamblaje, muy similar al interfaz del solucionador del Croquizador.


</div>


<div class="mw-translate-fuzzy">

### Interfaz de simulación física 

Interfaz para permitir a un software de simulación (multi)física (externo) tomar el control sobre el posicionamiento de las Piezas en el Ensamblaje. Esto podría permitir utilizar \"bullet\" o \"ODE\" para hacer los test de cinemática y DMU.


</div>


<div class="mw-translate-fuzzy">

## Próximas acciones 

-   Modelo de objetos
-   Esperar a que se libere la versión 0.12


</div>

[Category:Roadmap](Category:Roadmap.md)
