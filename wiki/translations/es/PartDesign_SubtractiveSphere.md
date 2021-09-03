---
- GuiCommand:/es
   Name:PartDesign SubtractiveSphere
   Name/es:PartDesign Esfera Sustractiva
   MenuLocation:Part Design → Crear una primitiva sustractiva → Esfera sustractiva
   Workbenches:[PartDesign](PartDesign_Workbench/es.md)
   Version:0.17
   SeeAlso:[Crear una Primitiva sustractiva](PartDesign_CompPrimitiveSubtractive/es.md)
---

## Descripción

Inserta una Esfera sustractiva en el Body (cuerpo) activo. Su forma es sustraída del sólido existente.

![](images/PartDesign_SubtractiveSphere_example.svg ) *A la izquierda: Body activo (A) mostrado en color gris y la Esfera sustractiva (B) mostrada en color rojo transparente. El resultado se puede apreciar a la derecha.*

## Uso

1.  Presionar el botón **<img src="images/PartDesign_SubtractiveSphere.svg" width=24px> '''Esfera Sustractiva'''** . **Nota**: La Esfera sustractiva forma parte de un icono de herramientas llamado *Crear una primitiva sustractiva*. Tras abrir FreeCAD, la Caja sustractiva es la única mostrada en la barra de herramientas. Para obtener el botón de la Esfera, pinchar en la flecha que indica hacia abajo que está al lado del icono visible y seleccionar Esfera sustractiva en el menú desplegable.
2.  Seleccionar los parámetros de la primitiva y el [Attachment](Part_Attachment.md).
3.  Aceptar **OK**.
4.  Una operación de Esfera aparece dentro del Body (cuerpo) activo.

## Opciones

Tras su creación, la Esfera puede ser editada de dos maneras:

-   Haciendo doble clic con el ratón sobre el árbol del Modelo, o pinchando con el botón derecho y seleccionando **Editar primitiva** en el menú contextual. Con ello se abre la ventana de selección de parámetros de la Primitiva.
-   Por medio del [Editor de propiedades](Property_editor/es.md).

## Propiedades

-    {{PropertyData/es|Attachment}}: Define el modo de Attachment y la separación del archivo adjunto. Ver [Part Attachment](Part_Attachment.md).

-    {{PropertyData/es|Label}}: Nombre dado al objeto Esfera. Se puede cambiar para adaptarlo a sus necesidades.

-    {{PropertyData/es|Radius}}: Radio de la Esfera.

-    {{PropertyData/es|Ángulo1}}: (Llamado parámetro *V* en los parámetros de la primitiva) Truncamiento inferior de la esfera, paralelo al corte de la sección circular (-90 grados en una esfera completa).

-    {{PropertyData/es|Ángulo2}}: (Sin nombre en los parámetros de la primitiva) Truncamiento superior de la esfera, paralelo al corte de la sección circular (90 grados en una esfera completa).

-    {{PropertyData/es|Ángulo3}}: (Llamado parámetro *U* en los parámetros de la primitiva) Ángulo de rotación del corte de la sección circular (360 grados en una esfera completa).





{{PartDesign Tools navi

}}  
