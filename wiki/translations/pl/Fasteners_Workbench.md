# <img alt="Ikonka FreeCAD dla środowiska pracy Elementy złączne" src=images/Fasteners_workbench_icon.svg  style="width:64px;"> Fasteners Workbench/pl






## Wprowadzenie

Środowisko pracy <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Elementów złącznych](Fasteners_Workbench.md) należy do [zewnętrznych środowisk pracy](External_workbenches/pl.md). Jest ono przeznaczone do łatwego, szybkiego i wygodnego dodawania różnych elementów złącznych z częściami.

<img alt="" src=images/Fasteners_Toolbars.png  style="width:500px;"> 
*Opcjonalny układ pojedynczego paska narzędzi w środowisku pracy.<br>
Elementy złączne o wymiarach metrycznych mają pomarańczowe ikonki.<br>
Elementy złączne o wymiarach calowych mają zielone ikonki.*



## Instalacja

1.  Zainstaluj środowisko Elementów Złącznych poprzez <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Menadżer dodatków](Std_AddonMgr/pl.md). Informacje na temat instalacji ręcznej znajdują się na stronie [Instalacja większej ilości środowisk pracy](Installing_more_workbenches/pl.md).
2.  Wybierz środowisko <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Elementów Złącznych](Fasteners_Workbench/pl.md) z [listy menu rozwijanego](Std_Workbench/pl.md).
3.  Opcjonalnie zmień układ paska narzędzi i menu:
    1.  Przejdź do: **Edycja → Preferencje ... → Elementy złączne → Ustawienia ogólne → Grupowanie ikon śrub na pasku narzędzi**.
    2.  Wybierz jedna z dostępnych opcji **Grupowanie ikon śrub na pasku narzędzi**:
        -   
            **Brak**
            
            : Wszystkie elementy złączne są wyświetlane na jednym pasku narzędzi. Aby zobaczyć wszystkie dostępne przybory, użyj przycisku **&gt;&gt;**, aby rozwinąć ten pasek.

        -   
            **Paski oddzielnie**
            
            : Elementy złączne są zgrupowane w kilku paskach narzędzi. Jest to układ domyślny.

        -   
            **Przyciski rozwijane**
            
            : Elementy złączne są zgrupowane w paskach narzędziowych z wysuwanymi przyciskami.
    3.  Opcjonalnie odznacz jedną lub więcej opcji **Standardy elementów złącznych wyświetlane na paskach narzędzi**. Odznaczone standardy są nadal dostępne z menu.
    4.  Uruchom ponownie program FreeCAD.



## Użycie

Elementy złączne mogą być dołączone lub niedołączone. Dołączone elementy złączne mają **Obiekt bazowy**, okrągłą krawędź, a ich **Umiejscowienie** jest dynamicznie powiązane z tym obiektem. Polecenie <img alt="" src=images/Fasteners_Move.svg  style="width:24px;"> [Przesuń element złączny](Fasteners_Move/pl.md) może być użyte do dołączenia lub odłączenia elementu złącznego.



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

1.  Określ, czy wybrane otwory są otworami gwintowanymi ślepymi czy przelotowymi, wybierając <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:24px;"> [Dopasowanie otworu pod gwint](Fasteners_MatchTypeInner/pl.md) lub <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:24px;"> [Dopasowanie otworu jako przelotowego](Fasteners_MatchTypeOuter/pl.md) *(nie używane dla śrub z łbem stożkowym)*.
2.  Wybierz jedną lub więcej okrągłych krawędzi i / lub powierzchni z okrągłymi krawędziami. W przypadku wkrętów z łbem stożkowym należy wybrać górną krawędź sfazowania otworu.
3.  Wybierz żądany łącznik klikając jego przycisk lub wybierając go z menu.
4.  Do każdej z wybranych krawędzi kołowych dołączany jest element złączny.
5.  Domyślne wymiary każdego z łączników zależą od promienia okrągłej krawędzi, do której jest on przymocowany. Śruby z łbem stożkowym są dopasowywane według średnicy łba, inne elementy złączne są dopasowywane według średnicy trzonu.
6.  Opcjonalnie można zmienić wymiary i inne właściwości elementów złącznych. Patrz wyżej.
7.  Elementy złączne, które wyglądają na odwrócone do góry nogami, mogą być odwrócone za pomocą narzędzia <img alt="" src=images/Fasteners_Flip.svg  style="width:24px;"> [Odwróć element złaczny](Fasteners_Flip/pl.md) lub poprzez zmianę ich właściwości **Odwróć**.
8.  Opcjonalnie zmień właściwość **Odsunięcie**, aby utworzyć przestrzeń między elementami złącznymi a krawędziami, do których są przymocowane.



## Uwagi

-   Aby generować gwinty, właściwość **Gwint** łącznika musi być zmieniona na wartość {{TRUE/pl}}. Generowanie gwintów jest kosztowne. Przeliczenia trwają znacznie dłużej, jeśli w dokumencie jest wiele gwintowanych łączników.
-   Właściwość **Odwróć** i **Odsunięcie** są ignorowane dla niezamocowanych elementów złącznych.



## Polecenia

-   <img alt="" src=images/Fasteners_Flip.svg  style="width:32px;"> [Odwróć](Fasteners_Flip/pl.md): odwrócenie orientacji dołączonego elementu złącznego.

-   <img alt="" src=images/Fasteners_Move.svg  style="width:32px;"> [Przesuń](Fasteners_Move/pl.md): przesuń i przymocuj element złączny do okrągłej krawędzi. Może być również używany do odłączania elementu złącznego.

