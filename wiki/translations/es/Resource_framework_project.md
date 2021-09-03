


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}

Esta es la planificación para la estructura de recursos de FreeCAD como parte del [Mapa de desarrollo](Development_roadmap/es.md).

## Propósito y principios 

Este es un proyecto de desarrollo de software que pretende implementar capacidades de [Product Data Management (PDM)](http://en.wikipedia.org/wiki/Product_Data_Management). Trata de implementar las partes y trozos necesarios.

Los pasos del desarrollo se planifican aquí y se siguen en el sistema de gestión de incidencias de Mantis para tener un historial de cambios bien definido: ![](images/Mantis_logo_button.gif )

## Resultado

-   Control de revisiones para proyectos de diseño grandes
-   Compartir trabajo con otros a través de internet/intranet(s); **Colaboración**
-   Catalogos online y offline con [standard parts](http://en.wikipedia.org/wiki/Interchangeable_parts).

## Tormenta de ideas 

### Lo que hacen los otros 

Aquí hay algunos enlaces con productos comerciales similares:

-   [PDMLink](http://www.ptc.com/product/windchill/pdmlink) de PTC - *\"\...cuando todos los interesados en un producto están accediendo a un repositorio de datos central, único y de confianza, los fabricantes tienen el poder de gestionar expertamente todos los formularios de datos de desarrollo de producto digitales \... PDMLink es la solución ideal. Basado en la Web para un sencillo acceso de diversas empresas, este probado sistema de gestión de datos de producto (PDM) soporta equipos con dispersión geográfica al tiempo que maneja procesos críticos como la gestión de cambios/configuración, y diseño detallado.\"*
-   Aras Corp. [Aras PLM Software](http://www.aras.com/) - Aparecen para ofrecer soluciones Open Source, este podría interesar que se investigara más adelante\...
-   [Catia V6](http://www.3ds.com/de/products/plm-v6/v6r2009x/#vid1)

### Casos de referencia 

*Proporcionado por Charles*

Por supuesto habrá diferentes tipos de personas utilizando este programa por razones diferentes, y quizás necesiten diferentes soluciones PDM, pero sería bueno investigar soluciones que podrían ser universales. Yo veo los siguientes métodos diferentes de desarrollo (también debe haber otros):

-   Usuarios individuales - Probablemente sea un porcentaje significativo de personas que trabajen de este modo pero el control de revisiones y las versiones siguen siendo útiles. Muchas de estas personas pueden estar trabajando en partes del mundo en las que un acceso a Internet no sea sencillo de conseguir o sea caro, así que es posible que trabajen offline durante largos periodos. Podría estar bien hacer que esos proyectos individuales sean más sencillos de replicar por otras personas si se trata de un trabajo interesante - así el diseño puede evolucionar en múltiples direcciones a la vez.

-   Pequeños grupos de gente que trabaja junta - quizá de la misma institución de educación - pero cada individuo pueda querer la libertad de explorar todos los aspectos del proyecto en lugar de asignar rígidamente una parte particular del proyecto. Encontramos que generalmente permite más opciones a ser exploradas de forma sencilla y ofrece mayor flexibilidad.

-   Proyectos de diseño de código libre más amplios - más miembros y dispersos geográficamente. La imagen de los proyectos de software de código libre - donde parece existir una tendencia general hacia los sistemas distribuidos (en realidad Python se ha [movido](http://mail.python.org/pipermail/python-dev/2009-March/087931.html) a un DVCS el mes pasado). Veo al diseño y los ingenieros ir en la misma dirección por las mismas razones. Así que creo que hay más razones para pensar sobre cómo un sistema distribuido podría funcionar en CAD - y si solucionamos esto tendremos una gran ventaja sobre las aplicaciones comerciales de CAD! Estoy convencido de que existe una solución (si nosotros no la encontramos, algún otro sistema de desarrollo de CAD lo hará!)

-   Proyectos con una jerarquía más rígida - pueden existir algunos proyectos donde los equipos prefieran esta adaptación pero sólo puedo verlo siendo popular con las empresas.

#### La Web de Blendswap 

[Blendswap](http://www.blendswap.com/) - en sus propias palabras - es *\"\...el lugar para encontrar y compartir archivos de Blender con el mundo entero. Tu creas impresionantes archivos de Blender, los compartes en el mayor repositorios de modelos 3D de código abierto creados con la impresionante suite 3D de código abierto Blender.\"*

[Blender](http://www.blender.org/) es una \'suite de creación de contenido 3D\' en código abierto muy popular.

Aunque no es una aplicación de CAD, tiene muchas similitudes para dibujar y lecciones para aprender del modo en que Blender y su comunidad ha ido haciendo cosas.

Blendswap es un ejemplo excelente de un repositorio **online**. Sus principales características de las que podemos aprender son:

-   Proporciona imágenes en miniatura detalladas en la web. Esto permite a la gente libremente navegar y encontrar contenido rápidamente.

-   Los modelos (archivos de Blender) vienen con licencias claramente detalladas (dichos detalles se pueden visualizar rápidamente de un vistazo desde la imagen en miniatura, por medio de un logo de Creative Commons).

### Posibles sistemas de control de revisiones 

Sólo hay un pequeño paso para pensar en el control de revisiones del mismo modo que se utiliza en el desarrollo de software moderno. Hay básicamente dos aproximaciones diferentes a la materia:

-   Estructurada, servidor centralizado ([Subversion](http://subversion.tigris.org/) o [CVS](http://www.nongnu.org/cvs/))
-   Estructurada, distribuida ([Mercurial](http://www.selenic.com/mercurial/wiki/), [Bazaar](http://bazaar-vcs.org/) y [Git](http://git-scm.com/))

Aunque los casos de uso demandan un sistema de control de revisiones distribuida, todos los indicados tienen un serio inconveniente. Si clonas un repositorio todas las versiones previas se replicarán en tu equipo. Lo que, en el caso de datos de CAD, puede ser una gran cantidad de Mb. En contraste a los sistemas de servidor centralizado que sólo se descarga la principal revisión y por lo tanto se transfieren relativamente pequeñas cantidades de datos.

### Licencia

En un proyecto distribuido en Internet se necesita que todo documento lleve una licencia clara. Esto es incluso más importante si piensas en catálogos. Las piezas de los catálogos son utilizadas en los proyectos (libres y no libres) y necesitan por lo tanto una licencia clara para definir claramente su utilización. Ya que existen diferentes sistemas de licencia, aquí están un conjunto de las posibles licencias para archivos de CAD:

#### Creative Commons 

Las licencias CC son muy populares para el material creativo, puedes encontrar una descripción aquí: <http://creativecommons.org>

#### ISO 16016 

fraganaut01 nos indica otro sistema de licencias para el CAD:

-   Copyright por Proveedor (sin más restricciones)
-   Referido al aviso de protección ISO16016 (sin restricciones especiales)
-   Confidencial, sólo para uso interno internal use only. Utilizado sólo con la obligación de confidenciabilidad. Referido al aviso ISO16016
-   Confidencial, sólo para uso interno. Referido al aviso ISO16016
-   Cualquier diseminación sólo con la aprobación expresa del autor

### Diseño

Todas las revisiones controladas de datos, catalogos, tutoriales, etc. tienen que tener algún tipo de representación en FreeCAD. Todo esto se puede resumir bajo el nombre **Recurso**. Tiene que existir una clase de diseño que contenga esta clase de información de recursos y distinga los diferentes casos.

### Arquitectura

Esta clase de servicio es por definición no sólo local al equipo del usuario. Es más sobre la [Nube](http://en.wikipedia.org/wiki/Cloud_computing) e implementado en diferentes servicios en diferentes servidores. Se distinguen cuatro tipos de servicio:

-   Servidores baratos - [LAMP](http://en.wikipedia.org/wiki/LAMP_(software_bundle))
-   Servidores completos (e.g. servidores Ubuntu/Debian)
-   Servidores de descarga - e.g. sf.net
-   [BitTorrent](http://en.wikipedia.org/wiki/BitTorrent_(protocol)) gestor de incidencias

Eso nos lleva al siguiente escenario:

<img alt="" src=images/ResourceFramework.png  style="width:1000px;">

## Organización

### Investigación

Antes de nada las diferentes alternativas de sistemas de control de revisiones tienen que probarse. Para tener números de como se comportan con datos de CAD.

### Diseño 

Un diseño de clase para la estructura de recursos.

## Siguientes acciones 

-   Construir repositorios de prueba en el servidor y dos equipos locales
-   Probar diferentes casos de uso



[Category:Roadmap{{\#translation:}}](Category:Roadmap.md)
