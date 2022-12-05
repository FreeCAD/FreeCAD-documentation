---
- GuiCommand:/ro
   Name/ro:Arch BimServer‏‎‏‎
   Workbenches:[Arch](Arch_Workbench/ro.md)
   MenuLocation:Arch → Utilities → BIM server
   Shortcut:‏‎
   SeeAlso:
---

# WebTools BimServer/ro


</div>


<div class="mw-translate-fuzzy">

**Notă:** Începând cu FreeCAD v0.17, acest instrument a fost eliminat din Arch Workbench și face parte acum din [WebTools Workbench](WebTools_Workbench.md) pe care îl puteți instala prin meniul Tools → Addons Manager.


</div>

## Descriere


<div class="mw-translate-fuzzy">

Această comandă vă permite să interacționați cu o instanță [BIMServer](http://www.bimserver.org), să deschideți fișierele stocate pe serverul Bim și să salvați noi revizii ale acestor fișiere. BIMServer este un sistem gratuit de server open source, creat pentru a lucra cu fișierele IFC. În starea sa actuală, permite gestionarea proiectelor cu mai multe fișiere IFC și gestionarea reviziilor. Sistemul de baze de date extrem de extensibil și arhitectura plugin-ului permit, de asemenea, proiectarea unor instrumente avansate de interogare / validare și a fluxurilor de lucru fuzibile inteligente.


</div>

Pentru a utiliza această comandă, trebuie îndeplinite următoarele condiții:


<div class="mw-translate-fuzzy">

-   Modulele Python **json** și **requests** trebuie să fie instalate în prealabil pe sistemul dumneavoastră
-   Trebuie să aveți acces la o instanță BimServer (citiți documentația [BIMServer](https://github.com/opensourceBIM/BIMserver/wiki) pentru a instala un BIMServer local) și să aveți acreditări (login și parolă) pentru acel server. La momentul scrierii, versiunea stabilă a BIMServer este 1,4, dar vă recomandăm să instalați una dintre versiunile beta 1.5.X disponibile, care instalează automat multe plugin-uri (în versiunea 1.4 trebuie să instalați manual plugin-urile).
-   Toate transferurile de fișiere cu BIMServer se fac cu fișiere IFC. Prin urmare, trebuie să știți cum să lucrați cu [IFC files](Arch_IFC.md).


</div>

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Asigurați-vă că cerințele de mai sus sunt îndeplinite și că aveți acces la o instanță BIMServer care rulează
2.  Selectați meniul Arch -\> Utilities -\> **<img src="images/WebTools_BimServer.svg" width=16px> [BIM Server](Arch_BimServer.md)
**
3.  Apăsați butonul **Connect** și completați detaliile dvs. de acreditare
4.  Odată ce conexiunea cu serverul BIMServer a fost făcută, alegeți un proiect de lucru din caseta derulantă **Project**


</div>

## Opţiuni

![](images/Arch_Bimserver_panel.jpg )


<div class="mw-translate-fuzzy">

-   Dacă aceasta este prima dată când vă conectați la un BIMServer de pe FreeCAD, apăsați butonul **Connect**și completați URL-ul serverului, login-ul dvs. (care este întotdeauna o adresă de email) și parola în caseta de dialog care va apărea. Dacă doriți să vă conectați automat data viitoare când veți folosi comanda BimServer, bifați opțiunea \"\'save credentials\'\'\'(numele și parola dvs. nu sunt salvate de FreeCAD, ci doar o cookie de sesiune).
-   Odată ce FreeCAD s-a conectat cu succes la o instanță BIMServer, butonul **Connect** se va transforma în **Connected**. Faceți clic din nou pe buton pentru a vă deconecta. De asemenea, aceasta va șterge cookie-ul de sesiune stocat, deci va trebui să introduceți din nou datele dvs. de acreditare data viitoare.
-   Pentru a șterge manual cookie-ul de sesiune și pentru a reseta totul, puteți să ștergeți pur și simplu URL-ul BIMServer stocat în **Edit -\> Preferences -\> Arch -\> BimServer**.
-   Butonul **Open in browser** va deschide interfata web a serverului BIMServer fie in browserul web intern al FreeCAD, fie daca ați marcat acea opțiune în**Edit -\> Preferences -\> Arch -\> BimServer**, într-un browser web extern. Aceasta permite, de exemplu, crearea de proiecte noi sau analizarea conținutului stocat pe serverul BIMServer.


</div>

### Descărcarea reviziilor 

-   Caseta derulantă contextuală **Project** va afișa proiectele disponibile stocate pe serverul BIMServer. Alegeți una pentru a vedea reviziile disponibile pentru acel proiect.
-   Selectați o revizuire și faceți clic pe **Open** pentru a descărca și deschide fișierul IFC corespunzător acelei revizuiri în FreeCAD.
-   Când apăsați butonul **Open**, se va deschide o casetă de dialog pentru a vă permite să salvați fișierul IFC descărcat într-o locație la alegere înainte de a o deschide. Dacă apăsați **Cancel**, fișierul va fi salvat sub un nume temporar în directorul temporar al sistemului.

### Încărcarea reviziilor 


<div class="mw-translate-fuzzy">

-   Dacă doriți să încărcați o nouă versiune, asigurați-vă că proiectul potrivit a fost selectat în caseta derulantă **Project**
-   Alegeți **Root object** pe care doriți să îl încărcați. Trebuie să fie fie [Arch Site](Arch_Site.md), fie [Arch Building](Arch_Building.md). Numai obiectele aparținând acelui obiect rădăcină vor fi încărcate.
-   Scrieți un **Comentariu**, care va fi descrierea (numele) reviziei.
-   Apăsați butonul **Upload**. Se va deschide o casetă de dialog pentru a vă permite să salvați fișierul IFC produs într-o locație la alegere înainte de al încărca. Dacă apăsați **Cancel**, fișierul va fi salvat sub un nume temporar în directorul temporar al sistemului.


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > WebTools BimServer/ro
