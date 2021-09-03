


<div class="mw-translate-fuzzy">


{{docnav|Feature list|Install on Linux}}


</div>

Cea mai usoară cale de instalare sub Windows este de a descărca unul dintre programele de instalare de mai jos.


{{DownloadWindowsStable}}

Dupa ce fișierul .msi (Microsoft Installer) a fost descarcat, doar faceți dublu-click pe el pentru a începe instalarea.

Mai jos sunt descrise opțiunile de instalare. Daca pare complicat nu va ingrijorați! Cei mai mulți utilizatori nu vor avea nevoie de nimic mai mult decat fișierul de mai sus .msi și articolul **[ Primii pasi](Getting_started/ro.md)**!

### Instalare Simpla Folosind Microsoft Installer 

Cea mai ușoară cale de **instalare a FreeCAD sub Windows** este de a folosi programul descărcabil de instalare de mai sus. Aceasta pagina descrie modul de folosire și funcționalitățile programului *Microsoft Installer* pentru a accesa mai multe opțiuni de instalare.

The easiest way to **install FreeCAD on Windows** is by using the downloadable installer bundle above. This page describes the usage and features of the *NSIS Installer* for more installation options.

Daca doriți sa descărcați versiunea pe 64 de biți sau versiunea aflată acum în dezvoltare (care ar putea fi instabilă) vizitați pagina de [descărcări](Download/ro.md).

## Chocolatey

