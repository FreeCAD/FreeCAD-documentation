---
- GuiCommand   */fr
   Name   *SheetMetal AddCornerRelief
   Name/fr   *SheetMetal Grugeage rond
   MenuLocation   *SheetMetal → Add Corner Relief
   Workbenches   *[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut   ***C** **R**
---

# SheetMetal AddCornerRelief/fr

## Description

La commande <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width   *24px;"> **SheetMetal AddCornerRelief** ajoute un grugeage circulaire pour gruger un coin. Un grugeage est généralement créé dans les coins où deux pliures se rencontrent, mais la commande peut également créer un grugeage dans un coin ouvert.

La commande ne peut créer qu\'un seul grugeage à la fois.

<img alt="" src=images/SheetMetal_AddCornerRelief-01.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-02.png  style="width   *300px;"> 
*Coin par défaut de deux pliures → Coin avec un grugeage*

<img alt="" src=images/SheetMetal_AddCornerRelief-03.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-04.png  style="width   *300px;"> 
*Coin par défaut de deux pliures → Coin ouvert avec un grugeage*

## Utilisation

1.  Sélectionnez deux bords d\'un coin.
2.  Lancez la commande <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width   *16px;"> **SheetMetal AddCornerRelief** en utilisant l\'une des méthodes suivantes    *
    -   Le bouton **<img src="images/SheetMetal_AddCornerRelief.svg" width=16px> [Add Corner Relief](SheetMetal_AddCornerRelief/fr.md)**.
    -   L\'option de menu **SheetMetal → <img src="images/SheetMetal_AddCornerRelief.svg" width=16px> Add Corner Relief**.
    -   Le raccourci clavier    * **C** puis **R**.

## Formes de grugeage 

La forme d\'un coin de grugeage peut être modifiée en changeant les valeurs de ses propriétés    *

La valeur de la propriété **ReliefSketch** peut être choisie parmi une liste    * {{value|Circle}} (par défaut), {{value|Circle-Scaled}}, {{value|Square}}, {{value|Square-Scaled}}, {{value|Sketch}}.

-    {{value|Circle}}et {{value|Square}} utilisent la valeur de la propriété **Size** pour mettre le grugeage à l\'échelle.

-    {{value|Circle-Scaled}}et {{value|Square-Scaled}} utilisent la valeur de la propriété **Size Ratio** pour mettre le grugeage à l\'échelle.

-    {{value|Sketch}}active l\'utilisation de l\'esquisse listée dans la propriété **Sketch** pour définir la forme du grugeage.

<img alt="" src=images/SheetMetal_AddCornerRelief-05.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-06.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-07.png  style="width   *200px;"> 
*Grugeage circulaire (paramètres par défaut) → Grugeage carré (paramètres par défaut) → Grugeage basé sur des esquisses.*

## Un regard plus attentif sur les tailles de grugeage 

Pour avoir une idée de comment et où le grugeage est placé, nous déplions un coin par défaut sans grugeage.

<img alt="" src=images/SheetMetal_AddCornerRelief-08.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-09.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-10.png  style="width   *200px;">



*Coin par défaut de deux pliures → Coin du solide déplié → Coin en vue de dessus.*

L\'étape suivante consiste à ouvrir l\'esquisse de dépliage, à créer un cercle à travers 3 points et à ajouter une dimension de rayon.
Maintenant, nous ajoutons un grugeage d\'angle, créons le solide de dépliage correspondant et ouvrons à nouveau la première esquisse de dépliage.
L\'ajout d\'un cercle concentrique de 3 mm de rayon révèle que nous avons trouvé comment le cercle interne est positionné car le nouveau cercle s\'insère parfaitement dans la découpe du solide de dépliage du grugeage.

<img alt="" src=images/SheetMetal_AddCornerRelief-11.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-12.png  style="width   *300px;">



*Coin par défaut avec esquisse dépliée → Coin avec grugeage par défaut et la même esquisse dépliée*

Si vous essayez de définir la propriété **Size** à une valeur inférieure à la valeur déterminée de 1,67 mm, vous obtiendrez une erreur ; toute valeur supérieure devrait fonctionner correctement.

En passant à Circle-Scaled et en créant un autre solide non plié, on constate que 1,67 mm est également la base de la propriété **Size Ratio**.

## Remarques

-   Le facteur k définit l\'emplacement de l\'axe neutre dans l\'épaisseur d\'une tôle.

   *   (Il serait bon de savoir si ce facteur est conforme à la norme ISO ou ANSI\...)

## Propriétés

Voir aussi    * [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Grugeage est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes    *

### Données


{{Properties_Title|Base}}

-    **Base Feature|Link|hidden**   * Fonctionnalité de base. Lien vers la caractéristique parent.

-    **_Body|LinkHidden|hidden**   * Lien caché vers le corps du parent.


{{Properties_Title|Parameters}}

-    {{PropertyData/fr|ReliefSketch|Enumeration}}   * \"Type de relief d\'angle\". {{value|Circle}} (par défaut), {{value|Circle-Scaled}}, {{value|Square}}, {{value|Square-Scaled}}, {{value|Sketch}}.

-    {{PropertyData/fr|Size|Length}}   * \"Taille de la forme\". Valeur par défaut    * {{value|3,00 mm}}.

-    {{PropertyData/fr|Size Ratio|Float}}   * \"Rapport de taille de la forme\". Valeur par défaut    * {{value|1,50}}.

-    {{PropertyData/fr|base Object|LinkSub}}   * \"Objet de base\". Liens vers la paire d\'arêtes définissant la position du Corner Relief.

-    {{PropertyData/fr|kfactor|FloatConstraint}}   * \"Position de l\'axe neutre\". Valeur par défaut    * {{value|0,50}}.


{{Properties_Title|Parameters1}}

-    {{PropertyData/fr|Sketch|Link}}   * \"Esquisse du relief de l\'angle\".

-    {{PropertyData/fr|XOffset|Distance}}   * \"Ecart par rapport au premier côté\". Valeur par défaut    * {{value|0,00 mm}}.

-    {{PropertyData/fr|YOffset|Distance}}   * \"Ecart du côté deux\". Valeur par défaut    * {{value|0,00 mm}}.




[Category   *SheetMetal](Category_SheetMetal.md) [Category   *Addons](Category_Addons.md) [Category   *External Command Reference](Category_External_Command_Reference.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddCornerRelief/fr
