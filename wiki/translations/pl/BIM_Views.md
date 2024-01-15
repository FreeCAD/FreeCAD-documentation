---
 GuiCommand:Addon/pl
   Name: BIM Views
   Name/pl: BIM: Widoki
   Workbenches: Image:IFC.svg BIM Workbench/pl
   Addon: BIM
   MenuLocation: Zarządzaj , Widoki
---

# BIM Views/pl



## Opis

Menedżer widoków i poziomów BIM to dokowane okno, które otwiera się poniżej normalnego widoku drzewa i zawiera wszystkie [części budowli](Arch_BuildingPart/pl.md) i [pośrednie płaszczyzny robocze](Draft_WorkingPlaneProxy/pl.md) modelu.

Celem tego okna jest umożliwienie szybkiego dostępu do poziomów i konfiguracji płaszczyzny roboczej, bez konieczności nawigowania po drzewie w celu ich znalezienia.

<img alt="" src=images/BIM_views_screenshot.png  style="width:800px;">



## Użycie

Menedżer widoków BIM pokaże wszystkie poziomy *(części budynku)* i pośrednie płaszczyzny robocze dokumentu. Można go zadokować w dowolnym miejscu interfejsu FreeCAD lub pozostawić w samodzielnym oknie. Części budynku pokażą również swój poziom *(współrzędną Z ich położenia)*.

-   Naciśnięcie kombinacji klawiszy **Ctrl** + **9** lub kliknięcie przycisku **Widoki BIM** w prawym dolnym rogu ekranu powoduje wyświetlenie lub ukrycie menedżera widoków BIM.
-   Kliknięcie dowolnego wpisu powoduje wybranie odpowiedniego obiektu
-   Dwukrotne kliknięcie wysokości poziomu umożliwia jego edycję.
-   Dwukrotne kliknięcie nazwy dowolnego obiektu ustawia na nim płaszczyznę roboczą, a jeśli opcja **Przywróć widok** obiektu jest włączona i zapisano w nim konfigurację widoku, ten punkt widzenia jest również przywracany.
-   Kliknięcie przycisku **Dodaj nowy poziom** tworzy nowy [poziom](Arch_BuildingPart/pl.md).
-   Kliknięcie przycisku **Dodaj nową pośrednią płaszczyznę roboczą** tworzy nową [pośrednią płaszczyznę roboczą](Draft_WorkingPlaneProxy/pl.md).
-   Kliknięcie przycisku **Usuń** usuwa wybrany element.
-   Kliknięcie przycisku **Włącz / wyłącz** włącza/wyłącza wybrany poziom (tak samo jak Spacja)
-   Kliknięcie przycisku **Izoluj** wyłącza wszystkie poziomy z wyjątkiem wybranego.
-   Kliknięcie przycisku **Zapisz ujęcie widoku** zapisuje bieżące ustawienia widoku w wybranym obiekcie, umożliwiając ich przywrócenie, jeśli jego właściwość **Przywróć widok** jest ustawiona na wartość Prawda
-   Kliknięcie przycisku **Zmień nazwę** umożliwia zmianę nazwy wybranego obiektu.



---
⏵ [documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > BIM Views/pl
