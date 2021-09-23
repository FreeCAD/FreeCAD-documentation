# Import from STL or OBJ/it
{{TutorialInfo/it
|Topic= Importare da STL o OBJ
|Level= Base
|Time= 30 minuti
|Author=r-frank
|FCVersion=0.16.6703
|Files=
}}

## Introduzione


<div class="mw-translate-fuzzy">

In questo tutorial ci occuperemo di come importare i file STL / OBJ in FreeCAD. Dato che il formato mesh STL / OBJ è adimensionale, nell\'importazione di questi file FreeCAD assume che l\'unità utilizzata nel modello sia il mm. Se non è così, bisogna scalare il proprio modello nell\'applicazione con cui è stato creato, prima di esportarlo, oppure scalare il modello in FreeCAD dopo l\'importazione e la conversione in solido.


</div>


<div class="mw-translate-fuzzy">

## Il modello 

Per questo tutorial è possibile utilizzare un proprio file STL o creare un file demo in questo modo:

-   Avviare FreeCAD
-   Creare un nuovo documento
-   Passare nell\'ambiente mesh
-   Inserire un toro cliccando su ** Meshes** → **<img src="images/Mesh_BuildRegularSolid.svg" width=32px> Solido regolare...** → ** Toro** , e poi selezionare queste impostazioni:
    -   Raggio 1: 10 mm
    -   Raggio 2: 2 mm
    -   Campionatura: 50
-   Cliccare su ** Crea** e poi su ** Chiudi**
-   Salvare il file con ** File** → ** Salva** per avere un file di FreeCAD contenente un oggetto mesh

Per importare un file STL o OBJ in FreeCAD, creare un nuovo documento di FreeCAD e poi, dal menu principale, scegliere ** File** → ** Importa**.


</div>


<div class="mw-translate-fuzzy">

## Pulizia e riparazione del file STL / OBJ per prepararlo all\'importazione 

In genere, FreeCAD può importare qualsiasi file STL / OBJ. Ma il nostro obiettivo è quello di avere un solido che possa essere misurato e modificato (con l\'aggiunta di estrusioni, scavi, ecc ..). Per la conversione da mesh a solido si deve fare in modo che la mesh sia \"a tenuta stagna\", cioè senza buchi o non abbia altri errori.
L\'obiettivo di FreeCAD non è quello di essere un buon modellatore di mesh, esso è stato progettato per essere un modellatore di solidi. FreeCAD ha alcune funzionalità per le operazioni su mesh negli ambienti Mesh e OpenSCAD (Alcune operazioni richiedono che OpenSCAD sia stato installato e configurato nelle preferenze di FreeCAD).
Ad alcuni utenti piace utilizzare software di terze parti per la pulizia e la riparazione delle mesh, ad esempio

-   [Netfabb Basic](http://www.netfabb.com/downloadcenter.php?basic=1) (Windows/Linux/Mac) - free per uso personale (è disponibile la riparazione automatica delle mesh)
-   [Meshlab](http://meshlab.sourceforge.net/) (Windows/Linux/Mac) - Open Source

In questo tutorial si usa l\'ambiente Mesh incorporato in FreeCAD per pulire / riparare / verificare le mesh del file di esempio.


</div>


<div class="mw-translate-fuzzy">

### Analisi e riparazione automatica 

-   Aprire FreeCAD e il file FreeCAD campione contenente l\'oggetto mesh
-   Passare nell\'ambiente Mesh
-   Accertarsi che nella vista ad albero sia selezionato l\'oggetto mesh
-   Scegliere ** Mesh** → ** Analizza** → ** Analizza & Ripara mesh...** dal menu principale
-   Assicurarsi che il menu a tendina visualizzi in alto a destra il nome dell\'oggetto mesh
-   Nell\'ultimo punto della lista \"Tutti i test insieme\" cliccare su ** Analizza**
-   I campi di testo accanto alle caselle riportano i risultati dei vari test
-   Se vengono rilevati errori le corrispondenti caselle di controllo appaiono spuntate ed è quindi possibile selezionare l\'azione ** Ripara**
-   Scegliere ** Chiudi** per chiudere il menu


</div>


<div class="mw-translate-fuzzy">

### Armonizzare le normali 

Per armonizzazione le normali di un oggetto mesh si può

-   Selezionare la mesh nella vista ad albero
-   Scegliere ** Mesh** → **<img src="images/Mesh_HarmonizeNormals.svg" width=32px> Armonizza le normali** nel menu principale.

Suggerimento: Scegliendo l\'oggetto mesh nella vista ad albero, andando alla scheda visualizzazione della finestra delle proprietà e cambiando \"Illuminazione\" da \"Two Side\" a \"One Side\" è possibile identificare i triangoli con le normali capovolte. Se le normali puntano verso la mesh il triangolo viene visualizzato in nero.


</div>


<div class="mw-translate-fuzzy">

### Chiudere i fori 

Inoltre è possibile chiudere manualmente i buchi nell\'oggetto mesh:

-   Selezionare la mesh nella vista ad albero
-   Scegliere ** Mesh** → ** Chiudi i fori...** dal menu principale
-   Specificare il numero massimo di spigoli da usare per riempire (3 è l\'impostazione predefinita)
-   Dato che STL e OBJ sono mesh con struttura costituita da triangoli il numero predefinito di bordi dovrebbe essere sufficiente

Un altro metodo di chiusura manuale dei fori in un oggetto mesh può essere:

-   Selezionare la mesh nella vista ad albero
-   Scegliere ** Mesh** → **<img src="images/Mesh_FillInteractiveHole.svg" width=32px> Chiudi fori** dal menu principale
-   Selezionare nella vista 3D uno dei bordi del foro dell\'oggetto mesh
-   Cliccare con il tasto destro nella vista 3D e scegliere ** Esci dalla modalità di riempimento del foro** per uscire dal comando


</div>


<div class="mw-translate-fuzzy">

## Convertire la mesh in solido 

-   Passare nell\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/it.md)
-   Accertarsi che l\'oggetto mesh sia selezionato nella vista ad albero, altrimenti selezionarlo
-   Scegliere ** Part** → **<img src="images/Part_ShapeFromMesh.svg" width=32px> Crea forma da mesh ...** nel menu principale
-   Specificare la tolleranza (di default è 0,1)
-   Nella vista ad albero viene creato un nuovo oggetto (con l\'icona blu di forma, invece dell\'icona verde di mesh)
-   Selezionare l\'oggetto appena creato nella struttura ad albero
-   Scegliere ** Part** → ** Crea una copia** → **<img src="images/Part_RefineShape.svg" width=32px> Affina forma** nel menu principale
-   Nella struttura ad albero viene creato un nuovo oggetto e quello precedente viene reso invisibile
-   Selezionare l\'oggetto appena creato nella struttura ad albero
-   Scegliere ** Part** → ** Converti in solido** dal menu principale
-   Nella struttura ad albero viene creato un nuovo oggetto, contenente \"(Solid)\" nel suo nome, per indicare che è un solido

Dato che il solido creato in questo modo non ha cronologia e non ha funzioni modificabili ( in FreeCAD è come una semplice copia) dalla vista ad albero si possono eliminare tutti gli oggetti precedenti. Questo riduce le dimensioni del file \...


</div>

## Link


<div class="mw-translate-fuzzy">

-   [Esportare in STL o OBJ](Export_to_STL_or_OBJ/it.md)
-   [Importazione e esportazione](Import_Export/it.md)


</div>


 

[Category:File\_Formats](Category:File_Formats.md)

---
[documentation index](../README.md) > [Import](Import_Workbench.md) > Import from STL or OBJ/it
