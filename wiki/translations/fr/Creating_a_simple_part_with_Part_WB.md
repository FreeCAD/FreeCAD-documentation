---
- TutorialInfo   */fr
   Topic   *Modélisation
   Level   *Débutant
   Author   *heda
   Time   *2 heures
   FCVersion   *0.19 ou supérieure
   Files   *
---

# Creating a simple part with Part WB/fr





## Introduction

Ce tutoriel a pour but d\'être utilisé comme une première introduction à la modélisation 3d en utilisant l\'[atelier Part](Part_Workbench/fr.md) ![](images/Switch_PartWorkbench.JPG ) de FreeCAD. Après avoir terminé ce tutoriel, vous devriez être en mesure de créer des modèles 3D simples en utilisant des primitives comme des cubes, des cylindres, etc. avec une technique appelée [Géométrie de construction de solides](https   *//fr.wikipedia.org/wiki/G%C3%A9om%C3%A9trie_de_construction_de_solides), en bref la modélisation **CSG** pour *Constructive Solid Geometry*. Une autre façon de créer des modèles 3D consiste à utiliser une forme 2D, par exemple en extrudant ou en faisant tourner la forme 2D dans l\'espace 3D. Pour une introduction à cette technique, veuillez suivre le tutoriel similaire *[PartDesign    * Créer une pièce simple](Creating_a_simple_part_with_PartDesign/fr.md)*. Les deux tutoriels ont intentionnellement généré exactement le même modèle, ce qui permet au débutant d\'avoir une expérience pratique des deux techniques différentes et de la façon dont elles sont mises en œuvre dans FreeCAD. La définition des deux techniques peut être considérée comme strictement divisée d\'un point de vue sémantique, cependant il n\'y a rien qui empêche directement un mélange des techniques lors de la création de modèles. Il y a quelques mises en garde à faire lors du mélange des techniques de modélisation, qui sont principalement liées à des aspects de la façon dont FreeCAD est programmé. Il y a un [3ème tutoriel](Creating_a_simple_part_with_Draft_and_Part_WB/fr.md) destiné à servir de première introduction à un exemple de modélisation mixte. Ce tutoriel utilise **l\'atelier \"Draft** pour créer un profil 2d utilisé pour extruder un solide dans **l\'atelier Part** pour créer le même modèle que dans ce tutoriel.

Avant de commencer, regardez comment **[naviguer](Mouse_navigation/fr.md)** dans l\'espace 3D. En passant le curseur sur le sélecteur de modèle de souris dans le coin inférieur droit de la fenêtre de FreeCAD, un aide-mémoire du modèle de navigation en cours apparaît comme dans l\'image ci-dessous.

![](images/T101pwb00-01_navi.png )

De nombreux nouveaux venus dans les programmes de CAO se retrouvent bloqués pendant l\'apprentissage du logiciel, si cela vous arrive, n\'hésitez pas à faire des recherches sur le wiki ou le forum pour obtenir plus d\'informations - il y a de fortes chances que d\'autres personnes aient été bloquées par la même chose dans le passé et qu\'il existe donc déjà une réponse à votre question spécifique. Vous pouvez également poster un message sur le forum pour poser vos questions ou faire part de vos découvertes. Le forum comporte plusieurs fils de discussion où les utilisateurs sont aidés à accomplir toutes sortes de tâches différentes. Ces fils de discussion sont souvent similaires à des didacticiels et comportent souvent des illustrations spécifiques.

### Le tutoriel couvre 

-   Le modèle à réaliser
-   Utilisation de l\'atelier Part pour créer et manipuler les blocs de construction primitifs.
-   Modification de la couleur et de la transparence
-   Une autre façon de localiser le trou
-   Faire du trou un trou fraisé
-   Fabrication d\'une pièce creuse
-   Une autre façon de positionner le chanfrein
-   Modification des dimensions
-   Organiser l\'arboscence un peu différemment

### Le modèle à réaliser 

<img alt="" src=images/GGTuto1_Vue.PNG  style="width   *372px;">

![](images/T101pwb01-02_dims.png )

## Utilisation de l\'atelier Part pour créer et manipuler les blocs de construction primitifs 

