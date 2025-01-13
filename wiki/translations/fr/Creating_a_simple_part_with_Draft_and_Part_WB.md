---
 TutorialInfo:r
   Topic: Modélisation
   Level: Débutant
   Author: heda
   Time: 1.5 heures
   FCVersion: 0.19 ou supérieure
   Files: 
   SeeAlso: Creating_a_simple_part_with_Part_WB/fr, Creating_a_simple_part_with_PartDesign/fr
---

# Creating a simple part with Draft and Part WB/fr





## Introduction

Ce tutoriel a pour but d\'être utilisé comme une première introduction à l\'[atelier Draft](Draft_Workbench/fr.md) ![](images/Switch_DraftWorkbench.JPG ) dans FreeCAD. Le tutoriel utilise une *forme 2D* pour créer un *solide 3D*, ce dernier étant réalisé par le biais de l\'[atelier Part](Part_Workbench/fr.md). Il est recommandé au lecteur de travailler d\'abord avec le tutoriel frère *[Créer une simple pièce avec l\'atelier Part](Creating_a_simple_part_with_Part_WB/fr.md)*, qui crée le même modèle avec une technique différente, tout en couvrant les bases de l\'interface utilisateur de FreeCAD. Ce tutoriel s\'attend à ce que l\'utilisateur soit familiarisé avec l\'interface utilisateur et certains flux de travail disponibles dans FreeCAD. Le tutoriel est composé de telle sorte que le but n\'est pas nécessairement de montrer la manière la plus efficace d\'utiliser le programme, mais plutôt de faire prendre conscience au lecteur des différentes fonctionnalités disponibles dans FreeCAD, comment les utiliser, et où les trouver.



### Le tutoriel couvre 

-   Le modèle à réaliser
-   Création du profil 2D
-   Pourquoi l\'extrusion peut échouer
-   Extrusion du profilé
-   Création du trou traversant
-   Réalisation d\'une esquisse à partir du profil 2D
-   Qualité des modèles
-   Conclusion



## Le modèle à réaliser 

<img alt="" src=images/GGTuto1_Vue.PNG  style="width:372px;">

![](images/T101pwb01-02_dims.png )



## Création du profil 2D 

Créez un nouveau document et enregistrez-le directement sous un nouveau nom. Changez la vue pour <img alt="" src=images/Std_ViewTop.svg  style="width:24px;"> [vue de dessus](Std_ViewTop/fr.md) et passez à l\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [atelier Draft](Draft_Workbench/fr.md), votre écran devrait ressembler à celui ci-dessous. Si la grille n\'apparaît pas, activez-la ou désactivez-la avec <img alt="" src=images/Draft_ToggleGrid.svg  style="width:24px;">. [Draft Basculer la grille](Draft_ToggleGrid/fr.md).

![](images/T101dwb01-01draftgrid.png )

Pour commencer le profil, dessinez un <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [rectangle](Draft_Rectangle/fr.md) aléatoire sur le plan xy en cliquant sur 2 points dans la [Vue 3D](3D_view/fr.md) formant n\'importe quelle diagonale d\'un rectangle. Un *panneau de tâches* s\'ouvre une fois la commande lancée. Cette fois, nous ne l\'utiliserons pas du tout, mais vous pouvez bien sûr entrer directement les coordonnées du rectangle. Votre vue 3D devrait maintenant avoir un rectangle dessiné, similaire à l\'image ci-dessous.

![](images/T101dwb01-02rectangleraw.png )

Lorsque l\'on travaille dans l**\'atelier Draft**, on dessine presque toujours sur un plan 2D. Ce plan 2D est appelé *[plan de travail](Draft_SelectPlane/fr.md)*, et, si les paramètres par défaut sont utilisés, il s\'alignera toujours automatiquement sur la vue 3D courante. Ainsi, jusqu\'à ce que le profil 2D soit terminé, il est préférable de conserver simplement la vue du dessus (position de la prise de vue) et de ne pas jouer avec la rotation de la vue. Si vous l\'avez modifiée, il vous suffit de revenir à la vue du dessus avant de lancer une nouvelle commande dans l**\'atelier Draft**.

