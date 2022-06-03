---
- GuiCommand   */it
   Name   *PartDesign Fillet
   Name/it   *Raccordo
   Workbenches   *[PartDesign](PartDesign_Workbench/it.md)
   MenuLocation   *PartDesign → Raccordo
   SeeAlso   *[PartDesign Smusso](PartDesign_Chamfer.md), [Part Raccordo](Part_Fillet.md)
---

# PartDesign Fillet/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento crea dei raccordi (arrotondamenti) sui bordi selezionati di un oggetto. Nella struttura del progetto viene creata una nuova voce **Fillet** (Raccordo), seguita da un numero sequenziale se nel documento esistono già altri raccordi.


</div>

## Utilizzo

### Add a fillet 


<div class="mw-translate-fuzzy">

-   Selezionare uno o più bordi di un oggetto, quindi avviare lo strumento facendo clic sulla sua icona o tramite il menu.
-   Nei **Parametri Raccordo** della finestra delle opzioni, impostare il raggio di raccordo inserendo il valore, o facendo clic sulle frecce su / giù. Il raccordo applicato viene mostrato in tempo reale.
-   Se si desidera aggiungere più bordi o facce, fare clic prima sul pulsante **Aggiungi** e quindi selezionare il bordo o la faccia.
-   Se si desidera rimuovere bordi o facce
    -   selezionare il bordo o la faccia nell\'elenco della finestra di dialogo e premere il tasto **Canc**. *Nota*   * poiché deve esserci almeno un bordo per la funzione, l\'ultimo bordo o faccia rimanente nell\'elenco non può essere rimosso.
    -   oppure fare clic sul pulsante **Rimuovi**. Tutti i bordi e le facce precedentemente selezionati vengono evidenziati in viola. Selezionare il bordo o la faccia da rimuovere.
-   Premere **OK** per convalidare.
-   Per una catena di spigoli tangenti l\'uno all\'altro, può essere selezionato un bordo singolo, il raccordo si propaga lungo la catena.
-   Per modificare il raccordo dopo che la funzione è stata convalidata, fare doppio clic sull\'etichetta del Raccordo nella struttura del progetto, oppure fare clic destro su di esso e selezionare **Modifica Raccordo**.


</div>

### Edit a fillet 

1.  Do one of the following   *
    -   Double-click the Fillet object in the [Tree view](Tree_view.md)
    -   Right-click the Fillet object in the [Tree view](Tree_view.md) and select **Edit Fillet** from the context menu.
2.  The **Fillet parameters** [task panel](Task_panel.md) opens.See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.

## Options

-   To add edges do one of the following   *
    -   Press the **Add** button to start selecting edges and/or faces in the [3D view](3D_view.md).
    -   To select all remaining edges do the following   *
        1.  If required press the **Add** button.
        2.  Use the **Ctrl**+**Shift**+**A** keyboard shortcut, or right-click the list and select **Add all edges** from the context menu. <small>(v0.20)</small> 
-   To remove edges do one of the following   *
    -   Press the **Remove** button to start deselecting edges and/or faces in the [3D view](3D_view.md). Selected elements are highlighted in purple.
    -   Select one or more elements in the list and press the **Del** key, or right-click the list and select **Remove** from the context menu.
-   Set the **Radius** of the fillet.
-   Check the **Use all edges** checkbox to select all edges of the previous feature. This deactivates the selection list and the related buttons. <small>(v0.20)</small> 

## Notes

-   PartDesign Fillet should not be confused with [Part Fillet](Part_Fillet.md). Unless you know what you are doing, [Part Fillet](Part_Fillet.md) should not be used on a PartDesign Body. See [Part and PartDesign](Part_and_PartDesign.md).
-   Fillets cannot completely consume the adjacent faces.

## Properties

See also   * [Property editor](Property_editor.md).

A PartDesign Fillet object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties   *

### Data


{{Properties_Title|Base}}

