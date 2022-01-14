# <img alt="Ikonka FreeCAD dla środowiska pracy FCGear" src=images/FCGear_workbench_icon.svg  style="width:64px;"> FCGear Workbench/pl

## Wprowadzenie


{{TOCright}}

Środowisko pracy [FCGear](FCGear_Workbench/pl.md) jest [zewnętrznym środowiskiem pracy](External_workbenches/pl.md) programu FreeCAD do wytwarzania różnych typów kół zębatych i ślimakowych. Modelowanie parametryczne pozwala na zmianę wymaganej geometrii w dowolnym momencie. Na przykład, poprzez zmianę kilku parametrów, koło zębate ewolwentowe staje się kołem zębatym walcowym, kołem zębatym śrubowym lub podwójnym kołem śrubowym.

Aby wyniki z FC Gear były użyteczne, wymagana jest pewna podstawowa wiedza na temat różnych typów przekładni. Moduł, średnica podziałowa lub średnica rdzenia są pojęciami powszechnymi i dlatego powinny być znane.

W połączeniu z drukiem 3D użytkownicy domowi mają teraz możliwość zaprojektowania i wyprodukowania kół zębatych i przekładni ślimakowych według własnego pomysłu, a w razie potrzeby dostosowania ich do warunków konstrukcyjnych.

Zanim [FCGear](FCGear_Workbench.md) będzie mógł zostać uruchomiony, musi zostać zainstalowany *(jak to zrobić zobacz poniżej w rozdziale **Instalacja**)*. Po instalacji, narzędzia są dostępne w pasku narzędzi.

:   ![](images/FCGear_Drop-down-menu_example-en.png )
:   
    
*Menu FCGear*
    

## Typy kół zębatych 

### Koło zębate ewolwentowe 

:   ![](images/Involute-Gear_example.png )
:   
    
*Od lewej do prawej: Przekładnia czołowa, przekładnia śrubowa, podwójna przekładnia śrubowa ''(zobacz [Koło zębate ewolwentowe](FCGear_InvoluteGear/pl.md))''*
    

### Listwa zębata ewolwentowa 

:   ![](images/Involute-Rack_example.png )
:   
    
*Przekładnia czołowa, przekładnia śrubowa, podwójna przekładnia śrubowa ''(zobacz [Listwa zębata ewolwentowa](FCGear_InvoluteRack/pl.md))''*
    

### Koło zębate cykloidalne 

:   ![](images/Cycloid-Gear_example_1.png )
:   
    
*Przekładnia czołowa, przekładnia śrubowa, podwójna przekładnia śrubowa ''(zobacz [Koło zębate cykloidalne](FCGear_CycloideGear/pl.md))''*
    

### Koło zębate stożkowe 

:   ![](images/Bevel-Gear_example.png )
:   
    
*Od lewej do prawej: Przekładnia czołowa, przekładnia śrubowa (zobacz [Koło zębate stożkowe](FCGear_BevelGear/pl.md))''*
    

### Ślimak

:   ![](images/Worm-Gear_example.png )
:   
    
*Powyżej: Przekładnia ślimakowa ''(zobacz [Ślimak](FCGear_WormGear/pl.md))''*
    

### Koło zębate koronowe 

:   ![](images/Crown-Gear_example.png )
:   
    
*Powyżej: Koło zębate koronowe ''(Zobacz [Koło zębate koronowe](FCGear_CrownGear/pl.md))''*
    

### Koło pasa zębatego i koło drabinkowe 

:   ![](images/Timing+Latern-gear_example.png )
:   
    
*Od lewej do prawej: Koło pasa zębatego, koło zębate latarni ''(zobacz [Koło pasa zębatego](FCGear_TimingGear/pl.md) oraz [Koło drabinkowe](FCGear_LanternGear/pl.md))''*
    

## Bibliografia

-   Autor: looooo
-   Strona domowa: <https://github.com/looooo/FCGear>
-   Kod źródłowy na githubie: <https://github.com/looooo/FCGear>

## Przybory

### Pasek narzędzi 

-   <img alt="" src=images/FCGear_InvoluteGear.svg  style="width:32px;"> [Koło zębate ewolwentowe](FCGear_InvoluteGear/pl.md): Tworzy koło zębate ewolwentowe.
-   <img alt="" src=images/FCGear_InvoluteRack.svg  style="width:32px;"> [Listwa zębata ewolwentowa](FCGear_InvoluteRack/pl.md): Tworzy listwę zębatą ewolwentową.
-   <img alt="" src=images/FCGear_CycloideGear.svg  style="width:32px;"> [Koło zębate cykloidalne](FCGear_CycloideGear/pl.md): Tworzy koło zębate cykloidalne.
-   <img alt="" src=images/FCGear_BevelGear.svg  style="width:32px;"> [Koło zębate stożkowe](FCGear_BevelGear/pl.md): Tworzy koło zębate stożkowe.
-   <img alt="" src=images/FCGear_WormGear.svg  style="width:32px;"> [Ślimak](FCGear_WormGear/pl.md): Tworzy śrubę ślimakową.
-   <img alt="" src=images/FCGear_CrownGear.svg  style="width:32px;"> [Koło zębate koronowe](FCGear_CrownGear/pl.md): Tworzy koło zębate koronowe.
-   <img alt="" src=images/FCGear_TimingGear.svg  style="width:32px;"> [Koło pasa zębatego](FCGear_TimingGear/pl.md): Tworzy koło pasa zębatego.
-   <img alt="" src=images/FCGear_LanternGear.svg  style="width:32px;"> [Koło drabinkowe](FCGear_LanternGear/pl.md): Tworzy koło drabinkowe.