-   <img alt="" src=images/Fasteners_Simplify.svg  style="width:32px;"> [Uprość kształt](Fasteners_Simplify/pl.md): tworzy nieparametryczne kopie elementów złącznych.

-   <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:32px;"> [Dopasowanie otworu pod gwint](Fasteners_MatchTypeInner/pl.md): okrągłe krawędzie należy traktować jako otwory gwintowane, gdy mocowane są do nich nowe elementy złączne.

-   <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:32px;"> [Dopasowanie otworu jako przelotowego](Fasteners_MatchTypeOuter/pl.md): okrągłe krawędzie należy traktować jako otwory przelotowe, gdy mocowane są do nich nowe elementy złączne.

-   <img alt="" src=images/Fasteners_BOM.svg  style="width:32px;"> [Utwórz zestawienie](Fasteners_BOM/pl.md): utwórz arkusz kalkulacyjny z zestawieniem materiałów dla elementów złącznych w dokumencie.

-   <img alt="" src=images/Fasteners_ScrewCalculator.svg  style="width:32px;"> [Kalkulator śrub](Fasteners_ScrewCalculator/pl.md): pokaż kalkulator, aby określić wielkość otworu gwintowanego dla śrub.

-   <img alt="" src=images/Fasteners_ChangeParameters.svg  style="width:32px;"> [Zmień parametry](Fasteners_ChangeParameters/pl.md): umożliwia dokonanie zmian parametrów elementów złącznych.



## Elementy złączne 

Elementy złączne o wymiarach metrycznych posiadają ikony w kolorze pomarańczowym. Elementy złączne o wymiarach calowych posiadają zielone ikony.



### Śruby i wkręty z łbem sześciokątnym 

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.6.svg  style="width:32px;"> **ASME B18.2.1.6** Śruba UNC z łbem sześciokątnym.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.8.svg  style="width:32px;"> **ASME B18.2.1.8** Śruba UNC z łbem sześciokątnym z kołnierzem.

-   <img alt="" src=images/Fasteners_DIN571.svg  style="width:32px;"> **DIN 571** Wkręt do drewna z łbem sześciokątnym.

-   <img alt="" src=images/Fasteners_DIN933.svg  style="width:32px;"> **DIN 933** Śruba z łbem sześciokątnym.

-   <img alt="" src=images/Fasteners_DIN961.svg  style="width:32px;"> **DIN 961** Śruba z łbem sześciokątnym.

-   <img alt="" src=images/Fasteners_EN1662.svg  style="width:32px;"> **EN 1662** Śruba z łbem sześciokątnym z kołnierzem, seria mała.

-   <img alt="" src=images/Fasteners_EN1665.svg  style="width:32px;"> **EN 1665** Śruba sześciokątna z kołnierzem, seria gruba.

-   <img alt="" src=images/Fasteners_ISO4014.svg  style="width:32px;"> **ISO 4014** Śruba z łbem sześciokątnym. *Klasy produktów A i B*.

-   <img alt="" src=images/Fasteners_ISO4015.svg  style="width:32px;"> **ISO 4015** Śruba z łbem sześciokątnym ze zredukowanym trzpieniem.

-   <img alt="" src=images/Fasteners_ISO4016.svg  style="width:32px;"> **ISO 4016** Śruba z łbem sześciokątnym. *Klasa produktu C*.

-   <img alt="" src=images/Fasteners_ISO4017.svg  style="width:32px;"> **ISO 4017** Śruba z łbem sześciokątnym. *Klasy produktów A i B*.

-   <img alt="" src=images/Fasteners_ISO4018.svg  style="width:32px;"> **ISO 4018** Śruba z łbem sześciokątnym. *Klasa produktu C*.

-   <img alt="" src=images/Fasteners_ISO4162.svg  style="width:32px;"> **ISO 4162** Śruba sześciokątna z kołnierzem, seria mała. *Produkt klasy A z właściwościami napędowymi klasy produktu B*.

-   <img alt="" src=images/Fasteners_ISO8676.svg  style="width:32px;"> **ISO 8676** Śruba z łbem sześciokątnym z gwintem o drobnym skoku. *Klasy produktów A i B*.

-   <img alt="" src=images/Fasteners_ISO8765.svg  style="width:32px;"> **ISO 8765** Śruba z łbem sześciokątnym z gwintem o drobnym skoku.

-   <img alt="" src=images/Fasteners_ISO15071.svg  style="width:32px;"> 
**ISO 15071** Śruba sześciokątna z kołnierzem, seria mała. *Klasa produktu A.*

-   <img alt="" src=images/Fasteners_ISO15072.svg  style="width:32px;"> **ISO 15072** Śruba sześciokątna z kołnierzem i gwintem o drobnym skoku, seria mała. *Klasa produktu A*.



### Śruby z gniazdem sześciokątnym 

-   <img alt="" src=images/Fasteners_ASMEB18.3.1A.svg  style="width:32px;"> **ASME B18.3.1A** Śruba UNC z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1G.svg  style="width:32px;"> **ASME B18.3.1G** Śruba UNC z łbem sześciokątnym niskim.

-   <img alt="" src=images/Fasteners_ASMEB18.3.2.svg  style="width:32px;"> **ASME B18.3.2** Śruba UNC z łbem stożkowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3A.svg  style="width:32px;"> **ASME B18.3.3A** Śruba UNC z łbem kulistym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3B.svg  style="width:32px;"> **ASME B18.3.3B** Śruba UNC z łbem sześciokątnym z kołnierzem.

