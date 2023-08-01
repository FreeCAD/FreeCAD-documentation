---
- GuiCommand:/pl
   Name:Std ToggleObjects
   Name/pl:Std: Przełącz widoczność
   MenuLocation:Widok → Widoczność → Przełącz widoczność wszystkich obiektów
   Workbenches:wszystkie
   SeeAlso:[Przełącz widoczność](Std_ToggleVisibility/pl.md), [Pokaż zaznaczone](Std_ShowSelection/pl.md), [Ukryj zaznaczone](Std_HideSelection.md), [Wyświetl wszystkie obiekty](Std_ShowObjects/pl.md), [Ukryj wszystkie obiekty](Std_HideObjects/pl.md)
---

# Std ToggleObjects/pl

## Opis

Polecenie **Przełącz widoczność** przełącza widoczność wszystkich obiektów należących do aktywnego dokumentu w oknie [widoku 3D](3D_view/pl.md). Uważaj, gdy używasz tego polecenia, ponieważ przełącza ono również widoczność elementów podrzędnych [Zawartości](PartDesign_Body/pl.md) w środowisku Projekt Części oraz obiektów używanych dla [funkcji logicznych](Part_Boolean/pl.md) środowiska Część. W większości przypadków powinny one pozostać niewidoczne.

## Użycie

1.  Wybierz opcję z menu **Widok → Widoczność → <img src="images/Std_ToggleObjects.svg" width=16px> Przełącz widoczność wszystkich obiektów
**

## Uwagi

-   Niewidoczne obiekty są wyświetlane z wyszarzoną etykietą i wyszarzoną ikoną w oknie [Widoku drzewa](Tree_view/pl.md).
-   Obiekty zagnieżdżone w [Części](Std_Part/pl.md), lub [obiekcie połączonym](Std_LinkMake/pl.md) do [Grupy](Std_Group/pl.md), lub Grupy linków, oraz [cech](PartDesign_Feature/pl.md) w [Zawartości Projektu Części](PartDesign_Body/pl.md) będą widoczne w oknie [Widoku 3D](3D_view/pl.md) tylko wtedy, gdy ich obiekt nadrzędny jest również widoczny. Oznacza to, że element w Zawartości Projektu Części, który jest zagnieżdżony w obiekcie Część będzie widoczny w oknie widoku 3D tylko wtedy, gdy sam element, Zawartości Projektu Części i Część są widoczne. A jeśli obiekt Część jest z kolei zagnieżdżony w innej obiekcie Część, to ten ostatni obiekt musi być również widoczny.
-   Jeśli widoczność [Grupy](Std_Group/pl.md) *(lub obiektu pochodnego, takiego jak [Część budowli](Arch_BuildingPart/pl.md) środowiska Architektura)* zostanie zmieniona, widoczność jej zagnieżdżonych obiektów zmieni się odpowiednio. Ale ich widoczność może być również zmieniana indywidualnie.
-   Działanie tego polecenia nie może być cofnięte za pomocą przycisku [Cofnij](Std_Undo/pl.md).
-   Widoczność obiektu można również zmienić poprzez jego powiązaną właściwość **Widoczność** w [Edytorze właściwości](Property_editor/pl.md) lub oknie [Widoku połączonego](Combo_view/pl.md).

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zapoznać się z przykładami skryptów zobacz stronę [Przełącz widoczność](Std_ToggleVisibility/pl.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ToggleObjects/pl
