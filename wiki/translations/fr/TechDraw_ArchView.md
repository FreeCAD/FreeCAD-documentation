---
 GuiCommand:
   Name: TechDraw ArchView
   Name/fr: TechDraw Vue d'un objet Arch
   MenuLocation: TechDraw , Vues des autres ateliers , Insérer un objet de l'atelier BIM
   Workbenches: TechDraw_Workbench/fr, BIM_Workbench/fr
   SeeAlso: Arch_SectionPlane/fr
---

# TechDraw ArchView/fr

## Description

L\'outil **TechDraw Vue d\'un objet Arch** insère une vue d\'un objet de Arch, un **<img src="images/Arch_SectionPlane.svg" width=16px> [Arch Plan de coupe](Arch_SectionPlane/fr.md)** dans une [TechDraw Page](TechDraw_PageDefault/fr.md).


{{Version/fr|1.0}}

: l\'outil [TechDraw Vue](TechDraw_View/fr.md) peut également créer une vue d\'un objet de Arch.

<img alt="" src=images/TechDraw_Arch_example.jpg  style="width:500px;">



## Utilisation

1.  Sélectionnez un plan de coupe Arch dans la [vue 3D](3D_view/fr.md) ou la [vue en arborescence](Tree_view/fr.md).
2.  S\'il y a plusieurs pages de dessin dans le document : ajoutez la page souhaitée à la sélection en la sélectionnant dans la [vue en arborescence](Tree_view/fr.md).
3.  Sélectionnez l\'option **TechDraw → Vues des autres ateliers → <img src="images/TechDraw_ArchView.svg" width=16px> Insérer un objet de l'atelier BIM ** du menu.
4.  S\'il y a plusieurs pages de dessin dans le document, et si aucune page n\'est affichée dans la [zone de vue principale](Main_view_area/fr.md) et que vous n\'avez pas encore sélectionné de page, la fenêtre de dialogue **Sélecteur de pages** s\'ouvre :
    1.  Sélectionnez la page désirée.
    2.  Appuyez sur le bouton **OK**.

## Options

-   La vue d\'un objet Arch est générée par l\'[atelier BIM](BIM_Workbench/fr.md).
-   [Draft Aimantation Dimensions](Draft_Snap_Dimensions/fr.md), [Draft Texte](Draft_Text/fr.md) et tout autre objet 2D (Sketch ou Draft) pris en compte par le plan de coupe est généré \"tel quel\" (pas d\'intersection ni de lignes cachées) par dessus la géométrie solide.
-   Le volume d\'un [Arch Espace](Arch_Space/fr.md) n\'est pas généré, seule l\'étiquette sera crée.
-   Les lignes de coupe, les lignes projetées (si la propriété Show Hidden est définie à True) et les lignes 2D ci-dessus peuvent être générées avec différentes largeurs de ligne. Cela peut être configuré dans les préférences Arch.
-   La vue d\'un objet Arch a deux modes de rendu :
    -   Filaire qui utilise les algorithmes OpenCasCade de l\'[atelier TechDraw](TechDraw_Workbench/fr.md) et est rapide et ne produit que des lignes (pas de remplissage de face possible)
    -   Solide qui est basé sur l\'[algorithme du peintre](https://fr.wikipedia.org/wiki/Algorithme_du_peintre) et est capable de rendre des surfaces remplies avec leur couleur de forme. Cependant, il est beaucoup plus lent et peut échouer dans de nombreuses situations.

:   L\'image ci-dessous illustre la différence entre les deux modes de rendu:





:   ![](images/TechDraw_Arch_rendering.jpg )

-   Seule la ligne de base des [Arch Conduites](Arch_Pipe/fr.md) est générée, pas le volume total des tubes :

:   ![](images/TechDraw_Arch_piping.jpg )



## Remarques

La vue d\'un objet Arch est générée dans l\'[atelier BIM](BIM_Workbench/fr.md) et donc TechDraw a un contrôle limité sur son apparence. Vous devrez peut-être apporter des modifications dans Arch pour obtenir la représentation souhaitée.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Une vue d\'un objet Arch, en fait un objet {{Incode|TechDraw::DrawViewArch}}, possède les [propriétés](TechDraw_View/fr#Propriétés_Vue_de_Part.md) communes à tous les types de vues. Elle possède également les propriétés supplémentaires suivantes :



### Données


{{TitleProperty|Arch view}}

-    **Source|Link**: l\'objet plan de coupe à afficher.

-    **All On|Bool**: si les objets cachés doivent être affichés ou non. Si `False`, seuls les objets visibles dans la vue 3D sont rendus.

-    **Render Mode|Enumeration**: le mode de rendu à utiliser, {{Value|Solid}} ou {{Value|Wireframe}}.

-    **Fill Spaces|Bool**: si `True`, les espaces d\'arc sont affichés sous forme de zone colorée.

-    **Show Hidden|Bool**: si la géométrie cachée (la partie de la géométrie qui se trouve derrière le plan de coupe) est affichée ou non. Elle sera rendue en ligne pointillée, ce qui peut être configuré dans les préférences d\'Arch.

-    **Show Fill|Bool**: si les zones coupées doivent être remplies avec une couleur grise ou non.

-    **Line Width|Float**: largeur des lignes principales. Les rapports de largeur des lignes coupées et des lignes projetées/2D peuvent être configurés dans les préférences d\'Arch.

-    **Font Size|Float**: taille de tous les textes qui apparaissent dans cette vue.

-    **Cut Line Width|Float**: largeur des lignes de coupe dans cette vue.

-    **Join Arch|Bool**: si `True`, les murs et les structures seront fusionnés par matériau.

-    **Line Spacing|Float**: espacement entre les lignes à utiliser pour les textes multilignes. {{Version/fr|1.0}}


{{TitleProperty|Drawing view}}

-    **Symbol|String|Hidden**: code SVG définissant ce symbole.

-    **Editable Texts|StringList**: valeurs de substitution pour les chaînes modifiables de ce symbole.

-    **Owner|Link**: fonction à laquelle ce symbole est rattaché. {{Version/fr|1.0}}



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Vue d\'un objet Arch peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
dv = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewArch','TestArch')
dv.Source = mySectionPlane
rc = page.addView(dv)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ArchView/fr
