# <img alt="Ikonka FreeCAD dla środowiska pracy Elementy złączne" src=images/Fasteners_workbench_icon.svg  style="width:64px;"> Fasteners Workbench/pl


{{TOCright}}

## Wprowadzenie

Środowisko pracy <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Elementów złącznych](Fasteners_Workbench.md) należy do [zewnętrznych środowisk pracy](External_workbenches/pl.md). Jest ono przeznaczone do łatwego, szybkiego i wygodnego dodawania różnych elementów złącznych z częściami.

![](images/Fasteners_toolbars.png ) 
*Opcjonalny układ pojedynczego paska narzędzi w środowisku pracy.<br>
Elementy złączne o wymiarach metrycznych mają pomarańczowe ikonki.<br>
Elementy złączne o wymiarach calowych mają zielone ikonki.*

## Instalacja

1.  Zainstaluj środowisko Elementów Złącznych poprzez <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Menadżer dodatków](Std_AddonMgr/pl.md). Informacje na temat instalacji ręcznej znajdują się na stronie [Instalacja większej ilości środowisk pracy](Installing_more_workbenches/pl.md).
2.  Wybierz środowisko <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Elementów Złącznych](Fasteners_Workbench/pl.md) z [listy menu rozwijanego](Std_Workbench/pl.md).
3.  Opcjonalnie zmień układ paska narzędzi i menu:
    1.  Przejdź do: **Ediycja → Preferenceje ... → Elementy złączne → Ustawienia ogólne → Grupowanie ikon śrub na pasku narzędzi**.
    2.  Wybierz jedną z dostępnych opcji:
        -   
            **Brak**
            
            : Wszystkie elementy złączne są wyświetlane na jednym pasku narzędzi. Aby zobaczyć wszystkie dostępne przybory, użyj przycisku **&gt;&gt;**, aby rozwinąć ten pasek.

        -   
            **Paski narzędzi oddzielnie**
            
            : Elementy złączne są zgrupowane w kilku paskach narzędzi. Jest to układ domyślny.

        -   
            **Przyciski rozwijane**
            
            : Elementy złączne są zgrupowane w paskach narzędziowych z wysuwanymi przyciskami.
    3.  Uruchom ponownie program FreeCAD.

## Użycie

Elementy złączne mogą być dołączone lub nie dołączone. Dołączone elementy złączne mają **obiekt bazowy**, okrągłą krawędź, a ich **Umiejscowienie** jest dynamicznie powiązane z tym obiektem. Polecenie <img alt="" src=images/Fasteners_Move.svg  style="width:24px;"> [Przesunięcie](Fasteners_Move/pl.md) może być użyte do dołączenia lub odłączenia elementu złącznego.

### Rozłączone elementy złączne 

1.  Wybierz żądany łącznik, klikając jego przycisk lub wybierając go z menu.
2.  Element złączny zostanie utworzony w punkcie początkowym.
3.  Opcjonalnie można zmienić wymiary i inne właściwości łącznika:
    1.  Wybierz element złączny.
    2.  Przejdź do zakładki **Dane** [Edytora właściwości](Property_editor/pl.md).
    3.  Zmień wymagane właściwości.

### Złączone elementy złączne 

<img alt="" src=images/Fasteners_Attached_Selected.png  style="width:200px;"> <img alt="" src=images/Fasteners_Attached_Created.png  style="width:200px;"> 
*Po lewej stronie dwie wybrane okrągłe krawędzie. Po prawej stronie zamocowane elementy złączne.*