La vue latérale de notre modèle terminé a un contour extérieur de 100 x 50 mm, et il serait bien que le coin inférieur gauche soit placé à la position zéro globale. Ceci peut être réalisé par l\'intermédiaire de l\'éditeur de propriétés. Assurez-vous que le **Rectangle** créé est sélectionné, puis changez la *Position* du rectangle en **(0, 0, 0)**, modifiez la *Hauteur* à **50** mm et la *Longueur* à **100** mm comme dans les images ci-dessous.

![](images/T101dwb01-03rectangleprops.png )

Le **rectangle** est terminé et il devrait ressembler à ceci après avoir appliqué <img alt="" src=images/Std_ViewFitAll.svg  style="width:24px;"> [Tout afficher](Std_ViewFitAll/fr.md) à la vue.

![](images/T101dwb01-04rectangledone.png )

Ensuite, nous allons décomposer le rectangle en ses quatre bords, en sélectionnant d\'abord le **rectangle** puis en lançant la commande <img alt="" src=images/Draft_Downgrade.svg  style="width:24px;"> [Draft Désagréger](Draft_Downgrade/fr.md), la face remplie disparaîtra et l\'objet dans l**\'arborescence** est maintenant une **polyligne** au lieu d\'un **rectangle**, comme le montre l\'image de gauche ci-dessous. En lançant **Draft Désagréger** une fois de plus, la *polyligne* sera décomposée en ses *bords*, comme le montre l\'image du milieu ci-dessous.

![](images/T101dwb01-05rectangledowngrade.png )

L\'observateur remarquera que l\'icône de l\'objet dans la vue en arborescence pour la polyligne s\'est déjà transformée en une *boîte bleue*. Cette boîte bleue est l\'icône utilisée pour les objets géométriques génériques (les objets géométriques de l\'atelier Part pour être précis, mais cela est pour les lecteurs avancés). Sélectionnez le bord vertical gauche et lancez la commande <img alt="" src=images/Draft_Upgrade.svg  style="width:24px;"> [Draft Agréger](Draft_Upgrade/fr.md), l\'ancien *bord* aura maintenant une icône différente et a changé de *label* en *Line*. C\'est maintenant un objet de l**\'atelier Draft** où l\'on peut modifier par exemple le *point de départ* et le *point d\'arrivée* à travers l*\'éditeur de propriétés*, ce qui n\'est pas possible avec les objets *arête*.



### Créer le congé 

Commencez par sélectionner les bords du coin supérieur droit, utilisez le menu **Edition → Sélection par boîte**, <img alt="" src=images/Std_BoxSelection.svg  style="width:24px;"> [Sélection par boîte](Std_BoxSelection/fr.md), maintenez le <img alt="" src=images/Mouse_LMB.svg  style="width:24px;"> **bouton gauche de la souris** et faites glisser **de droite à gauche** et relâchez le **bouton gauche de la souris**. Lorsque l\'on fait glisser *de droite à gauche*, la sélection résultante inclut tout ce qui se trouve entièrement ou partiellement dans la zone de sélection. Si l\'on fait glisser *de gauche à droite*, seuls les objets entièrement compris dans la zone de sélection sont inclus dans la sélection résultante. La sélection réelle se produit lorsque le bouton gauche de la souris est relâché, et il n\'y a pas d\'aperçu de ce qui sera sélectionné.

![](images/T101dwb02-01filletboxselection.png )

Avec les bords du coin supérieur droit sélectionnés, lancez la commande <img alt="" src=images/Draft_Fillet.svg  style="width:24px;"> [congé](Draft_Fillet/fr.md) dans l**\'atelier Draft**. Cochez la case *Supprimer les objets originaux* et modifiez le *rayon* à 20 mm et appuyez sur **entrée**.

![](images/T101dwb02-02fillettaskpanel.png )

Le **congé** est créé et votre modèle devrait maintenant ressembler à ce qui suit.

![](images/T101dwb02-03filletdone.png )



### Créer le chanfrein 

