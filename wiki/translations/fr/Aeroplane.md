---
- TutorialInfo:/fr
   Topic:Atelier Part
   Level:Débutant
   Time:10 minutes
   Author:Hughthecat
   FCVersion:
   Files:
---

# Aeroplane/fr







## Premiers pas 

Nous travaillerons dans l\'<img alt="" src=images/_Workbench_Part.svg  style="width:24px;"> [Atelier Part](Part_Workbench/fr.md) - sélectionnez-le dans les menus via **Affichage → Atelier → Part** ou depuis le [sélecteur d\'ateliers](Std_Workbench/fr.md).

-   Créez un nouveau document vide.
-   Basculez vers la <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> [Vue isométrique](Std_ViewIsometric.md).
-   Basculez l\'axe croisé **ON** (via le menu Affichage).
-   Assurez-vous que la [Vue combinée](Combo_view/fr.md) s\'affiche (via **Affichage → Panneaux → Vue combinée**).

-   Créer un cylindre, en cliquant sur le <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [Bouton de cylindre](Part_Cylinder/fr.md).
-   Sélectionnez le cylindre en cliquant dessus, dans la Vue combinée.
-   Cliquez sur l\'onglet Données au bas de la Vue combinée.

Changez la hauteur à 20 mm. Laissez le rayon à 2 mm.

Cliquez sur [Placement](Placement/fr.md) (notez le petit **[+]**) et un bouton avec trois points va apparaître **...**. Cliquez dessus. (Vous pouvez aussi sélectionner : **Menu → Edition → Positionnement**). Le visualiseur de tâches apparaît.

<img alt="" src=images/HTCaeroplane01.png  style="width:300px;">

Si vous n\'êtes pas familiarisé avec les axes X Y Z, alors faites des essais avec les nombres dans le tableau de Translation. Lorsque vous avez terminé de faire vos tests, cliquez sur le bouton **Reset** (réinitialisation).



## Seconde étape 

<img alt="" src=images/HTCaeroplane02.png  style="width:400px;">

Nous allons maintenant tourner le cylindre pour qu\'il se situe le long de l\'axe des X. Pour ce faire, il faut le faire pivoter autour de l\'axe Y. Dans la section Rotation → Axe de Rotation et angle, réglez l\'axe sur Y, et, incrémentez l\'Angle jusqu\'à ce qu\'il atteigne **90°**. Cliquez sur **OK**.

J\'aime jouer avec la rotation de la vue, souvent et, avec tous les moyens pour le faire. Vous devriez trouver la couture du cylindre sur le dessous.

<img alt="" src=images/HTCaeroplane03.png  style="width:400px;">

Nous allons maintenant ajouter et modifier une zone alors, cliquez sur le <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Cube](Part_Box/fr.md). Sélectionnez-le en cliquant sur la case dans la Vue combinée. Modifier la hauteur à 1 mm, la longueur à 5 mm et la largeur à 20 mm.

Cliquez sur [Placement→ **...**](Placement/fr.md) puis sur les trois points pour obtenir le visualiseur de tâches. Dans cette boîte de dialogue, entrez Y: -10 et Z: -1. Cliquez sur **OK**.

Nous allons maintenant fusionner ces deux formes, avec une opération booléenne. Cliquez sur le bouton <img alt="" src=images/Part_Boolean.svg  style="width:32px;"> [Exécuter une opération booléenne\...](Part_Boolean/fr.md) et la fenêtre des tâches affichera le sélecteur d\'opération booléenne.

Assurez-vous que Union soit sélectionné et que Cylinder et Box soient cochés une fois dans les deux listes de formes. Cliquez sur **Appliquer**. Cliquez sur **Fermer**. Vous avez maintenant un seul objet appelé **Fusion**.




Nous allons ajouter un <img alt="" src=images/Part_Box.png  style="width:32px;"> [Cube](Part_Box/fr.md) de plus, pour en finir avec notre modèle. Cliquez sur le <img alt="" src=images/Part_Box.png  style="width:32px;"> [bouton Cube](Part_Box/fr.md), puis sélectionnez, et, modifiez la hauteur à 5 mm, la longueur à 3 mm et la largeur à 1 mm. Modifier sa position par Y: -0,5.

Il nous faut maintenant joindre notre Fusion au Box001, donc nous allons le faire rapidement. Cliquez sur Fusion dans la Vue combinée et **Ctrl** + cliquez sur Box001. Cette commande sélectionne les deux pièces ensembles. Maintenant, cliquez sur le bouton <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Union](Part_Fuse/fr.md) pour obtenir **Fusion001**.

Vous devriez maintenant avoir le modèle d\'un avion tout simple. Faites un clic droit sur **Fusion001** et renommez-le en **Aeroplane**.

<img alt="" src=images/HTCaeroplane04.png  style="width:500px;">

Mais, je pense que les ailes doivent être déplacées un peu vers l\'avant, mais si nous sélectionnons Aeroplane, et, essayons de changer son Placement dans la direction X, tout bouge ! Mais nous voulons seulement déplacer les ailes, alors annulons le Placement.

Développez l\'avion (cliquez sur la petite flèche ou le **[+]** à côté), et développez Fusion.

Cliquez sur le <img alt="" src=images/Part_Box.png  style="width:32px;"> [Cube](Part_Box/fr.md) puis cliquez sur [Placement](Placement/fr.md). Remarquez qu\'il possède déjà Y: -10 et Z: -1 dans la fenêtre Translation. Remplacez la Translation X à 3 et cliquez sur **Appliquer**. C\'est mieux ainsi. Cliquez sur **OK**.




