---
 GuiCommand:
   Name: Std BoxElementSelection
   Name/pl: Std: Wybór elementów ramką zaznaczenia
   MenuLocation: Edycja , Wybór elementów ramką zaznaczenia
   Workbenches: Wszystkie
   Shortcut: **Shift** + **E**
   SeeAlso: Part_BoxSelection/pl,Std_BoxSelection/pl, Std_SelectAll/pl
---

# Std BoxElementSelection/pl



## Opis

Polecenie **Wybór elementów ramką zaznaczenia** wybiera ściany z prostokątnego obszaru zdefiniowanego przez użytkownika za pomocą ramki zaznaczenia, w oknie [widoku 3D](3D_view/pl.md).

Zauważ, że jeśli cały obiekt mieści się w prostokącie, sam obiekt zostanie zaznaczony zamiast jego ścian. Aby tego uniknąć utwórz dwa zaznaczenia prostokątem dla każdego obiektu (przytrzymaj klawisz **Ctrl** podczas przeciągania drugiego prostokąta) lub skorzystaj z polecenia [Część: Zaznacz obszarem](Part_BoxSelection/pl.md) zamiast tego.



## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Wybierz z menu opcję **Edycja → <img src="images/Std_BoxElementSelection.svg" width=16px> Wybór elementów ramką zaznaczenia**.
    -   Użyj skrótu klawiaturowego: **Shift** + **E**.
2.  Wykonaj jedną z poniższych czynności:
    -   Przeciągnij ramkę zaznaczenia od lewej do prawej, aby zaznaczyć ściany, których środek geometryczny leży wewnątrz tego pola.
    -   Przeciągnij ramkę zaznaczenia od prawej do lewej, aby zaznaczyć ściany, które znajdują się *(częściowo)* wewnątrz tego pola lub są przez nie dotykane.



## Uwagi

-   Użyj polecenia [Zaznacz obszar](Std_BoxSelection/pl.md), aby wybrać obiekty zamiast ścian.
-   Tego polecenia nie można użyć do wybrania elementów w szkicu. Zobacz [Szkicownik](Sketcher_Workbench/pl#Metody_zaznaczenia.md).





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std BoxElementSelection/pl
