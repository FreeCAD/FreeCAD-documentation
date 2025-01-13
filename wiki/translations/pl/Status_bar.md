# Status bar/pl
## Wprowadzenie

**Pasek statusu** to prosta wstążka, która pojawia się w dolnej części [interfejs](interface/pl.md) programu FreeCAD.

Gdy wskaźnik myszy znajduje się nad przyciskiem lub menu, informacje o użyciu tego polecenia są wyświetlane zarówno w wyskakującym okienku tekstowym, jak i na pasku statusu.

![](images/FreeCAD_Status_bar.png )

Pasek statusu pokazuje wybrany tryb [nawigacji myszką](Mouse_navigation/pl.md) i poziom powiększenia po prawej stronie. Poziom powiększenia podaje wielkość bieżącego [widoku 3D](3D_view/pl.md) w odpowiednich jednostkach dla bieżącej skali, na przykład milimetrach *(mm)* lub metrach *(m)*.

Pasek stanu pokazuje również ostatni wskazany obiekt *(każdy obiekt pod kursorem jest wstępnie wybrany)* lub element obiektu *(wierzchołek, krawędź, ściana)* oraz współrzędne kursora myszki w momencie ostatniego wskazania. Jest to przydatne, aby od razu znać współrzędne konkretnych wierzchołków w swoich kształtach. Współrzędne 3D są aktualizowane automatycznie, dopóki kursor myszki znajduje się nad elementem geometrycznym. Aktualizacja zatrzymuje się, gdy kursor myszki spoczywa nad pustą przestrzenią w oknie [widoku 3D](3D_view/pl.md).

![](images/FreeCAD_Status_bar_selected.png )



## Szybki pomiar 


{{Version/pl|1.0}}

Funkcja Szybki pomiar korzysta z prawej części paska statusu aby wyświetlać pomiary w oparciu o zaznaczenia w widoku 3D:

-   Długość krawędzi
-   Powierzchnia ścian
-   Odległość między punktami, krawędziami lub ścianami
-   Kąt między krawędziami
-   Promień krawędzi kołowych lub ścian cylindrycznych


{{Interface navi

}}



---
⏵ [documentation index](../README.md) > Status bar/pl
