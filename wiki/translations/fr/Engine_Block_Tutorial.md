# Engine Block Tutorial/fr

 } {{TutorialInfo/fr
|Topic=  Atelier Part
|Level=  Débutant
|Time=   1 heure
|Author= Andrewbuck40
|FCVersion= 0.14.3700
|Files=
}}

<img alt="" src=images/Engine_Block_Tutorial_-_Finished_Engine_Block.png  style="width:600px;">

Voici un tutoriel d\'introduction à la modélisation dans FreeCAD. Les objectifs de ce tutoriel sont de vous présenter les types de données primitives pour les objets paramétriques, les opérations booléennes, le dessin 2D, et le processus de conversion dessins 2D en objets 3D. Comme exemple de travail nous prendrons la modélisation d\'un simple bloc moteur et carter, visible ci-dessus.

## Démarrage

Pour commencer, ouvrez FreeCAD , aller à **Fichier → Nouveau** pour créer un nouveau document, puis **Fichier → Enregistrer** pour sauvegarder quelque part sur votre ordinateur, j\'ai nommé le projet **\"Moteur\"**. Vous remarquerez que lorsque vous enregistrez le projet, l*\'arborescence* sur le côté gauche de l\'écran affiche le nom du projet sur lequel vous travaillez. Vous pouvez avoir plus d\'un projet ouvert à la fois et chaque projet sera présenté comme la racine d\'un arbre dans l\'arborescence.

## Dégrossissage du bloc 

Maintenant, commençons à travailler sur le modèle réel. Nous allons commencer par l\'ajout d\'une boîte pour le contour global du bloc moteur. Pour cela, nous devons ajouter une *pièce* au modèle à faire, allez dans **Affichage → Atelier → Part** pour sélectionner l\'[atelier Part](Part_Workbench/fr.md). Vous remarquerez que lorsque vous sélectionnez l\'atelier, vous obtenez un jeu de boutons différent sur la barre d\'outils en haut. Voyagez dans d\'autres ateliers pour vous familiariser avec le système d\'ateliers et revenez ensuite à l\'atelier Part (pièce).

### Le bloc cylindre 

Dans l\'atelier Part, vous verrez une diversité de boutons pour les objets primitifs comme boîte, sphère, cône, etc. Cliquez sur le bouton du cube (<img alt="" src=images/Part_Box.svg  style="width:16px;">) pour ajouter un cube à la scène. Chacune des primitives énumérées a un jeu de paramètres par défaut qui s\'établissent lorsque la primitive est ajoutée. Si vous le voulez, vous pouvez tester l\'ajout de chacune des primitives pour voir à quoi elles ressemblent. Les primitives peuvent être retirées de la scène en les sélectionnant et en appuyant sur la touche Suppr. Il y a deux façons de sélectionner des objets, vous pouvez faire un clic gauche sur eux dans la vue 3D, ou faire un clic gauche sur eux dans l\'arborescence. Avec la méthode de maintenir **Ctrl** enfoncé, vous pouvez sélectionner plusieurs éléments. Vous pouvez zoomer la vue 3D avec la molette de défilement de votre souris. Pour déplacer la vue, clic du milieu et faites glisser. Pour faire pivoter la vue que vous cliquez, maintenez le bouton central de la souris enfoncé ainsi que le bouton droit, puis faire glisser la souris pour faire pivoter la vue. Vous pouvez également faire un simple clic du milieu sur une partie de votre objet 3D pour faire pivoter la vue autour de ce point dans l\'espace 3D. En outre, les numéros 1 à 6 et le nombre 0 sur le pavé numérique vous montrer différentes vues de la scène (en haut, à gauche, axonométrique, etc). Prenez une minute ou deux à vous familiariser avec la manipulation de la vue 3D.

