# PartDesign Preferences/it
<div class="mw-translate-fuzzy">





</div>




## Introduction


<div class="mw-translate-fuzzy">

La finestre delle preferenze di [PartDesign](PartDesign_Workbench/it.md) si trovano nell\'[editor delle preferenze](Preferences_Editor/it.md), **Modifica → Preferenze → Part design**.


</div>

Some advanced preferences can only be changed in the [Parameter editor](Std_DlgParameter.md). See [Fine-tuning](Fine-tuning#PartDesign_Workbench.md).

This page has been updated for version 1.0.

## Available preferences 


<div class="mw-translate-fuzzy">

Sono disponibili due schede: Generale e Visualizzazione della forma.


</div>




<div class="mw-translate-fuzzy">

## Generale


</div>

<img alt="" src=images/Preferences_PartDesign_Page_General.png  style="width:400px;">

On this page you can specify the following:

+++
| Name                                                                                | Description                                                                                                                                                                                                             |
+=====================================================================================+=========================================================================================================================================================================================================================+
|                                                                      | If checked, the [Boundary representation](https://en.wikipedia.org/wiki/Boundary_representation) (BRep) of the model is [validated](Part_CheckGeometry.md) after [boolean operations](Part_Boolean.md). |
| **Automatically check model after boolean operation**                   |                                                                                                                                                                                                                         |
|                                                                                  |                                                                                                                                                                                                                         |
+++
|                                                                      | If checked, the model is [refined](Part_RefineShape.md) after [boolean operations](Part_Boolean.md).                                                                                                    |
| **Automatically refine model after boolean operation**                  |                                                                                                                                                                                                                         |
|                                                                                  |                                                                                                                                                                                                                         |
+++
|                                                                      | If checked, the model is [refined](Part_RefineShape.md) after changes to source sketches of objects.                                                                                                            |
| **Automatically refine model after sketch-based operation**             |                                                                                                                                                                                                                         |
|                                                                                  |                                                                                                                                                                                                                         |
+++
|                                                                      | If checked, Bodies can have multiple solids. <small>(v1.0)</small>                                                                                                                                               |
| **Allow multiple solids in Part Design Body by default (experimental)** |                                                                                                                                                                                                                         |
|                                                                                  |                                                                                                                                                                                                                         |
+++




<div class="mw-translate-fuzzy">

## Visualizzazione della figura 


</div>

<img alt="" src=images/Preferences_PartDesign_Page_Shape_view.png  style="width:400px;">

On this page you can specify the following:

+++
| Name                                                                  | Description                                                                                                                                                                                                                            |
+=======================================================================+========================================================================================================================================================================================================================================+
|                                                        | The maximum [linear deflection](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) of the [tessellated](#Tessellation.md) objects from their surface.            |
| **Maximum deviation depending on the model bounding box** |                                                                                                                                                                                                                                        |
|                                                                    |                                                                                                                                                                                                                                        |
+++
|                                                        | The maximum [angular deflection](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) from one [tessellated](#Tessellation.md) object section to the next section. |
| **Maximum angular deflection**                            |                                                                                                                                                                                                                                        |
|                                                                    |                                                                                                                                                                                                                                        |
+++

### Shape appearance 

<img alt="" src=images/Preferences_PartDesign_Page_Shape_appearance.png  style="width:400px;">

An explanation of the colors can be found [here](Part_ColorPerFace#Usage.md).

On this page you can specify the following:

+++
| Name                                   | Description                                                                                                                                                                                                          |
+========================================+======================================================================================================================================================================================================================+
|                         | The diffuse color for new shapes. If the option **Random** is set, a random color is used instead.                                                                                         |
| **Shape color**            |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The ambient color for new shapes. <small>(v1.0)</small>                                                                                                                                                       |
| **Ambient shape color**    |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The emissive color for new shapes. <small>(v1.0)</small>                                                                                                                                                      |
| **Emissive shape color**   |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The specular color for new shapes. <small>(v1.0)</small>                                                                                                                                                      |
| **Specular shape color**   |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The transparency for new shapes. <small>(v0.21)</small>                                                                                                                                                       |
| **Shape transparency**     |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The shininess for new shapes. <small>(v1.0)</small>                                                                                                                                                           |
| **Shape shininess**        |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The line color for new shapes.                                                                                                                                                                                       |
| **Line color**             |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The line thickness for new shapes.                                                                                                                                                                                   |
| **Line width**             |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The color for new [vertices](Glossary#Vertex.md).                                                                                                                                                            |
| **Vertex color**           |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The size for new [vertices](Glossary#Vertex.md).                                                                                                                                                             |
| **Vertex size**            |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The color of [bounding boxes](Property_editor#View.md) in the 3D view.                                                                                                                                       |
| **Bounding box color**     |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The font size of [bounding boxes](Property_editor#View.md) in the 3D view. <small>(v1.0)</small>                                                                                                      |
| **Bounding box font size** |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | If checked, the color of the interior side of faces will be the same as the exterior side. If not checked either the [backlight color](Preferences_Editor#3D_View.md), if enabled, or black is used instead. |
| **Two-side rendering**     |                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                      |
+++
|                         | The text color for new document annotations.                                                                                                                                                                         |
| **Text color**             |                                                                                                                                                                                                                      |
|                                     | Currently these annotations can only be added by using the [Python console](Python_console.md):                                                                                                              |
|                                        |                                                                                                                                                                                                                      |
|                                        | obj = App.ActiveDocument.addObject("App::Annotation", "Label")                                                                                                                                                     |
+++

## Tessellation


<div class="mw-translate-fuzzy">

Al fine di visualizzare un oggetto in modo efficiente la sua superficie viene [tessellata](https://en.wikipedia.org/wiki/Tessellation_(computer_graphics)), cioè viene visualizzato con alcune piccole deviazioni dalla sua superficie reale. Questo vale non solo per i modelli di PartDesign, ma anche per altri oggetti di FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Il limite inferiore per la tassellatura è 0,01%. Se si vuole davvero passare più tempo di attesa dell\'elaborazione del modello si può ridurre ulteriormente il limite inferiore aprendo il menu **Strumenti → Modifica parametri ...**. Questo apre l\'editor dei parametri in cui si può accedere a **BaseApp → Preferenze → Mod → Part**.


</div>


<div class="mw-translate-fuzzy">

Fare clic con il tasto destro del mouse su **Deviazione mesh** scegliere nel menu contestuale **Modifica valore**. Impostare il valore di tessellatura minima desiderata. Ricordare che il valore è in%, ovvero per un valore di 0,005% si deve inserire \"0,00005\". Il valore più piccolo possibile è 1e-7. **Nota:** Nel menu delle preferenze vedrà ancora 0,01% anche se si imposta un valore più basso.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Preferences/it