1.  Określ, czy wybrane otwory są otworami gwintowanymi ślepymi czy przelotowymi, wybierając <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:24px;"> [Typ dopasowania wewnętrzny](Fasteners_MatchTypeInner/pl.md) lub <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:24px;"> [Typ dopasowania zewnętrzny](Fasteners_MatchTypeOuter/pl.md) *(nie używane dla śrub z łbem stożkowym)*.
2.  Wybierz jedną lub więcej okrągłych krawędzi i/lub powierzchni z okrągłymi krawędziami. W przypadku wkrętów z łbem stożkowym należy wybrać górną krawędź [fazki otworu](Fasteners_ChamferHole/pl.md).
3.  Wybierz żądany łącznik klikając jego przycisk lub wybierając go z menu.
4.  Do każdej z wybranych krawędzi kołowych dołączany jest element złączny.
5.  Domyślne wymiary każdego z łączników zależą od promienia okrągłej krawędzi, do której jest on przymocowany. Śruby z łbem stożkowym są dopasowywane według średnicy łba, inne elementy złączne są dopasowywane według średnicy trzonu.
6.  Opcjonalnie można zmienić wymiary i inne właściwości elementów złącznych. Patrz wyżej.
7.  Elementy złączne, które wyglądają na odwrócone do góry nogami, mogą być odwrócone za pomocą narzędzia <img alt="" src=images/Fasteners_Flip.svg  style="width:24px;"> [Odwróć](Fasteners_Flip/pl.md) lub poprzez zmianę ich właściwości **Odwróć**.
8.  Opcjonalnie zmień właściwość **Odsunięcie**, aby utworzyć przestrzeń między elementami złącznymi a krawędziami, do których są przymocowane.

## Uwagi

-   Aby generować gwinty, właściwość **gwint** łącznika musi być zmieniona na wartość {{TRUE/pl}}. Generowanie gwintów jest kosztowne. Przeliczenia trwają znacznie dłużej, jeśli w dokumencie jest wiele gwintowanych łączników.
-   Właściwość **odwróć** i **odsunięcie** są ignorowane dla niezamocowanych elementów złącznych.

## Polecenia

-   <img alt="" src=images/Fasteners_Flip.svg  style="width:32px;"> [Odwróć](Fasteners_Flip/pl.md): odwrócenie orientacji dołączonego elementu złącznego.

-   <img alt="" src=images/Fasteners_Move.svg  style="width:32px;"> [Przenieś](Fasteners_Move/pl.md): przesuń i przymocuj element złączny do okrągłej krawędzi. Może być również używany do odłączania elementu złącznego.

-   <img alt="" src=images/Fasteners_Shape.svg  style="width:32px;"> [Kształt](Fasteners_Shape/pl.md): tworzy nieparametryczne kopie elementów złącznych.

-   <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:32px;"> [Typ dopasowania wewnętrzny](Fasteners_MatchTypeInner/pl.md): okrągłe krawędzie należy traktować jako otwory gwintowane, gdy mocowane są do nich nowe elementy złączne.

-   <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:32px;"> [Typ dopasowania zewnętrzny](Fasteners_MatchTypeOuter/pl.md): okrągłe krawędzie należy traktować jako otwory przelotowe, gdy mocowane są do nich nowe elementy złączne.

-   <img alt="" src=images/Fasteners_BOM.svg  style="width:32px;"> [BOM](Fasteners_BOM/pl.md): utwórz arkusz kalkulacyjny z zestawieniem materiałów dla elementów złącznych w dokumencie.

-   <img alt="" src=images/Fasteners_ScrewCalculator.svg  style="width:32px;"> [Kalkulator śrub](Fasteners_ScrewCalculator/pl.md): pokaż kalkulator, aby określić wielkość otworu gwintowanego dla śrub.

-   <img alt="" src=images/Fasteners_ChamferHole.svg  style="width:32px;"> [Fazka otworu](Fasteners_ChamferHole/pl.md): sfazowanie otworów pod wkręty z łbem stożkowym.

-   <img alt="" src=images/Fasteners_ChangeParameters.svg  style="width:32px;"> [Zmiana parametrów](Fasteners_ChangeParameters/pl.md): umożliwia dokonanie zmian parametrów elementów złącznych.

## Elementy złączne 

Elementy złączne o wymiarach metrycznych posiadają ikony w kolorze pomarańczowym. Elementy złączne o wymiarach calowych posiadają zielone ikony.

