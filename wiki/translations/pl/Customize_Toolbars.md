# Customize Toolbars/pl
{{TutorialInfo/pl
|Topic=Przykład
|Level=początkujący
|Time=5 minut
|Author=[Mario52](User:Mario52.md)
|FCVersion=Wszystkie
}}

## Streszczenie

Ten poradnik pokazuje, jak dostosować paski narzędzi do własnych potrzeb. Narzędzia *(włącznie z Makro-narzędziami)* mogą być używane w różnych Środowiskach pracy. Na przykład Makropolecenie staje się Makro-Narzędziem poprzez utworzenie **Tekstu menu**, **Porady dla narzędzia** i **Ikonki**. Następnie to Makro-narzędzie staje się częścią dodatkowego paska narzędzi w środowisku pracy.

## Użycie

**1.** Znajdź menu Dostosuj

-   Kliknij w **Menu główne → Narzędzia → Dostosuj**,

<img alt="Dostosuj" src=images/CustomizeToolBar_01.png  style="width:640px;"> 

-   lub kliknij prawym przyciskiem myszki na dowolnym pasku narzędzi.

<img alt="Szybkie kliknięcie prawym przyciskiem myszki." src=images/CustomizeToolBar_02.png  style="width:640px;"> 

-   Pojawia się okienko modyfikacji.

<img alt="Pojawi się okno Dostosuj" src=images/CustomizeToolBar_03.png  style="width:640px;"> 

**2.** Zrób z makra narzędzie

-   Wybierz zakładkę \"Makrodefinicje\".

-   Aby dodać ikonę dla dostarczonej makrodefinicji kliknij przycisk Obrazek *(oznaczony **... **)*.

<img alt="Wybór paska narzędzi" src=images/CustomizeToolBar_04.png  style="width:640px;"> 

-   Wybierz odpowiadająca Ci ikonę, spośród dostępnych ikon programu FreeCAD,


<div class="mw-collapsible mw-collapsed toccolours">

      \[lub dodaj swoją własną ikonkę klikając w przycisk **Folder ikonek ...**\].                  *(rozwiń aby zobaczyć przykład)*


<div class="mw-collapsible-content">

<img alt="Dodawanie ikonek" src=images/CustomizeToolBar_05.png  style="width:640px;"> 

     \[Otrzymasz okno wyboru plików, wybierz swój własny plik obrazu *(format PNG, 64x64 piksele)*\]

<img alt="Znajdź plik" src=images/CustomizeToolBar_06.png  style="width:640px;"> 


</div>


</div>

-   Wybierz swoją ikonę i kliknij w przycisk **OK**.

<img alt="Wybór ikonki" src=images/CustomizeToolBar_07.png  style="width:640px;"> 

-   Wybrana ikonka jest teraz wyświetlana obok przycisku Obrazek oznaczonego **...**.

<img alt="Wyświetla się twoja ikonka" src=images/CustomizeToolBar_08.png  style="width:640px;"> 

-   W wierszu **Makrodefinicje:** należy wybrać dostarczone makro i podać **Tekst menu**: *(który pojawi się jako etykieta w menu)*. Należy również wypełnić pole **Wskazówka dotycząca narzędzia:** *(tekst pojawi się, gdy kursor myszki znajdzie się nad przyciskiem na pasku narzędzi)*, kolejne wiersze są opcjonalne.

-   Kliknij w przycisk **Dodaj**.

<img alt="Kliknij w przycisk" src=images/CustomizeToolBar_09.png  style="width:640px;"> 

-   Przycisk narzędzia-makro został właśnie utworzony.

<img alt="Twój przycisk jest stworzony" src=images/CustomizeToolBar_10.png  style="width:640px;"> 

**3.** Utwórz pasek narzędzi poza obszarem roboczym **Makrodefinicji**, który zawiera utworzone **Makro-narzędzie**.

-   Wybierz zakładkę *\'Paski narzędzi* i wybierz Środowisko pracy *(dla którego przeznaczony jest pasek narzędzi)* w rozwijanej liście po prawej stronie *(*\'Part\'\' w tym przykładzie)\'\'.

     \<img src=images/Freecad.svg style="width:Od wersji 0.15 istnieje pasek  **[16px"> dostępny wszędzie** . W przypadku wybrania tej opcji, dostarczony pasek narzędzi będzie znajdował się w każdym Środowisku pracy.\]

<img alt="Zakładka pasków narzędzi" src=images/CustomizeToolBar_11.png  style="width:640px;"> 

-   W rozwijanej liście po lewej stronie wybierz **Makropolecenie**.

<img alt="Makrodefinicje" src=images/CustomizeToolBar_12.png  style="width:640px;"> 

-   Na liście pojawia się makro-narzędzie z jego ikoną.

<img alt="Twoja ikona jest na liście" src=images/CustomizeToolBar_13.png  style="width:640px;"> 

-   Kliknij w przycisk **Nowy ...**.

<img alt="Kliknij na \"Nowy\"" src=images/CustomizeToolBar_14.png  style="width:640px;"> 

-   W oknie \"Nowy pasek narzędzi\" wprowadź nazwę dodatkowego paska narzędzi dla Środowiska pracy **Część** i kliknij w przycisk **OK**

<img alt="Wprowadź nazwę dla swojego paska narzędzi" src=images/CustomizeToolBar_15.png  style="width:640px;"> 

-   Pasek narzędzi jest teraz stworzony.

-   Aby dodać utworzone makro-narzędzie do tego paska narzędzi, zaznacz je w lewym oknie, a następnie kliknij przycisk **→** ze strzałką skierowaną w prawo.

<img alt="Wybór makropolecenia" src=images/CustomizeToolBar_07.png  style="width:640px;"> 

-   Stworzyłeś teraz pasek narzędzi zwany \"Camera\" *(z Makro-narzędziem **Camera**)*

-   Kliknij w przycisk **Zamknij**

<img alt="Zamknij" src=images/CustomizeToolBar_17.png  style="width:640px;"> 

-   Twój nowy pasek narzędzi znajduje się teraz w menu prawego przycisku myszy pasków narzędzi. Jego Ikonka *(w naszym przykładzie kamera)* jest widoczna, jeśli pasek narzędzi jest aktywny *(niebieski znacznik)*.

<img alt="Nowy pasek narzędzi" src=images/CustomizeToolBar_18.png  style="width:640px;"> 

## Uwagi

Zobacz również [Dostosowywanie interfejsu użytkownika do własnych potrzeb](Interface_Customization/pl.md).



[Category:Preferences](Category:Preferences.md)

---
[documentation index](../README.md) > [Preferences](Category:Preferences.md) > Customize Toolbars/pl
