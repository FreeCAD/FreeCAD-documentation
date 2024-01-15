# FEM Solver/pl
## Przedmowa

Ta strona zawiera informacje o solverach metody elementów skończonych (MES) używanych przez [środowisko pracy MES](FEM_Workbench/pl.md). Interfejs pomiędzy solverem i programem FreeCAD w czasie preprocessingu i postprocessingu jest oparty o pliki tekstowe. Oznacza to, że teoretycznie każdy solver, który można konfigurować i kontrolować poprzez pliki tekstowe nadaje się do pracy z FreeCAD. Żeby ta komunikacja działała, potrzebny jest odpowiedni kod parsujący i zapisujący pliki wejściowe i wyjściowe. Wątek na forum omawiający i zapowiadający wszelkie zmiany związane z różnymi solverami można znaleźć [tutaj](https://forum.freecadweb.org/viewtopic.php?f=18&t=26326).

Na Wikipedii jest [lista wielu pakietów metody elementów skończonych](https://en.wikipedia.org/wiki/List_of_finite_element_software_packages). Porównanie można zaś znaleźć na stronie [feacompare.com](https://feacompare.com/).



### Dostępne solvery w różnych dystrybucjach Linuxa 

Repozytorium [FreeCAD-dependencies](https://github.com/luzpaz/FreeCAD-dependencies) śledzi zależności programu FreeCAD dla wielu dystrybucji Linuxa. Strona [FEM.md](https://github.com/luzpaz/FreeCAD-dependencies/blob/master/FC-Workbenches/FEM.md) skupia się na dostępnych otwartych solverach MES, które mogłyby być używane ze [środowiskiem pracy MES](FEM_Workbench/pl.md). Ta strona uwzględnia wersję danego solvera w repozytorium danej dystrybucji Linuxa. Te informacje są przydatne jeśli solver jest aktualny lub nieaktualny i musi być zaktualizowany.

Te informacje są również omawiane w wątku o [wspieranych i niewspieranych solverach](https://forum.freecadweb.org/viewtopic.php?f=18&t=26326&start=10#p270325) na forum.



## Solvery z interfejsem we FreeCAD 

Te solvery są dobrze zintegrowane z programem FreeCAD, co oznacza, że można ustawić i uruchomić analizę przy pomocy środowiska graficznego i przycisków środowiska pracy MES.



### CalculiX

To pierwszy solver jaki został zintegrowany do pracy w środowisku MES. CalculiX jest zaprojektowany głównie do analiz statycznych, termomechanicznych i modalnych. Więcej informacji o nim można znaleźć na stronie [MES: CalculiX](FEM_CalculiX/pl.md).

### Elmer

Solver do zagadnień sprzężonych Elmer został zintegrowany z programem FreeCAD w ramach [projektu Google Summer of Code 2017](Google_Summer_of_Code_2017.md): [strona główna](https://www.csc.fi/web/elmer), [portal społeczności](http://www.elmerfem.org./), [repozytorium kodu źródłowego](https://github.com/ElmerCSC/elmerfem), [Elmer Integration (GSoC) - Activity Log (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=22576).

### Mystran

Mystran to program do analiz strukturalnych, który korzysta z formatu plików wejściowych Nastran. Jest dostępny w ramach licencji MIT. Oznacza to, że może być uznawany za otwarty. Zobacz [stronę główną](https://www.mystran.com/), [repozytorium kodu źródłowego](https://github.com/dr-bill-c/MYSTRAN) i [Mystran-FreeCAD-forum (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?t=46171).

### Z88

Solver Z88 jest zaprojektowany do liniowych analiz statycznych z naciskiem na nauczanie metody elementów skończonych. Było to drugi solver [zintegrowany z FreeCAD](https://forum.freecadweb.org/viewtopic.php?f=18&t=15568). Później jego integracja została usprawniona w ramach [projektu Google Summer of Code 2017](Google_Summer_of_Code_2017.md).

Zobacz:

-   [Strona główna](https://en.z88.de/z88os/), [strona pobierania](https://en.z88.de/download-z88os/), [repozytorium kodu źródłowego](https://github.com/LSCAD/Z88OS) (i prekompilowane pliki wykonywalne).
-   Informacje o wydaniu: [Z88os V15 wydany 17.07.2017](https://forum.z88.de/viewtopic.php?f=18&t=885), [Z88os V13 wydany 20.05.2009](https://forum.z88.de/viewtopic.php?t=90) (wersja w Debian Jessie 8, Stretch 9, Buster 10).
-   [How to use Z88 in FEM? (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?t=23318).

Istnieją dwie wersje, Z88OS to wersja z otwartym kodem źródłowym, podczas gdy Z88Aurora to freeware i uwzględnia interfejs graficzny oraz dodatkowe metody rozwiązywania.



## Solvery zaimplementowane jako zewnętrzne środowiska pracy 

Te solvery nie są zintegrowane ze [środowiskiem pracy MES](FEM_Workbench/pl.md), co oznacza, że potrzebują odrębnego interfejsu do ustawienia symulacji. Jest to osiągane poprzez [makra](Macros/pl.md) lub [zewnętrzne środowiska pracy](External_workbenches/pl.md).

### DualSPHysics

[DualSPHysics](https://dual.sphysics.org/) to zestaw bibliotek C++, CUDA i Java używających [metody smoothed particle hydrodynamics](https://en.wikipedia.org/wiki/Smoothed-particle_hydrodynamics) (SPH) nazwany [SPHysics](https://wiki.manchester.ac.uk/sphysics/index.php/Main_Page) do analizowania przepływów z wolną powierzchnią, takich jak fale.

DesignSPHysics to zewnętrzne środowisko wbudowane we FreeCAD, które zapewnia interfejs graficzny dla DualSPHysics: [strona główna](https://design.sphysics.org/), [repozytorium kodu źródłowego](https://github.com/dualsphysics/DesignSPHysics), [Interesting project: DesignSPHysics fluid simulator (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=20595).

DesignSPHysics można zainstalować poprzez [menedżer dodatków](Std_AddonMgr/pl.md).



### FastHenry i FasterCap 

FastHenry i FasterCap to solvery pól indukcyjno-opornościowych i pojemnościowych opracowane przez FastFieldSolvers: [strona główna](https://www.fastfieldsolvers.com/default.asp), [strona pobierania](https://www.fastfieldsolvers.com/download.htm) (pliki wykonywalne i kod źródłowy), [forum](https://www.fastfieldsolvers.com/forum/).

The [środowisko pracy EM](EM_Workbench/pl.md) to zewnętrzny moduł, który został stworzony aby służyć jako interfejs do tych solverów elektromagnetycznych. FastHenry, do analiz magneto-quasistatycznych 3D impedancji jest w pełni wspierany, podczas gdy FasterCap jest dostępny przez pewne makra w Python.

Zobacz: [ElectroMagnetic Workbench (główny wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=9&t=33372) , [Electromagnetic Workbench - again.. (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=31920), [FreeCAD for ElectroMagnetics (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=5400), [repozytorium kodu źródłowego środowiska pracy](https://github.com/ediloren/EM-Workbench-for-FreeCAD).

Środowisko pracy EM można zainstalować poprzez [menedżer dodatków](Std_AddonMgr/pl.md).

### fcFEM

fcFEM to solver MES do zagadnień strukturalnych, zaimplementowany w Python, który można uruchomić bezpośrednio z FreeCAD bez wywoływania plików wykonywalnych zewnętrznych solverów. Zatem można go uznać za własny solver programu FreeCAD.

fcFEM został zaprojektowany aby ominąć pewne ograniczenia innych solverów, takich jak CalculiX, aby przeprowadzać różne analizy strukturalne.

Niektóre problemy, które ten solver ma ominąć to

-   Analizy na mieszanych siatkach (bryłowo-powłokowych) do symulacji kompozytowych słupów lub prefabrykowanych komponentów architektonicznych: [typy obiektów MES (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=21029&p=216682&hilit=sandwich#p216682).
-   Ulepszone elementy belkowe i powłokowe, ponieważ elementy belkowe solvera CalculiX wydają się dawać złe wyniki: [element belkowy 3-węzłowy CalculiX (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=27903&hilit=beam#p226038), [typy obiektów MES (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=21029&start=100), [przykład analizy 1D (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=16044).
-   Sterowanie długością łuku do przekraczania punktów bifurkacji w sprężysto-plastycznych analizach wyboczeniowych: [MES - rurowe połączenie z elementami powłokowymi (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=24&t=26921&hilit=riks#p215325).
-   Elementy o zerowej grubości do modelowania połączeń w różnych zastosowaniach, takich jak beton sprężony z tarciem: [sprężony most betonowy (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=30286&hilit=classical&start=20#p259636).

Autor uważa FreeCAD za dobrą platformę do prototypowania, pozwalającą szybko ustawić, przetestować i zwizualizować różne zagadnienia strukturalne, więc posiadanie zintegrowanego solvera o większych możliwościach byłoby bardzo pomocne. Zobacz [fcFEM - FEA from start to finish (główny wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=33974).

fcFEM jest udostępniany jako biblioteka Python i makro i można go pobrać z [repozytorium GitHub](https://github.com/HarryvL/fcFEM). Finalnie ma być dostępny z poziomu [menedżera dodatków](Std_AddonMgr/pl.md) lub jako część programu FreeCAD.

### OpenFoam

[OpenFoam](https://openfoam.org/) to potężne środowisko do symulacji z dziedziny [obliczeniowej mechaniki płynów](https://pl.wikipedia.org/wiki/Obliczeniowa_mechanika_p%C5%82yn%C3%B3w) (CFD), udostępniane jako seria bibliotek C++.

OpenFoam jest dostępny we FreeCAD poprzez dwa zewnętrzne środowiska:

-   [Cfd](https://github.com/qingfengxia/Cfd), pierwotnie autorstwa Qingfeng Xia.
-   [CfdOF](https://github.com/jaheyns/CfdOF), fork Cfd, skupiający się na łatwości użycia.

Podczas gdy Cfd ma na celu oferować kompletny zestaw funkcjonalności dla zaawansowanych użytkowników, CfdOF skupia się na użytkownikach, którzy dopiero zaczynają pracę z CFD i OpenFoam.

Dla Cfd: [aktualizacja o FreeCAD + OpenFOAM (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=13699), [Postęp w ogólnym środowisku CFD: CfdWorkbench (stary wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=37&t=22993).

Dla CfdOF: [Środowisko CFD korzystające z OpenFOAM (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=21576), [materiały szkoleniowe](http://opensim.co.za/training.html).

Oba środowiska można zainstalować poprzez [menedżer dodatków](Std_AddonMgr/pl.md) i oba mają swoje miejsce do dyskusji na forum [CfdOF / CFD](https://forum.freecadweb.org/viewforum.php?f=37).



## Implementacja w toku 

### FEniCS

FEnicS to środowisko obliczeniowe do rozwiązywania równań różniczkowych cząstkowych (PDE) z interfejsem programistycznym wysokiego poziomu w Python i C++. Może być używane do opisywania zagadnień naukowych przy pomocy sformułowań metody elementów skończonych a następnie rozwiązywania ich numerycznie.

Zobacz: [strona główna](https://fenicsproject.org/), [Fenics jako solver (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=4677).

[FenicsSolver](https://github.com/qingfengxia/FenicsSolver) to platforma do symulacji do zagadnień wielobryłowych, sprzężonych i wieloskalowych. Celem jest integracja solvera FEniCS do zarówno [środowiska pracy MES](FEM_Workbench/pl.md), jak i [zewnętrznego środowiska](External_workbenches/pl.md) Cfd, więc uzyskany system funkcjonuje jako darmowa alternatywa dla Comsola lub Moose. FenicsSolver jest opracowywany przez autora środowiska Cfd.

### OOFEM

[OOFEM](http://www.oofem.org/) to zorientowany obiektowo program MES tworzony przez Czeski Uniwersytet Techniczny do rozwiązywania zagadnień mechanicznych, przenoszenia masy i przepływowych.

Wspomniane były pewne jego zalety w stosunku do CalculiX, takie jak elementy do modelowania połączeń ([sprężony most betonowy (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=30286&start=20#p260275)) i sterowanie długością łuku do sprężysto-plastycznych analiz wyboczeniowych ([MES - połączenie rurowe z elementami powłokowymi (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=24&t=26921&hilit=Arc#p215325)).

Wstępna integracja ze środowiskiem pracy MES została dokonana. Zobacz: [OOFem (główny wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=31288), [prośba o test, wiele solverów (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?t=15568&start=20#p126338).

Dopóki integracja solvera nie zostanie ukończona i nowy kod nie zostanie wprowadzony do głównego repozytorium FreeCAD, pliki wymagane do używania tego solvera w środowisku pracy MES będzie można pobrać z [tego repozytorium](https://github.com/berndhahnebach/FreeCAD_bhb/tree/femoofem/src/Mod/Fem/). Aby zobaczyć przegląd implementacji, przejrzyj bardzo czystą historię zmian <https://github.com/berndhahnebach/FreeCAD_bhb/commits/femoofem>

### MBDyn

-   Otwarty program do analiz dynamiki bryły sztywnych ogólnego przeznaczenia
-   [MBDyn](https://www.mbdyn.org/)
-   [FreeCAD jako pre-postprocessor do MBDyn (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=39165)



## Solvery niezintegrowane 

Następujące solvery nie zostały zintegrowane z FreeCAD, ale wywołały pewne zainteresowanie społeczności użytkowników. Jeśli developer chce utworzyć interfejs do komunikacji z danym solverem, powinien zajrzeć na [forum MES](https://forum.freecadweb.org/viewforum.php?f=18) aby uzyskać rady i wsparcie.

Następujące strony mogą być nieaktualne, ale informacje na nich zawarte mogą nadal być przydatne do zrozumienia jak integrować solvery z FreeCAD

-   [Rozszerzenie modułu MES](Extend_FEM_Module/pl.md)
-   [Poradnik: Dodawanie równań w środowisku MES](Add_FEM_Equation_Tutorial/pl.md)
-   [Poradnik: Dodawanie wiązań w środowisku MES](Add_FEM_Constraint_Tutorial/pl.md)

### ADAPy

Zobacz [ADAPy](https://github.com/Krande/adapy/) i [ADA - Assembly for Design & Analysis (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=64929).

### Agros2D and Hermes 

[Agros2D](http://www.agros2d.org/) to wieloplatformowy program graficzny zaprojektowany do rozwiązywania różnych zagadnień fizycznych. Wewnątrz korzysta z bibliotek C++ [Hermes](http://www.hpfem.org/hermes/) do rozwiązywania prostych i złożonych równań różniczkowych cząstkowych (PDE) z zależnością od czasu przy pomocy ogólnej wersji metody elementów skończonych [(hp-FEM)](https://en.wikipedia.org/wiki/Hp-FEM). Główny kod [repozytorium](https://github.com/hpfem/hermes) i [poradniki](https://github.com/hpfem/hermes-tutorial).



### Code-Aster i Code-Saturne 

[Code-Aster](https://www.code-aster.org/) to otwarty solver do zagadnień sprzężonych, razem z preprocessorem Salomé-Meca tworzą platformę do symulacji opracowaną przez EDF-GDF, największą firmę energetyczną we Francji. Był już dawno rozważany do uwzględnienia we FreeCAD: [FreeCAD i Code-Aster/Salome-Meca (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?t=2839).

[Code-Saturne](https://www.code-saturne.org/cms/) to darmowy, otwarty program opracowany i udostępniany przez EDF do rozwiązywania zagadnień obliczeniowej mechaniki płynów (CFD).

### FElt

[FElt](http://felt.sourceforge.net/) to pakiet metody elementów skończonych do rozwiązywania zagadnień liniowych statycznych i dynamicznych mechaniki konstrukcji. [Oryginalny kod](https://sourceforge.net/projects/felt/) jest nieaktualny, więc powstał fork w [nowym repozytorium](https://github.com/Sudhanshu-Dubey14/felt) aby odnowić projekt i umożliwić jego kompilację we współczesnych systemach.

Na forum zasugerowano przeprowadzanie analiz ram betonowych (złożeń belek i słupów) przy pomocy elementów belkowych 1D: [Automatyzacja w projektowaniu (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=17061&start=20#p268503), [Felt w środowisku pracy MES (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=33463).

### Frame3DD

[Frame3DD](http://frame3dd.sourceforge.net/) to pakiet oprogramowania do analiz statycznych i dynamicznych ram i kratownic 2D i 3D, [główne repozytorium](https://github.com/pslack/frame3dd). Wstępny kod do odczytu plików wejściowych został ogłoszony na forum: [Test czytania danych z pliku Frame3DD](https://forum.freecadweb.org/viewtopic.php?f=24&t=19428). Ogólny wątek na forum MES: [Frame3DD](https://forum.freecadweb.org/viewtopic.php?f=18&t=43389).

### Impact FEM 

-   <https://sourceforge.net/projects/impact/>

### libMesh

[libMesh](https://libmesh.github.io/) to biblioteka C++ metody elementów skończonych do numerycznego rozwiązywania równań różniczkowych cząstkowych, której głównym celem jest zapewnienie wsparcia dla obliczeń z użyciem adaptacyjnego zagęszczania siatki (adaptive mesh refinement - AMR) przy pomocy wielu rdzeni: [repozytorium kodu źródłowego](https://github.com/libMesh/libmesh).

Sugerowano integrację tej biblioteki z FreeCAD jako część [projektu Google Summer of Code](Google_Summer_of_Code.md): [GSOC 2019 Configuration Management Project (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=8&t=35493).

### Modelica

[Modelica](https://www.modelica.org/) to język do modelowania i optymalizacji złożonych i wzajemnie połączonych układów fizycznych, przykładowo mechanicznych, elektrycznych, termicznych, hydraulicznych i innych. Sam język i jego standardowe biblioteki są otwarte. Niektóre środowiska do symulacji oparte na Modelice, jak Dymola, są komercyjne, ale istnieją też darmowe implementacje jak [OpenModelica](https://openmodelica.org/) i [JModelica](https://jmodelica.org/).

Sugerowano użycie środowiska Modelicia we FreeCAD do wsparcia tworzenia animacji, ale szerzej mogłoby ono być wykorzystywane w inżynierii mechanicznej i budowlanej do rozwiązywania równań i optymalizacji projektów: [Modelica (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=32556).

Pakiet [PyFMI](https://pypi.org/project/PyFMI/) zawiera powiązania Pythona do pracy z modelami FMU, które są ustandaryzowanymi modelami w formacie binarnym tworzonymi przez środowiska zgodne z Modelica, wliczając Dymola, OpenModelica i JModelica. Sugerowano, iż ta biblioteka mogłaby pomóc połączyć program FreeCAD ze [środowiskiem Modelica](https://forum.freecadweb.org/viewtopic.php?f=18&t=32556#p272632) (wątek na forum).

### Mumps

[Mumps](http://mumps-solver.org/) to ogólny solver do ogromnych układów równań, które przede wszystkim zajmuje się faktoryzacją i operacjami na rzadkich macierzach. Był wspomniany na forum: [Prośba o test, wiele solverów (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?t=15568&start=20#p126087).

Nie przeprowadza analiz MES bezpośrednio, ale może być używany wewnętrznie przez inne pakiety, takie jak Code-Aster.

### Nastran

Nastran to program do analiz strukturalnych opracowany przez NASA w latach 70. Jego współczesne wersje są komercyjne i zamknięte, ale starsze wersje, [Nastran-93](https://github.com/nasa/NASTRAN-93) i [Nastran-95](https://github.com/nasa/NASTRAN-95) zostały udostępnione jako otwarte w 2015 r. Dyskusja: [Nastran (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=12753).

Nie ma wsparcia technicznego dla wersji z otwartym kodem źródłowym i prawdopodobnie ciężko ją skompilować we współczesnym systemie.

### OpenSees

[OpenSees](https://opensees.berkeley.edu/) to środowisko do tworzenia aplikacji do symulacji zagadnień strukturalnych i geotechnicznych, głównie w dziedzinie inżynierii sejsmicznej. [OpenSees, otwarty system do symulacji z dziedziny inżynierii sejsmicznej (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=20745) i [Relicencjonowanie OpenSees (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=31922).

### PolyFEM

[PolyFEM](https://polyfem.github.io/) to prosta biblioteka metody elementów skończonych C++ i Pythona. Zapewnia szeroki wybór równań różniczkowych cząstkowych, wliczając równania Laplace\'a, Helmholtza, liniowej sprężystości, sprężystości Saint-Venanta, sprężystości Neo-Hookean i Stokesa. [PolyFEM (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=42857).

### Sparselizard

[Sparselizard](http://www.sparselizard.org/) to szybka, ogólna, sprzężona, p-adaptacyjna, otwarta biblioteka MES działająca na systemach Linux, Mac i Windows. Jest używana do projektowania nowej generacji mikrourządzeń (przetworniki ultradźwiękowe, mikrolustra, mikrozawory, mikronapędy,\...) i jest ostrożnie weryfikowana przy pomocy rozwiązań analitycznych, innych programów i pomiarów wyprodukowanych urządzeń. Wydaje się być opracowana przez zespół tworzący generator siatek Gmsh.

### SU2

[SU2](https://su2code.github.io/) to zbiór narzędzi opracowanych w C++ i Python do rozwiązywania [równań różniczkowych cząstkowych](https://pl.wikipedia.org/wiki/R%C3%B3wnanie_r%C3%B3%C5%BCniczkowe_cz%C4%85stkowe) (PDE) i związanych z nimi zagadnień optymalizacji na nieregularnych siatkach. Jest głównie używany w aerodynamice i obliczeniowej mechanice płynów (CFD).



### Tochnog

Tochnog Professional to zamknięty program do symulacji geotechnicznych, takich jak osuwiska, wbijanie pali, stabilność zboczy i obliczenia w inżynierii budownictwa *(murarstwo i odpowiedź na trzęsienia ziemi)*, [strona projektu](https://www.tochnogprofessional.nl/).

Tochnog był z sukcesem używany we FreeCAD jako zamiennik dla CalculiX, chociaż wersja testowa ma ograniczenie liczby elementów: [Integracja solvera Tochong w środowisku pracy MES (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=26772).

### XC

[XC](http://www.xcengineering.xyz/) to program MES zaprojektowany do rozwiązywania zagadnień strukturalnych w inżynierii budownictwa, takich jak symulacji z użyciem prawdziwych elementów belkowych i powłokowych. Wewnątrz korzysta z bibliotek OpenSees: [główne repozytorium](https://github.com/xcfem/xc), [XC, otwarty kod do analiz strukturalnych MES (wątek na forum)](https://forum.freecadweb.org/viewtopic.php?f=18&t=31262).


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Solver/pl
