---
- GuiCommand:
   Name: PartDesign AdditiveCone
   Name/es: DiseñoPiezas ConoAditivo
   MenuLocation: DiseñoPiezas -> Crear una primitiva aditiva -> Cono Aditivo
   Workbenches: PartDesign_Workbench/es
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveAdditive/es, PartDesign_SubtractiveCone/es
---

# PartDesign AdditiveCone/es


</div>

## Descripción

Inserta un cono primitivo en el Cuerpo activo como primera característica, o lo fusiona con la(s) característica(s) existente(s).

<img alt="" src=images/PartDesign_AdditiveCone_example.png  style="width:200px;">

## Uso


<div class="mw-translate-fuzzy">

1.  Presionar el botón **<img src="images/PartDesign_AdditiveCone.svg" width=24px> '''Cono aditivo'''** . **Nota**: El Cono aditivo forma parte de un icono de herramientas llamado *Crear una primitiva aditiva*. Tras abrir Freecad, el Cubo aditivo es la única primitiva mostrada en la barra de herramientas. Para obtener el botón del Cono, pinchar en la flecha que indica hacia abajo, que está al lado del icono visible y seleccionar Cono aditivo en el menú desplegable.
2.  Seleccionar los parámetros de la primitiva (para un cono completo, poner 0 como el valor de uno de sus radios) y [Attachment](Part_EditAttachment.md).
3.  Aceptar **OK**.
4.  Una operación de Cono aparece dentro del Body (cuerpo) activo.


</div>

## Opciones

Tras su creación, el Cono puede ser editado de dos maneras:

-   Haciendo doble clic con el ratón sobre el árbol del Modelo, o pinchando con el botón derecho y seleccionando **Editar primitiva** en el menú contextual. Con ello se abre la ventana de selección de parámetros de la Primitiva.
-   Por medio del [Editor de propiedades](Property_editor/es.md).

## Propiedades


<div class="mw-translate-fuzzy">

-    {{PropertyData/es|Attachment}}: Define el modo de Attachment y la separación del archivo adjunto. Ver [Part EditAttachment](Part_EditAttachment.md).

-    {{PropertyData/es|Label}}: Nombre dado al objeto Cono. Se puede cambiar para adaptarlo a sus necesidades.

-    {{PropertyData/es|Radio1}}: El valor del radio de la base del cono.

-    {{PropertyData/es|Radio2}}: El valor del radio superior del cono. Un valor diferente de 0 crea un cono truncado.

-    {{PropertyData/es|Altura}}: La altura del cono a lo largo de su eje.

-    {{PropertyData/es|Ángulo}}: Ángulo de rotación del corte de la sección (360 grados forma un cono completo).


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveCone/es
