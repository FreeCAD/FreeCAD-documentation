# Part Revolve/es
---
- GuiCommand:   Name: Part_Revolve   MenuLocation: Part -> Revolve   Workbenches: Part_Workbench/es   Pieza, Completo|SeeAlso: ---


</div>

## Description


<div class="mw-translate-fuzzy">

Revoluciona los objetos seleccionados alrededor de un eje dado. Los siguientes tipos de formas están permitidos, y crean las formas de salida indicadas:


</div>


<div class="mw-translate-fuzzy">

  Forma de entrada   Forma de salida
   
  Vértice            Arista
  Arista             Cara
  Contorno           Cáscara
  Cara               Sólido
  Cáscara            Sólido compuesto


</div>


<div class="mw-translate-fuzzy">

Los sólidos o sólidos compuestos no están permitidos como formas de entrada. Los componentes perpendiculares tampoco están permitidos. Las versiones futuras comprobarán el tipo actual de forma de los objetos compuestos.


</div>


<div class="mw-translate-fuzzy">

![](images/Dialog-revolve.jpg )


</div>


<div class="mw-translate-fuzzy">

El argumento ángulo especifica lo lejos que se girará el objeto. Las coordenadas mueven el origen del eje de revolución relativamente al origen del sistema de coordenadas.


</div>


<div class="mw-translate-fuzzy">

Si seleccionas un eje definido por el usuario, los números definen la dirección del eje de revolución con respecto al sistema de coordenadas: Si la coordenada Z es 0 y las X e Y no son cero, entonces el eje estará en el plano XY. Su ángulo es tal que su tangente es el ratio de las coordenadas X e Y.


</div>

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types can also be used as shapes and to specify the axis. <small>(v0.20)</small> 
-   If the object to revolve intersects the rotation axis the operation will fail in most cases.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Revolve/es
