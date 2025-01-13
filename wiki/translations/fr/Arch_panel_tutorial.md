---
 TutorialInfo:r
   Topic: Modélisation d'un panneau architectural
   Level: Débutant
   Time: 60 minutes
   Author: Yorik
   FCVersion: 
   Files: 
---

# Arch panel tutorial/fr





Ceci est une publication croisée d\'un [tutoriel](http://opensourceecology.org/wiki/FreeCAD_Architecture_Tutorial) écrit à l\'origine pour [Open-Source Ecology](http://opensourceecology.org).



## Presentation de FreeCAD 

<img alt="" src=images/Arch_panel_tutorial_01.jpg  style="width:800px;">

FreeCAD est un modélisateur 3D paramétrique. La modélisation paramétrique vous permet de modifier facilement votre conception en revenant dans l\'historique de votre modèle et en modifiant ses paramètres. FreeCAD est open source (licence LGPL) et très modulaire, permettant une extension et une personnalisation très avancées, notamment grâce à son utilisation intensive du langage Python.

-   Website de FreeCAD : <http://www.freecad.org/>
-   Documentation du wiki de FreeCAD : <http://www.freecad.org/wiki/index.php?title=Main_Page>
-   Ateliers de FreeCAD : <http://www.freecad.org/wiki/index.php?title=Workbench_Concept>
-   Forum de FreeCAD : <http://forum.freecad.org/>
-   Commencer avec FreeCAD : <http://www.freecad.org/wiki/index.php?title=Getting_started>
-   Tutoriel en architecture : <http://www.freecad.org/wiki/index.php?title=Arch_tutorial>



## Installation de FreeCAD 

Vous avez le choix d\'installer la dernière version stable (version 0.16) ou une version de développement (actuellement 0.17). En fait, les versions de développement de FreeCAD sont généralement assez stables, et vous êtes fortement encouragé à essayer une version de développement, sauf si vous avez une raison spécifique de ne pas le faire. Puisque le développement FreeCAD est assez rapide, assurez-vous, si vous téléchargez manuellement, de vérifier de temps en temps et de réinstaller / mettre à jour pour bénéficier des dernières améliorations.

-   Sur Windows: Téléchargez la version la plus récente pour votre version Windows (32 ou 64 bits) à partir de <https://github.com/FreeCAD/FreeCAD/releases>. Double-cliquez sur le fichier à installer.
-   Sur Mac OS: Téléchargez la version la plus récente sur <https://github.com/FreeCAD/FreeCAD/releases>. Double-cliquez sur le fichier à installer.
-   Sur Ubuntu: La version de FreeCAD fournie par Ubuntu est généralement obsolète, il est donc conseillé d\'utiliser le PPA géré par la communauté FreeCAD à la place. Pour l\'installer, ouvrez l\'application \"Sources logicielles\" d\'Ubuntu, et ajoutez soit ppa: freecad-maintainers / freecad-stable pour la version stable, soit ppa: freecad-maintainers / freecad-daily pour la version de développement aux sources logicielles.
-   Sur d\'autres plateformes: Sur la plupart des distributions Linux classiques (Debian, Fedora, etc.), FreeCAD est inclus dans les dépôts de logiciels officiels. Cependant, il se peut que ce ne soit pas toujours la version la plus à jour. Si la version dont vous avez besoin n\'est pas disponible, votre seule option est de compiler vous-même FreeCAD (instructions sur le site FreeCAD)



## Contenus optionnels supplémentaires 

-   Activation de l\'importation / exportation IFC: Pour importer et exporter des projets vers / depuis le format de fichier IFC, FreeCAD s\'appuie sur l\'importateur IfcOpenShell, que vous devez installer séparément à partir de <http://ifcopenshell.org/python.html>. Veillez à choisir une version basée sur python2.7, qui est la même version python utilisée par FreeCAD.
-   Drawing dimensioning workbench: Un plan de travail supplémentaire pour FreeCAD, qui offre de nombreux outils pratiques pour ajouter des cotes et des annotations aux feuilles de dessin 2D de FreeCAD: <https://github.com/hamish2014/FreeCAD_drawing_dimensioning> (Instructions d\'installation sur la page Web)
-   Assembly2 workbench: Un workbench supplémentaire pour FreeCAD, qui offre une série d\'outils d\'assemblage de base: <https://github.com/hamish2014/FreeCAD_assembly2> (Instructions d\'installation sur la page Web)