Créez un nouveau document et enregistrez-le directement sous un nouveau nom. Il est bon de veiller à enregistrer le document à intervalles réguliers, ou juste avant des opérations plus importantes. Passez ensuite à l**\'[atelier Part](Part_Workbench/fr.md)** en utilisant soit le [sélecteur d\'atelier](Getting_started/fr#Explorer_l.27interface.md) (étiqueté 10 dans l\'image liée) ou en allant dans le menu **Affichage → Atelier**. FreeCAD démarre avec les barres d\'outils en haut, la vue combinée à gauche et la vue 3D à droite.

### Créer le bloc solide principal 

Appuyez sur <img alt="" src=images/Part_Box.svg  style="width   *24px;"> [Cube](Part_Box/fr.md) pour créer un cube solide par défaut. Le cube apparaît dans la vue 3D et aussi comme un nouvel objet dans la [Vue en arborescence](Tree_view/fr.md) dans la barre latérale.

Appuyez sur <img alt="" src=images/Std_ViewIsometric.svg  style="width   *24px;"> [Isométrique](Std_ViewIsometric/fr.md) pour voir le cube en 3D.

![](images/T101pwb01-03_cube1.png )

Sélectionnez le cube dans la [Vue en arborescence](Tree_view/fr.md), il devient vert dans la vue 3d. Dans la vue en arborescence, vous verrez que le cube est créé par défaut avec les dimensions **Longueur x Largeur x Hauteur** de *10 x 10 x 10 mm*. Changez ces dimensions en *100 x 30 x 50* comme dans le dessin initial du modèle.

![](images/T101pwb01-04_cubedims.png )

Lorsque l\'on modifie une propriété, comme *Length*, par l\'intermédiaire de la spinbox, on peut soit entrer les valeurs, soit utiliser la molette de défilement pour cocher les valeurs vers le haut ou vers le bas. Les flèches permettant de cocher les valeurs vers le haut ou vers le bas peuvent bien entendu être utilisées. Dans l\'image la plus à droite ci-dessus, la propriété *Height* est en mode édition, en faisant tourner la molette de défilement lorsque la souris se trouve sur cette cellule, la valeur sera modifiée d\'une unité vers le haut ou vers le bas.

Cliquez sur <img alt="" src=images/Std_ViewFitAll.svg  style="width   *24px;"> **[Tout afficher](Std_ViewFitAll/fr.md)** pour voir le cube entier.

![](images/T101pwb01-05_cube2.png )

### Créer le congé 

Pour réaliser le congé sur le coin, dans la barre d\'outils, appuyez sur <img alt="" src=images/Part_Fillet.svg  style="width   *24px;"> *[Congé](Part_Fillet/fr.md)* qui ouvre le *panneau de tâches* pour les congés dans la vue combinée sur le côté. Changez la spinbox *radius* à 20 mm, puis dans la vue 3D, sélectionnez le bord de largeur en haut à droite et cliquez sur **OK**.

![](images/T101pwb01-06_filletrad.png )

Le *panneau de tâches* se ferme et vous revenez à la Vue en arborescence qui comporte maintenant un objet congé au lieu du cube précédent.

### Visibilité des enfants 

Cliquez sur le signe plus/caret pour développer les enfants du congé, qui dans ce cas est le *cube* que nous avons créé plus tôt, mais il est grisé. Sélectionnez le cube et appuyez sur la barre d\'espacement - cela permet de rendre le cube visible à nouveau et l\'icône n\'est plus grisée. Pour désélectionner le cube, cliquez dans une zone vide de la vue en arborescence ou de la vue 3D.

![](images/T101pwb01-07_fillet.png )

### Créer le chanfrein 

Ensuite, nous allons créer le *chanfrein* de 30 degrés, en commençant par activer la visibilité du cube enfant du congé. Il existe un outil de chanfrein dans l\'[atelier Part](Part_Workbench/fr.md), mais au lieu de l\'utiliser, nous allons réaliser le chanfrein avec un autre bloc et une coupe booléenne.

Créez un nouveau <img alt="" src=images/Part_Box.svg  style="width   *24px;"> **[Cube](Part_Box/fr.md)** avec des dimensions de 60 x 30 x 30. Changez l**\'angle de placement** à -30 degrés.

![](images/T101pwb01-08_chamfer1.png )

L\'angle de placement utilise le **vecteur de placement** (Axis) comme axe de rotation. Le défaut est l\'axe z, qui ne correspond pas à notre direction cible, en changeant le vecteur de placement pour l\'axe y, on obtient l\'orientation souhaitée de l\'outil de coupe pour le chanfrein.

![](images/T101pwb01-09_chamfer2.png )

