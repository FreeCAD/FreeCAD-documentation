---
- GuiCommand:
   Name: PartDesign SubtractiveEllipsoid
   Name/es: PartDesign Elipsoide Sustractivo
   MenuLocation: Part Design - Crear una primitiva sustractiva - Elipsoide sustractivo
   Workbenches: [PartDesign](PartDesign_Workbench/es.md)
   Version: 0.17
   SeeAlso: [Crear una Primitiva sustractiva](PartDesign_CompPrimitiveSubtractive/es.md)
---

# PartDesign SubtractiveEllipsoid/es


</div>

## Descripción

Inserta un Elipsoide sustractivo en el Body (cuerpo) activo. Su forma es sustraída del sólido existente.

![](images/PartDesign_SubtractiveEllipsoid_example.svg )

*A la izquierda: Body activo (A) mostrado en color gris y el Elipsoide sustractivo (B) mostrado en color rojo transparente. El resultado se puede apreciar a la derecha.*

## Uso


<div class="mw-translate-fuzzy">

1.  Presionar el botón **<img src="images/PartDesign_SubtractiveEllipsoid.svg" width=24px> '''Elipsoide Sustractivo'''** . **Nota**: El Elipsoide sustractivo forma parte de un icono de herramientas llamado *Crear una primitiva sustractiva*. Tras abrir FreeCAD, la Caja sustractiva es la única mostrada en la barra de herramientas. Para obtener el botón del Elipsoide, pinchar en la flecha que indica hacia abajo que está al lado del icono visible y seleccionar Elipsoide sustractivo en el menú desplegable.
2.  Seleccionar los parámetros de la primitiva y el [Attachment](Part_EditAttachment.md).
3.  Aceptar **OK**.
4.  Una operación de Elipsoide aparece dentro del Body(cuerpo) activo.


</div>

## Opciones

Tras su creación, el Elipsoide puede ser editado de dos maneras:

-   Haciendo doble clic con el ratón sobre el árbol del Modelo, o pinchando con el botón derecho y seleccionando **Editar primitiva** en el menú contextual. Con ello se abre la ventana de selección de parámetros de la Primitiva.
-   Por medio del [Editor de propiedades](Property_editor/es.md).

## Propiedades


<div class="mw-translate-fuzzy">

-    {{PropertyData/es|Attachment}}: Define el modo de Attachment y la separación del archivo adjunto. Ver [Part EditAttachment](Part_EditAttachment.md).

-    {{PropertyData/es|Label}}: Nombre dado al objeto Elipsoide. Se puede cambiar para adaptarlo a sus necesidades.

-    {{PropertyData/es|Radio1}}: El valor del radio a lo largo del eje vertical del elipsoide; por defecto, paralelo al eje Z.

-    {{PropertyData/es|Radio2}}: El valor del radio a lo largo de la longitud del elipsoide; por defecto, paralelo al eje X.

-    {{PropertyData/es|Radio3}}: El valor del radio a lo largo del ancho del elipsoide; por defecto, paralelo al eje Y. al valor por defecto 0, el elipsoide forma un [oblate spheroid](http://en.wikipedia.org/wiki/Oblate_spheroid).

-    {{PropertyData/es|Ángulo1}}: (Llamado parámetro *V* en los parámetros de la primitiva) Truncamiento inferior del elipsoide, paralelo al corte de la sección circular (-90 grados en un esferoide completo).

-    {{PropertyData/es|Ángulo2}}: (Sin nombre en los parámetros de la primitiva) Truncamiento superior del elipsoide, paralelo al corte de la sección circular (90 grados en un esferoide completo).

-    {{PropertyData/es|Ángulo3}}: (Llamado parámetro *U* en los parámetros de la primitiva) Ángulo de rotación del corte de la sección elíptica (360 grados en un esferoide completo).


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveEllipsoid/es
