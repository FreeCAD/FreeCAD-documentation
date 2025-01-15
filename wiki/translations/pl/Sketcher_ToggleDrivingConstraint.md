---
 GuiCommand:
   Name: Sketcher ToggleDrivingConstraint
   Name/pl: Szkicownik: Przełącz kontrolę wiązania
   MenuLocation: Szkic , Wiązania szkicownika , Przełącz kontrolę wiązania
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **K** **X**
   Version: 0.16
   SeeAlso: Sketcher_ToggleActiveConstraint/pl
---

# Sketcher ToggleDrivingConstraint/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:24px;"> **Przełącz kontrolę wiązania** albo przełącza [narzędzia do tworzenia wiązań wymiarowych](Sketcher_Workbench/pl#Sketcher_CompDimensionTools.md) pomiędzy trybem konstrukcyjnym a trybem odniesienia, albo przełącza wybrane wiązania wymiarowe pomiędzy tymi trybami.

W przeciwieństwie do wiązań prowadzących, wiązania referencyjne nie wiążą szkicu, ich wartość zależy od innych wiązań, są one sterowane. Mogą być przydatne do weryfikacji pomiarów. Mogą być używane w [wyrażeniach](Expressions/pl.md), ale nie w samym szkicu.

![](images/Sketcher_ToggleConstraint_example.png ) 
*W celu zdefiniowania profilu ustawiono poziome wiązanie odniesienia odległości ''({{Value|50 mm*)'', wiązanie odniesienia pionowe ''({{Value|30 mm}})'' oraz wiązanie odniesienia kąta ''({{Value|75°}}); na odcinku linii ukośnej dodano wymiar odniesienia, aby poznać jego długość ''(31,0583 mm)''.}}



## Użycie



### Przełączanie narzędzi 

1.  Naciśnij przycisk **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [Przełącz kontrolę wiązania](Sketcher_ToggleDrivingConstraint/pl.md)**. Ikony wiązań wymiarowych na pasku narzędzi Wiązania szkicownika zmieniają kolor z czerwonego na niebieski.
2.  Zwykła metoda tworzenia wiązań wymiarowych działa tak samo, ale zamiast tego dodawany jest niebieski wymiar porównawczy.
3.  Aby przywrócić pasek narzędzi Wiązania szkicownik do trybu konstrukcyjnego *(czerwony)*, naciśnij ponownie przycisk **Przełącz kontrolę wiązania**.
4.  Aby przekształcić wiązanie wymiarowe w wymiar informacyjny lub odwrotnie, wybierz je i naciśnij przycisk **Przełącz kontrolę wiązania**.




1.  Upewnij się, że nie wybrano żadnych wiązań wymiarowych.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> '''Przełącz kontrolę wiązania'''**.
    -   Wybierz z menu opcję **Szkic → Elementy geometryczne szkicownika → <img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> Przełącz kontrolę wiązania**.
    -   Użyj skrótu klawiaturowego: **K**, a następnie **X**.
3.  Tryb narzędzi do tworzenia wiązań wymiarowych jest przełączany:
    -   W trybie kontroli ich ikony w menu i na pasku narzędzi są czerwone i tworzą wiązania kontrolujące *(domyślnie [kolor](Sketcher_Preferences/pl#Wygląd.md) czerwony)*. Ikona tego narzędzia to: <img alt="" src=images/Sketcher_ToggleConstraint.svg  style="width:16px;">.
    -   W trybie odniesienia ikony menu i paska narzędzi są niebieskie i tworzą wiązania odniesienia *(domyślny kolor niebieski)*. Ikona tego narzędzia to: <img alt="" src=images/Sketcher_ToggleConstraint_Driven.svg  style="width:16px;">.



### Przełączanie wiązań 

1.  Wybierz jedno lub więcej wiązań wymiarowych.
2.  Wywołaj narzędzie w sposób opisany powyżej lub z jedną z następujących dodatkowych opcji:
    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w oknie [widoku 3D](3D_view/pl.md) i wybierz z menu kontekstowego **<img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> Przełącz kontrolę wiązania**.

    -   Kliknij prawym przyciskiem myszy w sekcji **Wiązania** w [oknie dialogowym](Sketcher_Dialog/pl.md) i wybierz opcję **Przełącz z / do trybu konstrukcyjnego** z menu podręcznym.
3.  Wybrane wiązania zostaną zmienione z trybu kontroli na tryb odniesienia lub odwrotnie. Ich wygląd zmienia się odpowiednio.
4.  Tryb narzędzi do tworzenia wiązań wymiarowych nie ulega zmianie.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleDrivingConstraint/pl
