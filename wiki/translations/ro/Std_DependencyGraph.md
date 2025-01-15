---
 GuiCommand:
   Name: Std DependencyGraph
   MenuLocation: Std Tools Menu , Dependency graph...
   Workbenches: All
---

# Std DependencyGraph/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

**Dependency graph** afișează dependețele între obiecte în documentul activ sub formă de graf. Spre deosebire de arborescența Model, obiectele sunt listate în ordine cronologică inversă, cu primul obiect creat în partea de jos.


</div>


<div class="mw-translate-fuzzy">

Poate fi util în analizarea unui document FreeCAD și în localizarea ramurilor într-o arborescență. Schema de dependență a graficului va depinde de ce Atelier de lucru a fost folosit pentru a crea obiectele din document. De exemplu, în FreeCAD 0.16, un model realizat exclusiv în Atelierul PartDesign ar trebui să afișeze un grafic de dependență liniară cu o singură ramificație verticală. Un model realizat cu Atelierul Part va avea multe ramuri, dar pentru o singură parte se vor alătura la început după operațiunile booleene. Dacă nu, înseamnă că acestea sunt obiecte separate.


</div>

Graficul de dependență este pur și simplu un instrument de vizualizare, prin urmare nu poate fi editat; se actualizează automat dacă se fac modificări ale modelului.

<img alt="" src=images/Std_DependencyGraph_example.svg  style="width:400px;"> ![](images/DependencyGraph1.png ) 

## Installation


<div class="mw-translate-fuzzy">

## Instalarea

