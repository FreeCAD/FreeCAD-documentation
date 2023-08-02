---
- GuiCommand:
   Name: PartDesign AdditivePrism
   Name/es: DiseñoPiezas PrismaAditivo
   MenuLocation: DiseñoPiezas -> Crear una primitiva aditiva -> Prisma Aditivo
   Workbenches: PartDesign_Workbench/es
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveAdditive/es, PartDesign_SubtractivePrism/es
---

# PartDesign AdditivePrism/es


</div>



## Descripción

Inserta un prisma primitiva en el Cuerpo activo como primera característica, o lo fusiona con la(s) característica(s) existente(s).

<img alt="" src=images/PartDesign_AdditivePrism_example.png  style="width:200px;">



## Uso


<div class="mw-translate-fuzzy">

1.  Presionar el botón **<img src="images/PartDesign_AdditivePrism.svg" width=24px> '''Prisma aditivo'''** . **Nota**: El Prisma aditivo forma parte de un icono de herramientas llamado *Crear una primitiva aditiva*. Tras abrir Freecad, el Cubo aditivo es la única primitiva mostrada en la barra de herramientas. Para obtener el botón del Prisma, pinchar en la flecha que indica hacia abajo, que está al lado del icono visible y seleccionar Prisma aditivo en el menú desplegable.
2.  Establece los parámetros de Primitiva y [Adjunto](Part_EditAttachment/es.md).
3.  Aceptar **OK**.
4.  Una característica del Prisma aparece dentro del Cuerpo activo.


</div>



## Opciones


<div class="mw-translate-fuzzy">

Es posible crear prismas torcidos especificando ángulos con respecto al vector normal del adjunto seleccionado. {{Version/es|0.19}}


</div>

Tras su creación, el Prisma puede ser editado de dos maneras:

-   Haciendo doble clic con el ratón sobre el árbol del Modelo, o pinchando con el botón derecho y seleccionando **Editar primitiva** en el menú contextual. Con ello se abre la ventana de selección de parámetros de la Primitiva.
-   Por medio del [Editor de propiedades](Property_editor/es.md).



## Propiedades


<div class="mw-translate-fuzzy">

-    {{PropertyData/es|Adjunto}}: Define el modo de Attachment y la separación del archivo adjunto. Ver [Part EditAttachment](Part_EditAttachment.md).

-    {{PropertyData/es|Etiqueta}}: etiqueta dada al objeto Prisma. Cámbiela para adaptarla a sus necesidades.

-    {{PropertyData/es|Polígono}}: Número de lados en el corte transversal del polígono que forma el prisma.

-    {{PropertyData/es|Circunradio}}: [circumscribed radius](https://en.wikipedia.org/wiki/Circumscribed_circle) Radio de la circunferencia en la que está inscrito el corte transversal del polígono que forma el prisma.

-    {{PropertyData/es|Altura}}: Altura del prisma.

-    {{PropertyData/es|Primer Ángulo}}: Ángulo de la primera dirección. {{Version/es|0.19}}

-    {{PropertyData/es|Segundo Ángulo}}: Ángulo de la segunda dirección. {{Version/es|0.19}}


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditivePrism/es
