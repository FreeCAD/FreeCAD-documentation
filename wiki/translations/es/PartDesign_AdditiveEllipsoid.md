---
- GuiCommand:/es
   Name:PartDesign AdditiveEllipsoid
   Name/es:DiseñoPiezas  ElipsoideAditivo
   MenuLocation:DiseñoPiezas → Crear una primitiva aditiva → Elipsoide Aditivo
   Workbenches:[DiseñoPiezas](PartDesign_Workbench/es.md)
   Version:0.17
   SeeAlso:[DiseñoPiezas CompPrimitivaAditiva](PartDesign_CompPrimitiveAdditive/es.md)
---

# PartDesign AdditiveEllipsoid/es


</div>

## Descripción

Inserta un Elipsoide primitiva en el Cuerpo activo como primera característica, o lo fusiona con la(s) característica(s) existente(s).

<img alt="" src=images/PartDesign_AdditiveEllipsoid_example.png  style="width:200px;">

## Uso


<div class="mw-translate-fuzzy">

1.  Presionar el botón **<img src="images/PartDesign_AdditiveEllipsoid.svg" width=24px> '''Elipsoide aditivo'''** . **Nota**: El Elipsoide aditivo forma parte de un icono de herramientas llamado *Crear una primitiva aditiva*. Tras abrir Freecad, el Cubo aditivo es la única primitiva mostrada en la barra de herramientas. Para obtener el botón del Elipsoide, pinchar en la flecha que indica hacia abajo, que está al lado del icono visible y seleccionar Elipsoide aditivo en el menú desplegable.
2.  Seleccionar los parámetros de la primitiva y [Attachment](Part_EditAttachment.md).
3.  Aceptar **OK**.
4.  Una operación de Elipsoide aparece dentro del Body (cuerpo) activo.


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

-    {{PropertyData/es|Radio3}}: El valor del radio a lo largo del ancho del elipsoide; por defecto, paralelo al eje Y. Si el valor por defecto es 0, el elipsoide forma un [oblate spheroid](http://en.wikipedia.org/wiki/Oblate_spheroid). Esto tiene la misma forma que tendría si el Radio3 fuese idéntico al Radio2.

-    {{PropertyData/es|Ángulo1}}: (Llamado parámetro *V* en los parámetros de la primitiva) Truncamiento inferior del elipsoide, paralelo al corte de la sección circular (-90 grados en un esferoide completo).

-    {{PropertyData/es|Ángulo2}}: (Sin nombre en los parámetros de la primitiva) Truncamiento superior del elipsoide, paralelo al corte de la sección circular (90 grados en un esferoide completo).

-    {{PropertyData/es|Ángulo3}}: (Llamado parámetro *U* en los parámetros de la primitiva) Ángulo de rotación del corte de la sección elíptica (360 grados en un esferoide completo).


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveEllipsoid/es
