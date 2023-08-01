---
- GuiCommand:/pl
   Name:Std LinkSelectLinkedFinal
   Name/pl:Std: Przejdź do najgłębiej połączonego obiektu
   MenuLocation:brak
   Workbenches:wszystkie
   Version:0.19
   SeeAlso:[Std LinkSelectLinked](Std_LinkSelectLinked.md), [Wybierz wszystkie łącza](Std_LinkSelectAllLinks/pl.md), [Przywróć wybór](Std_SelBack/pl.md), [Ponów wybór](Std_SelForward/pl.md)
---

# Std LinkSelectLinkedFinal/pl



## Opis

Polecenie **Przejdź do najgłębiej połączonego obiektu** wybiera właściwość **Połączony obiekt**, obiektu źródłowego, obiektu [App: Łącze](App_Link/pl.md), czyli link. Ale jeśli ten obiekt źródłowy jest również łączem, zamiast niego wybierany jest obiekt połączony. Powtarza się to do momentu, gdy obiekt powiązany nie jest łączem. Ten końcowy obiekt źródłowy jest najgłębiej połączonym obiektem.



## Użycie

1.  Wybierz łącze.
2.  Z menu podręcznego [Widoku drzewa](Tree_view/pl.md) wybierz opcję **Akcje z łączami → <img src="images/Std_LinkSelectLinkedFinal.svg" width=16px> '''Przejdź do najgłębiej połączonego obiektu'''**.
3.  Połączony obiekt zostanie zaznaczony. Jeśli ten obiekt należy do zewnętrznego dokumentu, dokument ten jest aktywowany.
4.  Opcjonalnie użyj **<img src="images/Std_SelBack.svg" width=16px> [Std SelBack](Std_SelBack/pl.md)**, aby ponownie wybrać łacze.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std LinkSelectLinkedFinal/pl
