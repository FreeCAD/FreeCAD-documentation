---
- GuiCommand   */fr
   Name   *TechDraw LengthDimension
   Name/fr   *TechDraw Cote de longueur
   MenuLocation   *TechDraw → Dimensions → Insérer une cote de longueur
   Workbenches   *[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso   *[TechDraw Cote horizontale](TechDraw_HorizontalDimension/fr.md), [TechDraw Cote verticale](TechDraw_VerticalDimension/fr.md)
---

# TechDraw LengthDimension/fr

## Description

L\'outil <img alt="" src=images/TechDraw_LengthDimension.svg  style="width   *24px;"> 
**TechDraw Cote de longueur** ajoute une dimension linéaire à une vue. La dimension peut être la distance entre deux sommets, la longueur d\'un bord ou la distance entre deux arêtes. La dimension sera initialement la distance projetée (c.-à-d. comme indiqué sur le dessin), mais elle peut être remplacée par la distance 3D réelle en utilisant l\'outil **<img src="images/TechDraw_LinkDimension.svg" width=16px> [TechDraw Lier une dimension](TechDraw_LinkDimension/fr.md)**

<img alt="" src=images/TechDraw_Dimension_Length_example.png  style="width   *220px;"> 
*Dimension de longueur prise à partir de deux nœuds arbitraires de la vue*

## Utilisation

1.  Sélectionnez les points ou les arêtes qui définissent votre mesure.
2.  Il existe plusieurs façons de lancer l\'outil    *
    -   Appuyez sur le bouton **<img src="images/TechDraw_LengthDimension.svg" width=16px> [Insérer une cote de longueur](TechDraw_LengthDimension/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → Dimensions → <img src="images/TechDraw_LengthDimension.svg" width=16px> Insérer une cote de longueur** dans le menu.
3.  Une dimension sera ajoutée à la vue. La dimension peut être déplacée à la position désirée.
4.  Si nécessaire, ajoutez des tolérances comme décrit dans [cette page](TechDraw_Geometric_dimensioning_and_tolerancing/fr#Tol.C3.A9rances.md).

Pour modifier les propriétés d\'un objet de dimension, double-cliquez dessus dans le dessin ou dans la [Vue en arborescence](Tree_view/fr.md). Cela ouvrira le dialogue Dimension   *

## Boîte de dialogue Dimension 

La boîte de dialogue des dimensions propose les paramètres suivants    *

![](images/TechDraw_DimensionDialog.png )

### Tolérances

-   **Théoriquement exact**   * Si coché, spécifie la dimension comme dimension théoriquement exacte. En tant que telle, elle ne supportera aucune tolérance. La dimension sera affichée par un cadre autour de la valeur   * <img alt="" src=images/TechDraw_theoretically_exact.png  style="width   *100px;">

-   **Tolérance symétrique**   * Si coché, la sur-tolérance et la sous-tolérance sont égales et la valeur négative de la sur- et de la sous-tolérance est utilisée comme sous-tolérance. L\'affichage sera <img alt="" src=images/TechDraw_equal-tolerance.png  style="width   *100px;">, sinon ce sera <img alt="" src=images/TechDraw_Non-equal-tolerance.png  style="width   *80px;">.

-   **Tolérance supérieure**   * La valeur de combien la dimension peut être plus grande.

-   **Tolérance inférieure**   * La valeur de combien la dimension peut être plus petite.

### Mise en forme 

-   **Nombre de décimales**    * Comment la valeur de la dimension sera formatée. Par défaut, le spécificateur est {{Value|%.xf}} où {{Value|x}} est le nombre de décimales. Pour la syntaxe de formatage, voir [cette page Wikipedia](https   *//fr.wikipedia.org/wiki/Printf). Il existe également un format supplémentaire {{Value|%w}} qui imprime le nombre de chiffres spécifié après le séparateur décimal et supprime les zéros de fin. Par exemple, {{Value|%.2w}} signifie qu\'au maximum 2 décimales seront imprimées et que les zéros de queue seront supprimés.

-   **Texte arbitraire**   * Si coché, la dimension est remplacée par le contenu du champ **Nombre de décimales**.

-   **Précision de la tolérance supérieure**   * Comment la valeur de surtolérance sera formatée. Par défaut, le spécificateur est {{Value|%.xf}} où {{Value|x}} est le nombre de décimales. Pour la syntaxe de formatage, voir [cette page Wikipedia](https   *//fr.wikipedia.org/wiki/Printf).

-   **Précision de la tolérance inférieure**   * Comment la valeur de sous-tolérance sera formatée. Par défaut, le spécificateur est {{Value|%.xf}} où {{Value|x}} est le nombre de décimales. Pour la syntaxe de formatage, voir [cette page Wikipedia](https   *//fr.wikipedia.org/wiki/Printf).

-   **Tolérance du texte arbitraire**   * Si coché, les tolérances sont remplacées par le contenu des champs **Précision de la tolérance supérieure** **Précision de la tolérance inférieure**.

### Style d\'affichage 

-   **Inverser les flèches**   * Inverse la direction dans laquelle les flèches de la ligne de cote pointent. Par défaut, elles sont à l\'intérieur de la ligne de cote/de l\'arc et pointent vers l\'extérieur.

-   **Couleur**   * La couleur des lignes et du texte.

-   **Taille de la police**   * La taille du texte de la cote.

-   **Style de représentation**   * La norme (et son style) selon laquelle la cote est dessinée. Voir la propriété [**Norme et style**](#Vue.md) pour plus de détails.

### Lignes

-   **Remplacer les angles**    * Si cette case est cochée, les angles existants de la ligne de cote et des lignes d\'extension seront remplacés par les valeurs spécifiées.

-   **Angle de la cote**    * Valeur de substitution pour l\'angle de la cote avec l\'axe X de la vue (en degrés).

-   **Utiliser la valeur par défaut**    * Met l\'angle de la ligne de cote à l\'angle existant.

-   **Utiliser la sélection**    * Définit l\'angle de la ligne de cote pour qu\'il corresponde à l\'angle de l\'arête sélectionnée (ou de deux sommets) dans la vue.

-   **Angle des lignes d\'extension**    * Valeur de remplacement pour l\'angle des lignes d\'extension avec l\'axe X de la vue (en degrés).

-   **Utiliser la valeur par défaut**    * Met l\'angle de la ligne d\'extension à l\'angle existant.

-   **Utiliser la sélection**    * Définit l\'angle de la ligne d\'extension pour qu\'il corresponde à l\'angle de l\'arête sélectionnée (ou de 2 sommets) dans la vue.

## Propriétés

### Données


{{Properties_Title|Base}}

-    **X**   * position horizontale du texte de la cotation en mm par rapport à la vue.

-    **Y**   * position verticale du texte de la cotation en mm par rapport à la vue.

-    **Type**   * longueur, rayon, diamètre, etc. Normalement non manipulé par l\'utilisateur final.

-    **Measure Type**   * Comment la mesure est effectuée. Normalement, n\'est pas manipulé directement par l\'utilisateur.

   *   

       *   True - basé sur la géométrie 3D ou
       *   Projected - basé sur le dessin

-    **Theoretical Exact**   * spécifie une dimension théoriquement exacte (ou de base).

   *   

       *   
        `False`
        
        \- une dimension commune par défaut, éventuellement avec des tolérances.

       *   
        `True`
        
        \- une valeur théorique. En tant que tel, elle ne supportera aucune tolérance. La cote sera affichée par un cadre autour de la valeur   *

<img alt="" src=images/TechDraw_theoretically_exact.png  style="width   *100px;">

-    **Equal Tolerance**   * si la sur-tolérance et la sous-tolérance sont égales, la valeur négative de la sur-tolérance est alors utilisée comme sous-tolérance.

   *   

       *   
        `True`
        
        \- la valeur négative de la **Over Tolerance** est utilisée comme **Under Tolerance**. L\'affichage sera <img alt="" src=images/TechDraw_equal-tolerance.png  style="width   *100px;">.

       *   
        `False`
        
        \- la **Under Tolerance** est prise en compte. L\'affichage sera <img alt="" src=images/TechDraw_Non-equal-tolerance.png  style="width   *80px;">

-    **Over Tolerance**   * valeur de combien la dimension peut être plus grande.

-    **Under Tolerance**   * valeur de combien la dimension peut être plus petite.

-    **Inverted**   * indique si la dimension représente une valeur commune ou une valeur inversée.

   *   

       *   
        `False`
        
        \- la valeur ordinaire est utilisée. Pour la longueur, il s\'agit d\'un nombre positif, pour angle, la valeur oblique (0° à 180°).

       *   
        `True`
        
        \- la valeur inversée est utilisée. Pour la longueur un nombre négatif, pour l\'angle la valeur du réflexe (180° à 360°).


{{Properties_Title|Format}}

-    **Format Spec**   * comment la valeur de dimension sera formatée. Voir [Mise en forme](#Mise_en_forme.md).

-    **Format Spec Over Tolerance**   * comme **Format Spec**, mais pour les surtolérances.

-    **Format Spec Under Tolerance**   * comme **Format Spec**, mais pour les sous-tolérances.

-    **Arbitrary**   * indique si la dimension est remplacée par le contenu du champ **Format Spec**.

   *   

       *   
        `False`
        
        \- le contenu de **Format Spec** est utilisé pour formater la valeur dimensionnelle réelle.

       *   
        `True`
        
        \- le contenu de **Format Spec** sera affiché sous forme de texte à la place si la valeur de la dimension.

-    **Arbitrary Tolerances**   * comme **Arbitrary**, mais pour la tolérance.


{{Properties_Title|Override}}

-    **AngleOverride**   * indique si la direction des lignes de cote et d\'extension est remplacée.

   *   

       *   
        `False`
        
        \- les directions sont calculées comme d\'habitude.

       *   
        `True`
        
        \- les directions sont remplacées par les valeurs des propriétés LineAngle et ExtensionAngle.

-    **LineAngle**   * angle de la ligne de cote avec l\'axe X de la vue (en degrés).

-    **ExtensionAngle**   * angle de la ou des lignes d\'extension avec l\'axe X de la vue (en degrés).

### Vue


{{Properties_Title|Base}}

-    **Visibility**   * définit si la dimension est visible. `True` - visible, `False` - masqué.


{{Properties_Title|Dim Format}}

-    **Font**   * nom de la police à utiliser pour le texte de cote.

-    **Font Size**   * taille du texte.

-    **Gap Factor ASME**   * ajuste l\'écart entre les points de dimension et le début des lignes d\'extension. L\'écart est égal à cette valeur multipliée par la largeur de la ligne. {{Version/fr|1.0}}

-    **Gap Factor ISO**   * ajuste l\'écart entre les points de dimension et le début des lignes d\'extension. L\'écart est égal à cette valeur multipliée par la largeur de la ligne. {{Version/fr|1.0}}

-    **Line Width**   * épaisseur de la ligne de cote.

-    **Color**   * couleur des lignes et du texte.

-    **Standard And Style**   * spécifie le standard (et son style) en fonction duquel la dimension est dessinée   *

<img alt="Différences entre les normes prises en charge" src=images/TechDraw_Dimension_standardization.png  style="width   *500px;">

   *   

       *   ISO Oriented - dessine conformément à la norme ISO 129-1 (norme internationale), le texte est pivoté de manière à être parallèle à la tangente de la ligne de cote.
       *   ISO Referencing - dessine conformément à la norme ISO 129-1, le texte est toujours horizontal, au-dessus de la ligne de référence la plus courte possible.
       *   ASME Inlined - dessine conformément à la norme ASME Y14.5M (norme américaine), le texte est horizontal, inséré dans une rupture dans la ligne de cote ou dans l\'arc.
       *   ASME Referencing - dessiné conformément à la norme ASME Y14.5M, le texte est horizontal, la ligne de référence courte est attachée au centre vertical d\'un côté.

-    **Rendering Extent**   * propriété plutôt universelle spécifiant l\'espace que le dessin de dimension peut occuper   *

   *   

       *   None - aucune ligne ni aucune flèche ne sont dessinées, seule la valeur de cote nue est affichée.
       *   Minimal - pour les longueurs et les angles, une seule ligne en tête reliant la valeur dimensionnelle à la *ligne d\'extension virtuelle* du point final est tracée. La ligne d\'extension elle-même n\'est pas ajoutée.
       *   Les diamètres sont affichés en fonction de l\'étendue Confined, les rayons après l\'étendue Reduced.
       *   Confined - pour les longueurs et les angles, une ligne (ou un arc) à deux pointes reliant les \"\'lignes d\'extension virtuelles\" des points de départ et d\'arrivée est tracé, bien que les lignes d\'extension ne soient pas ajoutées.
       *   Les diamètres sont dessinés avec une ligne à simple tête allant de la valeur dimensionnelle au point le plus proche du cercle, les rayons étant identiques l\'optionReduced.
       *   Reduced - pour les longueurs et les angles, une ligne à simple tête reliant la valeur dimensionnelle à la *ligne d\'extension* du point final est dessinée avec la ligne d\'extension elle-même.
       *   Les diamètres sont dessinés avec une ligne simple allant du centre au point le plus proche du cercle, les rayons avec une simple ligne simple allant de la valeur dimensionnelle au point d\'arc le plus proche.
       *   Normal - la valeur par défaut. Pour les longueurs et les angles, une ligne à double tête (ou arc) reliant les \"lignes d\'extension\" des points de départ et d\'arrivée est dessinée, les lignes d\'extension elles-mêmes.
       *   Les diamètres sont tracés sous forme de lignes à deux pointes touchant le centre et reliant les points les plus proches et les plus éloignés du cercle.
       *   Les rayons sont dessinés comme une seule ligne en-tête du centre au point d\'arc le plus proche.
       *   Expanded - Seuls les diamètres prennent en charge cette valeur, ce qui les rend de manière horizontale ou verticale. Les autres types de dimension sont rendus comme avec l\'étendue Normal.

-    **Flip Arrowheads**   * par défaut, la valeur *à l\'intérieur* de la ligne/arc de cote désigne les flèches pointant vers *vers l\'extérieur*. Si elle est placée \"à l\'extérieur\" de la ligne/arc de cote, les flèches pointent \"à l\'intérieur\" de la ligne/arc de cote.

   *   

       *   
        `False`
        
        \- laisse le sens des flèches à sélectionner automatiquement en fonction de la règle ci-dessus.

       *   
        `True`
        
        \- ignore la direction choisie automatiquement et force la direction opposée.

## Limitations

Les objets de dimension sont vulnérables au \"[Problème de dénomination topologique](Topological_naming_problem/fr.md)\". Cela signifie que si vous modifiez la géométrie 3D, les faces et les arêtes du modèle peuvent être renommées en interne. Si une dimension est attachée à un bord qui est ensuite modifié, la dimension peut être faussée. En général, il n\'est pas possible de garder les dimensions 2D projetées synchronisées avec les objets 3D réels.

Cela signifie qu\'en général, il n\'est pas possible de garder les cotes 2D projetées synchronisées avec les objets 3D réels si ceux-ci sont modifiés.

### Procédure

Si vous souhaitez conserver une vue TechDraw avec des dimensions inaltérables, vous devez dimensionner un objet qui ne changera pas.

-   Sélectionnez l\'objet que vous souhaitez projeter, puis basculez vers l\'<img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [atelier Part](Part_Workbench/fr.md) et utilisez **Part → <img src="images/Part_SimpleCopy.svg" width=16px> [Créer une copie simple](Part_SimpleCopy/fr.md)**. Cela créera un seul objet non paramétrique, c\'est-à-dire qu\'il ne sera plus modifiable.
-   Sélectionnez cette copie, puis utilisez [TechDraw Vue](TechDraw_View/fr.md) et ajoutez les dimensions souhaitées.
-   Si le modèle 3D d\'origine est modifié, les modifications n\'affecteront pas la copie simple ni les dimensions de la vue TechDraw.

Voir [TechDraw Dimension de repère](TechDraw_LandmarkDimension/fr.md) pour une autre approche pour contourner le problème de dénomination topologique.

## Script


**Voir aussi   ***

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Cote de longueur peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes   *


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewDimension','Dimension')
dim1.Type = "Distance"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```

## Remarques

-   **Sélection d\'un bord**. Les bords peuvent être difficiles à sélectionner. Vous pouvez ajuster la zone de sélection des arêtes à l'aide du paramètre \"/Mod/TechDraw/General/EdgeFuzz\" (voir l\'[Editeur de paramètres](Std_DlgParameter/fr.md)). C\'est un nombre sans dimension. La valeur par défaut est 10.0. Des valeurs dans la plage 20-30 faciliteront considérablement la sélection des arêtes. Un grand nombre entraînera des chevauchements avec d\'autres éléments de dessin.
-   **Position des décimales**. Les cotes utilisent le paramètre de nombre total de décimales par défaut. Cela peut être changé via [préférences](TechDraw_Preferences/fr#Dimensions/fr.md) ou en modifiant la propriété FormatSpec.
-   **Plusieurs objets**. Les vues peuvent contenir plusieurs objets 3D comme source. Les cotes peuvent être appliquées à la géométrie à partir de n\'importe quel objet dans la vue (par exemple d\'Object1.Vertex0 à Object2.Vertex3).





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LengthDimension/fr
