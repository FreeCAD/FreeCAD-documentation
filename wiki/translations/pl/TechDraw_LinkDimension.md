---
- GuiCommand:
   Name: TechDraw LinkDimension
   Name/pl: Rysunek Techniczny: Powiąż wymiar z geometrią 3D
   MenuLocation: Rysunek Techniczny - Wymiary - Powiąż wymiar z geometrią 3D
   Workbenches: [Rysunek Techniczny](TechDraw_Workbench/pl.md)
   SeeAlso: [Wstaw widok](TechDraw_View/pl.md), [Wstaw grupę rzutów](TechDraw_ProjectionGroup/pl.md)
---

# TechDraw LinkDimension/pl

Oczekuje się, że narzędzie **Powiąż wymiar z geometrią 3D** zostanie w przyszłości wycofane. Narzędzie [Napraw odniesienia do wymiarów](TechDraw_DimensionRepair/pl.md) może być używane do zmiany zarówno odniesień 2D, jak i 3D.



## Opis

Narzędzie **Powiąż wymiar z geometrią 3D** tworzy łącze między geometrią 3D a jednym lub kilkoma istniejącymi rzutowanymi wymiarami na stronie. To połączenie umożliwia wymiarowi użycie rzeczywistych wartości 3D zamiast wartości rzutowanych 2D.

Najczęstszym zastosowaniem narzędzia **Powiąż wymiar z geometrią 3D** jest wymiarowanie widoków izometrycznych w Grupie rzutów. Rzutowana długość krawędzi w widoku izometrycznym niekoniecznie będzie równa rzeczywistej długości krawędzi. W widoku ortogonalnym długość rzutowana i rzeczywista będą równe.

Łącze nakazuje wymiarowi obliczenie jego wartości bezpośrednio z geometrii 3D.



## Użycie

1.  Utwórz odpowiedni wymiar na stronie rysunku przy użyciu [Wstaw wymiar długości](TechDraw_LengthDimension/pl.md), [Wstaw wymiar poziomy](TechDraw_HorizontalDimension/pl.md) itp. Wymiar ten będzie znajdował się we właściwym miejscu na stronie, ale będzie pokazywał przewidywaną wartość wymiaru.
2.  Wybierz geometrię w oknie widoku 3D, na przykład krawędź, która odpowiada rzutowanej geometrii wymiaru.
3.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_LinkDimension.svg" width=16px> '''Powiąż wymiar z geometrią 3D'''**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Wymiary → <img src="images/TechDraw_LinkDimension.svg" width=16px> Powiąż wymiar z geometrią 3D**.
4.  Otworzy się panel zadań.
5.  Wybierz jeden lub więcej wymiarów, które mają zostać połączone z wybraną geometrią 3D.
6.  Naciśnij **OK**.

Operacja powiązania zmienia właściwość **TypPomiaru** wymiaru z wartości `Rzutowany` na {{True/pl}}.



## Ograniczenia

-   Obiekty wymiarów są podatne na problemy z *[nazewnictwem topologicznym](Topological_naming_problem/pl.md)*. Aby uzyskać więcej informacji, zobacz informacje w narzędziu [Wstaw wymiar długości](TechDraw_LengthDimension/pl.md). Zaleca się, aby wymiarowanie było jednym z ostatnich kroków w procesie rysowania.

Narzędzie do tworzenia połączeń nie powstrzyma cię przed tworzeniem nielogicznych połączeń, więc musisz wybrać odpowiednią krawędź z widoku 3D podczas tworzenia połączenia.

Obecnie nie ma sposobu na zerwanie powiązania; można zmienić **TypPomiaru** z powrotem na `Rzutowany`, aby wymiar używał wartości przewidywanej zamiast wartości powiązanej.

Należy pamiętać, że jeśli wymiar do połączenia jest oparty na dwóch wierzchołkach, należy wybrać dwa wierzchołki w oknie widoku 3D. Podobnie, jeśli wymiar jest oparty na krawędzi, należy wybrać krawędź w oknie widoku 3D.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Powiąż wymiar z geometrią 3D** nie jest bezpośrednio użyteczne w makropoleceniach, ale zmiana właściwości **Odniesienia 3D** może osiągnąć ten sam rezultat.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LinkDimension/pl
