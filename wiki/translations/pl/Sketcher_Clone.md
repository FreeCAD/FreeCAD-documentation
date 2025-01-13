---
 GuiCommand:
   Name: Sketcher Clone
   Name/pl: Szkicownik: Klonuj
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Klonuj
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **Z** **L**
   Version: 0.16
   SeeAlso: Sketcher_Copy/pl, Sketcher_Move/pl
---

# Sketcher Clone/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_Clone.svg  style="width:16px;"> Klonuj, klonuje wybrane elementy szkicu z jednego punktu do drugiego, używając ostatnio wybranego punktu jako odniesienia. Jeśli jakiekolwiek wiązania są częścią elementów źródłowych, to nowe wiązania są powiązane z wiązaniami źródłowymi. Jeśli wiązania w źródle zostaną zmienione, to wiązania w klonie również zostaną zmienione. Aby uniknąć tego powiązania zobacz opis narzędzia **[<img src=images/Sketcher_Copy.svg style="width:16px"> [Kopiuj](Szkicownik_Copy/pl.md)**.

Należy pamiętać, że klon klonu staje się kopią szkicu. Jeśli chcesz utworzyć połączone wiązania, sklonuj ponownie oryginalne elementy źródłowe.



## Użycie

1.  Zaznacz elementy szkicu do sklonowania.




1.  Istnieje kilka sposobów wywołania polecenia:
    -   Naciśnij przycisk **<img src="images/Sketcher_Clone.svg" width=16px> '''Klonuj'''**.
    -   Wybierz z menu opcję **Szkic → Narzędzia szkicownika → [<img src=images/Sketcher_Clone.svg style="width:16px"> Klonuj** z menu głównego.
    -   Skrót klawiaturowy: **Z**, a następnie **L**.
2.  Przesuń kursor myszki w oknie [widoku 3D](3D_view/pl.md) do pożądanego miejsca dla klona.
    Przez przytrzymanie **Shift**, kąt do punktu lokalizacji może być ustalony w krokach co 5°. {{Version/pl|0.20}}
3.  Kliknij lewym przyciskiem myszki w oknie widoku 3D, aby utworzyć klon.

Nie są dodawane żadne dodatkowe wiązania dla klona.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Clone/pl
