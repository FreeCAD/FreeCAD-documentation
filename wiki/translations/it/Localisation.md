# Localisation/it
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}


<div class="mw-translate-fuzzy">

## Introduzione

**Localizzazione** è in generale il processo che fornisce un software con una interfaccia utente (GUI) multilingua.

In FreeCAD è possibile impostare la lingua dell\'interfaccia utente in **Modifica → Preferenze → Generale**.

FreeCAD utilizza [Qt](wikipedia:Qt_(toolkit).md) per abilitare il supporto di più lingue. Sui sistemi Unix / Linux, FreeCAD utilizza le impostazioni locali di default del sistema.


</div>

**Localisation** is in general the process of providing a Software with a multiple language user interface. In FreeCAD you can set the language of the user interface under **Edit → Preferences → General**. FreeCAD uses [Qt](wikipedia:Qt_(toolkit).md) to enable multiple language support. On Unix/Linux systems, FreeCAD uses the current locale settings of your system by default.

## Contribuire a tradurre FreeCAD 


<div class="mw-translate-fuzzy">

Una cosa molto importante che gli utenti possono fare per contribuire a FreeCAD (se per esempio non hanno competenze di programmazione) è quella di aiutare a tradurre i suoi diversi aspetti (codice sorgente, wiki, sito Web, documentazione ecc.) in un\'altra lingua. Ecco i modi per farlo.


</div>


<div class="mw-translate-fuzzy">

## Tradurre il codice sorgente di FreeCAD 

