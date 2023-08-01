---
- GuiCommand:
   Name: Std HideSelection
   Name/pl: Std: Ukryj zaznaczone
   MenuLocation: Widok - Widoczność - Ukryj zaznaczone
   Workbenches: wszystkie
   SeeAlso: [Przełącz widoczność](Std_ToggleVisibility/pl.md), [Pokaż zaznaczone](Std_ShowSelection/pl.md), [Przełącz widoczność wszystkich](Std_ToggleObjects/pl.md), [Wyświetl wszystkie obiekty](Std_ShowObjects/pl.md), [Ukryj wszystkie obiekty](Std_HideObjects/pl.md)
---

# Std HideSelection/pl

## Opis

Polecenie **Ukryj zaznaczone** ukrywa widoczność wybranych obiektów w oknie [widoku 3D](3D_view/pl.md).

## Użycie

1.  Wybierz jeden lub więcej obiektów.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Wybierz z menu opcję **Widok → Widoczność → <img src="images/Std_HideSelection.svg" width=16px> Ukryj zaznaczone**.
    -   Wybierz opcję z menu kontekstowego **<img src="images/Std_HideSelection.svg" width=16px> Ukryj zaznaczone** [Widoku drzewa](Tree_view/pl.md). Opcja ta nie jest dostępna w środowisku pracy [Projekt Części](PartDesign_Workbench/pl.md).

## Uwagi

-   Niewidoczne obiekty są wyświetlane z wyszarzoną etykietą i wyszarzoną ikoną w oknie [Widoku drzewa](Tree_view/pl.md).
-   Obiekty zagnieżdżone w [Części](Std_Part/pl.md), lub [obiekcie połączonym](Std_LinkMake/pl.md) do [Grupy](Std_Group/pl.md), lub Grupy linków, oraz [cech](PartDesign_Feature/pl.md) w [Zawartości Projektu Części](PartDesign_Body/pl.md) będą widoczne w oknie [Widoku 3D](3D_view/pl.md) tylko wtedy, gdy ich obiekt nadrzędny jest również widoczny. Oznacza to, że element w Zawartości Projektu Części, który jest zagnieżdżony w obiekcie Część będzie widoczny w oknie widoku 3D tylko wtedy, gdy sam element, Zawartości Projektu Części i Część są widoczne. A jeśli obiekt Część jest z kolei zagnieżdżony w innej obiekcie Część, to ten ostatni obiekt musi być również widoczny.
-   Jeśli widoczność [Grupy](Std_Group/pl.md) *(lub obiektu pochodnego, takiego jak [Część budowli](Arch_BuildingPart/pl.md) środowiska Architektura)* zostanie zmieniona, widoczność jej zagnieżdżonych obiektów zmieni się odpowiednio. Ale ich widoczność może być również zmieniana indywidualnie.
-   Działanie tego polecenia nie może być cofnięte za pomocą przycisku [Cofnij](Std_Undo/pl.md).
-   Widoczność obiektu można również zmienić poprzez jego powiązaną właściwość **Widoczność** w [Edytorze właściwości](Property_editor/pl.md) lub oknie [Widok połączonego](Combo_view/pl.md).

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zapoznać się z przykładami skryptów zobacz stronę [Przełącz widoczność](Std_ToggleVisibility/pl.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std HideSelection/pl
