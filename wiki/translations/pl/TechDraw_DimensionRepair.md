---
- GuiCommand:
   Name:TechDraw DimensionRepair
   Name/pl:Rysunek Techniczny: Napraw odniesienia do wymiarów
   MenuLocation:Rysunek Techniczny → Wymiary → Napraw odniesienia do wymiarów
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version:0.21
   SeeAlso:[Wstaw wymiar długości](TechDraw_LengthDimension/pl.md)
---

# TechDraw DimensionRepair/pl



## Opis

Narzędzie **Napraw odniesienia do wymiarów** może dostosować odniesienia geometrii 2D lub 3D wymiaru. Odniesienia te mogą stać się nieprawidłowe z powodu \"[problemu nazewnictwa topologicznego](Topological_naming_problem/pl.md)\" lub usuwania ukrytych linii.

Zobacz stronę [Wstaw wymiar długości](TechDraw_LengthDimension/pl#Ograniczenia.md), aby dowiedzieć się więcej na temat wymiarów i nazewnictwa topologicznego.



## Użycie

1.  Wybierz wymiar do skorygowania i opcjonalnie nowe odniesienia do geometrii, punktu lub krawędzi w widoku Rysunku Technicznego lub w [widoku 3D](3D_view/pl.md).
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_DimensionRepair.svg" width=16px> '''Napraw odniesienia do wymiarów'''**.
    -   Wybierz z menu opcję **Rysunek Techniczny → Wymiary → <img src="images/TechDraw_DimensionRepair.svg" width=16px> Napraw odniesienia do wymiarów**.
3.  Otworzy się panel zadań **Naprawa wymiaru** pokazujący wybrany wymiar i bieżące odniesienia do geometrii.
4.  Wybierz nowe odniesienia do geometrii, jeśli jeszcze tego nie zrobiłeś.
5.  Naciśnij przycisk **Zamień odwołania na aktualnie wybrane**.
6.  Naciśnij przycisk **OK**, aby zaktualizować wymiar.
7.  Jeśli wybrano odniesienia 3D: opcjonalnie zmień wartość właściwości **Tyo pomiaru** na {{True/pl}}.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie TechDraw DimensionRepair nie może być używane w [makroinstrukcjach](Macros/pl.md) lub z konsoli [Python](Python/pl.md). Właściwości odniesienia wymiaru mogą być aktualizowane przy użyciu języka Python.





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DimensionRepair/pl
