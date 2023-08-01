---
- GuiCommand:
   Name: Sketcher ConstrainRadiam
   Name/pl: Szkicownik: Zwiąż automatycznie promień / średnicę
   MenuLocation: Szkic - Wiązania szkicownika - Zwiąż automatycznie promień / średnicę
   Workbenches: [Szkicownik](Sketcher_Workbench/pl.md),
   Shortcut: **K** **S**
   Version: 0.20
   SeeAlso: [Wiązanie odległości](Sketcher_ConstrainDistance/pl.md), [Zwiąż w poziomie](Sketcher_ConstrainDistanceX/pl.md), [Zwiąż w pionie](Sketcher_ConstrainDistanceY/pl.md)
---

# Sketcher ConstrainRadiam/pl



## Opis

Więz ten automatycznie ustala, że wartość promienia / średnicy okręgu lub łuku będzie miała określoną wartość. Stosowane są następujące zasady:

-   Jeśli obiekt jest biegunem krzywej złożonej, dodawane jest wiązanie wagi.
-   Jeśli obiekt jest pełnym kołem, dodawane jest wiązanie średnicy.
-   W innych przypadkach *(zazwyczaj łuk)* dodawane jest wiązanie promienia.

Jeśli przed uruchomieniem polecenia wybrano więcej niż jeden okrąg lub łuk :

-   Jeśli wiązanie jest stosowane w trybie *Informacyjnym*, nowe wiązanie informacyjne jest dodawane do każdego obiektu osobno zgodnie z powyższymi zasadami.
-   Jeśli polecenie jest stosowane w trybie *Konstrukcji*, stosowane są następujące zasady.
    -   Wiązanie informacyjne jest stosowane oddzielnie na każdym obiekcie, który jest zewnętrzną geometrią

    -   
        **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Wiązania równości](Sketcher_ConstrainEqual/pl.md)**
        
        są stosowane kolejno pomiędzy wszystkimi obiektami geometrii rzeczywistej / konstrukcyjnej, a wiązanie wymiarowe jest stosowane do pierwszego wybranego obiektu zgodnie z powyższymi zasadami.

Uwaga: Bieguny krzywej złożonej nie mogą być mieszane z innymi typami obiektów w wyborze.



## Użycie

1.  Wybierz jeden lub więcej okręgów lub łuków.
2.  Naciśnij przycisk **[<img src=images/Sketcher_ConstrainRadiam.svg style="width:16px"> [Zwiąż automatycznie promień / średnicę](Sketcher_ConstrainRadiam/pl.md)**.
3.  Otworzy się okno dialogowe, w którym można edytować lub potwierdzić wartość. Naciśnij **OK**, aby zatwierdzić.
4.  Opcjonalnie etykieta wymiaru i linia mogą być przesuwane i obracane w oknie widoku 3D poprzez kliknięcie na wartość i przeciąganie przy wciśniętym lewym przycisku myszy.

**Uwaga:** Narzędzie wiązania może być również uruchomione bez wcześniejszego zaznaczenia obiektu. Domyślnie polecenie będzie w trybie kontynuacji, aby utworzyć nowe wiązanie. Naciśnij prawy przycisk myszy lub klawisz **Esc** raz, aby zakończyć wykonywanie polecenia.



## Tworzenie skryptów 

Nie ma zastosowania żaden konkretny skrypt. Zobacz stronę [skrypty szkicownika](Sketcher_scripting/pl.md), opisującą wartości, które mogą być używane dla `ArcOrCircle` i `Circle`, i zawiera dalsze przykłady, jak tworzyć wiązania przy użyciu skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadiam/pl
