---
- GuiCommand:/fr
   Name:Draft Join
   Name/fr:Draft Joindre
   MenuLocation:Modification → Joindre
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**J** **O**
   Version:0.18
   SeeAlso:[Draft Fractionner](Draft_Split/fr.md)
---

# Draft Join/fr

## Description

La commande <img alt="" src=images/Draft_Join.svg  style="width:24px;"> **Draft Joindre** permet de joindre [Draft Lignes](Draft_Line/fr.md) et [Draft Polylignes](Draft_Wire/fr.md) en une seule ligne. Cette commande est la contrepartie de la commande [Draft Scinder](Draft_Split/fr.md).

## Utilisation

1.  Les points d\'extrémité des [Draft Lignes](Draft_Line/fr.md) et/ou [Draft Polylignes](Draft_Wire/fr.md) à joindre doivent coïncider exactement. Si nécessaire, ajustez d\'abord les points pour vous assurer que c\'est le cas.
2.  Sélectionnez deux ou plusieurs [Draft Lignes](Draft_Line/fr.md) et/ou [Draft Polylignes](Draft_Wire/fr.md).
3.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Join.svg" width=16px> [Joint les lignes sélectionnées...](Draft_Join/fr.md)**.
    -   Sélectionnez l\'option **Modification → <img src="images/Draft_Join.svg" width=16px> Joindre** dans le menu.
    -   Utilisez le raccourci clavier : **J** puis **O**.

## Remarques

-   Les [Draft Lignes](Draft_Line/fr.md) et [Draft Polylignes](Draft_Wire/fr.md) peuvent aussi être jointes avec la commande [Draft Polyligne](Draft_Wire/fr.md) ou la commande [Draft Mettre à niveau](Draft_Upgrade/fr.md).
-   Pour réunir des objets qui ne sont pas [Draft Lignes](Draft_Line/fr.md) ou [Draft Polylignes](Draft_Wire/fr.md), vous pouvez essayer d\'utiliser [Draft Mettre à niveau](Draft_Upgrade/fr.md) et/ou [Draft Rétrograder](Draft_Downgrade/fr.md) sur eux une ou plusieurs fois d\'abord.

## Script

Voir aussi: _.

Pour réunir des lignes, utilisez la méthode `join_wires` ({{Version/fr|0.19}}) de l\'atelier Draft. Cette méthode remplace la méthode dépréciée `joinWires`. Cette méthode renvoie `None`.


```python
join_wires(wires)
```

-    `fils`est une liste d\'objets lignes à joindre.

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(500, 0, 0)
p3 = App.Vector(500, 500, 0)
p4 = App.Vector(0, 500, 0)

wire1 = Draft.make_wire([p1, p2])
wire2 = Draft.make_wire([p2, p3])
wire3 = Draft.make_wire([p3, p4])
wire4 = Draft.make_wire([p4, p1])

Draft.join_wires([wire1, wire3, wire2, wire4])
doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Join/fr
