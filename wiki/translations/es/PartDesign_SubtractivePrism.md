---
- GuiCommand:/es
   Name:PartDesign SubtractivePrism
   Name/es:PartDesign Prisma Sustractivo
   MenuLocation:Part Design → Crear una primitiva sustractiva → Prisma sustractivo
   Workbenches:[PartDesign](PartDesign_Workbench/es.md)
   Version:0.17
   SeeAlso:[Crear una Primitiva sustractiva](PartDesign_CompPrimitiveSubtractive/es.md), [Additive Prism](PartDesign_AdditivePrism.md)
---


</div>

## Descripción

Inserta un Prisma sustractivo en el Body (cuerpo) activo. Su forma es sustraída del sólido existente.

![](images/PartDesign_SubtractivePrism_example.svg )

*A la izquierda: Body activo (A) mostrado en color gris y el Prisma sustractivo (B) mostrado en color rojo transparente. El resultado se puede apreciar a la derecha.*

## Uso


<div class="mw-translate-fuzzy">

1.  Presionar el botón **<img src="images/PartDesign_SubtractivePrism.svg" width=24px> '''Prisma Sustractivo'''** . **Nota**: El Prisma sustractivo forma parte de un icono de herramientas llamado *Crear una primitiva sustractiva*. Tras abrir FreeCAD, la Caja sustractiva es la única mostrada en la barra de herramientas. Para obtener el botón del Prisma, pinchar en la flecha que indica hacia abajo que está al lado del icono visible y seleccionar Prisma sustractivo en el menú desplegable.
2.  Seleccionar los parámetros de la primitiva y el [Attachment](Part_Attachment.md).
3.  Aceptar **OK**.
4.  Una operación de Prisma aparece dentro del Body(cuerpo) activo.


</div>

## Opciones

Es posible crear prismas torcidos especificando ángulos con respecto al vector normal del adjunto seleccionado. {{Version/es|0.19}}

Tras su creación, el Prisma puede ser editado de dos maneras:

-   Haciendo doble clic con el ratón sobre el árbol del Modelo, o pinchando con el botón derecho y seleccionando **Editar primitiva** en el menú contextual. Con ello se abre la ventana de selección de parámetros de la Primitiva.
-   Por medio del [Editor de propiedades](Property_editor/es.md).

## Propiedades


<div class="mw-translate-fuzzy">

-    {{PropertyData/es|Attachment}}: Define el modo de Attachment y la separación del archivo adjunto. Ver [Part Attachment](Part_Attachment.md).

-    {{PropertyData/es|Label}}: Nombre dado al objeto Prisma. Se puede cambiar para adaptarlo a sus necesidades.

-    {{PropertyData/es|Polígono}}: Número de lados en el corte transversal del polígono que forma el prisma.

-    {{PropertyData/es|Circunradio}}: [circumscribed radius](https://en.wikipedia.org/wiki/Circumscribed_circle) Radio de la circunferencia en la que está circunscrito el corte transversal del polígono que forma el prisma.

-    {{PropertyData/es|Altura}}: Altura del prisma.

-    {{PropertyData/es|Primer Ángulo}}: Ángulo de la primera dirección. {{Version/es|0.19}}

-    {{PropertyData/es|Segundo Ángulo}}: Ángulo de la segunda dirección. {{Version/es|0.19}}


</div>





{{PartDesign Tools navi

}}  
