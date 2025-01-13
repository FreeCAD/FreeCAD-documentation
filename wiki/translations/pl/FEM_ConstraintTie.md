---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM ConstraintTie
   Name/pl: MES Wiązanie tie
   MenuLocation: Model , Warunki brzegowe i obciążenia mechaniczne , Wiązanie tie
   Workbenches: FEM_Workbench/pl
   Version: 0.19
   SeeAlso: FEM_ConstraintPressure/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: CalculiX
}}
---

# FEM ConstraintTie/pl



## Opis

Definiuje wiązanie tie łączące dwie wybrane powierzchnie w taki sposób, że (w przeciwieństwie do tego jak działa kontakt) nie mogą się rozdzielić ani ślizgać po sobie podczas analizy. Są więc trwale połączone.


{{Version/pl|1.0}}

: Może być również używany do definiowania symetrii cyklicznej.



## Użycie

1.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_ConstraintTie.svg" width=16px> [Wiązanie tie](FEM_ConstraintTie/pl.md)**.
    -   Wybierz opcję **Model → Warunki brzegowe i obciążenia mechaniczne → <img src="images/FEM_ConstraintTie.svg" width=16px> Wiązanie tie** z menu.

2.  Wciśnij przycisk **Dodaj** w panelu zadań a następnie kliknij na ścianie, którą chcesz dodać do definicji wiązania tie. Dokładnie dwie powierzchnie muszą być dodane, jedna po drugiej. Pierwsza wybrana ściana będzie ścianą podrzędną, podczas gdy druga będzie ścianą nadrzędną.

3.  Opcjonalnie, zdefiniuj Tolerancję - wiązanie Tie zostanie zastosowane tylko do węzłów powierzchni podrzędnej oddzielonych od powierzchni nadrzędnej odległością nie większą niż określona tutaj.

4.  
    {{Version/pl|1.0}}: Opcjonalnie zaznacz pole *Włącz dopasowanie*, aby umożliwić automatyczne przesuwanie węzłów powierzchni slave, aby leżały na powierzchni master, jeśli biorą udział w działaniu więzu *(tj. spełniają kryterium tolerancji)*.



## Symetria cykliczna 


{{Version/pl|1.0}}

: Wiązanie tie może być również wykorzystane do definiowania symetrii cyklicznej. Pozwala to na analizowanie modeli wykazujących obrotową periodyczność *(powtarzalne segmenty kołowe wokół osi symetrii)* przy pomocy pojedynczego reprezentatywnego sektora. Może to być szczególnie przydatne do symulacji wirników, wałów, turbin, łopatek wentylatorów, kół zamachowych i podobnych komponentów, często z użyciem [obciążenia siłą odśrodkową](FEM_ConstraintCentrif/pl.md) *(obciążenie musi również wykazywać tę formę symetrii)* .Symetrię cykliczną można zdefiniować wskazując dwie ściany w miejscach przecięcia przy definiowaniu wiązania tie i ustawiając następujące właściwości:

-    {{PropertyData/pl|Cyclic Symmetry}}: ustawienie na {{true/pl}} aktywuje symetrię cykliczną.

-    {{PropertyData/pl|Sectors}}: całkowita liczba sektorów, równa kątowi 360° podzielonemu przez kąt reprezentatywnego sektora *(np. 8 dla sektora 45° lub 6 dla sektora 60°)*.

-    {{PropertyData/pl|Connected Sectors}}: liczba sektorów wyświetlanych w wynikach, ustaw ją na taką samą wartość jak właściwość {{PropertyData/pl|Sectors}} jeśli chcesz zwizualizować całe 360° modelu.

-    {{PropertyData/pl|Symmetry Axis}}\- oś symetrii cyklicznej - domyślnie globalna oś Z, można ją przesunąć stosując transformację Umiejscowienia na wersorze Z *(podobnie do tego, co można zrobić z [liniami w środowisku pracy Część](Part_Line/pl.md) - aby zrozumieć jak przesunąć oś symetrii, pomocna może być zmiana Umiejscowienia takiej linii środowiska pracy Część, która i tak zwykle jest potrzebna do definicji obciążenia siłą odśrodkową)*.

Jednym istotnym ograniczeniem tej funkcji jest to, że nie można nakładać warunków brzegowych na węzły powierzchni slave symetrii cyklicznej *(powierzchni slave w definicji wiązania tie)*, ponieważ spowodowałoby to przewiązanie modelu. Więc w niektórych przypadkach może być konieczne usunięcie węzłów leżących na krawędzi między ścianą z warunkiem brzegowym a ścianą slave symetrii cyklicznej z definicji warunku brzegowego. Niestety FreeCAD nie pozwala operować na zbiorach węzłów i nie można odznaczać pojedynczych węzłów, więc należałoby skorzystać z obejść takich jak dodanie wąskiej [wydzielonej powierzchni](FEM_Geometry_Preparation_and_Meshing/pl#Partycjonowanie_geometrii.md) jako przejścia między ścianą slave a ścianą z warunkiem brzegowym.



## Uwagi

-   To narzędzie korzysta ze [słowa kluczowego \*TIE w CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node251.html).

-    {{Version/pl|1.0}}: Symetria cykliczna korzysta dodatkowo ze [słowa kluczowego \*CYCLIC SYMMETRY MODEL w CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node183.html).





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM ConstraintTie/pl
