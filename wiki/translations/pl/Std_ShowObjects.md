---
- GuiCommand:/pl
   Name:Std ShowObjects
   Name/pl:Std: Wyświetl wszystkie obiekty
   MenuLocation:Widok → Widoczność → Wyświetl wszystkie obiekty
   Workbenches:wszystkie
   SeeAlso:[Przełącz widoczność](Std_ToggleVisibility/pl.md), [Pokaż zaznaczone](Std_ShowSelection/pl.md), [Ukryj zaznaczone](Std_HideSelection.md), [Przełącz widoczność wszystkich obiektów](Std_ToggleObjects/pl.md), [Ukryj wszystkie obiekty](Std_HideObjects/pl.md)
---

# Std ShowObjects/pl

## Opis

Polecenie **Wyświetl wszystkie obiekty** powoduje wyświetlenie wszystkich obiektów należących do aktywnego dokumentu w oknie [widoku 3D](3D_view.md). Uważaj, gdy używasz tego polecenia, ponieważ pokaże ono również elementy podrzędne [Zawartości](PartDesign_Body/pl.md) środowiska Projekt Części oraz obiekty używane dla [funkcji logicznych](Part_Boolean/pl.md) środowiska Część. W większości przypadków powinny one pozostać niewidoczne.

## Użycie

1.  Wybierz z menu opcję **Widok → Widoczność → <img src="images/Std_ShowObjects.svg" width=16px> Wyświetl wszystkie obiekty**.

## Uwagi

-   Działanie tego polecenia nie może być cofnięte za pomocą przycisku [Cofnij](Std_Undo/pl.md).
-   Widoczność obiektu można również zmienić poprzez jego powiązaną właściwość **Widoczność** w [Edytorze właściwości](Property_editor/pl.md) lub oknie [Widoku połączonego](Combo_view/pl.md).

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zapoznać się z przykładami skryptów zobacz stronę [Przełącz widoczność](Std_ToggleVisibility/pl.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ShowObjects/pl
