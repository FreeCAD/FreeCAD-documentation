# Flamingo Workbench/fr
**L'atelier Flamingo (Python2/Qt4) a été remplacé par l'atelier Dodo (Python3/Qt5).
Cette page wiki mettra en évidence les différences entre ces deux ateliers.**

## Introduction

Il s\'agit d\'un ensemble de commandes et d\'objets FreeCAD personnalisés qui permettent principalement d\'accélérer le dessin des charpentes et des canalisations.

------------------------------------------------------------------------

:   L\'atelier \"*Flamingo*\" est dédié aux versions utilisant la syntaxe Python \>2.7 et la boîte à outils Qt4.





:   L\'atelier \"*Dodo*\" est pour Python \>3.6 et Qt5.

------------------------------------------------------------------------

Par commodité, les outils Flamingo/Dodo sont groupés dans trois barres d\'outils et menus + un ensemble utilitaire.

![](images/flamingoBlob.png )

![](images/dodoBlob.png )

:\* **Frame tools** : a pour but d\'organiser des poutres, des fermes et autres éléments similaires dans FreeCAD en utilisant les objets Structure du module Arch. \.../flamingo/tutorials/tutorialFrame.pdf

:\* **Pype tools** : la suite logique de l\'outil Frame puisqu\'il traite de la création de tuyauteries et de structures tubulaires. Il dispose également de ses propres classes Python pour créer les objets de tuyauterie, tels que des tubes, des coudes, des brides, etc. \.../flamingo/tutorials/tutorialPype2.pdf

:\* **Eagle tools** : il s\'agit essentiellement d\'un complément, et d\'un raccourci, de l\'atelier très professionnel [FreeCAD-PCB](https://github.com/marmni/FreeCAD-PCB) (également disponible dans le dépôt d\'extensions de FreeCAD) pour importer la position des objets d\'un fichier .brd Eagle sur un PCB dessiné dans FreeCAD avec l\'atelier a.m. en se basant uniquement sur leurs noms. C\'est aussi l\'origine, par extension, du nom de l\'ensemble du workbench. \.../flamingo/tutorials/tutorialEagle.pdf

:\* **Utils** fournit quelques fonctionnalités pour interroger les objets du modèle et leur distance, pour déplacer/pivoter le plan de travail et un petit hack de la boîte de dialogue de création de [Draft Polyligne](Draft_Wire/fr.md), qui permet de changer la position du plan de travail à la volée.

## Références

-   Auteur : oddtopus
-   Code source sur github :

<https://github.com/oddtopus/flamingo>

<https://github.com/oddtopus/dodo>

## Installation

Cet atelier peut être installé à partir du [Gestionnaire d\'Addon](Std_AddonMgr/fr.md). Pour une installation manuelle, voir [Installer des ateliers supplémentaires](Installing_more_workbenches/fr.md).

## Outils Frame 


<div class="center" style="width: auto; margin-left: auto; margin-right: auto;">

![](images/Flamingos_frame2.jpg )


</div>


:   1\) Placement d\'une poutre sur une arête (classe frameIt)

Avec un objet poutre et une arête dans le modèle, cet outil pose la poutre sur une arête en sélectionnant l\'une puis l\'autre jusqu\'à ce que vous appuyiez sur ESC.

:   2\) Remplissage du cadre (classe fillFrame)

Boîte de dialogue permettant de créer sur plusieurs arêtes sélectionnées dans la fenêtre les poutres du type de celles précédemment choisies parmi celles présentes dans le modèle.

Avec le bouton **Sélectionner**, il est possible de changer le type de poutre.


**Dodo : cette fonction a été remplacée dans la boîte de dialogue "Insert framebranch" par le bouton "Add single"**


:   3\) Insérer un chemin (classe insertPath)

Outil permettant de créer un fil DWire continu sur le chemin défini par les arêtes sélectionnées dans la fenêtre, même si celles-ci ne se touchent pas, se croisent au milieu ou appartiennent à des objets différents. La seule contrainte est qu\'il existe une intersection entre deux arêtes consécutives, dans l\'ordre dans lequel elles ont été sélectionnées. De plus, le DWire donne les propriétés d\'affichage d\'une ligne centrale, c\'est-à-dire orange et pointillé.

:   4\) Insérer des Sections Std. (classe insertSection)

Boîte de dialogue permettant de créer un ensemble de profils à utiliser dans le modèle pour l\'objet FrameLine.

-   Liste des **Sections** : comprend toutes les sections définies dans le fichier {{FileName|.csv}} correspondant au type de section sélectionné.
-   Liste des **types de section** : types de profils définis avec les fichiers {{FileName|.csv}} inclus dans le dossier {{FileName|/tables}}
-   Bouton **Insérer** : crée le groupe \"Profiles\_set\", s\'il n\'existe pas déjà, et y ajoute l\'objet du profil sélectionné.