Pour réaliser le *chanfrein*, nous devons disposer d\'une ligne avec la bonne inclinaison et aussi pouvoir la positionner correctement. Commençons par la position, qui est à la coordonnée *(50, 50, 0)*. Dans le profil actuel, nous n\'avons pas de point à cet endroit, alors créons-en un en faisant une *ligne d\'aide temporaire*. Sélectionnez d\'abord la **ligne** verticale gauche, puis créez la ligne d\'aide en <img alt="" src=images/Std_DuplicateSelection.svg  style="width:24px;"> [Dupliquer une sélection](Std_DuplicateSelection/fr.md) dans **Edition → Dupliquer la sélection**, **Ligne001** est créée. Utilisez l*\'éditeur de propriétés* et déplacez la **Ligne001** de 50 mm dans la direction x en utilisant la propriété *Placement*. Dupliquez ensuite *l\'arête horizontale inférieure* et modifiez *l\'angle* de l\'arête à 30 degrés, en utilisant à nouveau la propriété *Placement*. Le modèle devrait maintenant ressembler à l\'image ci-dessous.

![](images/T101dwb03-01chamferhelp.png )

Ensuite, il faut déplacer la *ligne angulaire* en position. Pour cela nous utilisons <img alt="" src=images/Draft_Move.svg  style="width:24px;"> [Draft Déplacer](Draft_Move/fr.md) ainsi que la fonctionnalité *aimantation* dans *l\'atelier Draft*, plus spécifiquement l\'aimantation *terminaison*. Assurez-vous d\'abord que votre barre d\'outils d\'aimantation ressemble à celle ci-dessous.

![](images/T101pwb03-02_snap.png )

Ensuite, sélectionnez la *ligne angulaire*, *Edge001*, appuyez sur *Déplacer* et un *panneau de tâches* s\'ouvre.

![](images/T101dwb03-03_movetaskpanel.png )

Assurez-vous que la case *Copier* n\'est pas cochée. Passez la souris sur le *quart supérieur* de la *ligne angulaire*, une fois que le *point blanc* est affiché au bon endroit et que le symbole *terminaison* apparaît, cliquez sur le <img alt="" src=images/Mouse_LMB.svg  style="width:24px;"> **bouton gauche de la souris**. Déplacez la souris vers le quart supérieur de la ligne d\'aide, une fois que le point blanc et le symbole Terminaison apparaissent, cliquez sur le *bouton gauche de la souris*. La séquence est illustrée ci-dessous.

![](images/T101dwb03-04_moveline.png )

La ligne est maintenant à la bonne position, mais elle est trop longue. Pour ajuster la longueur, <img alt="" src=images/Draft_Trimex.svg  style="width:24px;"> [Draft Ajuster ou prolonger](Draft_Trimex/fr.md) sera utilisé. Sélectionnez la *ligne angulaire*, **Edge001**, appuyez sur Ajuster et cliquez ensuite sur la partie inférieure de la *ligne verticale la plus à gauche*, **Line**, pour l\'utiliser comme arête d\'ajustage. La projection du point où le bord d\'ajustage est sélectionné sur le bord à couper, détermine le résultat. Si vous sélectionnez la ligne verticale la plus à gauche près de son extrémité supérieure, la mauvaise partie de la ligne angulaire sera coupée. L\'image ci-dessous montre la commande **Ajuster**, la ligne verticale présélectionnée, et le curseur survolant la mauvaise extrémité de cette ligne. Si vous regardez attentivement, vous pouvez voir l\'aperçu du résultat.

![](images/T101dwb03-05_trimline.png )

Ajustez également la ligne verticale la plus à gauche pour former le coin inférieur du chanfrein. Sélectionnez la *ligne angulaire*, **Edge001**, près de son extrémité supérieure droite pour obtenir un résultat correct. Si vous faites une erreur en ajustant, utilisez simplement <img alt="" src=images/Std_Undo.svg  style="width:24px;"> [Annuler](Std_Undo/fr.md) et <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Recalculer](Std_Refresh/fr.md) (ce dernier est souvent appelé *recompute*) et réessayez.

![](images/T101dwb03-06_chamferlowercornerdone.png )

Pour ajuster le *bord supérieur horizontal*, le **congé** doit être *désagrégé* de sorte que le bord supérieur soit son propre objet dans la vue en arborescence. Si vous tentez de l\'ajuster sans avoir préalablement effectué le déclassement, la fonction d\'ajustement tente d\'ajuster l\'arc dans le congé. Comme l\'arête d\'ajustement, la *ligne verticale centrale*, est perpendiculaire à l\'arête à ajuster, vous ne pouvez pas contrôler le résultat de l\'ajustement en choisissant un point correct sur l\'arête d\'ajustement. Dans ce cas, vous devez inverser la solution par défaut en maintenant la touche **Alt** enfoncée lorsque vous sélectionnez l\'arête de coupe.

