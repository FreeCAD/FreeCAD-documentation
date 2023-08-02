---
- GuiCommand:
   Name: Std LinkReplace
   Name/pl: Std: Zastąp przez łącze
   MenuLocation: brak
   Workbenches: wszystkie
   Version: 0.19
   SeeAlso: Std_LinkMake/pl, Std_LinkMakeRelative/pl, Std_LinkUnlink/pl
---

# Std LinkReplace/pl



## Opis

Narzędzie **[<img src=images/Std_LinkReplace.svg style="width:16px"> '''Zastąp przez łącze'''** zastępuje obiekt znajdujący się wewnątrz innego na wersję [łącza](App_Link/pl.md) do tego pierwszego.

Operacja ta działa na \"dzieciach\" obiektu \"rodzica\", tak jak jest to widoczne w oknie [widoku drzewa](Tree_view/pl.md). Na przykład, biorąc pod uwagę dwa obiekty *(A i B)*, które uczestniczą w operacji C = A + B, obiekt A może zostać zastąpiony przez łącze, tak że C = A_link + B.

Operacja ta może być wykonana w celu zastąpienia zagnieżdżonych obiektów, które znajdują się w obiekcie [złożenia](Assembly/pl.md) dla Łącza, co może być bardziej wydajne, jeśli ten zagnieżdżony obiekt jest używany wiele razy w różnych złożeniach. Operacją odwrotną jest **[<img src=images/Std_LinkUnlink.svg style="width:16px"> [Usuń powiązanie](Std_LinkUnlink/pl.md)**. Aby utworzyć ogólne łącze użyj funkcji **[<img src=images/Std_LinkMake.svg style="width:16px"> [Utwórz łącze](Std_LinkMake/pl.md)**.



## Użycie

1.  Upewnij się, że jeden obiekt znajduje się wewnątrz innego. Na przykład, rozważmy, że obiekt **[<img src=images/Part_Fuse.svg style="width:16px"> [scalenia](Part_Fuse/pl.md)** został użyty z dwoma wcześniej utworzonymi obiektami, **[<img src=images/Part_Sphere.svg style="width:16px"> [sfera](Part_Sphere/pl.md)** i **[<img src=images/Part_Cylinder.svg style="width:16px"> [walec](Part_Cylinder/pl.md)**.
2.  Wybierz <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:16px;"> [sferę](Part_Sphere.md) w oknie [Widoku drzewa](Tree_view/pl.md).
3.  Naciśnij **[<img src=images/Std_LinkReplace.svg style="width:16px"> [Zastąp przez łącze](Std_LinkReplace/pl.md)**.

Oryginalna <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:16px;"> [sfera](Part_Sphere/pl.md) musi teraz znajdować się poza obiektem **[<img src=images/Part_Fuse.svg style="width:16px"> [scalenia](Part_Fuse/pl.md)**, a wewnątrz musi znajdować się Łącze *(na ikonie wyświetlana jest mała strzałka)*.

![](images/Std_Link_tree_replace_fuse_1_example.png ) ![](images/Std_Link_tree_replace_fuse_2_example.png )



*Obiekt znajdujący się wewnątrz innego jest zastępowany przez Łącze. Łącze znajduje się teraz wewnątrz, a prawdziwy obiekt jest umieszczony na zewnątrz.*

Można to również zrobić z obiektami zawartymi wewnątrz obiektu {{button|[<img src=images/Std_Part.svg style="width:16px"> [części](Std_Part/pl.md)}} i {{button|[<img src=images/Std_Group.svg style="width:16px"> [grupy](Std_Group/pl.md)}}.

![](images/Std_Link_tree_replace_part_1_examples.png ) ![](images/Std_Link_tree_replace_part_2_examples.png )



*Obiekt wewnątrz kontenera jest zastępowany przez łącze. Łącze znajduje się teraz wewnątrz, a prawdziwy obiekt jest umieszczony na zewnątrz.*



## Właściwości

Polecenie to tworzy nowy obiekt [App: Łącze](App_Link/pl.md). Jego właściwości opisane są na stronie **[<img src=images/Std_LinkMake.svg style="width:16px"> [Utwórz łącze](Std_LinkMake/pl#Właściwości.md)**.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std LinkReplace/pl