D\'autres tables de profils peuvent être créées en ajoutant le fichier {{FileName|.csv}} approprié dans le dossier {{FileName|/tables}}. Les règles permettant de créer ou de personnaliser de tels tables sont similaires à celles relatives aux canalisations.

D\'autres profils peuvent être dessinés dans le modèle et glissés dans le groupe \"Profiles\_set\".

L\'orientation des fils DWires peut influer sur le rendu des poutres.


**Dodo: a changé la portée de cette fonction.
Dans dodo, cela ouvre une boîte de dialogue vous permettant de créer 10 formes pour une section de poutre avec des dimensions personnalisées :
* creux et carré plein
* creux et cercle complet
* T, I, C, L, Z
* omega
Il est également possible pour changer la position du centre ou d'éditer une section existante.**


:   5\) Gestionnaire FrameLine (classe FrameLineManager)

Comme pour les objets \"pype-line\", il s\'agit d\'une boîte de dialogue permettant de créer et de modifier les propriétés des objets \"frame-line\".

De même que ce qui a été vu ci-dessus, les FrameLine sont des objets qui collectent des propriétés communes à un ensemble de poutres (à savoir la section de la poutre), qui sont incluses dans un groupe commun de l\'arborescence du modèle. Elles ont également une propriété facultative \".Base\", définie par défaut sur Aucune, qui est la ligne médiane des poutres du cadre. Une fois qu\'un chemin, alias .Base, est défini (un DWire ou un Sketch), d\'autres poutres peuvent être ajoutées à la FrameLine, mais elles seront supprimés sur demande de **Redraw** (Redessiner). La boîte de dialogue offre les fonctionnalités suivantes :

-   une liste des profils de poutres précédemment inclus dans le modèle par la boîte de dialogue \"Insert Std. Sections\" (lire plus loin) ;
-   une liste déroulante pour sélectionner la FrameLine active parmi celles déjà créées ou  pour en créer une nouvelle ;
-   une zone de texte où écrire le nom de la FrameLine à créer ; si rien ou \"\", la FrameLine sera nommée par défaut \"Telaio00n\" ;
-   Bouton **Insert** : crée un nouvel objet FrameLine ou ajoute de nouveaux membres à celui sélectionné dans la liste déroulante si des arêtes sont sélectionnées dans la fenêtre active.
-   Bouton **Redraw** : crée de nouvelles poutres et les place sur le chemin sélectionné. Les nouvelles poutres seront collectés à l\'intérieur du groupe FrameLine. Ne crée pas et ne met pas à jour les poutres ajoutées à FrameLine en dehors de son chemin défini.
-   Bouton **Clear** : supprime toutes les poutres du groupe FrameLine. Cela s\'applique également aux poutres ajoutées à la FrameLine en dehors de son chemin défini.
-   Bouton **Get Path** : assigne le Dwire sélectionné à l\'attribut Path de l\'objet FrameLine.
-   Bouton **Get Profile** : modifie l\'attribut Profil de l\'objet FrameLine par celui de la poutre sélectionnée dans la fenêtre ou celle sélectionnée dans la liste.
-   Case à cocher **Copy profile** : si cette case est cochée, un nouvel objet profil est généré pour chaque poutre afin d'éviter les références multiples dans le modèle.
-   Case **Move to origin** : si cochée, déplace le centre de gravité du profil vers le système d\'origine des coordonnées : le centre de la poutre coïncide avec le centre de gravité du profil.

Si le nom d\'un objet FrameLine est modifié, le nom du groupe approprié changera automatiquement, mais pas l\'inverse.

:   6\) Gestionnaire FrameBranch

Semblable à la fonction analogue du menu Pype, il s'agit d'un conteneur pour les poutres structurées sur une .Base. La base peut être un DWire, une esquisse ou les bords d'une forme solide. Lorsque la base sous-jacente est modifiée, la position et la longueur des poutres sont également modifiées en conséquence. Il est possible de couper/étendre n\'importe quelle géométrie sur les poutres et de faire pivoter les sections le long de la ligne médiane à l\'aide des commandes fournies dans la boîte de dialogue : de cette manière la modification n\'est pas perdue lors du recalcul du document.