## Conseils de démarrage rapide 

La collection de tutoriels disponibles sur le wiki FreeCAD est encore très éparse. Cependant, de nombreux membres de la communauté FreeCAD utilisent youtube pour publier des didacticiels vidéo. Assurez-vous de rechercher des contenus relatifs à FreeCAD sur youtube, qui est certainement la meilleure source de matériel d\'apprentissage.

FreeCAD est une application très technique, et sa courbe d\'apprentissage peut être raide. Assurez-vous de compter sur les tutoriels, le wiki de la documentation et n\'hésitez pas à poser des questions sur le forum si vous rencontrez un problème spécifique. Les questions clairement énoncées reçoivent généralement des réponses très rapides et très complètes.



### Une liste très approximative de choses que vous devez savoir 

-   L\'interface FreeCAD est divisée en ateliers. Les ateliers sont simplement des collections d\'outils (boutons de la barre d\'outils et menus) qui sont regroupés, généralement pour une certaine tâche. Lorsque vous passez à un autre atelier, l\'interface affiche les outils de ce plan de travail. Mais le contenu de votre document 3D ne change pas. Vous travaillez toujours sur le même document et sur les mêmes objets.

-   FreeCAD est encore en développement, il y a encore beaucoup de bugs, et l\'application peut parfois tomber en panne. Enregistrez souvent et activez les fichiers de sauvegarde dans Edition → Préférences → Document

-   La plupart des objets dans FreeCAD sont paramétriques. Cela signifie que leur géométrie est créée automatiquement à partir d\'une série de paramètres. Ces paramètres sont toujours modifiables dans la vue Propriétés. Ils sont toujours répartis entre les paramètres qui affectent la géométrie elle-même (onglet Données) et les paramètres qui affectent uniquement l\'affichage de l\'objet (onglet Vue). Cependant, les objets créés avec d\'autres applications, et importés dans FreeCAD, ne seront généralement pas définis par des paramètres, et ne sont donc pas modifiables.

-   Plusieurs ateliers (PartDesign et Arch) sont conçus pour fonctionner uniquement avec des objets solides et refusent de travailler sur des objets qui ne sont pas solides. Une bonne règle est toujours essayer de travailler avec des objets solides.

-   Bien que FreeCAD puisse importer et travailler avec des objets mesh (Mesh workbench), il est principalement conçu pour fonctionner avec un type d\'objet plus avancé appelé brep, utilisé par la plupart de ses ateliers (Part, PartDesign, Draft, Sketcher, Arch). Lors de l\'importation de fichiers basés sur des maillages (.dae, .orb, .stl \...), vous devrez généralement convertir ces objets avant de pouvoir faire quelque chose d\'intéressant avec eux. Cependant, les formats de fichier basés sur des solides (.step, .iges), lorsqu\'ils sont importés dans FreeCAD, produisent directement des objets brep. Les formats 2D (.dxf, .svg) produisent également des contenus brep.

-   FreeCAD dispose de différents modes d\'utilisation des boutons de la souris. Ces modes peuvent être définis dans les préférences ou modifiés à la volée par un clic droit sur l\'arrière-plan de la vue 3D. Ils sont décrits sur <https://wiki.freecad.org/Mouse_navigation/fr>. Les modes les mieux adaptés au travail de CAO sont CAD ou Gestures.



## Exercice : modélisation d\'un panneau de toit 

Pour présenter un flux de travail typique dans FreeCAD, modélisons un panneau de toit comme décrit sur <http://opensourceecology.org/wiki/MicroHouse_4_Roof_-_Module_-_Build_Instructions>. Pour ce faire, nous allons commencer à dessiner les différentes pièces dans une esquisse contrainte 2D, puis nous tirerons parti de l\'objet Arch Window spécial, qui est capable de construire des objets 3D complexes à partir d\'une esquisse 2D contenant les contours de plusieurs pièces. Enfin, puisque ce dont nous avons besoin n\'est pas une fenêtre, mais un panneau de toit, nous allons simplement convertir notre objet fenêtre en un autre type Arc



