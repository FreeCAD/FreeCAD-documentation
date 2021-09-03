---
- GuiCommand:/fr
   Name:TechDraw ProjectionGroup
   Name/fr:TechDraw Groupe de projection
   MenuLocation:TechDraw → Insérer un groupe de projection
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Vue active](TechDraw_View/fr.md), [TechDraw Vue de coupe](TechDraw_SectionView/fr.md)
---


</div>

## Description

L\'outil <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:24px;"> [Groupe de projection](TechDraw_ProjectionGroup/fr.md) crée une [projection multi-vue](https://en.wikipedia.org/wiki/Multiview_projection) d\'un ou plusieurs objets 3D. Les vues isométriques des 4 coins de devant peuvent également être incluses.

Si vous ne voulez produire qu\'une seule vue, l\'utilisation de Projection de groupe ne présente aucun avantage. Vous devez alors utiliser [Insérer une vue dans la page](TechDraw_View/fr.md) à la place. Si vous ne souhaitez pas utiliser les traditionnelles [projection premier-angle](https://en.wikipedia.org/wiki/Multiview_orthographic_projection#First-angle_projection) / [projection troisième-angle](https://en.wikipedia.org/wiki/Multiview_orthographic_projection#Third-angle_projection), vous devez utiliser plusieurs *Vues* ([Insérer une vue dans la page](TechDraw_View/fr.md)) au lieu de *Groupe de projection*.

<img alt="" src=images/TechDraw_ProjGroup_example.png  style="width:400px;"> 
*Trois vues orthogonales et une vue isométrique d'un objet solide*

## Utilisation

1.  Sélectionnez un ou plusieurs objets \"Corps\" et/ou \"Part\" dans la fenêtre 3D ou dans l\'arborescence .
2.  Si vous avez plusieurs pages de dessin dans votre document, vous devrez également sélectionner la page désirée dans l\'arborescence.
3.  Appuyez sur le bouton **<img src="images/TechDraw_ProjectionGroup.svg" width=16px> [Insérer un groupe de projection](TechDraw_ProjectionGroup/fr.md)**.
4.  Une boîte de dialogue s\'ouvre dans laquelle vous pouvez sélectionner les vues qui doivent apparaître dans le groupe, l\'échelle du groupe et d\'autres paramètres.

![](images/TaskProjGroup.png ) *[Panneau des tâches](Task_Panel/fr.md) de Projection Group pour choisir les options du groupe de projection. Le champ central indique la direction de la vue actuelle avec les pourcentages des axes x, y et z.*

Après avoir créé le Groupe de projection, vous pouvez déplacer le groupe dans son ensemble en faisant glisser la vue centrale. Vous pouvez également déplacer les vues de projection en les faisant glisser.

## Propriétés

-    {{PropertyData/fr|Anchor}}: La vue de référence (centrale) dans le groupe. Normalement, la vue de face.

-    {{PropertyData/fr|ProjectionType}}: \"Premier Angle (Premier dièdre)\" ou \"Troisième Angle (Troisième dièdre)\".

-    {{PropertyData/fr|AutoDistribute}}: Si la valeur est sur \"True\", espace les vues individuelles automatiquement. Utilisez \"False\" pour positionner les vues manuellement.

-    {{PropertyData/fr|spacingX}}: Espace horizontal entre les vues si le positionnement automatique est demandé. Notez que l\'échelle et la taille des autres vues du groupe influencent également l\'espacement.

-    {{PropertyData/fr|spacingY}}: Espace vertical entre les vues si le positionnement automatique est demandé.

ProjectionGroup dans son ensemble hérite de X, Y, ScaleType, Scale (Échelle) et Rotation à partir de la vue de base.

Les vues individuelles au sein du groupe héritent de toutes les propriétés de vue de la pièce, mais l\'objet ProjectionGroup contrôle l\'échelle de toutes ses vues membres.

La propriété RotationVector des différentes vues du groupe est obsolète à partir de v0.19. Utilisez XDirection à la place.

Notez que la boîte centrale affiche la direction de projection actuelle de la vue principale. Elle ne peut pas être utilisée pour changer de direction.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

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


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}  
