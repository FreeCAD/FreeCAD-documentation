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
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Wciśnij przycisk **<img src="images/SheetMetal_AddJunction.svg" width=16px> [Wykonaj połączenie](SheetMetal_AddJunction/pl.md)**.
    -   Wybierz opcję **SheetMetal → <img src="images/SheetMetal_AddJunction.svg" width=16px> Wykonaj połączenie** z menu.
    -   Kliknij prawym przyciskiem myszy w [widoku drzewa](Tree_view/pl.md) lub [widoku 3D](3D_view/pl.md) i wybierz opcję **SheetMetal → <img src="images/SheetMetal_AddJunction.svg" width=16px> Wykonaj połączenie** z menu kontekstowego.
    -   Użyj skrótu klawiaturowego: **S** a następnie **J**.
3.  Otwarty zostanie [panel zadań](Task_panel/pl.md) **Add Junction Parameter** (wprowadzony w wersji 0.5.00).
4.  Opcjonalnie wciśnij przycisk **Wybierz** aby dodać więcej ścian.
    -   Wciśnij przycisk **Podgląd** aby zakończyć wybór i wyświetlić zmiany.
5.  Opcjonalnie dostosuj parametry w panelu zadań.
6.  Wciśnij przycisk **OK** aby zakończyć polecenie i zamknąć panel zadań.
7.  Utworzony zostanie obiekt **Junction** składający się z jednego otwarcia dla każdej wskazanej krawędzi.
8.  Opcjonalnie dostosuj parametry w [Edytorze właściwości](Property_editor/pl.md).

<img alt="" src=images/SheetMetal_ConvertShellObject-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-07.png  style="width:200px;">



## Uwagi

-   Polecenia <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[Wykonaj podcięcie](SheetMetal_AddRelief/pl.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[Wykonaj połączenie](SheetMetal_AddJunction/pl.md)** i <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[Wykonaj zagięcie](SheetMetal_AddBend/pl.md)** działają najlepiej z obiektami typu \"wydrążony\" prostopadłościan o stałej grubości i kątach 90° między ścianami.
-   Zobacz stronę [Wykonaj podcięcie](SheetMetal_AddRelief/pl#Uwagi.md) aby znaleźć wskazówki dotyczące tworzenia obiektów powłokowych prostopadłościanów.

-   **Junction** w tym przypadku nie jest wynikiem działania tego narzędzia, który jest przerwą między przylegającymi płaskimi ścianami, tylko opisuje położenie, w którym dwie płaskie ściany ukończonego rzeczywistego obiektu się spotykają, np. w celu ich zespawania.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Połaczenie środowiska Arkusz Blachy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) lub, jeśli jest w obrębie [Zawartości środowiska Projekt Części](PartDesign_Body/pl.md), z obiektu [Cechy tego środowiska](PartDesign_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Parametry}}

-    **Obiekt bazowy|LinkSub**: *Obiekt bazowy*. Łącza do krawędzi definiujących pozycje odstępów / połączeń.

-    **Szczelina|Length**: *Szczelina połączenia*. Domyślnie: {{value|2,00 mm}}. Rozmiar dodawanej szczeliny / połączenia.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal AddJunction/pl
