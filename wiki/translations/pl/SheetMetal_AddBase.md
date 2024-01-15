---
 GuiCommand:
   Name: SheetMetal AddBase
   Name/pl: Arkusz Blachy: Utwórz element bazowy
   MenuLocation: SheetMetal , Utwórz element bazowy
   Workbenches: SheetMetal_Workbench/pl
   Shortcut: **C** **B**
---

# SheetMetal AddBase/pl



## Opis

<img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> **Utwórz element bazowy** tworzy obiekt bazowy środowiska pracy Arkusz Blachy ze szkicu profilu.

Z otwartego konturu tworzy przestrzenny *profil*:

<img alt="" src=images/SheetMetal_AddBase-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddBase-02.png  style="width:200px;">

Z zamkniętego konturu tworzy bazową *(pustą)* *płytę*:

<img alt="" src=images/SheetMetal_AddBase-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddBase-04.png  style="width:200px;">



## Użycie



### Profil

1.  Wybierz <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [szkic](Sketcher_Workbench/pl.md) *otwartego konturu*.
2.  Aktywuj polecenie <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Dodaj element bazowy](SheetMetal_AddBase/pl.md) za pomocą jednej z następujących możliwości:
    -   Przycisk **<img src="images/SheetMetal_AddBase.svg" width=16px> [Dodaj element bazowy](SheetMetal_AddBase/pl.md)** na pasku narzędzi.
    -   Opcja w menu **Arkusz Blachy → <img src="images/SheetMetal_AddBase.svg" width=16px> Dodaj element bazowy**.
    -   Skrót klawiaturowy: **C** następnie **B**.
3.  Dostosuj parametry profilu, edytując odpowiednie wartości w [Edytorze właściwości](Property_editor/pl.md):
    -   Właściwość **Długość** dla długości profilu,
    -   Właściwość **Grubość** dla grubości profilu,
    -   Właściwość **Promień** dla promienia wewnętrznego łuków.



### Płyta

1.  Wybierz <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [szkic](Sketcher_Workbench/pl.md) *zamkniętego konturu*.<img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [sketch](Sketcher_Workbench.md).
2.  Aktywuj polecenie <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Dodaj element bazowy](SheetMetal_AddBase/pl.md) *(patrz powyżej)*.
3.  Dostosuj parametry profilu, edytując odpowiednie wartości w [Edytorze właściwości](Property_editor/pl.md):
    -   Właściwość **Grubość** dla grubości płyty.

:   

    :   *(Właściwość **Długość** oraz **Promień** są nieużywane dla płyty.)*



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt bazowy wygięcia środowiska Arkusz Blachy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **Etykieta|String**: Wartość domyślna: {{value|WallForming}} *(+ kolejny numer dla drugiej i następnych pozycji)*.

Edytowalna przez użytkownika nazwa tego obiektu, może to być dowolny ciąg znaków UTF8.

-    **Cecha podstawowa|Link|ukryte**: Cecha bazowa. Link do cechy nadrzędnej.

-    **_Body|LinkHidden|ukryte**: Link ukryty do zawartości nadrzędnej.


{{Properties_Title|Parametry}}

-    **Strona wygięcia|Enumeration**: \"Typ wpustu\". {{value|Na zewnątrz}} *(domyślnie)*, {{value|Do wewnątrz}}, {{value|Pośrodku}}.

-    **Szkic wygięcia|Link**: \"Obiekt szkicu ściany\". Link do profilu / szkicu konturu.

-    **Płaszczyzna środkowa|Bool**: \"Wyciągnięcie symetrycznie do płaszczyzny\".   {{TRUE/pl}}, profil rozciąga się symetrycznie na obie strony płaszczyzny szkicu.

-    **Odwrócony|Bool**: \"Odwrotny kierunek wyciągnięcia\". Domyślnie: {{FALSE/pl}}.

-    **Długość|Length**: \"Długość ściany\". Domyślnie: {{value|100,00 mm}}.

-    **Promień|Length**: \"Promień wygięcia\". Domyślnie: {{value|1,00 mm}}.

-    **Grubość|Length**: \"Grubość arkusza blachy\". Domyślnie: {{value|1,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddBase/pl
