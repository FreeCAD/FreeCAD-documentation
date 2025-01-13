---
 GuiCommand:Addon/pl
   Name: BIM Views
   Name/pl: BIM: Widoki
   MenuLocation: Zarządzaj , Widoki
   Workbenches: BIM_Workbench/pl
---

# BIM Views/pl



## Opis

**Menedżer widoków i poziomów BIM** to dokowalne okno, które otwiera się poniżej normalnego widoku drzewa i zawiera wszystkie [części budowli](Arch_BuildingPart/pl.md) i [pośrednie płaszczyzny robocze](Draft_WorkingPlaneProxy/pl.md) modelu.

Celem tego okna jest umożliwienie szybkiego dostępu do poziomów i konfiguracji płaszczyzny roboczej, bez konieczności nawigowania po drzewie w celu ich znalezienia.

<img alt="" src=images/BIM_views_screenshot.png  style="width:600px;"> 
*Menedżer widoków i poziomów BIM*



## Użycie

Menedżer widoków BIM pokaże wszystkie poziomy *(części budynku)* i pośrednie płaszczyzny robocze dokumentu. Można go zadokować w dowolnym miejscu interfejsu FreeCAD lub pozostawić w samodzielnym oknie. Części budynku pokażą również swój poziom *(współrzędną Z ich położenia)*.

-   Naciśnięcie kombinacji klawiszy **Ctrl** + **9** lub kliknięcie przycisku **Widoki BIM** na pasku statusu powoduje wyświetlenie lub ukrycie menedżera widoków BIM.

-   Kliknięcie dowolnego wpisu powoduje wybranie odpowiedniego obiektu

-   Dwukrotne kliknięcie wysokości poziomu umożliwia jego edycję.

-   Dwukrotne kliknięcie nazwy dowolnego obiektu ustawia na nim płaszczyznę roboczą, a jeśli właściwość **Przywróć widok** obiektu jest ustawiona na Prawda i zapisano w nim konfigurację widoku, ten punkt widzenia jest również przywracany.

-   Menedżer widoków BIM posiada menu kontekstowe dostępne po kliknięciu prawym przyciskiem myszy i zawierające poniższe opcje:
    -   
        **Dodaj poziom**
        
        tworzy nowy [poziom](Arch_BuildingPart/pl.md).

    -   
        **Dodaj nową pośrednią płaszczyznę roboczą**
        
        tworzy nową [pośrednią płaszczyznę roboczą](Draft_WorkingPlaneProxy/pl.md).

-    **Usuń**usuwa wybrany element.

-    **Włącz / wyłącz**włącza/wyłącza wybrany poziom (tak samo jak Spacja)

-    **Izoluj**wyłącza wszystkie poziomy z wyjątkiem wybranego.

-    **Zapisz ujęcie widoku**zapisuje bieżące ustawienia widoku w wybranym obiekcie, umożliwiając ich przywrócenie, jeśli jego właściwość **Przywróć widok** jest ustawiona na wartość Prawda

-    **Zmień nazwę**umożliwia zmianę nazwy wybranego obiektu.





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Views/pl