Le même placement peut également être obtenu avec d\'autres valeurs. L\'alternative la plus simple d\'un placement identique est un angle de +30 degrés et un axe des y de -1.

#### Console Python 

De plus, la position doit être ajustée. En regardant le dessin de la pièce finie, il n\'y a pas de dimension directe à utiliser pour la translation prévue vers le haut. Puisque la dimension vers le haut est celle qui est nécessaire, nous devons la calculer. Utilisons la **[console Python](Python_console/fr.md)** intégrée pour ces calculs, c\'est de la trigonométrie de base. Si la console Python de FreeCAD n\'est pas visible pour vous, il suffit de faire un clic droit dans un espace vide de la zone de la barre d\'outils et de cocher la case *console Python* et elle devrait apparaître dans l\'espace de travail. Lorsque vous y êtes, vous devriez également ajouter la *[Vue rapport](Report_view/fr.md)* si elle n\'est pas déjà visible. La *vue rapport* fournit la plupart du temps des informations utiles ou même des indications sur ce qu\'il faut faire ensuite pour les différentes commandes.

![](images/T101pwb01-10_pyconsole.png )

Après avoir importé le module *[math](https   *//docs.python.org/3/library/math.html#module-math)*\' des bibliothèques standard de Python, nous pouvons utiliser la formule *(50 - math.tan(math.radians(30)) \* 50)* pour trouver la distance dans la direction z que le bloc doit déplacer. Copiez le résultat de la formule depuis la console Python et collez-le dans la position z de **Cube001**. L\'outil à utiliser pour la *coupe* du chanfrein est maintenant correctement orienté et positionné.

![](images/T101pwb01-11_chamfer3.png )

#### Expressions

Il n\'est pas nécessaire d\'utiliser la console Python pour effectuer le calcul. Dans la plupart des cas, lorsqu\'il s\'agit de valeurs paramétriques numériques, FreeCAD dispose d\'un raccourci vers une calculatrice intégrée. Cela s\'appelle **[Expressions](Expressions/fr.md)** dans FreeCAD, vous pouvez entrer dans le *mode expression* en cliquant d\'abord dans la spinbox pour la position z, une petite icône circulaire bleuâtre apparaîtra à droite.

![](images/T101pwb01-12_expression1.png )

En cliquant sur cette icône, une nouvelle fenêtre *Editeurs de formules* s\'ouvre, dans laquelle des formules et des expressions peuvent être saisies, comme indiqué ci-dessous. L\'utilisation d\'expressions est un outil puissant, car on peut accéder aux paramètres du modèle, rendant ainsi tous les paramètres du modèle disponibles comme variables à utiliser lors de la création d\'une expression. En bref, dans notre formule, au lieu d\'entrer le nombre 50 dans l\'éditeur de formule, nous pouvons entrer un \"paramètre nommé\" contenant la valeur 50 du cube, avec l\'avantage que si nous changeons la \"hauteur\" du cube, la position du chanfrein suivra automatiquement. La valeur de 50 dans le modèle actuel est appelée *Cube.Length*, c\'est-à-dire la propriété *Length* de la fonction *Cube*. Vous trouverez de plus amples informations à ce sujet sur le wiki.

![](images/T101pwb01-13_expression2.png )

Pour effectuer la coupe, avec la touche **Ctrl** enfoncée, sélectionnez d\'abord le **Fillet** dans l\'arborescence, puis le dernier cube créé (nommé **Cube001**) et enfin, dans la barre d\'outils, appuyez sur le bouton <img alt="" src=images/Part_Cut.svg  style="width   *24px;"> **[Soustraction](Part_Cut/fr.md)**. Votre arborescence devrait à nouveau comporter un seul objet à la racine appelé **Cut**.

![](images/T101pwb01-14_model1.png )

#### L\'outil de mesure 

L**\'[outil de mesure](Part_Measure_Menu/fr.md)** de l**\'atelier Part** peut être utilisé pour vérifier que notre calcul et le placement du chanfrein sont corrects. Appuyez sur le bouton <img alt="" src=images/Part_Measure_Linear.svg  style="width   *24px;"> **[Mesure linéaire](Part_Measure_Linear/fr.md)** et un *panneau de tâches* s\'ouvre, puis sélectionnez les 2 points d\'extrémité d\'un côté du chanfrein.

![](images/T101pwb01-15_model1measure1.png )

Il est donné avec une dimension x de 50 mm, effacez la mesure et fermez le dialogue.

### Créer le trou 

Pour faire le trou, appuyez sur le bouton <img alt="" src=images/Part_Cylinder.svg  style="width   *24px;"> **[Cylindre](Part_Cylinder/fr.md)**, réglez le *rayon* à 5 mm et la *hauteur* à 50 mm.

![](images/T101pwb01-16_cyl1.png )

Ensuite, nous devons positionner le trou en fonction des dimensions du dessin. Changez la vue en <img alt="" src=images/Std_ViewTop.svg  style="width   *24px;"> **[Vue de dessus](Std_ViewTop/fr.md)**, puis cliquez avec le bouton droit de la souris sur le **Cylindre** dans l\'arborescence et sélectionnez **Transformer** dans le menu contextuel.

![](images/T101pwb01-17_cyl1translate.png )

Changez *Translation increment* à 5 et utilisez les flèches rouge et verte pour positionner le cylindre dans la bonne position, en le déplaçant de 15 mm en y et 65 en x en faisant glisser les extrémités des flèches avec la souris. Cliquez sur **OK** pour fermer la boîte de dialogue *Transformer*. Pour faire le trou, appuyez sur la touche **Ctrl** et sélectionnez **Cut** et **Cylinder** dans l\'arborescence, puis appuyez sur le bouton <img alt="" src=images/Part_Cut.svg  style="width   *24px;"> **[Soustraction](Part_Cut/fr.md)** dans la barre d\'outils. Votre vue en arborescence devrait à nouveau avoir un seul objet à la racine appelé **Cut001**.

Félicitations, le modèle est maintenant prêt.

![](images/T101pwb01-18_model1complete.png )

Le modèle de base étant prêt, explorons les différentes façons de modifier ce modèle. Certains exemples concernent l\'apparence, les fonctionnalités supplémentaires ou simplement une autre façon de faire.

## Changer couleur et transparence 

Il y a plusieurs façons de modifier l\'apparence des objets, dans ce cas, utilisons l\'onglet Vue dans la partie propriété de la vue combinée. Tout d\'abord, sélectionnez l\'objet dans la vue en arborescence, puis éditez n\'importe quelle propriété comme la couleur de la ligne, la couleur de la forme ou la transparence via l**\'onglet Vue** (qui se trouve en bas de la *Vue combinée*).

![](images/T101pwb02-01_appearance1.png )

Malheureusement, lorsque l\'objet est sélectionné, il est un peu difficile de voir à quoi il ressemblera après avoir ajusté sa nouvelle apparence. Pour voir le résultat final, il faut désélectionner l\'objet. Voici la nouvelle apparence du modèle, où l\'on peut maintenant voir le trou traversant également en vue iso. Une autre façon de modifier l\'apparence est via le **Affichage → ![](images/)_Apparence...**.

![](images/T101pwb02-02_appearance2.png )

## Une autre façon de repérer le trou 

Faites un *enregistrer sous* sous un nouveau nom. Supprimez ensuite la coupe qui a ajouté le trou et remettez le cylindre en position zéro. Votre modèle devrait ressembler à l\'image ci-dessous, qui est le point de départ pour utiliser une technique différente pour localiser le trou au centre de la face supérieure. Notez que la couleur est revenue au gris par défaut, le changement d\'apparence que nous avons fait était sur l\'objet coupé qui est maintenant supprimé.

![](images/T101pwb03-01_cyl.png )

Cette fois, l\'<img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> **[atelier Draft](Draft_Workbench/fr.md)** sera utilisé pour localiser le trou. Comme précédemment, le trou doit être situé au centre de la face supérieure, qui est le même que le point médian de la diagonale de la face supérieure. Commencez par basculer l\'atelier à **Draft**, il se peut qu\'une *grille* apparaisse dans la vue 3D, la visibilité de la grille peut être modifiée avec <img alt="" src=images/Draft_ToggleGrid.svg  style="width   *24px;"> [Basculer la grille](Draft_ToggleGrid/fr.md) dans la barre d\'outils. Lorsque vous utilisez la fonctionnalité **[aimantation](Draft_Snap/fr.md)** dans l**\'atelier Draft**, il est utile de n\'activer que les *types d\'aimantation* qui vous intéressent. Cette fois-ci, il suffit de laisser *point d\'extrémité, point milieu et centre du cercle activés*, ainsi les paramètres d\'aimantation devraient ressembler à ce qui suit.

![](images/T101pwb03-02_snap.png )

Trouver le point où placer le centre du cylindre pourrait être fait en créant une diagonale comme ligne d\'assistance et en utilisant le centre du cylindre et le point médian de la diagonale pour identifier les points entre lesquels se déplacer, cependant il s\'avère que nous n\'avons même pas besoin de créer des lignes d\'assistance, nous pouvons nous accrocher à une géométrie solide déjà existante.

Sélectionnez le **Cylindre** dans la vue en arborescence (il devient vert dans la vue 3D) et cliquez sur le bouton <img alt="" src=images/Draft_Move.svg  style="width   *24px;"> **[Déplacer](Draft_Move/fr.md)** dans la barre d\'outils. Un *panneau de tâches* s\'ouvre pour déplacer les objets, assurez-vous que *Copier* n\'est pas coché.

![](images/T101pwb03-03_move.png )

Déplacez ensuite la souris sur la face supérieure du cylindre de manière à voir un \"point blanc\" au centre du cercle, comme sur l\'image de gauche ci-dessous. Ce point, associé au symbole de centre situé à côté du pointeur de la souris, signifie qu\'un clic gauche de la souris se fera sur le point blanc.

![](images/T101pwb03-04_snapselect.png )

Lorsque vous avez le point blanc sur la face supérieure, cliquez sur le bouton gauche de la souris, et répétez l\'opération pour la face supérieure carrée du solide principal, comme l\'image de droite ci-dessus, et confirmez le choix par un clic sur le bouton gauche de la souris. La fonction d\'aimantation utilise le *centre de masse* pour tout type de face, et dans ce cas le centre de masse est le même que le centre géométrique recherché. Vous aurez maintenant remarqué que le déplacement du cylindre est animé, de sorte que vous voyez toujours ce qui va se passer.

En répétant l\'étape de la **soustraction booléenne** de tout à l\'heure, on obtient le trou traversant qui complète le modèle. À l\'aide de l**\'outil de mesure linéaire** de l\'atelier Part, on vérifie que le trou est correctement placé. La mesure ne peut être effectuée qu\'entre des *points*, la mesure est donc effectuée du point zéro du corps principal au point de jonction du cylindre, ce qui signifie que la distance correcte est de 70 mm au lieu des 65 mm indiqués sur le dessin pour tenir compte du rayon supplémentaire inclus dans la distance.

![](images/T101pwb03-05_modelmeasure.png )

## Faire du trou un trou fraisé 

Revenez à l\'[atelier Part](Part_Workbench/fr.md) et créez un *cône* en cliquant sur le bouton <img alt="" src=images/Part_Cone.svg  style="width   *24px;"> **[Cône](Part_Cone/fr.md)** dans la barre d\'outils. Changez *radius1* à 0 mm et *radius2* à 7 mm - cela donnera un *fraisage* de 2 mm sur le rayon. En fixant la \"hauteur\" du cône à 7 mm, on obtient un angle supérieur du cône de 90 degrés, ou un angle de fraisage de 45 degrés. Il convient de noter qu\'une fois encore, on pourrait tout aussi bien utiliser le <img alt="" src=images/Part_Chamfer.svg  style="width   *24px;"> [Chanfrein](Part_Chamfer/fr.md).

Lorsque vous travaillez avec FreeCAD, vous êtes continuellement confronté à plusieurs façons différentes d\'obtenir apparemment le même résultat. Il n\'y a guère de vérité absolue sur la bonne façon d\'obtenir un résultat final particulier - cependant, dans un contexte spécifique, un flux de travail particulier peut être plus flexible, permettre l\'utilisation de fonctionnalités ultérieures, etc. La façon dont vous construisez des modèles 3D évoluera avec le temps, au fur et à mesure que vous apprendrez à connaître les fonctionnalités et les capacités de FreeCAD.

![](images/T101pwb04-01_cone.png )

Translater le cône de façon à ce qu\'il soit \"concentrique\" au trou et \"coplanaire\" à la surface supérieure du solide principal. Utilisez n\'importe quelle méthode décrite précédemment dans ce tutoriel pour y parvenir. Dans l\'image ci-dessous, le déplacement est effectué avec *Transform* et un paramètre *increment* de 1 mm, car le cône a une dimension spécifique de 7 mm, ce qui signifie que le précédent paramètre d\'incrément de 5 mm ne permettra pas un positionnement correct. Le rendu <img alt="" src=images/Std_DrawStyleWireFrame.svg  style="width   *24px;"> **[filaire](Std_DrawStyle/fr#Filaire.md)** est utilisé pour voir facilement que le cône est dans la bonne position.

![](images/T101pwb04-02_conetranslate.png )

Pour terminer le modèle, utilisons la commande <img alt="" src=images/Part_Boolean.svg  style="width   *24px;"> **[Opération booléenne](Part_Boolean/fr.md)** au lieu de sélectionner d\'abord les objets et d\'appliquer une opération booléenne spécifique. Appuyez sur le bouton de la barre d\'outils et un *panneau de tâches* s\'ouvre comme dans l\'image ci-dessous à gauche.

![](images/T101pwb04-03_boolean.png )

Trois éléments doivent être spécifiés, le *type d\'opération*, la *première forme* et la *seconde forme*. Le cône est censé être soustrait, c\'est ce qu\'on appelle *Différence* dans cette commande, au lieu de *Soustraction*. La première forme est notre **Cut001**, elle est listée dans la catégorie *Composés*, puisqu\'elle est construite à partir de plusieurs solides. La deuxième forme est le **Cône**. Une fois les réglages corrects effectués pour la commande, cliquez sur le bouton **Appliquer** pour exécuter l\'opération. Tout cela a été fait dans l\'image de droite, et là on peut aussi voir qu\'un *composé* **Cut002** est maintenant apparu, c\'est la forme finale de notre modèle. Après avoir modifié l\'apparence, le modèle terminé ressemble à ceci.

![](images/T101pwb04-04_modelcomplete.png )

## Faire une pièce creuse 

Faites un *enregistrer sous* sous un nouveau nom. FreeCAD possède toutes les opérations typiques d\'un modeleur 3D, l\'une d\'entre elles est <img alt="" src=images/Part_Thickness.svg  style="width   *24px;"> **[Coque](Part_Thickness/fr.md)**, qui est utilisée pour *évider* les pièces.

Faites pivoter la vue de manière à ce que la face inférieure du modèle soit visible.

![](images/T101pwb05-01_frombottom.png )

Sélectionnez la *face inférieure* du modèle, puis dans l\'[Atelier Part](Part_Workbench/fr.md) sélectionnez <img alt="" src=images/Part_Thickness.svg  style="width   *24px;"> **[Coque](Part_Thickness/fr.md)** et l\'écran devrait ressembler à celui ci-dessous.

![](images/T101pwb05-02_thickness_cmd.png )

Cliquez sur **OK**, comme vous pouvez le voir, il y a maintenant un *rayon* sur la partie évidée.

![](images/T101pwb05-03_thickness_dimension.png )

De plus, en prenant la mesure de la largeur de la pièce, celle-ci est maintenant de 32 mm, donc la *coque* a été appliquée *vers l\'extérieur*. Modifions cela, double-cliquez sur le modèle dans l\'arborescence et modifiez les paramètres du *type de raccordement* en *intersection* et le paramètre *coque* en -1.

![](images/T101pwb05-04_thickness_modify.png )

La largeur extérieure de la pièce est maintenant de 30 mm, comme avant, et les coins sont tous anguleux.

![](images/T101pwb05-05_thickness_modified.png )

## Une autre façon de positionner le chanfrein 

Faites un *enregistrer sous* sous un nouveau nom. Ensuite, supprimez des caractéristiques pour que le modèle ressemble à celui ci-dessous.

![](images/T101pwb06-01_startingpoint.png )

Faites un **Cube** de dimensions **30x30x60**, comme ci-dessous.

![](images/T101pwb06-02_with_cube.png )

Modifiez **placement** en effectuant d\'abord une rotation de -120 degrés autour de l\'axe des Y.

![](images/T101pwb06-03_rotated_cube.png )

Enfin, modifiez la position en **X=50** et **Z=50** et effectuez la *soustraction* pour obtenir le même résultat que précédemment.

![](images/T101pwb06-04_cube_cut.png )

Cela montre une fois de plus qu\'il y a toujours plusieurs façons de produire le même résultat, ce qui est un thème récurrent en matière de modélisation 3D. Lorsqu\'il s\'agit de géométries de base ou de solides, on peut utiliser différents ateliers dans FreeCAD ainsi que différentes commandes et toujours obtenir la même forme extérieure d\'un solide. Vous devez simplement trouver votre propre manière vers un ensemble d\'outils préférés et un flux de travail avec lequel vous êtes à l\'aise. La modélisation en 3D paramétrique est un processus d\'apprentissage constant, et il faut de la pratique pour le maîtriser.

## Modification des dimensions, couleurs de la face et TNP 

FreeCAD est un modeleur 3D paramétrique, ce qui vous permet de changer n\'importe quel *placement* ou *dimension* et le modèle sera mis à jour en conséquence. En général, cela fonctionne, mais il est possible de casser un modèle lors de l\'édition - par exemple lorsqu\'un congé est basé sur une arête qui n\'existe plus à cause d\'une modification. Lorsqu\'un modèle se casse pendant la modification, on parle de **TNP, Topological Naming Problem**, en français Problème de dénomination topologique.

Allez-y et expérimentez en changeant les dimensions et les placements pour voir si vous pouvez casser le modèle, n\'oubliez pas de recalculer le modèle après les changements si nécessaire. Cela peut être fait avec le bouton <img alt="" src=images/Std_Refresh.svg  style="width   *24px;"> [Rafraîchir](Std_Refresh/fr.md) dans la barre d\'outils, si l\'icône est grisée, il n\'est pas nécessaire de rafraîchir l\'objet.

### Repositionner le cylindre 

Voici un exemple de cylindre déplacé du centre vers un côté du corps principal en utilisant *Transform* sur le cylindre. Comme on peut le voir sur l\'image, le cône est toujours dans sa position originale, non affecté par le déplacement du cylindre.

![](images/T101pwb07-01_cylindermoved.png )

Lorsque vous déplacez le cylindre et que vous percez la surface extérieure, dans la version 0.19 vous perdez une partie des paramètres de couleur de votre modèle. FreeCAD revient aux paramètres par défaut de l\'utilisateur pour les couleurs et la transparence des formes dans la vue 3D, cependant la forme **Cut002** montre toujours les couleurs et la transparence qu\'elle avait auparavant comme on le voit dans l\'image ci-dessous.

### Réparer les couleurs 

![](images/T101pwb07-02_wrongcolor.png )

Voici un moyen de les récupérer. Changez d\'abord *transparency* d\'un cran vers le haut ou vers le bas, puis revenez en arrière, cela ramène la transparence. Vous pouvez faire la même chose avec *shape color*. Une autre façon de récupérer la couleur est de faire un *clic droit* sur **Cut002** dans l\'arborescence et de sélectionner **Définir les couleurs** dans le menu contextuel. Dans le *panneau de tâches* qui s\'affiche, cliquez sur **Définir par défaut**, ce qui ramène la couleur à celle définie dans les propriétés de la vue.

![](images/T101pwb07-03_set_colors.png )

La commande **Définir les couleurs** vous permet de sélectionner des faces une par une d\'une forme et de définir une couleur unique pour les faces sélectionnées.

### Plusieurs solides 

Un autre exemple où le cube qui fait le chanfrein a été translaté et tourné.

![](images/T101pwb07-04_3solids.png )

Comme on peut le voir en repositionnant le chanfrein de cette manière, le résultat final est *3 solides disjoints*. L\'[atelier Part](Part_Workbench/fr.md) permet cela, l\'[atelier PartDesign](PartDesign_Workbench/fr.md) ne le permet pas, soit vous obtiendrez une *erreur de solides multiples*, soit il ne rendra tout simplement pas tous les solides.

### TNP

En revenant au modèle original complété, explorons comment les faces sont nommées. Ici, la **[fenêtre de sélection](Selection_view/fr.md)** a été rendue active, juste pour montrer clairement ce qui est sélectionné et ce qui ne l\'est pas, la coloration est également ajustée pour que la sélection soit plus facile à voir.

![](images/T101pwb07-05_face2and9.png )

En sélectionnant une face latérale et la face intérieure du cylindre, on voit qu\'elles sont appelées face *2* et *9*, où face *2* est la face latérale. La numérotation des faces peut être différente pour vous. En déplaçant le cylindre de façon à ce que la cavité se retrouve sur la face latérale, et en effectuant la sélection des faces, on obtient un numéro différent pour la face cylindrique.

![](images/T101pwb07-06_newfacenumbers.png )

La face 2 est le côté droit de la face 2 originale, le côté gauche de l\'ancienne face 2 est maintenant la face 8. La partie cylindrique était la face 9, elle est maintenant la face 7. FreeCAD réassigne la numérotation et l\'ordre n\'est pas nécessairement préservé. Le nombre total de faces dans le premier modèle est de 10, dans la version avec la face cylindrique perçant la face latérale, le nombre total de faces est de 11. Il est donc évident que la numérotation des faces doit changer lorsque la *topologie* change. Cela peut sembler un détail minuscule, mais il s\'avère être très important dans la CAO 3D paramétrique. Imaginez que vous ayez utilisé la face cylindrique comme référence pour un autre élément, qui s\'appelait auparavant face 9, mais qui s\'appelle maintenant face 8. La référence à la surface cylindrique prévue est perdue. Puisque FreeCAD, au moins dans les versions actuelles, ne garde pas la trace de la *face prévue* mais garde seulement la trace de la *face numérotée*, un modèle se casse lorsqu\'une référence est faite à une face qui est ensuite renumérotée. C\'est ce qu\'on appelle le **TNP, Topological Naming Problem**.

Vous êtes encouragés à apprendre comment éviter les modèles cassés à cause de TNP, des lectures supplémentaires peuvent être faites [ailleurs sur le wiki](Topological_naming_problem/fr.md), qui se concentre principalement sur un flux de travail *basé sur des esquisses*, le mécanisme sous-jacent est le même cependant. La renumérotation décrite ici pour les faces est valable pour toutes les entités géométriques, faces, arêtes et sommets.

## Organiser l\'arborescence un peu différemment 

Faites un *enregistrer sous* sous un nouveau nom. Puis supprimez toutes les soustractions pour obtenir un modèle ressemblant à celui ci-dessous.

![](images/T101pwb08-01_primitives.png )

Lorsque vous utilisez l**\'atelier Part** et que vous modélisez des solides avec de nombreuses fonctions, l\'arborescence d\'un solide peut devenir difficile à déchiffrer. Jusqu\'à présent, nous avons créé une primitive/fonction et appliqué une opération booléenne. Dans l\'atelier Part, il est possible de regrouper des primitives en une seule opération booléenne. Dans notre cas, nous avons le cylindre, le cône et le cube qui sont tous une opération booléenne de soustraction. Au lieu de faire une soustraction pour chaque primitive, nous pouvons d\'abord appliquer une union booléenne, <img alt="" src=images/Part_Fuse.svg  style="width   *24px;"> **[Unir](Part_Fuse/fr.md)** les primitives destinées à la soustraction booléenne, puis faire la *soustraction* entre le **congé** et l**\'union**.

En utilisant cette approche, la vue en arborescence finit par ressembler à ce qui suit, qui est simplement une façon différente de construire le même modèle. Comparez cela avec la vue arborescente originale, aucune n\'est meilleure que l\'autre, mais lors de la création de modèles plus complexes, une approche plutôt qu\'une autre peut présenter des avantages en termes de facilité de modification/réorganisation du modèle si nécessaire.

![](images/T101pwb08-02_fused.png )

## Enveloppe

Après avoir parcouru ce tutoriel, vous êtes maintenant brièvement familiarisé avec l\'interface utilisateur de FreeCAD et vous avez appris les bases de l\'utilisation de l**\'atelier Part**. Vous devriez maintenant être capable de construire des modèles simples à votre goût. L**\'atelier Part** est l\'un des ateliers qui peut être utilisé pour créer des solides, L**\'atelier PartDesign** en est un autre. Les différents ateliers ont des capacités et des flux de travail différents. L\'apprentissage complet de FreeCAD, en particulier en tenant compte de tous les add-ons et macros, prend des années, alors continuez à explorer de nouvelles et différentes façons de créer des modèles - suivez les différents tutoriels sur le wiki, l\'apprentissage ne s\'arrête jamais lorsque vous travaillez avec FreeCAD. Il est suggéré que vous appreniez les *esquisses* et l**\'atelier PartDesign** puis que vous vous concentriez sur la création de solides. Si votre objectif est de modéliser des bâtiments, votre prochain apprentissage devrait être les ateliers **Draft** et **Arch**.

Enfin, FreeCAD est réalisé par des volontaires pendant leur temps libre. Si vous voulez faire progresser les possibilités de FreeCAD, pensez à [contribuer](Help_FreeCAD/fr.md) à FreeCAD, par exemple en améliorant la documentation.

[Category   *Part](Category_Part.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Category_Part.md) > Creating a simple part with Part WB/fr
