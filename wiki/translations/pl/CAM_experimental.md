# CAM experimental/pl
## Opis

Środowisko pracy CAM zawiera zestaw ukrytych poleceń. Są one domyślnie ukryte, ponieważ są eksperymentalne. Polecenie może być uznane za eksperymentalne z jednego z następujących powodów:

-   Jest niekompletne.
-   Jest pełne błędów.
-   Jest niestabilne.
-   Nie tworzy poprawnych, stabilnych, bezpiecznych ścieżek.
-   Nie jest standardowym, regularnie używanym poleceniem w tradycyjnym obiegu CAM.
-   Jest dojrzałe, ale nie zostało jeszcze przeniesione na listę narzędzi standardowych.
-   \... inne powody.



## Wyłączenie poleceń eksperymentalnych 

Aby uzyskać dostęp do ukrytych poleceń eksperymentalnych środowiska pracy CAM, użytkownik musi je włączyć w [edytorze parametrów](Std_DlgParameter/pl.md).

1.  Otwórz [edytor parametrów](Std_DlgParameter/pl.md) za pomocą polecenia **Przybory → Edycja Parametrów ...**.
2.  Po wejściu do edytora ścieżka to **BaseApp → Preferences → Mod → CAM**.
3.  Aby włączyć polecenia [CAM: Obszar](CAM_Area/pl.md) i [CAM: Obszar płaszczyzny roboczej](CAM_Area_Workplane/pl.md):
    -   Kliknij prawym przyciskiem myszy w obszarze listy parametrów i wybierz z menu podręcznego pozycję **Nowy element z wartością logiczną**.
    -   Nadaj nazwę nowemu parametrowi: `EnableAdvancedOCLFeatures` *(z uwzględnieniem wielkości liter)*.
    -   Ustaw jego wartość na: `True`.
4.  Aby włączyć pozostałe polecenia eksperymentalne:
    -   Ponownie wybierz z menu podręcznego pozycję **Nowy element z wartością logiczną**.
    -   Nadaj nowemu parametrowi nazwę: `EnableExperimentalFeatures` *(z uwzględnieniem wielkości liter)*.
    -   Ustaw jego wartość na: `True`.
5.  Zapisz ustawienia.
6.  Uruchom ponownie program FreeCAD.



## Informacje dodatkowe 

Więcej informacji o konkretnych poleceniach eksperymentalnych można znaleźć na stronach [Wiki powiązanych z tematem](https://www.freecadweb.org/wiki/Special:WhatLinksHere/CAM_experimental).


 {{CAM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [CAM](CAM_Workbench.md) > CAM experimental/pl
