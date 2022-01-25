---
- GuiCommand:/es
   Name:Part Tube
   Name/es:Part Tubo
   MenuLocation:Pieza → Primitivas → Crear un tubo
   Workbenches:[Part](Part_Workbench/es.md)
   Version:0.19
   Seealso:[Part CreatePrimitives](Part_CreatePrimitives/es.md)
---

# Part Tube/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

El comando Tubo inserta un tubo en el documento activo. El tubo es geométricamente tratado como un corte de un cilindro más pequeño dentro de otro mayor. Por defecto, el comando insertará un tubo de 10 mm de altura con un radio exterior de 5 mm y un radio interior de 2 mm. Estos parámetros pueden ser modificados tras ser introducido el objeto.


</div>

![Screenshot of a Tube](images/Part_Tube-screenshot.png )

## Uso


<div class="mw-translate-fuzzy">

Se puede crear un tubo:

-   presionando el botón **<img src="images/Part_Tube.svg" width=16px> '''Crea un Tubo'''** en la barra de herramientas; o bien:
-   usando el menú **Pieza → Primitivas → Crear un tubo**


</div>


<div class="mw-translate-fuzzy">

Para editar el tubo:

-   con cualquiera de las siguientes maneras:
    -   seleccionándolo en el árbol y pinchando encima con doble clic
    -   editando los parámetros en la caja de diálogo que aparece
-   o usando el [Editor de propiedades](property_editor/es.md) modificando sus propiedades para editar sus parámetros


</div>

## Propiedades


<div class="mw-translate-fuzzy">

-   Por medio del [Editor de propiedades](Property_editor/es.md):
    -   **Height o Altura:** Selecciona la altura (por defecto es 10 mm).
    -   **Inner radius o Radio interior:** Selecciona el radio interior (por defecto es 2 mm).
    -   **Outer radius o Radio exterior:** Selecciona el radio exterior (por defecto es 5 mm).
    -   **Placement o Localización:** Especifica la orientación y la posición de la caja en el espacio 3D. Ver [ Placement](Placement/es.md). El punto de referencia es la esquina inferior izquierda frontal de la caja.
    -   **Label o Etiqueta:** Es el nombre dado a la operación. Este nombre puede ser cambiado si es conveniente.


</div>

## Scripting

A Part Tube can be created using the following function:


```python
tube = FreeCAD.ActiveDocument.addObject("Part::Tube", "myTube")
```

-   Where {{Incode|"myTube"}} is the name for the object.
-   The function returns the newly created object.


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Tube/es
