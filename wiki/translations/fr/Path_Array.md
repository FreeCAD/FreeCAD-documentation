---
- GuiCommand:/fr
   Name:Path Array
   Name/fr:Path Réseau
   MenuLocation:Path → Path Modification → Réseau
   Workbenches:[Path](Path_Workbench/fr.md)
---

# Path Array/fr

## Description

Cet outil crée un nouveau chemin en duplicant un autre chemin plusieurs fois avec un intervale donné.

## Utilisation

1.  Sélectionnez l\'opération que vous souhaitez répéter
2.  Pressez le bouton **<img src="images/Path_Array.svg" width=24px> [Réseau](Path_Array/fr.md)
**
3.  Pressez **Apply**
4.  Ajustez les propriétés souhaitées dans la boîte de dialogue des données

## Propriétés

-    {{PropertyData/fr|Type}}: Le type de réseau (polaire, linéaire dans une ou deux directions)

-    {{PropertyData/fr|Offset}}: L\'espace entre les copies du réseau pour chaque direction

-    {{PropertyData/fr|Copies}}: Le nombre de copies (sans compter l\'original) pour chaque direction

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
[documentation index](../README.md) > [Path](Path_Workbench.md) > Path Array/fr
