# UTF Project/es
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

Este es el plan del proyecto del [modelo de desarrollo](Development_roadmap/es.md) de FreeCAD.

## Propósito y proncipios 

Mejorar las capacidades de utilizar múltiples idiomas en FreeCAD mediante la implementación de soporte de carácteres UTF con la interfaz de Coin3D.

A pesar de que Coin3D se ha movido ahora a un plataforma de desarrollo más abierta, sigue siendo bastante difícil contribuir al proyecto.

(mrlukeparry) He recibido una respuesta sobre contribuir y de momento parece apropiado mantener esto con el proyecto de FreeCAD y podría significar que permitiéramos a los usuarios probar versiones en desarrollo de Coin3D. Podría tratar de conseguirlo para la versión 0.14 considerando que es de alta prioridad para incrementar la accesibilidad de FreeCAD a los usuarios de lengua no inglesa.

## Organización

-   Proporcionar una funcionalidad básica de manipulación de cadenas de texto UTF que sea independiente de las principales bibliotecas excepto STL.

-   Implementar los campos de Coin3D y nodos de texto 3D para la manejar el almacenamiento de los nuevos datos UTF.

-   Migrar módulos para utilizar los nuevos nodos de texto.

-   Evaluación rigurosa

## Siguientes acciones 

-   Implementar la clase de manipulación de cadenas de texto UTF **(En proceso)**

-   Manejo de fuentes y signos.

-   Implementar campos de texto y nodos de Coin3D para utilizar en el proyecto

-   Migrar módulos con SoText2 y SoText3 para utilizar nuevos módulos



[Category:Roadmap](Category:Roadmap.md)

---
[documentation index](../README.md) > [Roadmap](Category:Roadmap.md) > UTF Project/es
