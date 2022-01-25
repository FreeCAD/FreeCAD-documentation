# FreeCAD development model project/es
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

Esta página trata de la transición del código de FreeCAD en un repositorio en GIT y un modelo de desarrollo más competente. Sigue las reglas de la metodología \[<http://en.wikipedia.org/wiki/GTD#GTD_methodology>\| Getting things done\]. Los proyectos se recogen en el [Mapa de desarrollo](Development_roadmap/es.md).

## Propósito y principios 

Este proyecto intenta definir un nuevo modelo de desarrollo y dirección para FreeCAD. Llegamos a un punto en el que un repositorio SVN es dificil de dirigir. Trabajar con parches es un fastidio y complicado para la gente que está dispuesta a contribuir con el código. Ofrecer a todo el mundo acceso al SVN es peligroso. La gente puede de forma no intencionada romper algo en el sistema base o forzar decisiones apetecibles.


<div class="mw-translate-fuzzy">

De modo que mirando el proceso de desarrollo de Linux, que es de momento demasiado grande para nosotros, que utiliza Git como sistema de control de versiones distribuidas (DVCS), listas de correo y subgestores (lugartenientes).


</div>

## Resultado

## Tormenta de ideas 

### Git

-   Utilizar Git como nuevo sistema de control de versiones
-   Mantener SVN (al menos de momento)
    -   utilizarlo como algún tipo de repositorio de versiones para mantener los flujos de trabajo de los PPA y el excelente número de revisiones
    -   restringir la escritura en SVN a Werner, Yorik y Jurgen (El árbol oficial)
    -   Todas las demás cosas, como el desarrollo, las ramificaciones, experimentos irán en Git!
    -   **Opción:** cambiar por completo a Git
        -   debería dar algunos efectos colaterales en la numeración de versiones y la construcción de los PPA\....
-   Dar derechos de escritura (push) a todos los que estén interesados

### Listas de correo de desarrollo 

El foro tiene sus limitaciones, podríamos utilizar una o más listas de correo para manejar las ramificaciones y el arrancar propuestas. Eso tiene ventajas:

-   Puede funcionar off-line
-   utilizar búsquedas más potentes en el cliente de mail
-   sin restricción de adjuntos y tamaños

### Aclarar responsabilidades 

Seremos pronto más y más desarrolladores y los usuarios tendrán peticiones de características conflictivas. Necesitamos tener una estructura y responsabilidades para filtrar y decidir dichas peticiones y el código entrante.

#### Se han ofrecido 

Adrian Przekwas:
Publicidad - G+, Youtube,
Tutoriales - [http://freecad-tutorial.blogspot.com](http://freecad-tutorial.blogspot.com)
Traducción (no es seguro) - Polaco (Wiki, Crowdin)

Yorik van Havre:
Software: arch module, draft module, artwork
Documentación: general wiki organization and design
Traducción: francés, alemán, portugués brasileño
Publicidad: artículos en [http://yorik.uncreated.net/guestblog.php](http://yorik.uncreated.net/guestblog.php), G+, facebook

## Organización

Las reglas decididas y la información va al documento [Modelo de desarrollo de FreeCAD](FreeCAD_development_model/es.md).

## Siguientes acciones



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > FreeCAD development model project/es