### 1. Ouvrez FreeCAD, puis définissez vos unités préférées sur \"impérial\" 

Dans le menu Edition → Préférences → Général → Unités



### 2. Passez à l\'atelier de dessin et créez une nouvelle esquisse dans le plan XY. 

![](images/Arch_panel_tutorial_02.jpg )

Habituellement, à moins d\'une raison spécifique de ne pas le faire, vous devrez toujours commencer à dessiner vos esquisses 2D sur le plan du sol, autour du point d\'origine (0,0). Ensuite, c\'est l\'objet 3D généré à partir de cela, qui sera déplacé / tourné en position.



### 3. Dessinez deux rectangles. Sur chacune d\'entre elles, placez une contrainte verticale de 16 pieds et une contrainte horizontale de 2 pouce 

![](images/Arch_panel_tutorial_03.jpg )

Ne vous inquiétez pas des dimensions de vos pièces lorsque vous les dessinez, les contraintes les redimensionneront en conséquence. Pour ajouter une contrainte de cote (verticale ou horizontale), vous pouvez sélectionner une ligne ou deux points (en appuyant sur la touche CTRL).



### 4.Une fois que vos deux rectangles ont la taille correcte, placez une contrainte verticale de 0 entre leurs points d\'angle, et une contrainte horizontale de 4 pieds. 

![](images/Arch_panel_tutorial_04.jpg )

Cela garantit que nos deux rectangles sont correctement positionnés l\'un par rapport à l\'autre.



### 5. Ajouter les deux pièces supplémentaires de 2 in x 6 in 

![](images/Arch_panel_tutorial_05.jpg )

Ajoutez deux autres rectangles et répétez le processus. Notez que dans l\'exemple ci-dessus, nous n\'avons pas spécifié la longueur de ces pièces, mais plutôt placé une contrainte de distance entre leurs extrémités et les pièces verticales longues, et nous laissons un petit écart de 0,05 pouces entre eux. En effet, si nous faisons que les rectangles se touchent, FreeCAD pourrait déduire les boucles à tort, et nous pourrions obtenir des résultats étranges avec l\'outil de fenêtre Arch. Cette petite astuce garantit que chaque rectangle sera reconnu comme une boucle indépendante par l\'outil de fenêtre Arch.



### 6. Ajouter les pièces de renfort d\'angle 

![](images/Arch_panel_tutorial_06.jpg )

Même chose. Faites-en 6 pouces de large, et les séparer des autres rectangles par 0,05 pouces.



### 7. Dessiner 7 pièces de renfort intermédiaires, définir leur largeur à 2 pouces, et contraindre leurs extrémités gauche et droite à 0,05 pouces des rectangles verticaux (ou à 0 pouce des extrémités des autres rectangles horizontaux) 

![](images/Arch_panel_tutorial_07.jpg )

Selon votre système, FreeCAD peut commencer à être lent à traiter de nouvelles contraintes. C\'est l\'inconvénient d\'utiliser des objets contraints, ils avalent rapidement beaucoup de ressources système. Vous devez toujours considérer si vous en avez absolument besoin. Vous pouvez également supprimer les contraintes quand ils ont fait leur travail. Ces dimensions ne seront plus corrigées, mais à moins de déplacer les pièces, elles ne changeront pas. Si nécessaire, vous pouvez toujours rajouter des contraintes plus tard.



### 8. Calculez l\'espacement entre les 7 pièces de renforcement et réglez les contraintes verticales entre elles. 

Dans notre cas, notre longueur totale est de 192 pouces, moins les deux embouts (2 x 2 pouces) et les deux renforts d\'angle (2 x 6 pouces), = 192 - (4 + 12) = 176. Démontage des 7 pièces de renfort (7 x 2) = 162. Diviser ceci par 8 nous donne l\'espace entre chaque renfort: 20.25.

