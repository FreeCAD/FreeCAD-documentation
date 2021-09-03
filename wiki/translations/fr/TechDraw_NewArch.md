---
- GuiCommand:/fr
   Name:TechDraw ArchView
   Name/fr:TechDraw Vue Arch
   MenuLocation:TechDraw → Insérer un objet de l'atelier Arch
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md), [Atelier Arch](Arch_Workbench/fr.md)
   SeeAlso:[Arch Plan de section](Arch_SectionPlane/fr.md)
---

## Description

L\'outil Vue Arch insère une vue d\'un **<img src="images/Arch_SectionPlane.svg" width=16px> [Arch Plan de section](Arch_SectionPlane/fr.md)** dans une [TechDraw Page](TechDraw_PageDefault/fr.md).

![](images/TechDraw_Arch_example.jpg )

## Utilisation

1.  Sélectionnez un plan de section Arch dans la vue 3D ou dans l\'arborescence
2.  Si vous avez plusieurs pages de dessin dans votre document, vous devrez sélectionner la page désirée dans l\'arborescence.
3.  Appuyez sur le bouton **<img src="images/TechDraw_ArchView.svg" width=24px> [Insérer une vue d'un plan de coupe à partir de l'atelier Arch](TechDraw_ArchView/fr.md)
**
4.  Une vue des objets vus par le plan de coupe apparaîtra sur la page.

### Limitations

La Vue Arch est générée dans l\'[atelier Arch](Arch_Workbench/fr.md) et donc TechDraw a un contrôle limité sur son apparence. Vous devrez peut-être apporter des modifications dans Arch pour obtenir la représentation souhaitée.

## Options

-   La Vue Arch est générée par l\'[atelier Arch](Arch_Workbench/fr.md) de la même manière que dans l\'[atelier Drawing](Drawing_Workbench/fr.md). Voir les Remarques.
-   [Draft Accrochage Dimensions](Draft_Snap_Dimensions/fr.md), [Draft Texte](Draft_Text/fr.md) et tout autre objet 2D (Sketch ou Draft) pris en compte par le plan de section est généré \"tel quel\" (pas d\'intersection ni de lignes cachées) par dessus la géométrie solide.
-   Le volume de [Arch Espace](Arch_Space/fr.md) n\'est pas généré, seule l\'étiquette sera crée.
-   Les lignes de coupe, les lignes projetées (si la propriété Show Hidden est définie à True) et les lignes 2D ci-dessus peuvent être générées avec différentes largeurs de ligne. Cela peut être configuré dans les préférences Arch.
-   La Vue Arch a deux modes de rendu: Filaire qui utilise les algorithmes OpenCasCade de l\'[atelier Drawing](Drawing_Workbench/fr.md) et est rapide et ne produit que des lignes (pas de remplissage de face possible), et Solide qui est basé sur l\'[algorithme du peintre](https://fr.wikipedia.org/wiki/Algorithme_du_peintre) et est capable de rendre des surfaces remplies avec leur couleur de forme. Cependant, il est beaucoup plus lent et peut échouer dans de nombreuses situations. L\'image ci-dessous illustre la différence entre les deux modes de rendu:

![](images/TechDraw_Arch_rendering.jpg )

-   Seule la ligne de base des [Arch Tuyaux](Arch_Pipe/fr.md) est générée, pas le volume total des tubes:

![](images/TechDraw_Arch_piping.jpg )

## Propriétés

-    {{PropertyData/fr|Source}}: l\'objet du plan de section à afficher

-    {{PropertyData/fr|All On}}: si les objets cachés doivent être affichés ou non. Si Faux, seuls les objets visibles dans la vue 3D sont rendus

-    {{PropertyData/fr|Mode de rendu}}: le mode de rendu à utiliser, solide ou filaire

-    {{PropertyData/fr|Show Hidden}}: si la géométrie cachée (la partie de la goémétrie qui se trouve derrière le plan de section) est affichée ou non. Il sera rendu en ligne pointillée, qui peut être configuré dans les préférences Arch.

-    {{PropertyData/fr|Show Fill}}: si les zones coupées doivent être remplies de couleur grise ou non

-    {{PropertyData/fr|Line Width}}: la largeur des lignes principales. Les rapports de lignes de coupe et de largeur de ligne projetée/2D peuvent être configurés dans les préférences Arch

-    {{PropertyData/fr|Font Size}}: la taille de tous les textes qui apparaissent dans cette vue

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil New Arch peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
dv = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewArch','TestArch')
dv.Source = mySectionPlane
rc = page.addView(dv)
```





{{TechDraw Tools navi

}}  
