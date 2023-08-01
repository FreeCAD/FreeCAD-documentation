# Sketcher Examples/fr
{{TOCright}}

## Introduction

Je pense que l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [atelier Sketcher](Sketcher_Workbench/fr.md) a besoin de quelques exemples qui ne sont pas des tutoriels détaillés ou des vidéos\...



## Charnière film 

Une charnière film est le petit morceau de plastique pliable qui relie les deux côtés d\'un objet moulé par injection, tel qu\'un conduit avec un couvercle, ou les deux moitiés d\'un boîtier de bouchon protégeant de la poussière.

Cet exemple utilise une sorte d\'esquisse principale pour empiler des esquisses dépendantes. Il montre également comment attacher et animer un simple clip basé sur les fonctions de <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench/fr.md) et les contraintes de <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketcher](Sketcher_Workbench/fr.md). L\'utilisation des <img alt="" src=images/Bound-expression.svg  style="width:16px;"> [expressions](Expressions/fr.md) comme décrit ci-dessous nécessite FreeCAD **V 0.21 ou plus**.



### Esquisse de base 

En général, un objet est modélisé dans un environnement fermé. Plus tard, la partie mobile doit être retournée de 180° pour être moulée à l\'état ouvert.
La bande pliable est représentée par un arc de cercle pour l\'état fermé et par une ligne droite pour l\'état ouvert, les deux ayant le même point de départ.
Le point médian d\'une ligne reliant les deux extrémités indique la position de l\'axe de retournement, qui est normal au plan de l\'esquisse. (Il est placé sur l\'origine de l\'esquisse afin que l\'axe global normal au plan de l\'esquisse puisse être utilisé comme axe de basculement).


<div class="mw-collapsible mw-collapsed">

