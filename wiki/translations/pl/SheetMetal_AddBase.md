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
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Wciśnij przycisk **<img src="images/SheetMetal_AddBase.svg" width=16px> [Dodaj element bazowy](SheetMetal_AddBase/pl.md)** na pasku narzędzi.
    -   Wybierz opcję **Arkusz Blachy → <img src="images/SheetMetal_AddBase.svg" width=16px> Dodaj element bazowy** z menu.
    -   Kliknij prawym przyciskiem myszy w [widoku drzewa](Tree_view/pl.md) lub [widoku 3D](3D_view/pl.md) i wybierz opcję **Arkusz Blachy → <img src="images/SheetMetal_AddBase.svg" width=16px> Dodaj element bazowy** z menu kontekstowego.
    -   Użyj skrótu klawiszowego: **C** a następnie **B**.
3.  Utworzony zostanie obiekt **BaseBend**, narożniki wzdłuż konturu będą automatycznie przekształcone w zagięcia cylindryczne.
4.  Dostosuj parametry profilu w [Edytorze właściwości](Property_editor/pl.md):
    -   
        **Długość**
        
        do długości wyciągnięcia profilu,

    -   
        **Grubość**
        
        do grubości ściany profilu,

    -   
        **Promień**
        
        do wewnętrznego promienia automatycznie dodanych zagięć.



### Płyta

1.  Wybierz <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [szkic](Sketcher_Workbench/pl.md) *zamkniętego konturu*.<img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [sketch](Sketcher_Workbench.md).
2.  Aktywuj polecenie jak opisano wyżej.
3.  Dostosuj parametry płyty w [Edytorze właściwości](Property_editor/pl.md):
    -   
        **Grubość**
        
        dla grubości płyty.

:   

    :   (**Długość** oraz **Promień** są nieużywane dla płyt.)



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt bazowy wygięcia środowiska Arkusz Blachy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) lub, jeśli jest w obrębie [Zawartości środowiska Projekt Części](PartDesign_Body/pl.md), z obiektu [Cechy tego środowiska](PartDesign_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Parametry}}

-    **Strona wygięcia|Enumeration**: \"Typ wpustu\", definiuje do której strony krzywej profilu ma zastosowanie grubość. {{value|Na zewnątrz}} *(domyślnie)*, {{value|Do wewnątrz}}, {{value|Pośrodku}}. (nieużywane dla płyt)

-    **Szkic wygięcia|Link**: \"Obiekt szkicu ściany\". Link do profilu / szkicu konturu.

-    **Płaszczyzna środkowa|Bool**: \"Wyciągnięcie symetrycznie do płaszczyzny\". Długość profilu lub grubość płyty dochodzi do jednej strony płaszczyzny szkicu jeśli {{FALSE/pl}} (domyślne) lub symetrycznie do obu stron jeśli {{TRUE/pl}}.

-    **Odwrócony|Bool**: Odwraca kierunek wyciągnięcia profilu lub grubości płyty. Domyślnie: {{FALSE/pl}}.

-    **Długość|Length**: Długość wyciągnięcia profilu. Domyślnie: {{value|100,00 mm}}. (nieużywane dla płyt)

-    **Promień|Length**: Wewnętrzny promień automatycznie dodawanych zagięć. Domyślnie: {{value|1,00 mm}}. (nieużywane dla płyt)

-    **Grubość|Length**: Grubość ściany profilu lub płyty. Domyślnie: {{value|1,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddBase/pl
