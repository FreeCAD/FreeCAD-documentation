# PartDesign Thickness/it
---
- GuiCommand:   Name: PartDesign Thickness   Name/it: Spessore   Workbenches: [MenuLocation: Part Design - Spessore   Version: 0.17   SeeAlso: [[Part_Thickness/it|Spessore di Parte](PartDesign_Workbench/it___PartDesign]].md)---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento **Spessore** funziona su un corpo solido e lo trasforma in un oggetto cavo, con almeno una faccia aperta, e assegna a ciascuna delle sue facce rimanenti uno spessore uniforme. Su alcuni solidi permette di velocizzare significativamente il lavoro ed evita di fare estrusioni e tasche.


</div>

<img alt="" src=images/PartDesign_Thickness_example.svg  style="width:600px;"> 
*Base solid (A) →  Solid with selected face to be opened (B) →  Resulting hollow object (C)*

## Utilizzo

### Add a thickness 


<div class="mw-translate-fuzzy">

1.  Selezionare una o più facce nel corpo attivo.
2.  Premere il pulsante **<img src="images/PartDesign_Thickness.svg" width=24px> '''Spessore'''**.
3.  Definire i **Parametri dello spessore** (vedere le [Opzioni](#Options/it.md)).
4.  Per aggiungere più facce da aprire, premere su **Aggiungi faccia** e selezionare una faccia nella vista 3D.
5.  Per rimuovere una faccia selezionata in precedenza, premere su **Rimuovi faccia** e selezionare una faccia nella vista 3D o fare clic con il tasto destro sull\'etichetta della faccia nell\'elenco e selezionare *Rimuovi*.
6.  Premere **OK**.


</div>


:   *Remember*:
    -   Since there must be at least one face for the feature, the last remaining face in the list cannot be removed.

### Edit a thickness 

1.  Do one of the following:
    -   Double-click the Thickness object in the [Tree view](Tree_view.md)
    -   Right-click the Thickness object in the [Tree view](Tree_view.md) and select **Edit Thickness** from the context menu.
2.  The **Thickness parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.

## Opzioni


<div class="mw-translate-fuzzy">

-   **Thickness**: Spessore della parete dell\'oggetto risultante. Impostare il valore desiderato.
-   **Mode**
    -   *Skin*: Selezionare questa opzione per ottenere un oggetto simile ad un vaso, senza testa ma con il fondo
    -   *Pipe*: Selezionare questa opzione per ottenere un oggetto simile ad un tubo, senza testa e senza fondo. In questo caso può essere conveniente selezionare le facce da eliminare prima di avviare lo strumento. Aiutarsi con i pulsanti delle viste predefinite o utilizzare i tasti numerici.
    -   *Recto Verso*:
-   **Join Type**
    -   *Arc*: rimuove i bordi esterni e crea un raccordo con un raggio uguale allo spessore definito.
    -   *Intersection*: quando le facce sono spostate verso l\'esterno, gli spigoli tra le facce vengono mantenuti.
-   **Make thickness inwards**: quando è selezionato, le facce sono spostate verso l\'interno.


</div>

## Notes


<div class="mw-translate-fuzzy">

-   Deve essere selezionata almeno una faccia da aprire.
-   Se lo spessore va verso l\'interno, il valore deve essere inferiore alla dimensione più piccola del corpo.
-   Il comando potrebbe non riuscire con forme complesse. In questo contesto la superficie di un cono deve già essere considerata complessa.
    -   [Sweep additivi](PartDesign_AdditivePipe/it.md) o [Loft additivo](PartDesign_AdditiveLoft.md) possono funzionare meglio per creare forme complesse


</div>

## Properties

See also: [Property editor](Property_editor.md).

A PartDesign Thickness object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

-    **Base|LinkSub**: Sub-link to the parent feature\'s list of selected edges and faces.

-    **Support Transform|Bool**: \"Include the base additive/subtractive shape when used in pattern features. If disabled, only the dressed part of the shape is used for patterning\". Default: `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**: Link to the parent feature.

-    **_ Body|LinkHidden|hidden**: Link to the parent body.


{{Properties_Title|Part Design}}

-    **Refine|Bool**: \"Refine shape (clean up redundant edges) after adding/subtracting\". The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).


{{Properties_Title|Thickness}}

-    **Value|Length**: \"Thickness value\". Default: {{value|1 mm}}.

-    **Mode|Enumeration**: \"Mode\". {{value|Skin}} (default), {{value|Pipe}} or {{Value|Recto verso}}. Only {{value|Skin}} is implemented.

-    **Join|Enumeration**: \"Join type\". {{value|Arc}} (default) or {{Value|Intersection}}.

-    **Reversed|Bool**: \"Apply the thickness towards the solids interior\". Default: `False`.

-    **Intersection|Bool**: \"Enable intersection-handling\". Default: `False`.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Thickness/it