## Rotations

Cliquez sur Aeroplane pour obtenir son [Placement dans Taĉhes](Placement/fr.md) (Autres explications sur [Placement](Placement/fr.md)). Dans la section Rotation, changez la mention \'Axe de rotation avec angle\' en \'Angles d\'Euler\' car il est beaucoup plus facile de travailler avec eux.

![](images/Tache_Placement_Lacet_fr_Mini.gif ) **Lacet** est la rotation autour de l**\'axe Z** c\'est-à-dire une rotation de gauche à droite. (L\'angle de lacet est l\'angle **Psi ψ**)  ![](images/Tache_Placement_Tangage_fr_Mini.gif ) **Tangage** est la rotation autour de l**\'axe Y** c\'est-à-dire le piqué vers le bas et le piqué vers le haut. (L\'angle de tangage est l\'angle **Phi φ**).  ![](images/Tache_Placement_Roulis_fr_Mini.gif ) **Roulis** est la rotation autour de l**\'axe X**, c\'est-à-dire l\'aile de haut en bas. (L\'angle de roulis est l\'angle **Thêta θ**). 

Toutefois, même dans ce mode, il y a des choses importantes à retenir :

-   Les rotations positives sont dans le sens horaire vu du point d\'origine vers l\'extérieur le long d\'un axe positif ou pour le dire autrement: les rotations positives sont dans le sens anti-horaire vu depuis un axe positif dirigé vers le point d\'origine.

-   Bien, que les trois étiquettes qui sont Axe de lacet, Axe de tangage et Axe de roulis, ne sont pas vraiment ce qu\'ils sont. Ce sont des références aux coordonnées du corps d\'un objet dans l\'espace 3D. Les étiquettes devraient être Position, Altitude et Élévation ou même Azimut, Inclinaison et Élévation parce qu\'ils font référence aux coordonnées de l\'espace du système 3D. Ce sont les **Tait-Bryan angles**. Si vous souhaitez plus d\'informations, allez voir [Angles d\'Euler](http://fr.wikipedia.org/wiki/Angles_d'Euler).

-   Avec l\'avion dans sa position actuelle, des règles simples s\'appliquent. Le lacet est une rotation autour de l\'axe Z, c\'est-à-dire gauche et droite. Le pitch est une rotation autour de l'axe Y, c'est-à-dire le nez haut et bas. Rouler est une rotation autour de l\'axe X, c\'est-à-dire des ailes en haut et en bas. C\'est bien pour commencer mais ça ne sera plus vrai plus tard!

Jouez avec les trois paramètres Lacet, Tangage, Roulis (Yaw-Pitch-Roll). Vous devez seulement changer les paramètres de quelques degrés pour avoir une idée des mouvements. Réinitialisez lorsque vous avez terminé.

Maintenant nous allons voir pourquoi les étiquettes de Lacet, Tangage, et Roulis (Yaw-Pitch-Roll) ne sont pas vraiment adaptés. Modifiez le nombre de Lacet à 90 °, le nez de l\'avion doit bouger de haut en bas, et, le Tangage devrait le déplacer latéralement tel que vu de l\'extérieur de l\'avion, de là où nous sommes. Il le fait ? Non ce n\'est pas le cas ! Le tangage change le lacet, et, le lacet modifie le tangage. OK, cliquez sur **Reset **.

-   Ainsi, une meilleure façon de penser sur les rotations, est que les changements de lacet changent votre Longitude, les changements de tangage changent votre Latitude et que les changements de roulis changent la Direction (NSEW) auquel vous êtes confronté. Une adresse, ou vous pourrez en apprendre plus sur les [conventions sur les Axes](http://en.wikipedia.org/wiki/Axes_conventions).

Bon, retournons au travail. Changez le lacet à 45°, et, le tangage à-30°. Cliquez sur **OK** pour indiquer que l\'opération a été effectuée. Maintenant revenez dans [Tâche Placement](Placement/fr.md), et, examinez la zone Rotation. Il a été rétabli sur Axe de Rotation et angle, et, certaines boîtes d\'axes ont des valeurs d\'angles bizarres, Axe : (0.219493,-0.529904,0.819161), et, Angle : 53.65°. Les trois chiffres entre parenthèses sont les composants X Y Z, d\'un vecteur d\'unité dans l\'espace 3D. C\'est l\'Axe autour duquel notre avion original a été tourné, pour obtenir la position finale notre avion. Il donne la valeur de sa rotation. Intelligent, n\'est ce pas, mais pas très convivial! C\'est [Euler](http://fr.wikipedia.org/wiki/Euler) qui montre que vous pouvez combiner une série de rotations X Y Z, dans une rotation autour d\'un axe.

Voici quelques autres suggestions pour jouer avec l\'avion :

-   Modifier l\'emplacement de Z (et appliquez), puis modifier les valeurs de Lacet, Tangage, Roulis, et, regardez les effets. Puis essayez de changer l\'emplacement, et, la rotation de X et Y.
-   Changez le centre de X (et, appliquez), puis modifier les valeurs de, Lacet, Tangage, Roulis, et, regardez les effets. Alors essayez de changer les centres, et, rotations, Y et Z.

J\'espère, que ce petit tutoriel vous a aidé, à comprendre les rotations.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Category_Part.md) > Aeroplane/fr