-   **OK** crée une branche sur la géométrie présélectionnée
-   **Cancel** ferme la boîte de dialogue
-   la zone de texte **** permet d\'insérer un nom personnalisé à la fonctionnalité
-   la **liste déroulante** permet de sélectionner le type de section à afficher dans la liste. (voir ../Mod/flamingo/shapes ou ../Mod/dodo/shapez pour personnaliser)
-   **AddBeams** ajoute un membre à un cadre sur l\'arête sélectionnée. L\'arête doit appartenir à une branche existante
-   **RemoveBeams** supprime la poutre sélectionnée de l\'arête correspondante
-   **ChangeProfile** change les profils de la framebranch. Pour sélectionner la branche, il suffit de sélectionner l\'un de ses membres dans la zone d\'affichage.
-   **Get targets** sélectionne la géométrie dans la zone de visualisation pour couper/étendre les poutres. Les cibles peuvent également n\'appartenir à aucune branche.
-   **Trim/Extend** change la longueur des objets sélectionnés en fonction des objectifs.
-   **Add single** crée une poutre de la **** (longueur) spécifiée, non liée à la base des arêtes ou des surfaces sélectionnées.
-   **Redraw** recrée le cadre, en supprimant tous les décalages et rotations

Lorsqu\'une poutre appartenant à une branche est sélectionnée dans la zone de visualisation, son EXTRÉMITÉ est mise en surbrillance. Cela permet de modifier manuellement les décalages de queue et de tête, à côté de la rotation de la section, en utilisant les commandes fournies dans la boîte de dialogue.

:   7\) Tourner poutres de 45 deg. (classe spinSect)

Outil pour faire tourner un objet de 45 degrés autour de l'axe \"Z\" de sa forme.

:   8\) Inverser l\'orientation (classe reverseBeam)

Outil permettant de faire pivoter un objet de 180 degrés autour de l'axe \"X\" de sa forme. Notes : si un bord de l\'objet est sélectionné, il est utilisé comme pivot de rotation.

:   9\) Déplacer la poutre (classe shiftBeam)

Boîte de dialogue pour déplacer et copier des objets.

Les zones de texte **X**, **Y** et **Z** permettent de saisir directement la valeur de déplacement dans chaque direction.

Zone de texte **Multiple** est le coefficient multiplicateur de la valeur du déplacement.

Le champ **Steps** est le diviseur de la valeur du déplacement. Il est utilisé lorsque la valeur du déplacement doit correspondre à un certain nombre d\'étapes.

Le bouton **Get displacement** prend la quantité et le sens du déplacement de la distance des entités sélectionnées (points, arêtes, faces) ou même d'une seule arête. Dans ce dernier cas, une flèche verte s\'affiche pour indiquer la direction.

**OK** pour effectuer l\'action et **Cancel** pour fermer la boîte de dialogue.

:   13\) Rotation + alignement des bords (classe rotJoin)

Outil pour déplacer et faire pivoter les poutres pour aligner deux bords. Comme ci-dessus mais cela rend également les bords colinéaires.

:   10\) Pivoter la poutre (classe pivotBeam)

Boîte de dialogue permettant de faire pivoter une poutre ou un autre objet sur l'un de ses bords.

Zone de texte **Angle** pour insérer l\'angle de rotation.

Bouton **Reverse** pour tourner dans le sens opposé, si nécessaire.

**OK** pour effectuer l\'action et sur **Cancel** pour fermer la boîte de dialogue.

:   11\) Affleurer les surfaces (class levelBeam)

Outil pour affleurer les faces parallèles de deux objets. Actuellement la commande prend ce qui est au même niveau, respecte la position et l\'orientation de la première face sélectionnée, le centre de gravité de toutes les faces sélectionnées. Ainsi, elle translate les objets même si les faces ne sont pas parallèles.

:   12\) Aligner les bords (class alignEdge)

Outil pour faire correspondre deux bords parallèles. En fait, la commande déplace les objets le long de la distance minimale de leur bord sélectionné par rapport au premier. Elle translate donc l\'objet même si les bords ne sont pas parallèles et c\'est un bon moyen de placer les objets dans la position souhaitée. Il est également possible de sélectionner deux bords d\'un même objet. Avec cette méthode, il est possible de déplacer rapidement un objet par étapes définies sur sa propre géométrie.

:   14\) Alignement des cotés (classe alignFlange)

Boîte de dialogue pour faire pivoter les poutres de sorte que leurs surfaces soient parallèles à un plan de référence.

Il est possible de présélectionner la face de référence avant d\'appeler la commande.

Les trois boutons **XY**, **XZ** et **YZ** permettent de choisir directement l'orientation des plans principaux comme référence.

Enfin, il est possible d\'entrer directement la nouvelle orientation des faces à l\'aide des trois coordonnées du repère cartésien et du bouton **Set normal**.

:   15\) Étirer une poutre (classe stretchBeam)

Boite de dialogue pour changer la longueur des poutres.

