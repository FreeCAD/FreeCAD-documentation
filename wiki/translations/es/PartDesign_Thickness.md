---
 GuiCommand:
   Name: PartDesign Thickness
   Name/es: PartDesign Espesor
   MenuLocation: Part Design , Apply a dress up feature , Espesor
   Workbenches: PartDesign_Workbench/es
   Version: 0.17
   SeeAlso: Part_Thickness/es
---

# PartDesign Thickness/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

La herramienta **Espesor** trabaja sobre un cuerpo sólido y lo transforma en un objeto hueco con una pared de un grosor determinado, con al menos una cara abierta, dando a cada una de sus caras restantes un espesor uniforme. Con algunos sólidos permite un ahorro significativo de trabajo, evitando hacer extrusiones y vaciados innecesarios.


</div>

<img alt="" src=images/PartDesign_Thickness_example.svg  style="width:400px;"> 
*Base solid (A) →  Solid with selected face to be opened (B) →  Resulting hollow object (C)*



## Uso

### Add a thickness 


<div class="mw-translate-fuzzy">

1.  Seleccionar una o más caras del Body (cuerpo) activo.
2.  Presionar el botón **<img src="images/PartDesign_Thickness.svg" width=24px> '''Espesor'''**.
3.  Definir los **Parámetros de espesor** (Ver [Opciones](#Options/es.md)).
4.  Para añadir más caras a abrir, presionar el botón **Añadir cara** y seleccionarla(s) en [3D view](3D_view/es.md).
5.  Para eliminar una cara seleccionada previamente, presionar el botón **Eliminar cara** y seleccionar una nueva cara en la vista 3D, o pulsar con el botón derecho en la etiqueta del nombre de la cara de la lista y seleccionar *Remove*.
6.  Confirmar con **OK**.


</div>


:   *Remember*:
    -   Since there must be at least one face for the feature, the last remaining face in the list cannot be removed.

### Edit a thickness 

1.  Do one of the following:
    -   Double-click the Thickness object in the [Tree view](Tree_view.md)
    -   Right-click the Thickness object in the [Tree view](Tree_view.md) and select **Edit Thickness** from the context menu.
2.  The **Thickness parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.



## Opciones


<div class="mw-translate-fuzzy">

-   **Espesor**: Grosor de la pared del objeto resultante. Introducir el valor deseado en números positivos.
-   **Modo**
    -   *Piel*: Seleccionando esta opción se obtiene un objeto como un jarrón, con un vaciado desde la cara superior, pero conservando la cara inferior.
    -   *Tubo*: Seleccionando esta opción se obtiene un objeto como un tubo, sin las caras superior ni inferior. En este caso es conveniente seleccionar las caras a ser eliminadas antes de iniciar la herramienta. Se pueden utilizar los botones de vistas predeterminadas o usar las teclas numéricas como ayuda a la selección de caras.
    -   *Recto Verso*:
-   **Tipo de unión**
    -   *Arco*: Añade el espesor hacia el exterior de las paredes, quitando los bordes exteriores y creando un redondeo de las aristas de un radio igual al espesor definido.
    -   *Intersección*: Cuando el espesor se aplica hacia afuera, crea los bordes rectos, sin redondear.
-   **Hacer el grosor hacia el interior**: Al seleccionar esta casilla, el espesor es aplicado hacia el interior de las caras, con los bordes rectos, sin redondear.


</div>

## Notes


<div class="mw-translate-fuzzy">

-   Debe seleccionarse al menos una cara para ser abierta.
-   Si el espesor va hacia adentro, el valor debe de ser menor que la altura más pequeña del Body (cuerpo).
-   La operación podría fallar con formas complejas. En este contexto, la superficie, por ejemplo, de un cono, tiene que ser considerada como compleja.
    -   Las herramientas [Tubo aditivo](PartDesign_AdditivePipe/es.md) (barrido) o [Additive Loft](PartDesign_AdditiveLoft/es.md) (interpolación de secciones) podrían trabajar mejor para crear formas complejas.


</div>

## Properties

See also: [Property editor](Property_editor.md).

A PartDesign Thickness object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

-    **Base|LinkSub**: Sub-link to the parent feature\'s list of selected edges and faces.

-    **Support Transform|Bool**: Include the base additive/subtractive shape when used in pattern features. If disabled, only the dressed part of the shape is used for patterning. Default: `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**: Link to the parent feature.

-    **_ Body|LinkHidden|hidden**: Link to the parent body.


{{Properties_Title|Part Design}}

-    **Refine|Bool**: Refine shape (clean up redundant edges) after adding/subtracting. The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).


{{Properties_Title|Thickness}}

-    **Value|Length**: Thickness value. Default: {{value|1 mm}}.

-    **Mode|Enumeration**: Mode. {{value|Skin}} (default), {{value|Pipe}} or {{Value|Recto verso}}. Only {{value|Skin}} is implemented.

-    **Join|Enumeration**: Join type. {{value|Arc}} (default) or {{Value|Intersection}}.

-    **Reversed|Bool**: Apply the thickness towards the solids interior. Default: `False`.

-    **Intersection|Bool**: Enable intersection-handling. Default: `False`.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Thickness/es
