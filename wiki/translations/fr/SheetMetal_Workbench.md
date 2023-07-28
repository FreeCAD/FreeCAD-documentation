# SheetMetal Workbench/fr
}

<img alt="Icône de l\'atelier externe Sheet Metal" src=images/Sheetmetal_workbench_icon.svg  style="width:128px;">


{{TOCright}}



## Introduction

<img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:32px;"> [Sheet Metal](SheetMetal_Workbench/fr.md) est un [atelier externe](External_workbenches/fr.md) et ne fait pas partie de l\'installation standard de FreeCAD. Il a été développé pour fournir des outils permettant de créer et de déplier des objets en tôle.

Les caractéristiques des objets en tôle sont :

-   Ils ont une épaisseur constante
-   Ils peuvent être dépliés, s\'ils sont constitués uniquement de parois planes et de connexions cylindriques.

L\'outil de dépliage, dans ses deux versions, n\'est pas limité aux pièces fabriquées à l\'aide des outils de cet atelier mais peut également traiter les objets des ateliers [Part](Part_Workbench/fr.md) et [PartDesign](PartDesign_Workbench/fr.md), pour autant qu\'ils répondent aux caractéristiques ci-dessus.

<img alt="" src=images/SheetMetal_Example.png  style="width:600px;"> 
*Le modèle en tôle est construit avec l'extension Sheet Metal (arrière plan); devant, le solide déplié; au premier plan, l'esquisse dépliée avec des lignes de pliage pour l'exportation au format DXF.*

Si l\'export au format DXF est utilisée pour contrôler des machines (Lasercut par exemple), vous devez modifier le DXF pour supprimer les lignes indiquant les plis, ces lignes risquant d\'être utilisées pour la découpe par la machine.

## Installation

Cet atelier peut être installé à partir du [Gestionnaire des extensions](Std_AddonMgr/fr.md). Pour une installation manuelle, voir [Installer des ateliers supplémentaires](Installing_more_workbenches/fr.md).



## Outils

Une description détaillée (en anglais) des outils peut être trouvée [sur le blogue de l\'auteur](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/). Elle est un peu dépassée maintenant, car de nouveaux outils ont été ajoutés.

-   <img alt="" src=images/SheetMetal_AddBase.svg  style="width:32px;"> [Tôle de base](SheetMetal_AddBase/fr.md): crée une tôle à partir d\'une esquisse, soit un profil, soit une plaque.

-   <img alt="" src=images/SheetMetal_AddWall.svg  style="width:32px;"> [Tôle pliée](SheetMetal_AddWall/fr.md): ajoute un rebord sur chaque bord sélectionné d\'une tôle. (Le rebord peut être transformé en ourlet en modifiant son angle).

-   <img alt="" src=images/SheetMetal_Extrude.svg  style="width:32px;"> [Prolonger une face](SheetMetal_Extrude/fr.md): prolonge une tôle au niveau d\'une arête sélectionnée d\'une face le long de sa normale. (En ajoutant une esquisse de contour, peut être utilisé pour créer une géométrie d\'emboîtement).

-   <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:32px;"> [Pli sur tôle](SheetMetal_AddFoldWall/fr.md): plie une face sur une ligne choisie avec un rayon de courbure spécifié.

-   <img alt="" src=images/SheetMetal_Unfold.svg  style="width:32px;"> [Déplier](SheetMetal_Unfold/fr.md): aplatit un objet en tôle pliée et génère un solide déplié et une esquisse de contour avec des lignes de pliage (fournit une boîte de dialogue pour définir les paramètres).

-   <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:32px;"> [Déplier sans assistance](SheetMetal_UnattendedUnfold/fr.md) : aplatit un objet en tôle pliée et génère un solide déplié et une esquisse avec des lignes de pliage (si les paramètres ont déjà été définis).

-   <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:32px;"> [Grugeage rond du coin](SheetMetal_AddCornerRelief/fr.md): ajoute un perçage pour gruger un coin.

-   <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:32px;"> [Grugeage carré](SheetMetal_AddRelief/fr.md): 1ère étape pour convertir un objet coque en objet tôle dépliable, ajoute un relief (découpe) à un coin.

-   <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:32px;"> [Découpe d\'angle](SheetMetal_AddJunction/fr.md): 2ème étape pour convertir un objet coque en objet tôle dépliable, crée une jonction ouverte sur le bord de deux parois.

-   <img alt="" src=images/SheetMetal_AddBend.svg  style="width:32px;"> [Transformation en pli](SheetMetal_AddBend/fr.md): 3ème étape pour convertir un objet coque en un objet tôle dépliable, remplace les arêtes vives par des pliures arrondies.

-   <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:32px;"> [Perçage de paroi](SheetMetal_SketchOnSheet/fr.md): découpe d\'un motif de trous basé sur une esquisse le long des parois pliées d\'un objet en tôle.

-   <img alt="" src=images/SheetMetal_Forming.svg  style="width:32px;"> [Outil d\'emboutissage](SheetMetal_Forming/fr.md): emboutit des formes avec ou sans trous dans une plaque de tôle.



## Description sommaire 

Cet atelier fournit des outils pour les deux tâches principales :

-   Créer des objets en tôle
-   Déplier des objets en tôle

Cette section est destinée à donner une idée générale de la façon d\'utiliser les outils fournis. Des informations plus détaillées peuvent être trouvées sur la page de chaque outil (voir ci-dessus) ou dans les tutoriels liés (voir ci-dessous).



### Créer un objet en tôle 



#### Débuter avec un profil 

1.  Créer une polyligne ouverte (de préférence avec le sketcher)
2.  Utilisez la commande <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Make Base Wall](SheetMetal_AddBase/fr.md) pour créer un profilé en tôle.



#### Débuter avec un panneau 

1.  Créer une polyligne fermée (de préférence avec le sketcher)
2.  Utilisez la commande <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Make Base Wall](SheetMetal_AddBase/fr.md) pour créer un panneau de tôle.



