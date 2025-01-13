---
 GuiCommand:
   Name: TechDraw LengthDimension
   Name/fr: TechDraw Cote de longueur
   MenuLocation: TechDraw , Dimensions , Insérer une cote de longueur
   Workbenches: TechDraw_Workbench/fr
   SeeAlso: TechDraw_HorizontalDimension/fr, TechDraw_VerticalDimension/fr
---

# TechDraw LengthDimension/fr

## Description

L\'outil **TechDraw Cote de longueur** ajoute une cote linéaire à une vue. La cote peut être la distance entre deux points, la longueur d\'une ligne droite, la distance perpendiculaire entre deux arêtes ou la distance perpendiculaire entre un point et une arête.

<img alt="" src=images/TechDraw_Dimension_Length_example.png  style="width:220px;"> 
*Cote de longueur prise entre deux points*



## Utilisation

1.  Sélectionnez les points et/ou les arêtes qui définissent votre mesure. La géométrie peut être sélectionnée dans la vue 3D (deux premières options) ou dans le dessin (toutes les options) :
    -   Sélectionnez deux points.
    -   Sélectionnez une seule arête droite.
    -   Sélectionnez deux arêtes. Si les deux arêtes sont droites, elles doivent être parallèles. Cela produira une cote perpendiculaire si un point d\'extrémité de l\'une des arêtes a une projection perpendiculaire sur l\'autre arête (le point résultant doit se trouver sur l\'arête réelle). Si plusieurs solutions sont possibles, le point d\'extrémité le plus proche de son point de projection est utilisé. S\'il n\'y a pas de projection perpendiculaire valide, la cote sera la distance entre les extrémités les plus proches des arêtes.
    -   Sélectionnez un point et une arête. Cela produira une dimension perpendiculaire. Dans {{VersionMinus/fr|0.21}}, la cote ne sera perpendiculaire que si le point a une projection perpendiculaire sur l\'arête réelle. Dans le cas contraire, la cote sera la distance entre le point et l\'extrémité la plus proche de l\'arête.