![](images/Arch_panel_tutorial_08.jpg )



### 9. Obtention d\'un esquisseur entièrement contraint 

Sur le panneau de droite (Onglet Tâches de la vue combinée -\> Messages du solveur), vous pouvez voir le message \"\...2 degrés de liberté\". Cela signifie que notre croquis n\'est pas entièrement contraint (il a encore deux \"manières\" d\'être déformé). C\'est parce que, bien qu\'aucun morceau de celui-ci ne puisse maintenant se déplacer par rapport aux autres, l\'esquisse entière peut encore se déplacer verticalement et horizontalement. Pour éviter cela, nous pouvons simplement prendre l\'un de ses points d\'angle, sélectionner le point d\'origine de la grille (où les axes vert et rouge se croisent) et appuyer sur le bouton Point Constraint. Cela rend notre croquis vert, ce qui signifie qu\'il est entièrement contraint, aucune partie ne peut plus bouger.

![](images/Arch_panel_tutorial_09.jpg )

Ce n\'est en fait pas absolument nécessaire. Mais il est toujours préférable de garder une trace de la position exacte des objets (nous sommes maintenant certains que notre coin est au point (0,0)). Dans le cas où quelque chose ne va pas plus tard, ou nous devons déterminer la position d\'un objet construit sur ce croquis, cela sera utile.

Nous pouvons maintenant appuyer sur le bouton \"fermer\" et notre croquis de base est construit:

![](images/Arch_panel_tutorial_10.jpg )



### 10. Passez à l\'atelier Arch et, avec l\'esquisse sélectionnée, appuyez sur le bouton \"window\" 

Notre croquis a maintenant disparu et un de ses rectangles a été légèrement extrudé en une pièce solide:

![](images/Arch_panel_tutorial_11.jpg )

Bien que cela semble faux, c\'est simplement parce que l\'outil Arch Window a créé une pièce par défaut à partir de la plus grande boucle qu\'il pourrait trouver dans l\'esquisse de base. Nous allons réparer cela bientôt. Notez également que l\'esquisse n\'a pas disparu, elle a simplement été désactivée et \"avalée\" par son nouvel objet parent. Vous pouvez toujours le trouver dans l\'arborescence, en développant l\'objet fenêtre, et activer / désactiver son affichage en appuyant sur la touche ESPACE.



### 11. Modifiez les composants de la fenêtre en double-cliquant dessus dans l\'arborescence 

![](images/Arch_panel_tutorial_12.jpg )

En double-cliquant sur la fenêtre, son esquisse de base redevient visible, et nous obtenons son interface d\'édition: A gauche, une liste des boucles trouvées dans l\'esquisse de base, à droite les pièces solides construites dessus.

Commencez par enlever la pièce \"Default\".

Ensuite, sélectionnez la première boucle (Wire0). Il sera mis en évidence dans la vue 3D. Appuyez sur le bouton \"Ajouter\" pour en créer une nouvelle pièce. Donnez-lui un nom, assurez-vous que le bon fil est réglé, et donnez-lui une extrusion de 6 pouces. Le décalage devrait rester 0 puisque nous le voulons placé \"sur le terrain\".

La valeur \"Type\" sera utilisée pour attribuer des matériaux à la fenêtre (pas encore implémentée), donc vous pouvez actuellement laisser \"Frame\".

![](images/Arch_panel_tutorial_13.jpg )

Ensuite, appuyez sur le bouton \"Créer un composant\". Parfois, FreeCAD ne parvient pas à deviner correctement la direction de l\'extrusion, et vous devez donc éditer votre composant et changer la valeur de 6 pouces par -6 pouces.

Répétez ceci pour toutes les pièces nécessaires:

![](images/Arch_panel_tutorial_14.jpg )

Lorsque vous fermez le panneau d\'édition, nous obtenons l\'objet ci-dessus. Notez que par défaut, les objets fenêtre sont représentés semi-transparents. Comme il ne s\'agira pas d\'une fenêtre, nous pouvons simplement l\'éteindre en définissant sa valeur de transparence à 0 dans ses propriétés de vue.



### 12. Ajouter le panneau de couverture 

