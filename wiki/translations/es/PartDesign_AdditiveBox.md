---
- GuiCommand:/es
   Name:PartDesign AdditiveBox
   Name/es:DiseñoPiezas CuboAditivo
   MenuLocation:DiseñoPiezas → Crear una primitiva aditiva → Cubo Aditivo
   Workbenches:[DiseñoPiezas](PartDesign_Workbench/es.md)
   Version:0.17
   SeeAlso:[DiseñoPiezas Primitiva aditiva](PartDesign_CompPrimitiveAdditive/es.md)
---

## Descripción

Inserta un cubo primitivo en el Cuerpo activo como primera característica, o lo fusiona con la(s) característica(s) existente(s).

<img alt="" src=images/PartDesign_AdditiveBox_example.png  style="width:200px;">

## Uso

1.  Presionar el botón **<img src="images/PartDesign_AdditiveBox.svg" width=24px> '''Cubo aditivo'''** . **Nota**: El Cubo aditivo forma parte de un icono de herramientas llamado *Crear una primitiva aditiva*. Tras abrir Freecad, el Cubo aditivo es la única primitiva mostrada en la barra de herramientas. Si se muestra una primitiva diferente, pinchar en la flecha que indica hacia abajo, que está al lado del icono visible y seleccionar Cubo aditivo en el menú desplegable.
2.  Seleccionar los parámetros de la primitiva y [Attachment](Part_Attachment.md).
3.  Aceptar **OK**.
4.  Una operación de Cubo aparece dentro del Body (cuerpo) activo.

## Opciones

Tras su creación, el Cubo puede ser editado de dos maneras:

-   Haciendo doble clic con el ratón sobre el árbol del Modelo, o pinchando con el botón derecho y seleccionando **Editar primitiva** en el menú contextual. Con ello se abre la ventana de selección de parámetros de la Primitiva.
-   Por medio del [Editor de propiedades](Property_editor/es.md).

## Propiedades

-    {{PropertyData/es|Attachment}}: Define el modo de Attachment y la separación del archivo adjunto. Ver [Part Attachment](Part_Attachment.md).

-    {{PropertyData/es|Label}}: Nombre dado al objeto Cubo. Se puede cambiar para adaptarlo a sus necesidades.

-    {{PropertyData/es|Longitud}}: Dimensiones del Cubo en la dirección del eje X.

-    {{PropertyData/es|Anchura}}: Dimensiones del Cubo en la dirección del eje Y.

-    {{PropertyData/es|Altura}}: Dimensiones del Cubo en la dirección del eje Z.





{{PartDesign Tools navi

}}  