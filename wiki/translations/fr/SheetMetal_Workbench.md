


{{UnfinishedDocu

}} <img alt="Icône de l\'atelier externe Sheet Metal" src=images/Sheetmetal_workbench_icon.svg  style="width:128px;">

## Vue d\'ensemble 


{{TOCright}}

<img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:32px;"> **Sheet Metal** est un [atelier externe](external_workbenches/fr.md) servant à concevoir et déplier des pièces de métal en tôlerie. Par conséquent, il ne fait pas partie de l\'installation standard de FreeCAD.

<img alt="" src=images/SheetMetal_Example.png  style="width:600px;"> 
* Le modèle en tôle construit avec l'add-on Sheet Metal (arrière plan); devant, le solide déplié; au premier plan, l'esquisse déplier avec des lignes de pliage pour l'exportation au format DXF.*

Si l\'exportation au format DXF est utilisée pour contrôler des machines (Lasercut par exemple), vous devez modifier le DXF pour supprimer les lignes indiquant les plis, ces lignes pouvant être utilisées pour la découpe par la machine.

## Installation

Cet atelier peut être installé à partir du [Gestionnaire d\'Addon](Std_AddonMgr/fr.md). Pour une installation manuelle, voir [Installer des ateliers supplémentaires](Installing_more_workbenches/fr.md).

## Outils

Une description détaillée (en anglais) des outils peut être trouvée [sur le blogue de l\'auteur](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/).

-   <img alt="" src=images/SheetMetal_AddBase.svg  style="width:32px;"> [Tôle de base](SheetMetal_AddBase/fr.md): crée une paroi en tôle à partir d\'une esquisse ouverte.

-   <img alt="" src=images/SheetMetal_AddWall.svg  style="width:32px;"> [Tôle pliée](SheetMetal_AddWall/fr.md): génère une tôle à partir d\'une face latérale de la tôle.

-   <img alt="" src=images/SheetMetal_Extrude.svg  style="width:32px;"> [Prolonger une face](SheetMetal_Extrude/fr.md): prolonge une face le long de la normale.

-   <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:32px;"> [Pli sur tôle](SheetMetal_AddFoldWall/fr.md): plie une face sur la ligne choisie avec un rayon de courbure spécifié.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/SheetMetal_Unfold.svg  style="width:32px;"> [Déplier](SheetMetal_Unfold/fr.md): aplatit un objet en tôle pliée et génère un solide et une esquisse.


</div>

-   <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:32px;"> [Unattended Unfold](SheetMetal_UnattendedUnfold.md): Flattens folded sheet metal object and generates a solid and a sketch (if parameters have already been set).

-   <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:32px;"> [Grugeage rond du coin](SheetMetal_AddCornerRelief/fr.md): ajoute un perçage pour gruger un coin.

-   <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:32px;"> [Grugeage carré](SheetMetal_AddRelief/fr.md): ajoute une découpe carré à un coin.

-   <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:32px;"> [Découpe d\'angle](SheetMetal_AddJunction/fr.md): découpe un espace dans l\'angle de deux parois.

-   <img alt="" src=images/SheetMetal_AddBend.svg  style="width:32px;"> [Transformation en pli](SheetMetal_AddBend/fr.md): plie une face suivant une ligne choisie.

-   <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:32px;"> [Perçage de paroi](SheetMetal_SketchOnSheet/fr.md): découpe des trous dans la tôle à partir d\'un schéma.

-   <img alt="" src=images/SheetMetal_Forming.svg  style="width:32px;"> [Outil d\'emboutissage](SheetMetal_Forming/fr.md): crée un outil de formage.

## Deux outils complémentaires 

### Créer un profil de base 

Outil en forme d\'oméga : faites une pièce à partir d\'une simple multiligne créée dans Sketcher ou Draft, donnez-lui la hauteur et l\'épaisseur centrées, à gauche ou à droite de cette ligne, veillez à ne pas créer d\'auto-intersection dans les plis fermés d\'un espace moindre comme l\'épaisseur du matériau.

### Pliez le long d\'une ligne 

Pliez une plaque de base \"plate\" le long d\'une ligne (rectangle barré d\'une ligne) : sélectionnez la face, puis la ligne et l\'outil, choisissez l\'angle, le rayon, le côté, la position du pli par rapport à la ligne est pas très bien défini ; il semble que la ligne soit le bord d\'intersection à l\'extension des 2 faces.

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

#### 1ère opération 

-   Obtenez la base: utilisez soit les ateliers \"pièce\" ou \"brouillon\", faites 1 croquis qui contiendra tous les trous et toutes les coupes, extrudez cette base à l\'épaisseur de la feuille.
-   Gardez à l\'esprit que les bords seront toujours en plus des rayons de pliage.

![](images/sm2.png )

#### 2ème opération 

-   Ouvrez l\'atelier Sheet\_metal.
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


{{TOCright}}

## Liens

-   [Macro Sheet Metal Unfolder](Macro_Sheet_Metal_Unfolder/fr.md) macro originale sur laquelle l\'outil Unfold est basé.
-   Annonce du [Sheet Metal Workbench](http://forum.freecadweb.org/viewtopic.php?t=11303) (EN) sur le forum FreeCAD
-   [Un tutoriel en français et en anglais au format PDF](https://forum.freecadweb.org/viewtopic.php?f=3&t=25002) sur le forum FreeCAD
-   Fichiers:
-   Signalement des bogues/demande de fonctionnalités: <https://github.com/shaise/FreeCAD_SheetMetal/issues>

## Références

-   Auteur:
    -   Outils de pliage: Copyright 2015-2018 par Shai Seger
    -   Outil de dépliage: Copyright 2014 par Ulrich Brammer
-   Licence: [GPLv3](https://www.gnu.org/licenses/gpl-3.0.fr.html)
-   Blog officiel (EN): [Sheet metal Addon for FreeCAD](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/)
-   Code source sur github: <https://github.com/shaise/FreeCAD_SheetMetal>

## Ateliers externes 

Les ateliers FreeCAD sont faciles à programmer en [Python](Python/fr.md), de ce fait, beaucoup de personnes développent des ateliers supplémentaires en dehors des développeurs principaux de FreeCAD.

La page [ateliers externes](external_workbenches/fr.md) contient des informations et des tutoriels sur certains d'entre eux, et le projet [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) vise à les rassembler et à les rendre facilement installables depuis FreeCAD.

De nouveaux ateliers sont en développement, restez à l\'écoute !

[Category:SheetMetal{{\#translation:}}](Category:SheetMetal.md) [Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Command Reference{{\#translation:}}](Category:External_Command_Reference.md)