Nous avons maintenant notre cadre de panneau, mais pas le panneau de base lui-même. Pour ce faire, le meilleur moyen est d\'ouvrir notre esquisse de base et d\'ajouter un nouveau rectangle. Souvenez-vous cependant de ne pas faire coïncider les coins de ce rectangle avec les coins d\'autres rectangles, afin de ne pas confondre notre objet window, ce qui pourrait nous obliger à refaire toute la série de composants si l\'ordre des boucles change

On peut donc contraindre ce nouveau rectangle à 0,05 pouces à l\'intérieur du périmètre. Cela nous obligera à placer 4 nouvelles contraintes.

Nous pouvons ensuite modifier à nouveau notre fenêtre et ajouter de nouveaux composants. Nous pouvons voir qu\'un nouveau fil a été trouvé. Cette fois, nous allons l\'utiliser pour ajouter un panneau de polycarbonate de 8mm (notez que vous pouvez mélanger des unités sans problèmes dans FreeCAD, et écrire \"8mm\" comme épaisseur, même si vous travaillez en pouces). Nous allons également lui donner un décalage de 0,05 pouces, donc il est légèrement décalé du cadre, juste pour la cohérence, car toutes les parties de notre objet ont ce décalage entre eux.

![](images/Arch_panel_tutorial_15.jpg )

Nous pouvons maintenant créer un autre composant basé sur le même fil, afin de placer un autre panneau au-dessus de notre cadre. Cette fois, nous allons lui donner un décalage de 6,05 pouces. Notre panel est enfin complet:

![](images/Arch_panel_tutorial_16.jpg )



### 13. Transforme la fenêtre en un autre type de composant Arch 

Ce n\'est pas vraiment nécessaire pour le moment, mais cela pourrait devenir important plus tard quand nous exportons ou travaillons à d\'autres applications orientées construction, par exemple via IFC, nous ne voulons pas que notre panneau soit identifié comme une fenêtre.

Le Workbench Arch de FreeCAD fournit un moyen facile de gérer cela, c\'est-à-dire que n\'importe quel type d\'objet peut toujours en devenir un autre, en étant la base d\'un autre type. Dans ce cas, transformons notre fenêtre en un objet Panel, en sélectionnant simplement la fenêtre et en appuyant sur l\'outil Panel.

![](images/Arch_panel_tutorial_17.jpg )

Notez que la couleur du panneau résultant a changé, c\'est parce que le support des matériaux dans FreeCAD et le module Arch est encore incomplet. Quand c\'est fini, ceci sera correctement géré



### 14. Dupliquer le panneau 

Notre panneau peut ensuite être dupliqué et copié de plusieurs façons, par exemple en utilisant le copier / coller. Mais un moyen plus intéressant est d\'utiliser l\'outil Draft Clone (également présent sur l\'Arb Workbench, comme tous les autres outils Draft). L\'outil Cloner conserve la relation entre l\'objet de base et son clone, de sorte que toute modification apportée à l\'objet de base se reflète dans tous ses clones.

![](images/Arch_panel_tutorial_18.jpg )

Dans la version de développement actuelle de FreeCAD, les clones d\'objets Arch sont maintenant eux aussi des objets Arch.



### 15. Rotation et positionnement des panneaux. 

Bien que l\'atelier d\'assemblage de FreeCAD ne soit pas encore prêt, nous devons positionner nos pièces manuellement, soit en manipulant leur propriété Placement, soit en utilisant les outils Draft Move et Rotate, qui ne sont en réalité que des moyens visuels de modifier le placement des objets.

Les deux outils Draft Rotate et Move utilisent le système Snapping Draft. Différentes positions d\'accrochage (points de terminaison, points médians, etc.) sont disponibles, pouvant être activées / désactivées, ce qui permet d\'effectuer un positionnement et des rotations très précis.

![](images/Arch_panel_tutorial_19.jpg )

![](images/Arch_panel_tutorial_20.jpg )


{{BIM_Tools_navi

}} {{Draft_Tools_navi}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [Sketcher](Category_Sketcher.md) > Arch panel tutorial/fr
