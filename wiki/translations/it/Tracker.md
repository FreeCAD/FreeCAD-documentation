# Tracker/it
<div class="mw-translate-fuzzy">


{{docnav/it|[Licenze](Licence/it.md)|[Smistamento dei bug](Bug_Triage/it.md)}}


</div>


{{TOCright}}

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

-   **NOTA \#1** Per mantenere le cose organizzate, ricordarsi di indicare l\'URL del thread del forum nel ticket e il numero del ticket (come collegamento) nel thread del forum.
-   **NOTA \#2** Tenere presente che non ci sono garanzie che il desiderio sarà soddisfatto.

![Pagina di segnalazione Bugtracker di FreeCAD: utilizzare il menu a discesa per designare correttamente il tipo di ticket](images/MantisBT-setting-Feature-Request.jpg )

## Inviare patch 

Se avete creato il programma di correzione a un bug, una estensione o altro che può essere di uso pubblico in FreeCAD, create una patch utilizzando lo strumento Git diff e presentatela utilizzando il medesimo tracker (il file è una patch).

Addendumː FreeCAD development has switched to the [GitHub](https://github.com/FreeCAD/FreeCAD) development model so the workflow for submitting patches has been greatly enhanced/streamlined by submitting Pull Requests.

1.  Open a forum thread in the [Developer subforum](https://forum.freecadweb.org/viewforum.php?f=10) to announce and discuss your patch.
2.  Submit your Pull Request (PR) to the [FreeCAD GitHub repo](http://github.com/FreeCAD/FreeCAD). Be sure to link to the forum thread in the git commit summary. If you haven\'t worked with `git` before or are unfamiliar with submitting a PR to github, please read our introduction to [github](Source_code_management.md) wiki page.
3.  Paste the PR link in to the forum thread for the devs/testers to test.
4.  Be present for the discussion so that your code can potentially be merged more effectively.

**NOTEː** the FreeCAD community recommends to first discuss any large revision to the source code in advance to save everyone time.

## Richiedere la fusione 

(Stesse linee guida di come [Inviare delle patches](https://www.freecadweb.org/wiki/Tracker#Submitting_patches))

Se avete creato un ramo git contenente delle modifiche che desiderate far confluire nel codice di FreeCAD, potete fare la richiesta di avere la recensione e la fusione del vostro ramo, se ​​gli sviluppatori di FreeCAD sono d\'accordo. È necessario pubblicare prima il ramo in un repository git pubblico (github, bitbucket, sourceforge \...) e poi fornire l\'URL del vostro ramo nella richiesta di unione.

## Suggerimenti e trucchi per MantisBT 

### Markup di MantisBT 

MantisBT (Mantis Bug Tracker) ha il proprio markup.

-   **@**mention - funziona proprio come su GitHub dove anteponendo \"@\" al nome utente di qualcuno questi riceverà un\'e-mail che è stato \"menzionato\" in un thread del ticket

<img alt="" src=images/mantisbt-mention-example.jpg  style="width:600px;">

-   **\#**1234 - Aggiungendo un hash tag davanti a un numero viene presentata una scorciatoia per collegarsi a un altro ticket all\'interno di MantisBT.

    :   **Nota**: se si passa il mouse su un ticket, viene mostrato il riepilogo + se il ticket è chiuso, e sarà anche barrato come \#1234.

<img alt="" src=images/mantisbt-ticket-shortcut-example.jpg  style="width:600px;">

-   **\~**5678 - una scorciatoia che collega a una nota di bug all\'interno di un ticket. Questo può essere utilizzato per fare riferimento alla risposta di qualcuno all\'interno del thread. Per ogni persona che pubblica un post viene mostrato un numero \~\#\#\#\# univoco accanto al proprio nome utente. Guardando l\'immagine nell\'esempio, si vede che la scorciatoia fa riferimento al *numero del ticket:numero del commento* di detto ticket

<img alt="" src=images/mantisbt-comment-shortcut-example.jpg  style="width:600px;">

-   **\<del\>\</del\>** - L\'uso di questi tag crea un testo barrato.

<img alt="" src=images/mantisbt-strikeout-text-example.jpg  style="width:600px;">

-   **\<code\>\</code\>** - Per presentare una riga o un blocco di codice, usare questo tag che lo colorerà e lo differenzierà elegantemente.

<img alt="" src=images/mantisbt-colorized-code-example.jpg  style="width:600px;">

### MantisBT BBCode 

In addition to the above [MantisBT Markup](Tracker#MantisBT_Markup.md) one also has the possibility to use BBCode format. For a comprehensive list see the [BBCode plus plugin page](https://github.com/mantisbt-plugins/BBCodePlus#supported-bbcode-tags). Here is a list of supported BBCode tagsː 
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


=== MantisBT \<=\> GitHub Markup === Below are special MantisBT Source-Integration plugin keywords which will link to the FreeCAD GitHub repo. See [GitHub and MantisBT](Tracker#GitHub_and_MantisBT.md).

-   **c:FreeCAD:git commit hash:** - **c** stands for \'commit\'. FreeCAD stands for the FreeCAD GitHub repo. \'git commit hash\' is the specific git commit hash to reference. Note: the trailing colon is necessary. Exampleː cːFreeCADː709d2f325db0490016807b8fa6f49d1c867b6bd8ː
-   **d:FreeCAD:git commit hash:** - similar to the above, **d** stands for \'diff\' which will provide a Diff view of the commit. Exampleː dːFreeCADː709d2f325db0490016807b8fa6f49d1c867b6bd8ː
-   **p:FreeCAD:pullrequest:** - similar to the above, **p** stands for Pull Request. Exampleː pːFreeCADː498ː

<img alt="" src=images/mantisbt-source-integration-markup.jpg  style="width:600px;"> 

## GitHub and MantisBT 

The FreeCAD bugtracker has a plug-in called [Source Integration](https://github.com/mantisbt-plugins/source-integration) which essentially ties both the FreeCAD GitHub repo to our MantisBT tracker. It makes it easier to track and associate git commits with their respective MantisBT tickets. **The Source Integration plugin scans the git commit messages for specific keywords in order to execute the following actions:**

**Note** The below keywords need to be added in the git commit message and not the PR subject

### Remotely referencing a ticket 

Using this pattern will automagically associate a git commit to a ticket (**Note:** this will not close the ticket.) The format MantisBT will recognize:

-   bug \#1234
-   bugs \#1234, \#5678
-   issue \#1234
-   issues \#1234, \#5678
-   report \#1234
-   reports \#1234, \#5678

For the inquisitive here is the regex MantisBT uses for this operation:


### Remotely resolving a ticket 

The format MantisBT will recognize:

-   fix \#1234
-   fixed \#1234
-   fixes \#1234
-   fixed \#1234, \#5678
-   fixes \#1234, \#5678
-   resolve \#1234
-   resolved \#1234
-   resolves \#1234
-   resolved \#1234, \#5678
-   resolves \#1234, \#5678

For the inquisitive here is the regex MantisBT uses for this operation:



<div class="mw-translate-fuzzy">

## Pagine correlate 

-   [Smistamento dei bug](Bug_Triage/it.md)
-   [Gestione del codice sorgente](Source_code_management/it.md)


</div>


<div class="mw-translate-fuzzy">


{{docnav/it|[Licenze](Licence/it.md)|[Smistamento dei bug](Bug_Triage/it.md)}}


</div>




[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Administration](Category:Administration.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Tracker/it