2.  Si vous avez sélectionné une géométrie dans la vue 3D, ajoutez la bonne vue TechDraw à la sélection en la sélectionnant dans la vue en arborescense.
3.  Il y a plusieurs façons de lancer l\'outil :
    -   
        {{Version/fr|1.0}}
        
        : si la [préférence](TechDraw_Preferences/fr#Cotes.md) **Outils de cotation** est réglée sur {{Value|Outil unique}} (par défaut) : appuyez sur la flèche vers le bas à droite du bouton **<img src="images/TechDraw_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** et sélectionnez l\'option **<img src="images/TechDraw_ExtensionCreateHorizChainDimension.svg" width=16px> Cotes horizontales** du menu déroulant.

    -   Si cette préférence a une valeur différente (et dans {{VersionMinus/fr|0.21}}) : appuyez sur le bouton **<img src="images/TechDraw_LengthDimension.svg" width=16px> [Insérer une cote de longueur](TechDraw_LengthDimension/fr.md)**.

    -   Sélectionnez l\'option **TechDraw → Dimensions → <img src="images/TechDraw_LengthDimension.svg" width=16px> Insérer une cote de longueur** du menu.
4.  Une cote est ajoutée à la vue.
5.  La cote peut être déplacée jusqu\'à la position souhaitée.
6.  Si nécessaire, ajoutez des tolérances comme décrit sur [cette page](TechDraw_Geometric_dimensioning_and_tolerancing/fr#Tol.C3.A9rances.md).



### Affichage des mesures 3D 

La cote affichera initialement la mesure projetée (c\'est-à-dire telle qu\'elle apparaît dans le dessin). Si nécessaire, et si la cote est basée sur des références 3D, elle peut être remplacée par la mesure 3D réelle en changeant sa propriété **Measure Type** en {{Value|True}}. Pour baser une cote sur des références 3D, sélectionnez la géométrie dans la [vue 3D](3D_view/fr.md) au moment de la création, ou utilisez l\'outil <img alt="" src=images/TechDraw_DimensionRepair.svg  style="width:16px;"> [TechDraw Réparation des cotes](TechDraw_DimensionRepair/fr.md) pour mettre à jour les cotes existantes.



### Changer les propriétés 

Pour modifier les propriétés d\'un objet Cote, double-cliquez dessus dans le dessin ou dans la [vue en arborescence](Tree_view/fr.md). Cela ouvrira la [fenêtre de dialogue Cote](#Fenêtre_de_dialogue_Cote.md).



## Fenêtre de dialogue Cote 

![](images/TechDraw_DimensionDialog.png )

La fenêtre de dialogue Cote propose les paramètres suivants :



### Tolérances

-   **Théoriquement exact**: Si coché, spécifie la cote comme cote théoriquement exacte. En tant que telle, elle ne supportera aucune tolérance. La cote sera affichée par un cadre autour de la valeur: <img alt="" src=images/TechDraw_theoretically_exact.png  style="width:100px;">

-   **Tolérance symétrique**: Si coché, la tolérance supérieure et la tolérance inférieure sont égales et la valeur négative de la tolérance supérieure est utilisée comme tolérance inférieure. L\'affichage sera <img alt="" src=images/TechDraw_equal-tolerance.png  style="width:100px;">, sinon ce sera <img alt="" src=images/TechDraw_Non-equal-tolerance.png  style="width:80px;">.

-   **Tolérance supérieure** : valeur de combien la cote peut être plus grande.

-   **Tolérance inférieure** : valeur de combien la cote peut être plus petite.



### Mise en forme 

-   **Nombre de décimales** : comment la valeur de la cote sera formatée. Par défaut, le spécificateur est {{Value|%.xf}} où {{Value|x}} est le nombre de décimales. Pour la syntaxe de formatage, voir [cette page Wikipedia](https://fr.wikipedia.org/wiki/Printf). Il existe également un format supplémentaire {{Value|%w}} qui imprime le nombre de chiffres spécifié après le séparateur décimal et supprime les zéros de fin. Par exemple, {{Value|%.2w}} signifie qu\'au maximum 2 décimales seront imprimées et que les zéros de queue seront supprimés.

-   **Texte arbitraire** : si coché, la cote est remplacée par le contenu du champ **Nombre de décimales**.

-   **Précision de la tolérance supérieure** : comment la valeur de tolérance supérieure sera formatée. Par défaut, le spécificateur est {{Value|%.xf}} où {{Value|x}} est le nombre de décimales. Pour la syntaxe de formatage, voir [cette page Wikipedia](https://fr.wikipedia.org/wiki/Printf).

-   **Précision de la tolérance inférieure** : comment la valeur de tolérance inférieure sera formatée. Par défaut, le spécificateur est {{Value|%.xf}} où {{Value|x}} est le nombre de décimales. Pour la syntaxe de formatage, voir [cette page Wikipedia](https://fr.wikipedia.org/wiki/Printf).

-   **Tolérance du texte arbitraire** : si coché, les tolérances sont remplacées par le contenu des champs **Précision de la tolérance supérieure** **Précision de la tolérance inférieure**.



### Style d\'affichage 

-   **Inverser les flèches** : inverse la direction dans laquelle les flèches de la ligne de la cote pointent. Par défaut, elles sont à l\'intérieur de la ligne de cote/de l\'arc et pointent vers l\'extérieur.

-   **Couleur** : couleur des lignes et du texte.

-   **Taille de la police** : taille du texte de la cote.

-   **Style de représentation** : norme (et son style) selon laquelle la cote est dessinée. Voir la propriété [**Norme et style**](#Vue.md) pour plus de détails.



### Lignes

-   **Remplacer les angles** : si cette case est cochée, les angles existants de la ligne de la cote et des lignes d\'extension seront remplacés par les valeurs spécifiées.

-   **Angle de la cote** : valeur de substitution pour l\'angle de la cote avec l\'axe X de la vue (en degrés).

-   **Utiliser la valeur par défaut** : met l\'angle de la ligne de la cote à l\'angle existant.

-   **Utiliser la sélection** : définit l\'angle de la ligne de la cote pour qu\'il corresponde à l\'angle de l\'arête sélectionnée (ou de deux sommets) dans la vue.

-   **Angle des lignes d\'extension** : valeur de remplacement pour l\'angle des lignes d\'extension avec l\'axe X de la vue (en degrés).

-   **Utiliser la valeur par défaut** : met l\'angle de la ligne d\'extension à l\'angle existant.

-   **Utiliser la sélection** : définit l\'angle de la ligne d\'extension pour qu\'il corresponde à l\'angle de l\'arête sélectionnée (ou de 2 sommets) dans la vue.

## Limitations

Les objets Cote sont vulnérables au \"[Problème de dénomination topologique](Topological_naming_problem/fr.md)\". Cela signifie que si vous modifiez la géométrie 3D, les faces et les arêtes du modèle peuvent être renommées en interne. Si une cote est rattachée à un bord qui est ensuite modifié, la cote peut être faussée. En général, il n\'est pas possible de garder les cotes 2D projetées synchronisées avec les objets 3D réels.

Cela signifie qu\'en général, il n\'est pas possible de garder les cotes 2D projetées synchronisées avec les objets 3D réels si ceux-ci sont modifiés.



### Procédure

Si vous voulez conserver une vue TechDraw avec des cotes qui ne se cassent pas, vous devez coter un objet qui ne changera pas :

-   Créez une copie non paramétrique de l\'objet que vous voulez projeter avec [Part Copie simple](Part_SimpleCopy/fr.md).
-   Sélectionnez cette copie, puis utilisez [TechDraw Vue](TechDraw_View/fr.md) et ajoutez les cotes souhaitées.
-   Si le modèle 3D original est modifié, les modifications n\'affecteront pas la copie simple, ni les cotes dans la vue TechDraw.

Voir [TechDraw Cote à partir des points du repère](TechDraw_LandmarkDimension/fr.md) pour une autre approche pour contourner le problème de dénomination topologique.



## Remarques

-   **Sélection d\'un bord**. Les bords peuvent être difficiles à sélectionner. Vous pouvez ajuster la zone de sélection des bords en modifiant la préférence [Sélection autour des bords](TechDraw_Preferences/fr#Avancé.md).
-   **Position des décimales**. Les cotes utilisent le paramètre de nombre total de décimales par défaut. Cela peut être changé via les [préférences](TechDraw_Preferences/fr#Dimensions/fr.md) ou en modifiant la propriété FormatSpec.
-   **Plusieurs objets**. Les vues peuvent contenir plusieurs objets 3D comme source. Les cotes peuvent être appliquées à la géométrie à partir de n\'importe quel objet dans la vue (par exemple d\'Object1.Vertex0 à Object2.Vertex3).



## Propriétés



### Données


{{Properties_Title|Base}}

-    **References 2D|LinkSubList**: le(s) objet(s) de visualisation de dessin 2D sur lequel (lesquels) la mesure est basée. Utilisé si **Measure Type** est à {{Value|Projected}}.

-    **References 3D|LinkSubList**: le(s) objet(s) 3D sur lesquels la mesure est basée. Utilisé si **Measure Type** est {{Value|True}}.

-    **Type|Enumeration**: longueur, rayon, diamètre, etc. Normalement non manipulé par l\'utilisateur final.

-    **Measure Type|Enumeration**: la manière dont la mesure est effectuée.

:   

    :   True - basée sur une géométrie 3D.
    :   Projected - basée sur la géométrie de la vue du dessin 2D.

-    **Theoretical Exact|Bool**: spécifie une dimension théoriquement exacte (ou de base).

:   

    :   
        `False`
        
        \- une cote commune par défaut, éventuellement avec des tolérances.

    :   
        `True`
        
        \- une valeur théorique. En tant que telle, elle ne comporte pas de tolérances. La cote sera affichée par un cadre autour de la valeur : <img alt="" src=images/TechDraw_theoretically_exact.png  style="width:100px;">

-    **Equal Tolerance|Bool**: si la tolérance supérieure et la tolérance inférieure sont égales, alors la valeur négative de la tolérance supérieure est utilisée comme tolérance inférieure.

:   

    :   
        `True`
        
        \- la valeur niée de la **Over Tolerance** est utilisée comme **Under Tolerance**. L\'affichage sera <img alt="" src=images/TechDraw_equal-tolerance.png  style="width:100px;">.

    :   
        `False`
        
        \- la **Under Tolerance** est prise en compte. L\'affichage sera <img alt="" src=images/TechDraw_Non-equal-tolerance.png  style="width:80px;">

-    **Over Tolerance|QuantityConstraint**: la quantité de laquelle la cote peut être plus grande.

-    **Under Tolerance|QuantityConstraint**: la quantité par laquelle la cote peut être réduite.

-    **Inverted|Bool**: indique si la cote représente une valeur commune ou inversée.

:   

    :   
        `False`
        
        \- la valeur ordinaire est utilisée. Pour la longueur, c\'est un nombre positif, pour l\'angle, la valeur oblique (0° - 180°).

    :   
        `True`
        
        \- la valeur inversée est utilisée. Pour la longueur, c\'est un nombre négatif, pour l\'angle, la valeur réflexe (180° - 360°).

-    **X|Distance**: position horizontale du texte de la cote par rapport à la vue.

-    **Y|Distance**: position verticale du texte de la cote par rapport à la vue.

-    **Lock Position|Bool|Hidden**: verrouille la position du texte de la cote lorsque mis à `True`.

-    **Rotation|Angle|Hidden**: lecture uniquement.

-    **Scale Type|Enumeration|Hidden**: lecture uniquement.

-    **Scale|FloatConstant|Hidden**: lecture uniquement.

-    **Caption|String|Hidden**: non utilisé.


{{Properties_Title|Format}}

-    **Format Spec|String**: comment la valeur de dimension sera formatée. Voir [Mise en forme](#Mise_en_forme.md).

-    **Format Spec Over Tolerance|String**: comme **Format Spec**, mais pour les tolérances inférieures.

-    **Format Spec Under Tolerance|String**: comme **Format Spec**, mais pour les tolérances inférieures.

-    **Arbitrary|Bool**: indique si la cote est remplacée par le contenu du champ **Format Spec**.

:   

    :   
        `False`
        
        \- le contenu de **Format Spec** est utilisé pour formater la valeur de la cote réelle.

    :   
        `True`
        
        \- le contenu de **Format Spec** sera affiché sous forme de texte au lieu de la valeur de la cote.

-    **Arbitrary Tolerances|Bool**: comme **Arbitrary**, mais pour la tolérance.


{{Properties_Title|Override}}

-    **Angle Override|Bool**: indique si la direction des lignes de la cote et d\'extension est remplacée.

:   

    :   
        `False`
        
        \- les directions sont calculées comme d\'habitude.

    :   
        `True`
        
        \- les directions sont remplacées par les valeurs des propriétés LineAngle et ExtensionAngle.

-    **Line Angle|Angle**: angle de la ligne de la cote avec l\'axe X de la vue (en degrés).

-    **Extension Angle|Angle**: angle de la ou des lignes d\'extension avec l\'axe X de la vue (en degrés).


{{Properties_Title|References}}

-    **Saved Geometry|TopoShapeList|Hidden**: géométrie de référence. {{Version/fr|0.21}}



### Vue


{{TitleProperty|Base}}

-    **Keep Label|Bool**: non utilisé.

-    **Stack Order|Integer**: chevauchement ou sous-chevauchement par rapport à d\'autres objets du dessin. {{Version/fr|0.21}}


{{Properties_Title|Dimension Format}}

-    **Arrowsize|Length**: taille des flèches de cote. {{Version/fr|0.21}}

-    **Color|Color**: couleur des lignes et du texte.

-    **Flip Arrowheads|Bool**: par défaut, la valeur *à l\'intérieur* de la ligne/de l\'arc de la cote signifie que les flèches sont dirigées vers l\'extérieur. Si elle est placée *à l\'extérieur* de la ligne/arc de la cote, les flèches pointent *vers l\'intérieur* de la ligne/arc de la cote.

:   

    :   
        `False`
        
        \- permet de sélectionner automatiquement la direction des flèches selon la règle ci-dessus.

    :   
        `True`
        
        \- annule la direction choisie automatiquement et forcez la direction opposée.

-    **Font|Font**: nom de la police à utiliser pour le texte de la dimension.

-    **Fontsize|Length**: taille du texte de la dimension.

-    **Gap Factor ASME|Float**: ajuste l\'écart entre les points de la cote et le début des lignes d\'extension. L\'écart est égal à cette valeur multipliée par la largeur de la ligne. {{Version/fr|0.21}}

-    **Gap Factor ISO|Float**: ajuste l\'écart entre les points de dimension et le début des lignes d\'extension. L\'écart est égal à cette valeur multipliée par la largeur de la ligne. {{Version/fr|0.21}}

-    **Line Spacing Factor|Float**: ajuste l\'espace entre le texte de la cote et la ligne de cote. L\'espace est égal à cette valeur multipliée par la largeur de la ligne. {{Version/fr|0.21}}

-    **Line Width|Length**: épaisseur de la ligne de la cote.

-    **Rendering Extent|Enumeration**: propriété plutôt universelle spécifiant l\'espace du le dessin des cotes peut occuper :

:   

    :   None - aucune ligne ou flèche n\'est dessinée, seule la valeur de la cote est affichée.
    :   Minimal - pour les longueurs et les angles, une ligne à tête unique reliant la valeur de la cote et la *ligne d\'extension virtuelle* du point final est tracée. La ligne d\'extension elle-même n\'est pas ajoutée.
    :   Les diamètres sont affichés après l\'optionConfined, les rayons après l\'option Reduced.
    :   Confined - pour les longueurs et les angles, une ligne à double tête (ou un arc) reliant les *lignes d\'extension virtuelles* des points de départ et d\'arrivée est dessinée, bien que les lignes d\'extension elles-mêmes ne soient pas ajoutées.
    :   Les diamètres sont affichés avec une ligne minimale à une tête, de la valeur de la dimension au point le plus proche du cercle, les rayons comme pour l\'option Reduced.
    :   Reduced - pour les longueurs et les angles, une ligne à une tête reliant la valeur dimensionnelle et la *ligne d\'extension* du point final est dessinée avec la ligne d\'extension elle-même.
    :   Les diamètres sont affichés avec une ligne à une tête du centre au point le plus proche du cercle, les rayons avec une ligne à une tête minimale de la valeur de la cote au point d\'arc le plus proche.
    :   Normal - valeur par défaut. Pour les longueurs et les angles, une ligne à double tête (ou un arc) reliant les *lignes d\'extension* des points de départ et d\'arrivée est dessinée, ainsi que les lignes d\'extension elles-mêmes.
    :   Les diamètres sont dessinés comme des lignes à double tête qui frappent le centre et relient les points les plus proches et les plus éloignés du cercle.
    :   Les rayons sont dessinés comme une ligne à une tête partant du centre jusqu\'au point le plus proche de l\'arc.
    :   Expanded - seuls les diamètres prennent en charge cette valeur, ce qui permet de les rendre d\'une manière similaire à une longueur horizontale ou verticale. Les autres types de dimensions sont rendus comme avec l\'option Normal.

-    **Standard And Style|Enumeration**: spécifie la norme (et son style) selon laquelle la dimension est dessinée :

:   

    :   <img alt="Différences entre les normes prises en charge" src=images/TechDraw_Dimension_standardization.png  style="width:500px;">

    :   ISO Oriented - dessiné selon la norme ISO 129-1, le texte est tourné de façon à être parallèle à la tangente de la ligne de la cote.

    :   ISO Referencing - dessiné conformément à la norme ISO 129-1, le texte est toujours horizontal, au-dessus de la ligne de référence la plus courte possible.

    :   ASME Inlined - dessiné selon la norme ASME Y14.5M, le texte est horizontal, inséré dans une rupture à l\'intérieur de la ligne de la cote ou de l\'arc.

    :   ASME Referencing - dessiné conformément à la norme ASME Y14.5M, le texte est horizontal, une courte ligne de référence est fixée au centre vertical d\'un côté.



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Cote de longueur peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
dim1 = FreeCAD.ActiveDocument.addObject("TechDraw::DrawViewDimension", "Dimension")
dim1.Type = "Distance"
dim1.References2D=[(view1, "Edge1")]
page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LengthDimension/fr
