---
 GuiCommand:
   Name: SheetMetal AddBend
   Name/pl:  Arkusz Blachy: Wykonaj zagięcie
   MenuLocation: SheetMetal , Wykonaj zagięcie
   Workbenches: SheetMetal_Workbench/pl
   Shortcut: **S** **B**
   SeeAlso: SheetMetal_AddRelief/pl, SheetMetal_AddJunction/pl
---

# SheetMetal AddBend/pl



## Opis

Polecenie <img alt="" src=images/SheetMetal_AddBend.svg  style="width:24px;"> **Wykonaj zagięcie** zastępuje ostre krawędzie między dwiema sekcjami *(płyta bazowa / ściany / kołnierze)* obiektu z blachy na zaokrąglone zagięcia. Bez tych zagięć obiektu nie da się rozłożyć.

To polecenie jest trzecim z trzech kroków konwersji obiektu powłoki wykonanego za pomocą środowiska pracy [Część](Part_Workbench/pl.md) lub [Projekt Części](PartDesign_Workbench/pl.md) na rozkładany obiekt z blachy:

1.  [Wykonaj podcięcie](SheetMetal_AddRelief/pl.md)
2.  [Wykonaj połączenie](SheetMetal_AddJunction/pl.md)
3.  [Wykonaj zagięcie](SheetMetal_AddBend/pl.md)

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:200px;"> 
*Wykonaj zagięcie - zastąp krawędzie zagięciami*



## Użycie

1.  Wybierz jedną lub więcej krawędzi.
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Wciśnij przycisk **<img src="images/SheetMetal_AddBend.svg" width=16px> [Wykonaj zagięcie](SheetMetal_AddBend/pl.md)**.
    -   Wybierz opcję **SheetMetal → <img src="images/SheetMetal_AddBend.svg" width=16px> Wykonaj zagięcie** z menu.
    -   Kliknij prawym przyciskiem myszy w [widoku drzewa](Tree_view/pl.md) lub [widoku 3D](3D_view/pl.md) i wybierz opcję **SheetMetal → <img src="images/SheetMetal_AddBend.svg" width=16px> Wykonaj zagięcie** z menu kontekstowego.
    -   Użyj skrótu klawiaturowego: **S** + **B**.
3.  Otwarty zostanie [panel zadań](Task_panel/pl.md) **Bend sharp corner Parameters** (wprowadzony w wersji 0.5.00).
4.  Opcjonalnie wciśnij przycisk **Wybierz** aby dodać więcej ścian.
    -   Wciśnij przycisk **Podgląd** aby zakończyć wybór i wyświetlić zmiany.
5.  Opcjonalnie dostosuj parametry w panelu zadań.
6.  Wciśnij przycisk **OK** aby zakończyć polecenie i zamknąć panel zadań.
7.  Utworzony zostanie obiekt **SolidBend** składający się z jednego nowego zagięcia dla każdej wskazanej krawędzi.
8.  Opcjonalnie dostosuj parametry w [Edytorze właściwości](Property_editor/pl.md).

<img alt="" src=images/SheetMetal_ConvertShellObject-07.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-08.png  style="width:200px;">



## Uwagi

Polecenia <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[Wykonaj podcięcie](SheetMetal_AddRelief/pl.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[Wykonaj połączenie](SheetMetal_AddJunction/pl.md)** i <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[Wykonaj zagięcie](SheetMetal_AddBend/pl.md)** działają najlepiej z obiektami typu \"wydrążony\" prostopadłościan o stałej grubości i kątach 90° między ścianami.

Zobacz stronę z opisem narzędzia [Wykonaj podcięcie](SheetMetal_AddRelief/pl#Uwagi.md), aby uzyskać wskazówki dotyczące tworzenia obiektów powłoki na bazie prostopadłościanów.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Bryła Zagięcia środowiska Arkusz Blachy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) lub, jeśli jest w obrębie [Zawartości środowiska Projekt Części](PartDesign_Body/pl.md), z obiektu [Cechy tego środowiska](PartDesign_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada również następujące dodatkowe właściwości, a jego etykieta ma wartość domyślną:



### Dane


{{Properties_Title|Parametry}}

-    **Obiekt bazowy|LinkSub**: \"Obiekt bazowy\". Łącza do krawędzi, które mają zostać wygięte.

-    **Promień|Length**: \"Promień zagięcia\". Wartość domyślna: {{value|1,00 mm}}.

-    **Grubość|Length**: \"Grubość blachy\". Wartość domyślna: {{value|1,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal AddBend/pl
