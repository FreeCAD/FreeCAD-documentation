---
 GuiCommand:
   Name: BIM Project
   Name/it: BIM Progetto
   MenuLocation: 3D/BIM , Progetto
   Workbenches: BIM_Workbench/it
   Shortcut: 
   SeeAlso: 
---

# BIM Project/it



## Descrizione

Lo strumento **Progetto BIM** crea un progetto [NativeIFC](NativeIFC.md) nel documento corrente. In IFC, un progetto (IfcProject) è l\'oggetto radice di tutti i contenuti del modello. È obbligatorio averne uno in ciascun file IFC.

Non è necessario creare un progetto per esportare un modello di FreeCAD in IFC, poiché ne verrà aggiunto uno predefinito ogni volta che si esporta un file IFC. Tuttavia, quando si lavora con [NativeIFC](NativeIFC.md), un file IFC viene associato al modello e tutta la geometria e le proprietà di quel modello e dei suoi componenti provengono dal file IFC associato. Il progetto è il punto in cui il file IFC è associato al documento.

In genere, si crea un progetto BIM per associare un file IFC. Durante la creazione del progetto, il file IFC associato è vuoto e non viene salvato. La prossima volta che si salverà il file FreeCAD, verrà chiesto di salvare anche il file IFC.

Se si distribuisce il file di FreeCAD, tutti i file IFC associati devono essere distribuiti insieme, altrimenti FreeCAD non sarà in grado di estrarre la geometria. Tuttavia, se la proprietà **shape mode** di tutti gli oggetti contenuti in un progetto è impostata su **Shape**, il file di FreeCAD può essere distribuito senza il file IFC di accompagnamento e si aprirà comunque correttamente su altri computer. Gli oggetti IFC, tuttavia, non saranno più modificabili.

Quando si inserisce un file IFC, viene creato un oggetto di progetto che contiene tutto il contenuto del file. Come tutti gli oggetti NativeIFC, il progetto può essere espanso facendo doppio clic sullo stesso nell\'albero.



## Utilizzo

1.  Assicurarsi di avere un documento FreeCAD aperto.
2.  Premere il pulsante **<img src="images/BIM_Project.svg" width=16px> [Progetto](BIM_Project/it.md)**.
3.  Facoltativamente, bloccare il documento premendo il pulsante **<img src="images/IFC.svg" width=16px> [Blocca IFC](NativeIFC/it#Locked_and_unlocked_modes/it.md)**.



## Modalità bloccata e sbloccata 

Nell\'[Ambiente BIM](BIM_Workbench/it.md), la barra di stato presenta un pulsante **<img src="images/IFC.svg" width=16px> [Blocca IFC](NativeIFC/it#Locked_and_unlocked_modes.md)** che consente di alternare tra **bloccato** e **sbloccato**. Una volta sbloccato, è possibile avere diversi [progetti](BIM_Project/it.md) all\'interno del proprio documento FreeCAD e avere anche elementi IFC e non IFC.

In modalità bloccata, i dati associati all\'oggetto del progetto vengono associati direttamente al documento di FreeCAD. Il documento di FreeCAD agisce come una replica fedele, o rendering, del documento IFC. L\'oggetto del progetto viene quindi rimosso. E\' possibile avere un solo progetto nel proprio documento FreeCAD e non è più possibile avere oggetti non IFC (ogni nuovo oggetto viene immediatamente convertito in IFC).



## Aggiungere oggetti ad un progetto 

Gli oggetti vengono aggiunti a un progetto semplicemente trascinandoli sul progetto nella visualizzazione ad albero. Questi oggetti verranno convertiti in IFC e potrebbero perdere alcuni dei loro precedenti comportamenti parametrici quando non sono supportati da IFC.



## Differenza

Quando il progetto contiene modifiche non salvate, verrà visualizzato un punto rosso sull\'icona dell\'albero. Facendo clic con il pulsante destro del mouse sul progetto e scegliendo **IFC → Diff** si aprirà una finestra di dialogo per vedere un [diff](https://en.wikipedia.org/wiki/Diff) di ciò che è cambiato nel file IFC associato. Questo è un buon modo per assicurarsi che ciò che si ha cambiato sia realmente ciò che si voleva.



## Salvataggio

I file IFC associati ad un progetto vengono salvati automaticamente ogni volta che si salva il file di FreeCAD. Possono anche essere salvati manualmente in qualsiasi momento facendo clic con il pulsante destro del mouse sul progetto e scegliendo **IFC → Salva**.





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Project/it
