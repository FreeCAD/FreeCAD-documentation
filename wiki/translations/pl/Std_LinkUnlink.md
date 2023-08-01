---
- GuiCommand:
   Name:Std LinkUnlink
   Name/pl:Std: Usuń powiązanie
   MenuLocation:brak
   Workbenches:wszystkie
   Version:0.19
   SeeAlso:[Utwórz łącze](Std_LinkMake/pl.md), [Utwórz łącze względne](Std_LinkMakeRelative/pl.md), [Zastąp przez łącze](Std_LinkReplace/pl.md)
---

# Std LinkUnlink/pl



## Opis


**[<img src=images/Std_LinkUnlink.svg style="width:16px"> '''Usuń powiązanie'''**

jest zasadniczo operacją odwrotną do **[<img src=images/Std_LinkReplace.svg style="width:16px"> [Zastąp przez łącze](Std_LinkReplace/pl.md)**.

Ta operacja jest używana do usunięcia linku z kontenera, takiego jak **[<img src=images/Std_Part.svg style="width:16px"> [Część](Std_Part/pl.md)**, a zamiast niego umieszcza właściwy obiekt.



## Użycie

1.  Upewnij się, że masz Łącze, które znajduje się wewnątrz kontenera, na przykład Łącze do **[<img src=images/Part_Sphere.svg style="width:16px"> [Sfery](Part_Sphere/pl.md)** wewnątrz **[<img src=images/Std_Part.svg style="width:16px"> [Części](Std_Part/pl.md)**.
2.  Wybierz wewnętrzne Łącze w [widoku drzewa](Tree_view/pl.md).
3.  Naciśnij **[<img src=images/Std_LinkUnlink.svg style="width:16px"> [Usuń powiązanie](Std_LinkUnlink/pl.md)**.

Oryginalna <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:16px;"> [sfera](Part_Sphere/pl.md) musi teraz znajdować się wewnątrz **[<img src=images/Std_Part.svg style="width:16px"> [Części](Std_Part/pl.md)**, a Łącze musi znajdować się na zewnątrz. Teraz to łącze można usunąć, jeśli nie jest już potrzebne, i nie spowoduje to uszkodzenia kontenera.

![](images/Std_Link_tree_replace_1_example.png ) ![](images/Std_Link_tree_unlink_1_example.png )



*Łącze wewnątrz innego obiektu jest odłączane, a zamiast niego umieszczany jest prawdziwy obiekt.*

![](images/Std_Link_tree_replace_2_example.png ) ![](images/Std_Link_tree_unlink_2_example.png )



*Łącze wewnątrz grupy jest odłączane, a zamiast niego umieszczany jest rzeczywisty obiekt.*





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std LinkUnlink/pl
