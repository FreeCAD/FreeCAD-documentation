# <img alt="" src=images/BIM_tutorial_screenshot.png  style="width:1024px;"> BIM ingame tutorial/fr


{{BIMTutorialAction|descr=Il s'agit du tutoriel de l'[atelier BIM](BIM_Workbench/fr.md). Il n'est pas destiné à être lu ici sur le wiki, mais plutôt à être démarré depuis FreeCAD, dans l'atelier BIM, sous le menu '''Aide -> Tutoriel BIM'''. Il comprend une série d'étapes à effectuer par l'utilisateur. Chaque étape se termine par une instance du modèle [<nowiki>{{BIMTutorialAction|descr|goal1|test1|goal2|test2}}</nowiki>](Template_BIMTutorialAction.md) qui informe de la condition qui doit être remplie. Les images doivent avoir une largeur de 300 pixels. Aucune image SVG ne doit être utilisée sur cette page car elles ne sont pas prises en charge par le widget QTextBrowser}}



### Bienvenue dans l\'atelier BIM ! 

<img alt="" src=images/BIM_Tutorial_title.jpg  style="width:300px;">

Ce tutoriel vous guidera à travers les différentes fonctionnalités de l\'[atelier BIM](BIM_Workbench.md) et vous aidera à vous mettre en piste en modélisant un bâtiment de pavillon très simple. Cela devrait prendre entre une et deux heures pour le terminer entièrement, selon votre expérience antérieure avec les applications 3D.

Vous pouvez l\'interrompre à tout moment et le reprendre plus tard, en sélectionnant le menu **Aide -\> Écran de bienvenue** puis en cliquant à nouveau sur l\'élément **Tutoriel BIM**.

Certaines étapes de ce didacticiel nécessitent que vous preniez des mesures. Celles-ci seront indiqués sous cette zone de texte, avec une icône indiquant si la tâche est terminée ou non. Mais comme nous sommes de personnes sympathiques ici à FreeCAD, il n\'est pas obligatoire de terminer les actions pour avancer dans ces pages. Vous pouvez simplement parcourir le didacticiel et ignorer les actions à votre convenance.



#### À propos des versions de FreeCAD 

Ce tutoriel est écrit pour la [la version de développement la plus récente de FreeCAD disponible](Download/fr.md) (actuellement la version 0.19). L\'atelier BIM, cependant, est conçu pour être compatible avec n\'importe quelle version de FreeCAD. Si vous utilisez une version de FreeCAD antérieure à celle indiquée ici, certains outils BIM peuvent avoir un aspect différent, fonctionner différemment ou même ne pas être disponibles. Reportez-vous à la [documentation](BIM_Workbench/fr.md) pour en savoir plus en cas de doute.



#### Remarque

Ce tutoriel est toujours en cours d\'écriture et est donc **incomplet** ! Si vous avez des suggestions ou des choses que vous trouvez floues, pourquoi ne pas nous aider à l\'améliorer sur le [forum FreeCAD](https://forum.freecadweb.org/viewforum.php?f=23) !


{{BIMTutorialAction|descr=Aucune action à effectuer pour cette étape}}



### Configurez FreeCAD 

FreeCAD a un système de préférences conséquent avec de nombreuses options à définir, situé dans le menu **Édition-\> Préférences** . Chaque atelier supplémentaire peut ajouter d\'autres pages de préférences, ce qui le rend très complexe.

L\'atelier BIM fournit un [écran de configuration simplifié](BIM_Setup/fr.md), qui permet de définir rapidement certaines des préférences les plus utiles pour le travail avec BIM. L\'écran des préférences BIM se trouve sous le menu **Préférences -\> Configuration BIM** (vous pouvez également cliquer sur le bouton correspondant dans la barre d\'outils Gérer) :

<img alt="" src=images/BIM_Tutorial_01.jpg  style="width:300px;">

Ouvrez maintenant l\'écran simplifié des préférences BIM et définissez les différentes options à votre guise.

En cas de besoin, passez la souris sur une option ou un paramètre pour voir une description de son utilisation :

<img alt="" src=images/BIM_Tutorial_02.jpg  style="width:300px;">

Dans ce tutoriel, nous travaillerons en centimètres. Nous vous suggérons donc de définir les unités préférées sur **centimètres** et la taille par défaut du carré de la grille sur **10 cm**. Ces paramètres peuvent être modifiés à tout moment à partir du bouton du plan de travail situé sur la barres d\'outils principale et de l\'indicateur d\'unités situé sur la barre d\'état (en bas à droite):

<img alt="" src=images/BIM_tutorial_14.jpg  style="width:300px;">


