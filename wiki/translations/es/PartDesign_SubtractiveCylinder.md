---
- GuiCommand:/es
   Name:PartDesign SubtractiveCylinder
   Name/es:PartDesign Cilindro Sustractivo
   MenuLocation:Part Design → Crear una primitiva sustractiva → Cilindro Sustractivo
   Workbenches:[PartDesign](PartDesign_Workbench/es.md)
   Version:0.17
   SeeAlso:[Crear una Primitiva sustractiva](PartDesign_CompPrimitiveSubtractive/es.md), [Additive Cylinder](PartDesign_AdditiveCylinder.md)
---

# PartDesign SubtractiveCylinder/es

## Descripción

Inserta un Cilindro sustractivo en el Body (cuerpo) activo. Su forma es sustraída del sólido existente.

![](images/PartDesign_SubtractiveCylinder_example.svg )

*A la izquierda: Body activo (A) mostrado en color gris y el Cilindro sustractivo (B) mostrado en color rojo transparente. El resultado se puede apreciar a la derecha.*

## Uso


<div class="mw-translate-fuzzy">

1.  Presionar el botón **<img src="images/PartDesign_SubtractiveCylinder.svg" width=24px> '''Cilindro Sustractivo'''** . **Nota**: El Cilindro sustractivo forma parte de un icono de herramientas llamado *Crear una primitiva sustractiva*. Tras abrir FreeCAD, la Caja sustractiva es la única mostrada en la barra de herramientas. Para obtener el botón del Cilindro, pinchar en la flecha que indica hacia abajo que está al lado del icono visible y seleccionar Cilindro sustractivo en el menú desplegable.
2.  Seleccionar los parámetros de la primitiva y el [Attachment](Part_Attachment.md).
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

-    {{PropertyData/es|Attachment}}: Define el modo de Attachment y la separación del archivo adjunto. Ver [Part Attachment](Part_Attachment.md).

-    {{PropertyData/es|Label}}: Nombre dado al objeto Cilindro. Se puede cambiar para adaptarlo a sus necesidades.

-    {{PropertyData/es|Radio}}: El valor del radio del Cilindro.

-    {{PropertyData/es|Ángulo}}: Ángulo de rotación del corte de la sección (360 grados forma un Cilindro completo).

-    {{PropertyData/es|Altura}}: La longitud del Cilindro a lo largo de su eje.

-    {{PropertyData/es|Primer Ángulo}}: Ángulo en la primera dirección. {{Version/es|0.20}}

-    {{PropertyData/es|Segundo Ángulo}}: Ángulo en la segunda dirección. {{Version/es|0.20}}


</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveCylinder/es
