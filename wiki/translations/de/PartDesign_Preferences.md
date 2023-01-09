# PartDesign Preferences/de
{{TOCright}}

## Einleitung

Die Arbeitsbereiche <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md) und <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench.md) verwenden dieselben Einstellungen. Sie sind im Abschnitt <img alt="" src=images/Preferences-part_design.svg  style="width:24px;"> **Part/Part Design** des [Voreinstellungseditors](Preferences_Editor.md) zu finden. Dieser Abschnitt ist nur nur vorhanden, wenn einer der Arbeitsbereiche in der aktuellen FreeCAD-Sitzung geladen wurde.

## Verfügbare Einstellungen 

Es gibt vier Reiter: Allgemein, Form-Ansicht, Erscheinungsbild der Form und Messen.

### Allgemein

Im Reiter *Allgemein* kann Folgendes eingestellt werden:

+++
| Name                                                                               | Beschreibung                                                                                                                                                                                                                              |
+====================================================================================+===========================================================================================================================================================================================================================================+
|                                                                     | Wenn aktiviert, wird die [Boundary-Representation](https://en.wikipedia.org/wiki/Boundary_representation) (BREP) des Modells nach einer [booleschen Operation](Part_Boolean/de.md) [überprüft](Part_CheckGeometry/de.md). |
| **Modell automatisch nach Boolescher Operation überprüfen**            |                                                                                                                                                                                                                                           |
|                                                                                 |                                                                                                                                                                                                                                           |
+++
|                                                                     | Wenn aktiviert, wird das Modell nach einer [booleschen Operation](Part_Boolean/de.md) [aufbereitet](Part_RefineShape/de.md).                                                                                              |
| {{MenuCommand/de|Modell nach Boolescher Operation automatisch aufbereiten}}        |                                                                                                                                                                                                                                           |
|                                                                                 |                                                                                                                                                                                                                                           |
+++
|                                                                     | Wenn aktiviert, wird das Modell nach Änderungen an den Skizzen, auf denen das Objekt basiert, [aufbereitet](Part_RefineShape/de.md).                                                                                              |
| {{MenuCommand/de|Modell nach skizzenbasierter Operation automatisch  aufbereiten}} |                                                                                                                                                                                                                                           |
|                                                                                 |                                                                                                                                                                                                                                           |
+++

![](images/Preferences_Part_design_Tab_General.png )

### Form-Ansicht 

Im Reiter *Form-Ansicht* kann Folgendes eingestellt werden:

+++
| Name                                                                               | Beschreibung                                                                                                                                                                                                 |
+====================================================================================+==============================================================================================================================================================================================================+
|                                                                     | Maximale [lineare Abweichung](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) der tessellierten Objekte von ihrer Oberfläche.               |
| **Setzt die maximale Abweichung abhängig von der Modell-Bounding-Box** |                                                                                                                                                                                                              |
|                                                                                 |                                                                                                                                                                                                              |
+++
|                                                                     | Maximale [Winkelabweichung](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) von einem tessellierten Objektabschnitt zum nächsten Abschnitt. |
| **Maximale Winkelabweichung**                                          |                                                                                                                                                                                                              |
|                                                                                 |                                                                                                                                                                                                              |
+++

![](images/Preferences_Part_design_Tab_Shape_view.png )

### Erscheinungsbild der Form 

Im Reiter *Erscheinungsbild der Form* kann Folgendes eingestellt werden:

+++
| Name                               | Description                                                                                                                                                                                                               |
+====================================+===========================================================================================================================================================================================================================+
|                     | Color for new shapes. If the option **Random** is set, a random color is used instead.                                                                                                          |
| **Shape color**        |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+++
|                     | Transparency for new shapes <small>(v1.0)</small> .                                                                                                                                                                |
| **Shape transparency** |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+++
|                     | Line color for new shapes.                                                                                                                                                                                                |
| **Line color**         |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+++
|                     | Line thickness for new shapes.                                                                                                                                                                                            |
| **Line width**         |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+++
|                     | Color for new [vertices](Glossary#Vertex.md).                                                                                                                                                                     |
| **Vertex color**       |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+++
|                     | Size for new [vertices](Glossary#Vertex.md).                                                                                                                                                                      |
| **Vertex size**        |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+++
|                     | Color of [bounding boxes](Property_editor#View.md) in the 3D view.                                                                                                                                                |
| **Bounding box color** |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+++
|                     | If checked, the color of the interior side of faces will be the same as the exterior side. If not checked either the [backlight color](Preferences_Editor#3D_View.md), if enabled, or black will be used instead. |
| **Two-side rendering** |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+++
|                     | Text color for document annotations. There is currently no dialog to add annotations to documents. Annotations can only be added using the Python console with this command:                                              |
| **Text color**         |                                                                                                                                                                                                                           |
|                                 | obj = App.ActiveDocument.addObject("App::Annotation", "Label")                                                                                                                                                          |
|                                    |                                                                                                                                                                                                                           |
|                                    | This console is shown using the menu **View → Panels → Python console**.                                                                                                                        |
+++

![](images/Preferences_Part_design_Tab_Shape_appearance.png )

### Messen

These preferences control the appearance of measurements created with the [Measure tools](Part_Workbench#Measure.md) available in the [Part Workbench](Part_Workbench.md) and [PartDesign Workbench](PartDesign_Workbench.md).

On the *Measure* tab (<small>(v1.0)</small> ) you can specify the following:

+++
| Name                                     | Description                                                          |
+==========================================+======================================================================+
|                           | Color for 3D linear dimensions.                                      |
| **3D color**                 |                                                                      |
|                                       |                                                                      |
+++
|                           | Color for delta dimensions (parallel to the global X, Y and Z axes). |
| **Delta color**              |                                                                      |
|                                       |                                                                      |
+++
|                           | Color for angular dimensions.                                        |
| **Angular color**            |                                                                      |
|                                       |                                                                      |
+++
|                           | Font size in pixels.                                                 |
| **Font size**                |                                                                      |
|                                       |                                                                      |
+++
|                           | If checked, font style bold is used.                                 |
| **Bold**                     |                                                                      |
|                                       |                                                                      |
+++
|                           | If checked, font style italic is used.                               |
| **Italic**                   |                                                                      |
|                                       |                                                                      |
+++
|                           | The font to use.                                                     |
| **Font name**                |                                                                      |
|                                       |                                                                      |
+++
|                           | Press this button to update existing measurements.                   |
| **Refresh existing measurements** |                                                                      |
|                                       |                                                                      |
+++

![](images/Preferences_Part_design_Tab_Measure.png )

## Tesselierung

Um ein Objekt effizient darzustellen, ist seine Oberfläche [tesselliert](https://en.wikipedia.org/wiki/Tessellation_(computer_graphics)), d.h. es wird mit einigen kleinen Abweichungen von seiner realen Oberfläche dargestellt. Dies gilt nicht nur für PartDesign Modelle, sondern auch für andere Objekte in FreeCAD.

Es gibt eine untere Grenze für die Tessellierung von 0,01%. Wenn du die zusätzliche Zeit wirklich nutzen willst, kannst du die Untergrenze noch weiter reduzieren, indem du das Menü {{MenuCommand/de|Werkzeuge → Parameter bearbeiten...}} öffnest. Dies öffnet den Parametereditor, in dem du zu {{MenuCommand/de|BaseApp → Einstellungen → Mod → Part}} navigierst.

Rechtsklick auf **Netzabweichung** und wähle im Kontextmenü **Wert ändern**. Setze den Wert auf die minimale Tesselation deiner Wahl. Bitte beachte, dass der Wert in % angegeben wird, d.h. für einen Wert von 0,005% musst du \"0,00005\" eingeben. Der kleinstmögliche Wert ist 1e-7. **Hinweis:** Im Menü Einstellungen siehst du auch dann noch 0.01%, wenn du einen niedrigeren Wert einstellst.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Preferences/de
