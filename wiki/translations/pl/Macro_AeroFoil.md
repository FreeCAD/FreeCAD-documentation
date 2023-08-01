# Macro AeroFoil/pl
{{Macro/pl
|Name=Macro AeroFoil
|Name/pl=Makrodefinicja: Skrzydło samolotu
|Icon=AeroFoil.png
|Description=Makrodefinicja Skrzydło samolotu tworzy krzywe i powierzchnie profilu lotniczego używając predefiniowanych modeli, funkcji algebraicznych oraz plików DAT lub CSV.
|Author=Melwyncarlo
|Date=2021-03-10
|Version=2.0.1
|FCVersion=<small>(v0.17)</small> 
|Download=[https://github.com/melwyncarlo/AeroFoil/blob/main/AeroFoil.zip?raw=true AeroFoil.zip]
|Links=[https://github.com/melwyncarlo/AeroFoil Personal Github - AeroFoil]<br>[https://github.com/FreeCAD/FreeCAD-macros/tree/master/ObjectCreation FC Github - AeroFoil]<br>[https://forum.freecadweb.org/viewtopic.php?f=22&t=56162 forum FreeCAD - AeroFoil]
}}

## Opis

**Skrzydło samolotu** jest narzędziem utworzonym przez użytkownika, które może być używane w aplikacji FreeCAD. Skrzydło samolotu tworzy krzywe i powierzchnie profilu lotniczego używając predefiniowanych modeli, funkcji algebraicznych, jak również importowanych plików DAT lub CSV.

![](images/AeroFoil-reduced.png )    Ikonka makrodefinicji **Skrzydło samolotu**.

Makro Skrzydło samolotu można pobrać za pomocą wbudowany w program FreeCAD [Menadżer dodatków](Std_AddonMgr/pl.md).

####  Główne cechy 

-   Dopracowanie punktów profilu lotniczego.
-   Generowanie wielu kopii profilu lotniczego.
-   Wyjście dla krzywych 2D i powierzchni płaskich.
-   Wyjście dla DWire/PolyLine i BSpline.
-   Wyjście dla środowisk pracy Szkicownik i Rysunek Roboczy.
-   W pełni związane szkice w środowisku pracy Szkicownik.
-   Generowanie krzywych dzielonych *(górnych i dolnych)* dla profilu lotniczego.
-   Gotowe solwery NACA 4 i 5 cyfr.
-   Parser funkcji krzywych symetrycznych i asymetrycznych.
-   Parser danych z plików tekstowych DAT i arkuszy kalkulacyjnych CSV.
-   Wprowadzanie długości cięciwy w mm, cm, m, in, ft i yards.

####  Dodatkowe właściwości {{VersionPlus/pl|0.19}} 

Właściwości obiektu Skrzydło samolotu *(tylko do odczytu)* :
{{Properties Title/pl|Podstawowe}}

-    {{PropertyData/pl|Typ Skrzydła samolotu|String}}
    

-    {{PropertyData/pl|Długość cięciwy płata|Length}}
    

-    {{PropertyData/pl|Typ krzywej projektowej|String}}
    

-    {{PropertyData/pl|Liczba punktów|Integer}}
    

\[\[<File:AeroFoil-output-types.gif%7Cframe%7Ccenter%7Calt=AeroFoil-output-types.gif>\|


<div style="text-align: center">

Opis : Typy danych wyjściowych makrodefinicji Skrzydło samolotu


</div>

\]\]

\[\[<File:AeroFoil-input-types.gif%7Cframe%7Ccenter%7Calt=AeroFoil-input-types.gif>\|


<div style="text-align: center">

Opis : Typy danych wejściowych makrodefinicji Skrzydło samolotu


</div>

\]\]

## Instalacja

####  Linux

\"Skrzydło samolotu\" można zainstalować ręcznie, podobnie jak w przypadku instalacji w systemie Windows, lub za pomocą terminala i odpowiednich poleceń wymienionych w pliku [INSTALL](https://raw.githubusercontent.com/melwyncarlo/AeroFoil/main/INSTALL.sh).

Domyślnie terminal poleceń systemu Linux może być uruchomiony przez jednoczesne naciśnięcie następujących klawiszy:

**Control** + **Alt** + **T**

####  Windows

\"Skrzydło samolotu\" można zainstalować za pomocą następujących dwóch kroków:

1.  Pobierz plik [AeroFoil.zip](https://github.com/melwyncarlo/AeroFoil/blob/main/AeroFoil.zip?raw=true).
2.  Wypakuj zawartość pliku ZIP do katalogu *Macro* użytkownika programu FreeCAD.

Domyślnie, katalog Makro użytkownika FreeCAD powinien znajdować się w lokalizacji:

C:/Users/User_Name/AppData/Roaming/FreeCAD/Macro

## Użycie

\"Skrzydło samolotu\" można załadować, wykonując następujące czynności:

1.  Uruchom aplikację **FreeCAD**.
2.  Przejdź do menu **Makrodefinicje → Makrodefinicje ...**.
3.  Kliknij na zakładkę **Makra użytkownika** w wyskakującym oknie dialogowym.
4.  Wybierz **AeroFoil.FCMacro**.
5.  Kliknij na przycisk **Wykonaj makro**.

Po załadowaniu makra Skrzydło samolotu postępuj zgodnie z instrukcjami w poszczególnych oknach dialogowych, uzupełnij odpowiednie dane wejściowe i wykonaj odpowiednią nawigację. W przypadku wystąpienia błędu lub ostrzeżenia, zostaniesz automatycznie poinformowany o tym fakcie. Jeżeli zostaniesz powiadomiony o nieoczekiwanym błędzie, poinformuj o nim, podając wersję programu FreeCAD, opisując podjęte kroki i informując, czy *(i w jakim stopniu)* został wygenerowany jakikolwiek wynik.

####  Uwagi

   
  *(1)*   Wykonanie operacji makro z punktami niestandardowymi i udoskonaleniem nie powoduje żadnych widocznych zmian.
  *(2)*   Właściwości obiektu AeroFoil są widoczne tylko w wersji programu FreeCAD 0.19. W starszych wersjach pojawi się ostrzeżenie na konsoli. Ostrzeżenie to nie będzie miało wpływu na dane wyjściowe.
          
   

####  Wskazówki, o których należy pamiętać podczas pracy: 

1.  Dla profili NACA, dwie ostatnie cyfry *(łącznie)* nie mogą mieć wartości zero; grubość nie może być wartością zerową.
2.  Pięciocyfrowe profile NACA są ograniczone do następujących modeli *(\"XX\" oznacza dwie ostatnie cyfry, grubość, profilu lotniczego)*:
    -   210XX
    -   220XX
    -   221XX
    -   230XX
    -   231XX
    -   240XX
    -   241XX
    -   250XX
    -   251XX
3.  Dla funkcji krzywych, używaj tylko zestawów znaków i funkcji.
4.  W przypadku funkcji krzywej, $2 * x$ jest poprawne, podczas gdy $2x$ jest niepoprawne.
5.  Dla funkcji krzywej, $y = f(x)$ zawiera się w przedziale od **0** do **1**, w obu przypadkach.
6.  Dla funkcji krzywej, trygonometryczna *theta* jest w stopniach *(**θ °**)*.
7.  Dla funkcji krzywych, trygonometryczna *theta* obejmuje zakres od **0°** do **360°**, z zastrzeżeniem ograniczeń obliczeniowych.
8.  Krzywe lub punkty, które przecinają się między **0** i **1**, zarówno jedno jak i drugie wykluczające się, zwrócą błąd.
9.  Krzywe lub punkty, które zawierają dane dolnego profilu nie mogą być odzwierciedlone.
10. W przypadku importu plików sugeruje się pozostawienie domyślnych wartości numerów wierszy, rzędów i kolumn, chyba że jest się dobrze poinformowanym.
11. Zwiększanie parametrów **refine** i **quantity**\' zwiększa czas obliczeń i zasoby.
12. Bezwzględna długość cięciwy, w milimetrach, nie może być mniejsza niż **1mm**.

\[\[<File:AeroFoil-preset-functions.png%7Cframe%7Ccenter%7Calt=AeroFoil-preset-functions.png>\|


<div style="text-align: center">

Podpis: Wstępnie zdefiniowane znaki i funkcje


</div>

\]\]

## Tworzenie skryptów 


{{MacroCode|code=

__Title__         = "AeroFoil"
__Author__        = "Melwyncarlo"
__Version__       = "2.0.0"
__Date__          = "2021-03-09"
__Comment__       = "AeroFoil creates airfoil curves and faces using pre-defined models, algebraic functions, and DAT or CSV Files"
__Web__           = "https://github.com/melwyncarlo/AeroFoil"
__Wiki__          = "http://www.freecadweb.org/wiki/index.php?title=Macro_AeroFoil"
__Icon__          = "AeroFoil_UI_Files/AeroFoil.svg"
__Help__          = "Click on the AeroFoil button/macro, and follow the instructions in the subsequent dialog boxes."
__Status__        = "stable"
__Requires__      = "Freecad >= v0.17"
__Communication__ = "https://github.com/melwyncarlo/AeroFoil/issues"
__Files__         = "AeroFoil_UI_Files/AeroFoil_Initial_Dialog.ui, AeroFoil_UI_Files/AeroFoil_NACA4Digit_Dialog.ui, \
AeroFoil_UI_Files/AeroFoil_NACA5Digit_Dialog.ui, AeroFoil_UI_Files/AeroFoil_CurvesInput_Dialog.ui, \
AeroFoil_UI_Files/AeroFoil_PointsInput_Dialog.ui, AeroFoil_UI_Files/AeroFoil_DATInput_Dialog.ui, \
AeroFoil_UI_Files/AeroFoil_CSVInput_Dialog.ui, AeroFoil_UI_Files/AeroFoil_FileLoad_Dialog.ui, \
AeroFoil_UI_Files/AeroFoil_Final_Dialog.ui, AeroFoil_UI_Files/AeroFoil_Math_Functions_Box.ui, \
AeroFoil_UI_Files/AeroFoil_mfb_img.gif, AeroFoil_UI_Files/AeroFoil.svg"



#  OS: Ubuntu 18.04.5 LTS
#  Word size of OS: 64-bit
#  Word size of FreeCAD: 64-bit
#  Version: 0.18.4.
#  Build type: Release
#  Python version: 3.6.8
#  Qt version: 5.9.5
#  Coin version: 4.0.0a
#  OCC version: 7.3.0
#  Locale: English/UnitedKingdom (en_GB)

#  OS: Ubuntu 18.04.5 LTS (LXDE/Lubuntu)
#  Word size of OS  : 64-bit
#  Word size of FreeCAD: 64-bit
#  Version: 0.19
#  Build type: Release
#  Branch: unknown
#  Hash: 32200b604d421c4dad527fe587a7d047cf953b4f
#  Python version: 3.6.9
#  Qt version: 5.9.5
#  Coin versio: 4.0.0a
#  OCC version: 7.3.0
#  Locale: English/UnitedKingdom (en_GB)



}}


{{Codeextralink|https://raw.githubusercontent.com/melwyncarlo/AeroFoil/main/AeroFoil.FCMacro}}

## Odnośniki internetowe 

\[1\] [repozytorium Github dla AeroFoil](https://github.com/melwyncarlo/AeroFoil)
\[2\] [FreeCAD Macros Github Repository - AeroFoil](https://github.com/FreeCAD/FreeCAD-macros/tree/master/ObjectCreation)
\[3\] [dyskusja na forum FreeCAD, o - AeroFoil](https://forum.freecadweb.org/viewtopic.php?f=22&t=56162)
\[4\] [Airfoil Tools](http://airfoiltools.com/) zawiera około 1638 różnych profili lotniczych.
\[5\] [Baza danych współrzędnych profili lotniczych UIUC](https://m-selig.ae.illinois.edu/ads/coord_database.html) zawiera około 1600 różnych profili lotniczych.



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro AeroFoil/pl
