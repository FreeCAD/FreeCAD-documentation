---
 GuiCommand:
   Name: SheetMetal AddJunction
   Name/pl: Arkusz Blachy: Wykonaj połączenie
   MenuLocation: SheetMetal , Wykonaj połączenie
   Workbenches: SheetMetal_Workbench/pl
   Shortcut: **S** **J**
   SeeAlso: SheetMetal_AddRelief/pl, SheetMetal_AddBend/pl
---

# SheetMetal AddJunction/pl



## Opis

Polecenie <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:24px;"> **Wykonaj połączenie** tworzy otwarte połączenia między dwiema sekcjami *(ścianami / kołnierzami)* obiektu z blachy. Bez tych połączeń sekcje blachy połączone z tą samą podstawą nie będą mogły zostać rozłożone.

To polecenie jest drugim z trzech kroków konwersji obiektu powłoki wykonanego za pomocą środowiska pracy [Część](Part_Workbench/pl.md) lub [Projekt Części](PartDesign_Workbench/pl.md) na rozkładany obiekt z blachy:

1.  [Wykonaj podcięcie](SheetMetal_AddRelief/pl.md)
2.  [Wykonaj połączenie](SheetMetal_AddJunction/pl.md)
3.  [Wykonaj zagięcie](SheetMetal_AddBend/pl.md)

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:100px;"> 
*Wykonaj połączenie - rozcięte krawędzie*



## Użycie

1.  Wybierz jedną lub więcej krawędzi.
2.  Aktywuj polecenie <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **Wykonaj połączenie** używając jednej z poniższych opcji:
    -   Przycisk **<img src="images/SheetMetal_AddJunction.svg" width=16px> Wykonaj połączenie**.
    -   Opcja menu **SheetMetal → <img src="images/SheetMetal_AddJunction.svg" width=16px> Wykonaj połączenie**.
    -   Skrót klawiaturowy: **S** + **J**.

<img alt="" src=images/SheetMetal_ConvertShellObject-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-07.png  style="width:200px;">



## Uwagi

Polecenia <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[Wykonaj podcięcie](SheetMetal_AddRelief/pl.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[Wykonaj połączenie](SheetMetal_AddJunction/pl.md)** i <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[Wykonaj zagięcie](SheetMetal_AddBend/pl.md)** działają najlepiej z obiektami typu \"wydrążony\" prostopadłościan o stałej grubości i kątach 90° między ścianami.

Zobacz stronę z opisem narzędzia [Wykonaj podcięcie](SheetMetal_AddRelief/pl#Uwagi.md), aby uzyskać wskazówki dotyczące tworzenia obiektów powłoki na bazie prostopadłościanów.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Połaczenie środowiska Arkusz Blachy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **Etykieta|String**: Wartość domyślna: {{value|Junction}} *(+ kolejny numer dla drugiej i następnych pozycji)*. Edytowalna przez użytkownika nazwa tego obiektu, może to być dowolny ciąg znaków UTF8.

-    **Cecha podstawowa|Link|ukryte**: Cecha bazowa. Łącze do cechy nadrzędnej.

-    **_Body|LinkHidden|ukryte**: Łącze ukryte do zawartości nadrzędnej.


{{Properties_Title|Parametry}}

-    **Obiekt bazowy|LinkSub**: *Obiekt bazowy*. Łącza do krawędzi definiujących pozycje odstępów / połączeń.

-    **Szczelina|Length**: *Szczelina połączenia*. Domyślnie: {{value|2,00 mm}}. Rozmiar dodawanej szczeliny / połączenia.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddJunction/pl