{{BIMTutorialAction|goal1=Ouvrez l'écran de configuration de BIM|test1=True if hasattr(FreeCADGui,"BIMSetupDialog") else False|goal2=Réglez les unités en centimètres et la taille de la grille sur 10 cm|test2=True if ((FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema",0) == 4) and (FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Draft").GetFloat("gridSpacing",10) == 100)) else False}}



### Créez un nouveau document 

Si vous venez d\'installer FreeCAD, vous consultez probablement actuellement la **page de démarrage de FreeCAD** :

<img alt="" src=images/BIM_tutorial_13.jpg  style="width:300px;">

La page de démarrage répertorie les derniers documents avec lesquels vous avez travaillé et, sur ses différents onglets, explique comment obtenir de l\'aide. Mais pour commencer à travailler, nous devons créer un nouveau **document** vide. Si vous ne l\'avez pas encore fait, créez maintenant un nouveau document en utilisant l\'élément \"Créer nouveau \...\" de la page de démarrage, ou en accédant au menu **Fichier -\> Nouveau** :

<img alt="" src=images/BIM_tutorial_09.jpg  style="width:300px;">

Vous vous retrouverez alors dans l\'espace 3D de FreeCAD, prêt à travailler :

<img alt="" src=images/BIM_tutorial_10.jpg  style="width:300px;">


{{BIMTutorialAction|goal1=Créer un nouveau document|test1=True if FreeCAD.ActiveDocument else False}}



### Naviguer dans la vue 3D 

Il existe plusieurs façons d\'interagir avec la souris dans FreeCAD. Ils sont appelés [styles de navigation](Mouse_navigation/fr.md). Vous pouvez modifier le style de navigation actuel à tout moment en cliquant sur le bouton de style de navigation dans la barre d\'état. Passer la souris sur ce bouton vous montrera également ce que fait chaque bouton de la souris. Plusieurs d\'entre eux sont conçus pour correspondre à d\'autres applications bien connues. Choisissez celui avec lequel vous êtes à l\'aise.

<img alt="" src=images/BIM_Tutorial_03.jpg  style="width:300px;">

Le contrôle de la façon dont vous regardez votre modèle dans la vue 3D peut être effectué de plusieurs manières: à l\'aide de la **souris** (selon le style de navigation que vous avez choisi), du **clavier** (explorez le contenu de le menu **Affichage** pour en savoir plus) ou le [Cube de navigation](Navigation_Cube/fr.md) (cliquez sur les différentes flèches et faces du cube pour aligner la vue).

<img alt="" src=images/BIM_Tutorial_04.jpg  style="width:300px;">


{{BIMTutorialAction|goal1=Choisissez un style de navigation|test1=True|goal2=Choisissez Vue de dessus|test2=True if FreeCADGui.ActiveDocument.ActiveView.getViewDirection().getAngle(FreeCAD.Vector(0,0,-1)) < 0.01 else False}}



### Réorganiser l\'interface 

Tous les panneaux et barres d\'outils de FreeCAD peuvent être déplacés et réorganisés. Les panneaux plus grands peuvent également être joints en les faisant glisser et en les déposant sur un autre. Si votre écran est trop petit pour afficher toutes les barres d\'outils et leur contenu (les barres d\'outils tronquées apparaîtront avec un signe \>\>), il peut être judicieux de les déplacer vers une meilleure position.

<img alt="" src=images/BIM_Tutorial_05.jpg  style="width:300px;">

Les barres d\'outils et les panneaux peuvent également être activés et désactivés à partir du menu **Affichage**.

L\'atelier BIM comporte également des boutons de commutation dans la barre d\'état, qui active et désactive des panneaux supplémentaires tels que la vue de sélection, la vue de rapport et la console Python. Ces panneaux sont souvent utiles lorsque vous travaillez avec FreeCAD, mais ils utilisent un espace d\'écran précieux. Vous pouvez généralement tout désactiver jusqu\'à ce que vous en ayez besoin. N\'oubliez pas que les messages d\'erreur sont imprimés dans la fenêtre de rapport, donc en cas de problème, assurez-vous d\'y jeter un œil.

<img alt="" src=images/BIM_tutorial_17.jpg  style="width:300px;">


{{BIMTutorialAction|descr=Aucune action à effectuer pour cette étape}}



### Outils de l\'atelier BIM 

L\'[atelier BIM](BIM_Workbench.md) contient des outils empruntés à d\'autres ateliers tels que [Arch](Arch_Workbench/fr.md), [Draft](Draft_Workbench/fr.md) ou [Part](Part_Workbench/fr.md), ainsi que quelques-uns de leurs outils. Ceux-ci sont organisés en plusieurs catégories. Chaque catégorie a un menu et une barre d\'outils. Prenez un moment pour explorer le contenu des menus décrits ci-dessous.



#### Dessin 2D 

Ces outils vous permettent de dessiner des objets plats, tels que des lignes, des polylignes, des rectangles, des arcs, etc\... qui deviendront les bases de vos objets BIM. Par exemple, vous pouvez utiliser une polyligne pour définir la trace de base d\'un mur ou un rectangle comme profil pour une poutre. Tous les objets 2D sont créés dans le [plan de travail](Draft_SelectPlane/fr.md).

<img alt="" src=images/BIM_Tutorial_35.jpg  style="width:300px;">



#### Modélisation 3D et BIM 

Cette catégorie contient des outils pour créer des objets BIM tels que [murs](Arch_Wall/fr.md) ou [fenêtre](Arch_Window/fr.md) et des objets 3D génériques non BIM tels que [boîtes](BIM_Box/fr.md), que vous pouvez tourner dans des objets BIM ultérieurement. Le résultat est différent si vous utilisez l\'outil avec un objet sélectionné ou non. Sinon, une interface de création vous sera présentée. Si vous avez sélectionné un objet avant d\'exécuter l\'outil, un objet du type correspondant sera créé en utilisant l\'objet sélectionné comme base.

<img alt="" src=images/BIM_Tutorial_33.jpg  style="width:300px;">

Un exemple typique est d\'appuyer sur le bouton [mur](Arch_Wall/fr.md) avec un [ligne](Draft_Line/fr.md) ou [polyligne](Draft_Wire/fr.md) sélectionné. Un mur sera créé automatiquement en utilisant la ligne ou la polyligne comme ligne de base.

Les objets non BIM, y compris les objets créés dans d\'autres ateliers, peuvent être transformés à tout moment en objets BIM en les sélectionnant et en appuyant sur l\'un des boutons de l\'outil BIM.

#### Annotation

Ces outils produisent des objets annotatifs tels que des cotes, des textes, des étiquettes ou des grilles, qui ne sont pas utilisés pour la modélisation mais pour annoter vos modèles et produire des dessins compréhensibles.

<img alt="" src=images/BIM_Tutorial_34.jpg  style="width:300px;">



#### Accrochage

Ces outils activent/désactivent les [accrochages](Draft_Snap/fr.md). Comme dans la plupart des applications BIM, chaque position d\'accrochage supplémentaire ajoute du temps de calcul lors du dessin, il est donc préférable de ne garder que celles dont vous avez besoin activées.



#### Modifier

Ces outils modifient les objets existants. Ils contiennent des outils de transformation habituels tels que Déplacer ou Rotation, ainsi qu\'une série d\'autres qui ne fonctionnent que pour des types d\'objets spécifiques.



#### Gérer

Cette catégorie contient des outils de gestion générale. La plupart d\'entre eux vous permettent de modifier simultanément les propriétés BIM d\'un grand groupe d\'objets sans avoir à les sélectionner.

Chaque outil contenu dans ces menus possède sa propre page de documentation qui décrit en détail son fonctionnement et les options disponibles. Ils sont listés sur la page [atelier BIM](BIM_Workbench/fr.md), également accessible depuis le menu **Aide** ou en utilisant le menu **Aide -\> Qu\'est-ce que c\'est?** Et en cliquant sur n\'importe quel bouton de la barre d\'outils.


{{BIMTutorialAction|descr=Aucune action à effectuer pour cette étape}}



### Préparez votre espace de travail 

Il existe de nombreuses façons de créer des objets BIM dans FreeCAD. Vous pouvez utiliser les [outils BIM](BIM_Workbench/fr.md) natifs de cet atelier ou utiliser n\'importe quel autre outil FreeCAD d\'autres [ateliers](Workbenches/fr.md). Les outils de dessin 2D et les outils BIM 3D de cet atelier, contrairement à d\'autres ateliers tels que Part Design, utilisent largement les **plans de travail** et **l\'accrochage**.

Le [plan de travail](Draft_SelectPlane/fr.md) est l\'endroit où vos prochains objets seront créés. Vous pouvez le définir sur l\'un des plans orthogonaux de base (sol, avant, côté) ou utiliser n\'importe quelle face sélectionnée pour définir le plan de travail courant. Vous pouvez également utiliser des [Proxy pour le plan de travail](Draft_WorkingPlaneProxy/fr.md) depuis le menu **Utilities** pour stocker une position spécifique du plan de travail dans votre modèle. [Partie de bâtiment](Arch_BuildingPart/fr.md) contient également une position implicite du plan de travail. Le changement du plan de travail actuel se fait en appuyant sur le bouton du plan de travail dans la barre d\'outils BIM. La **grille** reflète toujours l\'emplacement du plan de travail.

Comme vous l\'aurez remarqué, l\'angle de vue et le plan de travail ne sont pas liés. Vous pouvez travailler sur votre plan de travail sous n\'importe quel angle de vue.

Réglez maintenant le plan de travail en mode \"Haut\":

<img alt="" src=images/BIM_Tutorial_06.jpg  style="width:300px;">

Les [outils d\'accrochage](Draft_Snap/fr.md) vous permettent de placer de nouveaux objets et points précisément en fonction de la géométrie existante. Cependant, l\'activation de nombreux emplacements d\'accrochage peut ralentir les opérations de dessin, il est donc judicieux de n\'activer que les outils d\'accrochage que vous souhaitez utiliser. Prenez un moment pour passer en revue ce que chacun d\'eux fait, afin que, si nécessaire, vous saurez lequel peut être désactivé.

<img alt="" src=images/BIM_Tutorial_07.jpg  style="width:300px;">

Faites particulièrement attention au dernier, l\'outil **Accrochage du plan de travail** car il forcera tout point cassé à se trouver sur le plan de travail, vous empêchant ainsi de vous enclencher au-dessus ou sous le plan de travail. Vous devrez souvent l\'activer ou la désactiver, selon l\'opération que vous effectuez.


{{BIMTutorialAction|goal1=Réglez le plan de travail en mode "Top" (XY)|test1=True if ((FreeCAD.DraftWorkingPlane.axis.getAngle(FreeCAD.Vector(0,0,1)) < 0.01) and (FreeCAD.DraftWorkingPlane.weak == False)) else False|goal2=Passez en revue les différents outils d'accrochage|test2=True}}



### Dessiner un premier mur 

Commençons à construire notre pavillon en créant des murs. Les murs peuvent être faits soit directement avec l\'outil [mur](Arch_Wall/fr.md), soit en dessinant d\'abord des objets 2D tels que [lignes](Draft_Line/fr.md), [fil](Draft_Wire/fr.md) (polylignes) ou [esquisses](Sketcher_NewSketch/fr.md) qui définiront la ligne de base de nos murs. Lorsque vous avez sélectionné un tel objet de ligne de base, le fait d\'appuyer sur l\'outil Mur le convertira automatiquement en mur.

Commencez par effectuer un zoom arrière jusqu\'à ce qu\'une bonne partie ou la totalité de la grille soit visible. Cela permettra de voir beaucoup plus facilement ce que nous faisons:

<img alt="" src=images/BIM_tutorial_15.jpg  style="width:300px;">

Ensuite, appuyez sur le bouton <img alt="" src=images/_Arch_Wall.png  style="width:16px;"> **Mur** dans la barre d\'outils (ou choisissez l\'élément de menu **3D/BIM -\> Mur**). Cliquez sur deux points de la grille, alignés verticalement, distants de **300 cm**. Appuyer sur SHIFT après avoir cliqué sur le premier point vous aidera à maintenir votre mur horizontal ou vertical. Le panneau latéral vous informera de la longueur du mur lors du dessin.

<img alt="" src=images/BIM_tutorial_16.jpg  style="width:300px;">

Si vous avez créé un mauvais mur, pas de soucis! Supprimez-le ou annulez-le simplement (menu **Édition -\> Annuler**) et réessayez.


{{BIMTutorialAction|goal1=Créer un mur|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "MakeBlocks" in o.PropertiesList]) == 1)}}



### Dessiner un second mur 

Faites un deuxième mur horizontal de 4 mètres (ou 400 centimètres) de long. Sélectionnez à nouveau l\'outil <img alt="" src=images/Arch_Wall.png  style="width:16px;"> **Mur**, effectuez un panoramique et un zoom arrière jusqu\'à ce que vous voyiez une bonne zone de la grille, puis choisissez deux points dans la grille pour définir les points de départ et de fin du nouveau mur:

<img alt="" src=images/BIM_tutorial_11.jpg  style="width:300px;">

Une fois qu\'ils sont créés, sélectionnez les deux murs en appuyant sur CTRL et en cliquant dessus tous les deux dans la vue 3D ou dans la [vue arborescente](Document_structure/fr.md), et ajustez leur propriété **height** (hauteur) à 2,5 mètres et leur **width** (largeur)à 20 centimètres (ou toute autre mesure avec laquelle vous êtes à l\'aise, si vous travaillez dans une autre unité), et donc ils ressemblent à ceci (Utilisez la souris pour faire pivoter la vue, en fonction du style de navigation que vous avez choisi) :

<img alt="" src=images/BIM_tutorial_08.jpg  style="width:300px;">

Vous pouvez toujours corriger ou modifier les propriétés après la création d\'un mur ou de tout autre objet BIM. En développant l\'objet mur dans l\'arborescence, puis en double-cliquant sur la ligne de base du mur, vous pouvez également modifier son objet 2D de base. La plupart des objets BIM de FreeCAD sont basés sur un autre objet, tel qu\'une ligne de base ou un profil.

<img alt="" src=images/BIM_tutorial_12.jpg  style="width:300px;">



#### Remarque importante 

Vous remarquerez que certaines modifications de propriété, dans FreeCAD, ne se reflètent pas immédiatement sur l\'objet dans la vue 3D. Au lieu de cela, l\'objet est marqué d\'une marque bleue \"à recalculer\" dans l\'arborescence:

<img alt="" src=images/BIM_Tutorial_20.jpg  style="width:300px;">

La raison en est qu\'un document FreeCAD peut être une chaîne très complexe d\'objets interdépendants. Une mise à jour peut déclencher une mise à jour sur beaucoup d\'autres objets et donc prendre du temps. Pour éviter cela, certaines opérations marquent simplement l\'objet à recalculer, et vous déclenchez le recalcul vous-même en utilisant le menu **Edition -\> Actualiser** ou en appuyant sur **Ctrl+R**.


{{BIMTutorialAction|goal1=Créer deux objets mur orthogonaux|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "MakeBlocks" in o.PropertiesList]) == 2)|goal2=Régler leur hauteur à 2,50 mètres et leur largeur à 20 centimètres|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "MakeBlocks" in o.PropertiesList and o.Height.Value == 2500 and o.Width.Value == 200]) == 2)}}



