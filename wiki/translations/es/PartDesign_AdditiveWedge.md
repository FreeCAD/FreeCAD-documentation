---
 GuiCommand:
   Name: PartDesign AdditiveWedge
   Name/es: PartDesign Cuña aditiva
   MenuLocation: Part Design , Crear una primitiva aditiva , Cuña aditiva
   Workbenches: PartDesign_Workbench/es
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveAdditive/es, PartDesign_SubtractiveWedge
---

# PartDesign AdditiveWedge/es


</div>

## Descripción

Inserta una cuña primitiva en el Body (cuerpo) activo como primera operación, o la fusiona con la(s) operación(es) existente(s).

<img alt="" src=images/PartDesign_AdditiveWedge_example.png  style="width:200px;">

## Uso


<div class="mw-translate-fuzzy">

1.  Presionar el botón **<img src="images/PartDesign_AdditiveWedge.svg" width=24px> '''Cuña aditiva'''** . **Nota**: La Cuña aditiva forma parte de un icono de herramientas llamado *Crear una primitiva aditiva*. Tras abrir FreeCad, el icono de Crear una primitiva aditiva es el único que se muestra en la barra de herramientas. Para obtener el botón de la Cuña, pinchar en la flecha que indica hacia abajo que está al lado del icono visible y seleccionar Cuña aditiva en el menú desplegable.
2.  Seleccionar los parámetros de la primitiva y el [Attachment](Part_EditAttachment.md).
3.  Aceptar **OK**.
4.  Una operación de Cuña aparece dentro del Body (cuerpo) activo.


</div>

## Opciones

Tras su creación, la Cuña puede ser editada de dos maneras:

-   Haciendo doble clic con el ratón sobre el árbol del Modelo, o pinchando con el botón derecho y seleccionando **Editar primitiva** en el menú contextual. Con ello se abre la ventana de selección de parámetros de la Primitiva.
-   Por medio del [Editor de propiedades](Property_editor/es.md).

## Propiedades

Usando el emplazamiento por defecto, las entradas siguientes son:

-    {{PropertyData/es|X min/max}}: Posición de los puntos iniciales y finales que forman la cara frontal en el eje X

-    {{PropertyData/es|Y min/max}}: Altura de la cuña, indicando los puntos iniciales y finales, que resultarán en la altura de la cuña.

-    {{PropertyData/es|Z min/max}}: Posición de los puntos iniciales y finales que forman la cara frontal en el eje Z

-    {{PropertyData/es|X2 min/max}}: Posición de los puntos iniciales y finales que forman la cara posterior en el eje X

-    **Z2 min/max**: Posición de los puntos iniciales y finales que forman la cara posterior en el eje Z

Teniendo en cuenta que X y Z se refieren a la cara frontal (base inferior) y X2 y Z2 a la cara posterior (base superior) de la cuña en la posición en que aparece por defecto.

## Pirámides

Las cuñas pueden ser usadas para crear pirámides, seleccionando {{PropertyData/es|X2 min/max}} y {{PropertyData/es|Z2 min/max}} , tal que min = max.

Para crear una pirámide regular con un vértice en el lado superior, los valores de {{PropertyData/es|X2 min/max}} y de {{PropertyData/es|Z2 min/max}} tienen que ser la mitad de {{PropertyData/es|X max}} y {{PropertyData/es|Z max}}


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveWedge/es