FreeCAD utilizza un sistema di traduzione in linea collaborativo di terze parti chiamato [Crowdin](https://crowdin.net).


</div>

FreeCAD utilizes a third party collaborative on-line translation system called [Crowdin](https://crowdin.net).

<img alt="" src=images/Logo-crowdin.png  style="width:320px;">

È un software proprietario ma gratuito per i progetti FOSS. Sotto ci sono le istruzioni su come usarlo:

-   Andare alla pagina [Traduzione del progetto FreeCAD](http://crowdin.net/project/freecad) in Crowdin.
-   Accedere creando un nuovo profilo, o utilizzando un account di terze parti (GitHub, GitLab, GMail etc\...).
-   Fare clic sulla lingua su cui si desidera lavorare.
-   Iniziare a tradurre facendo clic sul pulsante **Traduci** accanto a uno dei file. Ad esempio, su {{FileName|FreeCAD.ts}} che contiene le stringhe di testo per la GUI principale di FreeCAD.
-   Si può convalidare le traduzioni esistenti, oppure è possibile crearne di proprie.

{{Message|Se si partecipa alla traduzione di FreeCAD, e si desidera essere informati prima della pubblicazione di una prossima versione che è il momento di rivedere la propria traduzione, si prega di iscriversi a uno dei team di traduzione di FreeCAD in Crowdin}}.


**Note:**

Details on how to use crowdin can be found on the [Crowdin Administration](Crowdin_Administration.md) page.

## Traduzione degli ambienti esterni 

Vedere [Traduzione di un ambiente esterno](Translating_an_external_workbench/it.md)

## FreeCAD Preferences for Translators 

Starting with FreeCAD 0.20, the following variables can be manually added to the BaseApp/Preferences/General section of the user.cfg file to assist with the development of new translations:

**AdditionalLanguageDomainEntries** - to add entirely new languages to FreeCAD that are not currently supported by the source code, you can use this user preference to add to the list of available languages. The format of the languages is \"Language Name\"=\"code\"; for example:

    <FCText Name="AdditionalLanguageDomainEntries">"Esperanto"="eo";"French"="fr";</FCText>

**AdditionalTranslationsDirectory** - add an additional directory for FreeCAD to search for \*.qm files. This location will take precedence over \$userAppDataDir/translations and \$resourceDir/translations. For example:

    <FCText Name="AdditionalTranslationsDirectory">C:/Users/FreeCADUser/TestTranslations</FCText>

## Tradurre il wiki 

Questo wiki ospita molti contenuti, la maggior parte dei quali costruisce il manuale. È possibile sfogliare la documentazione a partire dalla [Pagina principale](Main_Page/it.md), o dare un\'occhiata al [Sommario](Online_Help_Toc/it.md) del manuale utente.


<div class="mw-translate-fuzzy">

Per poter tradurre nel wiki, è necessario [richiedere l\'autorizzazione](FAQ#How_can_I_get_edit_permission_on_the_wiki.3F.md).


</div>

È necessario avere una conoscenza di base sulla formattazione dello stile wiki e sulle linee guida generali del wiki di FreeCAD, perché durante la traduzione bisogna sapere cosa fare con alcuni tag. Potete trovare queste informazioni in [WikiPages](WikiPages.md) (en).

### Plugin Mediawiki Translation 

Quando il Wiki è stato spostato da SourceForge, [Yorik](User_Yorik.md) ha installato un [MediaWiki\'s plugin di traduzione](http://www.mediawiki.org/wiki/Help:Extension:Translate) che facilita la traduzione delle pagine. I vantaggi del plugin di traduzione sono che, ad esempio, ora può essere tradotto anche il titolo della pagina, che tiene traccia delle traduzioni, notifica se la pagina originale è stata aggiornata, e mantiene le traduzioni sincronizzate con la pagina originale inglese.

Lo strumento è documentato in [Help:Extension:Translate](http://www.mediawiki.org/wiki/Help:Extension:Translate), ed è parte di [MediaWiki Language Extension Bundle](http://www.mediawiki.org/wiki/MediaWiki_Language_Extension_Bundle).

Per sapere come preparare rapidamente una pagina per la traduzione e attivare il plugin, si prega di leggere [Page translation example](http://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example). In sostanza, una coppia di tag

    &lt;translate&gt; ... &lt;/translate&gt;

deve circondare l\'intera pagina per attivare il sistema di traduzione e la pagina deve essere contrassegnata per la traduzione.


<div class="mw-translate-fuzzy">

Per vedere un esempio di come funziona lo strumento di traduzione quando il plugin di traduzione è attivo su una pagina, è possibile visitare la [Main Page](Main_Page.md). Verrà visualizzata una nuova barra del menu lingua in basso. Esso viene generato automaticamente. Cliccando, per esempio, sul link tedesco, si apre la pagina [Main Page/de](Main_Page/de.md). Immediatamente sotto al titolo, è possibile leggere  \"Questa pagina è una *versione tradotta* di Main Page e la traduzione è xx% completa.\" (xx è la percentuale attuale di traduzione). Cliccare sul link \"Traduci questa pagina\" per avviare la traduzione, o per aggiornare o correggere la traduzione esistente.


</div>

Ora se andate nella pagina [Main Page](Main_Page.md), noterete che quando la pagina è stata contrassegnata per la traduzione non è possibile modificarla direttamente, ma che si deve passare attraverso l\'utility di traduzione.

Quando si aggiungono nuovi contenuti, prima deve essere creata la pagina inglese, e poi la pagina inglese può essere tradotta in un\'altra lingua. Se qualcuno vuole cambiare o aggiungere dei contenuti in una pagina esistente, deve farlo nella pagina inglese, marcarla per la traduzione e poi tradurre i contenuti editati.

Se non siete sicuri su come procedere, non esitate a chiedere aiuto nel [Development → Wiki subforum](https://forum.freecadweb.org/viewforum.php?f=21) o nel [specific language subforum](https://forum.freecadweb.org/viewforum.php?f=11) del [FreeCAD forum](http://forum.freecadweb.org).

### Note importanti 


<div class="mw-translate-fuzzy">

Ogni utente del wiki che dispone delle autorizzazioni \"Editor\" è in grado di avviare l\'utilità di traduzione e scrivere, salvare e rivedere le traduzioni.


</div>

Tuttavia, solo gli utenti con permessi di \"Amministratore\" possono contrassegnare le pagine per la traduzione. Una pagina che non è stata contrassegnata per la traduzione non fa uso dell\'estensione di traduzione e non è sincronizzata correttamente con le informazioni in inglese.

Anche la barra laterale (il menu di navigazione a sinistra) è traducibile, ma solo gli amministratori possono modificare questo elemento del sito. Si prega di seguire le istruzioni dedicate a questo nella pagina [Tradurre la Sidebar](Localisation_Sidebar/it.md).

La prima volta che una pagina viene passata al nuovo sistema di traduzione perde tutte le sue vecchie traduzioni \"manuali\". Per recuperare una traduzione, bisogna salvare una copia offline del vecchio testo prima della conversione. Quindi si può usare questo vecchio testo tradotto per riempire le unità di traduzione nel nuovo sistema. Si può anche aprire una versione precedente dalla cronologia (pulsante History) e ottenere il vecchio testo in questo modo. Questo deve essere fatto per ogni lingua che ha una pagina tradotta.

### Tradurre la documentazione di FreeCAD 

Come per consenso generale, la pagina di riferimento nel wiki è la pagina inglese, che dovrebbe essere creata per prima. Se si desidera modificare o aggiungere contenuto a una pagina, è necessario farlo prima alla pagina inglese e solo una volta completato l\'aggiornamento, portare la modifica nella pagina tradotta.

### Vecchie istruzioni di traduzione 


<div class="mw-translate-fuzzy">

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Queste istruzioni sono solo un background storico, mentre le pagine vengono passate al nuovo plugin di traduzione.                                                                                                                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Quindi il primo passo è **controllare se è già stato avviata la traduzione del manuale per la propria lingua** (cercare nella barra laterale sinistra, sotto \"manual\").                                                                                                                                                                                                                                   |
| In caso contrario, andare al [forum](http://forum.freecadweb.org/) e comunicare che si intende avviare una nuova traduzione, creeremo le impostazioni di base per la lingua che si desidera lavorare.                                                                                                                                                                                                       |
| È necessario [ottenere il permesso di modifica del wiki](FAQ/es#C.C3.B3mo_consigo_permisos_de_edici.C3.B3n_para_esta_wiki.3F.md).                                                                                                                                                                                                                                                                   |
| Se la lingua è già presente, vedere quali pagine da tradurre sono ancora mancanti (sono quelle elencate in rosso). La tecnica è semplice: **entrare in una pagina rossa, copiare e incollare il contenuto della corrispondente pagina inglese, e iniziare a tradurre.**.                                                                                                                                    |
| Non dimenticare di includere tutti i tag e i modelli dalla pagina originale in inglese. Alcuni di questi modelli avranno un equivalente nella nuova lingua (per esempio, esiste un modello di Docnav in francese denominato Docnav/fr). Si deve utilizzare **una barra slash e il codice della proria lingua** in quasi tutti i collegamenti. Guardare altre pagine già tradotte per vedere come procedere. |
| Aggiungere una barra e il codice della propria lingua nelle categorie, come \[\[<img src="images/Property.png" style="width:16px"> Developer Documentation/it\]\]                                                                                                                                                                                                                                                                                     |
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
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


</div>


<div class="mw-translate-fuzzy">

## Tradurre il sito Web di FreeCAD 

La traduzione del sito Web di FreeCAD è ora fatta tramite [Crowdin](https://crowdin.com/translate/freecad/561/en-en). Il file si chiama {{FileName|homepage.po}}.


</div>

Translation of the FreeCAD website is now done through [Crowdin](https://crowdin.com/translate/freecad/561/en-en). The file is named {{FileName|homepage.po}}.


<div class="mw-translate-fuzzy">

## Sviluppo - Come aggiungere la localizzazione 

Questa sezione è per gli sviluppatori che desiderano aggiungere la localizzazione al loro codice.


</div>

This section is for developers who want to add localisation to their code.


<div class="mw-translate-fuzzy">

### Preparare i moduli di FreeCAD/master per la traduzione 

Queste sono le parti del processo di traduzione di FreeCAD:

-   estrarre le stringhe di testo dal codice sorgente nei file \*.ts
-   caricare i file \*.ts in [FreeCAD Crowdin](http://crowdin.net/project/freecad).
-   tradurre le stringhe all\'interno di Crowdin
-   estrarre i nuovi o modicati file \*.ts da Crowdin
-   convertire i file \*.ts in file \*.qm e aggiornare il file \*.qrc di ogni modulo
-   aggiornare FreeCAD master


</div>

These are the parts to the FreeCAD translation process:

-   extract text strings from source code into \*.ts files
-   load \*.ts files into [FreeCAD Crowdin](http://crowdin.net/project/freecad).
-   translation of strings within Crowdin
-   extract modified/new \*.ts files from Crowdin
-   convert \*.ts files into \*.qm files and update each module\'s \*.qrc file
-   update FreeCAD master

Tutti i passaggi precedenti sono eseguiti dagli \"script di traduzione\" che vengono eseguiti periodicamente da un amministratore.


<div class="mw-translate-fuzzy">

Preparare il modulo per la traduzione è abbastanza semplice. Innanzitutto, è necessario assicurarsi di avere una directory \"translations\" in {{FileName|myModule/Gui/Resources}}. Quindi aprire una finestra di terminale (o equivalente in Windows/OSX) nella directory \"translations\" e inserire il seguente comando: 
```pythonlupdate -ts myModule.ts```


</div>


<div class="mw-translate-fuzzy">

Questo crea un file di traduzione vuoto. Una volta fatto questo, è necessario assicurarsi che gli script di traduzione siano aggiornati come in questa [pull request](https://github.com/FreeCAD/FreeCAD/pull/810).


</div>


<div class="mw-translate-fuzzy">

Tutto ciò che segue è automatico per quanto riguarda lo sviluppatore. L\'amministratore estrae le stringhe di testo, i traduttori le traducono, quindi l\'amministratore estrae le traduzioni e aggiorna FreeCAD/master.


</div>


<div class="mw-translate-fuzzy">

### Preparare il proprio modulo o la macro per la traduzione 

I moduli di terze parti o le macro sono tradotti in modo molto simile, tranne per il fatto che bisogna fare un po\' di lavoro da soli. Questa [discussione nel forum](https://www.forum.freecadweb.org/viewtopic.php?f=3&t=25180) descrive i dettagli.


</div>

3rd party modules or macros are translated in much the same fashion, except that you must do some of the work yourself. This [forum discussion](https://www.forum.freecadweb.org/viewtopic.php?f=3&t=25180) describes the details.

Update: see [Translating an external workbench](Translating_an_external_workbench.md)


<div class="mw-translate-fuzzy">

### Precedenti tecniche di traduzione dei moduli 

[Vecchi metodi di localizzazione](Localization_Older_Methods/it.md) descrive in dettaglio l\'uso di strumenti di traduzione come Qt Linguist, lupdate, lrelease, pylupdate4, ecc. La maggior parte di questo non è più richiesto per i moduli di FreeCAD/master, ma può essere utile per preparare e aggiornare i moduli di terze parti.


</div>

[Localization Older Methods](Localization_Older_Methods.md) describes the use of translation tools such as Qt Linguist, lupdate, lrelease, pylupdate4, etc in detail. Most of this is no longer required for FreeCAD/master modules, but may be helpful preparing and updating 3rd party modules.


<div class="mw-translate-fuzzy">

## Aggiornamento automatico delle traduzioni in Crowdin 

Attualmente i manutentori di FreeCAD utilizzano l\'API Crowdin tramite [Crowdin Scripts](Crowdin_Scripts/it.md) per estrarre e trasferire le traduzioni in Crowdin e riportarle nel repository Github. L\'API Crowdin offre ai manutentori di FreeCAD la possibilità di automatizzare aspetti del flusso di lavoro di traduzione del progetto, per maggiori informazioni fare riferimento alla [Crowdin API documentation](https://support.crowdin.com/api/api-integration-setup/).


</div>

Currently FreeCAD maintainers use the Crowdin API via [Crowdin Scripts](Crowdin_Scripts.md) to pull and push translations in to Crowdin and back in to the Github repo. The Crowdin API gives FreeCAD maintainers the ability to automate aspects of the project\'s translation workflow, for more info refer to the [Crowdin API documentation](https://support.crowdin.com/api/api-integration-setup/).


<div class="mw-translate-fuzzy">

## Pagine correlate 

-   [Crowdin Administration](Crowdin_Administration/it.md)
-   [Crowdin Scripts](Crowdin_Scripts/it.md)


</div>

-   [Crowdin Administration](Crowdin_Administration.md)
-   [Crowdin Scripts](Crowdin_Scripts.md)

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To get a dictionary with the languages the FreeCAD interface supports, use the `supportedLocales` method of the `FreeCADGui` module.


```python
locales = FreeCADGui.supportedLocales()
```

After execution `locales` will contain:


```python
{'English': 'en', 'Afrikaans': 'af', 'Arabic': 'ar', 'Basque': 'eu', 'Catalan': 'ca', 'Chinese Simplified': 'zh-CN', 'Chinese Traditional': 'zh-TW', 'Croatian': 'hr', 'Czech': 'cs', 'Dutch': 'nl', 'Filipino': 'fil', 'Finnish': 'fi', 'French': 'fr', 'Galician': 'gl', 'German': 'de', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Kabyle': 'kab', 'Korean': 'ko', 'Lithuanian': 'lt', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt-PT', 'Portuguese, Brazilian': 'pt-BR', 'Romanian': 'ro', 'Russian': 'ru', 'Slovak': 'sk', 'Slovenian': 'sl', 'Spanish': 'es-ES', 'Swedish': 'sv-SE', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Valencian': 'val-ES', 'Vietnamese': 'vi'}
```

To get the current interface language use the `getLocale` method of the same module:


```python
locale = FreeCADGui.getLocale()
```

If the current language is English `locale` will contain:


```python
'English'
```

To get the corresponding [language code](https://support.crowdin.com/api/language-codes/) you can use use:


```python
locale = FreeCADGui.supportedLocales()[Gui.getLocale()]
```

If the current language is English the result will be:


```python
'en'
```

To set the current interface language use the `setLocale` method of the same module. You can specify the language or the language code:


```python
FreeCADGui.setLocale('Russian')
FreeCADGui.setLocale('ru')
```


<div class="mw-translate-fuzzy">





</div>




[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Wiki](Category_Wiki.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Localisation/it
