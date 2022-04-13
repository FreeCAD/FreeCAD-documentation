---
- GuiCommand:/fr
   Name:Path Array
   Name/fr:Path Réseau
   MenuLocation:Path → Modification du parcours → Réseau
   Workbenches:[Path](Path_Workbench/fr.md)
---

# Path Array/fr

## Description

Cet outil crée un nouveau parcours en duplicant un autre parcours plusieurs fois avec un intervale donné.

## Utilisation

1.  Sélectionnez l\'opération que vous souhaitez répéter
2.  Pressez le bouton **<img src="images/Path_Array.svg" width=24px> [Réseau](Path_Array/fr.md)
**
3.  Pressez **Appliquer**
4.  Ajustez les propriétés souhaitées dans la boîte de dialogue des données

## Propriétés

-    **Type**: Le type de réseau (polaire, linéaire dans une ou deux directions)

-    **Offset**: L\'espace entre les copies du réseau pour chaque direction

-    **Copies**: Le nombre de copies (sans compter l\'original) pour chaque direction

## Limitations

Cette fonction ne fonctionne que sur les opérations de trajectoire réelles, et non sur les trajectoires dérivées produites par Path Dressups. Dans ce cas, l\'icône Array est désactivée.

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Exemple :


```python
#Place code example here.
```





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Array/fr
