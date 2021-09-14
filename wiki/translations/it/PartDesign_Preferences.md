# PartDesign Preferences/it




<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

La finestre delle preferenze di [PartDesign](PartDesign_Workbench/it.md) si trovano nell\'[editor delle preferenze](Preferences_Editor/it.md), **Modifica → Preferenze → Part design**.


</div>

## Available preferences 


<div class="mw-translate-fuzzy">

Sono disponibili due schede: Generale e Visualizzazione della forma.


</div>


<div class="mw-translate-fuzzy">

## Generale


</div>


<div class="mw-translate-fuzzy">

Nella scheda \"Generale\" è possibile specificare quanto segue:

+-------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Nome                                                                                            | Descrizione                                                                                                                                                                                                                                                                                                         |
+=================================================================================================+=====================================================================================================================================================================================================================================================================================================================+
|                                                                                  | Se selezionato, dopo una [operazione booleana](Part_Boolean/it.md) controlla se la [Boundary representation](https://en.wikipedia.org/wiki/Boundary_representation) (BRep) del modello è valida. Questo viene fatto internamente dalla funzione [Controlla la geometria](Part_CheckGeometry/it.md). |
| **Controlla automaticamente il modello dopo una operazione booleana**               |                                                                                                                                                                                                                                                                                                                     |
|                                                                                              |                                                                                                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                  | Se selezionato, dopo una [operazioone booleana](Part_Boolean/it.md) il modello viene ripulito utilizzando la funzione [Affina forma](Part_RefineShape/it.md).                                                                                                                                       |
| **Affina automaticamente il modello dopo una operazione booleana**                  |                                                                                                                                                                                                                                                                                                                     |
|                                                                                              |                                                                                                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                  | Se selezionato, dopo che uno schizzo di un oggetto è stato modificato il modello viene ripulito utilizzando la funzione [Affina forma](Part_RefineShape/it.md).                                                                                                                                             |
| **Ridefinisci automaticamente il modello dopo un'operazione basata su uno schizzo** |                                                                                                                                                                                                                                                                                                                     |
|                                                                                              |                                                                                                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                  | Questa opzione non ha attualmente alcun effetto.                                                                                                                                                                                                                                                                    |
| **Aggiungi il nome dell'oggetto base**                                              |                                                                                                                                                                                                                                                                                                                     |
|                                                                                              |                                                                                                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


</div>

+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                                                                    | Description                                                                                                                                                                                                            |
+=========================================================================+========================================================================================================================================================================================================================+
|                                                          | If checked, the [Boundary representation](https://en.wikipedia.org/wiki/Boundary_representation) (BRep) of the model is [validated](Part_CheckGeometry.md) after [boolean operations](Part_Boolean.md) |
| **Automatically check model after boolean operation**       |                                                                                                                                                                                                                        |
|                                                                      |                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                          | If checked, the model is [refined](Part_RefineShape.md) after [boolean operations](Part_Boolean.md)                                                                                                    |
| **Automatically refine model after boolean operation**      |                                                                                                                                                                                                                        |
|                                                                      |                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                          | If checked, the model is [refined](Part_RefineShape.md) after changes to source sketches of objects                                                                                                            |
| **Automatically refine model after sketch-based operation** |                                                                                                                                                                                                                        |
|                                                                      |                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

![](images/Preferences_Part_design_Tab_General.png )


<div class="mw-translate-fuzzy">

## Visualizzazione della figura 


</div>


<div class="mw-translate-fuzzy">

Nella scheda \'\' Visualizzazione della figura\'\' è possibile specificare quanto segue:

+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Nome                                                                                | Descrizione                                                                                                                                                                                                   |
+=====================================================================================+===============================================================================================================================================================================================================+
|                                                                      | Maximum [deflessione lineare](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) degli oggetti tessellati dalla loro superficie.                |
| **Deviazione massima secondo il riquadro di delimitazione del modello** |                                                                                                                                                                                                               |
|                                                                                  |                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                      | Maximum [deflessione angolare](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) da una sezione alla sezione successiva di oggetti tessellati. |
| **Massima deflessione angolare**                                        |                                                                                                                                                                                                               |
|                                                                                  |                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


</div>

+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                                                                  | Description                                                                                                                                                                                                                     |
+=======================================================================+=================================================================================================================================================================================================================================+
|                                                        | Maximum [linear deflection](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) of the [tesselated](#Tesselation.md) objects from their surface            |
| **Maximum deviation depending on the model bounding box** |                                                                                                                                                                                                                                 |
|                                                                    |                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                        | Maximum [angular deflection](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) from one [tesselated](#Tesselation.md) object section to the next section |
| **Maximum angular deflection**                            |                                                                                                                                                                                                                                 |
|                                                                    |                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

![](images/Preferences_Part_design_Tab_Shape_view.png )

### Shape appearance 

On the *Shape appearance* tab you can specify the following:

+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                               | Description                                                                                                                                                                                                               |
+====================================+===========================================================================================================================================================================================================================+
|                     | Color for new shapes. If the option **Random** is set, a random color is used instead.                                                                                                          |
| **Shape color**        |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Line color for new shapes                                                                                                                                                                                                 |
| **Line color**         |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Line thickness for new shapes                                                                                                                                                                                             |
| **Line width**         |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Color for new [vertices](Glossary#Vertex.md)                                                                                                                                                                      |
| **Vertex color**       |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Size for new [vertices](Glossary#Vertex.md)                                                                                                                                                                       |
| **Vertex size**        |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Color of [bounding boxes](Property_editor#View.md) in the 3D view                                                                                                                                                 |
| **Bounding box color** |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | If checked, the color of the interior side of faces will be the same as the exterior side. If not checked either the [backlight color](Preferences_Editor#3D_View.md), if enabled, or black will be used instead. |
| **Two-side rendering** |                                                                                                                                                                                                                           |
|                                 |                                                                                                                                                                                                                           |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                     | Text color for document annotations. There is currently no dialog to add annotations to documents. Annotations can only be added using the Python console with this command:                                              |
| **Text color**         |                                                                                                                                                                                                                           |
|                                 | obj=App.ActiveDocument.addObject("App::Annotation", "Label")                                                                                                                                                            |
|                                    |                                                                                                                                                                                                                           |
|                                    | This console is shown using the menu **View → Panels → Python console**.                                                                                                                        |
+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

![](images/Preferences_Part_design_Tab_Shape_appearance.png )

## Tesselation

Al fine di visualizzare un oggetto in modo efficiente la sua superficie viene [tessellata](https://en.wikipedia.org/wiki/Tessellation_(computer_graphics)), cioè viene visualizzato con alcune piccole deviazioni dalla sua superficie reale. Questo vale non solo per i modelli di PartDesign, ma anche per altri oggetti di FreeCAD.

Il limite inferiore per la tassellatura è 0,01%. Se si vuole davvero passare più tempo di attesa dell\'elaborazione del modello si può ridurre ulteriormente il limite inferiore aprendo il menu **Strumenti → Modifica parametri ...**. Questo apre l\'editor dei parametri in cui si può accedere a **BaseApp → Preferenze → Mod → Part**.

Fare clic con il tasto destro del mouse su **Deviazione mesh** scegliere nel menu contestuale **Modifica valore**. Impostare il valore di tessellatura minima desiderata. Ricordare che il valore è in%, ovvero per un valore di 0,005% si deve inserire \"0,00005\". Il valore più piccolo possibile è 1e-7. **Nota:** Nel menu delle preferenze vedrà ancora 0,01% anche se si imposta un valore più basso.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}} 

[Category:Preferences](Category:Preferences.md)
