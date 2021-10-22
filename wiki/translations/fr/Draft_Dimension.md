---
- GuiCommand:
   Name:Draft Dimension
   Name/fr:Draft Dimension
   MenuLocation:Annotation → Dimension
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**D** **I**
   Version:0.8
   SeeAlso:[Draft Inverser la direction de la cote](Draft_FlipDimension/fr.md)
---

# Draft Dimension/fr

## Description

La commande <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> **Draft Dimension** [crée](#Create.md) une [dimension linéaire](#Utilisation_pour_une_dimension_lin.C3.A9aire.md), une [dimension radiale](#Utilisation_pour_une_dimension_radiale.md) ou une [dimension angulaire](#Utilisation_pour_une_dimension_angulaire.md). La commande peut également être utilisée pour [convertir](#Convertir.md) des objets [Std Mesurer une distance](Std_MeasureDistance/fr.md).

Les dimensions linéaires basées sur les arêtes et les dimensions radiales sont paramétriques. Cela signifie qu\'elles seront mises à jour si l\'arête mesurée est modifiée. Les arêtes mesurées peuvent appartenir à des ébauches d\'objets mais aussi à des corps solides. Les dimensions angulaires ne sont pas paramétriques.

Les Draft Dimensions peuvent être affichées sur une page de l\'[Atelier Techdraw](TechDraw_Workbench/fr.md) à l\'aide des commandes [TechDraw Vue Draft](TechDraw_DraftView/fr.md) ou [TechDraw Vue Arch](TechDraw_ArchView/fr.md). L\'[Atelier Techdraw](TechDraw_Workbench/fr.md) propose également ses propres commandes de cotation. Mais celles-ci créent des dimensions qui ne sont affichées que sur la page de dessin et non dans la [Vue 3D](3D_view/fr.md).

<img alt="" src=images/Screenshot_Draft_Dimension.jpg  style="width:400px;"> 
*Dimension linéaire définie par trois points*

## Créer

Voir aussi : [Draft La barre](Draft_Tray/fr.md), [Draft Accrochage](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

### Utilisation pour une dimension linéaire 

1.  Sélectionnez éventuellement une règle dans la [Vue 3D](3D_view/fr.md).
2.  Il existe plusieurs façons d\'invoquer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Dimension.svg" width=16px> [Créer une cote](Draft_Dimension/fr.md)**.
    -   Sélectionnez l\'option **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** dans le menu.
    -   Utilisez les raccourcis clavier : **D** puis **I**.
3.  Le panneau de tâches **Dimension** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
4.  Si vous n\'avez pas encore sélectionné d\'arête, effectuez l\'une des opérations suivantes :
    -   Appuyez sur **E** ou sur le bouton **<img src="images/view-select.svg" width=16px> sélection d'un bord** et sélectionnez une arête droite dans la [Vue 3D](3D_view/fr.md).
    -   Maintenez la touche **Alt** enfoncée, sélectionnez une arête droite dans la [Vue 3D](3D_view/fr.md) et relâchez la touche **Alt**.
    -   Définissez la distance mesurée en choisissant des points :
        -   Choisissez un premier point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
        -   Choisissez un deuxième point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
5.  Pour positionner la ligne de cote, effectuez l\'une des opérations suivantes :
    -   Pour une cote alignée :
        -   Choisissez un point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
    -   Pour une dimension horizontale :
        -   Déplacez le pointeur au-dessus ou au-dessous du bord ou des points.
        -   Maintenez la touche **Shift** enfoncée, déplacez le pointeur et choisissez un point dans la [Vue 3D](3D_view/fr.md).
    -   Pour une dimension verticale :
        -   Déplacez le pointeur à gauche ou à droite de l\'arête ou des points.
        -   Maintenez la touche **Shift** enfoncée, déplacez le pointeur et choisissez un point dans la [Vue 3D](3D_view/fr.md).

### Utilisation pour une dimension radiale 

1.  Sélectionnez éventuellement un bord circulaire dans la [Vue 3D](3D_view/fr.md).
2.  Il existe plusieurs façons d\'invoquer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Dimension.svg" width=16px> [Créer une cote](Draft_Dimension/fr.md)**.
    -   Sélectionnez l\'option **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** dans le menu.
    -   Utilisez le raccourci clavier : **D** puis **I**.
3.  Le panneau de tâches **Dimension** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
4.  Si vous n\'avez pas encore sélectionné d\'arête, effectuez l\'une des opérations suivantes :
    -   Appuyez sur **E** ou sur le bouton **<img src="images/view-select.svg" width=16px> sélection d'un bord** et sélectionnez une arête circulaire dans la [Vue 3D](3D_view/fr.md).
    -   Maintenez la touche **Alt** enfoncée, sélectionnez une arête circulaire dans la [Vue 3D](3D_view/fr.md) et relâchez la touche **Alt**.
5.  Pour positionner la ligne de cote, effectuez l\'une des opérations suivantes :
    -   Pour une cote de diamètre :
        -   Choisissez un point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
    -   Pour une dimension radiale :
        -   Maintenez la touche **Shift** et choisissez un point dans la [Vue 3D](3D_view/fr.md).

### Utilisation pour une dimension angulaire 

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Dimension.svg" width=16px> [Créer une cote](Draft_Dimension/fr.md)**.
    -   Sélectionnez l\'option **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** dans le menu.
    -   Utilisez le raccourci clavier : **D** puis **I**.
2.  Le panneau de tâches **Dimension** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Maintenez la touche **Alt** enfoncée, sélectionnez deux arêtes droites dans la [Vue 3D](3D_view/fr.md) et relâchez la touche **Alt**.
4.  Pour positionner l\'arc de cotes, sélectionnez un point dans la [Vue 3D](3D_view/fr.md).
5.  Selon les bords et le point choisi, l\'angle affiché sera l\'angle aigu (pointu) ou obtus (émoussé) entre les bords, ou l\'angle d\'un des bords avec l\'horizontale. Dans certains cas, vous devrez d\'abord ajouter une géométrie auxiliaire ([Draft Lignes](Draft_Line/fr.md) par exemple) pour obtenir un angle particulier.

### Options

Les raccourcis clavier à caractère unique disponibles dans le panneau des tâches peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md). Les raccourcis mentionnés ici sont les raccourcis par défaut.

-   Pour saisir manuellement des coordonnées, entrez les valeurs X, Y et Z et appuyez sur **Entrée** après chacune. Ou vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point** lorsque vous avez les valeurs souhaitées. Il est conseillé de déplacer le pointeur hors de la [Vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   Appuyez sur **R** ou cliquez sur la case **Relative** pour activer le mode relatif. Si le mode relatif est activé, les coordonnées sont relatives au dernier point, si disponible, sinon elles sont relatives à l\'origine du système de coordonnées.
-   Appuyez sur **G** ou cliquez sur la case **Global** pour activer le mode global. Si le mode global est activé, les coordonnées sont relatives au système de coordonnées global, sinon elles sont relatives au système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md). {{Version/fr|0.20}}
-   Appuyez sur **T** ou cliquez sur la case **Continue** pour activer le mode continu. Ce mode ne fonctionne que pour les dimensions linéaires. Si le mode continu est activé, la commande redémarre après avoir terminé, ce qui vous permet de continuer à créer des dimensions. Toutes les dimensions suivantes commenceront à partir du point final de la dimension précédente, et utiliseront la même ligne de base que la première dimension. Notez que la sélection des bords n\'est pas possible pour les dimensions suivantes.
-   Appuyez sur **S** pour activer ou désactiver [Draft Accrochage](Draft_Snap/fr.md).
-   Appuyez sur **Echap** ou sur le bouton **Fermer** pour terminer la commande.

## Convertir

### Utilisation

1.  Sélectionnez un ou plusieurs objets [Std Mesurer une distance](Std_MeasureDistance/fr.md).
2.  Il existe plusieurs façons d\'invoquer la commande :
    -   Appuyez sur le **<img src="images/Draft_Dimension.svg" width=16px> [Créer une cote](Draft_Dimension/fr.md)**.
    -   Sélectionnez l\'option **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** dans le menu.
    -   Utilisez le raccourci clavier : **D** puis **I**.
3.  Chaque objet sélectionné est remplacé par une Draft Dimension linéaire non paramétrique.

## Remarques

-   Les Draft Dimensions linéaires et radiales peuvent être éditées avec la commande [Draft Editer](Draft_Edit/fr.md).

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Dimension est dérivé d\'un objet [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Les propriétés suivantes sont supplémentaires, sauf indication contraire :

### Données dimension linéaire et radiale 


{{TitleProperty|Dimension}}

-    {{PropertyData/fr|Dimline|VectorDistance}}: spécifie le point par lequel passe la ligne de dimension.

-    {{PropertyData/fr|Linked Geometry|LinkSubList}}: spécifie l\'objet et son sous-élément, ou ses sous-éléments, auxquels la dimension est liée.

-    {{PropertyData/fr|Normal|Vector}}: spécifie la normale du plan du texte.

-    {{PropertyData/fr|Support|Link|hidden}}: spécifie l\'objet mesuré.


{{TitleProperty|Linear/radial dimension}}

-    {{PropertyData/fr|Direction|Vector}}: spécifie la direction de la mesure.

-    {{PropertyData/fr|Distance|Length}}: (en lecture seule) spécifie la valeur de la mesure.

-    {{PropertyData/fr|End|VectorDistance}}: spécifie le dernier point de la mesure.

-    {{PropertyData/fr|Start|VectorDistance}}: spécifie le point de départ de la mesure.


{{TitleProperty|Radial dimension}}

-    {{PropertyData/fr|Diameter|Bool}}: spécifie si une dimension radiale est affichée comme une dimension de diamètre. Si cela change, le symbole utilisé dans {{PropertyView/fr|Override}} doit être mis à jour manuellement (de {{Value|Ø}} à {{Value|R}} ou vice versa). Non utilisé pour les dimensions linéaires.

### Données dimension angulaire 


{{TitleProperty|Angular dimension}}

-    {{PropertyData/fr|Angle|Angle}}: (en lecture seule) spécifie la valeur de la mesure.

-    {{PropertyData/fr|Center|VectorDistance}}: spécifie le centre de la mesure.

-    {{PropertyData/fr|First Angle|Angle}}: spécifie le début de l\'angle de la mesure.

-    {{PropertyData/fr|Last Angle|Angle}}: spécifie la fin de l\'angle de la mesure.


{{TitleProperty|Dimension}}

-    {{PropertyData/fr|Dimline|VectorDistance}}: spécifie le point par lequel passe l\'arc de dimension.

-    {{PropertyData/fr|Linked Geometry|LinkSubList|hidden}}: non utilisé.

-    {{PropertyData/fr|Normal|Vecteur|hidden}}: spécifie la normale du plan de la dimension.

-    {{PropertyData/fr|Support|Link|hidden}}: non utilisé.

### Vue


{{TitleProperty|Annotation}}

-    {{PropertyView/fr|Annotation Style|Enumeration}}: spécifie le style d\'annotation appliqué à la dimension. Voir [Draft Éditeur styles d\'annotations](Draft_AnnotationStyleEditor/fr.md).

-    {{PropertyView/fr|Scale Multiplier|Float}}: spécifie le facteur d\'échelle général appliqué à la dimension.


{{TitleProperty|Display Options}}

-    {{PropertyView/fr|Display Mode|Enumeration}}: spécifie comment le texte est affiché. S\'il s\'agit de {{value|2D text}}, le texte sera affiché dans un plan défini par la {{PropertyData/fr|Normal}} de la mesure. S\'il s\'agit de {{value|3D text}}, le texte fera toujours face à la caméra. Notez que ces valeurs sont inversées par rapport à [Draft Texte](Draft_Text/fr.md). Il s\'agit d\'une propriété héritée.


{{TitleProperty|Graphics}}

-    **Arrow Size|Length**: spécifie la taille des symboles affichés aux extrémités de la ligne ou de l\'arc de dimension.

-    **Arrow Type|Enumeration**: spécifie le type de symbole affiché aux extrémités de la ligne ou de l\'arc de dimension, qui peut être {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} ou {{value|Tick-2}}.

-    **Dim Overshoot|Distance**: spécifie la longueur supplémentaire ajoutée à la ligne de cote. Non utilisé pour les cotes angulaires.

-    **Ext Lines|Distance**: spécifie la longueur des lignes d\'extension qui vont de la ligne de dimension aux points mesurés. Utilisez {{Value|0}} pour des lignes d\'extension complètes. Une valeur négative définit l\'écart entre les extrémités des lignes d\'extension et les points mesurés. Une valeur positive définit la longueur maximale des lignes d\'extension. Utilisé uniquement pour les dimensions linéaires.

-    **Ext Overshoot|Distance**: spécifie la longueur supplémentaire des lignes d\'extension au-delà de la ligne de cote. Non utilisé pour les dimensions angulaires.

-    **Flip Arrows|Bool**: indique s\'il faut inverser l\'orientation des symboles aux extrémités de la ligne de cote ou de l\'arc. Ne fonctionne que si les symboles sont des flèches.

-    **Line Color|Color**: spécifie la couleur de la dimension, y compris le texte.

-    **Line Width|Float**: spécifie la largeur des lignes ou de l\'arc appartenant à la dimension.

-    **Show Line|Bool**: spécifie s\'il faut afficher la ligne de la dimension. N\'affecte pas l\'affichage des lignes d\'extension et des dépassements. Non utilisé pour les dimensions angulaires.


{{TitleProperty|Text}}

-    {{PropertyView/fr|Flip Text|Bool}}: indique si l\'orientation du texte doit être inversée.

-    {{PropertyView/fr|Font Name|Font}}: spécifie la police utilisée pour dessiner le texte. Il peut s\'agir d\'un nom de police, tel que {{value|Arial}}, d\'un style par défaut tel que {{value|sans}}, {{value|serif}} ou {{value|mono}}, d\'une famille telle que {{value|Arial,Helvetica,sans}} ou d\'un nom avec un style tel que {{value|Arial:Bold}}. Si la police donnée n\'est pas trouvée sur le système, une police par défaut est utilisée à la place.

-    {{PropertyView/fr|Font Size|Length}}: spécifie la taille des lettres. Le texte peut être invisible dans la [Vue 3D](3D_view/fr.md) si cette valeur est très petite.

-    {{PropertyView/fr|Override|String}}: spécifie un texte personnalisé à afficher à la place de la mesure réelle. Utilisez la chaîne {{value|$dim}} à l\'intérieur du texte pour inclure la mesure.

-    {{PropertyView/fr|Text Position|VectorDistance}}: spécifie la position du texte en coordonnées absolues. {{Value|[0, 0, 0]}} affichera le texte dans sa position par défaut près de la ligne ou de l\'arc de dimension.

-    {{PropertyView/fr|Text Spacing|Length}}: spécifie l\'espace entre le texte et la ligne ou l\'arc de dimension.


{{TitleProperty|Units}}

-    **Decimals|Integer**: spécifie le nombre de décimales à afficher pour la mesure.

-    **Show Unit|Bool**: indique s\'il faut afficher l\'unité à côté de la valeur numérique de la mesure. Non utilisé pour les dimensions angulaires.

-    **Unit Override|String**: spécifie l\'unité dans laquelle exprimer la mesure, par exemple, {{value|km}}, {{value|m}}, {{value|cm}}, {{value|mm}}, {{value|mi}}, {{value|ft}}, {{value|in}} ou {{value|arch}} pour les unités arch. Laissez ce champ vide pour utiliser l\'unité par défaut. Non utilisé pour les dimensions angulaires.

## Script

Voir aussi: _.

Pour créer une Draft Dimension, utilisez la méthode `make_dimension` ({{Version/fr|0.19}}) du module Draft. Cette méthode remplace la méthode dépréciée `makeDimension`.


```python
dimension = make_dimension(p1, p2, p3=None, p4=None)```

Il existe plusieurs façons de faire appel à cette méthode, en fonction des arguments qui lui sont passés :


```python
dimension = make_dimension(p1, p2, p3=None)
dimension = make_dimension(object, i1, i2, p4=None)
dimension = make_dimension(object, i1, mode, p4=None)
```

-   Crée un `dimension` linéaire en mesurant la distance entre les points `p1` et `p2`.
-   Crée un `dimension` linéaire lié à `object`, mesurant la distance entre ses sommets indexés `i1` et `i2`.
-   Crée un `dimension` circulaire lié à `object`, avec `i1` étant l\'index du bord incurvé à mesurer et `mode` étant soit `"radius"` ou `"diameter"` pour spécifier le type de dimension.
    -   
        `p3`
        
        lors du premier appel et `p4` dans les deux autres, spécifiez un point facultatif par lequel la ligne de cote doit passer.

    -   Tous les points sont définis par leur `FreeCAD.Vector`.

Pour créer une cote angulaire, utilisez la méthode suivante :


```python
dimension = make_angular_dimension(center, angles, p3, normal=None)
dimension = make_angular_dimension(center, [angle1, angle2], p3, normal=None)
```

-   Crée une `dimension` angulaire à partir du point `center`, de la liste d\'`angles` entre deux éléments et le point `p3` par lequel l\'arc devrait passer.
    -   Si `angle1 > angle2`, l\'angle affiché est la différence `angle1 - angle2` sinon l\'angle complémentaire est affiché `360 - (angle2 - angle1)`.
    -   Les angles doivent être exprimés en radians. La fonction `math.radians()` peut être utilisée pour convertir des angles donnés en degrés.

Les propriétés de vue de `dimension` peuvent être modifiées en remplaçant ses attributs, par exemple en changeant `ViewObject.FontSize` avec la nouvelle taille en millimètres.

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(-2500, 0, 0)
dimension1 = Draft.make_dimension(p1, p2, p3)
dimension1.ViewObject.FontSize = 200

polygon = Draft.make_polygon(3, radius=1000)
doc.recompute()

p4 = App.Vector(-2000, 1500, 0)
dimension2 = Draft.make_dimension(polygon, 1, 2, p4)
dimension2.ViewObject.FontSize = 200

center = App.Vector(2000, 0, 0)
p5 = App.Vector(3000, 1000, 0)
angle1 = 45
angle2 = 10
dimension3 = Draft.make_angular_dimension(center, [angle1, angle2], p5)
dimension3.ViewObject.FontSize = 200

dimension4 = Draft.make_angular_dimension(center, [angle2, angle1], p5*1.2)
dimension4.ViewObject.FontSize = 200

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Dimension/fr
