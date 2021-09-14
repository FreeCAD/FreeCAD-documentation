# Units project/es




{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}

Este proyecto trata de la implementación de un sistema de unidades decente en FreeCAD. Sigue las reglas de la metodología \[<http://en.wikipedia.org/wiki/GTD#GTD_methodology>\| Getting things done\]. Los proyectos se recogen en el [Mapa de desarrollo](Development_roadmap/es.md).

## Propósito y principios 

Este es un proyecto de desarrollo de software cuya intención es implementar un entorno de sistema de unidades en FreeCAD.

Los pasos del desarrollo se planifican aquí (Siguientes acciones) y se siguen en el sistema de gestión de incidencias para obtener un registro de cambios bien definido: [Gestor de incidencias](http://apps.sourceforge.net/mantisbt/free-cad/my_view_page.php)

## Resultado

Permitirá a FreeCAD manejar amplios sistemas de medición, como el sistema americano, y componentes de unidades complejos [SI](http://en.wikipedia.org/wiki/International_System_of_Units).

También manejar los formatos de importación y exportación que sean capaces de transportar unidades (como STEP).

Y permitir el escalado basado en la asumpción de unidades (mm-\>m, m-\>in).

## Tormenta de ideas 

Se ha discutido mucho aquí: <http://forum.freecadweb.org/viewtopic.php?f=10&t=1616>

Y mucha de la información que encontrarás en la página de [Unidades](Units/es.md).

## Organización

### Promoción del analizador de unidades 

Promocionar el analizador para manejar y generar firmas como se comenta en la página [Unidades](Units/es.md).

### Propiedades

Cambiar las propiedades por ejemplo de PropertyLength a PropertyUntit con una firma de unidades.

Eventualmente un editor de propiedades para el PropertyUntit.

### Entornos

-   Promocionar entornos para utilizar las Unidades. Debería empezar con el Croquizador y el Diseño de Piezas y avanzar desde ahí\...
-   Documentar el proceso de actualización para que otras personas puedan hacer lo mismo con otros entornos \--[Yorikvanhavre](User:Yorikvanhavre.md) 13:13, 28 November 2011 (UTC)

## Siguientes acciones 

-   Actualizar el analizador de unidades (jriegel)



[Category:Roadmap](Category:Roadmap.md)
