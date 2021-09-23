# Sketcher requirement for a sketch/es



{{TutorialInfo/es
|Topic=Croquis
|Level=Principiante
|Author=[Maker](User:Maker.md)
|Time=
|FCVersion=
}}

## Requisito mínimo para un croquis 

La creación de un cuerpo en el espacio de trabajo DiseñoPieza ya es posible y *sólo* con la ayuda de una curva cerrada (perfil). La determinación completa de todas sus dimensiones y propiedades (*totalmente restringida*) aún no es necesaria.

Que una curva cerrada está presente, no es evidente y no es reconocible. Cuando se conecta un arco circular a una línea recta, por ejemplo, los dos puntos finales se crean sólo uno sobre el otro. Debe utilizar el <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [Coincidente](Sketcher_ConstrainCoincident/es.md) para hacer un solo punto que realmente conecte la línea y el arco.

![](images/Skizze2a.png )


*Un boceto sencillo. 
Izquierda: Curva sólo en cuatro lugares (rojo, restricciones automáticas al dibujar con <img src=images/_Sketcher_CreatePolyline.svg style="width:32px"> [Polilínea](Sketcher_CreatePolyline/es.md)) cerrada. 
Medio: Advertencia - ... cara rota (curva rota). 
Derecha: Curva cerrada en los cuatro lugares restantes (verde)*

Sin embargo, el trabajo paramétrico consistente significa que el croquis está completamente determinado.

## Definir un croquis por completo 

Incluso un croquis relativamente sencillo puede contener docenas de indeterminaciones (indicadas en la vista combinada como un número de \"grados de libertad\"). Eliminarlas juntas al final es una tarea relativamente confusa.

![](images/Skizze4a.png )


*Un croquis sencillo; completamente determinado por 25 restricciones, de las cuales sólo 5 son restricciones de dimensión.*

Este trabajo es más claro y sencillo si se eliminan inmediatamente las \"libertades\" de cada elemento geométrico añadido, es decir, las \"dimensiones\" (es decir, los valores de las dimensiones y las colocaciones). La integridad provisional se alcanza si todas las líneas se muestran en verde.

Si se espera hasta el final del dibujo para determinarlo, se encuentran las \"libertades\" restantes tocando los puntos y las líneas con el puntero del ratón y determinando dónde no están fijados todavía. Cuando se completa, todo el dibujo se muestra en verde.

Si crea accidentalmente una \"sobremodulación\", aparece una advertencia en la vista combinada que le pide que deshaga las acciones correspondientes (restricciones).


{{Sketcher Tools navi

}}  