Pentru a se utiliza Dependency graph, un software terț numit [Graphviz](http://graphviz.org/) trebuie să fie instalat prima dată. Dacă nu-l aveți preinstalat sau este instalat într-o locație neconvențională, FreeCAD va afișa următorul dialog: ![](images/FreeCAD-0.17-missing-Graphviz-error-dialogue.png )


</div>

![](images/FreeCAD-0.17-missing-Graphviz-error-dialogue.png )

### Windows


<div class="mw-translate-fuzzy">

### Windows 

Descărcați programul **graphviz-2.xx.msi** de instalare de la [Graphviz Download page](https://graphviz.gitlab.io/_pages/Download/Download_windows.html) și lansați-l pentru a instala


</div>

### macOS


<div class="mw-translate-fuzzy">

### Mac/OSX

Puteți instala graphviz folosind [Homebrew](https://brew.sh/):


</div>


{{Code|lang=text|code=
brew install graphviz
}}


<div class="mw-translate-fuzzy">

Aceasta instalează binarele graphviz sub / usr / local / bin. Din păcate, nu putem naviga direct din dialogul de fișiere care apare din FreeCAD → Instrumente → Graficul dependenței. Când obțineți dialogul de selectare a fișierelor, utilizați tastele Cmd + Shift + G pentru a obține un câmp de introducere pentru cale. Introduceți


</div>


{{Code|lang=text|code=
/usr/local/bin
}}

or:


{{Code|lang=text|code=
/opt/homebrew/bin
}}

și confirmați câmpul de introducere și dialogul de selectare a fișierelor.


<div class="mw-translate-fuzzy">

În cazul în care fișierele binare Graphviz sunt instalate într-o locație nestandard, încercați să găsiți programul împreună cu comanda:


</div>


{{Code|lang=text|code=
type dot
}}


<div class="mw-translate-fuzzy">

Se va emite ceva de genul


</div>


{{Code|lang=text|code=
dot is /usr/local/bin/dot
}}


<div class="mw-translate-fuzzy">

Și, prin urmare, puteți să îi spuneți lui FreeCAD să se uite în acel director.


</div>

If you don\'t have macOS Big Sur (11) (or higher) Homebrew might not work, but you can use [MacPorts](https://www.macports.org/index.php) instead. Just download the [appropriate version for your OS](https://www.macports.org/install.php). Once the installation is complete, enter this command in the [Terminal](https://en.wikipedia.org/wiki/Terminal_(macOS)):


{{Code|lang=text|code=
sudo port install graphviz
}}

Enter your password and wait while the dependencies are downloaded and installed (it can take some time).

The Graphviz binaries may be under **/usr/local/bin** or **/opt/local/bin/dot**. FreeCAD may automatically find the Graphviz program with the file dialog that comes up from **Tools → Dependency graph...**, if not enter this command:


{{Code|lang=text|code=
type dot
}}

It will output something like:


{{Code|lang=text|code=
dot is /opt/local/bin/dot
}}

And you can tell FreeCAD to look in that directory as explained before.

It is also possible to make the opt directory visible with this command:


{{Code|lang=text|code=
defaults write com.apple.finder AppleShowAllFiles YES;
}}

then:


{{Code|lang=text|code=
killall Finder /System/Library/CoreServices/Finder.app;
}}

Therefore you can tell FreeCAD to follow this path. It has been successfully tested on macOS 10.13 (High Sierra).

### Linux


<div class="mw-translate-fuzzy">

### Linux 

Sub cele mai multe distribuții Linux (Debian / Ubuntu, Fedora, OpenSUSE), trebuie doar să instalați pachetul grafic din colecțiile de depozitare. Cu toate acestea, în mod similar cu MacOSX, în cazurile în care binarele Graphviz sunt instalate într-o locație nestandardă, încercați să găsiți programul cu comanda:


</div>


{{Code|lang=text|code=
type dot
}}

Poate ieși ceva asemănător


{{Code|lang=text|code=
dot is /usr/local/bin/dot
}}

Și, prin urmare, puteți orienta FreeCAD să se uite în acel director.

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

1.  Mergeți la meniu **Tools → Dependency graph\...**
2.  Un nou tab întitulat **Dependency graph**

se deschide în zona principală a ferestrei FreeCAD.

1.  Utilizați rotița de derulare a mouse-ului pentru a mări / micșora imaginea.
2.  Utilizați cursorul orizontal din partea inferioară a ecranului pentru a panorama în lateral.


</div>

## Save


<div class="mw-translate-fuzzy">

## Save/Export

Puteți salva / exporta graficul de dependență afișat ca fișier imagine. În timp ce tab-ul Dependency graph este în prim plan:

-   Just choose **File** → [Save As](Std_SaveAs.md) to save the graph as a picture (PNG/BMP/GIF/JPG), a vector graphic (SVG) or as a PDF document.
-   **File** → [Export](Std_Export.md) or **Tools** → [Save picture](Std_ViewScreenShot.md) will **NOT** work.


</div>



## Principii Generale 


<div class="mw-translate-fuzzy">

-   Graficul afișează obiectele în ordine cronologică inversă, de jos în sus.
-   Direcția săgeților care arată dependențele trebuie să fie întotdeauna în jos, de la obiectul copil la obiectul părinte. O săgeată îndreptată indică o dependență ciclică, o problemă care trebuie rezolvată.
-   O schiță care conține legături către [ geometry extern](Sketcher_External.md) va avea un număr cu un sufix \"x\", în afară de săgeata care o leagă de părinți, indicând numărul de geometrie externă legat în schiță.
-   Obiectele pot avea dependențe față de mai mulți părinți. De exemplu, pentru un model construit în PartDesign, un buzunar poate fi legat de schița sa și de caracteristica Pad (Protrusion) care a venit înainte.
-   Se vor afișa dependențe nepermise (de exemplu, între o operațiune de Draft/Part și un element din cadrul unui [PartDesign Body](PartDesign_Body.md)) cu o săgeată roșie. Acest tip de link afișează, de obicei, o eroare \"Links go out of allowed scope\" în afișarea raportului.
-   [Container](Std_Part.md) și [PartDesign_Body](PartDesign_Body.md) își înglobează conținutul într-un cadru cu fundal aleatoriu colorat. Originea acestora include, de asemenea, conținutul lor (planuri și axe standard) într-un cadru.
-   [ Group](Std_Group.md) este afișat ca un singur element legat de conținutul său.


</div>



---
⏵ [documentation index](../README.md) > [3rd_Party](Category_3rd_Party.md) > Std DependencyGraph/ro
