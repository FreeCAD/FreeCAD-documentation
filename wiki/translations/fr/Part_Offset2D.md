---
- GuiCommand:/fr
   Name:Part Offset2D
   Name/fr:Part Décalage 2D
   MenuLocation:Pièce → Décalage 2D...
   Workbenches:[Part](Part_Workbench/fr.md)
   Version:0.17
   SeeAlso:[Part Décalage 3D](Part_Offset/fr.md), [Part Évidement](Part_Thickness/fr.md), [Draft Décalage](Draft_Offset/fr.md)
---


</div>

## Description

Part Décalage 2D génère un profil parallèle au profil d\'origine, à une distance définie de celui-ci. Il est également possible de d\'agrandir/réduire une face plane de la même façon.

Le profil/la face doit être plan. il peux y avoir plusieurs profils dans un objet, sans être nécessairement coplanaire.

![600px](images/Part_Offset2D_Demo.png)

## Utilisation

1.  Sélectionner un objet à décaler
2.  Appuyer sur le bouton **<img src=images/Part_Offset2D.svg style="width:24px">** **Décalage 2D**.
3.  Définir la valeur de décalage dans le [Panneau des tâches](Task_Panel/fr.md) puis valider.
4.  Appuyer sur **OK**.

Un objet Décalage 2D paramétrique est crée. Les object originaux sont basculés en mode rendu filaire.

## Propriétés

-    {{PropertyData/fr|Source}}: lien vers la forme d\'origine

-    {{PropertyData/fr|Value}}Valeur d\'agrandissement de la face/profil. Si négative, la dimension de la face ou du profil est réduite.

-    {{PropertyData/fr|Mode}}(\"Pipe\" ou \"Skin\"): Définit le traitement des profils non fermés. Si \"Pipe\" est selectionné, le profil est décalé comme un contour fermé extrêmement petit. Si \"Skin\" est sélectionné, un profil ouvert est créé.

:   ![600px](images/Part_Offset2D_Mode.png)

-    {{PropertyData/fr|Join}}(\"Arc\", \"Tangent\", \"Intersection\"): Définit le traitement des coins. Avec \"Arc\", les segments décalés sont joints par des arcs de cercle dont le centre est le sommet d\'origine. \"Tangent\" n\'est pas supporté pour OCC7.0.0. \"Intersection\": les segments sont prolongés jusqu\'à ce qu\'ils se croisent.

:   ![600px](images/Part_Offset2D_Join.png)

-    {{PropertyData/fr|Intersection}}(\"false\", \"true\"): Définit si les profils multiples sont traités collectivement ou indépendamment. Avec \"false\", les profils sont traités indépendamment les uns des autres, les intersections entre les profils résultants sont ignorées. Avec \"true\", les profils sont gérés de façon collective.

:   ![600px](images/Part_Offset2D_Intersection.png)





:   Seuls les profils dans un composé sont couplés. Par exemple, si la structure est composé (wire1, wire2, compound (wire3, wire4)), wire1 et wire2 seront traités collectivement, mais indépendamment de wire3 et wire4. De même, wire3 et wire4 sont traités collectivement, mais indépendamment de wire1 + wire2.





:   De même, en mode groupé, les directions des profils sont importantes et influencent la direction du décalage. Ceci est étroitement lié à la façon dont les trous dans les faces sont traités.





:   Les profils traités collectivement doivent être coplanaires. Les profils devant être décalés indépendamment n\'ont pas besoin d\'être coplanaires.

-    {{PropertyData/fr|Fill}}(\"false\", \"true\"): Si \"true\", l\'espace entre le profil / la face original et le décalage forme une face.

:   ![600px](images/Part_Offset2D_Fill.png)

## Problèmes connus {#problèmes_connus}

-   La plupart des modes non par défaut ne fonctionnent qu\'avec OCC 7.0.0 ou ultérieur.

-   L\'utilisation de l\'outil peut bloquer FreeCAD (voir le point suivant). Sur Windows, ces accidents sont convertis en exceptions et ne provoquent généralement pas la fermeture de FreeCAD; Sur d\'autres systèmes d\'exploitation, ce n\'est pas le cas. il est donc conseillé d\'enregistrer un projet avant d\'essayer d\'utiliser l\'outil. Les ellipses ne sont pas gérées.

-   L\'agrandissement des faces avec des trous circulaires d\'une valeur suffisamment grande pour que les trous se referment, génère un crash (OCC 7.0.0). Le problème semble être spécifique aux cercles; D\'autres formes semblent se terminer correctement.

-   lors du décalage de cercles dont le placement est non nul, le résultat est mal placé. (OCC 7.0.0)

-   lors du décalage de cercles, ils sont parfois décalés dans une direction inattendue (par exemple vers l\'intérieur au lieu de l\'extérieur). (OCC 7.0.0)

-   Fill = \"true\" ne fonctionne pas avec décalage groupé de profils ouverts en mode \"Skin\"

-   le mode de jonction \"Tangent\" ne fonctionne pas. (OCC 7.0.0)

-   Le décalage des profils constitués d\'un seul segment de ligne n\'est pas pris en charge (car le segment de ligne ne définit pas un plan). Les segments de ligne simples ne peuvent pas non plus participer à un décalage groupé.

## Script

L\'outil peut être utilisé dans des [macros](macros/fr.md) et depuis la console Python en utilisant les fonctions suivantes: {{code|code=
f = App.ActiveDocument.addObject("Part::Offset2D", "Offset2D")
f.Source =  #some object
f.Value = 10.0
}}

Décalage 2D est également disponible comme méthode de Part.Shape. Exemple: {{code|code=
import Part
circle = Part.Circle().toShape()
enlarged_circle = circle.makeOffset2D(10.0)
Part.show(circle)
Part.show(enlarged_circle)
# makeOffset2D(offset, join = 0, fill = False, openResult = false, intersection = false)
# 
# * offset: distance to expand the shape by. 
# 
# * join: method of offsetting non-tangent joints. 0 = arcs, 1 = tangent, 2 =
# intersection
# 
# * fill: if true, the output is a face filling the space covered by offset. If
# false, the output is a wire/face.
# 
# * openResult: True for "Skin" mode; False for Pipe mode. 
# 
# * intersection: collective offset
# 
# Returns: result of offsetting (wire or face or compound of those). Compounding
# structure follows that of source shape.
}}


<div class="mw-translate-fuzzy">





</div>


  