#### Débuter avec une PartDesign protrusion 

1.  Créez une polyligne fermée (de préférence avec le sketcher)
2.  Utilisez la commande <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Protrusion](PartDesign_Pad/fr.md) pour créer un corps prismatique.
3.  La commande <img alt="" src=images/PartDesign_Thickness.svg  style="width:16px;"> [PartDesign Épaisseur](PartDesign_Thickness/fr.md) en fera un objet d\'épaisseur constante.
4.  Pour le rendre dépliable, il a besoin de quelques espaces ou connexions entre les parois :
    1.  La commande <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> [Make Relief](SheetMetal_AddRelief/fr.md) coupera les coins sélectionnés.
    2.  La commande <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> [Make Junction](SheetMetal_AddJunction/fr.md) créera des jonctions avec des espaces entre des côtés adjacents qui doivent être disjoints.
    3.  La commande <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> [Make Bend](SheetMetal_AddBend/fr.md) créera des connexions cylindriques pour les côtés restants qui doivent rester joints.

Certains paramètres seront hérités du ou des objets parents, mais il est préférable de vérifier les paramètres pertinents à chaque étape.

Il faut maintenant vérifier si l\'objet en tôle résultant peut être déplié. (voir [Déplier un objet en tôle](#D.C3.A9plier_un_objet_en_t.C3.B4le.md) ci-dessous).



#### Ajout de fonctionnalités supplémentaires 

Les objets de base en tôle dépliables peuvent être étendus :

1.  Utilisez la commande <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> [Extend Face](SheetMetal_Extrude/fr.md) pour agrandir les côtés.
2.  La commande <img alt="" src=images/SheetMetal_AddWall.svg  style="width:16px;"> [Make Wall](SheetMetal_AddWall.md) ajoutera de nouveaux rebords ou de nouveaux bords à l\'objet existant.
3.  Utilisez la commande <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:16px;"> [Add Corner Relief](SheetMetal_AddCornerRelief/fr.md) pour ajouter ou remodeler des angles.
4.  La commande <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:16px;"> [Fold a Wall](SheetMetal_AddFoldWall/fr.md) permet de plier une paroi sur une ligne donnée, c\'est-à-dire qu\'elle coupe une paroi sur cette ligne, déplace le côté coupé et les réunit par un raccord cylindrique.
5.  Utilisez la commande <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> [Sketch on Sheet metal](SheetMetal_SketchOnSheet/fr.md) pour découper des trous dans l\'objet en commençant par une paroi choisie, puis en suivant les parois adjacentes et les connexions.
6.  La commande <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Make Forming in Wall](SheetMetal_Forming/fr.md) permet d\'estamper une forme à une plaque (paroi).

:   

    :   Après la création d\'un élément WallForming, l\'objet SheetMetal n\'est **plus dépliable**!

Plusieurs outils provenant d\'autres ateliers peuvent être utilisés pour ajouter des trous ou remodeler des bords.



### Déplier un objet en tôle 

Pour déplier un objet en tôle, activez l\'outil <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Unfold](SheetMetal_Unfold/fr.md) ou l\'outil <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:16px;"> [Unattended Unfold](SheetMetal_UnattendedUnfold/fr.md).

Le résultat sera un objet 3D avec une esquisse de contour en option comprenant des lignes de pliage.



### Exemples

En attendant que des pages de tutoriel soient disponibles sur ce wiki, il existe une page [Exemples](SheetMetal_Examples/fr.md).

<img alt="" src=images/SheetMetal_Example-01.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-02.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-03.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-04.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-05.png  style="width:100px;">

