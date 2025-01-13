# PartDesign Preferences/de
## Einleitung

Die Arbeitsbereiche <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md) und <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench.md) verwenden dieselben Einstellungen. Sie sind im [Voreinstellungseditor](Preferences_Editor.md) zu finden. Im Menü **Bearbeiten → Einstellungen...** auswählen und dann **<img src="images/Preferences-part_design.svg" width=16px> Part/Part Design**. Diese Gruppe ist nur nur vorhanden, wenn einer der Arbeitsbereiche in der aktuellen FreeCAD-Sitzung geladen wurde.

Einige fortgeschrittene Einstellungen können nur im [Parameter-Editor](Std_DlgParameter/de.md) geändert werden. Siehe [Feinabstimmung](Fine-tuning/de#Arbeitsbereich_PartDesign.md).

Diese Seite wurde für Version 1.0 aktualisiert.



## Verfügbare Einstellungen 

Es gibt Drei Seiten: [Allgemein](#General/de.md), [Form-Ansicht](#Shape_view/de.md) und [Erscheinungsbild der Form](#Shape_appearance/de.md).



### Allgemein

<img alt="" src=images/Preferences_PartDesign_Page_General.png  style="width:400px;">

Auf dieser Seite kann Folgendes festgelegt werden:

+++
| Name                                                                                                | Beschreibung                                                                                                                                                                                                                              |
+=====================================================================================================+===========================================================================================================================================================================================================================================+
|                                                                                      | Wenn aktiviert, wird die [Boundary-Representation](https://en.wikipedia.org/wiki/Boundary_representation) (BREP) des Modells nach einer [booleschen Operation](Part_Boolean/de.md) [überprüft](Part_CheckGeometry/de.md). |
| **Modell automatisch nach Boolescher Operation überprüfen**                             |                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                                                                                                                                           |
+++
|                                                                                      | Wenn aktiviert, wird das Modell nach einer [booleschen Operation](Part_Boolean/de.md) [aufbereitet](Part_RefineShape/de.md).                                                                                              |
| **Modell nach Boolescher Operation automatisch aufbereiten**                            |                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                                                                                                                                           |
+++
|                                                                                      | Wenn aktiviert, wird das Modell nach Änderungen an den Skizzen, auf denen das Objekt basiert, [aufbereitet](Part_RefineShape/de.md).                                                                                              |
| **Modell nach skizzenbasierter Operation automatisch  aufbereiten**                     |                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                                                                                                                                           |
+++
|                                                                                      | Wenn aktiviert, können Körper mehrere Festkörper enthalten. {{Version/de|1.0}}                                                                                                                                              |
| **Mehrere Festkörper in einem PartDesign-Körper standardmäßig erlauben (experimental)** |                                                                                                                                                                                                                                           |
|                                                                                                  |                                                                                                                                                                                                                                           |
+++



### Form-Ansicht 

<img alt="" src=images/Preferences_PartDesign_Page_Shape_view.png  style="width:400px;">

Auf dieser Seite kann Folgendes festgelegt werden:

+++
| Name                                                                               | Beschreibung                                                                                                                                                                                                                                  |
+====================================================================================+===============================================================================================================================================================================================================================================+
|                                                                     | Die maximale [lineare Abweichung](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) der [tessellierten](#Tessellierung.md) Objekte von ihrer Oberfläche.               |
| **Setzt die maximale Abweichung abhängig von der Modell-Bounding-Box** |                                                                                                                                                                                                                                               |
|                                                                                 |                                                                                                                                                                                                                                               |
+++
|                                                                     | Die maximale [Winkelabweichung](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) von einem [tessellierten](#Tessellierung.md) Objektabschnitt zum nächsten Abschnitt. |
| **Maximale Winkelabweichung**                                          |                                                                                                                                                                                                                                               |
|                                                                                 |                                                                                                                                                                                                                                               |
+++



### Erscheinungsbild der Form 

<img alt="" src=images/Preferences_PartDesign_Page_Shape_appearance.png  style="width:400px;">

An explanation of the colors can be found [here](Part_ColorPerFace#Usage.md).

Auf dieser Seite kann Folgendes festgelegt werden:

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



## Tesselierung

Um ein Objekt effizient darzustellen, wird seine Oberfläche [tesselliert](https://en.wikipedia.org/wiki/Tessellation_(computer_graphics)), d.h. es wird mit einigen kleinen Abweichungen von seiner realen Oberfläche dargestellt. Dies gilt nicht nur für PartDesign Modelle, sondern auch für andere Objekte in FreeCAD.

Es gibt eine untere Grenze für die Tessellierung von 0,01%. Ist es OK mehr Zeit aufzuwenden, kann die Untergrenze noch weiter reduziert werden, indem der [Parametereditor](Std_DlgParameter/de.md) geöffnet wird.

Im Parametereditor wird zu **BaseApp → Preferences → Mod → Part** gewechselt und nach einem Rechtsklick auf **Netzabweichung** im Kontextmenü **Wert ändern** ausgewählt. Den Wert auf die gewünschte minimale Tessellierung festlegen. Nicht vergesen, dass der Wert in % angegeben wird, d.h. für einen Wert von 0,005% wird {{Value|0.00005}} eingeben. Der kleinstmögliche Wert ist {{Value|1e-7}}. Bitte beachten, dass Im [Voreinstellungseditor](Preferences_Editor/de.md) noch immer 0.01% angezeigt wird, auch wenn ein niedrigerer Wert eingestellt wurde.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Preferences/de
