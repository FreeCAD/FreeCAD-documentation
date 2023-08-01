---
- GuiCommand:
   Name:Mesh FromPartShape
   Name/pl:Siatka: Utwórz siatkę z kształtu
   MenuLocation:Siatki → Utwórz siatkę z kształtu ...
   Workbenches:[Siatka](Mesh_Workbench/pl.md)
---

# Mesh FromPartShape/pl



## Opis

Polecenie **Utwórz siatkę z kształtu** tworzy nieparametryczne obiekty [siatek](Mesh/pl.md) *([Siatka: Cecha](Mesh_Feature/pl.md))* z obiektów [kształtu](Shape/pl.md) *([Część: Cecha](Part_Feature/pl.md))*.

Operacją odwrotną jest [Kształt z siatki](Part_ShapeFromMesh/pl.md) ze środowiska <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md).



## Użycie

1.  Opcjonalnie wybierz jeden lub więcej obiektów.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Mesh_FromPartShape.svg" width=16px> [Utwórz siatkę z kształtu](Mesh_FromPartShape/pl.md)**.
    -   Wybierz opcję z menu **Siatki → <img src="images/Mesh_FromPartShape.svg" width=16px> Utwórz siatkę z kształtu ...**.
3.  Otwiera się panel zadań **Rozdrobnienie**.
4.  Gdy panel zadań jest otwarty, możesz stworzyć nowe zaznaczenie lub zmienić istniejące.
5.  Wybierz zakładkę dla generatora siatki, którego chcesz użyć.
6.  Określ wymagane ustawienia. Zobacz akapit [generator siatki](#Generator_siatki.md) aby uzyskać więcej informacji.
7.  Naciśnij przycisk **OK**, aby zamknąć panel zadań i zakończyć polecenie.



## Generator siatki 

Oto dostępne generatory siatki i ich ustawienia:



### Generator standardowy 

-    **Odchylenie powierzchni**: maksymalne [odchylenie liniowe](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) odcinka siatki od powierzchni obiektu.

-    **Odchylenie kątowe**: maksymalne [odchylenie kątowe](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) z jednej części siatki do następnej. To ustawienie jest używane podczas tworzenia siatek na zakrzywionych powierzchniach.

-    **Względne odchylenie powierzchni**: jeżeli opcja jest zaznaczona, maksymalnym odchyleniem liniowym segmentu siatki będzie określona wartość **Odchylenie powierzchni** pomnożona przez długość bieżącego segmentu siatki *(krawędzi)*.

-    **Zastosuj kolor powierzchni do siatki**: jeżeli opcja jest zaznaczona, siatka otrzyma kolory powierzchni obiektu.

-    **Zdefiniuj segmenty według kolorów ścian**: jeżeli opcja jest zaznaczona, segmenty siatki zostaną pogrupowane według kolorów powierzchni obiektu. Grupy te zostaną wyeksportowane do formatów wyjściowych siatki obsługujących tę funkcję *(na przykład format [OBJ](https://en.wikipedia.org/wiki/Wavefront_.obj_file))*.



### Generator Mefisto 

-    **Maksymalna długość krawędzi**: maksymalna długość krawędzi siatki. Mniejsza wartość powoduje, że siatka jest drobniejsza. Podanie wartości {{Value|0}} lub usunięcie zaznaczenia pola wyboru powoduje powstanie bardzo grubej siatki.

    -   Jeśli naciśniesz przycisk **Szacunkowo**, generator siatki wprowadzi szacunkową wartość dla parametru **Maksymalna długość krawędzi**. Wartość ta nie jest zbyt wiarygodna, jeśli wybrano wiele obiektów.



### Generator Netgen 

-    **Stopień rozdrobnienia**: wybierz opcje dla drobiazgowości siatki:

    -   
        **Bardzo zgrubnie**
        

    -   
        **Zgrubnie**
        

    -   
        **Umiarkowanie**
        

    -   
        **Drobno**
        

    -   
        **Bardzo drobno**
        

    -   
        **Wartość użytkownika**
        
        : dla tej opcji można określić następujące ustawienia:

        -   
            **Stopnie rozmiaru siatki**
            
            : mniejsza wartość skutkuje drobniejszą siatką. Wartość musi być z zakresu {{Value|0.1}} - {{Value|1.0}}.

        -   
            **Liczba elementów na krawędź**
            
            : większa wartość powoduje, że siatka jest drobniejsza. Wartość musi być z zakresu {{Value|0.2}} - {{Value|10.0}}.

        -   
            **Liczba elementów na promień krzywizny**
            
            : większa wartość powoduje powstanie drobniejszej siatki. Wartość musi być z zakresu {{Value|0.2}} - {{Value|10}}.

-    **Optymalizuj powierzchnię**: jeśli opcja jest zaznaczona, kształt powierzchni zostanie zoptymalizowany.

-    **Elementy drugiego rzędu**: jeśli opcja jest zaznaczona, zostaną wygenerowane elementy drugiego rzędu, co spowoduje powstanie drobniejszej siatki.

-    **Dominujące czworokąty**: jeśli opcja jest zaznaczona, siatka będzie preferowała [czworoboczne ściany](https://en.wikipedia.org/wiki/Types_of_mesh#Two-dimensional).



### Generator Gmsh 

Dla użytkowników systemu Linux: wymagany jest zewnętrzny moduł [Gmsh](https://gmsh.info/).

-    **Tworzenie siatki**: wybierz opcję tworzenia siatki:

    -   
        **Automatycznie**
        

    -   
        **Adaptacyjnie**
        

    -   
        **Delaunay**
        

    -   
        **Frontal**
        

    -   
        **BAMG**
        

    -   
        **Przedni czworobok**
        

    -   
        **Równoległoboki**
        

-    **Maksymalny rozmiar elementu**: mniejsza wartość powoduje, że siatka jest drobniejsza. Wprowadź wartość {{Value|0}}, aby rozmiar ten był określany automatycznie.

-    **Minimalny rozmiar elementu**: mniejsza wartość powoduje, że siatka jest drobniejsza. Wartość ta powinna być mniejsza niż **Maksymalny rozmiar elementu**. Wprowadź wartość {{Value|0}}, aby rozmiar ten był określany automatycznie.

-    **Kąt**: wydaje się być nieobsługiwane w tym momencie.

-    **Ścieżka**: naciśnij przycisk **...** i przejdź do pliku **gmsh.exe**.

-   Jeśli proces tworzenia siatki trwa zbyt długo, możesz nacisnąć przycisk **Zatrzymaj**, aby go przerwać.

-   Naciśnij przycisk **Wyczyść**, aby usunąć informacje w obszarze tekstowym.



## Uwagi

-   To narzędzie nie jest ograniczone jedynie do obiektów utworzonych za pomocą środowiska [Część](Part_Workbench/pl.md). Może ono utworzyć siatkę z dowolnego obiektu posiadającego kształt, w tym obiektów utworzonych za pomocą środowiska pracy [Projekt Części](PartDesign_Workbench/pl.md).
-   Polecenie [Ekport](Std_Export/pl.md) może eksportować obiekty kształtu bezpośrednio do formatu siatki.
-   Zobacz także poradnik: [Eksport do formatu STL lub OBJ](Export_to_STL_or_OBJ/pl.md).



## Ustawienia



### Standardowy

-   Ustawienie **Odchylenie powierzchni** jest zapisywane: **Przybory → Edycja parametrów ... → BaseApp → Preferences → Mod → Mesh → Meshing → Standard → LinearDeflection**
-   Ustawienie **Odchylenie kątowe** jest zapisywane: **Przybory → Edycja parametrów ... → BaseApp → Preferences → Mod → Mesh → Meshing → Standard → AngularDeflection**
-   Ustawienie **Względne odchylenie powierzchni** jest zapisywane: **Przybory → Edycja parametrów ... → BaseApp → Preferences → Mod → Mesh → Meshing → Standard → RelativeLinearDeflection**.



### Gmsh

-   Ustawienie **Ścieżka** jest zapisywane: **Przybory → Edycja parametrów ... → BaseApp → Preferences → Mod → Mesh → Meshing → gmshExe**.



## Właściwości

Zapoznaj się z informacjami na stronie: [cecha siatki](Mesh_Feature/pl.md).



## Tworzenie skryptów 

Zobacz również: [FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby stworzyć obiekt siatki z obiektu kształtu należy użyć metody `meshFromShape` modułu *MeshPart*. Metoda ta posiada kilka sygnatur. Sygnatura określa generator siatki, który zostanie użyty. Poniższy przykład używa sygnatury generatora siatki Mefisto.


```python
import FreeCAD, Part, Mesh, MeshPart

cyl = FreeCAD.ActiveDocument.addObject("Part::Cylinder","Cylinder")
FreeCAD.ActiveDocument.recompute()

msh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "Mesh")
msh.Mesh = MeshPart.meshFromShape(Shape=cyl.Shape, MaxLength=1)
msh.ViewObject.DisplayMode = "Flat Lines"
```





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh FromPartShape/pl
