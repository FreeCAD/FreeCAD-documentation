# Path ToolBit/pl
}





{{TOCright}}

## Opis

Końcówki narzędzia są podstawą systemu [narzędzi](Path_Tools/pl.md) środowiska Path. Reprezentują one konkretne narzędzie, które może być użyte w zadaniu do wygenerowania ścieżki narzędzia. Każdy zestaw końcówek narzędzi jest przechowywany jako plik JSON. Struktura pliku JSON to uporządkowane dane, które mogą być łatwo przetwarzane przez makrodefinicje lub skrypty środowiska Python, ale pozostają czytelne dla człowieka. Opisywanie zestawów narzędzi za pomocą JSON pozwala na automatyczne tworzenie dużych zbiorów dokładnych zestawów narzędzi automatycznie lub za pomocą skryptu.

Przechowywanie narzędzia jako pliku JSON brzmi świetnie, ale eliminuje możliwość uzyskania dokładnej miniatury lub reprezentacji bryły. Z drugiej strony, gdyby każdy zestaw narzędzi był tworzony jako obiekt FreeCAD, uzyskanie bryły byłoby proste, ale wymagałoby ogromnej pamięci masowej w przypadku dużych kolekcji narzędzi. Również automatyczne tworzenie zestawów narzędzi jako obiektów FreeCAD byłoby trudne lub niemożliwe.

Zamiast tego narzędzia są mieszane. Plik JSON zawiera ścieżkę do pliku profilu narzędzia oraz wartości wszystkich parametrów wymaganych do utworzenia określonego zestawu narzędzi.

Gdy narzędzie jest uruchamiane w zadaniu, obiekt jest tworzony na podstawie szablonu, a ograniczenia są ustawiane zgodnie z wartościami z pliku JSON. Wszystkie dodatkowe parametry są tworzone jako właściwości obiektu. Dzięki temu uzyskuje się prawidłowy kształt i wymiary, które można wykorzystać do wygenerowania chmury punktów lub siatki na potrzeby zaawansowanych algorytmów *(i potencjalnie symulacji)*.

## Użycie

W interfejsie graficznym programu FreeCAD menedżer biblioteki narzędziowej Path udostępnia mechanizm tworzenia nowego zestawu narzędzi. Pojedynczy zestaw narzędzi może znajdować się w wielu bibliotekach narzędzi.

1.  Otwórz menedżera narzędzi Path.
2.  Wybierz bibliotekę.
3.  Utwórz narzędzie.

## Struktura JSON 


{{Code|
{
  "version"   * 2,
  "name"   * "T1",
  "shape"   * "endmill.fcstd",
  "attribute"   * {},
  "parameter"   * {
    "CuttingEdgeHeight"   * "30.000 mm",
    "Diameter"   * "1.000 mm",
    "Length"   * "50.000 mm",
    "ShankDiameter"   * "3.000 mm"
  }
}
}}

## Opcje

## Powiązane

-   [Narzędzia](Path_Tools/pl.md)
-   [Otwarta biblioteka narzędzi](Path_ToolBitLibraryOpen/pl.md)





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path ToolBit/pl
