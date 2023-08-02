---
- GuiCommand:
   Name: Sketcher ConstrainDiameter
   Name/pl: Szkicownik: Wiązanie średnicy
   MenuLocation: Szkic -> Wiązania szkicownika -> Wiązanie średnicy
   Workbenches: Sketcher_Workbench/pl,
PartDesign_Workbench/pl
   Shortcut: **K** **O**
   Version: 0.18
   SeeAlso: Sketcher_ConstrainDistance/pl, Sketcher_ConstrainDistanceX/pl, Sketcher_ConstrainDistanceY/pl
---

# Sketcher ConstrainDiameter/pl



## Opis

To wiązanie powoduje, że wartość średnicy okręgu lub łuku ma określoną wartość. Jeśli przed uruchomieniem polecenia zostanie wybrany więcej niż jeden okrąg lub łuk:

-   Jeśli wiązanie jest zastosowane w trybie Odniesienia, do każdego obiektu osobno dodawane jest nowe wiązanie odniesienia zgodnie z powyższymi zasadami
-   Jeśli wiązanie jest zastosowane w trybie Normalny *(prowadzenie)*, to stosowane są następujące zasady
    -   Wiązanie odniesienia jest stosowane osobno dla każdego obiektu, który jest geometrią zewnętrzną

    -   
        **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Wiązania równości](Sketcher_ConstrainEqual/pl.md)**
        
        są stosowane kolejno pomiędzy wszystkimi obiektami geometrii rzeczywistej / konstrukcyjnej, a wiązanie wymiarowe jest stosowane do pierwszego wybranego obiektu zgodnie z powyższymi zasadami.

Uwaga: Bieguny krzywej złożonej nie mogą być mieszane z innymi typami obiektów podczas wyboru.



## Użycie

1.  Zaznacz jeden lub więcej okręgów lub łuków.
2.  Naciśnij przycisk **[<img src=images/Sketcher_ConstrainDiameter.svg style="width:16px"> [Wiązanie średnicy](Sketcher_ConstrainDiameter/pl.md)**.
3.  Zostanie otwarte okno dialogowe do edycji lub potwierdzenia wartości. Naciśnij przycisk **OK**, aby potwierdzić. W przypadku wybrania wielu okręgów/łuków, wszystkie wiązania przyjmą tę wartość. Edytuj ich odrębne wartości, klikając dwukrotnie na etykietę wymiaru w oknie widoku 3D, lub na liście Wiązań, kliknij dwukrotnie na wiązanie lub kliknij prawym przyciskiem myszy i wybierz *\'Zmień wartość*.
4.  Opcjonalnie etykietę wymiaru i linię można przesuwać i obracać w oknie widoku 3D klikając na wartość i przeciągając, jednocześnie trzymając wciśnięty lewy przycisk myszki.

**Uwaga:** Narzędzie wiązania może być również uruchomione bez wcześniejszego zaznaczenia obiektu. Domyślnie polecenie będzie w trybie kontynuacji, aby utworzyć nowe wiązanie. Naciśnij prawy przycisk myszy lub klawisz **Esc** raz, aby zakończyć wykonywanie polecenia.



## Tworzenie skryptów 


```pythonSketch.addConstraint(Sketcher.Constraint('Diameter', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

Strona [skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, których można użyć dla `ArcOrCircle` oraz zawiera dalsze przykłady tworzenia wiązań przy użyciu skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDiameter/pl
