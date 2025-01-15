# WikiPages/it
Questa pagina è un\'estensione della pagina [Help:Editing](Help_Editing.md) e fornisce linee guida comuni per scrivere e aggiornare la documentazione wiki di FreeCAD. Riassume diverse discussioni e sessioni di brainstorming



## Prima di iniziare 

-   Questa documentazione wiki è basata su [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki), lo stesso software con cui è realizzata [Wikipedia](https://en.wikipedia.org/wiki/Main_Page). Se si ha contribuito a Wikipedia, modificare le pagine wiki di FreeCAD dovrebbe essere facile.
-   Contrariamente a Wikipedia, la wiki di FreeCAD è protetta da scrittura per evitare spam. È necessario richiedere un account [sul forum](http://forum.freecadweb.org/viewtopic.php?f=21&t=6830).
-   Se non si ha mai utilizzato il software wiki prima, leggere [Help:Editing](Help_Editing.md) per acquisire familiarità con il markup utilizzato.
-   Per un utilizzo avanzato del software wiki, vedere [MediaWiki Help:Contents](https://www.mediawiki.org/wiki/Help:Contents). Non tutte le funzionalità di MediaWiki sono disponibili in questo wiki di FreeCAD, ma molte lo sono.
-   Si è intenzionati a mantenere la documentazione facile da leggere, quindi si dovrebbe evitare di utilizzare funzionalità complesse. Mantenerlo semplice.
-   Utilizzare una sandbox per testare il codice, ad esempio, [FreeCADDocu:Sandbox](FreeCADDocu_Sandbox.md) o una pagina personale con il proprio nome [Sandbox:Yourname](Sandbox_Yourname.md). Le pagine Sandbox devono essere inserite nella categoria Sandbox. Questo viene fatto aggiungendo [[Category:Sandbox]] in fondo al codice wiki.
-   Si prega di fare attenzione alle traduzioni. Il wiki di FreeCAD utilizza il supporto della traduzione automatizzata per fornire pagine in molte lingue. Per ogni pagina possono esistere versioni in più lingue. In molte pagine ci saranno tag come <translate>...</translate> e molti tag singoli come . Questi ultimi contrassegnano le cosiddette unità di traduzione e vengono creati dal sistema di traduzione, non andrebbero mai creati manualmente. Collegano i titoli e i paragrafi alle loro versioni tradotte. Non vanno cambiati perché ciò distruggerebbe i collegamenti. È comunque possibile spostare paragrafi o modificare il testo purché i tag rimangano con essi. Se si rimuove un\'intestazione o un paragrafo andrebbe rimosso anche il tag che gli appartiene. Tenere presente che le modifiche ai titoli e ai paragrafi esistenti influiscono sulle traduzioni esistenti. Le modifiche dovrebbero valerne la pena. Non preoccuparsi di aggiungere nuovo materiale perché il sistema aggiungerà automaticamente i nuovi tag dopo le modifiche. Per ulteriori informazioni vedere [Localizzazione](Localisation/it.md) e la [Mediawiki:Extension:Translate pagina originale](https://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example).



## Linee guida generali 



### Descrizioni concise 

Quando si descrive FreeCAD si deve cercare di essere concisi e diretti ed evitare ripetizioni. Descrivere cosa *fa* FreeCAD, non cosa *non fa* FreeCAD. Evitare anche espressioni colloquiali come \"una coppia\". Utilizzare \"alcuni\" quando si ha a che fare con un numero indeterminato o specificare la quantità corretta.

Descrizione errata
:   [Ambiente PartDesign](PartDesign_Workbench/it.md): PartDesign è un ambiente di lavoro per la progettazione di parti che mira a fornire strumenti per la modellazione di parti solide complesse.





Descrizione corretta
:   [Ambiente PartDesign](PartDesign_Workbench/it.md): mira a fornire strumenti per la modellazione di parti solide complesse.



### Informazioni centralizzate 

Evitare di duplicare le stesse informazioni in luoghi diversi. Inserire le informazioni in una nuova pagina e collegarsi a questa pagina da altre pagine che richiedono queste informazioni.

Non utilizzare la transclusione delle pagine ([Help:Editing#Templates and transclosure pagine](Help:Editing#Templates_and_transclosure_pages.md)), poiché ciò rende difficile la traduzione del wiki. Utilizzare solo i modelli descritti di seguito in [#Templates](#Templates.md).



### Stile

I modelli vengono utilizzati per definire lo stile delle pagine della guida. Conferiscono alla documentazione un aspetto coerente. C\'è un modello per i comandi di menu, **File → Salva**, un modello per definire lo stile dei tasti da premere, **Shift**, per mostrare un valore booleano, `True`, ecc. Per favore acquisire familiarità con la sezione [#Templates](#Templates.md) prima di scrivere pagine di aiuto.



### Flag temporanei 

Se si sta lavorando su una pagina di grandi dimensioni è consigliabile contrassegnare la pagina come work in progress o come incompiuta. Ciò garantisce che gli amministratori wiki non contrassegnino la tua pagina come pronta per la traduzione mentre la si sta ancora modificando.

Per contrassegnare una pagina, aggiungere come prima linea  o . Con  si invitano gli altri a collaborare per finire la pagina, mentre  indica che si svolgerà il lavoro da solo e che gli altri dovrebbero lasciarti un po\' di tempo.

Una volta terminato il lavoro, non dimenticare di rimuovere i flag!



## Esempi

Per acquisire rapidamente familiarità con la struttura e lo stile del wiki di FreeCAD, guardare la pagina del modello: [modello di base](GuiCommand_model/it.md).


<div class="mw-collapsible mw-collapsed toccolours">



## Struttura


<div class="mw-collapsible-content">

L\'[Hub degli utenti](User_hub/it.md) fornisce un [Sommario](Online_Help_Toc/it.md). Viene utilizzato come riferimento principale per creare automaticamente la guida offline raggiungibile da FreeCAD, nonché la documentazione PDF offline.

Il [Template:Docnav](Template_Docnav.md) viene utilizzato per collegare in sequenza le pagine, seguendo la struttura del [Sommario](Online_Help_Toc/it.md). Vedere [#Templates](#Templates.md) per un elenco di tutti i modelli.



### Nomi delle pagine 

I nomi delle pagine dovrebbero essere brevi e dovrebbero usare le maiuscole: ogni parola dovrebbe iniziare con una lettera maiuscola, a meno che non si tratti di articoli, preposizioni, congiunzioni o altre particelle grammaticali (ad esempio \'di\', \'su\', \'in\', \'a \', \'uno\', \'e\').

Nome della pagina errato:
:   Construction of AeroCompany airplanes





Nome della pagina corretto:
:   Construction of AeroCompany Airplanes

I nomi delle pagine dell\'ambiente di lavoro del livello superiore devono avere questo formato: XYZ Workbench, dove XYZ è il nome del workbench, ad esempio [PartDesign Workbench](PartDesign_Workbench/it.md). E i nomi delle pagine che descrivono i comandi (o strumenti) appartenenti a un ambiente devono avere questo formato: Comando XYZ, ad esempio [PartDesign Pad](PartDesign_Pad/it.md). Tenere presente che si dovrebbe utilizzare il nome del comando così come appare nel codice sorgente.



### Intestazioni

I titoli dei paragrafi dovrebbero essere brevi e utilizzare maiuscole e minuscole: tutte le parole, tranne la prima e i nomi propri, dovrebbero essere in minuscolo. Non si dovrebbero utilizzare le intestazioni H1 (= Heading =) nel markup della wiki, in quanto nel titolo della pagina viene aggiunto automaticamente come intestazione principale H1.



### Link

Si dovrebbe utilizzare il nome del collegamento originale per i collegamenti quando possibile. Questo rende più evidente la pagina di riferimento nella documentazione stampata oppure offline. Si prega di evitare parole prive di significato per il collegamento.

Collegamento errato
:   Per ulteriori informazioni sul disegno di oggetti 2D, fare clic [qui](Draft_Workbench/it.md).





Collegamento corretto
:   Per ulteriori informazioni sul disegno di oggetti 2D fare riferimento a [Draft](Draft_Workbench/it.md).

Il formato preferito per un collegamento è:

[Name of Page](Name_of_Page/it.md)

Tradotto

[Nom de la Page](Name_of_Page/fr.md)

Tenere presente che per la parte prima del carattere |, ovvero il link effettivo, è rilevante la distinzione tra maiuscole e minuscole. Se il nome della pagina è Name_of_page il collegamento non funzionerà se si digita Name_of_Page (P maiuscola). Prima del carattere | tutti gli spazi devono essere sostituiti da trattini bassi (_). Questo serve per aiutare i traduttori che utilizzano software di traduzione, senza i caratteri di sottolineatura il collegamento verrebbe tradotto dal software, il che è indesiderabile.

Per collegarsi a un determinato paragrafo aggiungere un segno # e le sue intestazioni al nome della pagina. Esempio:

[WikiPages](WikiPages#Links.md)

Tradotto

[WikiPages](WikiPages/fr#Liens.md)

All\'interno della stessa pagina si può omettere il nome della pagina. Esempio:

[Links](#Links.md)

Per collegarsi alla parte superiore della pagina è possibile utilizzare:

</translate>{{Top}}<translate>

Questo template dovrebbe visualizzare automaticamente il testo corretto a seconda della lingua della pagina. Un collegamento alla parte superiore della pagina è particolarmente utile per le pagine lunghe poiché consente all\'utente di tornare rapidamente al sommario. Lo si può mettere alla fine di ogni paragrafo. Assicurarsi che ci sia una riga vuota prima e dopo il template.

Collegamento a una immagine

:   <img alt="Testo facoltativo che viene mostrato quando passi il mouse sull\'immagine\|link=Draft_Wire" src=images/Draft_Wire.svg  style="width:24px;">

Per utilizzare un\'immagine come collegamento:

![](images/)

Immagine del Collegamento + testo del collegamento
:   <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Wire](Draft_Wire.md)

Se si tralascia il testo facoltativo, il collegamento stesso verrà mostrato quando si passa sull\'immagine, il che è preferibile, e si dovrebbe anche aggiungere un collegamento testuale dopo il collegamento dell\'immagine:

![](images/)_[Draft_Wire](Draft_Wire.md)



### Pagine degli Ambienti di lavoro 

Una pagina dell\'ambiente di livello superiore dovrebbe iniziare con:

-   Una descrizione dello scopo per cui viene utilizzato l\'ambiente.
-   Un\'immagine per illustrarne la descrizione.

Vedere [#Istantanee dello schermo](#Screen_capture.md) per le convenzioni su come inserire le immagini.



### Pagine dei comandi 

Le pagine dei comandi che descrivono gli strumenti dell\'ambiente di lavoro non dovrebbero essere troppo lunghe, dovrebbero solo spiegare cosa può fare un comando e cosa no, e come usarlo. Si dovrebbe ridurre al minimo le immagini e gli esempi. I tutorial si possono espandere riguardo l\'utilizzo dello strumento e fornire dettagli passo passo.

Per ulteriori dettagli, fare riferimento alla pagina dei [Modelli per la descrizione dei comandi](GuiCommand_model/it.md).



### Tutorial

Un tutorial ben scritto dovrebbe insegnare come ottenere rapidamente determinati risultati pratici. Non dovrebbe essere troppo lungo, ma dovrebbe includere immagini e istruzioni passo passo sufficienti per guidare l\'utente. Man mano che FreeCAD si evolve, i tutorial potrebbero diventare obsoleti, quindi è importante menzionare la versione di FreeCAD utilizzata o richiesta per un tutorial.

Per esempi visitare la pagina dei [Tutorial](Tutorials/it.md).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Templates


<div class="mw-collapsible-content">

Lo stile delle pagine wiki di FreeCAD si ottiene attraverso l\'uso di modelli ([Help:Editing#Templates_and_transcluding_pages](Help:Editing#Templates_and_transcluding_pages.md)). Garantiscono un aspetto standardizzato in tutte le pagine e consentono anche di rimodellare il wiki. È possibile visualizzare l\'elenco completo dei modelli definiti accedendo a [Special:PrefixIndex/Template:](Special:PrefixIndex/Template:.md). Si prega tuttavia di utilizzare solo i modelli elencati nelle tabelle seguenti. Solo in casi molto particolari si possono utilizzare direttamente i tag HTML.

Fare clic sul collegamento del modello per visualizzare le istruzioni di utilizzo di un modello e per visualizzarne l\'implementazione. I modelli sono una potente funzionalità del software MediaWiki. Si dovrebbe essere un utente wiki esperto per proporre aggiunte e modifiche ai modelli esistenti. Se implementati in modo errato, i template rendono difficile la traduzione delle pagine in altre lingue, quindi il loro utilizzo dovrebbe essere limitato alla formattazione del testo e la transclusione delle pagine dovrebbe essere evitata. Vedere [MediaWiki Help:Templates](https://www.mediawiki.org/wiki/Help:Templates) per ulteriori informazioni.



### Template semplici 

Questi template accettano un parametro semplice di testo e lo formattano con uno stile particolare.

++++
| Template                                                                                                      | Aspetto                                | Descrizione                                                                                                                                                                                                                                                                                                                   |
+===============================================================================================================+========================================+===============================================================================================================================================================================================================================================================================================================================+
| [Top](Template_Top.md)                                                                                |                         | Utilizzato per aggiungere un link che porta all\'inizio della pagina.                                                                                                                                                                                                                                                         |
|                                                                                                               | {{Top}}                                |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [Emphasis](Template_Emphasis.md)                                                                      |                         | Utilizzato per enfatizzare una parte di testo.                                                                                                                                                                                                                                                                                |
|                                                                                                               | **emphasis**                  |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [KEY](Template_KEY.md)                                                                                |                         | Utilizzato per indicare un tasto della tastiera che deve essere premuto.                                                                                                                                                                                                                                                      |
|                                                                                                               | **Alt**                            |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [ASCII](Template_ASCII.md)                                                                            |                         | Utilizzato per indicare un tasto ascii in un\'immagine (.svg) che deve essere premuto. E\' necessario fornire il carattere desiderato oppure il numero del codice ascii del carattere.                                                                                                                                        |
|                                                                                                               | {{ASCII|A}}                            |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [Button](Template_Button.md)                                                                          |                         | Utilizzato per indicare un pulsante nell\'interfaccia utente grafica che deve essere premuto.                                                                                                                                                                                                                                 |
|                                                                                                               | **Cancel**                      |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [RadioButton](Template_RadioButton.md)                                                                |                         | Utilizzato per indicare un pulsante di un\'opzione nell\'interfaccia utente grafica che deve essere {{RadioButton|TRUE|Selezionato}} o {{RadioButton|FALSE|No}}.                                                                                                                                  |
|                                                                                                               | {{RadioButton|Option}}                 |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [CheckBox](Template_CheckBox.md)                                                                      |                         | Utilizzato per indicare una casella di controllo nell\'interfaccia utente grafica che deve essere {{CheckBox|TRUE|Selezionata}} o {{CheckBox|FALSE|No}}.                                                                                                                                          |
|                                                                                                               | {{CheckBox|Option}}                    |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [SpinBox](Template_SpinBox.md)                                                                        |                         | Utilizzato per indicare una casella numerica nell\'interfaccia utente grafica che può essere modificata.                                                                                                                                                                                                                      |
|                                                                                                               | {{SpinBox|1.50}}                       |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [ComboBox](Template_ComboBox.md)                                                                      |                         | Utilizzato per indicare una casella combinata nell\'interfaccia utente grafica che può essere modificata.                                                                                                                                                                                                                     |
|                                                                                                               | {{ComboBox|Menu 1}}                    |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [LineEdit](Template_LineEdit.md)                                                                      |                         | Utilizzato per indicare un LineEdit nell\'interfaccia utente grafica che può essere modificato.                                                                                                                                                                                                                               |
|                                                                                                               | {{LineEdit|Metal Nickel (Ni)}}         |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [FALSE](Template_FALSE.md), [false](Template_false.md)                                        |                         | Utilizzato per indicare un valore booleano falso, ad esempio, come proprietà nell\'[editor delle proprietà](Property_editor/it.md). Questa è una scorciatoia. Poiché si tratta di un valore, preferire il Template [Value](Template_Value.md) {{Value|false}}                                   |
|                                                                                                               | `False`                              |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               | , {{false}}              |                                                                                                                                                                                                                                                                                                                               |
++++
| [TRUE](Template_TRUE.md), [true](Template_true.md)                                            |                         | Utilizzato per indicare un valore booleano vero, ad esempio, come proprietà nell\'[editor delle proprietà](Property_editor/it.md). Questa è una scorciatoia. Poiché si tratta di un valore, preferire Template [Value](Template_Value.md) {{Value|true}}                                        |
|                                                                                                               | `True`                               |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               | , {{true}}               |                                                                                                                                                                                                                                                                                                                               |
++++
| [MenuCommand](Template_MenuCommand.md)                                                                |                         | Utilizzato per indicare la posizione di un comando all\'interno di un particolare menu.                                                                                                                                                                                                                                       |
|                                                                                                               | **File → Save**            |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [FileName](Template_FileName.md)                                                                      |                         | Utilizzato per indicare il nome di un file o di una cartella.                                                                                                                                                                                                                                                                 |
|                                                                                                               | **File name**                 |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [SystemInput](Template_SystemInput.md)                                                                |                         | Utilizzato per indicare il testo di input digitato dall\'utente.                                                                                                                                                                                                                                                              |
|                                                                                                               | {{SystemInput|Type this text}}         |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [SystemOutput](Template_SystemOutput.md)                                                              |                         | Utilizzato per indicare l\'output di testo dal sistema.                                                                                                                                                                                                                                                                       |
|                                                                                                               | {{SystemOutput|Output text}}           |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [Incode](Template_Incode.md)                                                                          |                         | Utilizzato per includere il codice sorgente in linea con un carattere a spaziatura fissa. Dovrebbe stare in una riga.                                                                                                                                                                                                         |
|                                                                                                               | `import FreeCAD`              |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [PropertyView](Template_PropertyView.md)                                                              |                         | Utilizzato per indicare una proprietà View nell\'[editor delle proprietà](Property_editor/it.md). Esempi di proprietà di visualizzazione includono {{emphasis|Line Color}}, {{emphasis|Line Width}}, {{emphasis|Point Color}}, {{emphasis|Point Size}}, ecc.. |
|                                                                                                               | **Color**                 |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [PropertyData](Template_PropertyData.md)                                                              |                         | Utilizzato per indicare una proprietà Data nell\'[editor delle proprietà](Property_editor/it.md). Le proprietà dei dati sono diverse per i diversi tipi di oggetti.                                                                                                                                                   |
|                                                                                                               | **Position**              |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [Properties Title](Template_Properties_Title.md) / [TitleProperty](Template_TitleProperty.md) |                         | Utilizzato per indicare il titolo di un gruppo di proprietà nell\'[editor delle proprietà](Property_editor/it.md). Il titolo non verrà incluso nel sommario automatico.                                                                                                                                               |
|                                                                                                               | {{Properties_Title|Base}}              |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [Obsolete](Template_Obsolete.md)                                                                      |                         | Utilizzato per indicare che una funzionalità è diventata obsoleta nella versione di FreeCAD specificata.                                                                                                                                                                                                                      |
|                                                                                                               | {{Obsolete|0.19}}                      |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [Version](Template_Version.md)                                                                        |                         | Utilizzato per indicare che una funzionalità è stata introdotta nella versione di FreeCAD specificata.                                                                                                                                                                                                                        |
|                                                                                                               | <small>(v0.18)</small>                        |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [VersionMinus](Template_VersionMinus.md)                                                              |                         | Utilizzato per indicare che una funzionalità è disponibile nella versione di FreeCAD specificata e nelle versioni precedenti.                                                                                                                                                                                                 |
|                                                                                                               | {{VersionMinus|0.16}}                  |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [VersionPlus](Template_VersionPlus.md)                                                                |                         | Utilizzato per indicare che una funzionalità è disponibile nella versione di FreeCAD specificata e nelle versioni successive.                                                                                                                                                                                                 |
|                                                                                                               | <small>(v0.17)</small>                    |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [ColoredText](Template_ColoredText.md)                                                                |                         | Questo modello è utilizzato per colorare lo sfondo, il testo o lo sfondo e il testo. (Pagina [ColoredText](Template_ColoredText.md) per ulteriori esempi)                                                                                                                                                             |
|                                                                                                               | {{ColoredText|Colored Text}}           |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++
| [ColoredParagraph](Template_ColoredParagraph.md)                                                      |                         | Questo modello è utilizzato per colorare lo sfondo, il testo o lo sfondo e il testo di un intero paragrafo. (Pagina [ColoredParagraph](Template_ColoredParagraph.md) per ulteriori esempi)                                                                                                                            |
|                                                                                                               | {{ColoredParagraph|Colored Paragraph}} |                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                               |
++++



### Template complessi 

Questi template richiedono più parametri di input o producono un blocco di testo con un formato particolare.

++++
| Template                                                                                         | Aspetto                                                                                                                      | Descrizione                                                                                                                                                                                                                                                                                                                                          |
+==================================================================================================+==============================================================================================================================+======================================================================================================================================================================================================================================================================================================================================================+
| [Prettytable](Template_Prettytable.md)                                                   | This table                                                                                                                   | Utilizzato per formattare tabelle come questa. È possibile aggiungere ulteriori proprietà alla tabella.                                                                                                                                                                                                                                              |
++++
| [Caption](Template_Caption.md)                                                           |                                                                                                                    | Utilizzato per aggiungere una didascalia sotto un\'immagine. Può essere allineato a sinistra o al centro.                                                                                                                                                                                                                                            |
|                                                                                                  | <div style="width:400px;">                                                                                                   |                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  |                                                                                                               |                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  | 
*Some caption for an image*                                                                                        |                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  |                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  | </div>                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                      |
++++
| [Clear](Template_Clear.md)                                                               |                                                                                                                              | Utilizato per cancellare le colonne. Seguire la definizione del modello per una spiegazione dettagliata. Viene spesso utilizzato per impedire al testo di scorrere accanto a immagini non correlate.                                                                                                                                                 |
++++
| [Code](Template_Code.md)                                                                 |                                                                                                               | Utilizzato per includere esempi di codice su più righe con un carattere a spaziatura fissa. Il linguaggio predefinito è Python, ma è possibile specificare altri linguaggi.                                                                                                                                                                          |
|                                                                                                  | 
```pythonimport FreeCAD```                                                                                                 |                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  |                                                                                                                           | Il codice [Python](Python/it.md) deve aderire alle raccomandazioni generali stabilite da [PEP8: Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/). In particolare, le parentesi dovrebbero seguire immediatamente il nome della funzione e uno spazio dovrebbe seguire una virgola. Ciò rende il codice più leggibile. |
++++
| [CodeDownload](Template_CodeDownload.md)                                                 |                                                                                                               | Utilizzato per creare un collegamento su una pagina di una [macro](Macros/it.md).                                                                                                                                                                                                                                                            |
|                                                                                                  | {{CodeDownload|https://wiki.freecad.org/Main_Page|Some label}}                                                               |                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                      |
++++
| [Codeextralink](Template_Codeextralink.md)                                               |                                                                                                               | Utilizzato se il codice di una [macro](Macro/it.md) è troppo grande per essere ospitato sul Wiki. Il codice può quindi essere ospitato da qualche altra parte e il collegamento non elaborato ad esso può essere specificato con questo modello. [Addon Manager](Std_AddonMgr/it.md) utilizzerà questo collegamento.                 |
|                                                                                                  | {{Codeextralink|https://wiki.freecad.org/Main_Page}}                                                                         |                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                      |
++++
| [Fake heading](Template_Fake_heading.md)                                                 |                                                                                                               | Utilizzato per creare un\'intestazione che non verrà inclusa automaticamente nel sommario.                                                                                                                                                                                                                                                           |
|                                                                                                  | {{Fake heading|Heading|2}}                                                                                                   |                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                      |
++++
| [GuiCommand](Template_GuiCommand.md)                                                     | See [GuiCommand model](GuiCommand_model.md)                                                                          | Utilizzato per creare un riquadro con informazioni utili per documentare i comandi dell\'ambiente di lavoro (strumenti).                                                                                                                                                                                                                             |
++++
| [TutorialInfo](Template_TutorialInfo.md)                                                 | See for example [Basic modeling tutorial](Basic_modeling_tutorial.md)                                                | Utilizzato per creare un box con informazioni utili per documentare i [tutorial](Tutorials/it.md).                                                                                                                                                                                                                                           |
++++
| [Macro](Template_Macro.md)                                                               | See for example [Macro FlattenWire](Macro_FlattenWire.md)                                                            | Utilizzato per creare un box con informazioni utili per documentare le [macro](Macros/it.md).                                                                                                                                                                                                                                                |
++++
| [Docnav](Template_Docnav.md)                                                             |                                                                                                               | Utilizzato per creare una barra con frecce e collegamenti appropriati, adatto a disporre le pagine in una sequenza particolare.                                                                                                                                                                                                                      |
|                                                                                                  |                                                                                 |                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                      |
++++
| [VeryImportantMessage](Template_VeryImportantMessage.md)                                 |                                                                                                               | Utilizzato per creare una casella evidenziata con un messaggio molto importante. Utilizzare con parsimonia, solo per indicare gravi problemi nella funzionalità del software, interruzione degli strumenti e cose simili.                                                                                                                            |
|                                                                                                  | **Important Message**                                                                                   |                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                      |
++++
| [Page in progress](Template_Page_in_progress.md)                                         |                                                                                                               | Utilizzato per le pagine che sono ancora in elaborazione o che sono attualmente in fase di rielaborazione. Non dimenticarsi di rimuoverlo quando la pagina è completata.                                                                                                                                                                             |
|                                                                                                  | {{Page in progress|Page in progress}}                                                                                        |                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                      |
++++
| [UnfinishedDocu](Template_UnfinishedDocu.md)                                             |                                                                                                               | Utilizzato per creare una casella evidenziata che indica una pagina di documentazione incompleta.                                                                                                                                                                                                                                                    |
|                                                                                                  |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                      |
++++
| [Softredirect](Template_Softredirect.md)                                                 |                                                                                                                              | Utilizzato al posto del reindirizzamento normale, quando si sta reindirizzando a una pagina speciale (come Media: o Categoria:), nei quali casi il reindirizzamento normale è disabilitato.                                                                                                                                                          |
++++
| [Quote](Template_Quote.md)                                                               |                                                                                                               | Utilizzato per creare una casella di testo con una citazione letterale e un riferimento.                                                                                                                                                                                                                                                             |
|                                                                                                  | {{Quote|text=Cry "Havoc" and let slip the dogs of war.|sign=William Shakespeare|source=''Julius Caesar'', act III, scene I}} |                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                      |
++++
| [Userdocnavi](Template_Userdocnavi.md), [Powerdocnavi](Template_Powerdocnavi.md) |                                                                                                                              | Utilizzati per creare caselle di navigazione per la documentazione per l\'utente, la documentazione per utenti esperti e la documentazione per sviluppatori. Ciò consente di saltare rapidamente tra le diverse sezioni della documentazione. Inoltre inseriscono la pagina corrispondente nella categoria corretta.                                 |
++++


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



## Grafica


<div class="mw-collapsible-content">

Immagini e screenshot sono necessari per produrre una documentazione completa di FreeCAD. Sono particolarmente utili per illustrare esempi e tutorial. Le immagini devono essere mostrate nella loro dimensione originale, in modo che presentino dettagli sufficienti e siano leggibili se includono testo. Le immagini [Bitmap](bitmap/it.md) non devono essere ridimensionate.

Evitare le immagini animate (GIF) nelle pagine generiche di aiuto. Le animazioni e i video devono essere riservati ai tutorial non destinati a essere utilizzati come documentazione PDF offline.

Le immagini possono essere caricate tramite la pagina [Special:Upload](Special:Upload/it.md).



### Nome

Dare nomi significativi alle proprie immagini. Se si ha un\'immagine che mostra le caratteristiche di un particolare comando, si dovrebbe usare il nome di quel comando con `_example` alla fine. Ad esempio per il comando [Draft Offset](Draft_Offset/it.md) l\'immagine dovrebbe essere chiamata `Draft_Offset_example.png`.



### Istantanee dello schermo 

Le dimensioni consigliate per le istantanee dello schermo sono:

-   Nativo 400x200 (o larghezza=400 e altezza\<=200), per le pagine di [riferimento dei comandi](GuiCommand_model/it.md), per consentire all\'immagine di adattarsi alla parte sinistra della pagina e per altre istantanee standard.
-   Nativo 600x400 (o larghezza=600 e altezza\<=400), per le pagine di [riferimento dei comandi](GuiCommand_model.md), quando si ha davvero bisogno di un\'immagine più grande e si consente comunque all\'immagine di adattarsi alla parte sinistra della pagina e per altre istantanee standard.
-   1024x768 nativo (o larghezza=1024 e altezza\<=768), solo per immagini a schermo intero.
-   Sono possibili taglie più piccole quando si mostrano i dettagli.
-   Evitare immagini con risoluzioni maggiori, poiché non saranno molto trasferibili su altri tipi di display o sulla documentazione PDF stampata.

Non si dovrebbe dipendere da una configurazione personalizzata del proprio desktop o sistema operativo quando si creano schermate e si dovrebbero utilizzare le impostazioni visive predefinite dell\'interfaccia di FreeCAD quando possibile.

Per creare uno screenshot si possono utilizzare le opzioni fornite dal proprio sistema operativo, oppure una di queste macro: <img alt="" src=images/Snip.png  style="width:24px;"> [Macro Snip](Macro_Snip/it.md) e [24px ](Image:Macro_Screen_Wiki.png.md) [Macro Screen Wiki](Macro_Screen_Wiki/it.md).



### Testo

Per facilitare le traduzioni della documentazione, cercare di evitare screenshot che contengono testo. Se non lo si può evitare, prendere in considerazione l\'idea di acquisire screenshot separati dell\'interfaccia e della [Vista 3D](3D_view/it.md). L\'immagine della vista 3D può essere riutilizzata in ogni traduzione, mentre un traduttore può, se necessario, acquisire uno screenshot dell\'interfaccia localizzata.



### Icone e grafica 

Fare riferimento alla pagina [Artwork](Artwork/it.md) per tutti gli elementi grafici e le icone che sono state create per FreeCAD e che possono essere utilizzate anche nelle pagine di documentazione. Se si desidera contribuire alle icone, leggere le [Linee guida per le Artwork](Artwork_Guidelines/it.md).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



## Traduzioni


<div class="mw-collapsible-content">

Per consenso generale, la pagina di riferimento nel wiki è la pagina in inglese, che dovrebbe venire creata per prima. Se si desidera modificare o aggiungere contenuto a una pagina, si dovrebbe farlo prima sulla pagina inglese e, solo una volta completato l\'aggiornamento, trasferire la modifica sulla pagina tradotta.

Il wiki di FreeCAD supporta un\'estensione di traduzione che consente di gestire più facilmente le traduzioni tra le pagine; per i dettagli, vedere [Tradurre il wiki](Localisation/it#Tradurre_il_wiki.md).

Altre risorse utili sono:

-   [ISO language codes](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) per identificare il codice di due lettere per una particolare lingua in cui si desidera tradurre.
-   [Google Translate](http://translate.google.com/) per l\'aiuto con le traduzioni.
-   [Deepl translator](https://www.deepl.com/translator) per l\'aiuto con le traduzioni.



## Alcuni consigli per i traduttori 



### Tradurre GuiCommand 

    {{GuiCommand
    |Name=FEM EquationFlux
    |MenuLocation=Solve → Flux equation
    |Workbenches=[FEM](FEM_Workbench.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM tutorial](FEM_tutorial.md)
    }}

Tradotto:

    {{GuiCommand/fr
    |Name=FEM EquationFlux
    |Name/fr=FEM Équation d'écoulement
    |MenuLocation=Solveur → Équation de flux
    |Workbenches=[Atelier FEM](FEM_Workbench/fr.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM Tutoriel](FEM_tutorial/fr.md)
    }}



### Tradurre navi 

    {{FEM_Tools_navi}}

Tradotto:

    {{FEM_Tools_navi/fr}}



### Tradurre link 

    [Part Workbench](Part_Workbench.md)

Tradotto:

    [Atelier Part](Part_Workbench/fr.md)



### Tradurre Docnav 

    

Tradotto:

    

Esempio con le icone:

    

Tradotto:

    


</div>


</div>



## Creare, rinominare ed eliminare le pagine 



### Creare pagine 

Prima di creare una nuova pagina si dovrebbe prima verificare se esiste già una pagina simile. In questo caso, di solito è meglio prima modificare la pagina esistente. In caso di dubbi, aprire prima un topic nel [forum delle Wiki](https://forum.freecadweb.org/viewforum.php?f=21).

Per creare una nuova pagina, effettuare una delle seguenti operazioni:

-   Visitare l\'URL con il nome della pagina desiderata, ad esempio: https://wiki.freecadweb.org/My_New_Page, e fare clic su \'create this page\'.
-   Effettuare una ricerca nel wiki per il nome della pagina e fare clic sul testo in rosso in \'Create the page \"My New Page\" on this wiki!\'.



### Rinominare le pagine 

Poiché FreeCAD è un progetto in costante sviluppo, a volte è necessario rivedere il contenuto del wiki. Se i nomi dei comandi vengono modificati nel codice sorgente, anche le pagine wiki che li documentano dovranno essere rinominate. Questo può essere fatto solo dagli amministratori del wiki. Per informarli, aprire un argomento nel [Forum delle Wiki](https://forum.freecadweb.org/viewforum.php?f=21) ed elencare l\'operazione di ridenominazione necessaria in questo modulo:

    old name         new name
    Old_page_name_1  New_page_name_1
    Old_page_name_2  New_page_name_2
    ...



### Eliminare file e pagine 

Nel caso in cui sia necessario eliminare un file, andare alla relativa pagina (https://www.freecadweb.org/wiki/File:***.***) e modificarlo. Non importa se la pagina è vuota o meno, aggiungere quanto segue come primo elemento: {{Delete}} e direttamente sotto descrivere il motivo per cui la pagina dovrebbe essere eliminata. Inoltre, aprire un topic nel [Forum delle Wiki](https://forum.freecadweb.org/viewforum.php?f=21).

Per le pagine la procedura è la stessa.



## Discussioni

Il [Development/Wiki subforum](http://forum.freecadweb.org/viewforum.php?f=21) nel [Forum di FreeCAD](https://forum.freecadweb.org) fornisce uno spazio dedicato per discutere argomenti wiki, l\'aspetto delle wiki e qualsiasi altra cosa relativa al wiki. Indirizzare lì le proprie domande e i suggerimenti.



## Terminologia - politica di denominazione 



### Inglese

Vedere il [Glossario](Glossary/it.md).



### Altre lingue 

-   [Italiano](Italian_Translation.md)
-   [Français](French_Translation.md)
-   [Deutsch](German_Translation.md)
-   [Polish](Polish_Translation.md)
-   [Spanish](Spanish_Translation.md)



---
⏵ [documentation index](../README.md) > [Documentation](Category_Documentation.md) > [Wiki](Category_Wiki.md) > [Wiki Documentation](Category_Wiki%20Documentation.md) > [Administration](Category_Administration.md) > [FEM](Category_FEM.md) > WikiPages/it