-   <img alt="" src=images/Fasteners_ASMEB18.3.4.svg  style="width:32px;"> **ASME B18.3.4** Śruba UNC z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_DIN6912.svg  style="width:32px;"> **DIN 6912** Śruba z łbem o gnieździe sześciokątnym z niskim łbem i środkiem.

-   <img alt="" src=images/Fasteners_DIN7984.svg  style="width:32px;"> **DIN 7984** Śruba z gniazdem sześciokątnym z niskim łbem.

-   <img alt="" src=images/Fasteners_ISO2936.svg  style="width:32px;"> **ISO 2936** Klucz imbusowy do śruby sześciokątnej.

-   <img alt="" src=images/Fasteners_ISO4762.svg  style="width:32px;"> **ISO 4762** Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO7379.svg  style="width:32px;"> **ISO 7379** Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO7380-1.svg  style="width:32px;"> **ISO 7380-1** Śruba z łbem kulistym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO7380-2.svg  style="width:32px;"> **ISO 7380-2** Śruba z łbem sześciokątnym z kołnierzem.

-   <img alt="" src=images/Fasteners_ISO10642.svg  style="width:32px;"> **ISO 10642** Śruba z łbem stożkowym z gniazdem sześciokątnym.



### Śruby z gniazdem sześciokątnym, gwiazdowym (torx) 

-   <img alt="" src=images/Fasteners_ISO14579.svg  style="width:32px;"> **ISO 14579** Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO14580.svg  style="width:32px;"> **ISO 14580** Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO14581.svg  style="width:32px;"> **ISO 14581** Śruba z łbem stożkowym płaskim z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO14582.svg  style="width:32px;"> **ISO 14582** Śruba z łbem stożkowym z gniazdem sześciokątnym, wysoki łeb.

-   <img alt="" src=images/Fasteners_ISO14583.svg  style="width:32px;"> **ISO 14583** Śruba z łbem walcowym z gniazdem sześciokątnym.

-   <img alt="" src=images/Fasteners_ISO14584.svg  style="width:32px;"> **ISO 14584** Śruba z łbem stożkowym z gniazdem sześciokątnym.



### Śruby z łbem z nacięciem prostym 

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.2.svg  style="width:32px;"> **ASME B18.6.1.2** Wkręt do drewna z płaskim łbem stożkowym, z rowkiem.

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.4.svg  style="width:32px;"> **ASME B18.6.1.4** Wkręt do drewna z owalnym łbem stożkowym z rowkiem.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1A.svg  style="width:32px;"> **ASME B18.6.3.1A** Śruba UNC z stożkowym łbem płaskim z rowkiem.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.4A.svg  style="width:32px;"> **ASME B18.6.3.4A** Śruba UNC z łbem stożkowym owalnym.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.9A.svg  style="width:32px;"> **ASME B18.6.3.9A** Śruba UNC z łbem płaskim.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.10A.svg  style="width:32px;"> **ASME B18.6.3.10A** Śruba UNC z łbem walcowo soczewkowym z rowkiem.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.12A.svg  style="width:32px;"> **ASME B18.6.3.12A** Śruba UNC z łbem trójlistkowym i rowkiem.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.16A.svg  style="width:32px;"> **ASME B18.6.3.16A** Śruba UNC z łbem stożkowym z rowkiem.

-   <img alt="" src=images/Fasteners_DIN84.svg  style="width:32px;"> 
**DIN 84 (zastąpiony przez ISO 1207)**. Śruba z łbem walcowym z rowkiem. *Klasa produktu A.*

-   <img alt="" src=images/Fasteners_DIN96.svg  style="width:32px;"> **DIN 96** Wkręt do drewna z rowkiem i półokrągłym łbem.

-   <img alt="" src=images/Fasteners_GOST1144-1.svg  style="width:32px;"> **GOST 1144-1** Wkręt do drewna z rowkiem i półokrągłym łbem.

-   <img alt="" src=images/Fasteners_GOST1144-2.svg  style="width:32px;"> **GOST 1144-2** Wkręt do drewna z rowkiem i półokrągłym łbem.

-   <img alt="" src=images/Fasteners_ISO1207.svg  style="width:32px;"> **ISO 1207** Śruba z łbem serowym z rowkiem. *Produkt klasy A*.

-   <img alt="" src=images/Fasteners_ISO1580.svg  style="width:32px;"> **ISO 1580** Śruba z łbem walcowym z rowkiem. *Klasa produktu A*.

-   <img alt="" src=images/Fasteners_ISO2009.svg  style="width:32px;"> **ISO 2009** Śruba z łbem płaskim z rowkiem stożkowym. *Klasa produktu A*.

-   <img alt="" src=images/Fasteners_ISO2010.svg  style="width:32px;"> **ISO 2010** Śruba z łbem wpuszczanym z podwyższonym rowkiem. *Klasa produktu A*.



### Śruby z łbem z nacięciem krzyżowym typu H 

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.3.svg  style="width:32px;"> **ASME B18.6.1.3** \"ASME B18.6.1.3\" Wkręt do drewna z płaskim łbem z wcięciem.

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.5.svg  style="width:32px;"> 
**ASME B18.6.1.5**

