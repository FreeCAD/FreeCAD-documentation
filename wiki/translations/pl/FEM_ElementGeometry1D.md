---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM ElementGeometry1D
   Name/pl: MES: Przekrój poprzeczny belki
   MenuLocation: Model , Geometria elementu , Przekrój poprzeczny belki
   Workbenches: FEM_Workbench/pl
   Shortcut: **C** **B**
   SeeAlso: FEM_tutorial/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: CalculiX, Mystran, Z88
}}
---

# FEM ElementGeometry1D/pl



## Opis

**ElementGeometry1D** jest używane do definiowania przekrojów poprzecznych elementów belkowych. Obecnie dostępne są następujące typy przekrojówː prostokątny, kołowy, rurowy.


{{VersionPlus/pl|1.1}}

: Dostępny jest również przekrój skrzynkowy i eliptyczny.



## Użycie

1.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_ElementGeometry1D.svg" width=16px> [Przekrój poprzeczny belki](FEM_ElementGeometry1D/pl.md)**.
    -   Wybierz opcję **Model → Geometria elementu → <img src="images/FEM_ElementGeometry1D.svg" width=16px> Przekrój poprzeczny belki** z menu.
2.  Wybierz typ przekroju i podaj wymagane wymiary:
    -   Prostokątny: szerokość i wysokość,

    -   Kołowy: średnica,

    -   Rurowy: średnica zewnętrzna i grubość,

    -   
        {{VersionPlus/pl|1.1}}
        
        : Eliptyczny: długość osi 1i długość osi 2,

    -   
        {{VersionPlus/pl|1.1}}
        
        : Skrzynkowy: wysokość, szerokość, grubość T1 - T4.
3.  Opcjonalnie, wciśnij przycisk **Dodaj** w panelu zadań i wybierz krawędź, do której chcesz przypisać przekrój. Jeśli żadna krawędź nie została wybrana, wszystkie pozostałe krawędzie *(bez przypisanych innych obiektów **Przekrój poprzeczny belki**)* będą automatycznie użyte.



## Właściwości

-    **Section Type**: określa typ przekroju belkowego (*Rectangular* (prostokątny), *Circular* (kołowy), *Pipe* (rurowy), {{VersionPlus/pl|1.1}}: *Elliptical* (eliptyczny) i *Box* (skrzynkowy))

-    {{VersionPlus/pl|1.1}}: **Box Height**: height of box section, used if **Section Type** is *Box*

-    {{VersionPlus/pl|1.1}}: **Box T1**: grubość T1 przekroju skrzynkowego, używana jeśli właściwość **Section Type** jest ustawiona na *Box*

-    {{VersionPlus/pl|1.1}}: **Box T2**: grubość T2 przekroju skrzynkowego, używana jeśli właściwość **Section Type** jest ustawiona na *Box*

-    {{VersionPlus/pl|1.1}}: **Box T3**: grubość T3 przekroju skrzynkowego, używana jeśli właściwość **Section Type** jest ustawiona na *Box*

-    {{VersionPlus/pl|1.1}}: **Box T4**: grubość T4 przekroju skrzynkowego, używana jeśli właściwość **Section Type** jest ustawiona na *Box*

-    {{VersionPlus/pl|1.1}}: **Box Width**: szerokość przekroju skrzynkowego, używana jeśli właściwość **Section Type** jest ustawiona na *Box*

-    **Circ Diameter**: średnica przekroju kołowego, używana jeśli właściwość **Section Type** jest ustawiona na *Circular*

-    {{VersionPlus/pl|1.1}}: **Axis 1 Length**: długość osi 1 przekroju eliptycznego, używana jeśli właściwość **Section Type** jest ustawiona na *Elliptical*

-    {{VersionPlus/pl|1.1}}: **Axis 2 Length**: długość osi 2 przekroju eliptycznego, używana jeśli właściwość **Section Type** jest ustawiona na *Elliptical*

-    **Pipe Diameter**: średnica zewnętrzna przekroju rurowego, używana jeśli właściwość **Section Type** jest ustawiona na *Pipe*

-    **Pipe Thickness**: grubość przekroju rurowego, używana jeśli właściwość **Section Type** jest ustawiona na *Pipe*

-    **Rect Height**: wysokość przekroju prostokątnego, używana jeśli właściwość **Section Type** jest ustawiona na *Rectangular*

-    **Rect Width**: szerokość przekroju prostokątnego, używana jeśli właściwość **Section Type** jest ustawiona na *Rectangular*



## Ograniczenia

-    {{VersionMinus/pl|1.0}}: Inne typy przekrojów dostępnych w CalculiX (eliptyczny, skrzynkowy i ogólny) nie są obecnie wspierane. Można z nich skorzystać ręcznie edytując plik .inp.

-    {{VersionPlus/pl|1.1}}: Przekrój ogólny nie jest obecnie wspierany. Można z niego skorzystać ręcznie edytując plik .inp.



## Uwagi

-   Do wyświetlania wyników z solvera CalculiX na siatce zwizualizowanej dla danego przekroju, należy ustawić właściwość `Beam Shell Result Output 3D` w [solverze CalculiX](FEM_SolverCalculixCxxtools/pl.md) na wartość {{True/pl}}.
-   Niektóre przekroje wymagają użycia konkretnych typów elementów:
    -   przekrój kołowy - elementy drugiego rzędu

    -   przekrój rurowy - elementy drugiego rzędu ze zredukowanym całkowaniem ({{Version/pl|1.0}}: zredukowane całkowanie jest domyślnie włączone dla elementów belkowych i można je przełączać przy pomoc właściwości *Beam Reduced Integration* w [ustawieniach solvera CalculiX](FEM_SolverCalculixCxxtools/pl.md))

    -   
        {{VersionPlus/pl|1.1}}
        
        : przekrój eliptyczny - elementy drugiego rzędu

    -   
        {{VersionPlus/pl|1.1}}
        
        : przekrój skrzynkowy - elementy drugiego rzędu ze zredukowanym całkowaniem (zobacz wyjaśnienie powyżej)
-   To narzędzie korzysta ze [słowa kluczowego \*BEAM SECTION w CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node162.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry1D/pl
