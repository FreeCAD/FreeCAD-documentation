---
- GuiCommand:
   Name: Sketcher Clone
   Name/pl: Szkicownik: Klonuj
   MenuLocation: Szkic - Elementy geometryczne szkicownika - Klonuj
   Workbenches: [Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut: **Z** **L**
   Version: 0.16
   SeeAlso: [Kopiuj](Sketcher_Copy/pl.md), [Przesuń](Sketcher_Move/pl.md)
---

# Sketcher Clone/pl



## Opis

Klonuje wybrane elementy szkicu z jednego punktu do drugiego, używając ostatnio wybranego punktu jako odniesienia. Jeśli jakiekolwiek wiązania są częścią elementów źródłowych, to nowe wiązania są powiązane z wiązaniami źródłowymi. Jeśli wiązania w źródle zostaną zmienione, to wiązania w klonie również zostaną zmienione. Aby uniknąć tego powiązania zobacz opis narzędzia **[<img src=images/Sketcher_Copy.svg style="width:16px"> [Kopiuj](Szkicownik_Copy/pl.md)**.

Należy pamiętać, że klon klonu staje się kopią szkicu. Jeśli chcesz utworzyć połączone wiązania, sklonuj ponownie oryginalne elementy źródłowe.



## Użycie

1.  Zaznacz elementy szkicu do sklonowania.
2.  kliknij na **[<img src=images/Sketcher_Clone.svg style="width:16px"> [Clone](Sketcher_Clone/pl.md)** or choose **Szkic → Narzędzia szkicownika → [<img src=images/Sketcher_Clone.svg style="width:16px"> Klonuj** z menu głównego.
3.  Przesuń kursor myszki w oknie [widoku 3D](3D_view/pl.md) do pożądanego miejsca dla klona.
    Przez przytrzymanie **Shift**, kąt do punktu lokalizacji może być ustalony w krokach co 5°. {{Version/pl|0.20}}
4.  Kliknij lewym przyciskiem myszki w oknie widoku 3D, aby utworzyć klon.

Nie są dodawane żadne dodatkowe wiązania dla klona.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Clone/pl
