# <img alt="Ikonka FreeCAD dla środowiska pracy EM" src=images/EMWorkbench.svg  style="width:64px;"> EM Workbench/pl






## Wprowadzenie

Środowisko pracy EM *(ElectroMagnetic)* zapewnia interfejs CAD do niektórych darmowych solwerów open source. Obecnie obsługuje on solwer impedancji magnetokwazistatycznej 3D [FastHenry](https://www.fastfieldsolvers.com/software.htm#fasthenry2) *(tj. ekstrakcję indukcyjności i rezystancji przy \"niskich\" częstotliwościach)*. Trwają prace nad obsługą solwera pojemności elektrostatycznej 3D [FasterCap](https://www.fastfieldsolvers.com/software.htm#fastercap).

<img alt="" src=images/Screenshot_EM_window.png  style="width:600px;">



## Instalacja

Środowisko pracy EM jest [zewnętrznym środowiskiem pracy](External_workbenches/pl.md), które można zainstalować z poziomu <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md) FreeCAD. Można to zrobić przez menu **Przybory → Menadżer dodatków**.

Solwery elektromagnetyczne FastHenry2 i FasterCap muszą być zainstalowane oddzielnie. Ich kody binarne oraz źródła są dostępne bezpłatnie na stronie [FastFieldSolvers](https://www.fastfieldsolvers.com).



## Użycie



### FastHenry

FastHenry to oprogramowanie do obliczania zależnych od częstotliwości indukcyjności własnych i wzajemnych oraz rezystancji ogólnej trójwymiarowej struktury przewodzącej w przybliżeniu magnetoquasistatic. Może również generować kompatybilne ze Spice, wieloczęstotliwościowe modele obwodów zastępczych.

Znajomość FastHenry jest warunkiem wstępnym do biegłego korzystania ze środowiska ElectroMagnetic dla FastHenry. Sugerujemy zapoznanie się z oryginalną instrukcją [FastHenry User\'s manual](https://www.fastfieldsolvers.com/documentation.htm) i pobawienie się przykładowymi plikami, które są dostarczane wraz z instalacją.



### FasterCap

FasterCap to potężny program do ekstrakcji pojemności w trzech i dwóch wymiarach.

Znajomość FasterCap jest warunkiem wstępnym do biegłego korzystania ze środowiska ElectroMagnetic dla FasterCap. Sugerujemy zapoznanie się z oryginalną instrukcją [FasterCap help file](https://www.fastfieldsolvers.com/documentation.htm) i pobawienie się przykładowymi plikami, które są dostarczane wraz z instalacją.



## Narzędzia FastHenry 

Są to narzędzia używane do łączenia się z FastHenry:

-   <img alt="" src=images/EM_FHNode.svg  style="width:32px;"> [FHNode](EM_FHNode/pl.md): Tworzy obiekt węzła FastHenry
-   <img alt="" src=images/EM_FHSegment.svg  style="width:32px;"> [FHSegment](EM_FHSegment/pl.md): Tworzy obiekt segmentu FastHenry
-   <img alt="" src=images/EM_FHPath.svg  style="width:32px;"> [FHPath](EM_FHPath/pl.md): Tworzy obiekt ścieżki FastHenry
-   <img alt="" src=images/EM_FHPlane.svg  style="width:32px;"> [FHPlane](EM_FHPlane/pl.md): Tworzy jednolity obiekt przewodzący płaszczyzny FastHenry
-   <img alt="" src=images/EM_FHPlaneHole.svg  style="width:32px;"> [FHPlaneHole](EM_FHPlaneHole/pl.md): Tworzy obiekt Otwór jednolitej płaszczyzny przewodzącej FastHenry
-   <img alt="" src=images/EM_FHPlaneAddRemoveNodeHole.svg  style="width:32px;"> [FHPlaneAddRemoveNodeHole](EM_FHPlaneAddRemoveNodeHole/pl.md): Dodaje lub usuwa węzeł lub otwór z / do płaszczyzny przewodzącej
-   <img alt="" src=images/EM_FHEquiv.svg  style="width:32px;"> [FHEquiv](EM_FHEquiv/pl.md): Tworzy obiekt równoważności węzła FastHenry
-   <img alt="" src=images/EM_FHPort.svg  style="width:32px;"> [FHPort](EM_FHPort/pl.md): Tworzy obiekt portu FastHenry
-   <img alt="" src=images/EM_FHSolver.svg  style="width:32px;"> [FHSolver](EM_FHSolver/pl.md): Tworzy obiekt solwera FastHenry
-   <img alt="" src=images/EM_FHInputFile.svg  style="width:32px;"> [FHInputFIle](EM_FHInputFile/pl.md): Tworzy plik wejściowy FastHenry



## Narzędzia FasterCap 

Obecnie FasterCap jest obsługiwany przez niektóre makra w pliku **Export_mesh.py** dostępnym w kodzie źródłowym [środowiska ElektroMagnetyka na GitHub](https://github.com/ediloren/EM-Workbench-for-FreeCAD).



## API

Narzędzia **EM** mogą być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:



## Poradniki

Niektóre poradniki wideo są dostępne dla wersji beta środowiska EM:

-   [Poradnik FreeCAD dla środowiska pracy ElektroMagnetyka - Pierwsze kroki](https://www.youtube.com/watch?v=h6Pp-_ovLZM)
-   [Poradnik FreeCAD dla środowiska pracy ElektroMagnetyka: Tworzenie płaszczyzny przewodzącej, część 1](https://www.youtube.com/watch?v=5pSzPizw4e8)
-   [Poradnik FreeCAD dla środowiska pracy ElektroMagnetyka: Tworzenie płaszczyzny przewodzącej, część 2](https://www.youtube.com/watch?v=BeBNtfH25rM)
-   [Poradnik FreeCAD dla środowiska pracy ElektroMagnetyka: Tworzenie płaszczyzny przewodzącej, część 3](https://www.youtube.com/watch?v=BtgdJOf-ql0)
-   [Poradnik FreeCAD dla środowiska pracy ElektroMagnetyka: Korzystanie z obiektu ścieżki, część 1](https://www.youtube.com/watch?v=CRqDuEtbdds)
-   [Poradnik FreeCAD dla środowiska pracy ElektroMagnetyka: Korzystanie z obiektu ścieżki, część 2](https://www.youtube.com/watch?v=slsLdLoF2OI)


{{EM Tools navi

}}



---
⏵ [documentation index](../README.md) > [External Workbenches](Category_External%20Workbenches.md) > [EM](Category_EM.md) > EM Workbench/pl