Le profil est prêt et montré ci-dessous avec les arêtes organisées dans un <img alt="" src=images/Std_Group.svg  style="width:24px;"> [groupe](Std_Group/fr.md) nommé **Profile** (ou *étiqueté* pour être précis dans le jargon de FreeCAD), avec la ligne d\'aide supprimée. Les groupes peuvent être utilisés pour organiser les caractéristiques de vos *documents FreeCAD*, leur utilisation est similaire à une structure de dossiers sur le système de fichiers d\'un ordinateur. Pour déplacer des éléments à l\'intérieur et à l\'extérieur d\'un groupe, utilisez le *glisser-déposer* dans la vue en arborescence.

![](images/T101dwb03-07_profiledone.png )



## Pourquoi l\'extrusion peut échouer 

Enregistrez le document. Nous allons faire des expériences dans ce paragraphe et nous voulons pouvoir revenir au modèle en cours.

Allons-y : sélectionnez toutes les arêtes dans le *groupe* **Profile**, et dans l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md) lancez la commande <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Extruder](Part_Extrude/fr.md). Un *panneau des tâches* s\'ouvre, acceptez toutes les valeurs par défaut et cliquez sur **OK**.

![](images/T101dwb04-01_extrudelineserror.png )

Cela n\'a pas fonctionné, mais il semble assez facile de corriger l\'erreur, nous devons juste spécifier une direction. Cliquez sur **OK** pour revenir au *panneau des tâches* et sélectionnez *direction personnalisée*.

![](images/T101dwb04-02_extrudelineszaxis.png )

Acceptez l\'axe z par défaut et cliquez une nouvelle fois sur **OK**.

![](images/T101dwb04-03_extrudelinessheets.png )

Nous avons réussi à créer une structure ressemblant à une clôture, à en juger par la vue en arborescence, chaque bord est traité séparément. Ce n\'est pas le solide rempli que nous voulons. Appuyez sur [Annuler](Std_Undo/fr.md), et essayons autre chose.

En faisant défiler l\'écran jusqu\'en bas du *panneau de tâches* **Extruder**, il y a une option *Créer le solide*, cochez cette option et cliquez sur **OK**.

![](images/T101dwb04-04_extrudelinesfilled.png )

Tout a disparu, manifestement cela n\'a pas fonctionné non plus. Voyons pourquoi aucune de ces méthodes ne fonctionne. Dans le premier cas, nous avons reçu une erreur indiquant que la direction ne pouvait pas être déterminée. Une face plane a une normale, c\'est-à-dire une direction, une ligne n\'en a pas. Puisque nous savons, grâce à notre deuxième tentative, que cela a fonctionné en fournissant une direction, l\'erreur vient simplement du fait que nous essayons d\'extruder une ligne sans connaître de direction. L\'observateur dira qu\'un arc a une normale (direction), ce qui est vrai. Si vous sélectionnez uniquement l\'arête qui constitue l\'arc, FreeCAD l\'extrudera, également avec les paramètres par défaut.

Dans le second cas, cela a fonctionné, mais nous avons également obtenu une extrusion pour chaque arête de notre sélection. Les caractéristiques résultantes ne sont cependant pas ce que nous voulons, c\'est-à-dire un solide.

Dans le troisième cas, nous avons coché la case *Créer le solide*, et tout a disparu. Les objets dans la vue en arborescence ont également une icône différente, un *point d\'exclamation blanc* sur un fond rouge, cette *icône superposée* particulière signifie que l\'objet a une erreur qui doit être corrigée. Vous pouvez vous renseigner sur les différents types d\'[icônes de superposition](Tree_view/fr#Ic.C3.B4nes_de_superposition.md) du wiki.

En survolant l\'un des objets de l\'arborescence à l\'aide de l\'icône de superposition, une info-bulle s\'affiche, indiquant que *la polyligne n\'est pas fermée*

