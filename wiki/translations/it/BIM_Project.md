---
- GuiCommand:Addon/it
   Name:BIM_Project
   Name/it:Progetto BIM
   Workbenches:[BIM](BIM_Workbench/it.md)
   Addon:BIM
   MenuLocation:Gestione → Gestione progetto...
---

# BIM Project/it

## Descrizione

<img alt="" src=images/BIM_project_screenshot.png  style="width:1024px;">

La finestra di dialogo di impostazione del progetto è una finestra di dialogo della procedura guidata che consente di creare un set di base di oggetti guida nel documento corrente o in un nuovo documento, che è di aiuto all\'inizio della modellazione di un progetto BIM.

La finestra di dialogo di impostazione del progetto può creare:

-   Un nuovo [documento](Document_structure/it.md). In alternativa, gli altri oggetti verranno creati nel documento attualmente aperto.
-   Un [sito](Arch_Site/it.md). L\'oggetto Sito rappresenta un pezzo di terreno in cui viene localizzato il progetto. È possibile dargli una serie di proprietà utili, come l\'indirizzo e le coordinate terrestri. Al momento della creazione, il sito è solo un contenitore vuoto per altri oggetti BIM, ma in seguito ad esso può essere allegato un oggetto 3D che rappresenta il terreno reale.
-   Un [edificio](Arch_Building/it.md). L\'oggetto Edificio è un contenitore per tutti gli oggetti BIM che apparterranno a uno stesso edificio. È possibile definire un tipo di edificio e dargli delle dimensioni rettangolari grossolane, che saranno rappresentate come un rettangolo disegnato sul piano (X,Y).
-   Un set di [assi](Arch_Axis/it.md), definendo il loro numero e la loro spaziatura. Gli assi vengono utilizzati come linee guida per allineare oggetti 2D e 3D. Questi assi possono essere modificati e in seguito essere introdotti nuovi assi.
-   Un set di [Parti di edificio](Arch_BuildingPart/it.md) per rappresentare i livelli. Le Parti di edificio sono oggetti contenitori BIM generici che possono essere utilizzati per raggruppare altri oggetti BIM in un numero di modi significativi, ad esempio componenti ripetibili o livelli di costruzione.
-   Un set di [gruppi](Std_Group/it.md) di default all\'interno di ogni livello. I gruppi possono essere utilizzati per organizzare gli oggetti BIM in categorie più descrittive, come \"Muri\" o \"Colonne\". Non hanno alcun impatto sul modello stesso, ma spesso aiutano a rendere più chiara la struttura del modello quando contiene molti oggetti.

### Modelli

Lo strumento Progetto supporta due tipi di modelli:

Dopo aver riempito le diverse opzioni, il contenuto della procedura guidata di installazione del progetto BIM può essere **salvato** come modello. Questi modelli possono essere \"ripristinati\" e adattati in un secondo momento. I modelli di progetto sono memorizzati come file di testo nella cartella utente di FreeCAD.

In alternativa, si può salvare il contenuto del documento corrente come modello. Ciò salva il documento attualmente aperto come un file standard **.FCStd**, ma include anche le impostazioni BIM aggiuntive come il piano di lavoro corrente o le unità correnti. Utilizzando in qualsiasi momento l\'opzione **ripristina**, il contenuto di quel file modello verrà unito al documento attivo e verranno applicate tutte le impostazioni in esso contenute.



---
![](images/Right_arrow.png) [documentation index](../README.md) > BIM Project/it
