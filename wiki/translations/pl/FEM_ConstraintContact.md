---
 GuiCommand:
   Name: FEM ConstraintContact
|Name/pɬMES Kontakt
   MenuLocation: Model , Warunki brzegowe i obciążenia mechaniczne , Kontakt
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_ConstraintFixed/pl
---

# FEM ConstraintContact/pl



## Opis

Tworzy więz kontaktowy między 2 powierzchniami.



## Użycie

1.  Jest kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/FEM_ConstraintContact.svg" width=16px> [Kontakt](FEM_ConstraintContact/pl.md)**.
    -   Wybierz opcję **Model → Warunki brzegowe i obciążenia mechaniczne → <img src="images/FEM_ConstraintContact.svg" width=16px> Kontakt** z menu.
2.  Wybierz powierzchnię master.
3.  Wybierz powierzchnię slave.
4.  Wprowadź sztywność kontaktu.
5.  Wprowadź współczynnik tarcia.



## Ograniczenia

-   Kontakt może być zdefiniowany tylko dla 2 powierzchni.
-   Dyskusja o implementacji wielu kontaktów jednocześnie: <https://forum.freecadweb.org/viewtopic.php?f=18&t=15699&start=130#p303275>
-   Ponieważ nie ma obecnie wsparcia dla wielu siatek, kontakt musi być definiowany dla powierzchni, między którymi jest (co najmniej) niewielka przerwa. Gdyby powierzchnie się stykały (brak przerwy między nimi), rezultatem operacji boolowskiej (koniecznej do uniknięcia wielu siatek, co nie jest obecnie wspierane) byłaby ciągła siatka, więc nie byłoby sensu definiować kontakt. Więcej na ten temat można przeczytać w [wątku na forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=62307).



## Uwagi



### Wskazówki do modelowania 

-   Źródło: <https://forum.freecadweb.org/viewtopic.php?f=18&p=340874#p340494>
-   Zalecane jest używanie elementów liniowych. W innym wypadki, obliczenia mogą być czasochłonne.
-   Przypisanie powierzchni master/slave:
    -   Większa z dwóch powierzchni powinna być wybrana jako master.
    -   Jeśli powierzchnie są zbliżonej wielkości, ta należąca do ciała o większej sztywności powinna być wybrana jako master.
    -   Jeśli powierzchnie są zbliżonej wielkości i sztywności, ta o rzadszej siatce powinna być wybrana jako master.

### CalculiX

-   Sztywność kontaktu można oszacować jako 5 do 50 razy moduł Younga materiału. Im wyższa sztywność kontaktu, tym twardszy kontakt między powierzchniami.
-   Powierzchnia slave może przenikać powierzchnię master, a więc doświadczać większej deformacji.
-   Do definiowania kontaktu w CalculiX używane jest słowo kluczowe \*CONTACT PAIR. W tym przypadku wykorzystywany jest kontakt typu ściana do ściany z funkcją kary (penalty). Sformułowanie kontaktu jest szczegółow opisane na stronie <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node112.html>
-   Przegląd różnych typów kontaktu: <https://forum.freecadweb.org/viewtopic.php?f=18&t=15699&start=90#p188736>
-   Więcej interesujących informacji:
    -   <https://forum.freecadweb.org/viewtopic.php?f=18&t=23102#p180709> i kolejne posty !!!
    -   <https://forum.freecadweb.org/viewtopic.php?f=18&t=20276>
    -   <https://forum.freecadweb.org/viewtopic.php?f=18&t=21331>
    -   <https://forum.freecadweb.org/viewtopic.php?f=18&t=15699> (pierwszy wątek o kontakcie)

-   Bardzo szczegółowy przykład kontaktu w CalculiX. ([link](http://dip28p.web.fc2.com/calculix/netgen2calculix/index.html))

-   Ciekawy przykład znaleziony na niemieckim forum programu FreeCAD. ([link](https://forum.freecadweb.org/viewtopic.php?f=13&t=39663&start=10#p337254))





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintContact/pl
