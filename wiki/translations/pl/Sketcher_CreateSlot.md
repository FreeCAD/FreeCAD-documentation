---
 GuiCommand:
   Name: Sketcher CreateSlot
   Name/pl: Szkicownik: Utwórz owal
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Utwórz owal
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **S**
   SeeAlso: Sketcher_CreateArcSlot/pl
---

# Sketcher CreateSlot/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:24px;"> **Utwórz owal** tworzy szczelinę, zamkniętą polilinię składającą się z dwóch półkoli połączonych dwiema równoległymi liniami prostymi.

![](images/SketcherCreateSlotExample.png‎ )



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

Pos-OVP = Pozycyjne [Parametry w widoku](Sketcher_Preferences#Ogólne/pl.md). {{Version/pl|1.0}}
Dim-OVP = Wymiarowe parametry w widoku. {{Version/pl|1.0}}

1.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_CreateSlot.svg" width=16px> Utwórz szczelinę**.
    -   Wybierz z menu opcję **Szkic → Elementy geometryczne szkicownika → <img src="images/Sketcher_CreateSlot.svg" width=16px> Utwórz szczelinę**.
    -   Skrót klawiaturowy: **G**, a następnie **S**.
2.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
3.  Wybierz środek pierwszego półkola. Lub za pomocą Pos-OVP: wprowadź jego współrzędne X i / lub Y.
4.  Wybierz środek drugiego półkola. Lub za pomocą Dim-OVP: wprowadź odległość między środkami i / lub kąt szczeliny. Kąt odnosi się do osi X szkicu.
5.  Wybierz punkt, aby zdefiniować promień szczeliny. Lub za pomocą Dim-OVP: wprowadź ten promień.
6.  Szczelina jest tworzona i dodawane są odpowiednie wiązania oparte na Pos-OVP i Dim-OVP.
7.  Jeśli narzędzie działa w [trybie kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md):
    1.  Opcjonalnie kontynuuj tworzenie szczelin.
    2.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



## Uwagi

-    {{VersionMinus/pl|0.21}}*({{Version/pl|0.20}})*: Przytrzymanie **Ctrl** podczas wybierania drugiego środka ograniczy rysowanie szczeliny w poziomie lub w pionie.

-    {{Version/pl|1.0}}: [Przyciąganie do kąta](Sketcher_Snap/pl.md) może być używane do kontrolowania kąta szczeliny.

-    {{Version/pl|0.20}}: Szczelina może być również ograniczona poziomo lub pionowo, jeśli włączona jest opcja [Wiązania automatyczne](Sketcher_Workbench/pl#Wiązania_automatyczne.md).





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateSlot/pl
