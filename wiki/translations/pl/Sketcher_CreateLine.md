---
 GuiCommand:
   Name: Sketcher CreateLine
   Name/pl: Szkicownik: Utwórz linię
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Utwórz linię
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **L**
   SeeAlso: Sketcher_CreatePolyline/pl
---

# Sketcher CreateLine/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_CreateLine.svg  style="width:24px;"> **Utwórz linię** tworzy linię. {{Version/pl|1.0}}: Jeśli [parametry wyświetlane w widoku](Sketcher_Preferences/pl#Ogólne.md) są włączone, narzędzie ma trzy tryby.

![](images/Sketcher_LineExample1.png‎ )



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

Pos-OVP = Pozycyjne [Parametry w widoku](Sketcher_Preferences#Ogólne/pl.md). {{Version/pl|1.0}}
Dim-OVP = Wymiarowe parametry w widoku. {{Version/pl|1.0}}

1.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_CreateLine.svg" width=16px> '''Utwórz linię'''**.
    -   Wybierz z menu opcję **Szkic → Elementy geometryczne szkicownika → <img src="images/Sketcher_CreateLine.svg" width=16px> Utwórz linię**.
    -   Użyj skrótu klawiaturowego: **G**, a następnie **L**.
2.  Kursor zmieni się w krzyżyk z ikoną bieżącego trybu narzędzia.
3.  Jeśli [parametry wyświetlane w widoku](Sketcher_Preferences/pl#Ogólne.md) są włączone, sekcja **Parametry linii** ({{Version/pl|1.0}}) jest dodawana na górze [okna dialogowego](Sketcher_Dialog/pl.md).
4.  Opcjonalnie naciśnij klawisz **M** lub wybierz z rozwijanej listy w sekcji parametrów, aby zmienić tryb narzędzia:
    -   <img alt="" src=images/Sketcher_CreateLineAngleLength.svg  style="width:16px;"> **Punkt, długość, kąt**: {{Version/pl|1.0}}.
        1.  Wybierz punkt początkowy linii. Lub z Pos-OVP: wprowadź jego współrzędne X i / lub Y.
        2.  Wybierz punkt końcowy linii. Lub z Dim-OVP: wprowadź długość i / lub kąt linii. Kąt odnosi się do osi X szkicu.
    -   <img alt="" src=images/Sketcher_CreateLineLengthWidth.svg  style="width:16px;"> **Punkt, szerokość, wysokość**: {{Version/pl|1.0}}.
        1.  Wybierz punkt początkowy linii. Lub za pomocą Pos-OVP: wprowadź jego współrzędne X i / lub Y.
        2.  Wybierz punkt końcowy linii. Lub za pomocą Dim-OVP: wprowadź jego odległość X i / lub Y od punktu początkowego.
    -   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:16px;"> **Dwa punkty**:
        1.  Wybierz punkt początkowy linii. Lub za pomocą Pos-OVP: wprowadź jego współrzędne X i / lub Y.
        2.  Wybierz punkt końcowy linii. Lub za pomocą Pos-OVP: wprowadź jego współrzędną X i / lub Y.
5.  Linia jest tworzona i dodawane są odpowiednie ograniczenia oparte na Pos-OVP i Dim-OVP.
6.  Jeśli narzędzie działa w [trybie kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md):
    1.  Opcjonalnie kontynuuj tworzenie linii.
    2.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateLine/pl