Wkręt do drewna z łbem stożkowym owalnym.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1B.svg  style="width:32px;"> **ASME B18.6.3.1B** Śruba UNC z łbem stożkowym płaskim.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.4B.svg  style="width:32px;"> **ASME B18.6.3.4B** Śruba UNC z łbem stożkowym owalnym.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.9B.svg  style="width:32px;"> **ASME B18.6.3.9B** Śruba UNC Śruba z łbem cylindrycznym.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.10B.svg  style="width:32px;"> **ASME B18.6.3.10B** Śruba UNC z łbem walcowym.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.12C.svg  style="width:32px;"> **ASME B18.6.3.12C** Śruba UNC z łbem grzybkowym.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.16B.svg  style="width:32px;"> **ASME B18.6.3.16B** Śruba UNC z łbem okrągłym.

-   <img alt="" src=images/Fasteners_DIN967.svg  style="width:32px;"> **DIN 967** Śruba z łbem kulistym i kołnierzem.

-   <img alt="" src=images/Fasteners_DIN7996.svg  style="width:32px;"> **DIN 7996** Wkręt do drewna z łbem kulistym.

-   <img alt="" src=images/Fasteners_GOST1144-3.svg  style="width:32px;"> **GOST 1144-3** Wkręt do drewna łbem kulistym.

-   <img alt="" src=images/Fasteners_GOST1144-4.svg  style="width:32px;"> **GOST 1144-4** Wkręt do drewna łbem kulistym.

-   <img alt="" src=images/Fasteners_ISO7045.svg  style="width:32px;"> **ISO 7045** Śruba z łbem płaskim, stożkowym. *Klasa produktu A*.

-   <img alt="" src=images/Fasteners_ISO7046.svg  style="width:32px;"> **ISO 7046** Śruba z łbem płaskim, stożkowym. *Klasa produktu A*.

-   <img alt="" src=images/Fasteners_ISO7047.svg  style="width:32px;"> **ISO 7047** Śruba z łbem stożkowym podniesionym. *Klasa produktu A*.

-   <img alt="" src=images/Fasteners_ISO7048.svg  style="width:32px;"> **ISO 7048** Śruba z łbem płaskim.

-   <img alt="" src=images/Fasteners_ISO7049-C.svg  style="width:32px;"> **ISO 7049-C** Śruba samogwintująca z łbem cylindrycznym z klinowym końcem.

-   <img alt="" src=images/Fasteners_ISO7049-F.svg  style="width:32px;"> **ISO 7049-F** Śruba samogwintująca z łbem cylindrycznym z płaskim końcem.

-   <img alt="" src=images/Fasteners_ISO7049-R.svg  style="width:32px;"> **ISO 7049-R** Śruba samogwintująca z łbem cylindrycznym z zaokrąglonym końcem.



### Inne śruby z łbami 

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.1.svg  style="width:32px;"> **ASME B18.2.1.1** Śruba UNC z łbem kwadratowym.

-   <img alt="" src=images/Fasteners_ASMEB18.5.2.svg  style="width:32px;"> **ASME B18.5** Śruba UNC z okrągłym łbem i kwadratową szyjką.

-   <img alt="" src=images/Fasteners_DIN478.svg  style="width:32px;"> **DIN 478** Śruba z kwadratowym łbem z kołnierzem.

-   <img alt="" src=images/Fasteners_DIN603.svg  style="width:32px;"> **DIN 603** Śruba z okrągłym łbem i kwadratową szyjką.

-   <img alt="" src=images/Fasteners_ISO2342.svg  style="width:32px;"> **ISO 2342** Śruba bez łba z trzpieniem.



### Wkręty dociskowe 

-   <img alt="" src=images/Fasteners_ASMEB18.3.5A.svg  style="width:32px;"> **ASME B18.3.5A** Wkręty UNC dociskowe z gniazdem na imbus i płaskim końcem.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5B.svg  style="width:32px;"> **ASME B18.3.5B** Wkręty UNC dociskowe z gniazdem na imbus i końcówką stożkową.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5C.svg  style="width:32px;"> **ASME B18.3.5C** Wkręty UNC dociskowe z gniazdem na imbus z końcówką zaczepową.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5D.svg  style="width:32px;"> **ASME B18.3.5D** Wkręty UNC dociskowe z gniazdem na imbus i końcówką kielichową.

-   <img alt="" src=images/Fasteners_ISO4026.svg  style="width:32px;"> **ISO 4026** Wkręt dociskowy z gniazdem na imbus i płaskim końcem.

-   <img alt="" src=images/Fasteners_ISO4027.svg  style="width:32px;"> **ISO 4027** Wkręt dociskowy z gniazdem na imbus i końcówką stożkową.

-   <img alt="" src=images/Fasteners_ISO4028.svg  style="width:32px;"> **ISO 4028** Wkręt dociskowy z gniazdem na imbus z końcówką kłową.

-   <img alt="" src=images/Fasteners_ISO4029.svg  style="width:32px;"> **ISO 4029** Wkręt dociskowy z gniazdem na imbus i końcówką kielichową.

-   <img alt="" src=images/Fasteners_ISO4766.svg  style="width:32px;"> **ISO 4766** Wkręt z łbem walcowym z wgłębieniem krzyżowym.

-   <img alt="" src=images/Fasteners_ISO7434.svg  style="width:32px;"> **ISO 7434** Wkręt dociskowy z gniazdem rowkowym i stożkiem.

-   <img alt="" src=images/Fasteners_ISO7435.svg  style="width:32px;"> **ISO 7435** Wrkęt dociskowy z rowkiem i długim ząbkowanym czubkiem.

