---
- GuiCommand:/pl
   Name:Part CrossSections
   Name/pl:Część: Przekrój poprzeczny
   MenuLocation:Część → Przekrój poprzeczny ...
   Workbenches:[Część](Part_Workbench/pl.md)
   SeeAlso:[Przekrój](Part_Section/pl.md)
---

# Part CrossSections/pl



## Opis

Narzędzie **Przekrój poprzeczny** tworzy jeden lub więcej przekrojów przez wybrany kształt, równolegle do jednej z domyślnych płaszczyzn globalnych *(XY, XZ lub YZ)*.



## Użycie

1.  Wybierz kształt.
2.  Naciśnij przycisk **[24px|link=Part_CrossSections](File:Part_CrossSections.svg.md) '''Przekrój'''**.
3.  Zdefiniuj płaszczyznę prowadzącą.
4.  Zdefiniuj położenie *(wysokość przekroju)*.
5.  Opcjonalnie zaznacz opcję **Przekroje**, aby utworzyć więcej niż jeden przekrój:
    -   Zaznaczenie opcji **Po obu stronach** spowoduje rozmieszczenie przekrojów po każdej stronie położenia płaszczyzny prowadzącej.
    -   Ustaw liczbę.
6.  Naciśnij **OK**.



## Uwagi

-   Obiekty [App: Łącze](App_Link/pl.md) powiązane z odpowiednimi typami obiektów i kontenery [App: Część](App_Part/pl.md) z odpowiednimi widocznymi obiektami wewnątrz mogą być również używane jako obiekty źródłowe. {{Version/pl|0.20}}
-   Obiekt wynikowy nie jest parametryczny, tzn. nie jest powiązany z oryginalnym kształtem.
-   Tworzony jest pojedynczy obiekt, nawet z więcej niż jednym przekrojem.



## Przykład

![Zaznacz obiekt](images/SectionCross1.png )

![Okienko dialogowe](images/SectionCross2.png )

![Rezultat](images/SectionCross3.png )



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CrossSections/pl