![](images/T101dwb04-05_extrudelineserrortooltip.png )

Dans notre cas, l\'erreur n\'est pas réparable. Il est *géométriquement impossible* de créer un solide à partir d\'une simple ligne extrudée. Une ligne extrudée devient simplement une feuille, ou *coquille* dans le jargon de FreeCAD. En d\'autres termes, ce n\'est pas une limitation de FreeCAD, c\'est un résultat fondamental de la théorie géométrique. La raison pour laquelle la vue 3D devient complètement vide est que les éléments créés, ou les objets dans l\'arborescence, ont des erreurs dans la *forme* produite, et ne contiennent donc rien à rendre. FreeCAD crée cependant les nouveaux objets du document (dans ce cas des extrusions) et cache donc toute géométrie/objet utilisé pour créer les nouveaux objets du document. C\'est pourquoi l\'écran devient vide lorsqu\'on essaie de créer un solide à partir d\'une ou plusieurs lignes.

L\'astuce de l\'outil dit tout, afin d\'extruder dans un solide on a besoin d\'une *polyligne fermée, ou une face*. Une face est, par définition, simplement une polyligne fermée qui est remplie. Une façon de créer une polyligne fermée à partir de nos bords de profil est de les sélectionner tous et d\'appliquer <img alt="" src=images/Draft_Upgrade.svg  style="width:24px;"> [Draft Agréger](Draft_Upgrade/fr.md). Si appliqué une fois, elle devient une polyligne, tout en consommant les arêtes individuelles de la vue en arborescence. Si appliqué deux fois, cela devient une face, l\'un ou l\'autre permettant une extrusion solide réussie.

Avant de passer au paragraphe suivant : ouvrez la version précédente du document.



## Extrusion du profil 

Une autre façon de créer le fil fermé est d\'utiliser la commande <img alt="" src=images/Part_Builder.svg  style="width:24px;"> [Générateur de formes](Part_Builder/fr.md) de l\'atelier Part, qui permet de réaliser une polyligne sans consommer les arêtes individuelles. Le **Part Générateur de formes** est un outil puissant pour créer n\'importe quelle entité géométrique dans FreeCAD qui peut être utilisée plus loin pour créer des solides complexes, l\'exemple le plus simple est la création d\'une ligne entre deux sommets. Cliquez sur **Part Générateur de formes** pour faire apparaître le *panneau des tâches*.

![](images/T101dwb05-01_shapebuildertaskpanel.png )

On peut utiliser soit *Fil à partir d\'arêtes*, soit *Face à partir d\'arêtes*. Les sélections multiples doivent être faites avec la touche **Ctrl** enfoncée. Utilisons *Face à partir d\'arêtes*, une fois que cette option est sélectionnée, on peut aussi sélectionner *Planaire*, faites-le aussi. Sélectionnez ensuite toutes les arêtes du profil, l\'ordre n\'a pas d\'importance (dans ce cas) et cliquez sur **Créer**, puis sur **Fermer** pour revenir à la vue en arborescence. La *face* a été créée.

![](images/T101dwb05-02_shapebuilderfacedone.png )

Sélectionnez la *Face* et lancez **Part Extrusion**, réglez la *longueur* de l\'extrusion à **30** mm et cliquez sur **OK**.

![](images/T101dwb05-03_extrusiondone.png )



## Créer le trou traversant 

Pour réaliser le trou traversant, nous avons besoin d\'un *cylindre* correctement *positionné* pour effectuer une *soustraction* booléenne.

Créez un cylindre, et positionnez-le correctement. Dans ce cas, le *rayon* est de 5 mm, la *hauteur* est fixée à 60 mm. Pour le placement, il est d\'abord *tourné* de -90 degrés autour de l\'axe x, puis positionné à *(65, -5, 15)*. Le 5 négatif dans la direction y est dû au fait que la hauteur est 10 mm plus longue que nécessaire.

![](images/T101dwb05-04_cylinderplaced.png )

Il n\'y a pas de mal à rendre la hauteur du cylindre plus longue que nécessaire. Pour un modèle simple comme celui-ci, il importe peu que le cylindre ait la hauteur exacte du profil. Il est cependant bon d\'éviter les faces coplanaires pour éviter les erreurs numériques dans le noyau géométrique qui peuvent parfois entraîner des effets étranges, ou des échecs dans les opérations ultérieures.

