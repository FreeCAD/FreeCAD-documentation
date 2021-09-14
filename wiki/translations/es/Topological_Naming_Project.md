# Topological Naming Project/es



Esta página está dedicada a la descripción de la idea del proyecto Google Summer of Code relativa a la denominación topológica. Para el tema en sí, por favor vea [Proyecto denominación](Naming_project/es.md). La página wiki enlazada también puede servir como punto de partida para adentrarse en el problema de la denominación.

## Outline

FreeCAD es un sistema de modelado paramétrico, por lo que diferentes pasos de modelado dependen de uno o más pasos anteriores. Los cambios realizados en un objeto se propagan a través del historial de modelado a todos los objetos dependientes. Esto se logra a través de un sistema de vinculación, implementado con propiedades. Esta vinculación es muy robusta cuando se hace sobre la base de todo el objeto. Sin embargo, muchos enlaces deben ser más finos y enlazar con subpartes de un objeto. En el entorno del banco de trabajo de piezas, por ejemplo, muchos enlaces van a entidades topológicas especiales como vértices, aristas o caras. La estabilidad de esos enlaces depende de la denominación exacta de los elementos de topología después de un recálculo. Esto no está actualmente garantizado en FreeCAD, lo que puede llevar a muchos errores en los pasos de modelado dependientes después de simples cambios en un objeto base. Como la actual dirección de desarrollo de FreeCAD parece llevar a un mayor uso de estos enlaces, el problema de la denominación debe ser resuelto.

El proyecto GSoC pretende sentar las bases para resolver este problema y probar el enfoque elegido en casos de prueba. El enfoque preferido para resolver el problema se describe [aquí](https://docs.google.com/document/d/1-d2JD8RH13ar7QPh_SpX2H5eiNND4DiCPBmGwA2R9Ug/edit), con una implementación iniciada [aquí](https://github.com/ickby/FreeCAD_sf_master/tree/Naming).

## Detalles

1.  Familiarizarse con opencascade, el núcleo de modelado geométrico de FreeCAD, y comprender cómo funciona la estructura de datos de topología y cómo los algoritmos comparten, cambian y generan topología. Es preferible que el alumno ya haya trabajado con opencascade, ya que la librería es compleja y adentrarse en ella lleva su tiempo.
2.  Familiarizarse con el sistema de vinculación de FreeCAD y cómo se vincula a las entidades de topología en las estructuras de datos de opencascade. También es importante entender el uso de occ en FreeCAD, el uso de una clase de topología dedicada combinada con el uso directo de algoritmos occ fuera de esa clase. Este enfoque dual puede no ser ideal para una solución del problema de nomenclatura, por lo que se requiere una buena comprensión del mismo.
3.  Empezar a implementar una clase identificadora que almacene el historial de creación de una forma. Identificar todos los datos necesarios para hacerla única y detallar la interfaz.
4.  Integrar la clase identificadora en la estructura de datos de Topología y portar unos primeros algoritmos para utilizarla. También extender la interfaz de la clase Topology en python para permitir el uso de los identificadores para extraer subformas.
5.  Crear un conjunto de casos de prueba para mostrar la eficacia de la implementación.

## Resultado esperado 

1.  Una primera implementación dentro de FreeCAD para mostrar el algoritmo de trabajo
2.  Un conjunto de casos de prueba integrados en el sistema de pruebas disponible que muestren los principales casos del problema de nomenclatura topológica y cómo son resueltos por la implementación del prototipo

## Posibilidades futuras 

Si este proyecto se termina con éxito, una integración completa en el código fuente de FreeCAD puede ser parte de una contribución posterior o incluso de un proyecto GSoC propio

## Propiedades del proyecto 

### Habilidades

-   Lenguaje de programación C++
-   Conocimiento profundo y uso de las APIs de FreeCAD y opencascade
-   Capacidad para leer y comprender textos y artículos científicos
-   Conocimiento de modelado 3D, topología y geometría computacional es un plus

### Dificultad

Difícil

### Información adicional 

[Category:Google Summer of Code](Category:Google_Summer_of_Code.md)