Dans la zone de texte, écrivez la nouvelle longueur qui sera appliquée aux poutres ou tuyaux sélectionnés. Sinon, le bouton **Get Length** prend la nouvelle longueur de la géométrie sélectionnée (soit la longueur de la poutre ou de l\'arête, soit la distance entre des entités géométriques).

Avec le curseur, il est possible de changer la longueur saisie dans la zone de texte de -100% à + 100%.

Les boutons radio **Head** et **Tail** permettent de choisir le côté de la poutre à modifier.

:   16\) Étendre la poutre (classe extend)

Boîte de dialogue pour étendre une poutre jusqu\'à une cible sélectionnée.

Si des entités sont présélectionnées avant d\'appeler cette commande, la première entité est automatiquement prise comme cible et l\'objet qui lui est associé est supprimé de la sélection. Dans tous les cas, il est possible de changer d\'objet cible avec le bouton-poussoir **Select**.

:   17\) Ajuster l\'angle de la poutre (classe adjustFrameAngle)

Outil pour ajuster les poutres aux angles droits des encadrements. Pour comprendre au mieux son fonctionnement, reportez-vous au tutoriel précédent.

## Outils Pype 


<div class="center" style="width: auto; margin-left: auto; margin-right: auto;">

![](images/Flamingos_pype2.jpg )


</div>


:   1\) Ajouter un tube

Ouvre une boîte de dialogue pour insérer des tubes.

La liste déroulante située en haut à droite est une fonctionnalité commune à toutes les boîtes de dialogue \"Insert \...\" : elle répertorie les objets canalisation définis dans le document actuel : cette option permet de sélectionner à quelle canalisation attribuer les tuyaux nouvellement créés. Vous pouvez également laisser  (aucun) pour que l\'objet soit créé sur la ligne principale du modèle de pièce. Dans le coin supérieur gauche est imprimée la classification de tuyauterie actuellement sélectionnée, extraite de la liste dans la colonne de droite. Les dimensions des tuyaux pour chaque classe de tuyau sont définies dans des fichiers .csv, qu\'il est possible d\'ajouter ou de modifier, avec quelques règles de nommage simples, en fonction des besoins. Les courbes, les réductions, etc. ont les mêmes règles pour la définition de leurs tableaux de dimensions : voir les fichiers dans ../Mod/flamingo/Tables. Lisez aussi \"tutorialPype.pdf\" pour savoir comment les personnaliser ou les créer.

Pour définir la position et l'orientation des tuyaux, les sélections suivantes sont possibles:

-   un ou plusieurs bords droits
-   un ou plusieurs bords courbes
-   un ou plusieurs sommets
-   rien; dans ce cas, le tube sera placé à l\'origine.

Si aucune longueur n\'est spécifiée, la valeur par défaut est 200 unités (longueur conventionnelle en mm).

Le bouton **Reverse** permet de faire pivoter de 180 ° le dernier tube créé ou ceux sélectionnés.

Le bouton **Apply** permet d\'appliquer une longueur différente ou un diamètre nominal différent aux tubes sélectionnés.


**Dodo : ajout d'un menu circulaire (raccourci clavier : "Z") pour créer des objets pype (tuyauterie) : ceci est destiné à insérer plus rapidement des améliorations dans le dessin.**


:   2\) Ajouter un coude

Ouvre une boîte de dialogue pour insérer un coude.

En plus des widgets communs avec les autres boîtes de dialogue \"Insert\...\", le bouton **Trim/Extend** (Couper/Etendre) permet d\'ajuster la longueur des tuyaux sélectionnés au bord sélectionné de la courbe. Pour définir la position et l\'orientation, les sélections suivantes sont possibles:

-   un sommet,
-   un bord circulaire,
-   un tuyau à l\'une de ses extrémités. Dans ce cas, le diamètre et l\'épaisseur de la courbe s\'ajusteront automatiquement à ceux du tuyau sélectionné.
-   une paire d\'arêtes, de tuyaux ou de poutres, également non jointifs mais se croisant. Dans ce cas, les propriétés de la courbe seront automatiquement ajustées pour connecter les deux objets sélectionnés. Les tuyaux également sélectionnés seront automatiquement ajustés ou étendus jusqu\'aux bords de la courbe.
-   rien. Dans ce cas, la courbe sera placée à l\'origine.

Si aucun angle n\'est spécifié, la valeur par défaut est 90 degrés.

:   3\) Ajouter une réduction

Ouvre une boîte de dialogue pour insérer des réductions concentriques.

Pour définir la position et l\'orientation, les sélections suivantes sont possibles: deux tuyaux parallèles (éventuellement colinéaires)

