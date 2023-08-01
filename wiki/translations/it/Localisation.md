# Localisation/it
## Introduzione

**Localizzazione** è in generale il processo che fornisce un software con una interfaccia utente (GUI) multilingua. In FreeCAD è possibile impostare la lingua dell\'interfaccia utente in **Modifica → Preferenze → Generale**. FreeCAD utilizza [Qt](wikipedia:Qt_(toolkit).md) per abilitare il supporto di più lingue. Sui sistemi Unix / Linux, FreeCAD utilizza le impostazioni locali di default del sistema.



## Contribuire a tradurre FreeCAD 

Una cosa molto importante che gli utenti possono fare per contribuire a FreeCAD (se per esempio non hanno competenze di programmazione) è quella di aiutare a tradurre i suoi diversi aspetti (codice sorgente, wiki, sito Web, documentazione ecc.) in un\'altra lingua. Ecco i modi per farlo.



## Tradurre il codice sorgente di FreeCAD 

FreeCAD utilizza un sistema di traduzione in linea collaborativo di terze parti chiamato [Crowdin](https://crowdin.net).

<img alt="" src=images/Logo-crowdin.png  style="width:320px;">

È un software proprietario ma gratuito per i progetti [FOSS](https://en.wikipedia.org/wiki/Free_and_open-source_software). Sotto ci sono le istruzioni su come usarlo:

-   Andare alla pagina [Traduzione del progetto FreeCAD](http://crowdin.net/project/freecad) in Crowdin.
-   Accedere creando un nuovo profilo, o utilizzando un account di terze parti (GitHub, GitLab, GMail etc\...).
-   Fare clic sulla lingua su cui si desidera lavorare.
-   Iniziare a tradurre facendo clic sul pulsante **Traduci** accanto a uno dei file. Ad esempio, su **FreeCAD.ts** che contiene le stringhe di testo per la GUI principale di FreeCAD.
-   Si può convalidare le traduzioni esistenti, oppure è possibile crearne di proprie.

{{Message|Se si partecipa alla traduzione di FreeCAD, e si desidera essere informati prima della pubblicazione di una prossima versione che è il momento di rivedere la propria traduzione, si prega di iscriversi a uno dei team di traduzione di FreeCAD in Crowdin}}.


**Nota:**

I dettagli su come utilizzare crowdin possono essere trovati nella pagina [Amministrazione di Crowdin](Crowdin_Administration.md).



## Traduzione degli ambienti esterni 

Vedere [Traduzione di un ambiente esterno](Translating_an_external_workbench/it.md).



## Preferenze di FreeCAD per i traduttori 

A partire da FreeCAD 0.20, le seguenti variabili possono essere aggiunte manualmente alla sezione BaseApp/Preferences/General del file user.cfg per facilitare lo sviluppo di nuove traduzioni:

**AdditionalLanguageDomainEntries** - per aggiungere lingue completamente nuove a FreeCAD, che non sono attualmente supportate dal codice sorgente, è possibile utilizzare questa preferenza utente per aggiungere all\'elenco delle lingue disponibili. Il formato delle lingue è \"Language Name\"=\"codice\"; Per esempio:

    <FCText Name="AdditionalLanguageDomainEntries">"Esperanto"="eo";"French"="fr";</FCText>

**AdditionalTranslationsDirectory** - aggiunge una directory aggiuntiva per FreeCAD per cercare i file \*.qm. Questa posizione avrà la precedenza su \$userAppDataDir/translations e \$resourceDir/translations. Per esempio:

    <FCText Name="AdditionalTranslationsDirectory">C:/Users/FreeCADUser/TestTranslations</FCText>



## Tradurre il wiki 

Questo wiki ospita molti contenuti, la maggior parte dei quali costruisce il manuale. È possibile sfogliare la documentazione a partire dalla [Pagina principale](Main_Page/it.md), o dare un\'occhiata al [Sommario](Online_Help_Toc/it.md) del manuale utente.

Per tradurre il wiki, si deve disporre dei permessi di modifica del wiki; vedere [Come si può ottenere il permesso di modificare il wiki?](Frequently_asked_questions/it#Come_si_può_ottenere_il_permesso_di_modificare_il_wiki?.md).

È necessario avere una conoscenza di base sulla formattazione dello stile wiki e sulle linee guida generali del wiki di FreeCAD, perché durante la traduzione bisogna sapere cosa fare con alcuni tag. Potete trovare queste informazioni in [WikiPages](WikiPages.md) (en).



### Plugin Mediawiki Translation 

Quando il Wiki è stato spostato da SourceForge, [Yorik](User_Yorik.md) ha installato un [MediaWiki\'s plugin di traduzione](http://www.mediawiki.org/wiki/Help:Extension:Translate) che facilita la traduzione delle pagine. I vantaggi del plugin di traduzione sono che, ad esempio, ora può essere tradotto anche il titolo della pagina, che tiene traccia delle traduzioni, notifica se la pagina originale è stata aggiornata, e mantiene le traduzioni sincronizzate con la pagina originale inglese.

Lo strumento è documentato in [Help:Extension:Translate](http://www.mediawiki.org/wiki/Help:Extension:Translate), ed è parte di [MediaWiki Language Extension Bundle](http://www.mediawiki.org/wiki/MediaWiki_Language_Extension_Bundle).

Per sapere come preparare rapidamente una pagina per la traduzione e attivare il plugin, si prega di leggere [Page translation example](http://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example). In sostanza, una coppia di tag

    &lt;translate&gt; ... &lt;/translate&gt;

deve circondare l\'intera pagina per attivare il sistema di traduzione e la pagina deve essere contrassegnata per la traduzione.

Per vedere un esempio di come funziona lo strumento di traduzione, visitare la [Pagina principale](Main_Page/it.md). Si vedrà una barra della lingua generata automaticamente in alto. Cliccare su [Deutsch](Main_Page/de.md) (tedesco), si andrà a [Main_Page/de](Main_Page/de.md). Proprio sotto il titolo, \"Hauptseite\" (in inglese \"Main Page\"), si può leggere , XX è la percentuale corrente di traduzione. Fare clic su \"Traduci\" nella parte superiore della pagina per avviare l\'utilità di traduzione per aggiornare, correggere e rivedere la traduzione esistente.

Ora se si va nella pagina [Main Page](Main_Page.md), si nota che quando la pagina viene contrassegnata per la traduzione non è possibile modificarla direttamente, ma che si deve passare attraverso l\'utility di traduzione.

Quando si aggiungono nuovi contenuti, prima deve essere creata la pagina inglese, e poi la pagina inglese può essere tradotta in un\'altra lingua. Se qualcuno vuole cambiare o aggiungere dei contenuti in una pagina esistente, deve farlo nella pagina inglese, marcarla per la traduzione e poi tradurre i contenuti editati.

Se non siete sicuri su come procedere, non esitate a chiedere aiuto nel [Development → Wiki subforum](https://forum.freecadweb.org/viewforum.php?f=21) o nel [specific language subforum](https://forum.freecadweb.org/viewforum.php?f=11) del [FreeCAD forum](http://forum.freecadweb.org).



### Note importanti 

Ogni utente del wiki che dispone delle autorizzazioni \"Editor\" è in grado di avviare l\'utilità di traduzione per scrivere, salvare e rivedere le traduzioni.

Tuttavia, solo gli utenti con permessi di \"Amministratore\" possono contrassegnare le pagine per la traduzione. Una pagina che non è stata contrassegnata per la traduzione non fa uso dell\'estensione di traduzione e non è sincronizzata correttamente con le informazioni in inglese.

Anche la barra laterale (il menu di navigazione a sinistra) è traducibile, ma solo gli amministratori possono modificare questo elemento del sito. Si prega di seguire le istruzioni dedicate a questo nella pagina [Tradurre la Sidebar](Localisation_Sidebar/it.md).

La prima volta che una pagina viene passata al nuovo sistema di traduzione perde tutte le sue vecchie traduzioni \"manuali\". Per recuperare una traduzione, bisogna salvare una copia offline del vecchio testo prima della conversione. Quindi si può usare questo vecchio testo tradotto per riempire le unità di traduzione nel nuovo sistema. Si può anche aprire una versione precedente dalla cronologia (pulsante History) e ottenere il vecchio testo in questo modo. Questo deve essere fatto per ogni lingua che ha una pagina tradotta.



### Tradurre la documentazione di FreeCAD 

Come da consenso generale, la pagina di riferimento nel wiki è la pagina inglese, che dovrebbe essere creata per prima. Se si desidera modificare o aggiungere contenuto a una pagina, è necessario farlo prima alla pagina inglese e solo una volta completato l\'aggiornamento, portare la modifica nella pagina tradotta.



### Vecchie istruzioni di traduzione 

++
| Queste istruzioni sono solo un background storico, mentre le pagine vengono passate al nuovo plugin di traduzione.                                                                                                                                                                                                                                                                                          |
++
| Il primo passo è **controllare se è già stata avviata la traduzione del manuale per la propria lingua** (cercare nella barra laterale sinistra, sotto \"manual\").                                                                                                                                                                                                                                          |
| In caso contrario, andare al [forum](http://forum.freecadweb.org/) e comunicare che si intende avviare una nuova traduzione, verranno create le impostazioni di base per la lingua che si desidera lavorare.                                                                                                                                                                                                |
| Vedere [Come si può ottenere il permesso di modificare il wiki?](Frequently_asked_questions/it#Come_si_può_ottenere_il_permesso_di_modificare_il_wiki?.md).                                                                                                                                                                                                                                         |
| Se la lingua è già presente, vedere quali pagine da tradurre sono ancora mancanti (sono quelle elencate in rosso). La tecnica è semplice: **entrare in una pagina rossa, copiare e incollare il contenuto della corrispondente pagina inglese, e iniziare a tradurre.**.                                                                                                                                    |
| Non dimenticare di includere tutti i tag e i modelli dalla pagina originale in inglese. Alcuni di questi modelli avranno un equivalente nella nuova lingua (per esempio, esiste un modello di Docnav in francese denominato Docnav/fr). Si deve utilizzare **una barra slash e il codice della proria lingua** in quasi tutti i collegamenti. Guardare altre pagine già tradotte per vedere come procedere. |
| Aggiungere una barra e il codice della propria lingua nelle categorie, come \[\[Category:Developer Documentation/it\]\]                                                                                                                                                                                                                                                                                     |
| Se non si è sicuri, andare nel forum e richiedere un controllo su quello che si è fatto, qualcuno vi dirà se và bene oppure no.                                                                                                                                                                                                                                                                             |
| Nelle pagine del manuale sono comunemente utilizzati due modelli (maschere standard). Questi 2 modelli hanno versioni localizzate (Template:Docnav/it, Template:it, etc\...)                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| -   [Template:GuiCommand](Template_GuiCommand.md) : è il blocco di informazioni del comando Gui in alto a destra nella documentazione del comando.                                                                                                                                                                                                                                                  |
| -   [Template:Docnav](Template_Docnav.md) : è la barra di navigazione visualizzata nella parte inferiore delle pagine, mostra le pagine precedenti e successive                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Convenzioni sui nomi delle pagine**                                                                                                                                                                                                                                                                                                                                                                       |
| Si prega di prendere atto che, a causa di limitazioni in Sourceforge al motore MediaWiki, è necessario che tutte le pagine tradotte mantengano il nome originale in inglese della pagina corrispondente, con l\'aggiunta di uno slash e del codice della lingua.                                                                                                                                            |
| Per esempio, la pagina tradotta di **About FreeCAD** deve essere **About Freecad/it** in italiano, **About FreeCAD/pl** in polacco, etc. Il motivo è semplice: in questo modo se i traduttori interrompono il lavoro, gli amministratori del wiki, che non parlano tutte le lingue, sanno di quali pagine si tratta. Ciò facilita la manutenzione ed evita di perdere delle pagine.                         |
| Se si desidera che il modello Docnav mostri pagine collegate nella propria lingua, è possibile utilizzare **redirect pages**. Esse sono sostanzialmente collegate alla pagina vera e propria. Ecco un esempio con la pagina in francese di *About FreeCAD*.                                                                                                                                                 |
| \* La pagina **About FreeCAD/fr** è la pagina con il contenuto                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| -   La pagina **À propos de FreeCAD** contiene contiene questo codice:                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| #REDIRECT [[About FreeCAD/fr]]                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| -   Nella pagina About FreeCAD/fr, il codice Docnav sarà simile a questo:                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| {{docnav/fr|Bienvenue sur l'aide en ligne|Fonctionnalités}}                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| La pagina \"Bienvenue sur l\'aide en ligne\" reindirizza a Online Help Startpage/fr, e la pagina \"Fonctionnalités\" reindirizza a Feature list/fr.                                                                                                                                                                                                                                                         |
++



## Tradurre il sito Web di FreeCAD 

La traduzione del sito Web di FreeCAD viene ora eseguita tramite [Crowdin](https://crowdin.com/translate/freecad/561/en-en). Il file si chiama **homepage.po**.



## Sviluppo - Come aggiungere la localizzazione 

Questa sezione è per gli sviluppatori che desiderano aggiungere la localizzazione al loro codice.



### Preparare i moduli di FreeCAD/master per la traduzione 

Queste sono le parti del processo di traduzione di FreeCAD:

-   estrarre le stringhe di testo dal codice sorgente nei file \*.ts
-   caricare i file \*.ts in [FreeCAD Crowdin](http://crowdin.net/project/freecad).
-   tradurre le stringhe all\'interno di Crowdin
-   estrarre i file \*.ts nuovi o modicati da Crowdin
-   convertire i file \*.ts in file \*.qm e aggiornare il file \*.qrc di ogni modulo
-   aggiornare FreeCAD master

Tutti i passaggi precedenti sono eseguiti dagli \"script di traduzione\" che vengono eseguiti periodicamente da un amministratore.

Preparare il modulo per la traduzione è abbastanza semplice. Innanzitutto, è necessario assicurarsi di avere una directory \"translations\" in **myModule/Gui/Resources**. Quindi aprire una finestra di terminale (o equivalente in Windows/OSX) nella directory \"translations\" e inserire il seguente comando: 
```pythonlupdate -ts myModule.ts```

Questo crea un file di traduzione vuoto. Una volta fatto ciò, è necessario assicurarsi che gli script di traduzione siano aggiornati come in questa [pull request](https://github.com/FreeCAD/FreeCAD/pull/810).

Tutto quello che segue va in automatico per quanto riguarda lo sviluppatore. L\'amministratore estrarrà le stringhe di testo, i traduttori le tradurranno, quindi l\'amministratore estrarrà le traduzioni e aggiornerà FreeCAD/master.



### Preparare il proprio modulo o la macro per la traduzione 

I moduli o le macro di terze parti vengono tradotti più o meno allo stesso modo, tranne per il fatto che si deve eseguire parte del lavoro da solo. Questa [discussione del forum](https://www.forum.freecadweb.org/viewtopic.php?f=3&t=25180) descrive i dettagli.

Aggiornamento: vedere [Traduzione di un ambiente di lavoro esterno](Translating_an_external_workbench/it.md)



### Precedenti tecniche di traduzione dei moduli 

[Vecchi metodi di localizzazione](Localization_Older_Methods/it.md) descrive in dettaglio l\'uso di strumenti di traduzione come Qt Linguist, lupdate, lrelease, pylupdate4, ecc. La maggior parte di questi strumenti non sono più richiesti per i moduli FreeCAD/master, ma può essere utile conoscerli per la preparazione e l\'aggiornamento di moduli di terze parti.



## Aggiornamento automatico delle traduzioni in Crowdin 

Attualmente i manutentori di FreeCAD utilizzano l\'API Crowdin tramite [Crowdin Scripts](Crowdin_Scripts/it.md) per eseguire il pull e il push delle traduzioni in Crowdin e di nuovo nel repository Github. L\'API di Crowdin offre ai manutentori di FreeCAD la possibilità di automatizzare aspetti del flusso di lavoro di traduzione del progetto, per maggiori informazioni fare riferimento alla [Documentazione dell\'API di Crowdin](https://support.crowdin.com/api/api-integration-setup/).



## Pagine correlate 

-   [Amministrazione di Crowdin](Crowdin_Administration/it.md)
-   [Crowdin Scripts](Crowdin_Scripts/it.md)

## Scripting


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics.md).

Per ottenere un dizionario con le lingue supportate dall\'interfaccia di FreeCAD, utilizzare il metodo `supportedLocales` del modulo `FreeCADGui`.


```python
locales = FreeCADGui.supportedLocales()
```

Dopo l\'esecuzione `locales` conterrà:


```python
{'English': 'en', 'Afrikaans': 'af', 'Arabic': 'ar', 'Basque': 'eu', 'Catalan': 'ca', 'Chinese Simplified': 'zh-CN', 'Chinese Traditional': 'zh-TW', 'Croatian': 'hr', 'Czech': 'cs', 'Dutch': 'nl', 'Filipino': 'fil', 'Finnish': 'fi', 'French': 'fr', 'Galician': 'gl', 'German': 'de', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Kabyle': 'kab', 'Korean': 'ko', 'Lithuanian': 'lt', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt-PT', 'Portuguese, Brazilian': 'pt-BR', 'Romanian': 'ro', 'Russian': 'ru', 'Slovak': 'sk', 'Slovenian': 'sl', 'Spanish': 'es-ES', 'Swedish': 'sv-SE', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Valencian': 'val-ES', 'Vietnamese': 'vi'}
```

Per ottenere la lingua dell\'interfaccia corrente usa il metodo `getLocale` dello stesso modulo:


```python
locale = FreeCADGui.getLocale()
```

Se la lingua corrente è l\'inglese `locale` conterrà:


```python
'English'
```

Per ottenere il [language code](https://support.crowdin.com/api/language-codes/) corrispondente utilizzare:


```python
locale = FreeCADGui.supportedLocales()[Gui.getLocale()]
```

Se la lingua corrente è l\'inglese il risultato sarà:


```python
'en'
```

Per impostare la lingua dell\'interfaccia corrente utilizzare il metodo `setLocale` dello stesso modulo. È possibile specificare la lingua o il codice della lingua:


```python
FreeCADGui.setLocale('Russian')
FreeCADGui.setLocale('ru')
```



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Wiki](Category_Wiki.md) > Localisation/it
