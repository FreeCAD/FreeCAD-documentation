---
 GuiCommand:
   Name: Constraint Radius
   Name/pl: Szkicownik: Wiązanie promienia
   MenuLocation: Szkic , Wiązania szkicownika , Wiązanie promienia
   Workbenches: Sketcher_Workbench/pl, PartDesign_Workbench/pl
   Shortcut: **K** **R**
   SeeAlso: Sketcher_ConstrainRadiam/pl, Sketcher_ConstrainDiameter/pl
---

# Sketcher ConstrainRadius/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:24px;"> *Wiązanie promienia* ustala promień okręgów, łuków i [wag krzywych złożonych](Sketcher_CreateBSpline/pl#Uwagi.md).

![](images/Sketcher_ConstrainRadius_example.png )



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Wybierz jeden lub więcej okręgów lub łuków.
2.  Naciśnij przycisk **[<img src=images/Sketcher_ConstrainRadius.svg style="width:16px"> [Wiązanie promienia](Sketcher_ConstrainRadius.md)**.
3.  Otwiera się wyskakujące okno dialogowe do edycji lub potwierdzenia wartości. Naciśnij przycisk **OK** aby zatwierdzić. W przypadku wybrania wielu okręgów/łuków, wszystkie wiązania przyjmą tę wartość. Edytuj ich odrębne wartości, klikając dwukrotnie na etykietę wymiaru w widoku 3D, lub na liście Wiązań. Kliknij dwukrotnie na wiązanie lub kliknij prawym przyciskiem myszy i wybierz **Zmień wartość**.
4.  Opcjonalnie, etykietę wymiaru i linię można przesuwać i obracać w widoku 3D klikając na wartość i przeciągając, jednocześnie trzymając wciśnięty lewy przycisk myszy.




1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   
        {{Version/pl|1.0}}
        
        : Jeśli opcja **Wiązania wymiarów** w [preferencjach](Sketcher_Preferences/pl#Ogólne.md) jest ustawiona na {{Value|Narzędzie pojedyncze}} *(domyślnie)*: naciśnij strzałkę w dół po prawej stronie przycisku **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** i wybierz opcję **<img src="images/Sketcher_ConstrainRadius.svg" width=16px> Wiązanie promienia** z rozwijanej listy.

    -   Jeśli ta preferencja ma inną wartość *(i w {{VersionMinus/pl|0.21}})*: naciśnij przycisk **<img src="images/Sketcher_ConstrainRadius.svg" width=16px> '''Wiązanie promienia'''**.

    -   Wybierz opcję z menu **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainRadius.svg" width=16px> Wiązanie promienia**.

    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widok 3D](3D_view/pl.md) i wybierz opcję **Wiązania wymiarów → <img src="images/Sketcher_ConstrainRadius.svg" width=16px> Wiązanie promienia** z menu podręcznego.

    -   Użyj skrótu klawiaturowego: **K**, a następnie **R**.
3.  Dalsze kroki można znaleźć na stronie [Zwiąż automatycznie promień / średnicę](Sketcher_ConstrainRadiam/pl#Tryb_kontynuacji.md).



### Tryb jednorazowy 

Zapoznaj się z informacjami na stronie: [Zwiąż automatycznie promień / średnicę](Sketcher_ConstrainRadiam/pl#Tryb_jednorazowy.md).



## Tworzenie skryptów 


```pythonSketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

Strona [skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, których można użyć dla `ArcOrCircle` oraz zawiera dalsze przykłady tworzenia wiązań przy użyciu skryptów języka Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadius/pl