:   *Pour en savoir plus : [Navigation dans l\'espace 3D](Mouse_navigation/fr.md)*

Dès que vous avez votre cube et êtes à l\'aise avec le fonctionnement de la souris, nous allons commencer le paramétrage des dimensions du modèle CAO. Sélectionnez le *Cube* en cliquant dessus dans l\'arborescence, puis cliquez sur l\' *onglet Données* de la *Vue Propriété* situé en dessous de l\'arborescence (aller à **Affichage → Panels → Vue Combo** si vous l\'avez fermé). Dans l*\'onglet Données*, vous pouvez modifier les propriétés de l\'objet que vous avez sélectionné dans l\'arborescence. Selon le type d\'objet sélectionné, il y aura différents paramètres que vous pourrez ajuster dans l\' *onglet Données*. Pour une boîte nous avons besoin de trois facteurs, l\'un pour sa position dans l\'espace 3D, un autre pour son orientation, et un troisième pour spécifier les dimensions de la boîte. Pour une sphère vous seriez en mesure de préciser le point central et le rayon ; les cônes ont un rayon, une hauteur et une position ; et ainsi de suite. Nous construisons un petit bloc moteur 2 cylindres afin de définir la taille et la position de la boîte pour les valeurs suivantes (Assurez-vous de définir le XYZ sous « Position », ceux sous « Axis » détermine l\'axe de rotation et les valeurs par défaut sont celles que nous voulons) :

:   {\| Class = wikitable border = 1

\|- \| X : 0,0 mm \|\| Longueur: 140,0 mm \|- \| Y : -40,0 mm \|\| Largeur: 80,0 mm \|- \| Z : 0,0 mm \|\| Hauteur: 110,0 mm \|- \|}

Maintenant que vous avez votre bloc moteur dimensionné correctement, nous devrions lui donner un nom plus descriptif. Sélectionnez-le dans l\'arborescence et cliquer droit de renommer ou appuyez sur la touche **F2** sur votre clavier. Nommez cette partie **Bloc cylindres**.

### Le premier cylindre 

Étape suivante, nous allons tailler le premier cylindre à travers le bloc moteur. Pour ce faire, nous allons ajouter un cylindre au modèle avec la profondeur que nous voulons aléser et ensuite faire une opération booléenne de *soustraction* de la matière du bloc. Cliquez sur le bouton ajouter cylindre (<img alt="" src=images/Part_Cylinder.svg  style="width:16px;">) pour créer un nouveau cylindre, puis sélectionnez-le dans l\'arborescence et définissez ses propriétés comme suit :

:   {\| class=wikitable border=1

\|- \| X : 40.0 mm \|\| Hauteur: 110.0 mm \|- \| Y : 0.0 mm \|\| Rayon: 25.0 mm \|- \| Z : 0.0 mm \|\| \|- \|}

Une fois les propriétés définies correctement, vous devriez voir les extrémités circulaires du cylindre sur les faces supérieure et inférieure du bloc moteur. Nommez cet objet *\' Cylindre 1*\' en le sélectionnant dans l\'arborescence.

### Le deuxième cylindre 

On pourrait faire le deuxième cylindre de la même manière que nous avons fait le premier, mais il serait beaucoup plus facile de copier le travail existant sachant que la seule différence entre les deux est leur coordonnée X. Pour ce faire, sélectionnez **Cylindre 1** dans l\'arborescence, puis aller à **Édition → Dupliquer la Sélection**. Vous verrez le nouveau cylindre apparaitre dans l\'arborescence (nommer le **Cylindre 2** tout de suite), mais vous ne le verrez pas dans la vue 3D comme il est dans le même endroit que le premier cylindre. Maintenant, sélectionnez **Cylindre 2** dans l\'arborescence, puis changer la coordonnée X = 100 mm. Notez que lorsque vous mettez à jour les chiffres dans le champ de données, vous devriez voir le cylindre se déplacer dans la vue 3D. Une fois que le deuxième cylindre est correctement positionné, vous pouvez voir à quoi ils ressemblent en sélectionnant le **Bloc cylindres** dans l\'arborescence puis en appuyant sur **Espace** pour le cacher (notez que les objets cachés sont grisés dans l\'arborescence). Cachez les trois objets un par un, puis montrer les tous à nouveau.

### Alésage des cylindres 

<img alt="" src=images/_Engine_Block_Tutorial_-_Bored_Block.png  style="width:300px;">

Maintenant que les deux cylindres sont en place, nous voulons les utiliser pour aléser le bloc aux dimensions appropriées. Pour cela, nous allons utiliser les \'\' opérations booléennes \'\' sur nos trois primitives. Nous allons commencer par faire une *union* sur deux cylindres afin que nous puissions les soustraire en tant que groupe à partir du bloc. Sélectionnez **Cylindre 1** dans l\'arborescence, puis ***CTRL** + LeftClick* pour sélectionner **Cylindre 2**. Maintenant, appuyez sur le bouton *Union* (<img alt="" src=images/Part_Fuse.svg  style="width:16px;">) pour fusionner les objets ensemble. Vous remarquerez que, dans l\'arborescence, il y a maintenant un nouvel objet appelé *Fusion*. Si vous cliquez sur la flèche déroulante à côté de *Fusion*, vous verrez les deux cylindres mais ils seront grisés. Au lieu de *Fusion*, renommer le **Cylindres** de sorte qu\'il sera plus facile à trouver plus tard. Maintenant nous allons aléser le bloc moteur. Sélectionnez le **Bloc cylindres** et *ensuite* avec \'\' CTRL + LeftClick \'\' sélectionner **Cylindres** et appuyez sur le bouton Make Cut (<img alt="" src=images/Part_Cut.svg  style="width:16px;">). Les deux objets sélectionnés seront de nouveau réunis comme ils l\'étaient pour l\'union et l\'objet résultant unique sera nommé \'\' Cut \'\' (que vous devez renommer **Bloc alésé**). Appuyez sur le \'\' 2 \'\' du pavé numérique et vous devriez maintenant pouvoir regarder vers le bas à travers les cylindres de l\'autre côté du bloc moteur, puis \'\' MiddleClick + RightClick + Drag \'\' pour regarder votre bloc moteur. A droite, vous voyez ce à quoi le produit fini devrait ressembler, j\'ai développé l\'arborescence sur la gauche pour montrer les primitives individuelles et j\'ai choisi **Cylindre 2** pour examiner l\'onglet \'\' données \'\' de la *Vue Propriétés*.

### Principal avantage de la Modélisation Paramétrique 

Maintenant que nous avons alésé nos cylindres nous allons prendre une seconde pour voir l\'un des avantages de ce système. Supposons qu\'à un certain moment dans le développement, nous découvrons que nous voulons que les cylindres soient un peu plus grands. Puisque les opérations de réunion et d\'intersection que nous avons effectuées ont été enregistrées comme des regroupements dans l\'arborescence, nous pouvons changer la taille du cylindre et FreeCAD va tout simplement ré-exécuter le processus d\'union et d\'intersection et arriver à la nouvelle taille du moteur. Jouez avec le rayon et la position des deux cylindres un peu et puis retournez aux paramètres cités ci-dessus, avant de poursuivre le tutoriel.

## Le carter 

### Bloc et chapeaux de paliers 

Ensuite, nous allons fabriquer un carter sous le bloc moteur. Ajouter une nouvelle boîte, renommez la en **Bloc carter**, et donner lui les propriétés suivantes :

:   {\| class=wikitable border=1

\|- \| X: 0.0 mm \|\| Hauteur: 140.0 mm \|- \| Y: -50.0 mm \|\| Longueur: 100.0 mm \|- \| Z: -85.0 mm \|\| Largeur: 85.0 mm \|- \|}

Pour faire apparaître le carter donnons lui une couleur différente. Vous pouvez changer la couleur par un clic droit sur l\'objet à modifier dans l\'arborescence. Vous pouvez assigner une couleur vous-même ou donner à l\'objet une couleur aléatoire (choisissez aléatoire à nouveau si vous n\'aimez pas la couleur).

Ajoutez une autre boite appelée **Découpe palier**, donner lui les propriétés suivantes, puis couper **Découpe palier** du **Bloc carter** (c\'est à dire en sélectionnant le carter en premier) :

:   {\| class=wikitable border=1

\|- \| X: 0.0 mm \|\| Hauteur (height): 140.0 mm \|- \| Y: -40.0 mm \|\| Longueur (lenght): 80.0 mm \|- \| Z: -85.0 mm \|\| Largeur (widht): 30.0 mm \|- \|}

Renommez l\'objet résultat \'\' Cut \'\' en **Carter creusé**.

### Tailler les paliers 

Ensuite, nous allons découper un emplacement semi-circulaire pour poser le vilebrequin et un espace dans le carter pour qu\'il tourne. Nous commencerons par un cylindre, mais l\'orientation du cylindre par défaut est verticale, alors que nous avons besoin d\'une horizontale. Cela signifie que nous devons trouver une façon de tourner le cylindre pour l\'aligner correctement avec notre moteur. Si vous regardez l\'axe de guidage dans le coin inférieur droit de la fenêtre 3D, vous verrez que nous voulons que le vilebrequin se situe le long de l\'axe des x positifs. Cela signifie qu\'à partir de sa position de départ nous avons besoin de faire tourner de 90 degrés autour d\'un axe parallèle à l\'axe Y de la scène. Cela nous indique ce que nous devons saisir comme paramètres pour le cylindre. Créer un cylindre appelé **Découpe vilebrequin** et lui donner ces propriétés (notez que nous avons maintenant à spécifier les paramètres d\'orientation, ainsi que les dimensions régulières comme nous avons fait pour les alésages du cylindre) :

:   {\| class=wikitable border=1

\|- \| Axe X: 0.0 mm \|\| Angle: 90.0 degrés \|- \| Axe Y: 1.0 mm \|\| \|- \| Axe Z: 0.0 mm \|\| \|- \| Position X: 0.0 mm \|\| Hauteur: 140.0 mm \|- \| Position Y: 0.0 mm \|\| Radius: 20.0 mm \|- \| Position Z: -55.0 mm \|\| \|- \|}

Couper l\'objet **Découpe vilebrequin** depuis **Carter creusé** et renommer l\'objet résultant **Carter avec paliers**.

### Finition du carter 

Enfin, nous allons découper deux boîtes finales de sorte que les tiges de piston puissent atteindre le carter vers le haut dans le bloc moteur. Faire deux objets appelés **Box sculpte 1** et **Box sculpte 2** avec les propriétés suivantes ; vous pouvez aussi dupliquer **Box sculpte 1** et juste changer la coordonnée X pour obtenir la deuxième découpe. Faire une union dont le résultat sera un objet appelé **Box sculpture carter**, et avec cet objet creuser **Carter avec paliers**, appeler le résultat final **Carter**. N\'oubliez pas, vous pouvez masquer l\'objet **Bloc alésé** en le sélectionnant et en appuyant la barre d\'espace pour pouvoir voir ce que vous faites.

:   {\| class=wikitable border=1

\|- \| X: 15.0 mm \|\| Longueur: 50 mm \|- \| Y: -25.0 mm \|\| Largeur: 50.0 mm \|- \| Z: -55.0 mm \|\| Hauteur: 55.0 mm \|- \|}

:   {\| class=wikitable border=1

\|- \| X: 75.0 mm \|\| Longueur: 50.0 mm \|- \| Y: -25.0 mm \|\| Largeur: 50.0 mm \|- \| Z: -55.0 mm \|\|Hauteur: 55.0 mm \|- \|}

<img alt="" src=images/_Engine_Block_Tutorial_-_Crankcase.png  style="width:300px;">

Sur la droite, vous pouvez voir ce que devrait être le résultat final. J\'ai pleinement développé l\'arborescence de sorte que vous puissiez voir la hiérarchie des opérations booléennes utilisées pour construire le dispositif. N\'oubliez pas que vous pouvez toujours creuser dans cet arbre et modifier le diamètre des cylindres, changer la taille ou la position du vilebrequin, etc. sans avoir à reconstruire l\'ensemble du modèle à partir de zéro. Nous pourrions continuer à tailler le carter plus loin, mais ce sera assez pour le moment. Pour la suite nous allons regarder comment utiliser le mode de dessin 2D pour réaliser l\'implantation des boulons de culasse et réduire le poids du bloc moteur en supprimant une grande partie restante inutile du carter autour des cylindres.

## Modélisation 2D du dessin du joint de culasse 

Pour les goujons de culasse et la forme du bloc moteur, nous utiliserons de nombreuses opérations booléennes pour *tailler* les parties du bloc que nous ne voulons pas conserver. Toutefois, si nous nous posons pour réfléchir à cela, chaque goujon de culasse va regarder la même chose, il sera coupé tout en bas dans le carter, la seule différence sera où se trouve la tête sur le dessus. Cela signifie que nous pouvons tout simplement *dessiner* la forme du joint de culasse sur le dessus du moteur, et ensuite l\'utiliser comme un modèle pour faire la découpe que nous voulons.

### Entrée dans le mode élaboration 2D (Draft) 

Nous devons d'abord passer par l\'atelier de dessin 2D. Pour ce faire, vous pouvez sélectionner *Draft* dans la liste déroulante située en haut de la fenêtre, qui indique actuellement *Part*. Si vous ne trouvez pas le menu déroulant (tous les ateliers ne s\'affichent pas dans le menu déroulant), vous pouvez également sélectionner un atelier à partir de l\'entrée de menu **Affichage → Atelier**. Même si nous faisons du dessin 2D, nous allons dessiner dans la fenêtre 3D en disant à FreeCAD dans quel plan nous voulons que les dessins se projettent. Après avoir sélectionné l\'atelier de dessin Draft, cliquez sur le bouton en haut à gauche qui proposera l\'un des éléments suivants {none, top, front, size, ou d(\..., \..., \...)}. Une fois que vous cliquez sur l\'un d\'eux, le côté gauche de la barre contient une zone de texte dans laquelle vous pouvez entrer un décalage de plan et 5 boutons : XY, XZ, YZ, View et Aucun. Les trois premiers sont les vues standard, supérieure, avant et latérale, l\'entrée View utilise le plan perpendiculaire à la direction de visée de la caméra (le plan de la caméra), et la dernière ne fait pas saillie dans un plan et vous permet de définir complètement le Coordonnées XYZ pour chaque point dessiné. Nous voulons définir un décalage de plan de 110 (tapez-le et appuyez sur Entrée), puis cliquez sur le bouton XY pour projeter le dessin sur le plan XY, situé à 110 mm de l\'axe Z qui correspond au haut du bloc moteur. Maintenant que nous avons indiqué à FreeCAD dans quel plan dessiner, nous sommes prêts à commencer à concevoir le joint de culasse.

La dernière chose à faire est de configurer la vue 3D. Même si tous les dessins que nous produisons seront projetés dans notre plan 2D défini, nous pouvons regarder le plan que nous avons dessiné depuis n\'importe quel angle (y compris sur l\'autre face du plan, pour avoir le dessin « symétrique »). Depuis que nous avons défini que ce plan est coplanaire au sommet du bloc moteur, nous devrions probablement avoir la vue 3D regardant cela, ou au moins à peu près dans cette direction. Appuyez sur la touche 2 sur le pavé numérique pour regarder la vue de dessus (remarquez que sur le pavé numérique, les touches adjacentes sont les vues opposées de cette manière 1 et 4 sont devant-derrière, 2 et 5 sont dessus-dessous, et 3 et 6 sont gauche-droite). Quand vous regardez le moteur du haut vers le bas, vous pouvez centrer cela en faisant glisser avec le bouton du milieu de la souris pour déplacer la vue. Enfin, le mode Draft nous permettra de verrouiller les parties du dessin aux coins du bloc moteur, au centre des cylindres, etc, afin de mieux faire ce travail nous devrions cacher le carter, ainsi les dessins se verrouilleront seulement sur la partie sur laquelle nous travaillons (barre d\'espace pour afficher/masquer l\'objet sélectionné).

### Disposition des goujons de culasse 

Maintenant que la projection du bon plan et de la vue sont définis, nous ajoutons les éléments de dessin 2D de la même manière que nous avons ajouté les primitives. Cliquez sur le bouton *Ajouter cercle* (<img alt="" src=images/Draft_Circle.svg  style="width:16px;">) et déplacez votre souris dans la vue 3D. Vous devez ensuite indiquez à FreeCAD l\'emplacement XY pour le centre du cercle, et le rayon, pour ces deux mesures vous pouvez les entrer avec la souris (en suivant les instructions dans la barre d\'état en bas à gauche), ou vous pouvez taper les valeurs dans les zones de saisie de texte qui apparaissent au-dessus de la vue d\'arborescence. Allez-y et ajoutez quelques cercles aléatoires sur le dessus du moteur, ainsi que quelques-uns un peu dans l\'espace vide qui entoure votre vue du moteur. Après avoir fait cela, faites pivoter la caméra autour du sommet du bloc moteur et regardez les cercles que vous avez tracés, remarquez comme ils sont *à plat* dans le plan où nous les projetons et comme ce plan s\'aligne avec le sommet du bloc moteur ; ce sera important lorsque nous extruderons le dessin pour façonner le moteur. Maintenant que vous avez vu comment ajouter des éléments 2D vous pouvez supprimer les cercles de test que vous avez ajoutés et nous allons commencer à saisir la disposition de la tête. Notez que si votre cercle disparaît à l\'intérieur du bloc moteur, votre plan de projection de dessin n\'est pas correctement aligné sur le référentiel XY décalé de 110 mm.

L\'ajout des éléments avec la souris est rapide et facile, mais il n\'est pas très précis. Pour le motif de boulon réel, nous utilisons le fait que le déplacement de la souris met à jour les nombres dans les zones de texte juste au-dessus de la vue 3D afin que nous puissions voir approximativement les coordonnées de l\'emplacement où nous voulons placer des éléments. Une fois que nous avons ces coordonnées approximatives, nous pouvons taper les valeurs réelles que nous voulons pour un positionnement précis. Réinitialisez la vue de dessus du moteur, cliquez sur le bouton *Ajouter cercle* et déplacez votre souris dans le coin supérieur gauche du bloc moteur en prenant un mauvais emplacement pour le goujon de culasse. Il semble que X=10, Y=30, soit un bon emplacement pour le cercle (notez que la coordonnée Z doit être grisée, si ce n\'est pas le cas, vous devrez définir le plan correctement comme dans la section précédente, en appuyant sur espace pour annuler le tracé du cercle).

Maintenant que vous avez vu la façon de déterminer facilement les coordonnées des éléments de dessin, vous pouvez facilement concevoir un modèle de goujon ou d\'autres implantations en deux dimensions pour des pièces telles que des canaux de fluide, des tracés de circuits imprimés, etc. Pour nos 3 goujons de culasse nous allons sur ce côté du moteur, nous allons utiliser les coordonnées suivantes. Notez que lorsque vous tapez les valeurs dans les zones vous pouvez appuyez sur Entrée pour passer à la case suivante, c\'est aussi une bonne idée de déplacer votre souris en dehors de la vue 3D avant de commencer à taper les coordonnées car les mouvements de la souris écraserons les chiffres que vous avez déjà saisis dans les champs de saisie de texte. En outre, sur mon système, j\'ai eu des difficultés avec les cercles saisis qui avaient leurs coordonnées Z fixées à 12,5 pour une raison inconnue, si vous rencontrez ce problème, vous pouvez définir le plan de projection du dessin sur \'\' Aucun \'\' puis entrer manuellement la coordonnée Z des cercles à 110. Enfin, lors de la création des cercles, assurez-vous de cocher la case \'\' Rempli \'\', sinon, quand nous les extrudons plus tard, ils créeront simplement des tubes comme un tube de papier toilette au lieu d'un cylindre solide.

  ---------- --------- ----------------
  X1 : 10    Y1 : 25   Rayon : 2,5 mm
  X2 : 70    Y2 : 25   Rayon : 2,5 mm
  X3 : 130   Y3 : 25   Rayon : 2,5 mm
  ---------- --------- ----------------

Nommez ces cercles **Boulon 1** à **Boulon 3**.

### L'autre côté du bloc 

Maintenant que les trois premiers goujons de culasse sont en place d'un côté du moteur, il nous en faut trois autres en miroir de l'autre côté. Il y a trois façons de le faire :

-   Nous pourrions simplement ajouter des cercles comme nous l'avons fait pour les trois premiers et inverser simplement les coordonnées Y pour placer les goujons de l'autre côté du moteur.
-   Nous pourrions sélectionner les trois que nous avons ajoutés, aller à **Édition → Dupliquer la sélection**, puis inverser les coordonnées Y des trois nouveaux cercles.
-   Nous pourrions utiliser la fonctionnalité Miroir dans l\'atelier Part.

Comme vous devez déjà savoir faire selon les première et deuxième méthodes, nous choisirons la troisième pour cet exemple. Chacune des trois méthodes a ses avantages et ses inconvénients, mais une bonne règle opératoire est que des modèles simples (comme celui-ci) devraient probablement utiliser la première ou la deuxième méthode, alors que des modèles avec de nombreuses duplications et/ou des duplications de formes/objets très complexes devraient probablement utiliser la troisième méthode.

Même si c\'est un peu exagéré, nous allons symétriser ces goujons à titre de démonstration. Revenez à l\'atelier Part (notez que vous pouvez toujours basculer vers l\'atelier *Complete* pour voir tous les outils en même temps si vous préférez ne pas faire des allées et venues (caduc depuis v0.17)) en accédant à **Affichage → Atelier**. Sélectionnez les trois cercles de boulons dans l\'arborescence, puis appuyez sur le bouton miroir (<img alt="" src=images/Part_Mirror.svg  style="width:16px;">). Une fois que vous avez appuyé sur le bouton miroir, vous devriez remarquer un nouvel affichage appelé *Vue combinée* sous le volet *Vue Arborescence*. De nombreux outils nécessitent une entrée supplémentaire avant de pouvoir être exécutés et la vue combinée vous permet d\'entrer ces paramètres. Vous pouvez agrandir la vue combinée en faisant glisser vers le haut ou le bas la ligne de séparation qui la sépare de la vue Propriétés. Sélectionnez **Boulon 1** dans la liste de la vue combinée et réglez le plan miroir sur XZ, puis appuyez sur OK (faire de même pour les boulons 2 et 3).

À ce stade, vous devriez avoir le bloc moteur de base avec les cylindres percés et les emplacements des goujons de culasse marqués.

### Enlever les excédents de matière dans le bloc 

Maintenant que nous avons les trous pour les goujons de culasse (nous pourrions faire la même chose pour les canaux d\'huile, les chemises d\'eau, etc.), nous voudrons \"couper\" l\'extérieur du bloc selon une forme plus appropriée. Cela rendra le moteur plus léger, lui permettra de mieux refroidir, d\'utiliser moins d\'acier pour couler le bloc. Comme pour l\'implantation des boulons, nous allons établir un dessin en 2 dimensions décrivant la forme que nous voulons sur le produit fini. Nous pourrions dessiner la courbe enveloppe directement avec la souris ou utiliser une approche hybride, comme nous l\'avons fait pour les cercles lorsque nous avons utilisé la souris pour trouver des coordonnées approximatives, avant de taper les vraies valeurs souhaitées. Une approche plus intéressante consiste à utiliser le *mode construction* du dessin 2D pour tracer quelques formes guides qui nous aideraient à tracer une belle courbe enveloppe symétrique en alignant nos formes guides construites.

À titre indicatif, nous allons dessiner deux polygones réguliers pour chaque cylindre, les polygones étant concentriques au cylindre. Pour commencer, passez en vue de dessus du bloc moteur, cachez le carter moteur, revenez à l\'atelier de dessin 2D, sélectionnez le décalage du plan de référence sur 110 mm et le mode Plan XY (ou le mode *Aucun* si vous préférez), puis cliquez sur le bouton *Mode construction* de la barre de commandes (le bouton de mode construction ressemble à une truelle et se trouve juste au-dessus du coin supérieur droit de la vue 3D). Le mode Construction fonctionne comme le mode normal, sauf que les objets de dessin 2D créés en mode Construction sont dessinés dans une couleur différente et sont automatiquement placés dans un groupe séparé dans la vue Arborescence. Cela vous permet de masquer vos dessins guides et de ne laisser que les des choses réelles telles que les marques de trous de boulons en masquant le groupe de construction, ou de supprimer tous les objets de guidage en supprimant simplement le groupe.

:   *Lectures supplémentaires : [ Draft Construction Mode](Draft_ToggleConstructionMode/fr.md)*

Maintenant que votre plan de dessin est correctement configuré et que vous êtes en mode construction, cliquez sur le bouton *Polygone régulier* (<img alt="" src=images/Draft_Polygon.svg  style="width:16px;">) et déplacez votre souris le long du bord du cylindre de gauche tout en maintenant le bouton CTRL enfoncé. Vous devriez voir qu\'il est en train de plaquer un petit point noir soit au bord du cylindre, soit au centre du cylindre, en fonction de l\'emplacement de votre souris sur la circonférence. Déplacez-vous de sorte que le point noir s\'accroche au centre du cylindre et cliquez avec le bouton gauche de la souris. Cela place le centre du polygone au centre du cylindre, le programme nous demande le nombre d'arêtes sur le polygone et le rayon dans lequel il est inscrit. Estimez avec la souris un rayon approximatif de 30 (et cliquez cela) puis entrez 14 pour le nombre de faces, mais laissez la case *Rempli* décochée cette fois-ci. Si vous ne parvenez pas à vous verrouiller au centre du cylindre (j\'ai eu des difficultés avec le mien), vous pouvez toujours entrer les coordonnées manuellement (X=40, Y=0, Z=110). Ajoutez un deuxième polygone, également centré sur le cylindre de gauche, mais celui-ci doit avoir un côté de 22 et un rayon de 45 mm. Enfin, ajoutez les deux mêmes polygones sur le cylindre de droite (centré sur X=100, Y=0, Z=110). Lorsque vous avez terminé, vous devriez avoir deux \"figures en 8\" entourant les cylindres et les goujons de culasse. (Notez qu\'actuellement, le programme ne vous demande pas le nombre d\'arêtes, il vous suffira donc de définir le centre et le rayon, puis de modifier le nombre de faces dans la vue Propriétés).

<img alt="" src=images/_Engine_Block_Tutorial_-_Spline.png  style="width:300px;">

Maintenant que nos polygones guides sont en place, nous sommes prêts à tracer la courbe enveloppe définissant la forme extérieure du bloc moteur. Comme cette courbe fera partie de l'objet final, vous pouvez désactiver le mode Construction en cliquant sur le même bouton que vous avez appuyé pour l'activer. Cliquez maintenant sur le bouton *Ajouter BSpline* (<img alt="" src=images/Draft_BSpline.svg  style="width:16px;">) et commencez à dessiner BSpline par *CTRL + clic bouton gauche souris* sur chaque emplacement auquel vous souhaitez ajouter un point de contrôle pour la courbe enveloppe. Vous voudrez que votre premier point de contrôle se trouve à l\'extrême gauche du polygone de guidage intérieur du cylindre de gauche. Continuez à ajouter des points de contrôle tout au long de la courbe enveloppe jusqu\'à ce que vous cliquiez sur le dernier point avant celui que vous avez commencé à dessiner, puis cliquez sur le bouton *Fermer* où vous avez saisi la position et le rayon des cercles 2D que nous avons dessinés pour les goujon de culasse. En cliquant sur ce bouton de fermeture, les points de contrôle de la courbe enveloppe ont été dessinés et les extrémités jointes pour fermer la boucle. Il est très important que vous fermiez correctement les boucles comme celle-ci si vous envisagez de les extruder en objets solides, comme nous le ferons avec celui-ci. Pour les courbes enveloppes ouvertes, vous pouvez simplement cliquer sur le bouton *Terminer* au lieu du bouton *Fermer* lorsque vous avez terminé de dessiner. A droite, vous pouvez voir à quoi ressemble votre courbe enveloppe avant d\'appuyer sur le bouton de fermeture (remarquez que j\'ai dessiné tous les éléments sauf le dernier segment de ligne et que le pointeur de la souris est sur le point de cliquer sur le bouton de fermeture pour terminer la courbe enveloppe) . Vous remarquerez également que j\'ai coché la case *Rempli* afin que la courbe enveloppe résultante forme une feuille solide, plutôt que simplement un anneau vide. Cette opération doit être effectuée pour l\'extruder en forme solide fermée aux extrémités.

<img alt="" src=images/_Engine_Block_Tutorial_-_Spline_Edit_Mode.png  style="width:300px;">

Les points de contrôle ne sont pas affichés dans cette image. J\'ai donc ajouté une seconde capture d\'écran montrant l\'enveloppe terminée en mode édition (cliquez sur le bouton *Mode édition* pour activer ou désactiver l\'édition pour l\'objet sélectionné, assurez-vous de le désactiver lorsque vous avez terminé, ou passez simplement cette étape si vous êtes satisfait de la forme de votre bloc moteur). Notez également qu'il existe une discontinuité sur le bord le plus à gauche de la courbe des splines, même si elle est fermée correctement. Il s'agit là d'un bogue dans le comportement du programme et c\'est en cours de résolution. Par conséquent, votre courbe enveloppe peut être légèrement différente, si vous exécutez une version plus récente du logiciel que celle disponible actuellement.

### Extrusion du design de la tête 2D dans notre modèle 3D pour finir le design 

Nous nous rapprochons maintenant de la conception finale du moteur. Retournez à l\'atelier Part et cliquez sur le bouton *Extruder l\'esquisse* (<img alt="" src=images/Part_Extrude.svg  style="width:16px;">). Dans la liste déroulante qui apparaît, utilisez *CTRL+ClicGauche* pour sélectionner les 6 goujons de culasse et la courbe enveloppe pour l\'extrusion. La direction par défaut est l'axe Z positif, nous voulons qu\'elle soit l'axe Z négatif pour extruder l\'esquisse de la tête \"vers le bas\" dans le bloc moteur, définissez donc la direction sur X=0, Y=0 et Z=-1, puis tapez 110 pour la longueur (la hauteur du bloc moteur). Après avoir saisi toutes les valeurs et cliqué sur OK, les cercles des boulons seront extrudés vers le bas pour les cylindres et l\'enveloppe sera extrudée vers le bas pour produire une sorte de cylindre aux arêtes \"ondulées\". Sélectionnez et masquez le **Bloc alésé** pour pouvoir voir l\'enveloppe extrudée, puis masquez cet objet afin de voir les 6 cylindres de goujons de culasse. Vous voyez que des formes 3D très sophistiquées peuvent être créées en commençant par dessiner en 2D et en extrudant certaines de leurs parties vers le bas. Nous pourrions même extruder des parties du dessin selon des valeurs différentes pour effectuer des opérations telles que percer des trous de boulons qui ne traversent qu\'une partie du bloc, mais couper des chemises d'eau traversantes. À ce stade, tous vos objets extrudés sont simplement nommés \"Extrude001 \...\". Vous voudrez donc les nommer afin de pouvoir les identifier dans la section suivante (j\'ai nommé les miens **Boulon 1** à **6** et l\'enveloppe **Enveloppe extrudée**, je vous suggère d'utiliser les mêmes noms dans votre modèle). Maintenant que vous avez vos formes extrudées, il ne reste plus que quelques opérations booléennes pour produire le dessin final du bloc. Parcourez et affichez les principaux composants (le **Bloc alésé** et le **Carter**), ainsi que tous les objets extrudés que vous venez de créer.

<img alt="" src=images/Engine_Block_Tutorial_-_Finished_Engine_Block.png  style="width:300px;">

Maintenant que nous avons des objets 3D pour les trous et la forme extérieure, nous pouvons utiliser quelques opérations booléennes pour assembler le tout. Sélectionnez vos 6 goujons de culasse extrudés dans l'arborescence et joignez-les en une union (nommez l'objet obtenu **Trous goujons de culasse**). Ensuite, sélectionnez le **Bloc alésé** et les **Trous goujons de culasse** dans cet ordre et effectuez une coupe (comme vous l\'avez fait lorsque vous avez foré les cylindres), nommez l\'objet *Cut* obtenu **Bloc avec goujons de culasse**. Enfin, sélectionnez le **Bloc avec goujons de culasse** et l**\'Enveloppe extrudée** puis appuyez sur le bouton *Créer une intersection* (<img alt="" src=images/Part_Common.svg  style="width:16px;">), puis nommez le résultat obtenu **Bloc moteur**.

Votre objet final devrait ressembler à l\'image sur la droite.




