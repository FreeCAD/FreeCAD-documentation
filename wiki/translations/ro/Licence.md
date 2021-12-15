# Licence/ro
{{TOCright}}

## Licențe utilizate sub FreeCAD 

FreeCAD utilizează două licențe diferite, una pentru aplicația în sine și una pentru documentație:

**_** Toate sursele de cod FreeCAD poate fi găsit aici [official Git repository](https://github.com/FreeCAD/FreeCAD)


<div class="mw-translate-fuzzy">

**[Creative Commons Attribution 3.0 License (CC-BY-3.0)](http://creativecommons.org/licenses/by/3.0/)** For the documentation on <http://www.freecadweb.org>


</div>

See FreeCAD\'s [debian copyright file](http://sourceforge.net/p/free-cad/code/ci/master/tree/package/debian/copyright) pentru mai multe detalii despre licențele utilizate de diferitele componente open source găsite în FreeCAD

## Impactul licențelor 

Mai jos este o explicație mai prietenoasă despre ceea ce înseamnă licența LGPL pentru dvs.:

#### Toți utilizatorii 

Toți utilizatorii pot folosi, copia, modifica, redistribui, FreeCAD în mod gratuit, fără nici o restricție. Copia dvs. de FreeCAD este a dvs., precum și fișierele pe care le produceți cu FreeCAD.Nu sunteți obligați să actualizeze FreeCAD după un anumit timp. nici să schimbați utlizarea FreeCAD. Utilizarea FreeCAD nu le obligă la nici un fel de contract sau obligație.

Codul sursă al FreeCAD este public și poate fi inspectat. Prin urmare, este posibil să verificați că nu se fac lucruri fără știrea dvs., de exemplu prin trimiterea datelor dvs. private undeva.

#### Utilizatorii Profesionali 

Utilizatorii profesionali pot folosi FreeCAD în mod liber, pentru orice fel de muncă privată, comercială sau instituțională. Orice versiune de FreeCAD poate fi instalată și instalată oriunde, de ori câte ori doriți. Puteți de asemenea să modificați și să adaptați FreeCAD pentru scopurile dvs. fără nici o restricție. Cu toate acestea, nu puteți face dezvoltatorii FreeCAD răspunzători pentru orice daune comerciale sau pierderi care pot rezulta din utilizarea FreeCAD.

#### Deavoltatorii Open Source 

Puteți utiliza FreeCAD ca bază pentru a vă dezvolta propria aplicație sau o puteți extinde prin crearea de module noi pentru aceasta. Dacă FreeCAD este încorporat în propria dvs. aplicație, aveți posibilitatea să alegeți dintre licența GPL sau LGPL sau orice altă licență compatibilă cu LGPL pentru a permite utilizarea muncii dvs. în software-ul proprietar sau nu. Dacă dezvoltați un modul care să fie folosit ca extensie și nu includeți codul FreeCAD în el, puteți alege orice licență dorită. Cu toate acestea, dacă doriți să o utilizați cât de mult puteți, este o idee bună să utilizați aceeași licență ca FreeCAD în sine, astfel încât să poată fi accesată mai ușor în alte module viitoare sau chiar în FreeCAD.


<div class="mw-translate-fuzzy">

#### Commercial developers 

Puteți utiliza FreeCAD ca bază pentru propria aplicație și nu sunteți forțați să creați aplicația dvs. ca open source. Cu toate acestea, LGPL necesită două elemente de bază: 1) să informeze în mod clar utilizatorii că aplicația dvs. utilizează FreeCAD și FreeCAD este licențiată de LGPL și 2) să vă separați în mod clar propria aplicație de componentele FreeCAD. Acest lucru se face de obicei printr-o legătură dinamică cu componentele FreeCAD, permițând utilizatorilor să o modifice sau să pună la dispoziția utilizatorilor codul sursă al FreeCAD, precum și modificările aduse de dvs la acesta. Veți primi sprijin de la dezvoltatorii FreeCAD, atâta timp cât acest ajutor nu este pe o "stradă cu sens unic".


</div>


<div class="mw-translate-fuzzy">

#### Fișiere

Modelele și alte fișiere create cu FreeCAD nu sunt supuse niciunei licențe menționate mai sus și nu sunt legate de nici un fel de restricție sau de proprietate. Fișierele dvs. sunt cu adevărat ale tale. Puteți seta proprietarul fișierului și puteți specifica propriile condiții de licență pentru fișierele pe care le produceți în cadrul FreeCAD, prin meniul Fișier -\> Informații despre proiect.


</div>

## Declarația dezvoltatorului principal 

Știu că discuția despre \'\'\"dreptul\" \'\' licenței pentru open source a ocupat o parte semnificativă a lățimii de bandă a internetului și acesta este motivul pentru care, în opinia mea, FreeCAD ar trebui să aibă fie sub această licență LGPL.


<div class="mw-translate-fuzzy">

Am ales licențele LGPL și GPL pentru proiect, știu că există pro și anti LGPL și vă voi da câteva motive pentru această decizie.


</div>

FreeCAD este un amestec între o bibliotecă și o aplicație, deci GPL ar fi un pic mai puternic pentru aceasta. Aceasta ar împiedica scrierea de module comerciale pentru FreeCAD deoarece ar preveni legarea cu bibliotecile de bază FreeCAD. Puteți să întrebați de ce module comerciale ? Prin urmare, Linux este un bun exemplu. Ar fi Linux atât de reușit dacă Biblioteca GNU C ar fi GPL și, prin urmare, ar împiedica legarea aplicațiilor non-GPL? Și totuși, îmi place libertatea Linuxului și doresc să pot utiliza driverul grafic NVIDIA 3D. Înțeleg și accept motivul pentru care NVIDIA nu dorește să dea codul driverului. Muncim toți pentru întreprinderi/firme, și avem nevoie de bani, trebuie să cumpărăm cel puțin alimente\... Deci, pentru mine, coexistența open source și a a programelor proprietar nu este un lucru rău, atunci când se supune regulilor LGPL. Aș dori să văd un programator care scrie procesul de import/export Catia pentru FreeCAD și să-l distribuie gratuit sau pentru niște bani. Nu-mi place să-l forțez să dea mai mult decât vrea el. Nu ar fi bine nici pentru el nici pentru FreeCAD.

Această decizie se face numai pentru nucleul sistemul FreeCAD. Fiecare scriitor al unui modul de aplicație poate lua propria decizie.


{{Quote|Jürgen Riegel|15 October 2006}}


<div class="mw-translate-fuzzy">


{{docnav|Dialog creation|Tracker}}


</div>




_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Licence/ro