-   <img alt="" src=images/Fasteners_ISO7436.svg  style="width:32px;"> **ISO 7436** Wkręt dociskowy z rowkiem z łbem walcowym z końcówką kielichową.



### Śruby z łbem motylkowym 

-   <img alt="" src=images/Fasteners_DIN464.svg  style="width:32px;"> **DIN 464** Śruba radełkowana, typ wysoki.

-   <img alt="" src=images/Fasteners_DIN465.svg  style="width:32px;"> **DIN 465** Śruba radełkowana z rowkiem, typ wysoki.

-   <img alt="" src=images/Fasteners_DIN653.svg  style="width:32px;"> **DIN 653** Śruba radełkowana, typ niski.



### Nakrętki

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1A.svg  style="width:32px;"> **ASME B18.2.2.1A** Nakrętka sześciokątna UNC do śrub maszynowych.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1B.svg  style="width:32px;"> **ASME B18.2.2.1B** Kwadratowa nakrętka UNC do śrub maszynowych.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.2.svg  style="width:32px;"> **ASME 18.2.2** Nakrętka UNC kwadratowa.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4A.svg  style="width:32px;"> **ASME B18.2.2.4A** Nakrętka UNC sześciokątna.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4B.svg  style="width:32px;"> **ASME B18.2.2.4B** Nakrętka UNC sześciokątna cienka.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.5.svg  style="width:32px;"> **ASME 18.2.2.5** Nakrętka UNC sześciokątna zamkowa.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.12.svg  style="width:32px;"> **ASME 18.2.2.12** Nakrętka UNC sześciokątna z kołnierzem.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.13.svg  style="width:32px;"> **ASME 18.2.2.13** Nakrętka UNC sześciokątna sprzęgająca.

-   <img alt="" src=images/Fasteners_ASMEB18.6.9A.svg  style="width:32px;"> **ASME 18.6.9A** Nakrętka motylkowa, typ A.

-   <img alt="" src=images/Fasteners_DIN315.svg  style="width:32px;"> **DIN 315** Nakrętka motylkowa.

-   <img alt="" src=images/Fasteners_DIN557.svg  style="width:32px;"> **DIN 557** Nakrętka kwadratowa.

-   <img alt="" src=images/Fasteners_DIN562.svg  style="width:32px;"> **DIN 562** Nakrętka kwadratowa.

-   <img alt="" src=images/Fasteners_DIN917.svg  style="width:32px;"> **DIN 917** Nakrętka kołpakowa, niska.

-   <img alt="" src=images/Fasteners_DIN928.svg  style="width:32px;"> **DIN 928** Nakrętka kwadratowa do spawania.

-   <img alt="" src=images/Fasteners_DIN929.svg  style="width:32px;"> **DIN 929** Nakrętka sześciokątna do spawania.

-   <img alt="" src=images/Fasteners_DIN934.svg  style="width:32px;"> **DIN 934 (zastąpiona przez ISO 4035 i ISO 8673)** Nakrętka sześciokątna cienka, fazowana. *Klasy produktów A i B*.

-   <img alt="" src=images/Fasteners_DIN935.svg  style="width:32px;"> **DIN 935** Nakrętka sześciokątna zamkowa.

-   <img alt="" src=images/Fasteners_DIN985.svg  style="width:32px;"> **DIN 985** Nakrętka Nyloc.

-   <img alt="" src=images/Fasteners_DIN1587.svg  style="width:32px;"> **DIN 1587** Nakrętka kołpakowa.

-   <img alt="" src=images/Fasteners_DIN6330.svg  style="width:32px;"> **DIN 6330** Nakrętka sześciokątna, wysokości 1,5d.

-   <img alt="" src=images/Fasteners_DIN6331.svg  style="width:32px;"> **DIN 6331** Nakrętka sześciokątna z kołnierzem o wysokości 1,5d.

-   <img alt="" src=images/Fasteners_DIN6334.svg  style="width:32px;"> **DIN 6334** Nakrętka sześciokątna sprzęgająca.

-   <img alt="" src=images/Fasteners_DIN7967.svg  style="width:32px;"> **DIN 7967** Samozabezpieczająca przeciwnakrętka.

-   <img alt="" src=images/Fasteners_EN1661.svg  style="width:32px;"> **EN 1661** Nakrętka sześciokątna z kołnierzem.

-   <img alt="" src=images/Fasteners_GOST11860-1.svg  style="width:32px;"> **GOST 11860-1** Nakrętka kołpakowa.

-   <img alt="" src=images/Fasteners_ISO4032.svg  style="width:32px;"> **ISO 4032** Nakrętka sześciokątna, styl 1. *Klasy produktów A i B.*.

-   <img alt="" src=images/Fasteners_ISO4033.svg  style="width:32px;"> 
**ISO 4033** Nakrętka sześciokątna wysoka, typ 2. *Klasy produktów A i B.*

-   <img alt="" src=images/Fasteners_ISO4034.svg  style="width:32px;"> **ISO 4034** Nakrętka sześciokątna typ 1.

-   <img alt="" src=images/Fasteners_ISO4035.svg  style="width:32px;"> 
**ISO 4035** Nakrętka sześciokątna cienka, fazowana, typ 0. *Klasy produktów A i B.*

-   <img alt="" src=images/Fasteners_ISO4161.svg  style="width:32px;"> **ISO 4161** Nakrętka sześciokątna z kołnierzem.

