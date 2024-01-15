# Tracker/it
**Nel febbraio 2022 il monitoraggio dei bug di FreeCAD è stato migrato a [https://github.com/FreeCAD/FreeCAD/issues GitHub Issues]. Il bug tracker Mantis descritto di seguito è ora in modalità di sola lettura.**

![](images/Mantis_logo_262x90.png )

Il [FreeCAD BugTracker](https://www.freecadweb.org/tracker) è il posto dove segnalare i bug, presentare le richieste di funzionalità, patch, o richiedere di fondere un proprio ramo, se avete sviluppato qualcosa usando Git. Il tracker è suddiviso in moduli, quindi cercate di essere specifici e di presentare la richiesta nella sottosezione appropriata. In caso di dubbio, lasciare il messaggio nella sezione \"FreeCAD\".

## Flusso di lavoro raccomandato 

![](images/Bugreport-workflow.png )

Come mostrato nel diagramma di flusso sopra, prima di creare i ticket, cercare sempre prima nei forum e nel bugtracker per scoprire se il problema è già noto. Ciò consente di far risparmiare un sacco di tempo e di lavoro agli sviluppatori ed ai volontari che possono perciò dedicare più tempo per rendere FreeCAD ancora più fantastico.



## Segnalare i bug 

Quando si pensa di aver trovato un bug, si è invitati a segnalarlo lì, se si è prima discusso la questione nelle sedi opportune.

Prima di segnalare un bug, si prega di verificare i seguenti punti:

-   Assicurarsi di utilizzare la versione più aggiornata di FreeCAD. **NOTAː** il tuo bug potrebbe essere corretto nella versione di sviluppo (instabile). L\'utente medio esegue la versione stabile di FC.
-   Assicurarsi che il proprio bug sia davvero un bug, cioè qualcosa che dovrebbe funzionare ma non funziona. **Assicurarsi che lo stesso bug non sia già stato segnalato cercando prima nel bugtracker e nel forum**.
    -   Ricordareː se non si è sicuri, non esitare a spiegare il problema o bug nel f[Help forum](http://forum.freecadweb.org/viewforum.php?f=3) e chiedere cosa fare.
    -   **Nota**ː prima di postare sul forum leggere le [Forum Guidelines](https://forum.freecadweb.org/viewtopic.php?f=3&t=2264).
-   Descrivere il più chiaramente possibile il problema e come può essere riprodotto. Se non siamo in grado di verificare il bug, potremmo non essere in grado di risolverlo.
    -   Ciò significa **riportarlo in modo chiaro, ben formattato, passo dopo passo** in modo che anche un utente amatoriale possa riprodurlo.
    -   Racommandazioneː anche le **schermate** del bug sono molto utili da includere. Utenti Windows: non allegare schermate in formato Word o PDF. Usare lo strumento di cattura di Windows per salvare la cattura come immagine PNG.
    -   Racommandazioneː ancora meglio, una **GIF animata o screencast** aumenta la probabilità di riprodurre il problema.
-   **Aggiungere un file FreeCAD di esempio** (file .FCStd) in modo che gli sviluppatori o tester possano riprodurre rapidamente il bug.
    -   Si prega di non comprimere il file \*.FCStd, è già zippato.
    -   Le dimensioni dei file allegabili sono limitate. Se il proprio file \*.FCStd è troppo grande per essere allegato, si può utilizzare un servizio di archiviazione online (molti sono gratuiti come Google Drive, Microsoft OneDrive, Dropbox).
-   Includere tutte le informazioni dal pulsante \"Copia negli Appunti\" nel dialogo **Help (menu) -\> About FreeCAD**. Assicurarsi che i dati includano la versione di OCC o OCE utlizzata.
-   Si prega di inviare un rapporto separato per ogni bug.
-   Se il proprio bug causa un arresto anomalo in FreeCAD e si è su un sistema che lo supporta, si può provare a eseguire un **backtrace di debug** e allegare detta traccia al ticket. Questo può far risparmiare molto tempo agli sviluppatori nell\'individuare la fonte del crash. Vedere [Debugging](Debugging/it.md) per maggiori dettagli.



## Richiedere delle nuove funzioni 

Se desiderate qualcosa che in FreeCAD che non è ancora implementato, it is not a bug but a feature request questo non è un bug, ma una richiesta di nuove funzionalità.

1.  **IMPORTANTEː** Prima di richiedere una potenziale funzione **assicurarsi di essere il primo a farlo cercando nei forum e nel bugtracker**. Se non ci sono ticket o discussioni preesistenti, il passaggio successivo èː
2.  Avviare un thread del forum per discutere la propria richiesta di funzione con la comunità tramite il [Open Discussion forum](http://forum.freecadweb.org/viewforum.php?f=8).
3.  Una volta che la comunità ha accettato che si tratta di una funzione valida, è quindi possibile aprire un ticket sul tracker (da registrare come \"richiesta di funzione\" invece di \"bug\").

-   **NOTA #1** Per mantenere le cose organizzate, ricordarsi di indicare l\'URL del thread del forum nel ticket e il numero del ticket (come collegamento) nel thread del forum.
-   **NOTA #2** Tenere presente che non ci sono garanzie che il desiderio sarà soddisfatto.

![Pagina di segnalazione Bugtracker di FreeCAD: utilizzare il menu a discesa per designare correttamente il tipo di ticket](images/MantisBT-setting-Feature-Request.jpg )



## Inviare patch 

Nel caso in cui si programmi una correzione di un bug, un\'estensione o qualcos\'altro che può essere di uso pubblico in FreeCAD, inviare la patch come \"Pull Request\" a [GitHub](https://github.com/FreeCAD/FreeCAD).

1.  Per una richiesta ampia, complessa o che cambia il comportamento, aprire un thread del forum nel [Developer subforum](https://forum.freecadweb.org/viewforum.php?f=10) per annunciare e discutere la tua patch. Per piccole correzioni di bug questo non è necessario.
2.  Inviare la Pull Request (PR) al [FreeCAD GitHub repo](http://github.com/FreeCAD/FreeCAD). Il messaggio di invio della PR sarà precompilato con una lista di controllo da seguire per garantire che il tuo invio abbia le migliori possibilità di una rapida accettazione. Se non si è mai lavorato con `git` prima o non si ha familiarità con l\'invio di una PR a github, leggere la nostra introduzione alla pagina wiki [github](Source_code_management/it.md).
3.  Si deve essere presenti alla discussione, sia nel forum che nella richiesta della pull di GitHub, in modo che il codice possa potenzialmente essere unito in modo più efficace.



## Richiedere la fusione 

(Stesse linee guida di come [Inviare delle patches](https://www.freecadweb.org/wiki/Tracker#Submitting_patches))

Se avete creato un ramo git contenente delle modifiche che desiderate far confluire nel codice di FreeCAD, potete fare la richiesta di avere la recensione e la fusione del vostro ramo, se ​​gli sviluppatori di FreeCAD sono d\'accordo. È necessario pubblicare prima il ramo in un repository git pubblico (github, bitbucket, sourceforge \...) e poi fornire l\'URL del vostro ramo nella richiesta di unione.



## Suggerimenti e trucchi per MantisBT 

### Markup di MantisBT 

MantisBT (Mantis Bug Tracker) ha il proprio markup.

-   **@**mention - funziona proprio come su GitHub dove anteponendo \"@\" al nome utente di qualcuno questi riceverà un\'e-mail che è stato \"menzionato\" in un thread del ticket

<img alt="" src=images/mantisbt-mention-example.jpg  style="width:600px;">

-   **\#**1234 - Aggiungendo un hash tag davanti a un numero viene presentata una scorciatoia per collegarsi a un altro ticket all\'interno di MantisBT.

    :   **Nota**: se si passa il mouse su un ticket, viene mostrato il riepilogo + se il ticket è chiuso, e sarà anche barrato come #1234.

<img alt="" src=images/mantisbt-ticket-shortcut-example.jpg  style="width:600px;">

-   **\~**5678 - una scorciatoia che collega a una nota di bug all\'interno di un ticket. Questo può essere utilizzato per fare riferimento alla risposta di qualcuno all\'interno del thread. Per ogni persona che pubblica un post viene mostrato un numero \~#### univoco accanto al proprio nome utente. Guardando l\'immagine nell\'esempio, si vede che la scorciatoia fa riferimento al *numero del ticket:numero del commento* di detto ticket

<img alt="" src=images/mantisbt-comment-shortcut-example.jpg  style="width:600px;">

-   **\<del\>\</del\>** - L\'uso di questi tag crea un testo barrato.

<img alt="" src=images/mantisbt-strikeout-text-example.jpg  style="width:600px;">

-   **\<code\>\</code\>** - Per presentare una riga o un blocco di codice, usare questo tag che lo colorerà e lo differenzierà elegantemente.

<img alt="" src=images/mantisbt-colorized-code-example.jpg  style="width:600px;">

### MantisBT BBCode 

Oltre al suddetto [Markup di MantisBT](Tracker/it#Markup_di_MantisBT.md) si ha anche la possibilità di utilizzare il formato BBCode. Per un elenco completo, vedere la [pagina del plug-in BBCode plus](https://github.com/mantisbt-plugins/BBCodePlus#supported-bbcode-tags). Ecco un elenco di tag BBCode supportatiː 
[img][/img] - Images
[url][/url] - Links
[email][/email] - Email addresses
[color=red][/color] - Colored text
[highlight=yellow][/highlight] - Highlighted text
[size][/size] - Font size
[list][/list] - Lists
[list=1][/list] - Numbered lists (number is starting number)
[*] - List items
[b][/b] - Bold
[u][/u] - underline
[i][/i] - Italic
[s][/s] - Strikethrough
[left][/left] - Left align
[center][/center] - Center
[right][/right] - Right align
[justify][/justify] - Justify
[hr] - Horizontal rule
[sub][/sub] - Subscript
[sup][/sup] - Superscript
[table][/table] - Table
[table=1][/table] - Table with border of specified width
[tr][/tr] - Table row
[td][/td] - Table column
[code][/code] - Code block
[code=sql][/code] - Code block with language definition
[code start=3][/code] - Code block with line numbers starting at number
[quote][/quote] - Quote by *someone* (no name)
[quote=name][/quote] - Quote by *name*


=== MantisBT \<=\> GitHub Markup === Di seguito sono riportate parole chiave speciali del plug-in MantisBT Source-Integration che si collegheranno al repository GitHub di FreeCAD. Vedere [GitHub and MantisBT](Tracker/it#GitHub_and_MantisBT.md).

-   **c:FreeCAD:git commit hash:** - **c** sta per \'commit\'. FreeCAD sta per il repository GitHub di FreeCAD. \'git commit hash\' è l\'hash git commit specifico a cui fare riferimento. Nota: i due punti finali sono necessari. Esempioː cːFreeCADː709d2f325db0490016807b8fa6f49d1c867b6bd8ː
-   **d:FreeCAD:git commit hash:** - simile a quanto sopra, **d** sta per \'diff\' che fornirà una vista Diff del commit. Esempioː dːFreeCADː709d2f325db0490016807b8fa6f49d1c867b6bd8ː
-   **p:FreeCAD:pullrequest:** - simile a quanto sopra, **p** sta per Pull Request. Esempioː pːFreeCADː498ː

<img alt="" src=images/mantisbt-source-integration-markup.jpg  style="width:600px;"> 

## GitHub e MantisBT 

Il bugtracker di FreeCAD ha un plug-in chiamato [Source Integration](https://github.com/mantisbt-plugins/source-integration) che essenzialmente collega il repository GitHub di FreeCAD al nostro tracker MantisBT. Rende più facile tracciare e associare i commit git ai rispettivi ticket MantisBT. **Il plug-in Source Integration scansiona i messaggi di git commit alla ricerca di parole chiave specifiche per eseguire le seguenti azioni:**

**Nota** Le seguenti parole chiave devono essere aggiunte nel messaggio git commit e non nell\'oggetto PR

### Riferimento remoto a un ticket 

L\'utilizzo di questo modello assocerà automaticamente un commit git a un ticket (**Nota:** questo non chiuderà il ticket.) Il formato MantisBT riconoscerà:

-   bug #1234
-   bugs #1234, #5678
-   issue #1234
-   issues #1234, #5678
-   report #1234
-   reports #1234, #5678

Per i curiosi ecco la regex che MantisBT utilizza per questa operazione:


### Risoluzione remota di un ticket 

Il formato MantisBT riconoscerà:

-   fix #1234
-   fixed #1234
-   fixes #1234
-   fixed #1234, #5678
-   fixes #1234, #5678
-   resolve #1234
-   resolved #1234
-   resolves #1234
-   resolved #1234, #5678
-   resolves #1234, #5678

Per i curiosi ecco la regex che MantisBT utilizza per questa operazione:



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Administration](Category_Administration.md) > Tracker/it
