# <img alt="Ikonka FreeCAD dla środowiska pracy Rozłożony Zespół" src=images/ExplodedAssembly_workbench_icon.svg  style="width:64px;"> ExplodedAssembly Workbench/pl




## Wprowadzenie

Środowisko <img alt="" src=images/ExplodedAssembly_workbench_icon.svg  style="width:24px;"> [Rozłożony zespół](ExplodedAssembly_Workbench/pl.md) jest zewnętrznym narzędziem do tworzenia widoków rozwiniętych i animacji złożeń.

### Cechy

-   Twórz ładne rozbicia złożeń w sposób graficzny *(bez kodu!)*.
-   Tworzenie grup z rozbiciami.
-   Nadaj obrót śrubom i nakrętkom dla realistycznego demontażu.
-   Użyj pomocniczych narzędzi montażowych, aby umieścić swoje części razem.
-   Funkcja do wykonania: tworzenie trajektorii z linii i szkiców.

## Bibliografia

-   Autor: JMG1
-   Strona domowa: [ExplodedAssembly](https://github.com/JMG1/ExplodedAssembly)
-   Kod źródłowy na githubie: [ExplodedAssembly](https://github.com/JMG1/ExplodedAssembly)

## Przybory

![](images/ExplodedAssembly-menu-orizz.png ) 
*Pasek narzędzi*

![](images/ExplodedAssembly-menu-vert.png ) 
*Menu*

### Narzędzia standardowe 

-   <img alt="" src=images/ExplodedAssembly_CreateBoltGroup.png  style="width:32px;"> Utwórz grupę śrub
-   <img alt="" src=images/ExplodedAssembly_CreateSimpleGroup.png  style="width:32px;"> Utwórz grupę podstawową
-   <img alt="" src=images/ExplodedAssembly_ModifyIndividualObjectTrajectory.png  style="width:32px;"> Modyfikacja trajektorii pojedynczego obiektu
-   <img alt="" src=images/ExplodedAssembly_PlaceBefore.png  style="width:32px;"> Miejsce przed
-   <img alt="" src=images/ExplodedAssembly_ExplodeToSelection.png  style="width:32px;"> Rozbij do wyboru
-   <img alt="" src=images/ExplodedAssembly_Assemble.png  style="width:32px;"> Złożenie
-   <img alt="" src=images/ExplodedAssembly_PlayBackwards.png  style="width:32px;"> Odtwarzaj od tyłu
-   <img alt="" src=images/ExplodedAssembly_StopAnimation.png  style="width:32px;"> Zatrzymaj animację
-   <img alt="" src=images/ExplodedAssembly_PlayForward.png  style="width:32px;"> Odtwarzaj do przodu
-   <img alt="" src=images/ExplodedAssembly_Disassemble.png  style="width:32px;"> Demontuj
-   <img alt="" src=images/ExplodedAssembly_TrajectoryVisibility.png  style="width:32px;"> Widoczność trajektorii
-   <img alt="" src=images/ExplodedAssembly_AlignToEdge.png  style="width:32px;"> Wyrównaj do krawędzi
-   <img alt="" src=images/ExplodedAssembly_Rotate90.png  style="width:32px;"> Obróć o 90°
-   <img alt="" src=images/ExplodedAssembly_PoinToPoint.png  style="width:32px;"> Wskaż do punktu
-   <img alt="" src=images/ExplodedAssembly_PlaceConcentrically.png  style="width:32px;"> Umieść centralnie

### Narzędzia dodatkowe 

Te narzędzia można dodać do niestandardowego paska narzędzi. Zobacz stronę [Dostosowywanie interfejsu użytkownika do własnych potrzeb](Interface_Customization/pl.md).

-   <img alt="" src=images/ExplodedAssembly_AnimationCameraEdge.png  style="width:32px;"> Krawędź ujęcia widoku
-   <img alt="" src=images/ExplodedAssembly_AnimationCameraFollow.png  style="width:32px;"> Podążaj za ujęciem widoku
-   <img alt="" src=images/ExplodedAssembly_AnimationCameraManual.png  style="width:32px;"> Manualne ujęcie widoku
-   <img alt="" src=images/ExplodedAssembly_WireTrajectory.png  style="width:32px;"> Linia trajektorii

## Instalacja

### Instalacja automatyczna 

To środowisko pracy można zainstalować za pomocą [Menadżera dodatków](Std_AddonMgr/pl.md).

### Z repozytorium GitHub 

Używanie git na Ubuntu i Mint:

-   Otwórz wiersz poleceń *(terminal)* za pomocą klawiszy **Ctrl** + **Alt** + **t**.
-   Zainstaluj git: {{Incode|sudo apt-get install git}}
-   Sklonuj repozytorium: {{Incode|<nowiki>git clone https://github.com/JMG1/ExplodedAssembly ~/.FreeCAD/Mod/ExplodedAssembly</nowiki>}}

To wszystko, przy następnym uruchomieniu programu FreeCAD powinno być dostępne stanowisko pracy.

Aby przeprowadzić instalację samodzielnie, pobierz to repozytorium jako ZIP i:

-   Dla Ubuntu, Mint i podobnych OS rozpakuj go wewnątrz folderu: **/home/username/.local/share/FreeCAD/Mod** (<small>(v0.20)</small> ) lub **/home/username/.FreeCAD/Mod** ({{VersionMinus/pl|0.19}})
-   Dla Windows rozpakuj go w: **C:\Users\twoja_nazwa_użytkownika\AppData\Roaming\FreeCAD\Mod**

## Linki do środowiska pracy Rozłożony Zespół 

-   Forum FreeCAD: <http://forum.freecadweb.org/viewtopic.php?f=24&t=9028> .
-   Filmy: [Exploded Assembly Workbench 2](https://www.youtube.com/watch?v=lzYR7I2h7KQ) [Exploded Assembly Workbench 2.0](https://www.youtube.com/watch?v=t72qdG772Q8&feature=youtu.be).
-   Pliki: wewnątrz środowiska pracy.
-   Zgłaszanie błędów: Proszę zgłaszać błędy na <https://github.com/JMG1/ExplodedAssembly/issues> .

## Inne użyteczne odnośniki 

-   [Zewnętrzne środowiska pracy](External_workbenches/pl.md)
-   [Przepisy na makropolecenia](Macros_recipes/pl.md)



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > ExplodedAssembly Workbench/pl