-   un tuyau à l\'une de ses extrémités
-   un tuyau
-   un bord circulaire
-   un bord droit
-   un sommet
-   rien (créé à l\'origine)

Si un tuyau est sélectionné, ses propriétés sont appliquées à la réduction.

Si deux tuyaux sont sélectionnés, l\'outil essaiera automatiquement de les connecter avec le diamètre majeur et mineur de droite.

:   4\) Insérer un bouchon

Ouvre la boîte de dialogue pour insérer des bouchons.

Pour définir la position et l\'orientation, les sélections suivantes sont possibles:

-   un ou plusieurs bords courbes (axe et origine au centre)
-   un ou plusieurs sommets
-   rien

Si un bord de tuyau est sélectionné, les propriétés des bouchons s'adapteront automatiquement à celles du tuyau.

:   5\) Ajouter une vanne

Créez un \"espace réservé\" d\'une vanne à partir d\'une table .csv comme ci-dessus. Outre la dimension de décalage, il est important car il définit également le coefficient Kv qui sera utilisé pour calculer les pertes de pression avec l\'outil correspondant dans le menu \"Utils\". Notez que le symbole de l\'espace réservé change en fonction du type de vanne, si son nom est identifié par un mot clé parmi \"boule\", \"papillon\" ou \"globe\".

:   6\) Ajouter une bride

Ouvre une boîte de dialogue pour insérer des brides. Pour définir la position et l\'orientation, les sélections suivantes sont possibles:

-   un ou plusieurs bords circulaires,
-   un ou plusieurs sommets,
-   rien.

Si un tuyau est sélectionné, ses propriétés sont appliquées à la bride.

:   7\) Ajouter un boulon en U

Ouvre la boîte de dialogue pour insérer des boulons en U.

Pour définir la position et l\'orientation, les sélections suivantes sont possibles:

-   un ou plusieurs bords circulaires
-   un ou plusieurs tuyaux
-   rien.

Si un tuyau est sélectionné, ses propriétés sont appliquées au boulon en U. De plus, il est possible de choisir de placer le boulon en U au niveau des extrémités **Head** ou **Tail** ou au milieu **Middle** des tuyaux en cochant la case correspondante.

Avec le bouton **Ref. face**, il est possible de sélectionner la face du support sur laquelle orienter l\'axe du boulon en U.

------------------------------------------------------------------------

*Seulement dans **dodo** : les composants de tuyauterie ci-dessus peuvent également être insérés à partir du menu à tarte dédié.*

------------------------------------------------------------------------

:   8\) Gestionnaire canalisations

Avant de parler du dialogue, rappelez-vous ce qu\'est un objet canalisation dans le contexte de l\'atelier Flamingo.

Cet objet représente une collection d\'objets \"PType\" qui sont mis à jour avec les méthodes définies dans la classe Python elle-même. À l\'heure actuelle, cela crée, avec la méthode \"obj.Proxy.update(obj,\[edges\])\", tuyaux et courbes à partir des arêtes données et les rassemble dans un groupe nommé d\'après l\'obj.Label des objets. Un rayon de courbure standard \"3D\" (càd 1,5xdiamètre extérieur) est appliqué aux courbes. Le rayon de courbure est une propriété commune d\'un objet canalisation, vous pouvez donc le modifier, puis le redessiner. Lorsque l\'étiquette d\'un objet canalisation est renommée, le nom de son groupe est modifié en conséquence.

La classe PypeLine2 possède également l\'attribut facultatif \".Base\" qui représente notamment le trait d\'axe de la tuyauterie :

-   Si Base est None, PypeLine2 se comporte comme un conteneur d\'objets nu avec la possibilité de les regrouper automatiquement, d\'attribuer une couleur et d\'extraire la liste de pièces.
-   .Base peut être un fil, une esquisse ou tout objet dont les bords ont une forme.
-   En exécutant \"obj.Proxy.update (obj)\", sans \[edges\] (bords), la classe tente de restituer la canalisation (objets Pipe et Elbow) sur les bords \"obj.Base\" : pour les géométries bien définies, cela conduit généralement au résultat désiré. Si les \[edges\] sont donnés, des tuyaux et des courbes seront dessinés le long de ceux-ci.
-   L\'exécution de \"obj.Proxy.purge(obj)\" supprime du modèle tous les tuyaux et coudes appartenant à la canalisation.
-   N\'oubliez pas que l\'objet créé en dehors de la base .Base ne sera pas mis à jour lorsque la base .Base sera modifiée et que la canalisation sera redessiné et ne sera pas supprimé si canalisation est purgée (sauf les tuyaux et les courbes).

