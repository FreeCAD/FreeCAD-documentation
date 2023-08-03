---
 GuiCommand:
   Name: Std ToggleVisibility
   Name/pl: Std: Przełącz widoczność
   MenuLocation: Widok , Przełącz widoczność
   Workbenches: wszystkie
   Shortcut: **Spacja**
   SeeAlso: Std_ShowSelection/pl, Std_HideSelection/pl, Std_ToggleObjects/pl, Std_ShowObjects/pl, Std_HideObjects/pl
---

# Std ToggleVisibility/pl

## Opis

Polecenie **Przełącz widoczność** przełącza widoczność wybranych obiektów w oknie [widoku 3D](3D_view/pl.md).

## Użycie

1.  Wybierz jeden lub więcej obiektów.
    -   Niewidoczne obiekty mogą być zaznaczone w oknie [Widoku drzewa](Tree_view/pl.md).
    -   Bądź ostrożny, gdy używasz kombinacji klawiszy **Ctrl** + **A**, aby wybrać wszystkie obiekty w oknie Widoku drzewa. Spowoduje to również zaznaczenie elementów podrzędnych [Zawartości](PartDesign_Body/pl.md) środowiska Projekt Części i obiektów używanych dla [funkcji logicznych](Part_Boolean/pl.md) środowiska Część. W większości przypadków powinny one pozostać niewidoczne.
    -   Obiekty używane dla [funkcji logicznych](Part_Boolean/pl.md) środowiska Część są również wybierane, gdy używasz kombinacji klawiszy **Ctrl** + **A** w oknie widoku 3D.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Wybierz opcję z menu **Widok → <img src="images/Std_ToggleVisibility.svg" width=16px> Przełącz widoczność**.
    -   Wybierz opcję z menu **Widok → Widoczność → <img src="images/Std_ToggleVisibility.svg" width=16px> Przełącz widoczność**.
    -   Wybierz opcję **<img src="images/Std_ToggleVisibility.svg" width=16px> Przełącz widoczność** z menu kontekstowego okna widoku drzewa. Opcja ta nie jest dostępna w środowisku pracy [Projekt części](PartDesign_Workbench.md)
    -   Wybierz opcję **<img src="images/Std_ToggleVisibility.svg" width=16px> Przełącz widoczność** z menu kontekstowego okna widoku 3D.
    -   Użyj skrótu klawiaturowego: **Spacja**.

## Uwagi

-   Niewidoczne obiekty są wyświetlane z wyszarzoną etykietą i wyszarzoną ikoną w oknie [Widoku drzewa](Tree_view/pl.md).
-   Obiekty zagnieżdżone w [Części](Std_Part/pl.md), lub [obiekcie połączonym](Std_LinkMake/pl.md) do [Grupy](Std_Group/pl.md), lub Grupy linków, oraz [cech](PartDesign_Feature/pl.md) w [Zawartości Projektu Części](PartDesign_Body/pl.md) będą widoczne w oknie [Widoku 3D](3D_view/pl.md) tylko wtedy, gdy ich obiekt nadrzędny jest również widoczny. Oznacza to, że element w Zawartości Projektu Części, który jest zagnieżdżony w obiekcie Część będzie widoczny w oknie widoku 3D tylko wtedy, gdy sam element, Zawartości Projektu Części i Część są widoczne. A jeśli obiekt Część jest z kolei zagnieżdżony w innej obiekcie Część, to ten ostatni obiekt musi być również widoczny.
-   Jeśli widoczność [Grupy](Std_Group/pl.md) *(lub obiektu pochodnego, takiego jak [Część budowli](Arch_BuildingPart/pl.md) środowiska Architektura)* zostanie zmieniona, widoczność jej zagnieżdżonych obiektów zmieni się odpowiednio. Ale ich widoczność może być również zmieniana indywidualnie.
-   Działanie tego polecenia nie może być cofnięte za pomocą przycisku [Cofnij](Std_Undo/pl.md).
-   Widoczność obiektu można również zmienić poprzez jego powiązaną właściwość **Widoczność** w [Edytorze właściwości](Property_editor/pl.md) lub oknie [Widok połączonego](Combo_view/pl.md).

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Użyj metod obiektu `show` i `hide`, aby zmienić jego widoczność.


```python
import FreeCADGui

obj = FreeCADGui.ActiveDocument.myObjectName

if obj.Visibility == True:
  obj.hide()
else:
  obj.show()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ToggleVisibility/pl