-    **Base|LinkSub**   * Link to the selected edges and faces of the parent feature. Can be a link to only the parent feature if **Use All Edges** is `True`.

-    **Support Transform|Bool**   * If `True` the filleted shape of the additive/subtractive parent feature will be used when the fillet object is included in a [pattern](PartDesign_Workbench#Transformation_tools.md), else only the shape of the fillet itself will be used. The default is `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**   * Link to the parent feature.

-    **_ Body|LinkHidden|hidden**   * Link to the parent body.


{{Properties_Title|Fillet}}

-    **Radius|QuantityConstraint**   * The fillet radius. The default is {{value|1 mm}}.

-    **Use All Edges|Bool**   * If `True` all edges of the feature are filleted, and the edges specified by **Base** are ignored. The default is `False`.


{{Properties_Title|Part Design}}

-    **Refine|Bool**   * If `True` redundant edges are removed from the result of the operation. The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).


<div class="mw-translate-fuzzy">

## Problemi noti 


</div>


<div class="mw-translate-fuzzy">

Raccordi, smussi e altre funzionalità che operano su corpi solidi dipendono dal kernel OpenCASCADE Technology (OCCT) sottostante utilizzato da FreeCAD. Occasionalmente il kernel OCCT ha difficoltà nel gestire gli spigoli coincidenti, dove si incontrano due facce. In questo caso, FreeCAD potrebbe bloccarsi senza una spiegazione.


</div>


<div class="mw-translate-fuzzy">

Se eseguito dal terminale, FreeCAD può generare un registro come questo dopo l\'arresto anomalo   *


</div>


{{code|lang=text|code=
#1  0x7fff63d660ba in BRep_Tool   *   *Curve(TopoDS_Edge const&, TopLoc_Location&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x2a
#2  0x7fff63d69546 in BRep_Tool   *   *Curve(TopoDS_Edge const&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x46
#3  0x7fff71f4fef5 in ChFi3d_Builder   *   *PerformIntersectionAtEnd(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x3b05
#4  0x7fff71f58307 in ChFi3d_Builder   *   *PerformOneCorner(int, bool) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x1097
#5  0x7fff71ef6218 in ChFi3d_Builder   *   *PerformFilletOnVertex(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x4e8
#6  0x7fff71ef71d1 in ChFi3d_Builder   *   *Compute() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0xe31
#7  0x7fff720ad7c3 in BRepFilletAPI_MakeChamfer   *   *Build() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x33
#8  0x7fff723be48e in PartDesign   *   *Chamfer   *   *execute() from /usr/lib/freecad-daily/lib/_PartDesign.so+0x60e
...
}}


<div class="mw-translate-fuzzy">

Questo output fa riferimento a funzioni situate in `libTKBRep.so`, `libTKFillet.so`, ecc., che sono librerie OCCT. Se si verifica questo tipo di arresto anomalo, potrebbe essere necessario segnalare e risolvere il problema in OCCT anziché in FreeCAD.


</div>

Per maggiori informazioni vedere le discussioni del forum    *

-   [Bug Chamfer bigger than 2mm crashes freecad](https   *//forum.freecadweb.org/viewtopic.php?p=263818#p263818)
-   [Segfault when using part desigin fillet](https   *//forum.freecadweb.org/viewtopic.php?p=264827#p264827)

### Topological naming 


<div class="mw-translate-fuzzy">

### Denominazione topologica 

I numeri che rappresentano i nomi dei bordi non sono completamente stabili, pertanto è consigliabile terminare il lavoro di modellazione principale del corpo solido prima di applicare funzioni come raccordi e smussi, altrimenti i bordi potrebbero cambiare nome e i bordi raccordati diventerebbero probabilmente non validi.


</div>


<div class="mw-translate-fuzzy">

Ulteriori informazioni nella pagina dedicata al [problema di denominazione topologica](topological_naming_problem/it.md).


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Fillet/it