-   <img alt="" src=images/Fasteners_ISO7040.svg  style="width:32px;"> **ISO 7040** Nakrętka sześciokątna samohamowna *(z wkładką niemetalową)*.

-   <img alt="" src=images/Fasteners_ISO7041.svg  style="width:32px;"> **ISO 7041** Nakrętka sześciokątna samohamowna *(z wkładką niemetalową)*, styl 2.

-   <img alt="" src=images/Fasteners_ISO7043.svg  style="width:32px;"> **ISO 7043** Nakrętka sześciokątna samohamowna z kołnierzem *(z wkładką niemetalową)*.

-   <img alt="" src=images/Fasteners_ISO7044.svg  style="width:32px;"> **ISO 7044** Nakrętka sześciokątna, samohamowna z kołnierzem wykonana w całości z metalu.

-   <img alt="" src=images/Fasteners_ISO7719.svg  style="width:32px;"> **ISO 7719** Nakrętka sześciokątna, samohamowna wykonana w całości z metalu.

-   <img alt="" src=images/Fasteners_ISO7720.svg  style="width:32px;"> **ISO 7720** Nakrętka sześciokątna,samohamowna typu 2, wykonana w całości z metalu.

-   <img alt="" src=images/Fasteners_ISO8673.svg  style="width:32px;"> 
**ISO 8673** Nakrętka sześciokątna z gwintem o drobnym skoku, typ 1. *Klasy produktów A i B.*

-   <img alt="" src=images/Fasteners_ISO8674.svg  style="width:32px;"> 
**ISO 8674** Nakrętka sześciokątna z gwintem o drobnym skoku, typ 2. *Klasy produktów A i B.*

-   <img alt="" src=images/Fasteners_ISO8675.svg  style="width:32px;"> 
**ISO 8675** Nakrętka sześciokątna cienka z gwintem o drobnym skoku, styl 0. *Klasa produktu A i B.*

-   <img alt="" src=images/Fasteners_ISO10511.svg  style="width:32px;"> **ISO 10511** Nakrętka sześciokątna, samohamowna cienka *(z wkładką niemetalową)*.

-   <img alt="" src=images/Fasteners_ISO10512.svg  style="width:32px;"> **ISO 10512** Nakrętka sześciokątna, samohamowna z gwintem o drobnym skoku *(z wkładką niemetalową)*.

-   <img alt="" src=images/Fasteners_ISO10513.svg  style="width:32px;"> **ISO 10513** Nakrętka sześciokątna, samohamowna z gwintem o drobnym skoku, wykonana w całości z metalu.

-   <img alt="" src=images/Fasteners_ISO10663.svg  style="width:32px;"> **ISO 10663** Nakrętka sześciokątna z kołnierzem i gwintem o drobnym skoku.

-   <img alt="" src=images/Fasteners_ISO12125.svg  style="width:32px;"> **ISO 12125** Nakrętka sześciokątna. samohamowna z kołnierzem i gwintem o drobnym skoku *(z wkładką niemetalową)*.

-   <img alt="" src=images/Fasteners_ISO12126.svg  style="width:32px;"> **ISO 12126** Nakrętka sześciokątna, samohamowna z kołnierzem i gwintem o drobnym skoku.

-   <img alt="" src=images/Fasteners_ISO21670.svg  style="width:32px;"> **ISO 21670** Nakrętka sześciokątna, do spawania z kołnierzem.

-   <img alt="" src=images/Fasteners_SAEJ483a1.svg  style="width:32px;"> **SAE J483a 1** Nakrętka niska kołpakowa.

-   <img alt="" src=images/Fasteners_SAEJ483a2.svg  style="width:32px;"> **SAE J483a 2** Wysoka nakrętka kołpakowa.



### Łączniki z rowkiem teowym 

-   <img alt="" src=images/Fasteners_DIN508.svg  style="width:32px;"> **DIN 508** Nakrętka młoteczkowa, do rowka T.

-   <img alt="" src=images/Fasteners_GN505.svg  style="width:32px;"> **GN 505** Nakrętka ząbkowana ćwierćobrotowa do rowka T.

-   <img alt="" src=images/Fasteners_GN505.4.svg  style="width:32px;"> **GN 505.4** Śruba ząbkowana do rowka T.

-   <img alt="" src=images/Fasteners_GN506.svg  style="width:32px;"> **GN 506** Nakrętka do rowków T z możliwością obracania.

-   <img alt="" src=images/Fasteners_GN507.svg  style="width:32px;"> **GN 507** Nakrętka przesuwna do rowków teowych.

-   <img alt="" src=images/Fasteners_ISO299.svg  style="width:32px;"> **ISO 299** Nakrętka do rowka T.



### Podkładki

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12A.svg  style="width:32px;"> **ASME B18.21.1.12A** Podkładka UN, seria wąska.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12B.svg  style="width:32px;"> **ASME B18.21.1.12B** Podkładka UN, seria regularna.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12C.svg  style="width:32px;"> **ASME B18.21.1.12C** Podkładka UN, seria szeroka.

-   <img alt="" src=images/Fasteners_DIN6319C.svg  style="width:32px;"> **DIN 6319C** Podkładka sferyczna.

-   <img alt="" src=images/Fasteners_DIN6319D.svg  style="width:32px;"> **DIN 6319D** Podkładka z gniazdem stożkowym.

-   <img alt="" src=images/Fasteners_DIN6319G.svg  style="width:32px;"> **DIN 6319G** Podkładka z gniazdem stożkowym.

