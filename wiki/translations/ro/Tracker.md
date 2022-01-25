# Tracker/ro
<div class="mw-translate-fuzzy">


{{docnav|Licence|Bug Triage}}


</div>


{{TOCright}}

![](images/Mantis_logo_262x90.png )


<div class="mw-translate-fuzzy">

Tracker este locul pentru aː raporta bug-uri (eroare sau disfuncționalitate neprevăzută) , trimiteți cereri de funcționalități, patch-uri sau cereți să vă îmbinați codul corector propriu dacă ați dezvoltat ceva folosind Git. Dispozitivul de urmărire este împărțit în Ateliere \"Workbenches\", așa că vă rugăm să fiți preciși și să vă înscrieți cererea în subsecțiunea corespunzătoare. În caz de îndoială, lăsați-o în secțiunea \"FreeCAD\".


</div>

## Flux de lucru recomandat 

![](images/Bugreport-workflow.png )

După cum se arată în diagrama de mai sus, înainte de a crea tichete, vă rugăm să căutați mereu în forumurile și bugtracker pentru a afla dacă problema dvs. este o problemă cunoscută. Acest lucru economisește o mulțime de timp / muncă pentru dezvoltatori și voluntari care ar putea petrece timpul respectiv, făcând chiar mai minunat acest FreeCAD.

## Raportarea erorilor 

Dacă credeți că ați găsit un bug (disfuncționalitate sau eroare), sunteți binevenit să îl raportați atâta timp cât ați urmat pas cu pas următoarele elemente:

