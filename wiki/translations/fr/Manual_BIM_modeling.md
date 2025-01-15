# Manual:BIM modeling/fr
{{Manual:TOC}}

BIM signifie [Building Information Modeling](https://fr.wikipedia.org/wiki/Building_information_modeling). C\'est un processus utilisé en architecture, ingénierie et construction pour créer et gérer des représentations numériques de structures physiques. Il intègre non seulement la géométrie en 3D, mais aussi des données essentielles telles que les matériaux, les coûts et les calendriers, ce qui permet une analyse avancée et une collaboration tout au long du cycle de vie d\'un projet.

Dans FreeCAD, la fonction BIM a évolué de manière significative, en particulier avec la version 1.0, où les ateliers Arch et BIM, auparavant séparés, ont été fusionnés en un atelier BIM intégré. Cette consolidation rationalise les flux de travail, permettant aux utilisateurs de modéliser, de documenter et de gérer les projets de construction plus efficacement dans un environnement unique.

Une avancée majeure introduite dans FreeCAD v1.0 est l\'adoption du concept IFC natif. Auparavant, comme la plupart des applications BIM, FreeCAD traduisait les données dans les deux sens entre son modèle de données interne et le format de fichier IFC (Industry Foundation Classes), ce qui entraînait une perte potentielle de données au cours des processus d\'ouverture et d\'enregistrement. Avec Native IFC, les utilisateurs de FreeCAD peuvent désormais ouvrir, manipuler et enregistrer directement des fichiers IFC, le fichier IFC lui-même servant de structure de données. Cette approche élimine la traduction inutile des données et garantit que les modifications sont enregistrées sans réécrire l\'intégralité du fichier, ce qui la rend compatible avec les systèmes de contrôle de version tels que Git et offre un flux de travail plus transparent et plus précis pour la manipulation des fichiers IFC.

Dans ce chapitre, nous verrons comment modéliser ce petit bâtiment :

![](images/FreeCAD_BIMHouse.png )

-   Créez un nouveau document et passez à l'<img alt="" src=images/Workbench_BIM.svg  style="width:16px;"> [atelier BIM](BIM_Workbench/fr.md).
-   Depuis le menu **Edition → Préférences → Draft → Grille et aimantation** et réglez:
    -   **Lignes principales toutes les** `10`.
    -   **Espacement de la grille** `1000mm` pour avoir une grille d\'un mètre, ce qui convient à la taille de notre bâtiment.
    -   **Taille de la grille** `100 lignes`.
-   Sur la barre d\'outils **Aimantation**, assurez-vous que le bouton <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> [Aimantation Grille](Draft_Snap_Grid/fr.md) soit activé, afin que nous puissions utiliser la grille autant que possible.
-   Si vous ne voyez pas les axes, cliquez sur le bouton <img alt="" src=images/Draft_ToggleGrid.svg  style="width:16px;"> [Basculer la grille](Draft_ToggleGrid/fr.md).
-   Réglez le [Plan de travail](Draft_SelectPlane/fr.md) sur le plan **XY**
-   Dessinez quatre lignes avec l\'outil <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Draft Ligne](Draft_Line/fr.md). Vous pouvez entrer les coordonnées manuellement ou simplement sélectionner les points sur la grille avec la souris. Nous utiliserons des mètres pour nos dimensions :
    -   Du point (0,0) au point (0,3)
    -   Du point (0,3) au point (4,3)
    -   Du point (4,3) au point (4,0)
    -   Du point (4,0) au point (0,0)

<img alt="" src=images/Exercise_arch_03.jpg  style="width:600px;">

Remarquez que nous avons toujours tracé les lignes dans le même sens (sens des aiguilles d\'une montre). Bien que cela ne soit pas obligatoire, cela permet de s\'assurer que les murs que nous construirons ensuite seront orientés de la même manière à gauche et à droite. Vous vous demandez peut-être pourquoi nous n\'avons pas simplement dessiné un rectangle, ce qui aurait été plus simple. Cependant, l\'utilisation de quatre lignes distinctes nous permet de présenter d\'autres fonctions de BIM, comme la combinaison de plusieurs objets en un seul, qui est un élément essentiel du flux de travail.

-   Une fois que vous avez créé les lignes, vérifiez leurs points de départ et d\'arrivée et ajustez-les si nécessaire pour les obtenir exactement.

![](images/Manual-BIM_Modeling_-_Adjusting_Lines.png )

-   Sélectionnez les quatre lignes, puis appuyez sur le bouton <img alt="" src=images/Arch_Wall.svg  style="width:16px;"> [Arch Mur](Arch_Wall/fr.md).
-   Définissez la **Hauteur** des murs à 3m (par défaut).
-   Définissez la propriété **Alignement** à **gauche** En définissant la propriété Alignement à gauche, vous vous assurez que les murs que vous créez seront positionnés à gauche des lignes que vous avez tracées. Dans le BIM Workbench de FreeCAD, les murs sont généralement générés sur la base d\'une ligne de référence, et l\'alignement gauche ou droit indique de quel côté de la ligne le mur sera placé.

Si vous n\'avez pas tracé les lignes dans l\'ordre indiqué (dans le sens des aiguilles d\'une montre), l\'orientation de certains murs peut être inversée, ce qui signifie qu\'ils peuvent être placés de l\'autre côté de la ligne (à droite au lieu de gauche). Dans ce cas, vous devrez ajuster l\'alignement à droite pour ces murs spécifiques afin de vous assurer qu\'ils sont tous alignés de manière cohérente. Une fois ce réglage effectué correctement, vous obtiendrez quatre murs qui se croisent aux angles, positionnés à l\'intérieur de la ligne de base, formant ainsi la disposition souhaitée.

<img alt="" src=images/Exercise_arch_04.jpg  style="width:600px;">

Après avoir créé des murs, l\'étape suivante consiste à les joindre pour qu\'ils se croisent correctement. Cette opération est nécessaire lorsque les murs ne se connectent pas proprement à leurs intersections. Pour ce faire, vous sélectionnez un mur en tant qu\'« hôte » et vous ajoutez les autres murs en tant qu\'« ajouts », en fusionnant leur géométrie avec celle de l\'hôte. Tous les objets de l\'atelier BIM peuvent avoir plusieurs ajouts (qui ajoutent de la géométrie) ou soustractions (qui enlèvent de la géométrie). Ces relations peuvent être gérées à tout moment en double-cliquant sur l\'objet dans l\'arborescence, ce qui permet de procéder à des ajustements souples pour garantir une intégration harmonieuse des murs et des autres éléments architecturaux.

-   Sélectionnez les quatre murs en appuyant sur la touche **Ctrl**, le dernier étant le mur que vous avez choisi de devenir l\'hôte.
-   Appuyez sur le bouton <img alt="" src=images/Arch_Add.svg  style="width:16px;"> [Arch Ajouter](Arch_Add/fr.md). Les quatre murs ont maintenant été transformés en un seul :

<img alt="" src=images/Exercise_arch_05.jpg  style="width:600px;">

Les parois individuelles sont cependant toujours accessibles, en développant l\'objet mur dans l\'arborescence (petite flèche).

-   Plaçons maintenant une porte en appuyant sur l\'outil <img alt="" src=images/BIM_Door.svg  style="width:16px;"> [Porte](BIM_Door/fr.md).
-   Commencez par sélectionner le mur. Bien que cette étape ne soit pas obligatoire, c\'est une habitude utile à prendre. Si un objet est sélectionné avant de commencer une opération, l\'opération s\'appliquera automatiquement à cette entité par défaut.
-   Définissez le <img alt="" src=images/View-axonometric.svg  style="width:16px;"> [plan de travail](Draft_SelectPlane/fr.md) à **auto** pour ne pas être limité au plan du sol.
-   Appuyez sur le bouton <img alt="" src=images/BIM_Door.svg  style="width:16px;"> [Porte](BIM_Door/fr.md).
-   Dans le panneau de création de la porte, sélectionnez le préréglage **Porte en verre** et réglez sa **Largeur** à 1 m et sa **Hauteur** à 2,1m. Vous remarquerez que vous pouvez choisir entre différents types de portes et les paramétrer comme vous le souhaitez. Dans FreeCAD, une porte est dérivée par une opération de [fenêtre](Arch_Window/fr.md).
-   Assurez-vous que L\'option <img alt="" src=images/Draft_Snap_Near.svg  style="width:16px;"> [Aimantation Au plus proche](Draft_Snap_Near/fr.md) est activée, pour que nous puissions cliquer sur les visages.
-   Placez votre porte à peu près au milieu de la face avant du mur :

![](images/FreeCAD_BIMDoor.png )

-   Nous pouvons maintenant définir l\'emplacement précis en développant le mur et les objets de la fenêtre dans l\'arborescence et en changeant la propriété de **Placement** de l\'esquisse de base de notre porte. Réglez sa position sur **x = 0.5 m, y = 0, z = 0**. Notre porte est maintenant exactement là où nous le voulons :

![](images/FreeCAD_BIMDoorPos.png )

-   Plaçons une fenêtre à côté de notre porte. Sélectionnez le mur, appuyez sur l\'outil <img alt="" src=images/Arch_Window.svg  style="width:16px;"> [Fenêtre](Arch_Window/fr.md), sélectionnez le préréglage **Open 2-pane**, et placez une fenêtre **1m x 1m** sur la même face que la porte. Définissez le placement de l\'esquisse sous-jacente à la position **x = 0, y = 0, z = 1,1m**, de sorte que la ligne supérieure de la fenêtre soit alignée sur le haut de la porte.

![](images/FreeCAD_BIMWindow.png )

Les fenêtres sont toujours basées sur des esquisses. Vous pouvez facilement créer des fenêtres personnalisées en dessinant d\'abord une esquisse sur une face, puis en transformant cette esquisse en fenêtre en la sélectionnant et en cliquant sur le bouton de fenêtre. Vous pouvez ensuite définir les paramètres de la fenêtre (par exemple, les parties de l\'esquisse qui doivent être extrudées et leur quantité) en double-cliquant sur la fenêtre dans l\'arborescence. Passons maintenant à la création d\'une dalle :

-   Réglez le [Draft Plan de travail](Draft_SelectPlane/fr.md) sur le plan **XY**.
-   Créez un <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Draft Rectangle](Draft_Rectangle/fr.md) avec une **longueur** de 5m, une **hauteur** de 4m et placez-le à la position **x: -0.5m, y: -0.7m, z: 0**.
-   Sélectionnez le rectangle.
-   Cliquez sur l\'outil <img alt="" src=images/BIM_Slab.svg  style="width:16px;"> [Dalle](BIM_Slab/fr.md) pour créer une dalle à partir du rectangle.
-   Gardez les valeurs par défaut de 0.2m pour la propriété **height** et définissez la **direction** normale à (0,0,-1), afin que l\'extrusion aille vers le bas. Nous aurions pu déplacer l\'objet de 0,2 m vers le bas, mais c\'est une bonne pratique de garder les objets extrudés alignés avec leur profil de base pour maintenir la cohérence et la précision du modèle.
-   Définissez la propriété **Ifc Type** de la dalle sur **slab** (dalle). Ceci n\'est pas nécessaire dans FreeCAD, mais il est important pour l\'exportation IFC car il garantira que l\'objet est exporté avec le type IFC correct.

![](images/FreeCAD_BIMSlab.png )

-   Mettons un toit au-dessus de nos têtes. Nous pouvons facilement le faire en utilisant l\'outil <img alt="" src=images/Arch_Roof.svg  style="width:16px;"> [Toit](Arch_Roof/fr.md).
-   Appuyez sur l\'outil <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:16px;"> [Aimantation Plan de travail](Draft_Snap_WorkingPlane/fr.md) pour activer l\'ébauche sur tous les plans.
-   En choisissant l\'une des faces supérieures de notre maison, appuyez sur l\'option <img alt="" src=images/Draft_SelectPlane.svg  style="width:16px;"> [Sélectionner un plan](Draft_SelectPlane/fr.md) pour activer le dessin sur tous les plans. Le plan de travail est maintenant défini sur cette face.
-   Créer un <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [rectangle](Draft_Rectangle/fr.md) s\'accrochant à deux points opposés des murs :
-   Dans l\'onglet **Données** du toit, mettez le paramètre **Runs** à 1600.
-   Si vous souhaitez changer la couleur du toit, vous pouvez le faire dans l\'onglet *Vue*.

![](images/FreeCAD_BIMHouseg.png )

Notre modèle est maintenant complet. L\'étape suivante consiste à l\'organiser correctement pour s\'assurer qu\'il s\'exporte correctement au format IFC. Les fichiers IFC exigent que tous les éléments de construction soient regroupés au sein d\'un objet **bâtiment** et, éventuellement, au sein d\'un **étage** spécifique. En outre, tous les bâtiments doivent être situés sur un « site ». Cependant, l\'exportateur IFC de FreeCAD génère automatiquement un site par défaut s\'il n\'y en a pas, de sorte que nous n\'avons pas besoin de l\'ajouter manuellement. Il est important de structurer correctement le modèle pour respecter les normes IFC, afin d\'assurer une collaboration fluide et la compatibilité avec d\'autres logiciels BIM. Une bonne organisation permet également d\'éviter toute perte de données ou erreur lors du processus d\'exportation.

-   Sélectionnez les murs, la dalle et le toit.
-   Appuyez sur le bouton <img alt="" src=images/Arch_Floor.svg  style="width:16px;"> [Arch Niveaux](Arch_Floor/fr.md).
-   Sélectionnez le niveau que nous venons de créer.
-   Appuyez sur le bouton <img alt="" src=images/Arch_Building.svg  style="width:16px;"> [Arch Bâtiment](Arch_Building/fr.md).

Notre modèle est maintenant prêt à exporter :

![](images/FreeCAD_BIMExport.png )

Le [format IFC](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) est l\'un des atouts les plus précieux dans un monde BIM gratuit, car il permet l\'échange de données entre toute application et acteur du monde de la construction, de manière ouverte (le format est ouvert, gratuit et maintenu par un consortium indépendant). L\'exportation de vos modèles BIM comme IFC garantit que tout le monde peut les voir et les analyser, peu importe l\'application utilisée.

-   Sélectionnez l\'objet de niveau supérieur que vous souhaitez exporter, c\'est-à-dire l\'objet Bâtiment.
-   Sélectionnez le menu **Fichier -\> Exporter -\> Industry Foundation Classes** et enregistrez votre fichier.
-   Le fichier IFC résultant peut maintenant être ouvert dans un large éventail d\'applications et de visionneuses (l\'image ci-dessous montre le fichier ouvert dans la visionneuse gratuite [IfcPlusPlus](http://www.ifcquery.com/)). Il est important de vérifier le fichier exporté dans une telle application de visualisation avant de le distribuer à d\'autres personnes afin de vérifier que toutes les données contenues dans le fichier sont correctes. FreeCAD lui-même peut également être utilisé pour rouvrir le fichier IFC résultant.

![](images/FreeCAD_BIMIFC.png )

Nous pouvons utiliser l\'<img alt="" src=images/Workbench_TechDraw.svg  style="width:16px;"> [atelier TechDraw](TechDraw_Workbench/fr.md) pour créer un dessin de notre bâtiment. Le processus est similaire à ce qui a été montré dans la section précédente, nous n\'entrerons donc pas trop dans les détails ici. Il suffit de créer une nouvelle vue en utilisant le <img alt="" src=images/TechDraw_PageDefault.svg  style="width:16px;">. [insérer une page par défaut](TechDraw_PageDefault/fr.md), puis sélectionnez la vue que vous souhaitez afficher dans le dessin et ajoutez des dimensions si nécessaire. Cela nous permettra de créer une représentation 2D professionnelle du modèle 3D à des fins de documentation ou de présentation.

![](images/FreeCAD_BIMHouseDrawing.png )

Notre page est maintenant prête, et nous pouvons l\'exporter vers les formats SVG ou DXF, ou l\'imprimer. Le format SVG vous permet d\'ouvrir le fichier en utilisant des applications d\'illustration telles que [Inkscape](http://www.inkscape.org), avec lesquelles vous pouvez rapidement améliorer les dessins techniques et les transformer en dessins de présentation beaucoup plus agréable. Il offre beaucoup plus de possibilités que le format DXF.



## Téléchargements

-   Le fichier produit lors de cet exercice: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/house.FCStd>
-   Le fichier IFC exporté à partir du fichier ci-dessus: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/house.ifc>
-   Le fichier SVG exporté à partir du fichier ci-dessus: <https://github.com/yorikvanhavre/FreeCADmanual/Blob/master/files/house.svg>



## En relation 

-   [Atelier BIM](BIM_Workbench.md)
-   [Atelier Arch](Arch_Workbench/fr.md)
-   [Draft Plan de travail](Draft_SelectPlane/fr.md)
-   [Draft Aimantation](Draft_Snap/fr.md)
-   [Expressions](Expressions/fr.md)
-   [Le format IFC](https://fr.wikipedia.org/wiki/Industry_Foundation_Classes)
-   [IfcOpenShell](http://ifcopenshell.org/)
-   [IfcPlusPlus](http://ifcplusplus.com/)
-   [Inkscape](http://www.inkscape.org)



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Manual:BIM modeling/fr