-   <img alt="" src=images/Fasteners_DIN6340.svg  style="width:32px;"> **DIN 6340** Podkładka do urządzeń zaciskowych.

-   <img alt="" src=images/Fasteners_ISO7089.svg  style="width:32px;"> 
**ISO 7089** Podkładka ślizgowa, seria normalna. *Klasa produktu A.*

-   <img alt="" src=images/Fasteners_ISO7090.svg  style="width:32px;"> **ISO 7090** Podkładka ślizgowa fazowana, seria normalna. *Klasa produktu A*.

-   <img alt="" src=images/Fasteners_ISO7092.svg  style="width:32px;"> **ISO 7092** Podkładka zwykła, seria mała. *Klasa produktu A*.

-   <img alt="" src=images/Fasteners_ISO7093-1.svg  style="width:32px;"> 
**ISO 7093-1** Podkładka ślizgowa, seria duża. *Klasa produktu A.*

-   <img alt="" src=images/Fasteners_ISO7094.svg  style="width:32px;"> **ISO 7094** Podkładka zwykła, seria ekstra duża. *Klasa produktu C*.

-   <img alt="" src=images/Fasteners_ISO8738.svg  style="width:32px;"> **ISO 8738** Zwykła podkładka pod sworzeń widełkowy.

-   <img alt="" src=images/Fasteners_NFE27-619.svg  style="width:32px;"> **NFE27-619** Podkładka stożkowa.



### Pręty, gwintowniki i matryce 

-   <img alt="" src=images/Fasteners_ScrewTapInch.svg  style="width:32px;"> Pręt gwintowany calowy do nacinania otworów.

-   <img alt="" src=images/Fasteners_ScrewDieInch.svg  style="width:32px;"> Narzędzie do cięcia zewnętrznych gwintów calowych.

-   <img alt="" src=images/Fasteners_ThreadedRodInch.svg  style="width:32px;"> **DIN 975** Pręt gwintowany calowy UNC.

-   <img alt="" src=images/Fasteners_ThreadedRod.svg  style="width:32px;"> **DIN 975** Pręt gwintowany metryczny.

-   <img alt="" src=images/Fasteners_ScrewTap.svg  style="width:32px;"> Pręt gwintowany metryczny do nacinania otworów.

-   <img alt="" src=images/Fasteners_ScrewDie.svg  style="width:32px;"> Narzędzie do nacinania zewnętrznych gwintów metrycznych.



#### Wkładki

-   <img alt="" src=images/Fasteners_IUTHeatInsert.svg  style="width:32px;"> Wkładka metryczna mocowana na gorąco.

-   <img alt="" src=images/Fasteners_PEMPressNut.svg  style="width:32px;"> Nakrętka samokontrująca PEM.

-   <img alt="" src=images/Fasteners_PEMStandoff.svg  style="width:32px;"> Dystans samokontrujący PEM.

-   <img alt="" src=images/Fasteners_PEMStud.svg  style="width:32px;"> Kołek samozaciskowy PEM.

-   <img alt="" src=images/Fasteners_PCBSpacer.svg  style="width:32px;"> Podkładka dystansowa **PCB** żeńska / żeńska.

-   <img alt="" src=images/Fasteners_PCBStandoff.svg  style="width:32px;"> Element dystansowy **PCB** męski / żeński.

-   <img alt="" src=images/Fasteners_4PWTI.svg  style="width:32px;"> Wkładka gwintowana do drewna z czterema ząbkami *(nakrętki typu T DIN 1624)*.



### Pierścienie osadcze 

-   <img alt="" src=images/Fasteners_DIN471.svg  style="width:32px;"> **DIN 471** Zewnętrzny metryczny pierścień Segera.

-   <img alt="" src=images/Fasteners_DIN472.svg  style="width:32px;"> **DIN 472** Wewnętrzny metryczny pierścień Segera.

-   <img alt="" src=images/Fasteners_DIN6799.svg  style="width:32px;"> **DIN 6799** Płytka osadcza metryczna E-clip.



### Gwoździe

-   <img alt="" src=images/Fasteners_DIN1143.svg  style="width:32px;"> **DIN 1143** Gwóźdź z okrągłym łbem do stosowania w automatach gwoździarskich.

-   <img alt="" src=images/Fasteners_DIN1144-A.svg  style="width:32px;"> **DIN 1144-A** Gwóźdź do montażu płyt kompozytowych z wełny drzewnej, łeb okrągły 20 mm.

-   <img alt="" src=images/Fasteners_DIN1151-A.svg  style="width:32px;"> **DIN 1151-A** Okrągły gładki gwoźdź o płaskiej główce.

-   <img alt="" src=images/Fasteners_DIN1151-B.svg  style="width:32px;"> **DIN 1151-B** Okrągły gładki gwoźdź o wpuszczanej główce.

-   <img alt="" src=images/Fasteners_DIN1152.svg  style="width:32px;"> **DIN 1152** Gwóźdź z okrągłym łbem.

**DIN 1160-A** Gwoźdź ciesielski lub dachowy.

-   <img alt="" src=images/Fasteners_DIN1160-B.svg  style="width:32px;"> **DIN 1160-B** Gwoźdź ciesielski lub dachowy z szeroką główką.



### Szpilki

-   <img alt="" src=images/Fasteners_ISO1234.svg  style="width:32px;"> **ISO 1234** Zawleczka.

-   <img alt="" src=images/Fasteners_ISO2338.svg  style="width:32px;"> **ISO 2338** Sworzeń równoległy.

