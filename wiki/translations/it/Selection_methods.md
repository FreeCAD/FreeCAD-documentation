# Selection methods/it
{{TOCright}}

## Presentazione

I metodi di selezione in FreeCAD consentono di selezionare gli oggetti nell\'_, nella [struttura ad albero](Tree_view/it.md), nella [vista selezione](Selection_view/it.md), e tramite altri dialoghi. Alcuni metodi di selezione sono specifici di un particolare ambiente e sono documentati nella documentazione specifica di tale ambiente.

## Vista 3D 

Nella [vista 3D](3D_view/it.md) ci sono vari modi per selezionare gli oggetti.

### Selezione semplice 

La selezione semplice con il mouse (per impostazione predefinita clic sinistro) e la preselezione (passaggio del mouse) sono descritte nella pagina [navigare col mouse](Mouse_navigation/it.md).

### Clic ripetuti 

Il primo clic seleziona un sottoelemento (vertice, bordo o faccia) dell\'oggetto sotto il mouse. Un secondo clic seleziona l\'intero oggetto. {{Version/it|0.18}}

Il terzo clic estende la selezione al suo oggetto contenitore ([Corpo di PartDesign](PartDesign_Body/it.md), [Parte](Std_Part/it.md) e altri). Ulteriori clic espandono la selezione nella catena del contenitore. {{Version/it|0.19}}

### Comandi di selezione 

-   Per selezionare tutti gli oggetti: [Std SelectAll](Std_SelectAll/it.md).
-   Per inquadrare selezionare più oggetti principali: [Std BoxSelection](Std_BoxSelection/it.md).
-   Per inquadrare più facce: [Std BoxElementSelection](Std_BoxElementSelection/it.md) o [Part BoxSelection](Part_BoxSelection/it.md).

## Vista selezione 

La [vista selezione](Selection_view/it.md) mostra i nomi degli oggetti selezionati, incluso il loro nome completo all\'interno di un oggetto, ad esempio, `Unnamed#Body.Box001.Face17`.

Permette anche di eseguire alcune azioni come [visualizzare la selezione](Std_ViewFitSelection/it.md), e di inviare l\'oggetto alla [console Python](Python_console/it.md).

### Esportazione dell\'oggetto 

*Questo dovrebbe essere aggiunto nella pagina [visualizzare la selezione](selection_view/it.md).*

Selezionare un oggetto complesso, ad esempio un [Corpo di PartDesign](PartDesign_Body/it.md) o una [Parte](Std_Part/it.md), quindi nel pannello [vista selezione](selection_view/it.md) selezionare nuovamente l\'oggetto, quindi premere **Ctrl** + **C** sulla tastiera per aprire la finestra di dialogo **Selezione oggetto**. Ciò consente di copiare l\'oggetto selezionato insieme a tutti o solo alcuni degli oggetti dipendenza di quell\'oggetto. Ad esempio, per una [Parte](Std_Part/it.md) i possibili oggetti da selezionare includono la [Parte](Std_Part/it.md) stessa, ma anche la sua origine, i suoi tre assi di base (XYZ) e i suoi tre piani di base (XY , YZ, XZ).

Dopo aver premuto **OK**, gli oggetti selezionati vengono copiati in memoria e quindi possono essere incollati nel documento per duplicare solo questi oggetti.

![](images/ObjectSelection.png )



*Finestra di dialogo per la selezione degli oggetti avviata da [vista selezione](Selection_view/it.md).*

## Vista ad albero 

Nella [vista ad albero](tree_view/it.md) gli elementi possono essere selezionati o deselezionati uno alla volta, tenendo premuto il tasto **Ctrl** e facendo clic con il mouse.

È possibile selezionare un intervallo di elementi facendo clic sul primo elemento, tenendo premuto **Maiusc** e facendo clic sull\'ultimo elemento.

La selezione di un singolo elemento mostrerà anche le sue proprietà nell\'[editore delle proprietà](property_editor/it.md).

Facendo doppio clic si apre la [scheda azioni](task_panel/it.md) contente tutte le azioni associate. Assicurarsi di chiudere questo pannello delle azioni prima di eseguire un altro comando o di passare a qualsiasi altro ambiente.

Sono disponibili altri metodi aprendo il menu di scelta rapida (tasto destro), a seconda dell\'oggetto selezionato o dell\'ambiente attivo; vedere le informazioni in [vista ad albero](tree_view/it.md).

## Script

La selezione di oggetti è intrinsecamente un\'attività grafica e pertanto è disponibile solo quando è caricata l\'interfaccia utente grafica.

Questi comandi possono essere utilizzati nelle [macro](Macros/it.md) o dalla [console Python](Python_console/it.md).


```python
import FreeCADGui as Gui

Gui.Selection.addSelection
Gui.Selection.addSelectionGate
Gui.Selection.Filter
```

Il comando `addSelectionGate` impedisce all\'utente di selezionare oggetti non specificati nella stringa di selezione. Viene visualizzato un simbolo quando il puntatore si trova su un elemento che non è nel gruppo specificato.


```python
Gui.Selection.addSelectionGate("SELECT Part::Feature SUBELEMENT Edge")
```

Vedere nella [Documentazione del codice sorgente](Source_documentation/it.md) e nella [Documentazione dei moduli Python](Std_PythonHelp/it.md) per ulteriori aiuti sull\'uso di questi strumenti.

---
[documentation index](../README.md) > Selection methods/it