However, it is highly recommended that you use a package manager such as Chocolatey to keep your software updated. You can installed Chocolatey following [these instructions](https://chocolatey.org/install) and then open a PowerShell terminal as admin and run:


```python
choco install freecad
```

every once in a while you can update your software with


```python
choco upgrade freecad
```

to get the latest version available on Chocolatey repository. If there are any issues with the chocolatey package, you may contact maintainers on [this page](https://chocolatey.org/packages/freecad).

### Instalare de la Consola de Comandă 

Cu ajutorul utilitarului linie de comandă \"msiexec.exe\", sunt disponibile funcții suplimentare, cum ar fi instalarea non-interactivă și instalarea ca administrator. Vedeți exemplele de mai jos.

With the *msiexec.exe* command line utility, additional features such as non-interactive installation and administrative installation are available. See examples below.

#### Instalarea Automată 

Folosind comanda:

With the command line


```python
msiexec /i FreeCAD<version>.msi
```

instalarea poate fi inițiată programat. Parametrii suplimentari pot fi transmiși la sfârșitul liniei de comandă, de exemplu:


```python
msiexec /i FreeCAD-2.5.msi TARGETDIR=R:\FreeCAD25
```

#### Interfața Limitată 

Numărul de ferestre de dialog permise utilizatorului poate fi controlat cu grupul de optiuni /q, astfel:

The amount of user control permitted by the installer can be controlled with /q options:


<div class="mw-translate-fuzzy">

-   /qn - fără interfață
-   /qb - interfață minimală - o fereastră ce indica doar progresul având butonul Cancel
-   /qb! - precum/qb, dar fără butonul \"renunță\" (Cancel)
-   /qr - interfață redusă - prezintă toate ferestrele dar nu solicită intervenția utilizatorului

(sare peste toate dialogurile modale)

-   /qn+ - precum /qn, dar afișează mesajul \"Completed\" la sfârșit
-   /qb+ - precum /qb, dar afișează mesajul \"Completed\" la sfârșit


</div>

#### Directorul Țintă 

Proprietatea TARGETDIR determină locația de instalare a FreeCAD. De exemplu o locație se specifică folosind

The property TARGETDIR determines the root directory of the FreeCAD installation. For example, a different installation drive can be specified with


```python
TARGETDIR=R:\FreeCAD25
```

Implicit TARGETDIR este \[WindowsVolume\\Programm Files\\\]FreeCAD.

#### Instalarea Pentru Toti Utilizatorii 

Adaugand

Adding


```python
ALLUSERS=1
```

determină o instalare utilizabilă de către toți utilizatorii. În mod implicit, o instalare non-interactivă (/ i) face ca pachetul să poată fi utilizat numai de utilizatorul curent (cel care efectuează instalarea); o instalare interactivă prezintă un dialog care implică \"toți utilizatorii\" dacă utilizatorul care realizează instalarea are suficiente drepturi de administrare.

#### Selectarea Caracteristicilor 

Un numar de caracteristici pot fi alese pentru instalare, reinstalate sau indepartate. Cracteristicile ce pot fi selectate pentru FreeCAD sunt:

A number of properties allow selection of features to be installed, reinstalled, or removed. The set of features for the FreeCAD installer is

-   DefaultFeature - instaleaza pachetul software propriu-zis și nucleul de librării utilizate
-   Documentation - instalează documentația
-   Source code - instalează codul sursă
-   \... ToDo

In plus, optiunea ALL activeaza toate caracteristicile. Toate componentele depind de DefaultFeature, astfel ca instalarea oricarei alteia va instala si caracteristicile implicite. Urmatoarele variabile controleaza caracteristicile instalate sau inlaturate:

-   ADDLOCAL - lista componentelor ce vor fi instalate în sistem
-   REMOVE - lista componentelor ce vor fi înlaturate din calculatorul local
-   ADDDEFAULT - lista componentelor adăugate în configurare implicită (local pentru toate funcționalitățile FreeCAD)
-   REINSTALL - lista componentelor ce vor fi reinstalate/reparate
-   ADVERTISE - lista funcționalităților care se instalează public

Pentru restul de proprietati disponibile consultati documentatia MSDN disponibila on-line.

Pe baza celor spuse mai sus, adaugand


```python
ADDLOCAL=Extensions
```

programul va instala interpretatorul si va inregistra extensiile dar nu instaleaza nimic altceva.

### Dezinstalarea

Folosind

With


```python
msiexec /x FreeCAD<version>.msi
```

FreeCAD poate fi dezinstalat. Daca fisierul .msi nu este disponibil pachetul poate fi dezinstalat folosind codul prodsului sau pachetului. Codul produsului poate fi aflat exminand proprietatile scurtaturii Uninstall pe care FreeCAD o instaleaza in meniul Start.

### Instalare în rețea 

Folosind

With


```python
msiexec /a FreeCAD<version>.msi
```

o instalare \"administrativa\" (in retea) poate fi realizata. Fisierele sunt extrase in directorul tinta (care trebuie sa fie un director de retea), dat nici o alta modificare nu este adusa calculatorului local. In plus, un fisier .msi (de dimensiuni reduse) este generat in directorul tinta. Utilizatorii calculatorului tinta pot folosi apoi fisierul .msi generat pentru instalare (e posibil ca versiunile viitoare sa ofere posibilitatea stocarii unor fisiere in directorul de retea (comun)).

Pentru instalarea administrativa nu exista interfata grafica, astfel ca directorul de retea trebuie specificat la linia de comanda.

Nu există nici o procedură de dezinstalare specifică pentru o instalare de administrator - doar ștergeți directorul țintă în cazul în care nici un client nu-l mai folosește.

### Publicitate

Folosind

With


```python
msiexec /jm FreeCAD<version>.msi
```

ar fi posibil, în principiu, sa \"publicam\" FreeCAD la un calculator (cu /ju la un utilizator). Acest lucru ar face pictogramele să apară în meniul de start și extensiile să fie înregistrate, fără ca software-ului sa fie instalat. Prima utilizare a unei funcționalități ar conduce la instalarea sa.

Instalatorul FreeCAD acceptă în prezent doar \"publicitate\" pentru intrări in meniul Start, nu și pentru comenzi rapide.

### Instalare Automata pe un Grup de Calculatoare 

Folosind Windows Group Policy este posibil sa se instaleze FreeCAD automat pe un grup de calculatoare. Pentru a face asta urmați următorii pași:

1.  Autentificați-vă în controlller-ul de domeniu
2.  Copiați fișierul MSI intr-un director partajat la care au acces toate calculatoarele
3.  Deschideți \"Active Directory users and computers\"
4.  Navigați la grupul de calculatoare pe care se instalează FreeCAD
5.  Deschideți Proprietăț
6.  Deschideți Politici de Grup
7.  Adaugati o noua politica și editați-o
8.  In Configurări Calculator/Instalare soft selectați Nou/Pachet
9.  Selectați fișierul MSI folosind calea de rețea
10. Puteți opta ca FreeCAD să fie dezinstalat dacă părăsește rețeaua

With Windows Group Policy, it is possible to automatically install FreeCAD on a group of machines. To do so, perform the following steps:

1.  Log on to the domain controller
2.  Copy the MSI file into a folder that is shared with access granted to all target machines.
3.  Open the MMC snapin \"Active Directory users and computers\"
4.  Navigate to the group of computers that need FreeCAD
5.  Open Properties
6.  Open Group Policies
7.  Add a new policy, and edit it
8.  In Computer Configuration/Software Installation, choose New/Package
9.  Select the MSI file through the network path
10. Optionally, select that you want FreeCAD to be de-installed if the computer leaves the scope of the policy.

Acest mod de instalare durează ceva timp, de obicei. Pentru finalizarea instalării toate calculatoarele trebuiesc repornite.

### Instalarea in Linux folosind Crossover Office 

Versiunea de FreeCAD pentru Windows poate fi instalată pe un sistem Linux folosind *CXOffice 5.0.1*. Rulați comanda *msiexec* de la linia de comandă CXOffice. Presupunând că pachetul de instalare se află în directorul \"soft\" pe discul \"Y:\":

```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```


```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

FreeCAD rulează dar s-a raportat că interfața OpenGL nu funcționează, la fel ca și în cazul altor programe rulate sub [Wine](wikipedia:Wine_(software).md), de exemplu Google [SketchUp](wikipedia:SketchUp.md).


<div class="mw-translate-fuzzy">


{{docnav|Feature list|Install on Linux}}


</div>



