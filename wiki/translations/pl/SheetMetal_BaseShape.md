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



## Użycie

1.  Aktywuj polecenie <img alt="" src=images/SheetMetal_BaseShape.svg  style="width:16px;"> *\'Dodaj kształt bazowy* używając jednej z poniższych możliwości:
    -   Przycisk **<img src="images/SheetMetal_BaseShape.svg" width=16px> '''Dodaj kształt bazowy'''**.
    -   Opcja menu **Arkusz blachy → <img src="images/SheetMetal_BaseShape.svg" width=16px> Dodaj kształt bazowy**.
    -   Skrót klawiaturowy: **H**.
2.  Otworzy się panel zadań **Rozłóż obiekt z blachy**.
3.  Wybierz żądany kształt z opcji **Typ kształtu bazowego**.
4.  Dostosuj parametry.
5.  Naciśnij **OK**, aby zakończyć polecenie.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt **Kształt bazowy** środowiska Arkusz Blachy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **Etykieta|String**: Wartość domyślna: {{value|KształtBazowy}} *(+ kolejny numer dla drugiego i kolejnych elementów)*.
    Nazwa edytowalna przez użytkownika, może to być dowolny ciąg znaków UTF8.


{{Properties_Title|Parametry}}

-    **Wypełnij szczeliny|Bool**: Rozszerza boki i kołnierze, aby zamknąć wszystkie szczeliny. Domyślnie: {{TRUE/pl}}.

-    **szerokośćKołnierza|Length**: Szerokość górnego kołnierza. Wartość domyślna: {{Value|5,00 mm}}.

-    **wysokość|Length**: Wysokość kształtu. Wartość domyślna: {{Value|10,00 mm}}.

-    **długość|Length**: Długość kształtu. Wartość domyślna: {{Value|30,00 mm}}.

-    **promień|Length**: Promień zgięcia. Wartość domyślna: {{Value|1,00 mm}}.

-    **Typ kształtu|Enumeration**: Typ kształtu bazowego. {{Value|L-Shape}} (domyślnie), {{Value|U-Shape}}, {{Value|Tub}}, {{Value|Hat}}, {{Value|Box}}.

-    **grubość|Length**: Grubość blachy. Wartość domyślna: {{Value|1,00 mm}}.

-    **width|Length**: Szerokość kształtu. Wartość domyślna: {{Value|20,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal BaseShape/pl