## Instalacja

### Instalacja automatyczna 

Zalecaną metodą instalacji od v0.17 jest instalacja poprzez <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżer dodatków](Std_AddonMgr/pl.md). Można go znaleźć w menu **Przybory → Menadżer dodatków**.


<div class="mw-collapsible mw-collapsed toccolours" style="width:700px">

### Instalacja samodzielna 

Jeśli istnieje konieczność ręcznego zainstalowania tego środowiska pracy, poniżej znajdują się instrukcje, jak to zrobić:


<div class="mw-collapsible-content">

#### Linux

-    `git clone https://github.com/looooo/FCGear.git`
    

-   podlinkuj lub skopiuj folder do {{FileName|/freecad/Mod}}.

:   

    :   
        `sudo ln -s (path_to_FCGear) (path_to_freecad)/Mod`
        

#### Windows

Testowane na (7/8/8.1/10) (z GitHub)

-   pobierz archiwum ZIP klikając na przycisk w prawym górnym rogu,
-   przejdź do folderu FreeCAD-Macro *(wewnątrz FreeCAD, wybierz **Edycja > Preferencje → Ogólne → Makrodefinicje**, aby zobaczyć Ścieżkę do katalogu Macro)*,
-   jeśli nie zmieniłeś standardowych ustawień, powinno to być

:   

    :   
        `C:\Users\Twój_Windows_User_Name\AppData\Roaming\FreeCAD`
        
        ,

-   \\appdata jest ukrytym folderem, więc może być konieczna zmiana ustawień eksploratora plików, aby go zobaczyć,
-   utwórz folder podrzędny o nazwie `FCGear`,
-   upewnij się, że skopiujesz pliki i foldery DOKŁADNIE tak, jak pokazano powyżej do właśnie utworzonego folderu podrzędnego,
-   zrestartuj program FreeCAD, a środowisko pracy powinno pojawić się w rozwijanym menu,
-   w programie FreeCAD możesz wybrać **Przybory → Dostosuj → środowiska pracy** aby włączyć / wyłączyć środowisko pracy.

#### MacOSX

Patrz instrukcje dla systemu Linux powyżej


</div>


</div>

## Linki do środowiska pracy Gear 

-   Wiki środowiska pracy: <https://github.com/looooo/FCGear/wiki>
-   FreeCAD Wiki: [Macro\_FCGear](http://www.freecadweb.org/wiki/index.php?title=Macro_FCGear) oraz [Bevel gear](http://forum.freecadweb.org/viewtopic.php?f=3&t=12878)
-   Forum FreeCAD: <http://forum.freecadweb.org/viewtopic.php?f=21&t=12968>
-   Poradniki:
-   Filmiki:
-   Pliki:
-   Zgłaszanie błędów: Proszę zgłaszać błędy na <https://github.com/looooo/FCGear/issues>

## Inne użyteczne odnośniki 

-   <img alt="PartDesign\_InvoluteGear/pl" src=images/PartDesign_InvoluteGear.svg  style="width:24px;"> [Koło zębate ewolwentowe](PartDesign_InvoluteGear/pl.md): To narzędzie pozwala na tworzenie profilu 2D koła zębatego ewolwentowego. Ten profil 2D jest w pełni parametryczny i może być uzupełniony za pomocą funkcji [Wyciągnięcia](PartDesign_Pad.md).
-   [Zewnętrzne środowiska pracy](External_workbenches/pl.md): Lista wszystkich aktualnych zewnętrznych środowisk pracy programu FreeCAD.
-   [Przepisy na makropolecenia](Macros_recipes/pl.md)
-   [Przekładnia cykloidalna *(niemiecki)*](https://vivat-geo.de/zykloidenverzahnung.html)
-   [Przekładnia ewolwentowa *(niemiecki)*](https://vivat-geo.de/evolventenverzahnung.html)




[<img src="images/Property.png" style="width:16px"> External Workbenches](Category_External_Workbenches.md) [<img src="images/Property.png" style="width:16px"> Addons](Category_Addons.md) [<img src="images/Property.png" style="width:16px"> FCGear](Category_FCGear.md)

---
[documentation index](../README.md) > [External Workbenches](Category_External Workbenches.md) > FCGear Workbench/pl
