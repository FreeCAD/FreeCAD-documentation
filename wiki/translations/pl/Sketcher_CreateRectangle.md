---
 GuiCommand:
   Name: Sketcher CreateRectangle
   Name/pl: Szkicownik: Utwórz prostokąt
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Utwórz prostokąt
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **R**
   SeeAlso: Sketcher_CreatePolyline/pl
---

# Sketcher CreateRectangle/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:24px;"> **Utwórz prostokąt** tworzy prostokąt. {{Version/pl|1.0}}: Narzędzie posiada cztery tryby, z których dwa mogą również tworzyć równoległoboki. Zaokrąglone rogi i tworzenie kopii z przesunięciem są funkcjami opcjonalnymi.

![](images/SketcherCreateRectangleExample.png‎ )



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

Pos-OVP = Pozycyjne [Parametry w widoku](Sketcher_Preferences#Ogólne/pl.md). {{Version/pl|1.0}}
Dim-OVP = Wymiarowe parametry w widoku. {{Version/pl|1.0}}

1.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_CreateRectangle.svg" width=16px> '''Utwórz prostokąt'''**.
    -   Wybierz z menu opcję **Szkic → Elementy geometryczne szkicownika → <img src="images/Sketcher_CreateRectangle.svg" width=16px> Utwórz prostokąt**.
    -   Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_CreateRectangle.svg" width=16px> Utwórz prostokąt** z menu podręcznego.
    -   Użyj skrótu klawiaturowego: **G**, a następnie **R**.
2.  Kursor zmieni się w krzyżyk z ikoną bieżącego trybu narzędzia.
3.  Sekcja **Parametry prostokąta** *({{Version/pl|1.0}})* jest dodawana na górze [okna dialogowego](Sketcher_Dialog/pl.md).
4.  Opcjonalnie można nacisnąć klawisz **U** lub zaznaczyć pole wyboru **Zaokrąglone narożniki**, aby zaokrąglić prostokąt. {{Version/pl|1.0}}
5.  Opcjonalnie naciśnij klawisz **J** lub zaznacz pole wyboru **Ramka**, aby utworzyć drugi odsunięty kształt. <small>(v1.0)</small> 
6.  Opcjonalnie naciśnij klawisz **M** lub wybierz z listy rozwijanej w sekcji parametrów, aby zmienić tryb narzędzia:
    -   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:16px;"> **Wierzchołek, szerokość, wysokość**:
        1.  Wybierz pierwszy róg prostokąta. Lub za pomocą Pos-OVP: wprowadź jego współrzędną X i / lub Y.
        2.  Wybierz przeciwległy róg prostokąta. Lub za pomocą Dim-OVP: wprowadź szerokość i / lub wysokość prostokąta.
    -   <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:16px;"> **Środek, szerokość, wysokość**: {{Version/pl|1.0}}.
        1.  Wybierz środek prostokąta. Lub z Pos-OVP: wprowadź jego współrzędną X i / lub Y.
        2.  Wybierz róg prostokąta. Lub za pomocą Dim-OVP: wprowadź szerokość i / lub wysokość prostokąta.
    -   <img alt="" src=images/Sketcher_CreateRectangle3Points.svg  style="width:16px;"> **Trzy wierzchołki**: {{Version/pl|1.0}}.
        1.  Wybierz pierwszy róg prostokąta. Lub z Pos-OVP: wprowadź jego współrzędne X i / lub Y.
        2.  Wybierz punkt końcowy pierwszej krawędzi prostokąta. Lub za pomocą Dim-OVP: wprowadź długość i / lub kąt pierwszej krawędzi. Kąt jest względem osi X szkicu.
        3.  Wybierz trzeci narożnik prostokąta, przeciwległy do pierwszego. Lub z Dim-OVP: wprowadź długość i / lub kąt drugiej krawędzi. Kąt jest względny w stosunku do pierwszej krawędzi. Tylko jeśli kąt ten wynosi 90°, wynikiem będzie prostokąt.
    -   <img alt="" src=images/Sketcher_CreateRectangle3Points_Center.svg  style="width:16px;"> **Środek, dwa wierzchołki**: {{Version/pl|1.0}}.
        1.  Wybierz środek prostokąta. Lub za pomocą Pos-OVP: wprowadź jego współrzędne X i / lub Y.
        2.  Wybierz pierwszy róg prostokąta. Lub za pomocą Pos-OVP: wprowadź jego współrzędną X i / lub Y.
        3.  Wybierz drugi narożnik prostokąta. Lub za pomocą Dim-OVP: wprowadź długość i / lub kąt krawędzi między pierwszym a drugim narożnikiem. Kąt jest względny w stosunku do drugiej krawędzi połączonej z pierwszym narożnikiem. Tylko jeśli kąt ten wynosi 90°, wynikiem będzie prostokąt.
7.  Jeśli wybrano opcję **Zaokrąglone narożniki**: Wybierz punkt, aby zdefiniować promień zaokrąglenia. Lub za pomocą Dim-OVP: wprowadź go.
8.  Jeśli wybrano opcję **Obramowanie**: Wybierz punkt, aby zdefiniować odległość odsunięcia. Lub za pomocą Dim-OVP: wprowadź ją. Jeśli odsunięcie jest do wewnątrz i większe niż promień, odsunięty kształt nie będzie miał zaokrągleń.
9.  Geometria jest tworzona i dodawane są odpowiednie wiązania oparte na Pos-OVP i Dim-OVP.
10. Jeśli narzędzie działa w [trybie kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md):
    1.  Opcjonalnie kontynuuj tworzenie prostokątów.
    2.  Aby zakończyć, kliknij prawym przyciskiem myszki lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateRectangle/pl