Ceci compris, la commande ouvre la boîte de dialogue permettant de créer ou de modifier une canalisation.

Le dialogue est très similaire à ceux pour insérer d\'autres objets vus auparavant.

Les tableaux de cotes de tuyauterie, où l'O.D. et l\'épaisseur sont définis, sont les mêmes de ceux pour les tubes (ex. Pipe\_SCH-STD.csv).

Lorsque  est dans la liste déroulante et que vous appuyez sur la touche **Insert**, un nouvel objet canalisation est créé dans le document avec le groupe approprié.

Il est possible de créer une canalisation de trois manières, en fonction des objets sélectionnés dans la fenêtre lorsque vous pressez Insérer :

-   rien n\'est sélectionné. Une canalisation est créée avec la propriété .Base = None et incluse dans son groupe avec le nom et la couleur spécifiés (ou les valeurs par défaut). Les objets tuyauterie à ajouter peuvent être créés un à un avec les commandes ci-dessus ou une ligne médiane peut être sélectionnée par la suite à l'aide des boutons **Get Profile** et **Redraw**.
-   un objet DWire est sélectionné. Il est automatiquement pris comme base et converti en chemin (orange, pointillé) avec des tuyaux et des courbes le long de celui-ci.
-   un ensemble d\'arêtes est sélectionné (même non contigu mais ayant des intersections prolongeant leurs extrémités). Un chemin est créé en connectant toutes les arêtes (voir l'outil Chemin dans la barre d'outils Frame) et attribué en tant que .Base à la nouvelle canalisation créée. Ensuite, les tuyaux et les courbes sont dessinés comme ci-dessus.

Après cela, il est toujours possible d\'ajouter d\'autres objets (tels que Flange, Reduct \...) à l\'aide des commandes d\'insertion appropriées décrites ci-dessus. Lorsque des objets sont créés dans une canalisation, ils sont automatiquement inclus dans le groupe pertinent du modèle et les propriétés communes (c\'est-à-dire le diamètre optique, l\'épaisseur, la couleur, le rayon de courbure, etc.) sont appliquées.

Si au moins une canalisation est déjà présente dans le modèle, vous pouvez la sélectionner dans la liste déroulante : dans ce cas, appuyer sur Insert crée les tuyaux et les courbes comme décrit ci-dessus, mais au lieu de créer un nouvel objet canalisation, cela les ajoute à la canalisation existante sélectionnée. Attention, la tuyauterie ainsi créée sera supprimée lors du prochain **Redraw**.

**Get Path**, Get Profile et Color permettent de modifier la propriété .Base, la taille nominale et la couleur de l\'objet, respectivement.

**Redraw** recrée les tubes et les courbes le long de la .Base (Si défini) après toute modification du chemin ou des propriétés de la canalisation.

**Part list** génère un fichier .csv avec la nomenclature des objets de tuyauterie inclus dans la canalisation sélectionnée dans la liste déroulante.

:   9\) Insérer une branche de tuyauterie

Cet objet tuyau se comporte comme une canalisation, sauf qu\'il se met automatiquement à jour chaque fois que la Base (un DWire ou un SketchObject) est modifiée : cela inclut la modification de l\'emplacement, l\'étirement, le déplacement, l\'ajout ou la suppression d\'arêtes. Il est principalement destiné à représenter les branches secondaires de la canalisation (voir le didacticiel dédié), mais il peut également agir en tant qu\'objet indépendant. C'est une commande importante qui permet de changer rapidement la disposition des tuyaux, mais qui présente un inconvénient, sa géométrie est définie de manière plus rigide. En d\'autres termes, les tuyaux ne peuvent pas être divisés ou redimensionnés indépendamment, car ils seront éventuellement redessinés sur la base. En revanche, modifier l\'OD, le thk ou le rayon de courbure de la branche de tuyauterie s'appliquera à tous les tubes et à toutes ses courbes.

:   10\) Insérer un réservoir

[Voir tutoriel Part 4 (1/2)](#Liens.md)

:   11\) Insérer une conduite

[Voir tutoriel Part 4 (2/2)](#Liens.md)

:   12\) Couper la tuyauterie

Ouvre une boîte de dialogue pour couper un tuyau en un point défini, en créant éventuellement un espace entre les extrémités des deux pièces. La sélection multiple est possible.

Indiquez dans la zone de texte **Point** la longueur à laquelle le ou les tuyaux seront coupés : il peut s\'agir d\'une valeur absolue ou simplement d\'un pourcentage de la longueur (un chiffre suivi de %). Dans certains cas, il est plus rapide d'utiliser la barre coulissante en bas pour modifier cette valeur.

