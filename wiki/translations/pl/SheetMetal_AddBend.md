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
2.  Aktywuj polecenie <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **Wykonaj zagięcie** używając jednej z poniższych opcji:
    -   Przycisk **<img src="images/SheetMetal_AddBend.svg" width=16px> Wykonaj zagięcie**.
    -   Opcja menu **SheetMetal → <img src="images/SheetMetal_AddBend.svg" width=16px> Wykonaj zagięcie**.
    -   Skrót klawiaturowy: **S** + **B**.

<img alt="" src=images/SheetMetal_ConvertShellObject-07.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-08.png  style="width:200px;">



## Uwagi

Polecenia <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[Wykonaj podcięcie](SheetMetal_AddRelief/pl.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[Wykonaj połączenie](SheetMetal_AddJunction/pl.md)** i <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[Wykonaj zagięcie](SheetMetal_AddBend/pl.md)** działają najlepiej z obiektami typu \"wydrążony\" prostopadłościan o stałej grubości i kątach 90° między ścianami.

Zobacz stronę z opisem narzędzia [Wykonaj podcięcie](SheetMetal_AddRelief/pl#Uwagi.md), aby uzyskać wskazówki dotyczące tworzenia obiektów powłoki na bazie prostopadłościanów.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Bryła Zagięcia środowiska Arkusz Blachy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada również następujące dodatkowe właściwości, a jego etykieta ma wartość domyślną:



### Dane


{{Properties_Title|Podstawowe}}

-    **Etykieta|String**: Wartość domyślna: {{value|SolidBend}} *(+ kolejny numer dla drugiej i następnych pozycji)*.

Edytowalna przez użytkownika nazwa tego obiektu, może to być dowolny ciąg znaków UTF8.

-    **Cecha podstawowa|Link|ukryte**: Cecha bazowa. Link do cechy nadrzędnej.

-    **_Body|LinkHidden|ukryte**: Link ukryty do zawartości nadrzędnej.


{{Properties_Title|Parametry}}

-    **Obiekt bazowy|LinkSub**: \"Obiekt bazowy\". Łącza do krawędzi, które mają zostać wygięte.

-    **Promień|Length**: \"Promień zagięcia\". Wartość domyślna: {{value|1,00 mm}}.

-    **Grubość|Length**: \"Grubość blachy\". Wartość domyślna: {{value|1,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddBend/pl
