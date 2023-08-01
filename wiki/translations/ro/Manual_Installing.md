# Manual:Installing/ro
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC/ro}}

FreeCAD utilizează licența [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) , care vă permite să descărcați, să instalați, să redistribuiți și să utilizați FreeCAD așa cum doriți, indiferent de tipul de muncă pe care o veți realiza (comercială sau necomercială). Nu sunteți obligat la nicio clauză sau restricție, iar fișierele pe care le produceți cu ele sunt pe deplin ale dvs. Singurul lucru pe care licența îl interzice, într-adevăr, este să susții că ai programat tu însuți FreeCAD!


<div class="mw-translate-fuzzy">

FreeCAD rulează fără nici o diferență pe Windows, Mac OS și Linux. Cu toate acestea, modurile de instalare diferă ușor în funcție de platforma dvs. Pe Windows și Mac, comunitatea FreeCAD furnizează pachete precompilate (instalatori) gata de descărcare, în timp ce pe Linux, codul sursă este pus la dispoziția administratorilor de distribuții Linux, care sunt apoi responsabili pentru ambalarea FreeCAD în distribuția lor specifică. Ca rezultat, pe Linux, puteți instala, de obicei, FreeCAD chiar din aplicația de manager de software.


</div>

Pagina oficială de descărcat pentru Windows și Mac OS este <https://github.com/FreeCAD/FreeCAD/releases>

**Versiuni FreeCAD**


<div class="mw-translate-fuzzy">