### N\'oubliez pas de sauvegarder le fichier régulièrement! 

Comme toute autre application informatique, FreeCAD est susceptible de malfonctionner ou de planter, surtout lorsque nous en avons peu d\'expérience. Enregistrer souvent votre fichier est une très bonne habitude à prendre dans ces premiers instants. FreeCAD dispose également d\'un mécanisme d\'enregistrement automatique, que vous pouvez configurer dans le menu **Édition -\> Préférences -\> Général -\> Document**.

Enregistrez votre fichier maintenant en utilisant le menu **Fichier -\> Enregistrer**.


{{BIMTutorialAction|goal1=Enregistrez votre fichier|test1=bool(FreeCAD.ActiveDocument.FileName)}}



### Dessiner une dalle de toit 

Nous allons maintenant placer une dalle de toit sur nos murs. Au lieu de dessiner directement la dalle, comme nous l\'avons fait avec les murs, nous allons d\'abord dessiner un rectangle, puis transformer le rectangle en dalle. Nous allons maintenant explorer deux méthodes pour ce faire, les deux sont utiles à connaître, nous vous suggérons donc d\'en essayer une d\'abord, puis de l\'annuler (ou de recharger le fichier) et essayer l\'autre méthode.



#### Méthode 1: dessinez la dalle au sol, puis déplacez-la en position 

