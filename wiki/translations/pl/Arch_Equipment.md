---
 GuiCommand:
   Name: Arch Equipment
   Name/pl: BIM: Wyposażenie
   MenuLocation: 3D / BIM , Wyposażenie
   Workbenches: BIM_Workbench/pl
   Shortcut: **E** **Q**
   SeeAlso: 
---

# Arch Equipment/pl



## Opis

Narzędzie **Wyposażenie** oferuje prosty i wygodny sposób wstawiania do projektów niekonstrukcyjnych, samodzielnych elementów, takich jak meble, sprzęt hydro-sanitarny lub urządzenia elektryczne. Elementy wyposażenia są oparte na [kształcie części](Part_Workbench/pl.md), co pozwala im korzystać z solidności i możliwości geometrii BRep, a także generować ładne widoki podczas renderowania do widoków planu i przekroju.

<img alt="" src=images/Arch_equipment_example.jpg  style="width:600px;"> 
*Obiekty meblowe zamknięte w obiekcie '''Wyposażenie'''. Rzuty płaskie można uzyskać za pomocą narzędzia [Widok 2D kształtu](Draft_Shape2DView/pl.md).*

Od wersji 0.17 obiekty wyposażenia mają również właściwość **HiRes**, do której można dołączyć obiekt [siatki](Mesh_Workbench/pl.md). Obiekty wyposażenia mogą być następnie wyświetlane w widoku 3D zamiast ich kształtu, co pozwala na użycie dowolnych obiektów siatkowych o wysokiej rozdzielczości, takich jak szczegółowe meble powszechnie spotykane na stronach internetowych.

<img alt="" src=images/Arch_equipment_mesh.jpg  style="width:600px;"> 
*Obiekty meblowe zamknięte w obiekcie '''Wyposażenie''' z dołączoną siatką o wysokiej rozdzielczości.*

Podczas korzystania z eksportera OBJ wszystkie obiekty wyposażenia, które są w trybie wyświetlania siatki, zostaną wyeksportowane jako ich siatka zamiast kształtu.



## Użycie

1.  Wybierz kształt [części](Part_Workbench/pl.md) i opcjonalnie obiekt [siatki](Mesh_Workbench/pl.md).
2.  Naciśnij przycisk **<img src="images/Arch_Equipment.svg" width=16px> '''Wyposażenie'''** lub naciśnij klawisze **E**, a następnie **Q**.



## Opcje

-   Obiekty Wyposażenie dzielą wspólne właściwości i zachowania wszystkich [komponentów](Arch_Component/pl.md).



## Właściwości

-    **Model**: Opis modelu tego urządzenia.

-    **Url**: Adres URL strony produktu, na której można znaleźć więcej informacji o tym urządzeniu.

-    **Siatka**: Reprezentacja [siatki](Mesh_Workbench/pl.md) do użycia dla tego sprzętu. Po ustawieniu dostępny staje się tryb wyświetlania **Siatka**.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wyposażenie** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji: 
```python
Equipment = makeEquipment(baseobj=None, placement=None, name="Equipment")
```

-   Tworzy obiekt `Equipment` z podanego `baseobj`, który może być `Part` lub `Mesh`.
-   Jeśli podano `placement`, jest on używany.
-   Zwraca `None` jeśli operacja się nie powiedzie.

Przykład: 
```python
import FreeCAD, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 500
Box.Width = 2000
Box.Height = 600

Equip = Arch.makeEquipment(Box)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Equipment/pl
