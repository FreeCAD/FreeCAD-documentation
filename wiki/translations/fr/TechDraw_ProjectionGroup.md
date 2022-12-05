---
- GuiCommand:/fr
   Name:TechDraw ProjectionGroup
   Name/fr:TechDraw Groupe de projections
   MenuLocation:TechDraw → Insérer un groupe de projections
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Vue active](TechDraw_View/fr.md), [TechDraw Vue de coupe](TechDraw_SectionView/fr.md)
---

# TechDraw ProjectionGroup/fr

## Description

L\'outil <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:24px;"> [Groupe de projections](TechDraw_ProjectionGroup/fr.md) crée une [projection multi-vue](https://en.wikipedia.org/wiki/Multiview_projection) d\'un ou plusieurs objets 3D. Les vues isométriques des 4 coins de devant peuvent également être incluses.

Si vous ne voulez produire qu\'une seule vue, l\'utilisation de Groupe de projections ne présente aucun avantage. Vous devez alors utiliser [Insérer une vue dans la page](TechDraw_View/fr.md) à la place. Si vous ne souhaitez pas utiliser les traditionnelles [projection premier-angle](https://en.wikipedia.org/wiki/Multiview_orthographic_projection#First-angle_projection) / [projection troisième-angle](https://en.wikipedia.org/wiki/Multiview_orthographic_projection#Third-angle_projection), vous devez utiliser plusieurs *Vues* ([Insérer une vue dans la page](TechDraw_View/fr.md)) au lieu de *Groupe de projections*.

<img alt="" src=images/TechDraw_ProjGroup_example.png  style="width:400px;"> 
*Trois vues orthogonales et une vue isométrique d'un objet solide*

## Utilisation

1.  Vous pouvez faire pivoter la [Vue 3D](3D_view/fr.md). La direction de la caméra dans la [Vue 3D](3D_view/fr.md) détermine la valeur initiale de la **Direction primaire** du groupe de projection (la propriété **Direction** de la vue centrale).
2.  Sélectionnez un ou plusieurs objets dans la [Vue 3D](3D_view/fr.md) ou de la [Vue en arborescence](Tree_view/fr.md).
3.  S\'il y a plusieurs pages de dessin dans le document : ajoutez éventuellement la page souhaitée à la sélection en la sélectionnant dans la [Vue en arborescence](Tree_view/fr.md). Ceci n\'est pas optionnel pour {{VersionMinus/fr|0.19}}.
4.  Il existe plusieurs façons d\'invoquer l\'outil :
    -   Appuyez sur le bouton **<img src="images/TechDraw_ProjectionGroup.svg" width=16px> [Insérer un groupe de projections ](TechDraw_ProjectionGroup/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → <img src="images/TechDraw_ProjectionGroup.svg" width=16px> Insérer un groupe de projections ** dans le menu.
5.  Si le document comporte plusieurs pages de dessin et que vous n\'avez pas encore sélectionné de page, la boîte de dialogue **Sélecteur de page** s\'ouvre : {{Version/fr|0.20}}
    1.  Sélectionnez la page souhaitée.
    2.  Appuyez sur le bouton **OK**.
6.  Le panneau de tâches **Groupe de projection** s\'ouvre.
7.  Sélectionnez les vues qui doivent apparaître dans le groupe de projection, ainsi que l\'échelle et les autres paramètres du groupe de projection.
8.  Appuyez sur le bouton **OK**.
9.  Vous pouvez déplacer le Groupe de Projection en faisant glisser sa vue centrale.
10. Vous pouvez également déplacer les autres vues du groupe de projection par rapport à la vue centrale en les faisant glisser individuellement.

![](images/TaskProjGroup.png ) 
*Le [Panneau des tâches](Task_Panel/fr.md) Groupe de projections. Le champ Direction primaire indique la direction en cours de la vue.*

## Propriétés

### Données


{{TitleProperty|Base}}

-    **Source|LinkList**: liens vers les objets dessinables à représenter.

-    **XSource|XLLinkList**: liens vers les objets dessinables dans un fichier externe. {{Version/fr|0.19}}

-    **Anchor|Link**: vue centrale du groupe. Normalement, il s\'agit de la vue de face.

-    **ProjectionType|Enumeration**: {{Value|First Angle}} ou {{Value|Third Angle}}.

Pour les autres propriétés de ce groupe, voir [TechDraw Vue](TechDraw_View/fr#Propri.C3.A9t.C3.A9s.md).


{{TitleProperty|Collection}}

-    **Views|LinkList**: liens vers les vues de ce Groupe de projections.


{{TitleProperty|Distribute}}

-    **Auto Distribute|Bool**: si `True`, espace automatiquement les vues individuelles. Utilisez `False` pour un positionnement manuel.

-    **spacing X|Length**: espace horizontal entre les vues lorsqu\'elles sont positionnées automatiquement. Notez que l\'échelle et la taille des autres vues du groupe influencent également l\'espacement.

-    **spacing Y|Length**: espace vertical entre les vues lorsqu\'elles sont positionnées automatiquement.

### Vue


{{TitleProperty|Base}}

Voir [TechDraw Vue](TechDraw_View/fr#Propri.C3.A9t.C3.A9s.md)

## Remarques

Groupe de projections dans son ensemble hérite de X, Y, ScaleType, Scale (Échelle) et Rotation à partir de la vue de base.

Les vues individuelles au sein du groupe héritent de toutes les propriétés de vue de la pièce, mais l\'objet ProjectionGroup contrôle l\'échelle de toutes ses vues membres.

La propriété RotationVector des différentes vues du groupe est obsolète à partir de v0.19. Utilisez XDirection à la place.

Notez que la boîte centrale affiche la direction de projection en cours de la vue principale. Elle ne peut pas être utilisée pour changer de direction.

## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil NewProjGroup peut être utilisé dans des [macro](Macros/fr.md) et à partir de la console [Python](Python/fr.md). Un script complet est disponible dans la distribution source sous \"source-dir/src/Mod/TechDraw/TDTest/DProjGroupTest.py\".


```python
    #make a page
    print("making a page")
    page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
    FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
    FreeCAD.ActiveDocument.Template.Template = templateFileSpec
    FreeCAD.ActiveDocument.Page.Template = FreeCAD.ActiveDocument.Template

    #make projection group
    group = FreeCAD.ActiveDocument.addObject('TechDraw::DrawProjGroup','ProjGroup')
    rc = page.addView(group)
    group.Source = [fusion]

    #add Front(Anchor) view
    frontView = group.addProjection("Front")               ##need an Anchor

    #update group
    group.Anchor.Direction = FreeCAD.Vector(0,0,1)
    group.Anchor.RotationVector = FreeCAD.Vector(1,0,0)

    #add more projections
    leftView = group.addProjection("Left")
    topView = group.addProjection("Top")
    rightView = group.addProjection("Right")
    rearView = group.addProjection("Rear")
    BottomView = group.addProjection("Bottom")

    #remove a view from projection group
    iv = group.removeProjection("Left")

```

Remarque de programmation: le groupe de projection doit toujours être ajouté à la page (par exemple, page.addView(group) avant d\'ajouter des projections au groupe. Cela permet au groupe de projection d\'utiliser les valeurs de paramètre par défaut dérivées de la page parente.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ProjectionGroup/fr