Il est souvent pratique de considérer le plan XY supérieur (le plan du sol) comme une sorte de \"planche à dessin\", où nous construirons nos objets, puis nous nous déplacerons à côté de leur position correcte. Il y a un avantage supplémentaire ici: notre plan de travail est déjà en mode \"Top\" donc nous n\'avons pas besoin de le changer.

Placez-vous en vue de dessus, effectuez un zoom arrière jusqu\'à ce que vous voyiez les deux murs et dessinez un rectangle les englobant tous les deux. Appuyez sur le bouton <img alt="" src=images/Draft_Rectangle.png  style="width:16px;"> **Rectangle** dans la barre d\'outils (ou choisissez l\'élément de menu **2D Drafting -\> Rectangle**):

<img alt="" src=images/BIM_Tutorial_18.jpg  style="width:300px;">

Faites pivoter votre vue pour inspecter les résultats. Par défaut, le rectangle est fait d\'une face. Cela peut être changé en changeant la propriété **Make Face** de notre rectangle sur False. Pour la dalle que nous allons construire, cela n\'a aucun impact, pour d\'autres types d\'objets, cependant, l\'objet de base étant une polyligne ou une face peut faire la différence.

<img alt="" src=images/BIM_Tutorial_19.jpg  style="width:300px;">

L\'étape suivante consiste à construire une dalle en \"extrudant\" celle-ci avec notre rectangle comme son \"profil\" de base. Dans FreeCAD, les objets structurels tels que les poteaux, les poutres ou les dalles sont tous fabriqués avec un même objet, appelé **Structure**. Après la création d\'un objet structurel, il suffit de définir la propriété **Type IFC** sur le type souhaité (colonne, dalle, etc.) pour changer son type.

Assurez-vous que notre rectangle est sélectionné, puis appuyez sur le bouton <img alt="" src=images/_BIM_Slab.png  style="width:16px;"> **Slab** dans la barre d\'outils (ou choisissez l\'élément du menu **3D/BIM -\> Slab**) . Comme indiqué ci-dessus, cela peut également être fait avec les outils Column (Colonne) ou Beam (Poutre), car ils produisent tous le même type d\'objet. Une fois notre objet créé, nous devons apporter les modifications suivantes à ses propriétés:

-   Réglez **Height** à **20 cm**
-   Vérifiez que **IFC Type** est défini sur **Slab**

Nous devons maintenant déplacer notre nouvelle dalle de toit dans sa position correcte, c\'est-à-dire au-dessus des murs. Il faut donc le déplacer vers le haut, dans la direction Z, d\'une distance de 250 cm, qui est la hauteur de nos murs. Nous pouvons simplement modifier la propriété **Placement** de notre dalle, étendre son attribut **Position** et définir la valeur de **z** sur 250 cm. Notre dalle est maintenant bien en place:

<img alt="" src=images/BIM_Tutorial_21.jpg  style="width:300px;">

Une autre façon de déplacer notre dalle à sa position correcte, est d\'utiliser l\'outil <img alt="" src=images/Draft_Move.png  style="width:16px;"> **Déplacer** du menu **Modifier**. Pour cela, nous devons d\'abord définir notre plan de travail dans un plan vertical, en appuyant sur le bouton <img alt="" src=images/Draft_SelectPlane.png  style="width:16px;"> **plan de travail** (assurez-vous qu\'aucune face n\'est sélectionnée ), et le régler sur **XZ (avant)**. En nous plaçant en vue de face (appuyez sur la touche **1**), nous pouvons maintenant sélectionner la dalle, appuyer sur le bouton <img alt="" src=images/Draft_Move.png  style="width:16px;"> **Déplacer** et déplacer notre dalle en cliquant sur l\'un de ses points de base puis en appuyant sur **Shift** pour restreindre le mouvement verticalement, cliquez sur un point au-dessus des murs :

<img alt="" src=images/BIM_Tutorial_23.jpg  style="width:300px;">



#### Méthode 2: dessinez la dalle directement dans le plan correct 

Une autre méthode utile consiste à travailler directement sur le plan prévu. Nous pouvons facilement placer le plan de travail sur la surface supérieure des murs, là où nous voulons notre dalle. En sélectionnant une face et en appuyant sur le bouton <img alt="" src=images/Draft_SelectPlane.png  style="width:16px;"> **plan de travail**, le plan de travail coïncide avec la face sélectionnée. Sélectionnez la face supérieure du mur et définissez-la comme plan de travail courant. Le placement de la grille se déplace pour afficher le plan de travail actuel.

<img alt="" src=images/BIM_Tutorial_22.jpg  style="width:300px;">

Tout ce que nous tirons désormais se passera dans cet avion. Si vous le souhaitez, vous pouvez maintenant vous mettre en vue de dessus, mais ce n\'est pas nécessaire. Une fois que votre plan de travail est défini et si **l\'accrochage au plan de travail** est activé, vous pouvez dessiner directement dans n\'importe quel type de vue 3D.

Une fois notre *profil* rectangulaire dessiné, nous pouvons suivre la même méthode que dans la première méthode pour créer une dalle (sélectionnez-la, appuyez sur le bouton **Structure**, ajustez ses propriétés).


