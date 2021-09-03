---
- GuiCommand:/pl
   Name:Constraint Radius
   Name/pl:Szkicownik: Wiązanie promienia
   MenuLocation:Szkic → Wiązania szkicownika → Wiązanie promienia
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md), [Projekt części](PartDesign_Workbench/pl.md)
   SeeAlso:[Szkicownik: Wiązanie odległości](Sketcher_ConstrainDistance/pl.md), [Szkicownik: Zwiąż odległość poziomą](Sketcher_ConstrainDistanceX/pl.md), [Szkicownik: Zwiąż odległość pionową](Sketcher_ConstrainDistanceY/pl.md)
---

## Opis

To wiązanie powoduje, że wartość promienia okręgu lub łuku jest ściśle określona. Jeśli przed uruchomieniem polecenia zostanie wybrany więcej niż jeden okrąg lub łuk:

-   Jeśli wiązanie jest zastosowane w trybie Odniesienia, do każdego obiektu osobno dodawane jest nowe wiązanie odniesienia zgodnie z powyższymi zasadami
-   Jeśli wiązanie jest zastosowane w trybie Normalny *(prowadzenie)*, to stosowane są następujące zasady
    -   Wiązanie odniesienia jest stosowane osobno dla każdego obiektu, który jest geometrią zewnętrzną

    -   
        **<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Wiązania równości](Sketcher_ConstrainEqual/pl.md)**
        
        są stosowane kolejno pomiędzy wszystkimi obiektami geometrii rzeczywistej / konstrukcyjnej, a wiązanie wymiarowe jest stosowane do pierwszego wybranego obiektu zgodnie z powyższymi zasadami.

Uwaga: Bieguny linii złożonej nie mogą być mieszane z innymi typami obiektów w selekcji.

![](images/Sketcher_ConstrainRadius_example.png )

## Użycie

1.  Wybierz jeden lub więcej okręgów lub łuków.
2.  Naciśnij przycisk **<img src=images/Sketcher_ConstrainRadius.svg style="width:16px"> [Wiązanie promienia](Sketcher_ConstrainRadius.md)**.
3.  Otwiera się wyskakujące okno dialogowe do edycji lub potwierdzenia wartości. Naciśnij przycisk **OK** aby zatwierdzić. W przypadku wybrania wielu okręgów/łuków, wszystkie wiązania przyjmą tę wartość. Edytuj ich odrębne wartości, klikając dwukrotnie na etykietę wymiaru w widoku 3D, lub na liście Wiązań. Kliknij dwukrotnie na wiązanie lub kliknij prawym przyciskiem myszy i wybierz **Zmień wartość**.
4.  Opcjonalnie, etykietę wymiaru i linię można przesuwać i obracać w widoku 3D klikając na wartość i przeciągając, jednocześnie trzymając wciśnięty lewy przycisk myszy.

**Uwaga:** Narzędzie wiązania może być również uruchomione bez wcześniejszego zaznaczenia obiektu. Domyślnie polecenie będzie w trybie kontynuacji, aby utworzyć nowe wiązanie. Naciśnij prawy przycisk myszy lub klawisz **Esc** raz, aby zakończyć wykonywanie polecenia.

## Tworzenie skryptów {#tworzenie_skryptów}


```pythonSketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

Strona [skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, których można użyć dla `ArcOrCircle` oraz zawiera dalsze przykłady tworzenia wiązań przy użyciu skryptów języka Python.





{{Sketcher Tools navi

}}  
