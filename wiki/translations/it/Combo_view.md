# Combo view/it
{{TOCright}}

## Introduzione

La [vista combinata](combo_view/it.md) è uno dei pannelli principali nell\'interfaccia di FreeCAD. Di default si trova sul lato sinistro dello schermo. È composta da due parti   *

-   la [parte superiore](Combo_view/it#Sezione_superiore.md) che contiene due schede   * **Modello** e **Azioni**
-   la [parte inferiore](Combo_view/it#Sezione_inferiore.md) che mostra l\'[editor delle proprietà](property_editor/it.md). Essa contiene due schede   * le proprietà **Vista** e **Dati**. L\'[editor delle proprietà](property_editor/it.md) viene visualizzato solo quando è attiva la scheda **Modello**, ovvero quando è visibile la [vista ad albero](tree_view/it.md).


**Nota.**

Inizialmente la parte superiore (la [vista ad albero](tree_view/it.md)) era separata dalla parte inferiore (l\'[editor delle proprietà](property_editor/it.md)) ma poi sono state combinate e quindi è stata creata la vista \"combinata\".

## Sezione superiore 

La scheda **Modello** mostra la [vista ad albero](tree_view/it.md), che è una rappresentazione del contenuto del documento, inclusa la geometria 2D e 3D con la loro cronologia parametrica, ma supporta anche oggetti che contengono i dati salvati nel documento.

La scheda **Azioni** contiene il [pannello delle azioni](task_panel/it.md), che mostra diverse azioni a seconda dell\'ambiente di lavoro attivo e dello strumento attivo.

<img alt="" src=images/FreeCAD_Combo_view_Tree_View_properties.png  style="width   *" height="600px;"> <img alt="" src=images/FreeCAD_Combo_view_Task_panel.png  style="width   *" height="600px;">



*La vista combinata ha due schede   * la scheda Modello che mostra e controlla la [vista ad albero](tree_view/it.md) e l'[editor delle proprietà](property_editor/it.md), e la scheda Azioni che mostra e controlla il [pannello delle azioni](task_panel/it.md).*

## Sezione inferiore 

La parte inferiore della vista combinata mostra l\'[editor delle proprietà](property_editor/it.md), che contien due schede per le proprietà **Vista** e **Dati**. L\'editor delle proprietà viene visualizzato solo quando la scheda **Modello** è attiva, ovvero quando la [vista ad albero](tree_view/it.md) è visibile.

-   La scheda **Vista** mostra le proprietà di visualizzazione degli oggetti, che influiscono solo sul loro aspetto nella [vista 3D](3D_view/it.md).

-   La scheda **Dati** mostra le proprietà parametriche degli oggetti, quelle che definiscono le forme geometriche.

<img alt="" src=images/FreeCAD_Combo_view_Tree_View_properties.png  style="width   *" height="600px;"> <img alt="" src=images/FreeCAD_Combo_view_Tree_Data_properties.png  style="width   *" height="600px;">



*La parte inferiore della vista combinata è l'editor delle proprietà, che mostra le proprietà Vista e Dati.*

## Disabilitazione della vista combinata 

Per utilizzare questi pannelli in modo indipendente, utilizzare l\'[editor dei parametri](Std_DlgParameter/it.md). Creare i seguenti sottogruppi se non esistono

-    `BaseApp/Preferences/DockWindows/TreeView`
    

-    `BaseApp/Preferences/DockWindows/PropertyView`
    

quindi aggiungere il parametro `Enabled` di tipo `Boolean`, e impostarlo su `True`.

Quindi attivare la vista utilizzando il menu **Visualizza → Pannelli → Struttura** o **→ Proprietà**.


{{Std Base navi

}} {{Interface navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Combo view/it
