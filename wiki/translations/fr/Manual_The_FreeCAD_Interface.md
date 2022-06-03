# Manual:The FreeCAD Interface/fr
{{Manual   *TOC/fr}}

FreeCAD utilise le [framework Qt](https   *//fr.wikipedia.org/wiki/Qt) pour dessiner et gérer son interface. Ce framework est utilisé par un large éventail d\'applications. Ainsi l\'interface FreeCAD est alors très classique et ne présente pas de difficulté particulière à comprendre. La plupart des boutons sont standards et vous les trouverez où vous les attendez **Fichier → Ouvrir, Modifier → Coller, etc.** Voici l\'apparence de FreeCAD lorsque vous l'ouvrez pour la première fois, juste après l\'installation    *

![](images/FreeCAD-v0-18-FirstStart.png )

L\'écran de démarrage est un « écran de bienvenue » qui présente des informations utiles pour les nouveaux arrivants comme les derniers fichiers sur lesquels vous avez travaillé, les nouveautés de FreeCAD ou des informations rapides sur les ateliers les plus courants. Il vous informera également si une nouvelle version stable de FreeCAD est disponible.

Après quelques temps, lorsque vous vous serez familiarisés avec FreeCAD, vous pourrez peut-être modifier les préférences afin qu'au démarrage de FreeCAD vous vous trouviez directement dans l'un des ateliers avec un nouveau document ouvert. Ou, fermez simplement l\'onglet de la page de démarrage et créez un nouveau document    *

![](images/FreeCAD-v0-18-NewProject.png )

### Les ateliers 

Notez que certaines des icônes ont changé entre les deux captures d\'écran ci-dessus. C\'est là où le concept le plus important utilisé dans l\'interface FreeCAD entre en jeu    * les ateliers.

Les ateliers sont des groupes d\'outils (boutons de barre d\'outils, menus et autres contrôles d\'interface) qui sont regroupés par spécialité. Pensez à un atelier où vous auriez différentes personnes travaillant ensemble    * une personne travaille le métal, une autre le bois. Chacune d\'elles a dans son atelier une table séparée avec des outils spécifiques pour son travail. Elles peuvent aussi toutes travailler sur les mêmes objets. Il en va de même dans FreeCAD.

Le contrôle le plus important de l\'interface FreeCAD est le sélecteur d'atelier (Workbench) que vous utilisez pour passer d\'un atelier à l\'autre    *

![](images/FreeCAD-v0-18-WorkbenchMenu.png )

Les ateliers perturbent souvent les nouveaux utilisateurs car il n\'est pas toujours facile de savoir dans quel atelier rechercher un outil spécifique. Mais après un certain temps, ces utilisateurs ont une meilleure perception des outils qu\'offre FreeCAD et s\'adaptent. Les ateliers sont également entièrement personnalisables (voir ci-dessous). Le même outil peut apparaître dans plusieurs ateliers. L\'icône du bouton d\'un outil particulier sera toujours le même quel que soit l\'atelier dans lequel il apparaît.

Plus loin dans ce manuel, vous trouverez également un tableau montrant le contenu de tous les ateliers.

### L\'interface

Regardons mieux les différentes parties de l\'interface    *

![](images/FreeCAD-v0-18-Cube.png )

-   **La vue 3D** est le composant principal de l\'interface. Il peut être séparé de la fenêtre principale, dans une fenêtre qui lui est dédiée. Vous pouvez avoir plusieurs vues du même document (ou des mêmes objets) ou plusieurs documents ouverts en même temps. Vous pouvez sélectionner des objets ou des parties d\'objets en cliquant dessus et vous pouvez obtenir une vue panoramique, zoomer et faire pivoter la vue avec les boutons de la souris. Ceci sera expliqué plus tard, dans le prochain chapitre.

Outre le panneau de la vue 3D, les panneaux d'informations suivants sont disponibles. Ils peuvent être rendus visibles ou masqués en les sélectionnant depuis **Affichage → Panneaux**. Le nom du panneau apparaît dans le coin supérieur gauche du panneau lorsqu\'il est affiché    *

-   **La vue combinée** *( ![en Anglais,](images/Flag-en.jpg ) Combo View)* comporte deux onglets    *
    -   L\'onglet Modèle *( ![en Anglais,](images/Flag-en.jpg ) Model)* vous montre le contenu et la structure de votre document ci-dessus et les propriétés (ou les paramètres) des objets sélectionnés ci-dessous. Ces propriétés sont séparées en deux catégories    *
        -   Données *( ![en Anglais,](images/Flag-en.jpg ) Data)*    * propriétés qui concernent la géométrie elle-même,
        -   Affichage *( ![en Anglais,](images/Flag-en.jpg ) View)*    * propriétés qui affectent la façon dont la géométrie apparait à l\'écran.
    -   L\'onglet Tâches *( ![en Anglais,](images/Flag-en.jpg ) Tasks)* est l\'endroit où FreeCAD vous demandera des valeurs spécifiques à l\'outil que vous utilisez à cet instant, par exemple, en entrant une valeur « longueur » lorsque l\'[outil Ligne de l\'atelier Draft](Draft_Line/fr.md) est utilisé. Il se ferme automatiquement après avoir appuyé sur le bouton **OK** (ou Annuler). En double-cliquant sur l\'objet associé dans la vue combinée, la plupart des outils vous permettront de rouvrir cet onglet Tâches afin de modifier les paramètres.
        L\'onglet Tâches a parfois des effets secondaires déroutants et frustrants. Si l\'onglet Tâche n\'est pas vide, certaines opérations FreeCAD ne fonctionneront pas comme prévu. Par exemple, si vous avez un seul objet dans votre modèle, tel qu\'un cube, double-cliquez dessus pour ouvrir l\'onglet Tâches afin de vous permettre de modifier les paramètres caractérisant le cube. Si vous avez ouvert la vue [Afficher la Sélection ](#Affichage_Sélection.md), le nom interne du cube y est répertorié. Le cube entier deviendra vert dans le panneau 3D, indiquant que le cube entier est sélectionné. Un clic sur l'arrière-plan désélectionnera le cube entier et effacera la vue Sélection. Jusqu\'à présent, c\'est un comportement normal. Toutefois, si vous cliquez maintenant sur une face du cube au lieu de sélectionner cette face, rien ne sera sélectionné car l'onglet Tâches n'a pas été complété. Même si vous n'avez apporté aucune modification aux paramètres, FreeCAD attend que le bouton **OK** (ou autre) de l'onglet Tâches soit cliqué.

-   **La vue rapport** est normalement caché. Toutefois il est intéressant de l\'ouvrir. Elle permet de voir un certain nombre d\'informations telles que des avertissements ou des erreurs vous aidant à debugger ce que vous auriez pu mal faire.
-   **La console Python** est aussi cachée par défaut. C\'est ici que vous interagissez avec le contenu du document en utilisant [le langage Python](https   *//fr.wikipedia.org/wiki/Python_%28programming_language%29). Chaque action que vous faites dans FreeCAD est traductible par du code Python. En ayant cette fenêtre ouverte, cela vous permet de voir la correspondance dans le code en temps réel --- c\'est aussi une manière d\'apprendre un peu de Python sans même sans rendre compte.
-   **La vue arborescente** affiche uniquement l\'arborescence sous l\'onglet Modèle dans la vue combinée. Elle est habituellement cachée.
-   **La vue propriété** montre les informations propres à l\'objet en bas de la vue combinée. Elle est habituellement cachée.
-    **La vue afficher sélection** affiche les noms des objets couramment sélectionnés. Ce sont les objets sur lesquels les opérations de l\'atelier seront effectives. Elle peut être utilisée pour affiner la sélection en désélectionnant certains objets avant l\'application d\'une opération de l\'atelier. La vue de sélection peut également être utilisée pour rechercher des objets par nom, puis de les sélectionner. Par défaut, la vue de sélection est masquée. Bien que vous puissiez souvent déterminer le ou les objets couramment sélectionnés en consultant l'arborescence des objets dans l'onglet Modèle de la vue combinée, pour les opérations complexes nécessitant plusieurs sélections et où la sélection est difficile, il est utile de rendre cette vue visible afin que vous puissiez voir à la fois les étiquettes et compter les objets sélectionnés.

![](images/FreeCAD-v0-18-ExtrudeTask.png )

### Personnalisation de l\'interface 

L\'interface de FreeCAD est hautement personnalisable. Tous les panneaux et barres d\'outils peuvent être déplacés à différents endroits ou empilés les uns sur les autres. Ils peuvent également être fermés et rouverts quand c'est nécessaire dans le menu Affichage ou en cliquant avec le bouton droit de la souris sur une zone vide de l\'interface. Il existe bien d\'autres options disponibles, telles que la création de barres d\'outils personnalisées avec des outils à partir de n\'importe quel atelier ou l'affectation et la modification des raccourcis clavier.

Ces options de personnalisation avancées sont disponibles à partir du menu **Outils → Personnaliser...**    *

![](images/FreeCAD-v0-18-CustomizeInterface.png )

**Pour en savoir plus**    *

-   [Pour commencer avec FreeCAD](Getting_started/fr.md)
-   [Personnalisation de l\'interface](Interface_Customization/fr.md)
-   [Ateliers](Workbenches/fr.md)
-   [En savoir plus sur Python](https   *//www.python.org)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Manual:The FreeCAD Interface/fr