{{BIMTutorialAction|goal1=Créer un rectangle|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Rectangle" in o.Name]) == 1)|goal2=Créer une dalle de 20 cm d'épaisseur|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "IfcType" in o.PropertiesList and o.IfcType == "Slab" and o.Height.Value == 200]) == 1)}}



### Créer une colonne métallique 

Ajoutons une colonne métallique pour donner un meilleur support à notre dalle. Assurez-vous que le plan de travail est en mode Top. Commençons par nous mettre en vue de dessus (appuyez sur la touche **2**) et faites disparaitre la dalle pour mieux voir ce qui se trouve en dessous. Sélectionnez la dalle et appuyez sur la touche **Espace** pour désactiver son affichage.

Dans FreeCAD, il est très facile d\'activer et de désactiver des objets ou des groupes. L\'arborescence vous montre clairement ce qui est affiché et ce qui est caché. Assurez-vous de l\'utiliser souvent!

L\'outil **Colonne** (ainsi que l\'outil Beam) a des profils intégrés que nous allons utiliser maintenant. Assurez-vous que rien n\'est sélectionné, puis appuyez sur le bouton Colonne. Dans les **Options de structure**, sélectionnez **CHS** (pour \"Circular Hollow Section\"; RHS est \"Rectangular Hollow Section\", HEA, HEB, etc. sont des variantes de section \"H\", etc.) :

<img alt="" src=images/BIM_Tutorial_24.jpg  style="width:300px;">

Et cliquez sur un point pour placer votre colonne, plus ou moins à cette position. Assurez-vous que la nouvelle colonne a un type IFC de \"Column\" et donnez-lui une hauteur de 250 cm pour qu\'elle soit à la même hauteur que nos murs.

<img alt="" src=images/BIM_Tutorial_25.jpg  style="width:300px;">

Malheureusement, le préréglage CTS n\'a qu\'une seule option de diamètre de 42 mm, qui est très mince pour supporter notre dalle de toit en béton. Heureusement, comme tout est paramétrique, il est facile de changer le diamètre. Développez le nouvel objet structurel dans l\'arborescence et vous trouverez son objet de profil, nommé CTS423. Changez son diamètre à 12 cm et son épaisseur à 8 mm. Maintenant, nous avons une colonne assez forte. Notez que vous pouvez spécifier des unités à la volée et basculer entre 0,8 cm et 8 mm sans problème. FreeCAD se chargera de la conversion.



#### Ajouter une plaque de support 

Nous avons besoin d\'un moyen de fixer notre colonne métallique à la dalle de béton. Ajoutons donc une plaque à son sommet, qui peut être boulonnée à la dalle de béton. Cela illustrera comment vous pouvez facilement modifier les objets BIM et créer ceux très précis dont vous avez besoin.

Commençons par changer la hauteur de notre colonne de 250cm à 249cm, pour lui donner un espace pour une plaque de 1cm d\'épaisseur. Dessinez ensuite un rectangle de 20 cm x 20 cm, soit sur le plan du sol, soit en définissant le haut de la colonne comme plan de travail courant, comme nous l\'avons appris à l\'étape précédente. Utilisez l\'outil **Move**, avec les accrochages au milieu et au centre activés, si nécessaire, pour centrer le rectangle sur le centre de la colonne.

En utilisant à nouveau l\'outil Slab (Dalle), créez un objet structurel à partir du rectangle, donnez-lui une hauteur de 1 cm et déplacez-le à une hauteur de 249 cm:

<img alt="" src=images/BIM_Tutorial_26.jpg  style="width:300px;">

Ajoutons maintenant notre plaque à la colonne. Les objets BIM dans FreeCAD ont deux propriétés nommées **Ajouts** et **Soustractions** qui peuvent recevoir des objets qui doivent être réunis ou soustraits à / à partir d\'eux. Pour ajouter la plaque à notre colonne, sélectionnez la plaque, puis, en appuyant sur **Ctrl**, sélectionnez la colonne et utilisez l\'outil <img alt="" src=images/Arch_Add.png  style="width:16px;"> **Ajouter** du menu **Modifier**. Notre plaque fait désormais partie de la colonne:

<img alt="" src=images/BIM_Tutorial_27.jpg  style="width:300px;">

En partant de formes simples comme des \"profils\" et en ajoutant ou en soustrayant des objets, nous pouvons créer rapidement des objets BIM très complexes. Notez que les ajouts et soustractions d\'un objet BIM donné peuvent facilement être modifiés en double-cliquant dessus dans l\'arborescence et en utilisant les boutons Ajouter et Supprimer. En outre, un même objet peut être utilisé comme addition ou soustraction à plusieurs autres objets.

<img alt="" src=images/BIM_Tutorial_28.jpg  style="width:300px;">


{{BIMTutorialAction|goal1=Créer une colonne tubulaire CTH|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "CTH" in o.Label]) == 1)|goal2=Ajouter une plaque de 20 cm x 20 cm à la colonne|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Shape" in o.PropertiesList and (abs(o.Shape.Volume - 7409000) < 10000)]) == 1)}}



### Ajouter une porte 

Comme les colonnes et les poutres, les portes et les fenêtres sont créées avec le même objet [fenêtre](Arch_Window/fr.md) dans FreeCAD. Seul leur type IFC change. Ils peuvent être indépendants ou, si un objet est sélectionné lors de l\'exécution de l\'outil, insérés dans un autre objet BIM, auquel cas ils créeront automatiquement un trou à travers celui-ci.

Insérons une porte en verre de 80 cm x 210 cm dans l\'un de nos murs. Commencez par placer le plan de travail sur une face d\'un mur, ce qui facilitera le positionnement précis de notre fenêtre:

<img alt="" src=images/BIM_Tutorial_29.jpg  style="width:300px;">

Ensuite, avec le mur sélectionné, sélectionnez **Door** dans le menu **BIM**. Sélectionnez le préréglage **Glass door** et réglez la **Width** sur 80 cm et la **Height** sur 210 cm. Vous pouvez définir les autres valeurs à votre guise:

<img alt="" src=images/BIM_Tutorial_30.jpg  style="width:300px;">

Cliquez sur un point de la base du mur où vous souhaitez placer la fenêtre. Cela peut être difficile, car les lignes de la grille ne correspondent pas nécessairement aux bords du mur. Appuyez sur la touche **Q** pendant que vous avez un accrochage actif à une intersection de la grille, puis appuyez à nouveau avec un accrochage actif sur le bas du mur. FreeCAD créera un nouveau point d\'accrochage à l\'intersection de leur axe horizontal/vertical. Utilisez ceci pour trouver un point approprié:

<img alt="" src=images/BIM_Tutorial_31.jpg  style="width:300px;">

Si votre porte n\'a pas été placée correctement, essayez l\'outil **Move** pour la déplacer dans sa position correcte. Sinon, utilisez l\'annulation ou supprimez-le de l\'arborescence du modèle et réessayez.

Lorsque tout est fait, vous devriez obtenir une porte correctement insérée dans son mur:

<img alt="" src=images/BIM_Tutorial_32.jpg  style="width:300px;">


{{BIMTutorialAction|goal1=Créer une porte vitrée|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Window" in o.Name]) == 1)}}



### Organiser votre modèle 

Nous avons maintenant dans notre modèle une collection croissante d\'objets BIM. Il est temps de ranger les choses. La création de modèles bien organisés, facilement compréhensibles par les autres, est une partie très importante de la construction de modèles BIM de qualité.

Une première habitude très simple et très bonne à prendre est de donner des noms corrects et significatifs à nos objets, afin que nous puissions les identifier facilement dans l\'arborescence par la suite. Pour renommer un objet, cliquez dessus avec le bouton droit de la souris dans l\'arborescence et choisissez **Renommer**. Un modèle où les composants sont facilement identifiables par les autres est une grande partie de ce qui fait un bon modèle BIM.

Une autre opération intéressante à faire est le **regroupement**. Les groupes vous permettent d\'organiser vos objets dans l\'arborescence, comme des fichiers et des dossiers. Un objet ne peut appartenir qu\'à un seul groupe. Les groupes sont créés en cliquant avec le bouton droit de la souris sur la racine du document ou sur tout autre groupe dans l\'arborescence et en sélectionnant **Create group**. Vous pouvez ensuite faire glisser des objets dans et hors des groupes dans l\'arborescence.

Une troisième façon d\'organiser les choses consiste à utiliser des calques. Les couches sont indépendantes des groupes, vous pouvez utiliser les deux systèmes en même temps si vous le souhaitez. Comme les groupes, les calques vous permettent d\'activer/désactiver facilement une série d\'objets, mais contrairement aux groupes, ils ne peuvent pas être empilés les uns dans les autres. Ils vous permettent également de remplacer les paramètres visuels tels que la couleur et la largeur de ligne de leurs objets enfants. Les calques sont créés et gérés à l\'aide de l\'outil de gestion des calques qui se trouve dans le menu **Gestion -\> Gérer les calques**. Les objets sont ajoutés ou supprimés en les faisant glisser dans et hors des calques dans l\'arborescence.

Le **Sélecteur de calque** (Layer selector)sur la barre d\'outils principale vous permet de définir un calque courant. Après cela, tout nouvel objet 2D ou BIM sera automatiquement placé dans ce calque.

Enfin, les applications BIM permettent généralement de regrouper des objets en **levels** (niveaux ou étages) et **buildings** (bâtiments). FreeCAD propose également ces outils dans le menu **3D/BIM modeling**. Comme les poutres et les poteaux, les niveaux et les bâtiments utilisent un même type d\'objet appelé [Partie de bâtiment](Arch_BuildingPart/fr.md) avec un type IFC différent. Ils fonctionnent de la même manière que les groupes, une fois créés, vous pouvez faire glisser et déposer n\'importe quel objet à l\'intérieur et à l\'extérieur. Les éléments de construction sont compatibles avec les groupes, vous pouvez donc y placer des groupes.

<img alt="" src=images/BIM_Tutorial_36.jpg  style="width:300px;">

Les Building Parts ont de nombreuses autres utilisations, reportez-vous à leur [documentation](Arch_BuildingPart/fr.md) pour en savoir plus.

Créez une Building Part (Partie de bâtiment) maintenant en sélectionnant **Level** dans le menu **3D/BIM Modeling**. Assurez-vous que son type IFC est défini sur **Building Storey** et faites glisser tous nos autres objets racine BIM (pas besoin de le faire avec les objets inclus comme la porte ou la plaque de la colonne) dedans, c\'est-à-dire nos deux murs, la dalle de toit et la colonne métallique.

Notez que, comme les éléments de construction sont des composants de construction génériques, vous n\'êtes pas obligé d\'organiser votre modèle par niveaux dans FreeCAD. Vous pouvez choisir de regrouper vos éléments différemment. Le format IFC s\'attend à ce que les éléments soient regroupés par niveau, donc si vous prévoyez d\'utiliser ce format, il est préférable de considérer vos éléments de construction comme des niveaux.


{{BIMTutorialAction|goal1=Créer un niveau|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "BuildingPart" in o.Name]) == 1)|goal2=Ajoutez-y les quatre autres objets BIM racine|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "BuildingPart" in o.Name and (len(o.Group) == 4)]) == 1)}}