(Quelques explications supplémentaires cachées et une description du flux de travail peuvent être développées ici. \--\>

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:400px;"> 
*Esquisse maître et charnière du film final animé (cliquez sur l'image si l'animation s'est arrêtée après quelques répétitions)*


<div class="mw-collapsible-content toccolours">

Pour un demi-cercle, la longueur de l\'arc est le rayon multiplié par Pi (*l = r \* Pi*). Le rayon est appelé NeutralRadius et la ligne est appelée DevelopedLength. Une expression pour la longueur développée relie les deux valeurs : `.Constraints.NeutralRadius * pi`

:   Dans la même esquisse, une expression commence par un `.` suivi de ValueType.ValueName pour traiter une autre valeur.


</div>



### Esquisse intermédiaire 

L\'arc de cette charnière film a une longueur constante et un rayon variable. Une entrée est le NeutralRadius de l\'esquisse de base. Pour l\'avoir à portée de main dans cette esquisse, il est lié en tant que <img alt="" src=images/Sketcher_External.svg  style="width:16px;"> [géométrie externe](Sketcher_External/fr.md) ayant une dimension de référence appelée ReferenceRadius.


<div class="mw-collapsible-content toccolours">

Un quartier de géométrie de construction affiche la relation entre l\'arc et le rayon pour un angle donné.
**InputLength = ReferenceRadius \* Pi**
et
**ArcLength = DynamicRadius \* Pi \* ArcAngle / 180°**
de longueur constante se traduit par :
**ReferenceRadius \* Pi = DynamicRadius \* Pi \* ArcAngle / 180°**
et avec Pi éliminé, nous obtenons :
**ReferenceRadius = DynamicRadius \* ArcAngle / 180°** or **DynamicRadius = ReferenceRadius \* 180° / ArcAngle**

:   L\'<img alt="" src=images/Bound-expression.svg  style="width:16px;"> [expression](Expressions/fr.md) pour la valeur DynamicRadius : `.Constraints.ReferenceRadius * 180 ° / .Constraints.ArcAngle`

Une charnière film étant généralement symétrique, un autre arc avec le même point central, appelé HalfArc, est utilisé pour la sortie et représente une moitié de l\'arc de la charnière.

:   L\'<img alt="" src=images/Bound-expression.svg  style="width:16px;"> [expression](Expressions/fr.md) pour la valeur HalfArc : `.Constraints.ArcAngle / 2`


</div>

<img alt="" src=images/Sketcher_ExampleHinge-02.png  style="width:400px;"> 
*Esquisse intermédiaire montrant le DynamicRadius de l'arc de la charnière de 4 (mm) à un angle donné de 45° (et le demi-arc pour la sortie)*



### Esquisse de la charnière film 

Cette esquisse définit l\'épaisseur et la géométrie adjacente de la charnière film. Par conséquent, nous chargeons le demi-arc de l\'esquisse intermédiaire en tant que géométrie externe afin de l\'utiliser comme base pour la partie film. (une fraction de 180° dans ce cas)

Cette charnière film est destinée à maintenir les parties connectées en contact l\'une avec l\'autre lorsqu\'elles sont fermées. Pour ce faire, il suffit de calculer un arc de cercle de la longueur nécessaire, puis de créer une bande d\'épaisseur constante et enfin d\'appliquer des filets à l\'endroit où la bande rencontre les moitiés de l\'objet. La dernière étape raccourcit d\'une certaine manière la boucle, mais dans le monde réel, ce n\'est pas un problème, car l\'arc ne sera jamais circulaire et les filets ont donc une influence sur la courbure de l\'arc, mais pas sur sa fonctionnalité.

<img alt="" src=images/Sketcher_ExampleHinge-03.png  style="width:400px;"> 
*Esquisse de la charnière montrant le contour de la charnière sur la base de la géométrie extérieure à partir du demi-arc de cercle de l'esquisse intermédiaire.*

<img alt="" src=images/Sketcher_ExampleHinge-04.png  style="width:300px;"> <img alt="" src=images/Sketcher_ExampleHinge-05.png  style="width:300px;"> 
*A gauche : <img src="images/PartDesign_Pad.svg" width=16px> [protrusion](PartDesign_Pad.md) de la demi-charnière avec esquisse visible. A droite : demi-charnière avec ajout de <img src="images/PartDesign_Fillet.svg" width=16px> [congés](PartDesign_Fillet/fr.md)*

<img alt="" src=images/Sketcher_ExampleHinge-06.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-07.png  style="width:300px;"> 
*Demi-charnière avec plan de symétrie sélectionné → charnière film [symétrisée](PartDesign_Mirrored/fr.md)*

Conseil : <img alt="" src=images/Part_Mirror.svg  style="width:16px;"> [Part Miroir](Part_Mirror/fr.md) n\'accepte que les trois plans de base et ne peut donc pas être utilisé dans ce cas.

:   (Rétrospectivement, il était judicieux de commencer cet exemple avec la combinaison de PartDesign et de Sketcher).

Enfin, deux paramètres définissent la taille de la charnière-film :

-   le NeutralRadius de l\'esquisse de base
-   la valeur de l\'épaisseur de l\'esquisse de la charnière-film



### Fléchir la charnière film 

L\'angle de courbure est contrôlé par la contrainte ArcAngle de l\'esquisse intermédiaire et peut être modifié dans son éditeur de propriétés.
Mais nous sommes de vrais concepteurs et nous avons nommé correctement les contraintes et les dimensions de nos esquisses, ce qui nous permet de contrôler l\'angle de pliage via Python.
Quelques lignes de code de base à intégrer dans un contexte d\'interface graphique pourraient ressembler à ceci :


```python
doc=App.ActiveDocument
sketch=doc.getObjectsByLabel('IntermediateSketch')[0]
 ...
sketch.getDatum('ArcAngle')
 ...
sketch.setDatum('ArcAngle',App.Units.Quantity('50.000000 deg'))
doc.recompute(None,True,True)
```


<div class="mw-collapsible-content toccolours">

Une brève explication :

-    {{Incode|doc {{=}}App.ActiveDocument}} : pour adresser le document actif par un alias appelé **doc**

-    {{Incode|sketch {{=}}doc.getObjectsByLabel(\'IntermediateSketch\')\[0\]}} : pour adresser l\'esquisse concernée par l\'alias **sketch**.

-   : La méthode **getObjectsByLabel()** renvoie une liste d\'objets et nous devons suffixer l\'index {{value|0}} pour choisir le premier objet de la liste. (Nous ne nous attendons pas à ce qu\'un autre objet ait le même label et nous n\'avons donc pas à nous préoccuper des autres éléments de la liste).

-    {{Incode|sketch.getDatum('ArcAngle')}}: renvoie la valeur en cours de la contrainte dimensionnelle **ArcAngle** (dans la vue rapport).

-    {{Incode|sketch.setDatum('ArcAngle', App.Units.Quantity('50.0 deg'))}}: définit la valeur de **ArcAngle** à {{value|50°}}

-    {{Incode|doc.recompute(None,True,True)}}: pour mettre à jour l\'ensemble du document afin d\'afficher également les modifications de la géométrie dépendante.


</div>



### Connexion de la géométrie 

Les deux moitiés du truc du clip attendent d\'être fixées à la charnière, l\'une du côté statique et l\'autre du côté mobile.

<img alt="" src=images/Sketcher_ExampleHinge-08.png  style="width:300px;"> 
*Deux moitiés d'un simple clip*


<div class="mw-collapsible-content toccolours">

Le côté statique est facile :

1.  Activez le corps et ajustez les propriétés de position et d\'orientation dans l\'éditeur de propriétés jusqu\'à ce qu\'il corresponde à la charnière du film.
2.  Activez le corps de la charnière.
3.  Sélectionnez l\'<img alt="" src=images/PartDesign_Boolean.svg  style="width:16px;"> [opération booléenne](PartDesign_Boolean/fr.md) avec l\'option (par défaut) Union.
4.  Dans la boîte de dialogue, appuyez sur le bouton **Ajouter un corps**.
5.  Sélectionnez le **corps** de la moitié statique du clip.
6.  Appuyez sur OK pour terminer et fermer la boîte de dialogue.


</div>

<img alt="" src=images/Sketcher_ExampleHinge-09.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-10.png  style="width:300px;"> 
*Charnière film et moitié statique en position de modélisation → charnière film avec la moitié statique repositionnée et [unie](PartDesign_Boolean/fr.md)*


<div class="mw-collapsible-content toccolours">

Mais le côté mobile est différent : la moitié concernée de la géométrie du clip doit se déplacer dans la bonne position avant que le (re)calcul d\'une opération Union ne commence.

A ce stade, il me manque une fonction \"Attachment with offset\" comme celle d\'Assembly3 pour attacher la géométrie du clip à l\'une des faces mobiles. Mais après quelques expériences et ajustements, j\'ai trouvé une solution :

-   Les conteneurs <img alt="" src=images/Std_Part.svg  style="width:16px;"> [Std Part](Std_Part/fr.md) et <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [PartDesign Corps](PartDesign_Body/fr.md) ne sont pas pris en charge par <img alt="" src=images/Part_EditAttachment.svg  style="width:16px;"> [Part Ancrage](Part_EditAttachment/fr#Limitations.md).

Bien qu\'il soit possible d\'utiliser l\'ancrage pour les aligner, l\'ancrage ne sera pas paramétriquement lié.

-   L\'ancrage peut être appliqué à une fonction PartDesign. Cet élément et les éléments qui en dépendent sont repositionnés en fonction de la géométrie de base. Mais !
    -   Les éléments indépendants de PartDesign ne bougeront pas, ce qui modifiera la forme résultante et la cassera à la fin.
    -   Il est conseillé de garder les fonctions indépendantes pour éviter les impacts dus au [problème de dénomination topologique](Topological_naming_problem.md).
-   <img alt="" src=images/PartDesign_Clone.svg  style="width:16px;"> [PartDesign Clone](PartDesign_Clone/fr.md) crée un corps avec une seule fonction qui peut être utilisée avec l\'ancrage.

Dans cette idée, un flux de travail pourrait ressembler à ce qui suit :

1.  Sélectionner le corps de la moitié mobile.
2.  Utilisez la commande <img alt="" src=images/PartDesign_Clone.svg  style="width:16px;"> [Clone](PartDesign_Clone/fr.md).
3.  Dans le nouveau corps, sélectionnez l\'objet Clone dans la vue en arborescence.
4.  Utilisez la commande <img alt="" src=images/Part_EditAttachment.svg  style="width:16px;"> [Part Ancrage](Part_EditAttachment/fr.md) pour ajouter des propriétés d\'ancrage à l\'objet Clone.
5.  La boîte de dialogue Ancrage s\'ouvre.
    -   Sélectionnez un sommet pour l\'origine.
    -   Sélectionnez une arête pour la première direction.
    -   Sélectionnez une arête pour la deuxième direction.
    -   Examinez les modes d\'ancrage pour trouver celui qui convient le mieux.
    -   Ajustez les valeurs de rotation et de coordonnées jusqu\'à ce que la géométrie soit à nouveau en position de modélisation.
6.  Appuyez sur OK pour fermer la boîte de dialogue.
7.  Avec le corps de la charnière toujours actif, sélectionnez l\'<img alt="" src=images/PartDesign_Boolean.svg  style="width:16px;"> [opération booléenne](PartDesign_Boolean/fr.md).
8.  Dans la boîte de dialogue, cliquez sur le bouton **Ajouter un corps**.
9.  Sélectionnez le corps de la moitié mobile.
10. Appuyez sur OK pour terminer et fermer la boîte de dialogue.


</div>


</div>

<img alt="" src=images/Sketcher_ExampleHinge-14.png  style="width:300px;"> 
*La moitié mobile sera <img src="images/Part_EditAttachment.svg" width=16px> [ancrée](Part_EditAttachment/fr.md) à un coin du côté de la charnière mobile (Mode associé OXZ : sommet, arête, arête)*

Rétrospectivement, il aurait été plus judicieux de fournir la géométrie d\'ancrage avec l\'esquisse intermédiaire afin d\'éviter une autre source de [problème de dénomination topologique](Topological_naming_problem.md).

<img alt="" src=images/Sketcher_ExampleHinge-11.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-12.png  style="width:300px;"> 
*Le clip jusqu'à présent et la moitié mobile en position de modélisation → clip terminé avec la moitié mobile [ancrée](Part_EditAttachment/fr.md) et [unie](PartDesign_Boolean/fr.md)*

Le résultat devrait être un seul clip solide, qui peut être fermé et ouvert en changeant l\'ArcAngle de la charnière film. Angles autorisés : 0,1° à 180°, la section film ne doit pas devenir droite et, plus que fermé cela n\'a pas de sens. (À 180°, l\'objet peut être fusionné dans les zones tangentes ou de chevauchement, mais un petit écart supplémentaire peut être utile si cela n\'est pas acceptable).

<img alt="" src=images/Sketcher_ExampleHinge-13.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Sketcher_ExampleHinge-16.png  style="width:200px;"> 
*Clip presque fermé → Clip à moitié fermé → Clip prêt à être moulé*


{{PartDesign Tools navi

}} {{Sketcher Tools navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Examples/fr
