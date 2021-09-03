


<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

Der Einstellungsbildschirm des [PartDesign Arbeitsbereichs](PartDesign_Workbench/de.md) befindet sich im [Einstellungseditor](Preferences_Editor/de.md), {{MenuCommand/de|Bearbeiten → Einstellungen → Part design}}.


</div>

## Available preferences {#available_preferences}


<div class="mw-translate-fuzzy">

Es gibt zwei Reiter: Allgemein und Formansicht.


</div>


<div class="mw-translate-fuzzy">

## Allgemein


</div>


<div class="mw-translate-fuzzy">

Im Reiter *Allgemein* kannst Du folgendes angeben:

+---------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                                                                                        | Beschreibung                                                                                                                                                                                                                                                                                                                     |
+=============================================================================================+==================================================================================================================================================================================================================================================================================================================================+
|                                                                              | Wenn gekreuzt, nach einer [booleschen Bearbeitung](Part_Boolean/de.md) wird es geprüft wenn die [Darstellung der Grenze](https://en.wikipedia.org/wiki/Boundary_representation) (BRep) des Modells gültig ist . Dies wird intern durch die Funktion [ÜberprüfeGeometrie](Part_CheckGeometry/de.md) durchgeführt. |
| {{MenuCommand/de|Modell nach boolescher Bearbeitung automatisch prüfen}}                    |                                                                                                                                                                                                                                                                                                                                  |
|                                                                                          |                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                              | If checked, Das Modell wird mit der Funktion verfeinert [VerfeinernForm](Part_RefineShape/de.md) nach einer [booleschen Bearbeitung](Part_Boolean/de.md).                                                                                                                                                        |
| {{MenuCommand/de|Automatically refine model after boolean operation}}                       |                                                                                                                                                                                                                                                                                                                                  |
|                                                                                          |                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                              | Wenn gekreuzt, wird das Modell mit der Funktion [VerfeinernForm](Part_RefineShape/de.md) verfeinert, nachdem eine Skizze eines Objekts geändert wurde.                                                                                                                                                                   |
| {{MenuCommand/de|Automatische Verfeinerung des Modells nach skizzenbasierter Bearbeitung.}} |                                                                                                                                                                                                                                                                                                                                  |
|                                                                                          |                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                              | Diese Option hat derzeit keine Auswirkungen.                                                                                                                                                                                                                                                                                     |
| {{MenuCommand/de|Name des Basisobjekts hinzufügen}}                                         |                                                                                                                                                                                                                                                                                                                                  |
|                                                                                          |                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


</div>

+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                                                                    | Description                                                                                                                                                                                                            |
+=========================================================================+========================================================================================================================================================================================================================+
|                                                          | If checked, the [Boundary representation](https://en.wikipedia.org/wiki/Boundary_representation) (BRep) of the model is [validated](Part_CheckGeometry.md) after [boolean operations](Part_Boolean.md) |
| {{MenuCommand|Automatically check model after boolean operation}}       |                                                                                                                                                                                                                        |
|                                                                      |                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                          | If checked, the model is [refined](Part_RefineShape.md) after [boolean operations](Part_Boolean.md)                                                                                                    |
| {{MenuCommand|Automatically refine model after boolean operation}}      |                                                                                                                                                                                                                        |
|                                                                      |                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                          | If checked, the model is [refined](Part_RefineShape.md) after changes to source sketches of objects                                                                                                            |
| {{MenuCommand|Automatically refine model after sketch-based operation}} |                                                                                                                                                                                                                        |
|                                                                      |                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

![](images/Preferences_Part_design_Tab_General.png )


<div class="mw-translate-fuzzy">

## Formansicht


</div>


<div class="mw-translate-fuzzy">

Im Reiter *Formansicht* kannst Du folgendes angeben:

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                                                                   | Beschreibung                                                                                                                                                                                                 |
+========================================================================+==============================================================================================================================================================================================================+
|                                                         | Maximum [linear deflection](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) der tessellierten Objekte von ihrer Oberfläche                  |
| {{MenuCommand/de|Maximale Abweichung je nach Modellbegrenzungsrahmen}} |                                                                                                                                                                                                              |
|                                                                     |                                                                                                                                                                                                              |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                         | Maximum [angular deflection](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) von einem tessellierten Objektabschnitt zum nächsten Abschnitt |
| {{MenuCommand/de|Maximale Winkelablenkung}}                            |                                                                                                                                                                                                              |
|                                                                     |                                                                                                                                                                                                              |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


</div>

+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                                                                  | Description                                                                                                                                                                                                                     |
+=======================================================================+=================================================================================================================================================================================================================================+
|                                                        | Maximum [linear deflection](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) of the [tesselated](#Tesselation.md) objects from their surface            |
| {{MenuCommand|Maximum deviation depending on the model bounding box}} |                                                                                                                                                                                                                                 |
|                                                                    |                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                        | Maximum [angular deflection](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) from one [tesselated](#Tesselation.md) object section to the next section |
| {{MenuCommand|Maximum angular deflection}}                            |                                                                                                                                                                                                                                 |
|                                                                    |                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

![](images/Preferences_Part_design_Tab_Shape_view.png )

### Shape appearance {#shape_appearance}

On the *Shape appearance* tab you can specify the following:

+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                               | Description                                                                                                                                                                                                               |
+====================================+===========================================================================================================================================================================================================================+
|                     | Color for new shapes. If the option {{MenuCommand|Random}} is set, a random color is used instead.                                                                                                          |
| {{MenuCommand|Shape color}}        |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Line color for new shapes                                                                                                                                                                                                 |
| {{MenuCommand|Line color}}         |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Line thickness for new shapes                                                                                                                                                                                             |
| {{MenuCommand|Line width}}         |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Color for new [vertices](Glossary#Vertex.md)                                                                                                                                                                      |
| {{MenuCommand|Vertex color}}       |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Size for new [vertices](Glossary#Vertex.md)                                                                                                                                                                       |
| {{MenuCommand|Vertex size}}        |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Color of [bounding boxes](Property_editor#View.md) in the 3D view                                                                                                                                                 |
| {{MenuCommand|Bounding box color}} |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | If checked, the color of the interior side of faces will be the same as the exterior side. If not checked either the [backlight color](Preferences_Editor#3D_View.md), if enabled, or black will be used instead. |
| {{MenuCommand|Two-side rendering}} |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Text color for document annotations. There is currently no dialog to add annotations to documents. Annotations can only be added using the Python console with this command:                                              |
| {{MenuCommand|Text color}}         |                                                                                                                                                                                                                           |
|                                 | obj=App.ActiveDocument.addObject("App::Annotation", "Label")                                                                                                                                                            |
|                                    |                                                                                                                                                                                                                           |
|                                    | This console is shown using the menu {{MenuCommand|View → Panels → Python console}}.                                                                                                                        |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

![](images/Preferences_Part_design_Tab_Shape_appearance.png )

## Tesselation

Um ein Objekt effizient darzustellen, ist seine Oberfläche [tesselliert](https://en.wikipedia.org/wiki/Tessellation_(computer_graphics)), d.h. es wird mit einigen kleinen Abweichungen von seiner realen Oberfläche dargestellt. Dies gilt nicht nur für PartDesign Modelle, sondern auch für andere Objekte in FreeCAD.

Es gibt eine untere Grenze für die Tessellierung von 0,01%. Wenn du die zusätzliche Zeit wirklich nutzen willst, kannst du die Untergrenze noch weiter reduzieren, indem du das Menü {{MenuCommand/de|Werkzeuge → Parameter bearbeiten...}} öffnest. Dies öffnet den Parametereditor, in dem du zu {{MenuCommand/de|BaseApp → Einstellungen → Mod → Part}} navigierst.

Rechtsklick auf **Netzabweichung** und wähle im Kontextmenü **Wert ändern**. Setze den Wert auf die minimale Tesselation deiner Wahl. Bitte beachte, dass der Wert in % angegeben wird, d.h. für einen Wert von 0,005% musst du \"0,00005\" eingeben. Der kleinstmögliche Wert ist 1e-7. **Hinweis:** Im Menü Einstellungen siehst du auch dann noch 0.01%, wenn du einen niedrigeren Wert einstellst.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}} 

[Category:Preferences{{\#translation:}}](Category:Preferences.md)
