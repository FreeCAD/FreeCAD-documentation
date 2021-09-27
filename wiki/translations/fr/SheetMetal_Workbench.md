# <img alt="Icône de l\'atelier externe Sheet Metal" src=images/Sheetmetal_workbench_icon.svg  style="width:64px;"> SheetMetal Workbench/fr


{{TOCright}}

## Introduction

<img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:32px;"> [Sheet Metal](SheetMetal_Workbench/fr.md) est un [atelier externe](External_workbenches/fr.md) et ne fait pas partie de l\'installation standard de FreeCAD. Il a été développé pour fournir des outils permettant de créer et de déplier des objets en tôle.

Les caractéristiques des objets en tôle sont :

-   Ils ont une épaisseur constante
-   Ils peuvent être dépliés, s\'ils sont constitués uniquement de parois planes et de connexions cylindriques.

L\'outil de dépliage, dans ses deux versions, n\'est pas limité aux pièces fabriquées à l\'aide des outils de cet atelier mais peut également traiter les objets des ateliers [Part](Part_Workbench/fr.md) et [PartDesign](PartDesign_Workbench/fr.md), pour autant qu\'ils répondent aux caractéristiques ci-dessus.

<img alt="" src=images/SheetMetal_Example.png  style="width:600px;"> 
* Le modèle en tôle construit avec l'add-on Sheet Metal (arrière plan); devant, le solide déplié; au premier plan, l'esquisse déplier avec des lignes de pliage pour l'exportation au format DXF.*

Si l\'exportation au format DXF est utilisée pour contrôler des machines (Lasercut par exemple), vous devez modifier le DXF pour supprimer les lignes indiquant les plis, ces lignes pouvant être utilisées pour la découpe par la machine.

## Installation

Cet atelier peut être installé à partir du [Gestionnaire d\'Addon](Std_AddonMgr/fr.md). Pour une installation manuelle, voir [Installer des ateliers supplémentaires](Installing_more_workbenches/fr.md).

## Outils

Une description détaillée (en anglais) des outils peut être trouvée [sur le blogue de l\'auteur](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/). Elle est un peu dépassée maintenant, car de nouveaux outils ont été ajoutés.

-   <img alt="" src=images/SheetMetal_AddBase.svg  style="width:32px;"> [Tôle de base](SheetMetal_AddBase/fr.md): crée une paroi en tôle à partir d\'une esquisse ouverte.

-   <img alt="" src=images/SheetMetal_AddWall.svg  style="width:32px;"> [Tôle pliée](SheetMetal_AddWall/fr.md): génère une tôle à partir d\'une face latérale d\'une tôle.

-   <img alt="" src=images/SheetMetal_Extrude.svg  style="width:32px;"> [Prolonger une face](SheetMetal_Extrude/fr.md): prolonge une face le long d\'une normale.

-   <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:32px;"> [Pli sur tôle](SheetMetal_AddFoldWall/fr.md): plie une face sur la ligne choisie avec un rayon de courbure spécifié.

-   <img alt="" src=images/SheetMetal_Unfold.svg  style="width:32px;"> [Déplier](SheetMetal_Unfold/fr.md): aplatit un objet en tôle pliée et génère un solide et une esquisse (fournit une boîte de dialogue pour définir les paramètres).

-   <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:32px;"> [Déplier sans assistance](SheetMetal_UnattendedUnfold/fr.md) : Aplatit un objet en tôle pliée et génère un solide et une esquisse (si les paramètres ont déjà été définis).

-   <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:32px;"> [Grugeage rond du coin](SheetMetal_AddCornerRelief/fr.md): ajoute un perçage pour gruger un coin.

-   <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:32px;"> [Grugeage carré](SheetMetal_AddRelief/fr.md): ajoute une découpe carré à un coin.

-   <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:32px;"> [Découpe d\'angle](SheetMetal_AddJunction/fr.md): découpe un espace dans l\'angle de deux parois.

-   <img alt="" src=images/SheetMetal_AddBend.svg  style="width:32px;"> [Transformation en pli](SheetMetal_AddBend/fr.md): plie une face suivant une ligne choisie.

-   <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:32px;"> [Perçage de paroi](SheetMetal_SketchOnSheet/fr.md): découpe un trou dans la tôle à partir d\'une esquisse.

-   <img alt="" src=images/SheetMetal_Forming.svg  style="width:32px;"> [Outil d\'emboutissage](SheetMetal_Forming/fr.md): crée un outil de formage.

## Description sommaire 

Cet atelier fournit des outils pour les deux tâches principales :

-   Créer des objets en tôle
-   Déplier des objets en tôle

Cette section est destinée à donner une idée générale de la façon d\'utiliser les outils fournis. Des informations plus détaillées peuvent être trouvées sur la page de chaque outil (voir ci-dessus) ou dans les tutoriels liés (voir ci-dessous).

### Créer un objet en tôle 

#### Débuter avec un profil 

1.  Create an open polyline (preferably with the sketcher)
2.  Use the <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Make Base Wall](SheetMetal_AddBase.md) command to create a sheet metal profile.

#### Start with a blank 

1.  Create a closed polyline (preferably with the sketcher)
2.  Use the <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Make Base Wall](SheetMetal_AddBase.md) command to create a sheet metal blank.

#### Start with a PartDesign Pad 

1.  Create a closed polyline (preferably with the sketcher)
2.  Use the <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Pad](PartDesign_Pad.md) command to create a prismatic body.
3.  The <img alt="" src=images/PartDesign_Thickness.svg  style="width:16px;"> [PartDesign Thickness](PartDesign_Thickness.md) command will make it an object of constant thickness.
4.  To make it unfoldable it needs some gaps or connections between the walls:
    1.  The <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> [Make Relief](SheetMetal_AddRelief.md) command will cut off selected corners.
    2.  The <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> [Make Junction](SheetMetal_AddJunction.md) command will create junctions with gaps between adjoining walls that need to be disjoined.
    3.  The <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> [Make Bend](SheetMetal_AddBend.md) command will create cylindrical connections for the remaining walls that need to stay joined.

