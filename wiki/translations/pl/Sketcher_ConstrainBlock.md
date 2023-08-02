---
- GuiCommand:
   Name: Sketcher ConstrainBlock
   Name/pl: Szkicownik: Wiązanie zablokowania
   MenuLocation: Szkic -> Wiązania szkicownika -> Wiązanie zablokowania
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **K** **B**
   Version: 0.17
   SeeAlso: Sketcher_ConstrainLock/pl
---

# Sketcher ConstrainBlock/pl



## Opis

**Wiązanie zablokowania** powoduje unieruchomienie elementu geometrycznego w miejscu za pomocą pojedynczego wiązania.

Jest ono przeznaczone głównie do użycia z narzędziem **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [Utwórz krzywą złożoną](Sketcher_CreateBSpline/pl.md)**, która może być trudna do pełnego związania w inny sposób.



## Użycie

1.  Wybierz element, który chcesz związać.
2.  Naciśnij przycisk **[<img src=images/Sketcher_ConstrainBlock.svg style="width:16px"> '''Wiązanie zablokowania'''**.

Albo najpierw naciśnij przycisk, a potem wybierz elementy.



## Tworzenie skryptów 


```pythonSketch.addConstraint(Sketcher.Constraint('Block', Edge))```

Strona [skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, których można użyć dla `Krawędzi` oraz zawiera dalsze przykłady tworzenia wiązań przy użyciu skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainBlock/pl