### Ajout de plans de coupe 

L\'une des opérations les plus couramment effectuées avec un modèle BIM consiste à en extraire des dessins 2D, tels que des plans ou des élévations. Il existe plusieurs façons de le faire dans FreeCAD, en fonction du résultat que vous souhaitez obtenir. Fondamentalement, vous pouvez choisir entre produire le résultat 2D à l\'intérieur de l\'espace 3D, ce qui est utile si vous souhaitez le retravailler là-bas, construire plus loin ou mieux contrôler la façon dont il est exporté vers des formats tels que [DXF](Draft_DXF/fr.md) ou [DWG](FreeCAD_and_DWG_Import/fr.md), ou sur une [TechDraw feuille](TechDraw_Workbench/fr.md) mieux adaptée pour l\'impression ou l\'exportation au format PDF. Dans les deux cas, cela commence par placer un [Plan de coupe](Arch_SectionPlane/fr.md) dans votre modèle:

<img alt="" src=images/BIM_Tutorial_37.jpg  style="width:300px;">

1.  Sélectionnez l\'objet Level qui contient vos objets, que nous avons créé à la dernière étape
2.  Ajouter un plan de coupe à partir du menu **Annotations-\>Section Plane**

Les plans de coupe ne traversent pas tout le modèle, mais seulement les objets dans leur propriété *Objets*. Vous pouvez sélectionner le plan de coupe pour vérifier et modifier le contenu de cette propriété à tout moment.

Par défaut, le nouveau plan de coupe sera placé au milieu de l\'objet sélectionné ou de son contenu, et regardera vers le bas, comme pour créer une vue de plan d\'étage. Mais le plan de coupe est un objet comme un autre et peut être déplacé et tourné pour faire ce dont vous avez besoin. Placez-le horizontalement pour créer une vue en plan, verticalement à l\'intérieur de votre modèle pour créer une coupe ou à l\'extérieur du modèle pour créer une élévation.


