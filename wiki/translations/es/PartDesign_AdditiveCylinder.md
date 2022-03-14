---
- GuiCommand:/es
   Name:PartDesign AdditiveCylinder
   Name/es:DiseñoPiezas CilindroAditivo
   MenuLocation:DiseñoPiezas → Crear una primitiva aditiva → Cilindro Aditivo
   Workbenches:[DiseñoPiezas](PartDesign_Workbench/es.md)
   Version:0.17
   SeeAlso:[Crear una primitiva aditiva](PartDesign_CompPrimitiveAdditive/es.md), [Cilindro sustractivo](PartDesign_SubtractiveCylinder/es.md)
---

# PartDesign AdditiveCylinder/es

## Descripción

Inserta un Cilindro primitivo en el Cuerpo activo como primera característica, o lo fusiona con la(s) característica(s) existente(s).

<img alt="" src=images/PartDesign_AdditiveCylinder_example.png  style="width:200px;">

## Uso


<div class="mw-translate-fuzzy">

1.  Presionar el botón **<img src="images/PartDesign_AdditiveCylinder.svg" width=24px> '''Cilindro aditivo'''** . **Nota**: El Cilindro aditivo forma parte de un icono de herramientas llamado *Crear una primitiva aditiva*. Tras abrir Freecad, el Cubo aditivo es la única primitiva mostrada en la barra de herramientas. Para obtener el botón del Cilindro, pinchar en la flecha que indica hacia abajo, que está al lado del icono visible y seleccionar Cilindro aditivo en el menú desplegable.
2.  Seleccionar los parámetros de la primitiva y [Attachment](Part_EditAttachment.md).
3.  Aceptar **OK**.
4.  Una operación de Cilindro aparece dentro del Body (cuerpo) activo.


</div>

## Opciones

Es posible crear prismas torcidos especificando ángulos con respecto al vector normal del adjunto seleccionado. {{Version/es|0.20}}

Tras su creación, el Cilindro puede ser editado de dos maneras:

-   Haciendo doble clic con el ratón sobre el árbol del Modelo, o pinchando con el botón derecho y seleccionando **Editar primitiva** en el menú contextual. Con ello se abre la ventana de selección de parámetros de la Primitiva.
-   Por medio del [Editor de propiedades](Property_editor/es.md).

## Propiedades


<div class="mw-translate-fuzzy">

-    {{PropertyData/es|Attachment}}: Define el modo de Attachment y la separación del archivo adjunto. Ver [Part EditAttachment](Part_EditAttachment.md).

-    {{PropertyData/es|Label}}: Nombre dado al objeto Cilindro. Se puede cambiar para adaptarlo a sus necesidades.

-    {{PropertyData/es|Radio}}: El valor del radio del Cilindro.

-    {{PropertyData/es|Ángulo}}: Ángulo de rotación del corte de la sección (360 grados forma un Cilindro completo).

-    {{PropertyData/es|Altura}}: La longitud del Cilindro a lo largo de su eje.

-    {{PropertyData/es|Primer Ángulo}}: Ángulo en la primera dirección. {{Version/es|0.20}}

-    {{PropertyData/es|Segundo Ángulo}}: Ángulo en la segunda dirección. {{Version/es|0.20}}


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveCylinder/es
