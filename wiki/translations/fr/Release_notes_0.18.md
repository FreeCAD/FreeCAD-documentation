# Release notes 0.18/fr
FreeCAD 0.18 est sorti le 12 mars 2019, à télécharger sur la page [GitHub](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.18.4). Ceci est un résumé des changements les plus intéressants. La liste complète des modifications est disponible sur [MantisBT bugtracker FC 0.18 - Liste des changements](https   *//www.freecadweb.org/tracker/changelog_page.php?version_id=78). Les notes de versions de FreeCAD sont disponibles dans la [liste des fonctionnalités](Feature_list/fr#Notes_de_versions.md).

## Points forts 

Outils [TechDraw](#Atelier_TechDraw.md) étendus.

<img alt="Modèle par Laurent14" src=images/TechDraw_sheet_screenshot.png  style="width   *700px;">




Nouveaux outils [Sketcher (esquisse)](#Atelier_Sketcher_(esquisseur).md), [PartDesign (Conception de pièces)](#Atelier_PartDesign_(Conception_de_pièces).md) plus stables et plus robustes

<img alt="Modèle par un1corn" src=images/Part_engine_screenshot.jpg  style="width   *700px;">




Outils [Arch (architecture) et BIM (Building information modeling)](#Atelier_Arch_(architecture).md) améliorés et étendus

<img alt="Modèle par regis" src=images/Arch_work_screenshot.png  style="width   *700px;">




## Généralités

-   Centre de démarrage (Start) repensé
-   L\'arborescence du document (onglet Modèle) propose désormais 3 options d\'affichage de tous les documents, avec les options définies dans le menu **Affichage → Arborescence du document**    *
    -   Document unique (Affiche uniquement le document actuellement actif)
    -   Multi Document (Affiche tous les documents tels qu\'ils étaient auparavant jusqu\'à FreeCAD 0.17)
    -   Réduire/Développer (développe le document actif et réduit tous les autres)
-   Lorsqu\'une tâche est active et requiert une saisie de l\'utilisateur, une icône représentant un crayon apparaît maintenant dans l\'onglet Tâches et disparaît à la fin de la tâche.
-   La vue 3D bénéficie désormais d\'un nouveau **[Cube de navigation](Navigation_Cube/fr.md)** pour orienter rapidement la vue. Il comporte également un petit menu pour définir la projection orthographique ou en perspective, ainsi que pour adapter le contenu à la vue. L\'emplacement du cube de navigation peut être défini dans **Préférences → Affichage → Vue 3D** et il peut également être masqué.
-   La prise en charge du système d\'unités des États-Unis ingénierie civile / transport a été ajouté. Ces unités incluent ft, ft\^2, ft\^3, mph et angles en degrés/minutes/secondes. Ces unités permettent d'exprimer les pieds sous forme décimale, contrairement à Construction US, qui force des fractions de pouce.
-   Il est maintenant possible de spécifier une image d\'arrière-plan personnalisée pour la fenêtre principale de FreeCAD en utilisant l\'option [**Préférences → Général → Activer l'arrière-plan en mosaïque**](Preferences_Editor/fr#Général.md).

<File   *Start> center 0.18 screenshot.jpg\|thumb\|left\|Le Start center repensé <File   *FC018> Navigation Cube.png\|thumb\|left\|Le cube de navigation <File   *FreeCAD> with background image.jpg\|thumb\|left\|FreeCAD avec une image d\'arrière-plan personnalisée




## Atelier Arch (Architecture) 

![ 700px \| thumb \| right \| L\'atelier Arch au travail](images/_Arch_release018_example.jpg )

-   [ Walls](Arch_Wall/fr.md) peut maintenant être affiché comme une pile de blocs. Il existe de nombreuses options pour configurer leurs tailles et la manière dont les blocs doivent être empilés.
-   Les [ Building Parts](Arch_BuildingPart/fr.md) sont le nouveau conteneur Arch à tout faire. Ils peuvent regrouper n'importe quel nombre d'objets, ils peuvent être utilisés pour créer des sols (étages), des bâtiments (les outils [Arch Floor](Arch_Floor/fr.md) et [ Arch Building](Arch_Building/fr.md) produisent désormais des parties de construction), ou tout autre groupe de Objets Arch. Ils peuvent être déplacés comme [ Parts](Std_Part/fr.md), et ils sont [ clonables](Draft_Clone/fr.md) et [ référençables](Arch_Reference/fr.md) !
-   L\'[Atelier BIM](BIM_Workbench/fr.md) (ajouté via le <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md)) est un nouveau pendant externe expérimental de [ Arch](Arch_Workbench/fr.md). Nous y testons de nouvelles fonctionnalités et de nouveaux flux de travail dans un environnement plus libre. Pour en être sûr, faites un essai !
-   [ Windows](Arch_Window/fr.md) dispose de nouveaux préréglages, tels qu\'une fenêtre coulissante à 4 volets. Si la [librairie Parts](https   *//github.com/FreeCAD/FreeCAD-library/tree/c5eea12cdda7a3e6349323808815f63b0f97ef2e) est installée, on dispose de toutes les portes et fenêtres de la bibliothèque.
-   [ Panneaux](Arch_Panel/fr.md) peut désormais créer différents types de panneaux profilés, tels que des panneaux ondulés ou même des panneaux sandwich.
-   Les objets [ Structure](Arch_Structure/fr.md) ont un nouveau mode de dessin de poutre, qui vous permet de cliquer sur deux points pour placer un élément structurel entre eux.
-   Tous les types IFC sont maintenant disponibles pour tous les objets Arch. Tous les objets peuvent être exporté de n\'importe quel autre type vers IFC.
-   [ Window placement](Arch_Window/fr.md) a été entièrement repensé. Placer correctement les fenêtres dans les objets hôtes était auparavant très pénible, c\'est maintenant beaucoup plus facile.
-   Paramètres de fenêtre dynamiques    * la taille des cadres de fenêtre est maintenant une propriété de fenêtre. Il est donc maintenant possible d\'ajuster l\'épaisseur des fenêtres prédéfinies sans qu\'il soit nécessaire de modifier leurs composants ou leurs esquisses de base.
-   Les jeux de propriétés IFC sont désormais pris en charge par tous les objets Arch.
-   L\'importateur et l\'exportateur IFC ont été considérablement améliorés avec une multitude de nouvelles fonctionnalités    * prise en charge des ensembles de propriétés, prise en charge de la grille, compression de fichiers, profils partagés, prise en charge des groupes, ensembles de quantités, etc.
-   [ Materiaux](Arch_SetMaterial/fr.md) prend désormais en charge la hiérarchie. Si vous attribuez à un matériau un autre matériau en tant que père, il apparaît correctement empilé dans l\'arbre.
-   Tous les objets et matériaux Arch prennent désormais en charge les systèmes de classification (pas encore pris en charge par l\'import/export IFC).
-   [Références externes](Arch_Reference/fr.md) vous permet maintenant de lier dans un fichier FreeCAD des pièces d\'un autre fichier FreeCAD.

-   Mais il y a beaucoup plus ! Consultez le [rapports de développement Arch / BIM](https   *//github.com/yorikvanhavre/BIM_Workbench/wiki) pour voir tout ce qui y a été fait cette année.

## Atelier Draft (Planche à dessin) 

<img alt="Outils d\'annotation Draft plus précis" src=images/Draft_release018_example.jpg  style="width   *700px;">

-   L\'outil [Draft Échelle](Draft_Scale/fr.md) a été entièrement repensé. Il comporte désormais plus d\'options et est beaucoup plus confortable à utiliser.
-   L\'outil [Draft Texte](Draft_Text/fr.md) a également été entièrement repensé. Il dispose désormais de son propre objet paramétrique avec beaucoup plus d\'options. Attention, ces nouveaux textes ne sont pas supportés par la version 0.17
-   [Les filaires Draft](Draft_Wire/fr.md) ont maintenant une option de clic droit qui permet de les aplatir de force sur leur plan médian.
-   Nouvel outil [ Draft Joindre](Draft_Join/fr.md), qui vous permet de joindre des tracés et des lignes individuelles en un seul tracé.
-   Nouvel outil [ Draft Fractionner](Draft_Split/fr.md), qui divise une ligne ou un tracé en un point pour créer un autre tracé ou une ligne.
-   Si vous appuyez sur la touche **** pendant que vous dessinez en mode Draft, la cible de capture est activée, ce qui vous permet de capturer des objets masqués par d\'autres.
-   L\'outil Draft Ajouter un Point a été amélioré pour ajouter de manière plus fiable des nœuds sur des lignes et des tracés exactement à l\'endroit où vous cliquez.




## Atelier FEM 

<img alt="Le dialogue Matériau FEM optimisé" src=images/FEM-Material-dialog-018.png  style="width   *300px;"> En v0.17, des quantités de fonctionnalités nouvelles ont été ajoutées à FEM. Aussi, l'objectif principal de FEM dans la version 0.18 de FreeCAD n'a pas été d'ajouter encore de nouvelles fonctionnalités et outils, mais de rendre les outils existants plus stables et de corriger autant que possible les bogues. FEM a reçu 470 rectificatifs au cours du cycle de développement de FreeCAD 0.18 [1](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=13154&p=297292#p297110).

### Améliorations générales sur la base du code 

-   Quantité de corrections de bugs.
-   Code révisé et nettoyé. Suppression du code en double.
-   Correction de nombreuses fautes de frappe dans le code et les messages visibles.
-   Correctifs de compatibilité avec Python 3.
-   Plus de tests unitaires ont été ajoutés.
-   Possibilité de compiler FreeCAD avec mise à jour externe SMESH.

### Outils

-   Un outil de plan de coupe a été ajouté pour pouvoir sélectionner les solides qui se trouvent dans d\'autres solides.
-   Le filtre de déformation VTK a suscité un certain intérêt.
-   Un type d\'analyse pour la vérification du modèle CalculiX a été ajouté.

### Matériau

La gestion des matériaux a été améliorée. Il est maintenant possible d\'utiliser l\'éditeur global de matériaux FreeCAD. Voir aussi les [fiches Matériau](Release_notes_0.18/fr#Manipulation_des_matériaux.md). Pour cela, le panneau de travail Matériau FEM a été optimisé.

## Atelier Part (Pièce) 

-   L\'outil [Vérifier la géométrie](Part_CheckGeometry/fr.md) ouvre maintenant une petite fenêtre avec une barre de progression et un bouton **Annuler** pour terminer la tâche si cela prend trop de temps.
-   Le nouvel outil [Defeaturing](Defeaturing_Workbench/fr.md) est basé sur l\'outil du même nom inclus dans OCCT 7.3.0. On peut supprimer des attributs sélectionnés sur un solide, tels que des trous, des protubérances, des espaces, des chanfreins, des congés, etc. Pour plus d\'informations, voir l\'article sur la [modélisation de modèle 3D](https   *//dev.opencascade.org/index.php?q=node/1211) sur le site Web de OCCT. Veuillez noter que si FreeCAD est construit sur une version plus ancienne que OCTCT 7.3.0, cet outil ne sera pas disponible et sera grisé.

-   Le nouvel outil [SliceApart (trancheur)](Part_SliceApart/fr.md) est basé sur le composant [Slice to Compound (Scinder en composants)](Part_Slice/fr.md) et comprend un découpeur automatique de composant permettant de fractionner facilement des objets.

## Atelier PartDesign (Conception de pièces) 

-   Le nouvel outil [Système de coordonnées](PartDesign_CoordinateSystem/fr.md) permet désormais l\'ajout d\'une visualisation du système de coordonnées locales par rapport à un ou plusieurs objets de référence.

## Atelier Path 

### Améliorations générales 

-   Le chemin peut maintenant afficher correctement le gcode avec les termes d\'axe ABC
-   Améliorations de l\'éditeur Outils - Édition simplifiée pour des types d\'outils sélectifs

### Amélioration de la Tâche (Job) 

-   Les travaux (jobs) peuvent maintenant avoir plusieurs objets de base
-   L\'organisation des conteneurs de travail (jobs) a été améliorée
-   Les valeurs par défaut pour les préférences d\'Opération peuvent être contrôlées via SetupSheets

### Opérations

-   Nouvelle opération de compensation adaptative
-   Nouvelle opération Deburr (ébavurage)
-   Le nouvel habillage AxisMap qui limite le 4ème axe en faisant correspondre une direction linéaire à un axe de rotation
-   Prise en charge des objets 2D et du fraisage de bords individuels via Engrave (Gravure) et Deburr (Ébavurage)
-   RampEntry Dressup (rampe d\'entrée d\'usinage) a maintenant un point de départ configurable
-   L\'opération PocketShape (forme en poche) peut maintenant \"utiliser les contours\"

### Post-traitement 

-   grbl_post -- argument pour supprimer les commandes de changement d\'outil
-   post-traitement grbl_g81

## Atelier Sketcher (Esquisseur) 

<img alt="Démo Vue sectionnée Sketcher" src=images/Sketch-clip-plane-demo.png  style="width   *700px;">

-   Le nouvel outil **[View section](Sketcher_ViewSection/fr.md)** crée un plan de coupe qui rend invisible la partie du modèle situé en avant du plan d\'esquisse. Cela est utile lorsque le plan d\'esquisse est situé à l\'intérieur d\'un modèle solide. En appuyant à nouveau sur l\'outil Afficher la section, vous revenez à une vue complète.
-   Le solveur **Sketcher** a bénéficié d\'améliorations et détecte mieux les contraintes redondantes et conflictuelles, en particulier celles induites par des contraintes symétriques.
-   Nouvel outil **[Constrain Diameter](Sketcher_ConstrainDiameter/fr.md)** ajouté
-   **DoF Finder** est un nouvel utilitaire permettant de mettre en évidence les degrés de liberté restants. Dans le message animé du solveur du panneau Tâches, le message traditionnel*Esquisse sous-contrainte avec x degrés de liberté* souligne maintenant le texte *x degrés* en bleu. Cliquez dessus pour mettre en surbrillance verte, dans la vue 3D, les éléments qui ne sont pas complètement contraints.
-   **Sketcher Auto Remove Redundants** est une nouvelle case à cocher dans la boîte de message du solveur. Lorsque cette option est activée, elle empêche la création de contraintes redondantes lorsque l\'utilisateur applique des contraintes, et supprime automatiquement les contraintes redondantes.
-   Il existe une nouvelle commande pour supprimer toutes les contraintes en même temps. Vous pouvez le trouver dans le menu **Sketch → Outils d'esquisse → Supprimer toutes les contraintes**.
-   Nouvelle option dans **Préférences → Esquisseur → Général → Masquer les unités de longueur de base pour les systèmes d'unités pris en charge**. Cela masque l\'unité des contraintes dimensionnelles en mode d\'édition d\'esquisse.
-   La taille des sommets (points) peut maintenant être définie dans **Préférences → Affichage → Vue 3D → Taille du marqueur**.
-   Nouvelle commande **[Déplacer](Sketcher_Move/fr.md)** pour déplacer toute la géométrie sélectionnée du dernier point sélectionné. Vous pouvez y accéder via la liste déroulante de l\'outil Cloner.
-   Ajout de la case à cocher *Informations étendues* au widget de liste de contraintes.

Liens de forum pertinents    *

-   [améliorations récentes de Sketcher](https   *//forum.freecadweb.org/viewtopic.php?f=9&t=29192)
-   [Feature #1632   * autoriser la saisie d\'un diamètre au lieu d\'un rayon pour la contrainte de rayon du cercle](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=29152)
-   [Sketcher Suppression automatiquement des modes redondants](https   *//forum.freecadweb.org/viewtopic.php?f=9&t=30594)
-   [Nomenclature étendue des contraintes](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=28890)

## Atelier Spreadsheet (Feuille de calcul) 

## Atelier Surface 

## Atelier TechDraw 

L\'atelier TechDraw a bénéficié de plusieurs ajouts et améliorations dans la V0.18.

-   Nouvelle page pour l\'exportation vers Dxf
-   nouveau tutoriel pour TechDraw
-   amélioration de la mise en forme des cotes pour les vues isométriques, les angles et l\'emplacement du texte
-   amélioration des messages d\'erreur
-   amélioration du formatage de la vue en coupe
-   autoriser les groupes de lignes personnalisés
-   préférences supplémentaires
-   sélection plus facile des marqueurs de bord et de centre
-   direction de la vue en fonction de la vue 3D actuelle ou de la face sélectionnée
-   ajout de tolérances +/\* aux dimensions
-   nouvelle dimension d\'angle à partir de 3 points
-   menu contextuel RMB
-   zoom à partir du clavier (Ctrl +/-)
-   support pour les dimensions DMS

## Manipulation des matériaux 

<img alt="Une fiche de matériau" src=images/_Material-Card-018.png  style="width   *300px;"> La manipulation des matériaux a été améliorée. Il est maintenant possible de créer des **fiches de matériau** pour chaque matériau. Les fiches peuvent contenir toutes les informations, propriétés physiques, spécifications architecturales, liens Web, commentaires, etc. Les fiches sont des fichiers texte avec le suffixe **.FCMat** et peuvent être utilisées pour tous les ateliers de FreeCAD.

FreeCAD fournit des fiches de matériau pour les métaux standard, les plastiques et différents types d\'acier.

## Modules Additionnels 

Certains des nouveaux modules communautaires activement développés au cours du cycle de développement de V0.18.

-   [A2plus](A2plus_Workbench/fr.md) est un nouvel atelier permettant d\'assembler différentes pièces dans FreeCAD. Il s'agit d'une extension de l'atelier Assembly2, qui offre une gestion étendue de la couleur et de la transparence des pièces, ainsi qu'une nouvelle contrainte utilisant le centre de gravité des pièces.

-   [Curves](https   *//github.com/tomate44/CurvesWB), un ensemble d'outils permettant de créer et d'éditer des courbes et des surfaces NURBS.

-   [Nurbs](https   *//github.com/microelly2/freecad-nurbs), une collection de scripts pour la gestion des surfaces et des courbes de formes libres.

-   [Silk](https   *//github.com/edwardvmills/Silk), une collection d'outils de modélisation de surface NURBS axés sur des courbes de bas niveau et la continuité aux jonctions.

-   L\'[atelier Flamingo](Flamingo_Workbench/fr.md), un ensemble de commandes et d'objets FreeCAD personnalisés permettant d'accélérer le dessin des charpentes et des tubulures.

-   [Atelier de génie civil/transports](Civil_Engineering_Workbench/fr.md)

-   [GDT](https   *//github.com/juanvanyo/FreeCAD-GDT), cotation géométrique et tolérancement (GD&T).

-   [InventorLoader](https   *//github.com/jmplonka/InventorLoader) pour importer des fichiers AutoDesk Inventor (en cours).

-   L\'[atelier KicadStepUp](KicadStepUp_Workbench.md) est destiné à aider les utilisateurs de KiCad et FreeCAD dans la collaboration ECAD et MCAD.

-   [CadQuery FreeCAD Module](https   *//github.com/jmwright/cadquery-freecad-module/wiki) est un atelier permettant aux utilisateurs d\'écrire des scripts Python. Il est adapté à ceux basés sur l\'API de script CadQuery CAD. Un nouvel éditeur de code est mis à disposition et les variables de script peuvent être éditées de manière dynamique à l\'aide d\'un dialogue de paramètre. L\'atelier ajoute également un menu qui inclut les opérations normales de fichier pour les scripts CadQuery (ouvrir, nouveau, fermer, etc.) et des exemples de scripts pour aider les utilisateurs à apprendre de nouveaux concepts.

-   L\'[atelier Defeaturing](Defeaturing_Workbench/fr.md) est destiné à l\'édition de modèles STEP importés, à la suppression d\'éléments sélectionnés du modèle.

[Category   *News](Category_News.md) [Category   *Documentation](Category_Documentation.md) [Category   *Releases](Category_Releases.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.18/fr
