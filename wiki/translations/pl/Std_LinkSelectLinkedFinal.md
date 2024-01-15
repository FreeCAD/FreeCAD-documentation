---
 GuiCommand:
   Name: Std LinkSelectLinkedFinal
   Name/pl: Std: Przejdź do najgłębiej połączonego obiektu
   MenuLocation: Widok , Nawigacja przy użyciu łączy , Przejdź do najgłębiej połączonego obiektu
   Workbenches: wszystkie
   Version: 0.19
   SeeAlso: Std_LinkSelectLinked/pl, Std_LinkSelectAllLinks/pl
---

# Std LinkSelectLinkedFinal/pl



## Opis

Polecenie **Przejdź do najgłębiej połączonego obiektu** wybiera właściwość **Połączony obiekt**, obiektu źródłowego, obiektu [App: Łącze](App_Link/pl.md), czyli link. Ale jeśli ten obiekt źródłowy jest również łączem, zamiast niego wybierany jest obiekt połączony. Powtarza się to do momentu, gdy obiekt powiązany nie jest łączem. Ten końcowy obiekt źródłowy jest najgłębiej połączonym obiektem.



## Użycie

1.  Wybierz łącze.
2.  Istnieje kilka sposobów wywołania polecenia:
    -   Wybierz z menu opcję **Widok → Nawigacja łączami → <img src="images/Std_LinkSelectLinkedFinal.svg" width=16px> Przejdź do najgłębiej połączonego obiektu**.
    -   Wybierz z menu opcję **Akcje z łączami → <img src="images/Std_LinkSelectLinkedFinal.svg" width=16px> Przejdź do najgłębiej połączonego obiektu** z menu kontekstowego [Widoku drzewa](Tree_view/pl.md).
    -   Użyj skrótu klawiaturowego: **S**, a następnie **D**.
3.  Wybrany zostanie najgłębiej powiązany obiekt. Jeśli ten obiekt należy do zewnętrznego dokumentu, dokument ten jest aktywowany.
4.  Opcjonalnie można użyć funkcji <img alt="" src=images/Std_SelBack.svg  style="width:16px;"> [Przywróć zaznaczenie](Std_SelBack/pl.md), aby ponownie wybrać link.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std LinkSelectLinkedFinal/pl
