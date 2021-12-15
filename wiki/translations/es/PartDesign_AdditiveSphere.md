---
- GuiCommand:/es
   Name:PartDesign AdditiveSphere
   Name/es:DiseñoPiezas EsferaAditiva
   MenuLocation:Part Design → Crear una primitiva aditiva → Esfera aditiva
   Workbenches:[DiseñoPiezas](PartDesign_Workbench/es.md)
   Version:0.17
   SeeAlso:[DiseñoPiezas CompPrimitivaAditiva](PartDesign_CompPrimitiveAdditive/es.md)
---

# PartDesign AdditiveSphere/es

## Descripción

Inserta una Esfera primitiva en el Cuerpo activo como primera característica, o lo fusiona con la(s) característica(s) existente(s).

<img alt="" src=images/PartDesign_AdditiveSphere_example.png  style="width:200px;">

## Uso


<div class="mw-translate-fuzzy">

1.  Presionar el botón **<img src="images/PartDesign_AdditiveSphere.svg" width=24px> '''Esfera aditiva'''** . **Nota**: La Esfera aditiva forma parte de un icono de herramientas llamado *Crear una primitiva aditiva*. Tras abrir Freecad, el Cubo aditivo es la única primitiva mostrada en la barra de herramientas. Para obtener el botón de la Esfera, pinchar en la flecha que indica hacia abajo, que está al lado del icono visible y seleccionar Esfera aditiva en el menú desplegable.
2.  Seleccionar los parámetros de la primitiva y [Attachment](Part_EditAttachment.md).
3.  Aceptar **OK**.
4.  Una operación de Esfera aparece dentro del Body (cuerpo) activo.


</div>

## Opciones

Tras su creación, la Esfera puede ser editada de dos maneras:

-   Haciendo doble clic con el ratón sobre el árbol del Modelo, o pinchando con el botón derecho y seleccionando **Editar primitiva** en el menú contextual. Con ello se abre la ventana de selección de parámetros de la Primitiva.
-   Por medio del [Editor de propiedades](Property_editor/es.md).

## Propiedades


<div class="mw-translate-fuzzy">

-    {{PropertyData/es|Attachment}}: Define el modo de Attachment y la separación del archivo adjunto. Ver [Part EditAttachment](Part_EditAttachment.md).

-    {{PropertyData/es|Label}}: Nombre dado al objeto Esfera. Se puede cambiar para adaptarlo a sus necesidades.

-    {{PropertyData/es|Radius}}: Radio de la Esfera.

-    {{PropertyData/es|Ángulo1}}: (Llamado parámetro *V* en los parámetros de la primitiva) Truncamiento inferior de la esfera, paralelo al corte de la sección circular (-90 grados en una esfera completa).

-    {{PropertyData/es|Ángulo2}}: (Sin nombre en los parámetros de la primitiva) Truncamiento superior de la esfera, paralelo al corte de la sección circular (90 grados en una esfera completa).

-    {{PropertyData/es|Ángulo3}}: (Llamado parámetro *U* en los parámetros de la primitiva) Ángulo de rotación del corte de la sección circular (360 grados en una esfera completa).


</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveSphere/es