Some parameters will be inherited from the parent object(s) but it is better to check the relevant parameters at each stage.

It should now be checked if the resulting sheet metal object can be unfolded. (see [Unfold\...](#Unfold_a_sheet_metal_object.md) below).

#### Adding more features 

The unfoldable basic sheet metal objects can be extended:

1.  Use the <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> [Extend Face](SheetMetal_Extrude.md) command to enlarge walls.
2.  The <img alt="" src=images/SheetMetal_AddWall.svg  style="width:16px;"> [Make Wall](SheetMetal_AddWall.md) command will add new walls to the existing object.
3.  Use the <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:16px;"> [Add Corner Relief](SheetMetal_AddCornerRelief.md) command to add or reshape corner reliefs.
4.  The <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:16px;"> [Fold a Wall](SheetMetal_AddFoldWall.md) command will fold a wall at a chosen line, i.e. it will trimm a wall at said line, relocate the cut away side, and rejoin them with a cylindrical connection.
5.  Use the <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> [Sketch on Sheet metal](SheetMetal_SketchOnSheet.md) command to cut holes into the object starting on a chosen wall and then following the adjoined walls and connections.
6.  The <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Make Forming in Wall](SheetMetal_Forming.md) command will stamp a shape into a wall.

Several tools from other workbenches can be used to add holes or to reshape edges.

### Unfold a sheet metal object 

To unfold a sheet metal object aktivate the <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> _ tool.

The result will be a 3D object with an optional outline sketch including bend lines.

### Examples

Until tutorial pages are available on this wiki there is an [Examples](SheetMetal_Examples.md) page.

<img alt="" src=images/SheetMetal_Example-01.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-02.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-03.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-04.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-05.png  style="width:100px;">

## Limitations

-   L\'atelier est affecté par le problème de [nommage topologique](Glossary/fr#Topological_Naming.md) inhérent à FreeCAD. Si l\'édition d\'un pli plus tôt dans l\'historique de la pièce renumérote les faces, alors les plis suivants peuvent être affectés et changer de face. Si les entités de pliage ne se cassent pas, vous pouvez double-cliquer dessus pour obtenir une boîte de dialogue dans laquelle vous pouvez sélectionner la face appropriée dans la [vue 3D](3D_view/fr.md) et mettre à jour le pliage.
-   L\'outil Unfold (Dépliage) présente certaines limitations et échouera dans certaines situations complexes. En cas d\'échec, essayez de sélectionner une face différente.
-   Cas fréquent de crash : prenez beaucoup de précautions pour ne pas couper dans les charnières (les plis) le long des faces ou dans les angles ,ni de faire des trous ou des encoches dans les angles.

## Tutoriels


<div class="mw-collapsible mw-collapsed toccolours" style="width:800px">

### Tutoriel de tôlerie par meme2704 

Le tutoriel suivant est reproduit à partir du tutoriel PDF mentionné dans [Liens](#Liens.md).


<div class="mw-collapsible-content">

#### Présentation de l\'atelier 

Après avoir téléchargé et installé l\'extension, l\'ouvrir. ![](images/sm1.png )

#### 1st operation 


<div class="mw-translate-fuzzy">

#### 1ère opération 

-   Obtenez la base: utilisez soit les ateliers \"pièce\" ou \"brouillon\", faites 1 croquis qui contiendra tous les trous et toutes les coupes, extrudez cette base à l\'épaisseur de la feuille.
-   Gardez à l\'esprit que les bords seront toujours en plus des rayons de pliage.


</div>

![](images/sm2.png )

#### 2nd operation 


<div class="mw-translate-fuzzy">

#### 2ème opération 

-   Ouvrez l\'atelier Sheet\_metal.
-   Sélectionnez 1 épaisseur du bord (arête) de la plaque de base et cliquez sur l\'outil \"bend\" 90°/ L\'angle de courbure par défaut peut être modifié de 0 à 90°.
-   La hauteur des bords est de 10 mm par défaut, modifiable de 0,1 à xxxmm.
-   Le rayon de cintrage est par défaut égal à l\'épaisseur, modifiable de 0,1 à xxmm (ne jamais mettre 0).
-   Gap1, gap2 est le retrait du bord plié du coin de la base (0 accepté).
-   Inverser par défaut: false se replie en Z +, true en ZReliefd coupe le coin entre le pli et la base (inactif si gap = 0).
-   Reliefw ajoute 1 fente entre la base et le bord (inactive si reliefd = 0).


</div>

![](images/sm3.png ) Répétez autant de fois qu\'il y a de côtés à plier.
Plier 1 retour en utilisant \"étendre\".
![](images/sm4a.png ) Pour ajouter 1 retour, répétez la même opération en sélectionnant l\'épaisseur du bord concerné.
Pour réduire l\'espace entre les deux bords, utilisez \"extends\".
Sélectionnez l\'épaisseur et spécifiez la longueur à ajouter.
Notez que si l\'extension du 1er bord est faite avant le pli du retour, il ne sera pas pris en compte, si 1 pli identique est ajouté à l\'extension, il apparaîtra correct mais le dépliage ne sera pas fait.
Pliage d\'un 2ème bord:
Maintenant nous devons séparer les 2 bords sinon ils vont fusionner et le déploiement sera impossible.
\* 1ère méthode: faire 1 retrait de 1 bord.

-   -   Donne 1 valeur légèrement supérieure à gap1 (ou gap2), à zéro il y a toujours fusion.

-   2ème méthode faire 1 coupe à 45 ° voir plus loin, utiliser cet outil.

![](images/sm5a.png )

#### Unfolding


<div class="mw-translate-fuzzy">

#### Dépliage

Choisissez 1 face de référence (ici la face orange) et cliquez sur le bouton dans la barre d\'outils.
Nous obtenons la partie bleue dont il suffit de modifier les valeurs X, Y ou Z pour le voir en totalité.


</div>

![](images/sm6.png )

#### Cut the flaps at 45° 


<div class="mw-translate-fuzzy">

#### Couper les retours à 45 ° 

Après avoir plié les retours sans avoir fait de retrait, la forme apparaît ainsi.


</div>

![](images/sm7a.png ) Pour ce faire, il doit se diviser à 45 ° (ou suivant les bissectrices pour les largeurs inégales).
\* Créer 1 nouveau sketch lié à la partie commune aux 2 volets.

-   Créer 1 arrêt lié en sélectionnant le bord extérieur de la \"charnière\".(important)

Dessinez 1 triangle dont le haut est contraint à la fin, orienté 1 côté à 45 °, donnez au petit côté 1 largeur minimum (0.1mm suffit), et faites 1 pocket.
Veillez à ne pas érafler la \"charnière\" où la nudité de lier la pointe du triangle au bord de la ligne de pliage. ![](images/sm8a.png ) Dépliage ![](images/sm9.png )

#### Piercing edges and flaps 


<div class="mw-translate-fuzzy">

#### Perçage des bords et des rabats 

Faites ces trous et coupes après le pliage et avant le dépliage.
Veillez toujours à ne pas \"érafler\" ou couper les lignes de pliage.


</div>

![](images/sm10.png )

#### Make wired flaps 


<div class="mw-translate-fuzzy">

#### Faire des rabats tangents 

Faire 1 pli sur le bord du coté, à 45 ° de 0.1mm de long, puis 1 autre inverse à 45 ° de la longueur du rabat contigu, puis étendre le coté opposé, il passera et ils ne seront pas confondus.


</div>

![](images/sm11.png )

#### Special case of this same pierced edge 


<div class="mw-translate-fuzzy">

#### Cas particulier de ce même bord percé 

Dans ce cas particulier, le dépliage ne fonctionne qu\'en choisissant la face jaune comme référence.


</div>

![](images/sm12.png )

#### Special case hole straddling the folds 


<div class="mw-translate-fuzzy">

#### Cas spécial de trou enjambant les plis 

Auparavant, il est dit plusieurs fois qu\'il est interdit de couper les lignes de pliage.
Comment faire ?


</div>

![](images/sm13.png )

-   Faire la base avec son trou demi-rond et faire les 2 demi-faces et les 2 demi-plis séparément.
-   Faites ensuite 1 extension sur 1 des côtés de la largeur de l\'ouverture moins 0.1mm, les 2 bords restent ainsi séparés.
-   Puis sur cette extension (en vert) dessiner le contour de la coupe et faire 1 poche
-   Le résultat est le morceau rouge ci-dessus, et le dépliage fonctionne, reste la ligne qui séparait les 2 bords précédemment

![](images/sm14.png )


</div>


</div>

## Videos


<div class="mw-translate-fuzzy">


{{TOCright}}


</div>

## Liens


<div class="mw-translate-fuzzy">

-   [Macro Sheet Metal Unfolder](Macro_Sheet_Metal_Unfolder/fr.md) macro originale sur laquelle l\'outil Unfold est basé.
-   Annonce du [Sheet Metal Workbench](http://forum.freecadweb.org/viewtopic.php?t=11303) (EN) sur le forum FreeCAD
-   [Un tutoriel en français et en anglais au format PDF](https://forum.freecadweb.org/viewtopic.php?f=3&t=25002) sur le forum FreeCAD
-   Fichiers:
-   Signalement des bogues/demande de fonctionnalités: <https://github.com/shaise/FreeCAD_SheetMetal/issues>


</div>

## Références

-   Auteur:
    -   Outils de pliage: Copyright 2015-2018 par Shai Seger
    -   Outil de dépliage: Copyright 2014 par Ulrich Brammer
-   Licence: [GPLv3](https://www.gnu.org/licenses/gpl-3.0.fr.html)
-   Blog officiel (EN): [Sheet metal Addon for FreeCAD](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/)
-   Code source sur github: <https://github.com/shaise/FreeCAD_SheetMetal>

_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal Workbench/fr