#### Samokontrujące elementy złączne i elementy złączne PCB 

-   <img alt="" src=images/Fasteners_PEMPressNut.svg  style="width:32px;"> Nakrętka samokontrująca.

-   <img alt="" src=images/Fasteners_PEMTHStandoff.svg  style="width:32px;"> Dystans samozaciskowy.

-   <img alt="" src=images/Fasteners_PEMStud.svg  style="width:32px;"> Samozaciskowy kołek.

-   <img alt="" src=images/Fasteners_PCBStandoff.svg  style="width:32px;"> **PCB** Dystans męski / żeński.

-   <img alt="" src=images/Fasteners_PCBSpacer.svg  style="width:32px;"> **PCB** Przekładka żeńska / żeńska.

-   <img alt="" src=images/Fasteners_IUTHeatInsert.svg  style="width:32px;"> Wkładka mocowana na gorąco.

### Śruby i wkręty z łbem sześciokątnym 

-   <img alt="" src=images/Fasteners_ISO4017.svg  style="width:32px;"> **ISO 4017** Śruba z łbem sześciokątnym. Klasy produktów A i B.

-   <img alt="" src=images/Fasteners_ISO4014.svg  style="width:32px;"> **ISO 4014** Śruba z łbem sześciokątnym. Klasy produktów A i B.

-   <img alt="" src=images/Fasteners_EN1662.svg  style="width:32px;"> **EN 1662** Śruba z łbem sześciokątnym z kołnierzem, seria mała.

-   <img alt="" src=images/Fasteners_EN1665.svg  style="width:32px;"> **EN 1665** Śruba sześciokątna z kołnierzem, seria gruba.

-   <img alt="" src=images/Fasteners_DIN571.svg  style="width:32px;"> **DIN 571** Wkręt do drewna z łbem sześciokątnym.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.6.svg  style="width:32px;"> **ASME B18.2.1.6** UNC Śruba z łbem sześciokątnym.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.8.svg  style="width:32px;"> **ASME B18.2.1.8** UNC Śruba z łbem sześciokątnym z kołnierzem.

### Śruby z gniazdem sześciokątnym 

-   <img alt="" src=images/Fasteners_ISO4762.svg  style="width:32px;"> **ISO 4762** Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_DIN7984.svg  style="width:32px;"> **DIN 7984** Śruba z gniazdem sześciokątnym z niskim łbem.

-   <img alt="" src=images/Fasteners_DIN6912.svg  style="width:32px;"> **DIN 6912** Śruba z łbem o gnieździe sześciokątnym z niskim łbem i środkiem.

-   <img alt="" src=images/Fasteners_ISO7380-1.svg  style="width:32px;"> **ISO 7380-1** Śruba z łbem kulistym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO7380-2.svg  style="width:32px;"> **ISO 7380-2** Śruba z łbem sześciokątnym z kołnierzem.

-   <img alt="" src=images/Fasteners_ISO10642.svg  style="width:32px;"> **ISO 10642** Śruba z łbem stożkowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO7379.svg  style="width:32px;"> **ISO 7379** Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO4026.svg  style="width:32px;"> **ISO 4026** Śruba z gniazdem sześciokątnym z płaskim czubkiem.

-   <img alt="" src=images/Fasteners_ISO4027.svg  style="width:32px;"> **ISO 4027** Śruba z gniazdem sześciokątnym z czopem stożkowym.

-   <img alt="" src=images/Fasteners_ISO4028.svg  style="width:32px;"> **ISO 4028** Śruba z gniazdem sześciokątnym z czubkiem.

-   <img alt="" src=images/Fasteners_ISO4029.svg  style="width:32px;"> **ISO 4029** Śruba z gniazdem sześciokątnym z czubkiem.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1A.svg  style="width:32px;"> **ASME B18.3.1A** UNC Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1G.svg  style="width:32px;"> **ASME B18.3.1G** Śruba z łbem sześciokątnym UNC niskim.