Il contient également quelques indications sur les [propriétés](SheetMetal_Examples/fr#Propri.C3.A9t.C3.A9s_de_SheetMetal.md).



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

#### 1ère operation 

-   Obtenez la base: utilisez soit les ateliers \"pièce\" ou \"brouillon\", faites 1 croquis qui contiendra tous les trous et toutes les coupes, extrudez cette base à l\'épaisseur de la feuille.
-   Gardez à l\'esprit que les bords seront toujours en plus des rayons de pliage.

![](images/sm2.png ) 

#### 2ème opération 

-   Ouvrez l\'atelier Sheet_metal.
-   Sélectionnez 1 épaisseur du bord (arête) de la plaque de base et cliquez sur l\'outil \"bend\" 90°/ L\'angle de courbure par défaut peut être modifié de 0 à 90°.
-   La hauteur des bords est de 10 mm par défaut, modifiable de 0,1 à xxxmm.
-   Le rayon de cintrage est par défaut égal à l\'épaisseur, modifiable de 0,1 à xxmm (ne jamais mettre 0).
-   Gap1, gap2 est le retrait du bord plié du coin de la base (0 accepté).
-   Inverser par défaut: false se replie en Z +, true en ZReliefd coupe le coin entre le pli et la base (inactif si gap = 0).
-   Reliefw ajoute 1 fente entre la base et le bord (inactive si reliefd = 0).

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

#### Dépliage

Choisissez 1 face de référence (ici la face orange) et cliquez sur le bouton dans la barre d\'outils.
Nous obtenons la partie bleue dont il suffit de modifier les valeurs X, Y ou Z pour le voir en totalité.
![](images/sm6.png ) 

#### Couper les retours à 45 ° 

Après avoir plié les retours sans avoir fait de retrait, la forme apparaît ainsi. ![](images/sm7a.png ) Pour ce faire, il doit se diviser à 45 ° (ou suivant les bissectrices pour les largeurs inégales).
\* Créer 1 nouveau sketch lié à la partie commune aux 2 volets.

-   Créer 1 arrêt lié en sélectionnant le bord extérieur de la \"charnière\".(important)

Dessinez 1 triangle dont le haut est contraint à la fin, orienté 1 côté à 45 °, donnez au petit côté 1 largeur minimum (0.1mm suffit), et faites 1 pocket.
Veillez à ne pas érafler la \"charnière\" où la nudité de lier la pointe du triangle au bord de la ligne de pliage. ![](images/sm8a.png ) Dépliage ![](images/sm9.png ) 

#### Perçage des bords et des rabats 

Faites ces trous et coupes après le pliage et avant le dépliage.
Veillez toujours à ne pas \"érafler\" ou couper les lignes de pliage.
![](images/sm10.png ) 

#### Faire des rabats tangents 

Faire 1 pli sur le bord du coté, à 45 ° de 0.1mm de long, puis 1 autre inverse à 45 ° de la longueur du rabat contigu, puis étendre le coté opposé, il passera et ils ne seront pas confondus.
![](images/sm11.png ) 

#### Cas particulier de ce même bord percé 

Dans ce cas particulier, le dépliage ne fonctionne qu\'en choisissant la face jaune comme référence.
![](images/sm12.png ) 

#### Cas spécial de trou enjambant les plis 

Auparavant, il est dit plusieurs fois qu\'il est interdit de couper les lignes de pliage.
Comment faire ?
![](images/sm13.png )

-   Faire la base avec son trou demi-rond et faire les 2 demi-faces et les 2 demi-plis séparément.
-   Faites ensuite 1 extension sur 1 des côtés de la largeur de l\'ouverture moins 0.1mm, les 2 bords restent ainsi séparés.
-   Puis sur cette extension (en vert) dessiner le contour de la coupe et faire 1 poche
-   Le résultat est le morceau rouge ci-dessus, et le dépliage fonctionne, reste la ligne qui séparait les 2 bords précédemment

![](images/sm14.png )


</div>


</div>



## Vidéos

-   [The Elegant Sheet Metal Workbench](https://www.youtube.com/watch?v=xidvQYkC4so) par Joko Engineering



## Liens

-   [Macro Sheet Metal Unfolder](Macro_Sheet_Metal_Unfolder/fr.md) macro originale sur laquelle l\'outil Unfold est basé.
-   [Un tutoriel en français et en anglais au format PDF](https://forum.freecadweb.org/viewtopic.php?f=3&t=25002) sur le forum FreeCAD
-   Signalement des bogues/demande de fonctionnalités: <https://github.com/shaise/FreeCAD_SheetMetal/issues>.



## Références

-   Auteur :
    -   Outils de pliage : copyright 2015-2018 par Shai Seger
    -   Outil de dépliage : copyright 2014 par Ulrich Brammer
-   Licence: [GPLv3](https://www.gnu.org/licenses/gpl-3.0.fr.html)
-   Code source sur github: <https://github.com/shaise/FreeCAD_SheetMetal>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Workbench/fr