{{BIMTutorialAction|goal1=Sélectionner le principal Building Part|test1=bool(len([o for o in FreeCADGui.Selection.getSelection() if "BuildingPart" in o.Name]) == 1)|goal2=Créer un plan de coupe|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Section" in o.Name and (len(o.Objects) == 1) and ("BuildingPart" in o.Objects[0].Name)]) == 1)}}



### Extraction de vues 2D sous forme de géométrie 

Une fois votre plan de coupe en place, nous pouvons maintenant créer une géométrie 2D à partir de ce qu\'il voit à l\'aide de l\'outil [Projection 2D d\'une forme](Draft_Shape2DView/fr.md):

<img alt="" src=images/BIM_Tutorial_38.jpg  style="width:300px;">

1.  Sélectionnez le plan de coupe
2.  Créez une vue de forme 2D en utilisant **Modify-\>Shape 2D View**
3.  Notre objet de vue est caché sous les murs. Désactivez l\'affichage du niveau et du plan de coupe en les sélectionnant tous les deux dans l\'arborescence et en appuyant sur la touche **Espace** afin que nous puissions mieux visualiser notre résultat

<img alt="" src=images/BIM_Tutorial_39.jpg  style="width:300px;">

La vue 2D que nous avons créée est un objet 2D tout-en-un et sera située sur le plan du sol (0,0) dans le modèle. Il peut être déplacé et sera recalculé si le modèle change.

Pour créer des lignes plus épaisses pour les zones coupées, vous pouvez créer une autre vue Shape 2D, et définir sa propriété *Projection Mode* à *Cutlines* ou *Cutfaces*, et sa propriété *In Place* à *False*. Vous aurez alors deux objets, un pour les lignes vues et un pour les lignes coupées, pour lesquels vous pouvez donner des épaisseurs de lignes différentes.


{{BIMTutorialAction|goal1=Sélectionner le pla de section|test1=bool(len([o for o in FreeCADGui.Selection.getSelection() if "Section" in o.Name]) == 1)|goal2=Créer une vue Forme 2D|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Shape2DView" in o.Name]) == 1)}}



### Annotation et exportation aux formats CAO 2D 

Vous pouvez placer [Textes](Draft_Text/fr.md), [Etiquettes](Draft_Label/fr.md) (texte avec ligne et flèche), [Dimensions](Draft_Dimension/fr.md) sur n\'importe quel élément de l\'espace objet: soit directement sur le modèle 3D, ou sur la vue 2D que nous avons créée à l\'étape ci-dessus. Le choix vous appartient, en fonction de ce que vous souhaitez réaliser. Si vous laissez la vue 2D exactement sous le modèle 3D, vous souhaiterez peut-être également effectuer les deux en une seule fois.

![](images/BIM_Tutorial_34.jpg )

Les annotations (textes, étiquettes, cotes) seront placées sur le **plan de travail** courant. Assurez-vous de placer votre plan de travail là où vous voulez vos annotations. Vous pouvez ainsi placer des annotations dans n\'importe quel plan de l\'espace 3D: horizontalement ou verticalement. Vous pouvez également les déplacer ou les faire pivoter après leur création.

Plaçons une dimension horizontale entre les extrémités de nos deux murs:

![](images/BIM_Tutorial_40.jpg )

1.  Réglez le **plan de travail** sur la position **Top**
2.  Orientez votre vue pour pouvoir voir la base des deux murs
3.  Choisissez le menu **Annotations -\>** <img alt="" src=images/Draft_Dimension.png  style="width:16px;"> [Dimension](Draft_Dimension/fr.md)
4.  Cliquez sur un premier point à l\'extrémité du mur gauche
5.  Appuyez sur **SHIFT** pour contraindre la cote verticalement ou horizontalement
6.  Cliquez sur un deuxième point à l\'extrémité du mur droit
7.  Cliquez sur un troisième point pour indiquer où placer la ligne de cote

Les [Dimensions](Draft_Dimension/fr.md) disposent de nombreux paramètres pour modifier leur aspect ainsi que la taille et le type du texte et de la flèche. Vous pouvez définir vos paramètres par défaut préférés dans le menu **Edition-\> Préférences-\> Draft-\> Texte et dimensions**.

Ajoutons maintenant un texte:

![](images/BIM_Tutorial_41.jpg )

1.  Choisissez le menu **Annotations -\>** <img alt="" src=images/Draft_Text.png  style="width:16px;"> [Texte](Draft_Text/fr.md)
2.  Cliquez sur un emplacement dans la vue 3D pour placer le texte
3.  Écrivez le texte que vous souhaitez, par exemple **Pavilion** puis cliquez sur le bouton **Create Text** ou appuyez deux fois sur Entrée.

Une bonne idée est de créer des **Groupes** pour les différents ensembles d\'annotations (plan, coupe, différentes échelles, etc\...):

1.  Créez un groupe en faisant un clic droit sur la racine du document et sélectionnez **Create group**, renommez-le en \"Annotations\"
2.  Sélectionnez les annotations que nous avons créées ci-dessus dans l\'arborescence et faites-les glisser et déposez-les dans le groupe



#### Exportation en DXF 

Les objets 2D tels que les lignes, les cercles ou les vues 2D comme nous l\'avons créé ci-dessus ou les annotations sont très adaptés pour être exportés vers des formats de CAO 2D traditionnels tels que [DXF ou DWG](Draft_DXF/fr.md). Le format DWG nécessite l\'installation d\'un logiciel supplémentaire sur votre système, vérifiez les [instructions](Draft_DXF/fr.md) pour le faire si nécessaire.

Essayons d\'exporter notre travail 2D en DXF:

1.  Sélectionnez la vue 2D, la cote et le texte
2.  Sélectionnez le menu **Fichier-\> Exporter**, choisissez le format **Autodesk DXF**, un nom de fichier et appuyez sur **Exporter**

Si vous n\'utilisez aucun programme de CAO 2D, il existe plusieurs applications gratuites et open-source qui peuvent ouvrir des fichiers DXF (en dehors de FreeCAD lui-même, bien sûr!), par exemple [LibreCAD](https://librecad.org/) et [QCAD CE](https://qcad.org/).

![](images/BIM_Tutorial_42.jpg )


{{BIMTutorialAction|goal1=Créer une dimension|test1=bool(len([obj for obj in FreeCAD.ActiveDocument.Objects if "Dimension" in obj.Name]))|goal2=Créer un texte|test2=bool(len([obj for obj in FreeCAD.ActiveDocument.Objects if "Text" in obj.Name]))}}



### Création d\'une géométrie 2D sur une feuille imprimable 

Les feuilles imprimables sont créées et gérées avec l\'[atelier TechDraw](TechDraw_Workbench/fr.md). Créons une nouvelle feuille et y plaçons une vue de notre modèle:

1.  Basculez vers l**\'atelier TechDraw**
2.  Créez une nouvelle feuille vide en utilisant le modèle par défaut dans le menu **TechDraw -\> Insérer une nouvelle page par défaut**
3.  Sélectionnez le plan de coupe et créez une vue sur la page en utilisant **TechDraw -\> Insérer un objet de l\'atelier Arch**
4.  Modifiez la propriété **Scale** de votre vue Arch et recalculez le modèle (F5) pour voir vos changements.

\... Et ainsi de suite


{{BIMTutorialAction|descr=Aucune action à effectuer pour cette étape}}



### Exportation d\'un fichier IFC 

Le [IFC, ou Industry Foundation Classes](https://fr.wikipedia.org/wiki/Industry_Foundation_Classes), est un protocole et un format de fichier visant à échanger le modèle BIM entre les applications. En enregistrant votre modèle en tant que fichier IFC, vous pourrez l\'ouvrir dans la plupart ou toutes les autres applications BIM open source ou propriétaires.

Les opérations d\'importation/exportation IFC dans FreeCAD sont effectuées par un logiciel externe appelé [IfcOpenShell](http://www.ifcopenshell.org/). Lisez la page [Arch IFC](Arch_IFC/.md) pour en savoir plus sur la façon de l\'installer.

Une fois IfcOpenShell installé, exporter votre modèle sous forme de fichier IFC est aussi simple que de sélectionner les objets que vous souhaitez exporter, ou simplement le conteneur supérieur (groupe ou partie de construction) qui contient tous les autres objets que vous souhaitez exporter, et utilisez le menu **Fichier-\> Exporter** et choisissez le format de fichier IFC.

Enfin, une fois que vous avez exporté un fichier IFC, c\'est toujours une bonne idée de l\'inspecter avant de l\'envoyer à d\'autres personnes, pour vous assurer que le modèle est beau et qu\'aucun objet ne manque. Il existe de nombreuses applications de visualisation IFC gratuites disponibles sur Internet pour de nombreuses plates-formes. Un bon visualiseur open-source qui fonctionne sur toutes les plates-formes est [IFC++](http://ifcquery.com/). Si vous souhaitez utiliser le fichier IFC pour des modifications ultérieures, le [module d\'extension Blender BIM](https://blenderbim.org/) peut vous être utile.

Pour tester la structure et la validité de votre modèle pour l\'exportation IFC, utilisez l\'outil *Manage-\>IFC Preflight*. Nous y reviendrons dans la section suivante.


{{BIMTutorialAction|goal1=Ouvrez l'outil de contrôle en amont BIM et exécutez tous les tests|test1=True if (hasattr(FreeCADGui,"BIMPreflightDone") and (FreeCADGui.BIMPreflightDone == True)) else False}}



### Gestion des propriétés BIM 

Une grande partie de ce qui fait un bon modèle BIM sont les propriétés non géométriques que vous pouvez donner à vos objets, telles que le type, le matériau ou les propriétés spécifiques à un certain type. Par exemple, un mur peut être marqué comme porteur ou non, ou comme extérieur ou intérieur. Le [format IFC](https://fr.wikipedia.org/wiki/Industry_Foundation_Classes) est très riche à cet égard. La quantité de spécifications et de propriétés que vous souhaitez donner à vos objets dépend principalement de vos besoins et de la manière dont vous travaillez avec les autres et de ce qu\'ils attendent de votre modèle BIM.

Une chose est importante à garder à l\'esprit: tous les objets BIM/Arch dans FreeCAD prennent en charge l\'ensemble complet des propriétés IFC. D\'autres objets FreeCAD, tels que ceux modélisés avec d\'autres ateliers, seront également exportés vers IFC, mais vous ne pouvez modifier aucune de leurs propriétés IFC. Vous pouvez cependant convertir n\'importe quel objet FreeCAD en objet BIM en sélectionnant l\'objet et en utilisant **3D/BIM -\> Create Component**.

Les principales informations que vous pouvez donner à vos objets sont:



#### Nom et description 

Cela semble évident, mais le moyen le plus simple de rendre votre modèle plus compréhensible pour les autres est de nommer correctement chacun de vos objets et, le cas échéant, d\'ajouter une description. Cela se fait simplement en sélectionnant un objet et en appuyant sur **F2** ou en changeant sa propriété **Label** pour le renommer. La description se trouvera parmi les propriétés de l\'objet.



#### Le type BIM/IFC 

C\'est l\'information la plus fondamentale. Dans FreeCAD, un objet créé avec l\'outil de mur aura son type IFC défini sur \"Wall\" par défaut. Mais vous pouvez changer cela à tout moment. Vous pouvez donc utiliser l\'outil de mur pour modéliser une poutre par exemple. Il vous suffit de changer son type IFC après l\'avoir créé. Pour modifier le type IFC d\'un objet, sélectionnez-le, recherchez son **IFC Type** dans ses propriétés et passez à un autre type dans la liste déroulante.

Vous pouvez également gérer en bloc les noms, les types et les matériaux de plusieurs objets à la fois en utilisant le gestionnaire d\'éléments IFC qui se trouve sous le menu **Manage-\>IFC elements**.



#### Matériaux

Chaque objet d\'une construction a un matériau. Il est donc logique de donner à chaque objet de votre modèle un matériau approprié, tel que du béton ou du bois. Pour attribuer un matériau à un objet, sélectionnez l\'objet, et utilisez le [gestionnaire de matériaux](Arch_SetMaterial/fr.md) du menu **Manage-\>Materials**.



#### Propriétés

Chaque objet BIM peut également recevoir des propriétés supplémentaires, par exemple pour indiquer qu\'un mur est porteur ou non. IFC vous permet d\'ajouter des propriétés personnalisées à n\'importe quoi, mais la plupart des types tels que Wall ou Beam ont également des ensembles de propriétés spéciaux et prédéfinis, généralement appelés Pset_WallCommon ou Pset_BeamCommon. Vous pouvez choisir d\'ajouter ces ensembles à vos objets, modifier la valeur des propriétés contenues dans l\'ensemble ou ajouter vos propriétés personnalisées. La gestion des propriétés IFC d\'un objet sélectionné ou la modification en bloc des propriétés de plusieurs objets à la fois se fait à l\'aide du gestionnaire de propriétés sous le menu **Manage-\>IFC properties**.



#### Quantités

Les quantités telles que la longueur ou la largeur ou la hauteur d\'un mur peuvent également être spécifiquement écrites dans un fichier IFC. Elles ne sont pas liés à la géométrie de l\'objet, donc lorsque vous rencontrez de telles quantités dans un fichier IFC, il n\'y a aucune garantie qu\'elles reflètent la géométrie réelle de l\'objet. Cependant, ces grandeurs permettent aux applications qui ne sont pas capables de traiter la géométrie, comme les tableurs, de connaître les principales dimensions des objets. Vous pouvez vérifier quelles quantités seront exportées vers IFC en utilisant le gestionnaire de quantités situé dans le menu **Manage-\>IFC quantities**.

Le format IFC a de nombreuses particularités et parfois l\'application avec laquelle vous ouvrirez votre fichier IFC ou la personne qui recevra votre fichier IFC aura des exigences supplémentaires. Devenir un modélisateur BIM courant signifie souvent se familiariser avec toutes ces particularités et ce qui doit être ajouté ou spécifié à votre modèle BIM. L\'atelier BIM de FreeCAD fournit un outil [BIM Contrôle en amont](BIM_Preflight/fr.md) qui vous permet de vérifier votre modèle pour plusieurs de ces particularités et exigences les plus courantes, et vous aide à décider ce qu\'il faut inclure ou non dans votre modèle.


{{BIMTutorialAction|descr=Aucune action à effectuer pour cette étape}}



### Explorez d\'autres outils BIM et d\'autres ateliers 

Prenez un moment pour explorer les autres outils BIM disponibles. N\'oubliez pas que certains ne sont toujours pas terminés et qu\'ils ne feront peut-être pas tout ce que vous attendez d\'eux. Utilisez le \"Qu\'est-ce que c\'est?\" bouton trouvé dans le menu **Aide** pour ouvrir la page d\'aide de n\'importe quel outil. Le [Forum FreeCAD](https://forum.freecadweb.org) est également toujours un bon endroit pour rechercher ou demander lorsque vous rencontrez un problème spécifique que vous ne pouvez pas résoudre.

FreeCAD est une grande famille d\'ateliers et les outils d\'autres ateliers sont souvent utiles. Comme nous l\'avons vu ci-dessus, presque tous les objets créés à partir d\'autres ateliers peuvent être transformés en un objet BIM valide, en utilisant simplement l\'outil **3D/BIM -\> Create component** et en leurs donnant le type IFC correct.

Davantages de tutoriels sur BIM et les autres ateliers dans la section [Tutoriels](Tutorials/fr.md) de la [documentation FreeCAD](https://wiki.freecadweb.org) et une série vidéo complète de [tutoriels BIM](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU) sur youtube.


{{BIMTutorialAction|descr=Aucune action à effectuer pour cette étape}}



### Aidez FreeCAD à devenir un meilleur outil! 

FreeCAD est un logiciel gratuit, développé par une communauté passionnée d\'utilisateurs, certains d\'entre eux développant du code, et beaucoup d\'autres contribuant sous une forme ou une autre à améliorer le logiciel, en écrivant de la documentation, en trouvant et en signalant des bogues, en soumettant des idées, en écrivant des tutoriels, et beaucoup d\'autres choses. Plus nous sommes actifs, plus le logiciel se développe rapidement. Pourquoi ne pas nous rejoindre? Un bon point de départ est la [section BIM sur le forum FreeCAD](https://forum.freecadweb.org/viewforum.php?f=23). On se voit là-bas!


{{BIMTutorialAction|descr=Aucune action à effectuer pour cette étape}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [BIM](Category_BIM.md) > [Tutorials](Category_Tutorials.md) > BIM ingame tutorial/fr
