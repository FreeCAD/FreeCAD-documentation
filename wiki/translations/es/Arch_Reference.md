---
- GuiCommand:
   Name:Arch Reference
   Name/es:Arquitectura Referencia
   MenuLocation:Arquitectura → Referencia
   Workbenches:[Arquitectura](Arch_Workbench/es.md)
   SeeAlso:[Arquitectura EdificioPieza](Arch_BuildingPart/es.md)
---

# Arch Reference/es


</div>

## Descripción

<img alt="" src=images/Arch_reference_screenshot.png  style="width:800px;">


<div class="mw-translate-fuzzy">

La herramienta Referencia permite colocar un objeto en el documento actual que copia su forma y colores de un objeto basado en [Part](Part_Workbench.md) (incluyendo [Arch BuildingPart](Arch_BuildingPart.md)) almacenado en otro archivo de FreeCAD. Si ese archivo de FreeCAD cambia, el objeto de referencia se marca para ser recargado.


</div>

## Utilización

1.  Pulse el botón **<img src="images/Arch_Reference.svg" width=16px> '''Arquitectura Referencia'''** botón,
2.  Pulsa el botón \"Elegir archivo\...\" y selecciona un archivo existente de FreeCAD,
3.  Selecciona uno de los objetos basados en la Parte incluidos en la lista desplegable,
4.  Pulsa **OK**.

## Opciones

-   El objeto de referencia puede ser movido y rotado, la posición actual se mantendrá después de recargar el objeto.
-   Si el objeto original se mueve en el archivo contenedor, este movimiento se reflejará en el objeto de referencia.
-   Haciendo clic con el botón derecho en un objeto de referencia en la vista de árbol, tiene las opciones de recargar el objeto original o abrir el archivo que lo contiene.
-   Para referenciar varios objetos a la vez, colóquelos dentro de una [Arquitectura EdificioPieza](Arch_BuildingPart/es.md).
-   Al desactivar la propiedad de la vista **Actualizar colores** de la Referencia, ya no se recargarán los colores originales, por lo que puede cambiarlos con seguridad.

## Propiedades

-    **Archivo**: El archivo base sobre el que se construye este componente

-    **Pieza**: La pieza a utilizar del archivo base

-    **Actualizar Colores**: Si es verdadero, los colores del archivo vinculado se mantendrán actualizados

## Guión

La herramienta Referencia puede utilizarse en [macros](macros/es.md) y desde la consola de python utilizando la siguiente función: 
```python
makeReference ([file_path,object_name])
```

crea un objeto Referencia a partir del objeto dado en el archivo dado.

Ejemplo: 
```python
import Arch
Arch.makeReference("/path/to/some/file.FSCtd","myPart")
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Reference/es