Versiunile oficiale ale FreeCAD, pe care le puteți găsi pe pagina de mai sus și în managerul de software al distribuției, sunt versiuni stabile. Cu toate acestea, dezvoltarea FreeCAD este rapidă! Noi caracteristici și corecții de erori sunt adăugate aproape în fiecare zi. Deoarece uneori poate dura o perioadă lungă de timp între lansări stabile, s-ar putea să fiți interesat să încercați o versiune mai eficace a FreeCAD. Aceste versiuni de dezvoltare sau pre-lansări sunt încărcate din când în când în [download page](https://github.com/FreeCAD/FreeCAD/releases) menționat mai sus, sau dacă utilizați Ubuntu sau Fedora, comunitatea FreeCAD menține de asemenea [PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) (Personal Package Archives) și [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/) sau pași zilnici de avansare \'daily builds\' care sunt regulat actualizați cu cel mai recente modificări.


</div>


<div class="mw-translate-fuzzy">

Dacă instalați FreeCAD într-o mașină virtuală, vă rugăm să fiți conștienți de faptul că performanța poate să fie slabă sau, în unele cazuri, inutilizabilă din cauza limitelor [OpenGL](https://en.wikipedia.org/wiki/OpenGL) pe majoritatea mașinilor virtuale.


</div>

### Instalarea pe Windows 

1.  Descărcați un pachet executabil (.exe) corespunzător la vesiunea dvs de Windows (32bit or 64bit) de la [download page](https://github.com/FreeCAD/FreeCAD/releases). Executabilul FreeCAD ar trebui să funcționeze pe orice versiune windows începând Windows 7.
2.  Double-click pe executabilul descărcat.
3.  Accept termenii licenței LGPL , acesta va fi unul dintre puținele cazuri în care puteți să faceți clic în mod sigur pe butonul \"acceptați\" fără a citi textul. Nu există clauze ascunse: ![](images/Freecad-windows-install-01.jpg )
4.  Puteți să părăsiți aici calea implicită sau să o modificați dacă doriți: ![](images/Freecad-windows-install-02.jpg )
5.  Nu este nevoie să setați variabila PYTHONPATH, cu excepția cazului în care intenționați să îmbunătățiți programul în python, caz în care probabil că deja știți despre ce este vorba: ![](images/Freecad-windows-install-03.jpg )
6.  În timpul instalării, vor fi instalate și câteva componente suplimentare, care sunt incluse în interiorul programului de instalare:![](images/Freecad-windows-install-04.jpg )
7.  Gata, Asta este, FreeCAD este instalat. Îl veți găsi în meniul de pornire. ![](images/Freecad-windows-install-05.jpg )

**Instalarea versiunii în curs de dezvoltare**


<div class="mw-translate-fuzzy">

Realizarea pachetelor FreeCAD și crearea unui program de instalare necesită timp și dedicare, de obicei, versiunile de dezvoltare (numite și versiuni pre-lansare) sunt furnizate ca arhive .zip (sau .7z). Acestea nu trebuie să fie instalate, este suficient să le dezarhivați și a lansa FreeCAD făcând dublu clic pe fișierul FreeCAD.exe pe care îl veți găsi înăuntru. Acest lucru vă permite, de asemenea, să păstrați ambele versiuni stabile și \"instabile\" împreună pe același computer.


</div>

### Instalare sub Linux 


<div class="mw-translate-fuzzy">

Pe cele mai moderne distribuții Linux (Ubuntu, Fedora, OpenSUSE, Debian, Mint, Elementary etc.), FreeCAD poate fi instalat cu un clic pe un buton, direct de la aplicația de management software furnizată de distribuția dvs. (aspectul poate diferi de imaginile de mai jos, fiecare distribuție utilizează propriul instrument).


</div>


<div class="mw-translate-fuzzy">

1.  Deschideți managerul software și căutați \"freecad\": ![](images/Freecad-linux-install-01.jpg )
2.  Faceți click pe butonul \"install\" și gata, asta este, FreeCAD este instalat. Nu uitați să evaluați ulterior! ![](images/Freecad-linux-install-02.jpg )


</div>

**Căi alternative**

Una dintre bucuriile mari de a utiliza Linux este multitudinea de posibilități de a personaliza software-ul dvs., așa că nu vă abțineți. Sub Ubuntu și derivatele sale, FreeCAD poate fi de asemenea instalat de la [PPA](https://launchpad.net/~freecad-maintainers) fiind menținut de către comunitatea FreeCAD (conține și ambele versiuni și cea stabilă și cea în curs de dezvoltare) . În Fedora, versiunile recente de dezoltare a FreeCAD pot fi instalate de pe [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/), și deoarece acest lucru este un software open source, puteți, de asemenea, cu ușurință [compile FreeCAD yourself](Compiling.md).

### Instalaarea pe Mac OS 


<div class="mw-translate-fuzzy">

Instalarea FreeCAD pe Mac OSX este la fel de simplă ca și pe alte platforme. Cu toate acestea, deoarece există mai puțini oameni din comunitate care dețin un Mac, pachetele disponibile sunt adesea întârziate cu câteva versiuni în spatele celorlalte platforme.


</div>


<div class="mw-translate-fuzzy">

1.  Descărcați un pachet arhivat corepunzător versiunii dvs de la [download page](https://github.com/FreeCAD/FreeCAD/releases).
2.  Deschideți folderul Downloads, și expandați fișierul zip descărcat: ![](images/Freecad-mac-01.jpg )
3.  Glisați aplicația FreeCAD din interiorul arhevei în dosarul Aplicații: ![](images/Freecad-mac-02.jpg )
4.  Gata, asta e, FreeCAD este isntalat! ![](images/Freecad-mac-03.jpg )

5\. Dacă sistemul previne lansarea FreeCAD, din cauza restricțiiilor pentru aplicațiile care nu provin din magazinul de aplicații, va trebui să-l activați din setările de sistem:![](images/Freecad-mac-04.jpg )


</div>

### Dezinstalare


<div class="mw-translate-fuzzy">

Sperăm că nu veți dori să faceți acest lucru, dar este bine să-l știți oricum. Sub Windows și Linux, dezinstalarea FreeCAD este foarte simplă. Utilizați opțiunea standard \"eliminați software\" găsită în panoul de control din Windows sau eliminați-o cu același manager de software pe care l-ați folosit pentru a instala FreeCAD pe Linux. Pe Mac, tot ce trebuie să faceți este să îl eliminați din dosarul Aplicații.


</div>

### Definirea preferințelor de bază 


<div class="mw-translate-fuzzy">

Odată ce ați instalat FreeCAD, este posibil să doriți să îl deschideți și să setați câteva preferințe. Definirea de preferințe din FreeCAD sunt localizate în meniu**Edit -\> Preferences** Puteți să răsfoiți paginile diferite pentru a vedea dacă există altceva pe care doriți să-l schimbați, dar aici sunt câteva dintre cele de bază:


</div>


<div class="mw-translate-fuzzy">

1.  **Language**: FreeCAD va prelua aatomat limba sistemul dvs de operare, dar dacă vreți să puteți schimba asta. FreeCAD este aproape în întregime tradus în 5 sau 6 limbi, plus multe altele care în prezent sunt doar parțial traduse. Puteți ușor:[help to translate FreeCAD](https://crowdin.com/project/freecad). ![](images/Freecad-basic-options01.jpg )
2.  **Auto-load module**: În mod normal, FreeCAD va începe să vă afișeze pagina centrului de start. Puteți trece peste acest lucru și puteți începe o sesiune FreeCAD direct în atelierul de lucru ales de dumneavoastră.[Workbenches](Workbenches.md) va fi explicat în detaliu în [next chapter](Manual_The_FreeCAD_Interface.md).
3.  **Create document at startup**: Combinat cu opțiunea de mai sus, acest lucru pornește FreeCAD gata de muncă. ![](images/Freecad-basic-options02.jpg )
4.  **Storage options**: Ca orice aplicație complexă, FreeCAD ar putea să se prăbușească din când în când. Aici puteți configura câteva opțiuni care vă vor ajuta să vă recuperați activitatea în caz de accident.
5.  **Authoring and license**: Puteți defini setările implicite care vor fi utilizate pentru fișierele dvs. noi. Luați în considerare posibilitatea de a face ca fișierele dvs. să poată fi redistribuite chiar de la început,[copyleft](https://en.wikipedia.org/wiki/Copyleft) licențiate ca [Creative Commons](https://creativecommons.org/).
6.  **Redirect python messages to output view**:

Aceste două opțiuni sunt întotdeauna bune pentru a fi marcate, deoarece acestea vă vor permite să vedeți ce este greșit în RaportView atunci când există o problemă cu rularea unui anumit script python. ![](images/Freecad-basic-options03.jpg )

1.  **Units**: aici puteți defini sistemul implicit de unități de măsură pe care doriți să-l utilizați. ![](images/Freecad-basic-options04.jpg )


</div>

### Instalarea de conținut adițional 


<div class="mw-translate-fuzzy">

Pe masura ce proiectul FreeCAD si comunitatea sa cresc rapid si pentru ca este usor de extins, contributiile externe si proiectele secundare facute de membrii comunitatii si de alti entuziasti incep sa apara pretutindeni pe internet. Se face un efort pentru a strânge toate aceste adăugiri interesante într-un singur loc, pe[FreeCAD github page](https://github.com/FreeCAD). Acolo, printre alte lucruri, vei găsi:


</div>


<div class="mw-translate-fuzzy">

1.  O bilbiotecă [Parts library](https://github.com/FreeCAD/FreeCAD-library), care conține toate tipurile de modele utile sau de modele create de utilizatorii FreeCAD care pot fi utilizate în mod gratuit în proiectele dvs. Biblioteca poate fi utilizată și accesată chiar de la instalarea FreeCAD.
2.  O colecție de [collection of addons](https://github.com/FreeCAD/FreeCAD-addons), cea mai mare parte dintre ei ateliere adiționale, care extind funcționalitatea FreeCAD pentru anumite sarcini. Instrucțiuni pentru instalare sunt date separate pe fiecare pagină complementară de addon.
3.  O colecție [collection of macros](https://github.com/FreeCAD/FreeCAD-macros), care este de asemenea disponibilă [on the FreeCAD wiki](Macros_recipes.md) cu documentație despre cum se utilizeză. Wikipedia conține mult mai multe macrocomenzi.


</div>

<img alt="" src=images/FreeCAD-addon-manager01.jpg  style="width:800px;">

If you are using the Ubuntu operating system, some of the addons above are also available as packages on the [FreeCAD addons PPA](https://launchpad.net/freecad-extras)

**De citit în plus**


<div class="mw-translate-fuzzy">

-   [More download options](Download.md)
-   [Detailed installation instructions](Installing.md)
-   [FreeCAD PPA for Ubuntu](https://launchpad.net/~freecad-maintainers)
-   [FreeCAD addons PPA for Ubuntu](https://launchpad.net/freecad-extras)
-   [compile FreeCAD yourself](Compiling.md)
-   [FreeCAD translations](https://crowdin.com/project/freecad)
-   [FreeCAD github page](https://github.com/FreeCAD)


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Installing/ro
