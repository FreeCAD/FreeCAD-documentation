# <img alt="" src=images/MOOC_workbench_icon.svg  style="width:240px;">  MOOC Workbench/pl
*align=center|Ikonka FreeCAD dla zewnętrznego środowiska pracy MOOC*



## Informacje ogólne 




Środowisko pracy MOOC to [zewnętrzne środowisko pracy](External_workbenches/pl.md), za pomocą którego można śledzić interaktywne poradniki i dokonywać oceny swojej pracy bezpośrednio w interfejsie FreeCAD. Środowisko pracy MOOC oferuje 2 narzędzia: interaktywne poradniki i oceny.

-   Obecnie tylko w języku francuskim *(i zakodowane na stałe)*.
-   Kompatybilny tylko z FreeCAD Py3 i Qt5 *(PySide2)*
-   Kod LGPLv2 *(lub podobny)* finansowany przez Europę za pośrednictwem IMT i EESAB.
-   Modułowy: Ten workbench został stworzony z zamiarem, aby dodawanie poradników i ocen było modułowe. Innymi słowy, należy dodać poradnik w folderze **lessons** lub ewaluację w folderze **exercises**, aby pojawiły się w odpowiednim narzędziu.

## Interaktywność

**Interaktywne** samouczki *(AKA <img alt="" src=images/MOOC_Player.svg  style="width:24px;"> Player)* są ćwiczeniami prowadzonymi krok po kroku z obiektywnymi kontrolami. Uruchamia się bezpośrednio w programie FreeCAD i pozwala na przejście jednego kroku w modelowaniu obiektu. Użytkownik ma do dyspozycji tekst, wideo, a przede wszystkim sprawdzenie, czy cele zostały osiągnięte.

<img alt="" src=images/MOOC_Player_Dialog_Context.png  style="width:1024px;"> 
*align=center|Okno dialogowe odtwarzacza MOOC w interfejsie graficznym FreeCAD* ![](images/MOOC_Player_Dialog.png ) 
*Okno dialogowe odtwarzacza MOOC w zbliżeniu*

### Oceny

**Oceny** (AKA <img alt="" src=images/MOOC_Grader.svg  style="width:24px;"> Grader) składają się z małego programu, który sprawdza pewne kryteria dokumentu FreeCAD, na przykład obecność Zawartości części, szkicu lub ostatecznej objętości. <img alt="" src=images/MOOC_Grader_Dialog.png  style="width:1024px;"> 
*align=center|Okno dialogowe MOOC Oceny*



## Instalacja

To środowisko pracy może być zainstalowane z <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md). Aby zainstalować je samodzielnie zobacz stronę [Instalacja zewnętrznych środowisk pracy](Installing_more_workbenches/pl.md).



## Ograniczenia

Te środowisko pracy jest dostępne tylko w języku francuskim.



## Szczegóły techniczne 

Z technicznego punktu widzenia, środowisko pracy składa się z:

-   \"API\" zawierającego kod analizujący dokument (**MoocChecker.py**)
-   kodu wykonującego samouczki w folderze \"lessons\" (**MoocPlayer.py**)
-   kodu wykonującego oceny w folderze \"exercises\" (**MoocGrader.py**).

## Mapa rozwoju 

-   internacjonalizacja środowiska pracy
-   Integracja wideo we FreeCAD (PySide2.QtWebEngineWidgets?)
-   zażądaj integracji środowiska pracy z listą menedżera dodatków zrobione



## Odnośniki internetowe 

-   Kod źródłowy hostowany na Framagit: [1](https://framagit.org/freecad-france/mooc-workbench)
-   Oficjalnye kompletne [środowisko pracy](https://framagit.org/freecad-france/mooc-workbench#mooc-workbench)
-   Wątki dyskusyjne: [English](https://forum.freecadweb.org/viewtopic.php?f=9&t=37584) / [French](https://forum.freecadweb.org/viewtopic.php?f=12&t=37322)



## Zewnętrzne środowiska pracy 

Środowiska pracy FreeCAD są łatwe do zaprogramowania w środowisku [Python](Python/pl.md). Dlatego też, wiele osób opracowuje dodatkowe \"przestrzenie robocze\" wykraczające poza główny obszar rozwoju programu FreeCAD.

Strona [Zewnętrzne środowiska pracy](External_workbenches/pl.md) zawiera informacje i poradniki na temat niektórych z nich, a projekt [Dodatki FreeCAD](https://github.com/FreeCAD/FreeCAD-addons) ma na celu zebranie ich i uczynienie łatwymi do zainstalowania z poziomu programu FreeCAD.

Nowe środowiska pracy są w czasie tworzenia, bądź cierpliwy!



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > MOOC Workbench/pl
