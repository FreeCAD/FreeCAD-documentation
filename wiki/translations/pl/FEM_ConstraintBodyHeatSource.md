---
 GuiCommand:
   Name: FEM ConstraintBodyHeatSource
   Name/pl: MES: Objętościowe źródło ciepła
   MenuLocation: Model , Warunki brzegowe i obciążenia termiczne , Objętościowe źródło ciepła
   Workbenches: FEM_Workbench/pl
   Version: 0.19
   SeeAlso: FEM_tutorial/pl
---

# FEM ConstraintBodyHeatSource/pl



## Opis

Definiuje wewnętrznie wytworzone ciepło ciała podane w W/kg.



## Użycie

1.  Wciśnij przycisk **<img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> '''Objętościowe źródło ciepła'''** lub wybierz opcję **Model → Warunki brzegowe i obciążenia termiczne → <img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> Objętościowe źródło ciepła** z menu.
2.  Wprowadź wartość:
    -   
        {{VersionPlus/pl|0.21}}
        
        : Do analizy 3D wybierz bryłę z modelu, do analizy 2D wybierz powierzchnię.

    -   
        {{VersionMinus/pl|0.20}}
        
        : Ponieważ narzędzie nie ma okna dialogowego, użyj [edytora właściwości](Property_editor/pl.md) i ustaw właściwość {{PropertyData/pl|Heat Source}}.



## Ograniczenia


{{VersionMinus/pl|0.20}}

: Objętościowe źródło ciepła jest przykładane na cały model. Nie można wskazać pojedynczych brył.



## Uwagi

-   To narzędzie działa tylko z solverem Elmer.
-   Więcej informacji można znaleźć w [tym wątku forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=44705&start=490#p422539) i kolejnych postach. [Ten wątek na forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=28926) może być również przydatny.
-   Przykłady z Elmera można również znaleźć w poradniku [Elmer GUI Tutorials](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintBodyHeatSource/pl