Le bouton **Length** permet de mesurer la longueur du tuyau sélectionné et de l'utiliser comme référence de l'échelle à barres coulissantes.

Si vous avez juste besoin de couper des tuyaux en deux, laissez la zone de texte **Gap** à 0 ; sinon, définissez la longueur de l\'espace. Si une longueur de référence est choisie, l'espace peut également être défini en pourcentage. Comme le montre le [tutorial](https://github.com/oddtopus/flamingo/blob/master/tutorials), il est possible de mesurer l\'écart entre les géométries du modèle à l\'aide du bouton **Get gap** : c\'est la distance entre toute entité géométrique ou même la longueur d\'un seul bord.

Appuyer sur **Break** exécute l\'action.

La liste déroulante canalisation, comme d'habitude, permet de choisir le groupe auquel attribuer les nouveaux objets créés.

:   13\) Joindre les extrémités de tuyaux.

Lorsque deux bords circulaires appartenant à des objets différents sont sélectionnés, une pression sur ce bouton déplacera le deuxième objet pour rendre les bords concentriques et coplanaires.

Cela fonctionne non seulement avec des tuyaux.

:   14\) Joindre les tuyauteries

Joint les connecteurs de différents objets de manière graphique. Cela ne fonctionne qu\'entre objets tuyauterie, de même que dans différents ateliers, où la propriété Ports\[\] est définie de manière congruente.

:   15\) Assemble un coude

Sélectionner 2 tuyaux en intersection + 1 coude : en exécutant cette commande, ils seront joints. Cela ne fonctionne que parmi les objets tuyaux, ainsi que dans différents ateliers.

:   16\) Étendre les tuyaux depuis l\'intersection

En sélectionnant deux tuyaux, cette commande les étend tous les deux depuis leur point d\'intersection, s\'il existe.

:   17\) Étendre le tuyau depuis l\'intersection

En sélectionnant deux tuyaux, cette commande étend le premier depuis l\'intersection avec l\'autre, s\'il existe.

:   18\) Poser les tuyaux

En sélectionnant une face et plusieurs tuyaux, cette commande convertit le tuyau le long de la normale de la face afin de les faire reposer sur son plan.

:   19\) Redimensionner le support

Semblable à l\'outil ci-dessus, mais dans ce cas, le support est élevé ou abaissé, de sorte que la face soit tangente au tuyau.

:   20\) Attacher au tube

Attache un objet tuyau (2, 3, 4, 5 ou 6) de façon rigide à l\'extrémité la plus proche d\'un tuyau (1). Pour se détacher, cliquer sur le bouton lorsque l\'objet attaché est sélectionné seul.

:   21\) Créer des tuyaux point à point

Ouvre une boîte de dialogue similaire à \"Dessiner un DWire\" avec la boîte de dialogue \"Insérer un tuyau\" : cela permet de dessiner une séquence de tuyaux, reliés par des coudes, en sélectionnant simplement un point après l\'autre. Il est également permis de modifier les propriétés du tuyau et/ou de la canalisation à la volée.

:   22\) Insérer n\'importe quelle forme

C\'est un outil pour créer un objet \"tuyau\" à partir d\'un fichier .STEP ou .IGES ou .BREP. Il charge le fichier importé dans la propriété Shape d\'un FeaturePython.

## Utilitaires


<div class="center" style="width: auto; margin-left: auto; margin-right: auto;">

![](images/Flamingos_utils.jpg )


</div>


:   1\) Faire un polygone

Les deux premiers outils d'utilitaires font partie d'un projet distinct visant à créer un scanner automatique de pièces avec moteur pas à pas et télémètre ultrasonore. Cet outil crée un polygone régulier dans une esquisse.

:   2\) Polygone depuis un fichier

Outil pour créer n\'importe quel polygone dans une esquisse prenant ses sommets dans un fichier .csv, où ils sont stockés en coordonnées polaires.

:   3\) Interroger le modèle

Outil permettant d\'obtenir diverses informations en fonction de l\'objet ou des objets sélectionnés. En plus de la longueur ou des distances, il est spécialement adapté pour donner des informations relatives aux poutres et aux tuyaux (longueur, section, angle).

:   4\) Aligner le plan de travail

Outil permettant de définir la position et la rotation du plan de travail en fonction de la géométrie existante sélectionnée.

La normale du plan de travail est définie en analysant les éléments dans l\'ordre suivant :

1.  la normale de la face
2.  la normale du plan d\'une courbe
3.  la normale du plan contenant deux segments

L\'origine du plan de travail est définie (dans l\'ordre) par

1.  un sommet
2.  le centre de courbure d\'une ligne
3.  l\'intersection de deux lignes
4.  le centre d\'un bord

