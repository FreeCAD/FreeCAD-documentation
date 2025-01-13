---
 GuiCommand:Container|
{{GuiCommand/pl
   Name: FEM ConstraintBodyHeatSource
   Name/pl: MES: Objętościowe źródło ciepła
   MenuLocation: Model , Warunki brzegowe i obciążenia termiczne , Objętościowe źródło ciepła
   Workbenches: FEM_Workbench/pl
   Version: 0.19
   SeeAlso: FEM_tutorial/pl
}}
{{GuiCommandFemInfo/pl
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintBodyHeatSource/pl



## Opis

Definiuje wewnętrznie wytworzone ciepło ciała podane w W/kg.


{{VersionPlus/pl|1.0}}

: Można również definiować źródło ciepła w W.



## Użycie

1.  Wciśnij przycisk **<img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> '''Objętościowe źródło ciepła'''** lub wybierz opcję **Model → Warunki brzegowe i obciążenia termiczne → <img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> Objętościowe źródło ciepła** z menu.

2.  
    {{VersionPlus/pl|0.21}}: Wciśnij przycisk **Dodaj**. Do analizy 3D wybierz \'Bryłę\' (body), a do analizy 2D wybierz \'Powierzchnię\'.

3.  Wprowadź wartość:
    -   
        {{VersionMinus/pl|0.20}}
        
        : Ponieważ to narzędzie nie ma panelu zadań, użyj [edytora właściwości](Property_editor/pl.md) i ustaw odpowiednio właściwość **Heat Source**.

    -   
        {{Version/pl|0.21}}
        
        : Wprowadź wartość źródła ciepła w W/kg.

    -   
        {{VersionPlus/pl|1.0}}
        
        : Wybierz tryb:

        -   *Szybkość dyssypacji* - wprowadź szybkość dyssypacji w W/kg .
        -   *Moc całkowita* - wprowadź moc całkowitą w W.



## Ograniczenia

-    {{VersionMinus/pl|0.20}}: Objętościowe źródło ciepła jest przykładane na cały model. Nie można wskazać pojedynczych brył.

-    {{VersionMinus/pl|0.21}}: Ta funkcja działa tylko z solverem Elmer.



## Uwagi

-   Więcej informacji można znaleźć w [tym wątku forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=44705&start=490#p422539) i kolejnych postach. [Ten wątek na forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=28926) może być również przydatny.

-   Przykłady z Elmera można również znaleźć w poradniku [Elmer GUI Tutorials](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf).

-    <small>(v1.0)</small> : Ta funkcja wykorzystuje kartę [\*DFLUX w CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node188.html).

-    <small>(v1.0)</small> : Ponieważ CalculiX oczekuje danych wejściowych strumienia ciepła ciała w W/mm\^3, podczas gdy dla Elmera jest to W/kg, w razie potrzeby konwersja określonej wartości *(w W lub W/kg)* jest wykonywana wewnętrznie dla każdego solwera, przy użyciu objętości wybranej bryły i gęstości przypisanego do niej materiału.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintBodyHeatSource/pl
