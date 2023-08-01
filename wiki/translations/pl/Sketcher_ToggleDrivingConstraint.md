---
- GuiCommand:
   Name: Sketcher ToggleDrivingConstraint
   Name/pl: Szkicownik: Przełącz kontrolę wiązania
   MenuLocation: Szkic - Wiązania szkicownika - Przełącz kontrolę wiązania
   Workbenches: [Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut: **K** **X**
   Version: 0.16
   SeeAlso: [Przełącz tryb konstrukcji](Sketcher_ToggleConstruction/pl.md)
---

# Sketcher ToggleDrivingConstraint/pl



## Opis

Narzędzie **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> '''Przełącz kontrolę wiązania'''** zmienia więzy wymiarowe *(blokady odległości, odległości pionowej / poziomej, Długości, Promienia i Kąta)* w tryb referencyjny i z powrotem. Ikony na pasku narzędzi zmieniają kolor na niebieski i zamiast ograniczeń wymiarowych tworzone są wymiary informacyjne. Wymiary te nie wiążą szkicu. Tworzenie wymiarów referencyjnych w szkicu może być użyteczne jako sposób sprawdzania wymiarów. Po nadaniu im nazwy mogą być również używane do tworzenia więzów w innym szkicu poprzez [wyrażenia](Expressions/pl.md).

![](images/Sketcher_Constraint_Toolbar_ReferenceMode.png ) 
*Pasek narzędzi Wiązania szkicownika z wiązaniami wymiarowymi w trybie wymiaru odniesienia ''(kolor niebieski)''.*

![](images/Sketcher_ToggleConstraint_example.png ) 
*W celu zdefiniowania profilu ustawiono poziome wiązanie odległości ''({{Value|50 mm*)'', wiązanie pionowe ''({{Value|30 mm}})'' oraz wiązanie kąta ''({{Value|75°}}); na odcinku linii ukośnej dodano wymiar odniesienia, aby poznać jego długość ''(31,0583 mm)''.}}



## Użycie

1.  Naciśnij przycisk **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [Przełącz kontrolę wiązania](Sketcher_ToggleDrivingConstraint/pl.md)**. Ikony wiązań wymiarowych na pasku narzędzi Wiązania szkicownika zmieniają kolor z czerwonego na niebieski.
2.  Zwykła metoda tworzenia wiązań wymiarowych działa tak samo, ale zamiast tego dodawany jest niebieski wymiar porównawczy.
3.  Aby przywrócić pasek narzędzi Wiązania szkicownik do trybu konstrukcyjnego *(czerwony)*, naciśnij ponownie przycisk **Przełącz kontrolę wiązania**.
4.  Aby przekształcić wiązanie wymiarowe w wymiar informacyjny lub odwrotnie, wybierz je i naciśnij przycisk **Przełącz kontrolę wiązania**.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleDrivingConstraint/pl