5\) Décalage plan de travail

Déplace le plan de travail le long de son vecteur normal. Pour indiquer la direction du décalage, une flèche verte temporaire s\'affiche à l\'écran. Clairement, des valeurs négatives sont également autorisées.

:   6\) Faire pivoter le plan de travail

Fait pivoter le plan de travail autour d\'un de ses axes. Dans ce cas également, une flèche verte est affichée dans la fenêtre pour identifier l'orientation actuelle du plan de travail : la flèche est pointée dans la direction Z et la base longue de la flèche est posée dans la direction X.

:   7\) Dessiner un DWire

Cet outil fonctionne exactement comme l\'outil correspondant de l\'atelier Draft, mais avec quelques options supplémentaires à la fin de la boîte de dialogue. Par défaut, l\'origine du plan de travail est redéfinie à chaque point ajouté, car cela simplifie le tracé de segments de longueur et d\'orientation connues à l\'aide de l\'option d\'accrochage à la grille. Ensuite, deux boutons-poussoirs, également appelés avec la touche de raccourci Ctrl+Maj+(), permettent de faire pivoter et de décaler le plan de travail comme indiqué ci-dessus sans casser l\'objet DWire. Les trois derniers boutons permettent de changer rapidement la rotation du plan de travail pour être parallèle aux plans principaux.

:   8\) Déplacement rapide d\'objets

Pour déplacer rapidement une pièce, par exemple pour accéder aux objets sous-jacents, cet outil fournit une poignée graphique (flèche verte) cliquable, avec laquelle il est possible de déplacer et de faire pivoter les objets sélectionnés.

:   9\) Calculateur de perte de pression

Ouvre une boîte de dialogue pour calculer les pertes de pression sur les pièces tuyauterie sélectionnées dans la fenêtre ou sur un embranchement. Le coefficient de frottement est calculé pour chaque tube droit et chaque coude. Pour les autres objets, la perte de charge concentrée est calculée à l\'aide du facteur de débit, à condition que l\'attribut Kv soit disponible et défini sur une valeur positive.

## Liens

-   Forum : [Nouvel atelier pour structure métallique](http://forum.freecadweb.org/viewtopic.php?f=8&t=17035) (annonce)
-   Forum: [Fil de discussion ateliers Flamingo & Dodo](https://forum.freecadweb.org/viewtopic.php?t=22711)
-   Tutoriels : [flamingo/tutoriels](https://github.com/oddtopus/flamingo/tree/master/tutorials)

-   Tutoriels vidéo :
    -   [Simple tutoriel video pour créer des structures tubulaires](https://www.youtube.com/watch?v=_Or91gdBLMU)
    -   [Part 1 : Comment créer des lignes de tuyauterie](https://www.youtube.com/watch?v=cBj0umlvzAk)
    -   [Part 2 : cadres, supports, brides et composants importés](https://www.youtube.com/watch?v=e81PpWY5L00)
    -   [Part 3 : dessiner un bâtiment avec quatre croquis (et plusieurs autres caractéristiques)](https://www.youtube.com/watch?v=IqEccmsg5dU)
    -   [Part 4 (1/2) : Disposition de la salle des pompes et plan de la tuyauterie](https://www.youtube.com/watch?v=aPF8SS_1Aqo)
    -   [Part 4 (2/2) : Importation de la salle des pompes dans les bâtiments et les conduites](https://www.youtube.com/watch?v=iGnW88x9bKQ)
-   Rapports de bugs :
    -   [File d\'attente de Flamingo GitHub](https://github.com/oddtopus/flamingo/issues)
    -   [File d\'attente de Dodo GitHub](https://github.com/oddtopus/dodo/issues)

## Autres liens intéressants 

-   [Ateliers externes](External_workbenches/fr.md)
-   [Macros](Macros_recipes/fr.md)
-   [OSE-Piping-Workbench : pour créer des raccords de tuyauterie supplémentaires](https://wiki.opensourceecology.org/wiki/OSE_Piping_Workbench)

## Ateliers externes 

Les ateliers FreeCAD sont faciles à programmer en [Python](Python/fr.md), de ce fait de nombreuses personnes développent des ateliers supplémentaires en dehors des développeurs principaux de FreeCAD.

La page [ateliers externes](external_workbenches/fr.md) contient des informations et des tutoriels sur certains d'entre eux, et le projet [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) vise à les rassembler et à les rendre facilement installables depuis FreeCAD.

De nouveaux ateliers sont en développement, tenez vous au courant!




[Category:Addons](Category:Addons.md) [Category:External Workbenches](Category:External_Workbenches.md)

---
[documentation index](../README.md) > Flamingo Workbench/fr
