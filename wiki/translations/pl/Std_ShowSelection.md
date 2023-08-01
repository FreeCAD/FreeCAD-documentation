---
- GuiCommand:/pl
   Name:Std ShowSelection
   Name/pl:Std: Pokaż zaznaczone
   MenuLocation:Widok → Widoczność → Pokaż zaznaczone
   Workbenches:wszystkie
   SeeAlso:[Przełącz widoczność](Std_ToggleVisibility/pl.md), [Ukryj zaznaczone](Std_HideSelection/pl.md), [Przełącz widoczność wszystkich](Std_ToggleObjects/pl.md), [Wyświetl wszystkie obiekty](Std_ShowObjects/pl.md), [Ukryj wszystkie obiekty](Std_HideObjects/pl.md)
---

# Std ShowSelection/pl

## Opis

Polecenie **Pokaż zaznaczone** pokazuje wybrane obiekty w oknie [widoku 3D](3D_view/pl.md).

## Użycie

1.  Wybierz jeden lub więcej obiektów.
    -   Niewidoczne obiekty mogą być zaznaczone w oknie [Widoku drzewa](Tree_view/pl.md).
    -   Bądź ostrożny, gdy używasz skrótu **Ctrl** + **A**, aby wybrać wszystkie obiekty w widoku Drzewa. Spowoduje to również zaznaczenie elementów podrzędnych [Zawartości Projektu Części](PartDesign_Body/pl.md) i obiektów używanych dla [funkcji logicznych](Part_Boolean/pl.md) środowiska Część. W większości przypadków powinny one pozostać niewidoczne.
    -   Obiekty użyte dla [funkcji logicznych](Part_Boolean.md) środowiska Część zostaną również wybrane, gdy użyjesz skrótu **Ctrl** + **A** w oknie widoku 3D.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Wybierz z menu opcję **Widok → Widoczność → <img src="images/Std_ShowSelection.svg" width=16px> Pokaż zaznaczone**.
    -   Wybierz z menu kontekstowego widoku drzewa opcję **<img src="images/Std_ShowSelection.svg" width=16px> Pokaż zaznaczone** . Opcja ta nie jest dostępna w środowisku [Projekt Części](PartDesign_Workbench/pl.md).

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
![](images/Button_right.svg) [documentation index](../README.md) > Std ShowSelection/pl