-   <img alt="" src=images/Fasteners_ASMEB18.3.2.svg  style="width:32px;"> **ASME B18.3.2** UNC Śruba z łbem stożkowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3A.svg  style="width:32px;"> **ASME B18.3.3A** UNC Śruba z łbem kulistym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3B.svg  style="width:32px;"> **ASME B18.3.3B** UNC Śruba z łbem sześciokątnym z kołnierzem.

-   <img alt="" src=images/Fasteners_ASMEB18.3.4.svg  style="width:32px;"> **ASME B18.3.4** UNC Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5A.svg  style="width:32px;"> **ASME B18.3.5A** UNC Śruba z gniazdem sześciokątnym z płaskim czubkiem.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5B.svg  style="width:32px;"> **ASME B18.3.5B** UNC Śruba z gniazdem sześciokątnym z czopem stożkowym.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5C.svg  style="width:32px;"> **ASME B18.3.5C** UNC Śruba z gniazdem sześciokątnym z czubkiem.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5D.svg  style="width:32px;"> **ASME B18.3.5D** UNC Śruba z gniazdem sześciokątnym z czubkiem.

### Śruby z gniazdem sześciokątnym 

-   <img alt="" src=images/Fasteners_ISO14579.svg  style="width:32px;"> **ISO 14579** Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO14580.svg  style="width:32px;"> **ISO 14580** Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO14582.svg  style="width:32px;"> **ISO 14582** Śruba z łbem stożkowym z gniazdem sześciokątnym, wysoki łeb.

-   <img alt="" src=images/Fasteners_ISO14583.svg  style="width:32px;"> **ISO 14583** Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO14584.svg  style="width:32px;"> **ISO 14584** Śruba z łbem stożkowym z gniazdem sześciokątnym.

### Śruby z łbem wpuszczanym 

-   <img alt="" src=images/Fasteners_ISO2009.svg  style="width:32px;"> **ISO 2009** Śruba z łbem płaskim z rowkiem stożkowym. Klasa produktu A.

-   <img alt="" src=images/Fasteners_ISO2010.svg  style="width:32px;"> **ISO 2010** Śruba z łbem wpuszczanym z podwyższonym rowkiem. Klasa produktu A.

-   <img alt="" src=images/Fasteners_ISO1580.svg  style="width:32px;"> **ISO 1580** Śruba z łbem walcowym z rowkiem. Klasa produktu A.

-   <img alt="" src=images/Fasteners_ISO1207.svg  style="width:32px;"> **ISO 1207** Śruba z łbem serowym z rowkiem. Produkt klasy A.

-   <img alt="" src=images/Fasteners_DIN96.svg  style="width:32px;"> **DIN 96** Wkręt do drewna z rowkiem i półokrągłym łbem.

-   <img alt="" src=images/Fasteners_GOST1144-1.svg  style="width:32px;"> **GOST 1144-1** Wkręt do drewna z rowkiem i półokrągłym łbem.

-   <img alt="" src=images/Fasteners_GOST1144-2.svg  style="width:32px;"> **GOST 1144-2** Wkręt do drewna z rowkiem i półokrągłym łbem.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1A.svg  style="width:32px;"> **ASME B18.6.3.1A** UNC śruba z łbem płaskim z rowkiem stożkowym.

### Śruby z łbem krzyżowym typu H 

-   <img alt="" src=images/Fasteners_DIN967.svg  style="width:32px;"> **DIN 967** Śruba z łbem walcowym z kołnierzem z wgłębieniem krzyżowym typu H.

-   <img alt="" src=images/Fasteners_ISO7045.svg  style="width:32px;"> **ISO 7045** Śruba z łbem walcowym typu H z wgłębieniem krzyżowym. Klasa produktu A.

-   <img alt="" src=images/Fasteners_ISO7046.svg  style="width:32px;"> **ISO 7046** Śruba z łbem stożkowym płaskim z wgłębieniem krzyżowym typu H . Klasa produktu A.

