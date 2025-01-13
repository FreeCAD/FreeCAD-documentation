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

In questo tutorial spiegheremo come importare file STL/OBJ in FreeCAD. Poiché il formato mesh STL/OBJ è adimensionale, FreeCAD presumerà durante l\'importazione che le unità utilizzate nel modello siano mm. In caso contrario, è necessario ridimensionare il proprio modello nell\'applicazione con cui è stato creato (prima di esportarlo) oppure è necessario ridimensionare il proprio modello in FreeCAD dopo averlo importato e convertito in un solido.

## Modello di Esempio 

Per questo tutorial si può usare un proprio file STL o creare un file demo facendo questo:

-   Aprire FreeCAD
-   Creare un nuovo documento
-   Passare al workbench mesh
-   Inserire un toroide cliccando su **Meshes** → **<img src="images/Mesh_BuildRegularSolid.svg" width=32px> Solido regolare...**, scegliendo impostazioni come:
    -   Raggio1: 10 mm
    -   Raggio2: 2 mm
    -   Campionamento: 50
-   Cliccare su **Crea** e poi su **Chiudi**
-   Salvare il proprio file con **File** → **Salva** per ottenere un file FreeCAD contenente un oggetto mesh

Per importare un file STL o OBJ in FreeCAD, creare un nuovo documento FreeCAD e scegliere **File** → **Importa** dal menu in alto.

## Pulizia e riparazione del file STL/OBJ per la preparazione dell\'importazione 

In pratica, FreeCAD importerebbe qualsiasi file STL/OBJ. Ma il nostro obiettivo è avere un solido che possa essere misurato e modificato (aggiungendo estrusioni/tasche\...). Per una conversione di successo da mesh a solido, dobbiamo assicurarci che la mesh sia \"impermeabile\" (non abbia buchi) o non abbia altri errori.
L\'obiettivo di FreeCAD non è quello di essere un buon modellatore di mesh, è progettato per essere un modellatore di solidi. FreeCAD ha alcune capacità per l\'operazione di mesh negli ambienti Mesh e OpenSCAD (alcune operazioni richiedono che OpenSCAD sia installato e configurato nelle preferenze di FreeCAD).
Alcuni utenti preferiscono usare software di terze parti per pulire e riparare le mesh, ad esempio

-   [Netfabb Basic](http://www.netfabb.com/downloadcenter.php?basic=1) (Windows/Linux/Mac) - gratuito per uso personale (disponibile la riparazione automatica delle mesh)
-   [Meshlab](http://meshlab.sourceforge.net/) (Windows/Linux/Mac) - Open Source

In questo tutorial useremo il workbench delle mesh all\'interno di FreeCAD per pulire/riparare/verificare la mesh del proprio file di esempio.

### Test e riparazione automatica 

-   Aprire FreeCAD e il file di esempio FreeCAD contenente l\'oggetto mesh
-   Passare al workbench mesh
-   Assicurarsi che il proprio oggetto mesh sia selezionato nella vista ad albero
-   Scegliere **Mesh** → **Analizza** → **Valuta & Ripara mesh...** dal menu in alto
-   Assicurarsi che il menu a discesa nell\'angolo in alto a destra visualizzi il nome del proprio oggetto mesh
-   Con l\'ultimo punto nell\'elenco che riporta \"Tutti i test precedenti insieme\", fare clic su **Analizza**
-   I testi accanto alle caselle di controllo cambieranno per riflettere i risultati dei diversi test
-   Se sono stati rilevati degli errori, le caselle di controllo corrispondenti saranno spuntate e sarà possibile selezionare **Ripara**
-   Scegliere **Chiudi** per chiudere il menu

### Armonizzazione delle normali 

L\'armonizzazione delle normali di un oggetto mesh può essere eseguita

-   Selezionando l\'oggetto mesh nella vista ad albero
-   Scegliere **Mesh** → **<img src="images/Mesh_HarmonizeNormals.svg" width=32px> Armonizza normali** dal menu in alto.

Suggerimento: scegliendo l\'oggetto mesh nella vista ad albero, andando alla scheda vista nella vista proprietà e cambiando \"Illuminazione\" da \"Due lati\" a \"Un lato\" è possibile identificare i triangoli con normali capovolte. Se le normali puntano all\'interno della mesh, il triangolo verrà mostrato in nero.

### Chiudere i fori 

Inoltre è possibile chiudere manualmente i fori nell\'oggetto mesh:

-   Selezionare la mesh nella vista ad albero
-   Scegliere **Mesh** → **Chiudi i fori...** dal menu principale
-   Specificare il numero massimo di spigoli da usare per riempire (3 è l\'impostazione predefinita)
-   Dato che STL e OBJ sono mesh con struttura costituita da triangoli il numero predefinito di bordi dovrebbe essere sufficiente

Un altro metodo di chiusura manuale dei fori in un oggetto mesh può essere:

-   Selezionare la mesh nella vista ad albero
-   Scegliere **Mesh** → **<img src="images/Mesh_FillInteractiveHole.svg" width=32px> Chiudi fori** dal menu principale
-   Selezionare nella vista 3D uno dei bordi del foro dell\'oggetto mesh
-   Cliccare con il tasto destro nella vista 3D e scegliere **Esci dalla modalità di riempimento del foro** per uscire dal comando

## Convertire la mesh in solido 

-   Passare nell\'ambiente <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/it.md)
-   Accertarsi che l\'oggetto mesh sia selezionato nella vista ad albero, altrimenti selezionarlo
-   Scegliere **Part** → **<img src="images/Part_ShapeFromMesh.svg" width=32px> Crea forma da mesh ...** nel menu principale
-   Specificare la tolleranza (di default è 0,1)
-   Nella vista ad albero viene creato un nuovo oggetto (con l\'icona blu di forma, invece dell\'icona verde di mesh)
-   Selezionare l\'oggetto appena creato nella struttura ad albero
-   Scegliere **Part** → **Crea una copia** → **<img src="images/Part_RefineShape.svg" width=32px> Affina forma** nel menu principale
-   Nella struttura ad albero viene creato un nuovo oggetto e quello precedente viene reso invisibile
-   Selezionare l\'oggetto appena creato nella struttura ad albero
-   Scegliere **Part** → **Converti in solido** dal menu principale
-   Nella struttura ad albero viene creato un nuovo oggetto, contenente \"(Solid)\" nel suo nome, per indicare che è un solido

Dato che il solido creato in questo modo non ha cronologia e non ha funzioni modificabili (in FreeCAD è come una semplice copia) dalla vista ad albero si possono eliminare tutti gli oggetti precedenti. Questo riduce le dimensioni del file \...



## Link

-   [Esportare in STL o OBJ](Export_to_STL_or_OBJ/it.md)
-   [Importazione e esportazione](Import_Export/it.md)



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [Import](Import_Workbench.md) > Import from STL or OBJ/it