-   Asigurați-vă că utilizați cea mai recentă versiune de FreeCAD. **NOTEː** eroarea dumneavoastră ar putea fi deja rezolvată în versiunea în Dezvoltare(instabilă). Utilizatorii medii utilizează varianta stabilă a FC.
-   Asigurați-vă ca bug-ul este un adevărat bug, asta e, câteodată ar putea să meargă dar să nu fie. **Asigurați-vă că aceeași eroare nu a fost raportată înainte , căutând în bugtracker și forum**.
    -   Nu uitațiː dacă nu sunteți siguri , vă rog nu ezitați să explicați problema/bug-ul pe [Help forum](http://forum.freecadweb.org/viewforum.php?f=3) și întrebați ce este de făcut.
    -   **Notă**ː înainte de a posta pe forum vă rugăm citiți [Forum Guidelines](https://forum.freecadweb.org/viewtopic.php?f=3&t=2264).
-   Descrieți cât mai clar posibil problema, și cum poate fi reprodusă. Dacă noi nu putem verifica eroarea, nu putem să o rezolvăm.
    -   Aceasta înseamnă **raportarea într-un mod clar, bine formatat, pas cu pas** astefel încât și un amator să o poată reproduce.
    -   Recomandatː **Screenshots** a erorii este de asemenea foarte folositor a fi inclus. Useri de Windows: vp rugăm nu atașați capturi de ecran în Word sau format PDF. Utilizați instrumentul Windows Snipping pentru a salva captura ca imagine PNG.
    -   Recomandatː Chiar mai bine, un **Animated gif or Screencast** ar crește posibilitatea de areproduce problema.
-   **Adaugați un exemplul de fișier FreeCAD** (.FCStd file) astfel ca devs/testers să poată reproduce ușor eroarea/disfuncționalitatea.
    -   Vă rugăm nu arhivați fișierul \*.FCStd, este deja zipped.
    -   Atașametnele fișierului sunt limitatea ca mărime. Dacă fișierul dvs \*.FCStd este prea marea pentru a fi atașat, puteți utiliza online storage service (multe sunt gratuite ca de exemplu Google Drive, Microsoft OneDrive, Dropbox).
-   Includeți toate informațiile din butonul \"Copy to Clipboard\" în dialogul **Help (menu) -\> About FreeCAD**. fiți siguri că datele dumneavoastră includ versiunile de OCC ori OCE .
-   Vă rugăm completați un raport separat pentru fiecare bug.
-   Dacă eroarea dvs cauzează un crash in FreeCAD și sunteți pe un sistem care permite aceasta,încercați să rulați un **debug backtrace** și să atașați said trace la ticket. Aceasta poate salva devs foarte mult timp pentru a ținti sursa prăbușirii/crash-ului. Vezi [Debugging](Debugging.md) pentru mai multe detalii.

## Solicitarea de funcționalități 

Dacă doriți să apară ceva în FreeCAD, care încă nu este implementat, it nu este un bug și o solicitarea de funcționalitate.

1.  **IMPORTANTː** Înainte de a solicita a funcționalitate potențială Feature Request **please be certain that you are the first one doing so by searching the forums and the bugtracker**. Dacă ați ajuns la concluzia că nu există token/tichete / discuții pre-existente, următorul pas este \...
2.  Începeți un fir de discuții de forum pentru a discuta despre cererea dvs. cu comunitatea prin [Open Discussion forum](http://forum.freecadweb.org/viewforum.php?f=8).
3.  Odată ce comunitatea este de acord că aceasta este o caracteristică valabilă, puteți deschide un token/tiket pe tracker(file it under *feature request* instead of *bug*).

-   **NOTE \#1** Pentru a păstra lucrurile organizate, nu uitați să conectați adresa URL a firului la tichet și numărul (ca legătură) în firul de pe forum.
-   **NOTE \#2** Rețineți că nu există garanții că dorința dvs. va fi îndeplinită.

![FreeCAD Bugtracker report page - use the dropdown to correctly designate what the ticket is](images/MantisBT-setting-Feature-Request.jpg )

## Propunerea de îmbunătățiri 


<div class="mw-translate-fuzzy">

In cazul în care ați realizat un program de corectare a unei erori/disfuncționalități, o extensie sau orice altceva care poate fi de uz public în FreeCAD, creați un patch utilizând instrumentul Git diff și trimiteți-o pe același bug tracker (ca pe un *patch*).


</div>

## Solicitarea fuzionare 

(Same guidelines as [Submiting patches](https://www.freecadweb.org/wiki/Tracker#Submitting_patches))

Dacă ați creat o modificarea (git branch) conținând schimbări pe care le-ați dori să fie topite/fuzionate în codul FreeCAD, puteți solicita ca ramura dvs. să fie revizuită și integrată în cazul în care dezvoltatorii FreeCAD sunt de acord cu aceasta. Mai întâi trebuie să vă publicați modificarea într-un depozit public git (github, gitlab, bitbucket, sourceforge etc \...) și apoi să dați URL-ul modificării dvs în cererea dvs. de fuziune.

## MantisBT sfaturi și Trucuri 

### MantisBT Markup 

MantisBT (Mantis Bug Tracker) are propria marcă.

-   **@**mention - funcționează ca pe GitHub unde, dacă adăugați prefixul \"@\" la un nume de utilizator, acesta va primi un e-mail pe care a fost \"menționat\" într-un thread de tichet

<img alt="" src=images/mantisbt-mention-example.jpg  style="width:600px;">

-   **\#**1234 - Prin adăugarea unei etichete de tip hash tag în fața unui număr, va fi prezentată o comandă rapidă către un link către un alt bilet în MantisBT.

    :   **Note**: Dacă survolați cu mouse-ul peste un bilet, acesta vă va afișa rezumatul + dacă biletul este închis, acesta va fi blocat ca\#1234.

<img alt="" src=images/mantisbt-ticket-shortcut-example.jpg  style="width:600px;">

-   **\~**5678 - o comandă rapidă care face legătura cu o notă de bug în cadrul unui bilet. Acest lucru poate fi folosit pentru răspunsul cuiva în cadrul firului. Fiecare persoană va avea un număr unic de postare \#\#\#\# la numele de utilizator. Dacă priviți imaginea din exemplu, veți observa că comanda rapidă face referire la numărul *ticket number:comment number* al biletului menționat

<img alt="" src=images/mantisbt-comment-shortcut-example.jpg  style="width:600px;">

-   **\<del\>\</del\>** - Utilizând această etichetă aceasta va strikeout text.

<img alt="" src=images/mantisbt-strikeout-text-example.jpg  style="width:600px;">

-   **\<code\>\</code\>** - pentru a prezenta o linie sau un bloc de cod, utilizați această etichetă și aceasta o va colora și o va diferenția elegant.

<img alt="" src=images/mantisbt-colorized-code-example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

### MantisBT BBCode 

În plus față de mai sus [Tracker/MantisBT ̠Markup](Tracker/MantisBT_̠Markup.md) are de asemenea posibilitatea să utilizeze formatul BBCode. Pentru o listă completă, vezi [BBCode plus plugin page](https://github.com/mantisbt-plugins/BBCodePlus#supported-bbcode-tags). aici este o listă a etichetelor BBCode suportateː 
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
 === MantisBT \<=\> GitHub Markup === Mai jos sunt cuvintele cheie speciale pentru plugin-ul MantisBT Source-Integration, care vor face legătura cu repo-ul FreeCAD GitHub. Vezi [Tracker\#GitHub\_and\_MantisBT](Tracker#GitHub_and_MantisBT.md).

-   **c:FreeCAD:git commit hash:** - **c** stands for \'commit\'. FreeCAD stands for the FreeCAD GitHub repo. \'git commit hash\' is the specific git commit hash to reference. Note: the trailing colon is necessary. Exampleː cːFreeCADː709d2f325db0490016807b8fa6f49d1c867b6bd8ː
-   **d:FreeCAD:git commit hash:** - similar to the above, **d** stands for \'diff\' which will provide a Diff view of the commit. Exampleː dːFreeCADː709d2f325db0490016807b8fa6f49d1c867b6bd8ː
-   **p:FreeCAD:pullrequest:** - similar to the above, **p** stands for Pull Request. Exampleː pːFreeCADː498ː

<img alt="" src=images/mantisbt-source-integration-markup.jpg  style="width:600px;"> 


</div>

=== MantisBT \<=\> GitHub Markup === Below are special MantisBT Source-Integration plugin keywords which will link to the FreeCAD GitHub repo. See [GitHub and MantisBT](Tracker#GitHub_and_MantisBT.md).

-   **c:FreeCAD:git commit hash:** - **c** stands for \'commit\'. FreeCAD stands for the FreeCAD GitHub repo. \'git commit hash\' is the specific git commit hash to reference. Note: the trailing colon is necessary. Exampleː cːFreeCADː709d2f325db0490016807b8fa6f49d1c867b6bd8ː
-   **d:FreeCAD:git commit hash:** - similar to the above, **d** stands for \'diff\' which will provide a Diff view of the commit. Exampleː dːFreeCADː709d2f325db0490016807b8fa6f49d1c867b6bd8ː
-   **p:FreeCAD:pullrequest:** - similar to the above, **p** stands for Pull Request. Exampleː pːFreeCADː498ː

<img alt="" src=images/mantisbt-source-integration-markup.jpg  style="width:600px;"> 

## GitHub și MantisBT 

FreeCAD bugtracker are un plug-in numit [Source Integration](https://github.com/mantisbt-plugins/source-integration) care în principiu care, în esență, leagă atât repo-ul FreeCAD GitHub cât și tracker-ul nostru MantisBT. El facilitează urmărirea și asocierea git commits cu tichetele lor MantisBT. \'\'\'Pluginul Source Integration scanează mesajele de git commits pentru anumite cuvinte cheie pentru a executa următoarele acțiuni:\' \'\'

**Notă** Cuvintele cheie de mai jos trebuie adăugate în git commit message și nu în subiectul PR

### Referința distantă a unui tichet 

Folosind acest model, se va asocia automat o comanda git cu un ticket (\'\' \'Notă:\' \'\' acest lucru nu va închide biletul.)Formatul MantisBT va recunoaște:

-   bug \#1234
-   bugs \#1234, \#5678
-   issue \#1234
-   issues \#1234, \#5678
-   report \#1234
-   reports \#1234, \#5678

For the inquisitive here is the regex MantisBT uses for this operation:


### Rezolvarea la distanță a unui tichet 

Formatul MantisBT va recunoaște:

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

## Înrudite

-   [Bug Triage](Bug_Triage.md)
-   [Source Code Management](Source_Code_Management.md)


</div>


<div class="mw-translate-fuzzy">


{{docnav|Licence|Bug Triage}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Administration](Category_Administration.md) > Tracker/ro