-   <img alt="" src=images/Fasteners_ISO7047.svg  style="width:32px;"> **ISO 7047** Śruba z łbem stożkowym podniesionym z wgłębieniem krzyżowym typu H . Klasa produktu A.

-   <img alt="" src=images/Fasteners_ISO7048.svg  style="width:32px;"> **ISO 7048** Śruba z łbem serowym z wgłębieniem krzyżowym typu H.

-   <img alt="" src=images/Fasteners_GOST1144-3.svg  style="width:32px;"> **GOST 1144-3** Wkręt do drewna z łbem półokrągłym z wgłębieniem krzyżowym typu H.

-   <img alt="" src=images/Fasteners_GOST1144-4.svg  style="width:32px;"> **GOST 1144-4** Wkręt do drewna z łbem półokrągłym z wgłębieniem krzyżowym typu H.

### Inne śruby z łbami 

-   <img alt="" src=images/Fasteners_DIN603.svg  style="width:32px;"> **DIN 603** Śruba z okrągłym łbem i kwadratową szyjką.

-   <img alt="" src=images/Fasteners_ASMEB18.5.2.svg  style="width:32px;"> **ASME B18.5** Śruba UNC z okrągłym łbem i kwadratową szyjką.

### Nakrętki

-   <img alt="" src=images/Fasteners_ISO4032.svg  style="width:32px;"> **ISO 4032** Nakrętka sześciokątna, styl 1. *Klasy produktów A i B.*.

-   <img alt="" src=images/Fasteners_ISO4033.svg  style="width:32px;"> **ISO 4033** Nakrętka sześciokątna, styl 2. *Klasy produktów A i B.*.

-   <img alt="" src=images/Fasteners_ISO4035.svg  style="width:32px;"> **ISO 4035** Nakrętka sześciokątna cienka, fazowana. Gatunek produktu A i B.

-   <img alt="" src=images/Fasteners_EN1661.svg  style="width:32px;"> **EN 1661** Nakrętka sześciokątna z kołnierzem.

-   <img alt="" src=images/Fasteners_DIN917.svg  style="width:32px;"> **DIN 917** Nakrętka kołpakowa, niska.

-   <img alt="" src=images/Fasteners_DIN1587.svg  style="width:32px;"> **DIN 1587** Nakrętka kołpakowa.

-   <img alt="" src=images/Fasteners_GOST11860-1.svg  style="width:32px;"> **GOST 11860-1** Nakrętka kołpakowa.

-   <img alt="" src=images/Fasteners_DIN557.svg  style="width:32px;"> **DIN 557** Nakrętka czworokątna.

-   <img alt="" src=images/Fasteners_DIN562.svg  style="width:32px;"> **DIN 562** Nakrętka czworokątna.

-   <img alt="" src=images/Fasteners_DIN985.svg  style="width:32px;"> **DIN 985** Nakrętka Nyloc.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1A.svg  style="width:32px;"> **ASME B18.2.2.1A** UNC Nakrętka do śruby maszynowej.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4A.svg  style="width:32px;"> **ASME B18.2.2.4A** UNC Nakrętka sześciokątna.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4B.svg  style="width:32px;"> **ASME B18.2.2.4B** UNC Nakrętka sześciokątna cienka.

### Nakrętki do rowków T 

-   <img alt="" src=images/Fasteners_DIN508.svg  style="width:32px;"> **DIN 508** Nakrętka młoteczkowa - T.

-   <img alt="" src=images/Fasteners_GN507.svg  style="width:32px;"> **GN 507** Nakrętka do rowka T.

### Podkładki

-   <img alt="" src=images/Fasteners_ISO7089.svg  style="width:32px;"> 
**ISO 7089** Podkładka ślizgowa, seria normalna. *Klasa produktu A.*

-   <img alt="" src=images/Fasteners_ISO7090.svg  style="width:32px;"> **ISO 7090** Podkładka ślizgowa fazowana, seria normalna. Gatunek produktu A.