Avec une dernière soustraction booléenne, et après avoir modifié l\'apparence de l\'objet résultant, le modèle est terminé.

![](images/T101dwb05-05_modelcomplete.png )



## Faire une esquisse à partir du profil 2D 

L\'utilisation de **l\'atelier Draft** est une façon de créer un profil en 2D. Dans **l\'atelier Draft**, une polyligne peut être réalisée dans un espace 3D. FreeCAD fournit un autre outil pour réaliser des profils 2D - l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [atelier Sketcher](Sketcher_Workbench/fr.md). L\'utilisation d\'une *esquisse* est un moyen plus polyvalent de créer un profil 2D. Tout profil 2D créé dans **l\'atelier Draft** peut être converti en une esquisse *sans contrainte*.

Commencez par masquer la fonction **Soustraction** et rendez visibles les bords du profil. Sélectionnez les bords et, dans **l\'atelier Draft**, cliquez sur le bouton de la barre d\'outils <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:24px;"> [Draft vers Esquisse](Draft_Draft2Sketch/fr.md). Vous devriez voir la même chose que dans l\'image ci-dessous.

![](images/T101dwb06-01_draft2sketch.png )

Ensuite, cachez les bords d\'origine et double-cliquez sur l\'objet **Sketch** dans l\'arborescence, ce qui vous amène à l\'état suivant, le *panneau des tâches de Sketcher* est ouvert.

![](images/T101dwb06-02_sketchedit.png )

Voici à quoi cela ressemble lorsque l\'on *édite une esquisse*. Comme il ne s\'agit pas d\'un tutoriel sur l\'utilisation de Sketcher, vous pouvez le fermer. Si vous souhaitez une introduction à l\'esquisse, qui est un flux de travail essentiel dans toute CAO 3D paramétrique, veuillez suivre le tutoriel associé *[Créer une pièce simple avec PartDesign](Creating_a_simple_part_with_PartDesign/fr.md)*.

Une fois que **l\'esquisse** est fermée et sélectionnée, utilisez Extruder de la même manière que précédemment dans **l\'atelier Part**. Le bloc de base du modèle simple est à nouveau prêt.

![](images/T101dwb06-03_sketchextruded.png )



## Qualité des modèles 

Tôt ou tard, lorsque vous travaillez avec la CAO paramétrique 3D, vous rencontrez un modèle cassé, qu\'il s\'agisse d\'un modèle que vous avez créé vous-même ou d\'un modèle que vous avez importé. Un modèle cassé peut fonctionner pour son objectif, mais le plus souvent, il y a des opérations ultérieures qui ne fonctionneront tout simplement pas. Pour réparer un modèle cassé, il faut savoir ce qu\'il faut réparer, et c\'est là qu\'interviennent les outils de contrôle de qualité intégrés dans FreeCAD.

Tout d\'abord, vérifions la qualité de la pièce **Extrude001** récemment créée. Avec l**\'atelier Part** actif, sélectionnez d\'abord **Extrude001** et utilisez ensuite la commande <img alt="" src=images/Part_CheckGeometry.svg  style="width:24px;"> [Vérifier la géométrie](Part_CheckGeometry/fr.md). Cochez toutes les cases des paramètres, sauf celle du haut, et cliquez sur le bouton **Lancer la vérification**.

![](images/T101dwb07-01_geocheck.png )

Notre modèle est OK, aucune erreur n\'est signalée. Il y a aussi une liste du contenu du modèle, ou dans le jargon de FreeCAD, le contenu de la *forme*, c\'est à dire comment elle est constituée à partir de la base. Ici on peut voir qu\'apparemment pour faire un *solide* il faut aussi une *coque*, et la coque est faite de *faces*, et ainsi de suite. En d\'autres termes, on peut créer n\'importe quel solide en commençant simplement par créer des points, ou *sommets*, à partir desquels on crée des *arêtes*, et à partir de celles-ci on crée des *polylignes*, et à partir des polylignes on crée des *faces* qui sont ensuite assemblées en une *coque*, à partir de laquelle on arrive finalement à un *solide*. Un solide ne peut être fabriqué qu\'à partir d\'une coque étanche. Une coque non étanche est une source fréquente de modèles CAO problématiques, cela peut par exemple se produire lors de l\'importation de géométries créées dans un autre logiciel, surtout si l\'on utilise les formats de fichiers neutres couramment disponibles.