-   <img alt="" src=images/Fasteners_ISO2339.svg  style="width:32px;"> **ISO 2339** Sworzeń stożkowy.

-   <img alt="" src=images/Fasteners_ISO2340A.svg  style="width:32px;"> **ISO 2340A** Sworzeń widełkowy.

-   <img alt="" src=images/Fasteners_ISO2340B.svg  style="width:32px;"> **ISO 2340B** Sworzeń widełkowy bez główki *(z otworami na zawleczkę)*.

-   <img alt="" src=images/Fasteners_ISO2341A.svg  style="width:32px;"> **ISO 2341A** Sworzeń rozporowy z główką.

-   <img alt="" src=images/Fasteners_ISO2341B.svg  style="width:32px;"> **ISO 2341B** Sworzeń widełkowy z główką *(z otworem na zawleczkę)*.

-   <img alt="" src=images/Fasteners_ISO8733.svg  style="width:32px;"> **ISO 8733** Sworzeń cylindryczny z wewnętrznym gwintem, niehartowany.

-   <img alt="" src=images/Fasteners_ISO8734.svg  style="width:32px;"> **ISO 8734** Sworzeń dociskowy.

-   <img alt="" src=images/Fasteners_ISO8735.svg  style="width:32px;"> **ISO 8735** Sworzeń z gwintem wewnętrznym, hartowany.

-   <img alt="" src=images/Fasteners_ISO8736.svg  style="width:32px;"> **ISO 8736** Sworzeń stożkowy z gwintem wewnętrznym, niehartowany.

-   <img alt="" src=images/Fasteners_ISO8737.svg  style="width:32px;"> **ISO 8737** Sworzeń stożkowy z gwintem zewnętrznym, niehartowany.

-   <img alt="" src=images/Fasteners_ISO8739.svg  style="width:32px;"> **ISO 8739** Sworzeń żłobiony na całej długości z prowadnicą.

-   <img alt="" src=images/Fasteners_ISO8740.svg  style="width:32px;"> **ISO 8740** Sworzeń żłobiony na całej długości z fazą.

-   <img alt="" src=images/Fasteners_ISO8741.svg  style="width:32px;"> **ISO 8741** Sworzeń stożkowy żłobiony w odwrotnym kierunku, na połowie długości.

-   <img alt="" src=images/Fasteners_ISO8742.svg  style="width:32px;"> **ISO 8742** \"ISO 8742\" Sworzeń z wgłębieniem środkowym na długości jednej trzeciej.

-   <img alt="" src=images/Fasteners_ISO8743.svg  style="width:32px;"> **ISO 8743** \"ISO 8743\" Sworzeń z wgłębieniem środkowym na połowie długości.

-   <img alt="" src=images/Fasteners_ISO8744.svg  style="width:32px;"> **ISO 8744** Sworzeń z wgłębieniem stożkowym na całej długości.

-   <img alt="" src=images/Fasteners_ISO8745.svg  style="width:32px;"> **ISO 8745** Sworzeń z wgłębieniem stożkowym na połowie długości.

-   <img alt="" src=images/Fasteners_ISO8746.svg  style="width:32px;"> **ISO 8746** Sworzeń z rowkiem i zaokrągloną główką.

-   <img alt="" src=images/Fasteners_ISO8747.svg  style="width:32px;"> **ISO 8747** Sworzeń z rowkiem z łbem stożkowym.

-   <img alt="" src=images/Fasteners_ISO8748.svg  style="width:32px;"> **ISO 8748** Sworzeń sprężynowy zwojowy, o wzmocnionej konstrukcji.

-   <img alt="" src=images/Fasteners_ISO8750.svg  style="width:32px;"> **ISO 8750** **ISO 8750** Sworzeń sprężynowy zwojowy, standardowej wytrzymałości.

-   <img alt="" src=images/Fasteners_ISO8751.svg  style="width:32px;"> **ISO 8751** Sworzeń sprężynowy zwojowy, do lekkich obciążeń.

-   <img alt="" src=images/Fasteners_ISO8752.svg  style="width:32px;"> **ISO 8752** Sworzeń sprężynujący z rowkiem, do dużych obciążeń.

-   <img alt="" src=images/Fasteners_ISO13337.svg  style="width:32px;"> **ISO 13337** **ISO 8752** Sworzeń sprężynujący z rowkiem, do lekkich obciążeń.



## Przestarzałe

-   <img alt="" src=images/Fasteners_ChamferHole.svg  style="width:32px;"> [Utwórz pogłębienie stożkowe](Fasteners_ChamferHole/pl.md): sfazowanie otworów pod wkręty z łbem stożkowym. Niedostępne w {{VersionPlus/pl|0.5.13}}.



## Bibliografia

-   Autor: [shaise](http://theseger.com/projects/author/shaise/),
    -   ScrewMaker: Ulrich Brammer,
    -   Workbench wrapper: Shai Seger,
-   Kod źródłowy: <https://github.com/shaise/FreeCAD_FastenersWB>,
-   Zgłoszenia błędów i prośby o nowe funkcje: <https://github.com/shaise/FreeCAD_FastenersWB/issues>,
-   Tematy na forum: <https://forum.freecadweb.org/viewtopic.php?t=11429>.



## Odnośniki internetowe 

-   [ŚRUBY](https://github.com/jreinhardt/BOLTS): Otwarta biblioteka dla specyfikacji technicznych


{{Fasteners_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [External_Workbenches](Category_External_Workbenches.md) > Fasteners Workbench/pl