-   <img alt="" src=images/Fasteners_ISO7092.svg  style="width:32px;"> 
**ISO 7092** Podkładka zwykła, seria mała. *Gatunek produktu A.*

-   <img alt="" src=images/Fasteners_ISO7093-1.svg  style="width:32px;"> 
**ISO 7093-1** Podkładka ślizgowa, seria duża. *Klasa produktu A.*

-   <img alt="" src=images/Fasteners_ISO7094.svg  style="width:32px;"> 
**ISO 7094** Podkładka zwykła, seria ekstra duża. *Gatunek produktu C.*

-   <img alt="" src=images/Fasteners_NFE27-619.svg  style="width:32px;"> **NFE27-619** Podkładka stożkowa.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12A.svg  style="width:32px;"> **ASME B18.21.1.12A** UN podkładka, seria wąska.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12B.svg  style="width:32px;"> **ASME B18.21.1.12B** UN podkładka, seria regularna.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12C.svg  style="width:32px;"> **ASME B18.21.1.12C** UN podkładka, seria szeroka.

### Pierścienie oporowe 

-   <img alt="" src=images/Fasteners_DIN471.svg  style="width:32px;"> **DIN 471** Zewnętrzny pierścień zabezpieczający.

-   <img alt="" src=images/Fasteners_DIN472.svg  style="width:32px;"> **DIN 472** Wewnętrzny pierścień zabezpieczający.

-   <img alt="" src=images/Fasteners_DIN6799.svg  style="width:32px;"> **DIN 6799** Pierścień zabezpieczający E-clip.

### Elementy złączne różne 

-   <img alt="" src=images/Fasteners_ScrewTap.svg  style="width:32px;"> Gwintownik o dowolnej długości do gwintowania otworów *(metryczny)*.

-   <img alt="" src=images/Fasteners_ScrewTapInch.svg  style="width:32px;"> Gwintownik o dowolnej długości do gwintowania otworów *(calowy)*.

-   <img alt="" src=images/Fasteners_ScrewDie.svg  style="width:32px;"> Narzynka o dowolnej długości do nacinania gwintów zewnętrznych *(metryczna)*.

-   <img alt="" src=images/Fasteners_ScrewDieInch.svg  style="width:32px;"> RNarzynka o dowolnej długości do nacinania gwintów zewnętrznych *(calowa)*.

-   <img alt="" src=images/Fasteners_ThreadedRod.svg  style="width:32px;"> Gwintownik **DIN 975** o dowolnej długości *(metryczny)*.

-   <img alt="" src=images/Fasteners_ThreadedRodInch.svg  style="width:32px;"> PGwintownik **DIN 975** o dowolnej długości *(calowy)*.

## Bibliografia

-   Autor: [shaise](http://theseger.com/projects/author/shaise/),
    -   ScrewMaker: Ulrich Brammer,
    -   Workbench wrapper: Shai Seger,
-   Strona domowa: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>,
-   Kod źródłowy: <https://github.com/shaise/FreeCAD_FastenersWB>,
-   Zgłoszenia błędów i prośby o nowe funkcje: <https://github.com/shaise/FreeCAD_FastenersWB/issues>,
-   Tematy na forum: <https://forum.freecadweb.org/viewtopic.php?t=11429>.

## Odnośniki internetowe 

-   [Generowanie otworów pod wkręty z łbem stożkowym z użyciem programu FreeCAD.](http://theseger.com/projects/2015/07/generating-holes-for-countersunk-screws-in-freecad/)
-   [ŚRUBY](https://github.com/jreinhardt/BOLTS): Otwarta biblioteka dla specyfikacji technicznych
-   [Środowiska zewnętrzne](External_workbenches/pl.md)
-   [Przepisy na makropolecenia](Macros_recipes/pl.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > [External Workbenches](Category_External Workbenches.md) > [Fasteners](Category_Fasteners.md) > Fasteners Workbench/pl