Une autre vérification que l\'on peut faire concerne l\'esquisse. Fermez le *panneau des tâches* pour le contrôle de la géométrie. Sélectionnez l\'esquisse, développez **Extrude001** dans la vue en arborescence si nécessaire afin de voir l\'objet de l\'esquisse. Passez à l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [atelier Sketcher](Sketcher_Workbench/fr.md), utilisez la commande <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:24px;"> [Valider une esquisse\...](Sketcher_ValidateSketch/fr.md), un *panneau de tâches* s\'ouvre. Dans le *panneau des tâches*, cliquez sur le bouton **Trouver** les *Coïncidences manquantes*. Il met en évidence et signale *6* d\'entre elles, c\'est-à-dire tous les points où les arêtes se rencontrent.

![](images/T101dwb07-02_sketchvalidate.png )

Cliquez sur **OK** dans le dialogue contextuel, puis cliquez sur le bouton **Réparer** pour corriger les *coïncidences manquantes*. Si vous fermez le *panneau des tâches*, et que vous passez en *mode édition* de l\'esquisse, celle-ci indique *12 degrés de liberté*, au lieu de *24* précédemment. Ce résultat a été obtenu en ajoutant des *contraintes coïncidentes* aux extrémités des bords.

Le lecteur attentif remarquera que, lors de l\'utilisation des arêtes de Draft, celles-ci doivent être jointes en une polyligne fermée pour former une extrusion solide, alors que dans Sketcher, cela n\'est apparemment pas nécessaire. La logique ici est que l\'esquisse est un objet, et l\'extrusion d\'un objet est traitée comme s\'il s\'agissait d\'une polyligne fermée (dans ce cas).

Enfin, il convient de souligner que, bien que la création d\'objets ultérieurs à partir d\'esquisses avec des *sommets ouverts* puisse fonctionner, il est préférable de ne pas en avoir, et d\'avoir une *esquisse entièrement contrainte* (par opposition à une esquisse sous-contrainte). La raison pour laquelle cela fonctionne ici est que l*\'esquisse* est créée à partir d\'un Draft profil construit de manière à ce que les points d\'extrémité des arêtes correspondent sans aucun vide. Si vous dessinez à la main dans une esquisse et que vous essayez également de faire correspondre les points d\'extrémité à la main, il est pratiquement garanti que les points d\'extrémité ne correspondront pas, c\'est-à-dire que les écarts (bien qu\'ils ne soient pas vraiment visibles à l\'écran) seront suffisamment importants pour que le noyau géométrique ne puisse pas considérer les arêtes comme étant géométriquement jointes.



## Conclusion

Après avoir suivi le tutoriel, vous vous êtes familiarisé avec les fonctionnalités de base de FreeCAD, ainsi qu\'avec les ateliers de base **Part** et **Draft**. Vous êtes également au courant de l\'existence de **l\'atelier Sketcher**, qui pour beaucoup d\'utilisateurs expérimentés est le seul outil utilisé pour créer des profils 2D utilisés plus tard dans les opérations sur les solides. L\'utilisation des *esquisses* est un concept fondamental de l**\'atelier PartDesign**. Nous vous suggérons de vous familiariser avec les *esquisses* et l**\'atelier PartDesign** si vous vous concentrez sur la création de solides. Le tutoriel frère *[Créer une pièce simple avec PartDesign](Creating_a_simple_part_with_PartDesign/fr.md)* fait le même modèle que ce tutoriel. Si votre objectif est de modéliser des bâtiments, votre prochain apprentissage devrait être les ateliers **Draft** et **Arch**.

Enfin, FreeCAD est réalisé par des volontaires pendant leur temps libre. Si vous voulez faire progresser les possibilités de FreeCAD, pensez à [contribuer](Help_FreeCAD/fr.md) à FreeCAD, par exemple en améliorant la documentation.



---
⏵ [documentation index](../README.md) > Creating a simple part with Draft and Part WB/fr
