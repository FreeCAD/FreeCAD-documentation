---
- GuiCommand:/fr
   Name:Curves Pipeshell
   Name/fr:Curves Enveloppe de tube
   MenuLocation:Surfaces → Pipeshell 
   Workbenches:[Curves](Curves_Workbench/fr.md)
---

# Curves Pipeshell/fr

## Description

<img alt="" src=images/Curves_Pipeshell.svg  style="width:24px;"> [Enveloppe de tube](Curves_Pipeshell/fr.md) crée un objet de balayage pour former une enveloppe de tube. Cet outil fait partie des [ateliers externes](External_workbenches/fr.md) appelés [Curves](Curves_Workbench/fr.md).

## Utilisation

1.  Passer à l\'atelier <img alt="" src=images/Curves_workbench_icon.svg  style="width:24px;"> [Curves](Curves_Workbench/fr.md) (à installer à partir du <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md) si ce n\'est pas déjà fait)
2.  Sélectionnez l\'arête qui crée le chemin de balayage dans la [vue 3D](3D_view/fr.md)
3.  Sélectionnez un ou plusieurs profils requis dans la [vue en arborescence](Tree_view/fr.md)
4.  Pour appeler la commande, effectuez l\'une des opérations suivantes :
    -   Appuyez sur le bouton <img alt="" src=images/Curves_Pipeshell.svg  style="width:24px;"> [Creates a Pipeshell sweep object](Curves_Pipeshell/fr.md) dans la barre d\'outils
    -   Utilisez le **Surfaces → Pipeshell**
5.  Modifiez le paramètre `Pipeshell` aux conditions requises

## Propriétés

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Placement}}: [Placement](Placement/fr.md) est l\'emplacement et l\'orientation d\'un objet dans l\'espace.

-    {{PropertyData/fr|Label}}: nom d\'utilisateur de l\'objet dans [vue en arborescence](tree_view/fr.md).


{{Properties_Title|Main}}

-    {{PropertyData/fr|Mode}}: La valeur par défaut est **Frenet**. Le mode est utilisé pour sélectionner l\'algorithme de balayage. Choix: Frenet, DiscreteTrihedron, FixedTrihetron, Binormal, ShapeSupport, AuxiliarySpine.

-    {{PropertyData/fr|Output}}: La valeur par défaut est **Surface**. La sortie détermine la forme de l\'objet. Choix: Surface, Sections, Lofted Sections.

-    {{PropertyData/fr|Profile}}: Liste des profils utilisés.

-    {{PropertyData/fr|Spine}}:


{{Properties_Title|Mode}}

-    {{PropertyData/fr|Auxiliary}}:

-    {{PropertyData/fr|Contact}}:

-    {{PropertyData/fr|Corrected}}:

-    {{PropertyData/fr|Direction}}:

-    {{PropertyData/fr|Equi Curvi}}:

-    {{PropertyData/fr|Location}}:

-    {{PropertyData/fr|Support}}:


{{Properties_Title|Settings}}

-    {{PropertyData/fr|Max Degree}}:

-    {{PropertyData/fr|Max Segments}}:

-    {{PropertyData/fr|Samples}}:

-    {{PropertyData/fr|Solid}}: par défaut **False**

-    {{PropertyData/fr|Tol3d}}: par défaut **0.00**.

-    {{PropertyData/fr|Tol Ang}}: par défaut **0.00**.

-    {{PropertyData/fr|Tol Bound}}: par défaut **0.00**.

## Remarques

-    **Pipeshell**a besoin d\'un objet filaire (comme chemin de balayage) et d\'au moins un **Pipeshell Profile**.

-   Les deux outils **Pipeshell** et **Pipeshell Profile** fonctionnent ensemble comme un outil de balayage \"avancé\".

## Limitations

## Script





{{Curves Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Curves](Category_Curves.md) > Curves Pipeshell/fr
