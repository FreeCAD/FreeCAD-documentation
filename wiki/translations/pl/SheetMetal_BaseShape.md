---
 GuiCommand:
   Name: SheetMetal BaseShape
   Name/pl: Arkusz blachy: Dodaj kształt bazowy
   MenuLocation: Arkusz blachy , Dodaj kształt bazowy
   Workbenches: SheetMetal_Workbench/pl
   Version: 0.3.10
   Shortcut: **H**
---

# SheetMetal BaseShape/pl



## Opis

Polecenie <img alt="" src=images/SheetMetal_BaseShape.svg  style="width:24px;"> **Dodaj kształt Bazowy** tworzy parametryczny obiekt Kształt Bazowy Arkusza Blachy.

<img alt="" src=images/SheetMetal_BaseShape-01.png  style="width:400px;">



*Pięć dostępnych kształtów bazowych: Kształt L, Kształt U, Kształt wanny, Kształt kapelusza i Kształt prostopadłościanu*

Prostokątny szósty kształt o nazwie Flat został wprowadzony w wersji 0.4.10.



## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Wciśnij przycisk **<img src="images/SheetMetal_BaseShape.svg" width=16px> '''Dodaj kształt bazowy'''**.
    -   Wybierz opcję **Arkusz blachy → <img src="images/SheetMetal_BaseShape.svg" width=16px> Dodaj kształt bazowy** z menu.
    -   Kliknij prawym przyciskiem myszy w [widoku drzewa](Tree_view/pl.md) lub [widoku 3D](3D_view/pl.md) i wybierz opcję **SheetMetal → <img src="images/SheetMetal_BaseShape.svg" width=16px> Dodaj kształt bazowy** z menu kontekstowego.
    -   Użyj skrótu klawiaturowego: **H**.
2.  Otworzy się [panel zadań](Task_panel/pl.md) **Generuj kształt bazowy blachy**.
3.  Wybierz żądany kształt z opcji **Typ kształtu bazowego**.
4.  Wybierz położenie początkowe w widżecie **Lokalizacja punktu bazowego części**.
5.  Opcjonalnie dostosuj parametry w panelu zadań.
6.  Wciśnij przycisk **OK** aby zakończyć polecenie i zamknąć panel zadań.
7.  Utworzony zostanie obiekt **BaseShape**.
8.  Opcjonalnie dostosuj parametry w [Edytorze właściwości](Property_editor/pl.md).



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt **Kształt bazowy** środowiska Arkusz Blachy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) lub, jeśli jest w obrębie [Zawartości środowiska Projekt Części](PartDesign_Body/pl.md), z obiektu [Cechy tego środowiska](PartDesign_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Parametry}}

-    **Wypełnij szczeliny|Bool**: Rozszerza boki i kołnierze, aby zamknąć wszystkie szczeliny. Domyślnie: {{TRUE/pl}}.

-    **szerokośćKołnierza|Length**: Szerokość górnego kołnierza. Wartość domyślna: {{Value|5,00 mm}}.

-    **wysokość|Length**: Wysokość kształtu. Wartość domyślna: {{Value|10,00 mm}}.

-    **długość|Length**: Długość kształtu. Wartość domyślna: {{Value|30,00 mm}}.

-    **origin Loc|Enumeration**: Lokalizacja punktu odniesienie położenia.

    :   
        {{Value|-X,-Y}}
        
        , {{Value|-X,0}}, {{Value|-X,+Y}}, {{Value|0,-Y}}, {{Value|0,0}} *(domyślnie)*, {{Value|0,+Y}}, {{Value|+X,-Y}}, {{Value|+X,0}} i {{Value|+X,+Y}}.

-    **promień|Length**: Promień zgięcia. Wartość domyślna: {{Value|1,00 mm}}.

-    **Typ kształtu|Enumeration**: Typ kształtu bazowego.

    :   
        {{Value|Flat}}
        
        *(wprowadzona w wersji 0.4.10)*, {{Value|L-Shape}} (domyślnie), {{Value|U-Shape}}, {{Value|Tub}}, {{Value|Hat}} i {{Value|Box}}.

-    **grubość|Length**: Grubość blachy. Wartość domyślna: {{Value|1,00 mm}}.

-    **width|Length**: Szerokość kształtu. Wartość domyślna: {{Value|20,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal BaseShape/pl
