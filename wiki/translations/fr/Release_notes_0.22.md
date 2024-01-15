# Release notes 0.22/fr
**FreeCAD 0.22 est en cours de développement, il n'y a pas encore de date de sortie prévue.**


{{Message|Des fonctions sont manquantes? Faites en part dans le fil du forum [https://forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;80197 Release notes for v0.22].

Voir [Contribuer à FreeCAD](Help_FreeCAD/fr.md) pour savoir comment contribuer à FreeCAD.
}}


{{Message|Toutes les images de cette page doivent utiliser le suffixe **_relnotes_0.22**}}




**FreeCAD 0.22** a été publié le **JJ MM 2024**, téléchargez la depuis la page [Téléchargement](Download/fr.md). Cette page liste toutes les nouvelles fonctions et les changements.

Les notes de versions plus anciennes de FreeCAD sont disponibles dans la [liste des notes de versions](Feature_list/fr#Notes_de_versions.md).

L\'endroit pour une image accrocheuse sélectionnée par les administrateurs sur le [forum des modèles des utilisateurs](https://forum.freecadweb.org/viewforum.php?f=24).



## Général



## Interface utilisateur 

+++
| <img alt="" src=images/Rotation_Center_Indicator_relnotes_0.22.gif  style="width:320px;"> | Un indicateur de centre de rotation a été ajouté. Cet indicateur s\'affiche lorsque la vue a pivoté en faisant glisser la souris. Il peut être désactivé dans les préférences. Il est également possible de régler sa couleur, sa transparence et sa taille. [Pull request #9909](https://github.com/FreeCAD/FreeCAD/pull/9909) et [Pull request #10790](https://github.com/FreeCAD/FreeCAD/pull/10790) |
+++

   
  <img alt="" src=images/Selection_filters_relnotes_0.22.gif  style="width:320px;">.Cliquez sur l\'image si l\'animation ne démarre pas.   Des filtres de sélection ont été ajoutés, facilitant la sélection des sommets, des arêtes et des faces. [Pull request #10271](https://github.com/FreeCAD/FreeCAD/pull/10271)
   

+++
| <img alt="" src=images/Tasks_Dockable_relnotes_0.22.png  style="width:320px;"> | Pour plus de flexibilité, le panneau des tâches est désormais un widget autonome et ancrable, mais l\'ancienne disposition est conservée par défaut. [Pull request #10681](https://github.com/FreeCAD/FreeCAD/pull/10681) et [Pull request #10848](https://github.com/FreeCAD/FreeCAD/pull/10848) |
+++

+++
| <img alt="" src=images/Transform_tool_relnotes_0.22.png  style="width:320px;"> | L\'apparence de l\'outil de déplacement [Transformer](Std_TransformManip/fr.md) a été améliorée. Il dispose maintenant aussi d\'un ensemble d\'outils de déplacement des objets le long des 3 plans par défaut. [Pull request #10706](https://github.com/FreeCAD/FreeCAD/pull/10706) |
+++

+++
| <img alt="" src=images/Overlay_relnotes_0.22.png  style="width:320px;"> | La fonction de Realthunder permettant la superposition des widgets d\'ancrage (transparence de la vue en arborescence et des tâches) a été ajoutée. [Pull request #7888](https://github.com/FreeCAD/FreeCAD/pull/7888) |
+++

+++
| <img alt="" src=images/Light_source_relnotes_0.22.PNG  style="width:320px;"> | La position de la source lumineuse peut désormais être définie dans les préférences (Préférences → Affichage). [Pull request #11146](https://github.com/FreeCAD/FreeCAD/pull/11146) |
+++

+++
| <img alt="" src=images/Preference_tree_relnotes_0.22.png  style="width:320px;"> | La fenêtre Préférences a été redessinée pour remplacer les onglets par une vue arborescente. [Pull request #11018](https://github.com/FreeCAD/FreeCAD/pull/11018) |
+++



### Autres améliorations de l\'interface utilisateur 

-   Un système d\'unités de projet a été introduit. [Pull request #9521](https://github.com/FreeCAD/FreeCAD/pull/9521)
-   L\'outil [Coupe persistante](Part_SectionCut/fr.md) fonctionne maintenant aussi dans une vue en perspective. [Pull request #10143](https://github.com/FreeCAD/FreeCAD/pull/10143)
-   Une option permettant de trier les ateliers par ordre alphabétique (disponible après un clic droit dans Préférences → Ateliers) a été ajoutée. [Pull request #10363](https://github.com/FreeCAD/FreeCAD/pull/10363)
-   Un filtre **Rechercher un fichier** et un filtre **Rechercher dans les fichiers** ont été ajoutés à la boîte de dialogue de [Std Exécuter une macro](Std_DlgMacroExecute/fr.md). [Pull request #10714](https://github.com/FreeCAD/FreeCAD/pull/10714)
-   Le [menu Affichage](Std_View_Menu/fr.md) et la barre d\'outils de l\'Affichage ont été révisés. [Pull request #10761](https://github.com/FreeCAD/FreeCAD/pull/10761)
-   Le bouton stop a été supprimé de la [barre d\'outils des macros](Macros/fr.md). Le bouton [Enregistrer](Std_DlgMacroRecord/fr.md) est désormais remplacé par un bouton d\'arrêt lorsque l\'enregistrement est en cours. [Pull request #10836](https://github.com/FreeCAD/FreeCAD/pull/10836)
-   Le bouton de réinitialisation dans les Préférences affiche maintenant un menu avec des options pour réinitialiser les paramètres à différents niveaux : tous, dans le groupe actuel ou dans l\'onglet actuel. [Pull request #10688](https://github.com/FreeCAD/FreeCAD/pull/10688) et [Pull request #11038](https://github.com/FreeCAD/FreeCAD/pull/11038)
-   Le module d\'Aide a été fusionné de sorte qu\'il n\'est plus nécessaire de télécharger une extension pour l\'utiliser. [Pull request #11008](https://github.com/FreeCAD/FreeCAD/pull/11008)
-   Des préférences pour personnaliser le thème utilisé ont été ajoutées. [Pull request #10238](https://github.com/FreeCAD/FreeCAD/pull/10238)
-   Les paramètres de sélection par défaut ont été modifiés pour faciliter la sélection des objets dans la fenêtre 3D. [Pull request #11187](https://github.com/FreeCAD/FreeCAD/pull/11187)
-   Un système d\'unités en mètres seulement nommé **Mètre décimal** a été ajouté car le système MKS (m/kg/s/degré) n\'entraîne pas toujours l\'affichage des dimensions en mètres - les millimètres sont toujours utilisés pour les valeurs inférieures à 0,1 m alors que pour certaines applications (par exemple le génie civil) un système d\'unités qui change l\'affichage de toutes les dimensions en mètres est utile. [Pull request #11365](https://github.com/FreeCAD/FreeCAD/pull/11365)
-   Des tailles de marqueurs supplémentaires (20, 25 et 30px) ont été ajoutées aux *Préférences → Affichage → Vue 3D → Taille des marqueurs* afin d\'aider les utilisateurs d\'écrans 4K. [Pull request #11524](https://github.com/FreeCAD/FreeCAD/pull/11524)
-   Une option *Basculer la transparence* a été ajoutée au menu Affichage et au menu contextuel pour activer ou désactiver rapidement la transparence des objets sélectionnés. [Pull request #10805](https://github.com/FreeCAD/FreeCAD/pull/10805)



## Noyau et API 



### Noyau

-   Les fonctions vectorielles de [Vector API](Vector_API/fr.md) peuvent maintenant être utilisées dans des [Expressions](Expressions/fr.md). [Pull request #8603](https://github.com/FreeCAD/FreeCAD/pull/10237).
-   La liste des fichiers dans la boîte de dialogue de [Std Exécuter une macro](Std_DlgMacroExecute/fr.md) peut maintenant être filtrée à la fois par le nom et le contenu du fichier. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/10714).
-   L\'éditeur Python fait désormais correspondre l\'indentation de la ligne précédente lorsque vous appuyez sur la touche Entrée. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/11356).

### API



#### Nouvelles API en Python 

-    {{Incode|getUpDirection}}: permet d\'obtenir la direction vers le haut d\'une vue View3DInventor. [Pull request #10060](https://github.com/FreeCAD/FreeCAD/pull/10060)



#### Suppression d\'API en Python 



## Gestionnaire des extensions 



## Atelier Arch 



### Autres améliorations de Arch 



## Atelier Draft 

-   Une option de justification et plusieurs propriétés connexes ont été ajoutées à [Draft Forme à partir d\'un texte](Draft_ShapeString/fr.md). [Pull request #10233](https://github.com/FreeCAD/FreeCAD/pull/10233)
-   Les [dimensions radiales](Draft_Dimension/fr#Utilisation_pour_une_dimension_radiale.md) n\'affichent plus qu\'une seule flèche. [Pull request #10655](https://github.com/FreeCAD/FreeCAD/pull/10655)
-   Une propriété Angle oblique a été ajoutée à [Draft Forme à partir d\'un texte](Draft_ShapeString/fr.md). [Pull request #10783](https://github.com/FreeCAD/FreeCAD/pull/10783)
-   La prise en charge des hyperliens a été ajoutée. Les hyperliens, vers des fichiers locaux et distants et des URL, des [Draft Textes](Draft_Text/fr.md) et [Draft Étiquettes](Draft_Label/fr.md) peuvent être ouverts à partir de leur menu contextuel de la [vue en arborescence](Tree_view/fr.md) ou de la [vue 3D](3D_view/fr.md). [Pull request #10878](https://github.com/FreeCAD/FreeCAD/pull/10878)
-   Le code de [Draft Plan de travail](Draft_SelectPlane/fr.md) a été retravaillé. Il y a maintenant un plan de travail par vue 3D. [Pull request #11010](https://github.com/FreeCAD/FreeCAD/pull/11010)
-   La fonction d\'historique et les options d\'alignement de la commande [Draft Plan de travail](Draft_SelectPlane/fr.md) ont été améliorées. [Pull request #11062](https://github.com/FreeCAD/FreeCAD/pull/11062)
-   Le comportement de la [grille](Draft_ToggleGrid/fr.md) a été amélioré. Sa visibilité est désormais stockée par vue 3D. Lors du passage à un autre atelier, toutes les grilles sont masquées (un paramètre [réglage fin](Fine-tuning/fr.md) est disponible pour désactiver cela). [Pull request #11336](https://github.com/FreeCAD/FreeCAD/pull/11336)
-   Les préférences de Draft ont été vérifiées et améliorées. Certaines préférences ont été ajoutées, des préférences obsolètes ont été supprimées. Les pages de l\'[éditeur de propriétés](Property_editor/fr.md) ont une nouvelle mise en page et affichent les unités le cas échéant. Il n\'est plus nécessaire de redémarrer FreeCAD après avoir modifié une préférence de Draft. [Pull request #11379](https://github.com/FreeCAD/FreeCAD/pull/11379), [Pull request #11503](https://github.com/FreeCAD/FreeCAD/pull/11503), [Pull request #11512](https://github.com/FreeCAD/FreeCAD/pull/11512), [Pull request #11550](https://github.com/FreeCAD/FreeCAD/pull/11550), [Pull request #11579](https://github.com/FreeCAD/FreeCAD/pull/11579), [Pull request #11585](https://github.com/FreeCAD/FreeCAD/pull/11585), [Pull request #11677](https://github.com/FreeCAD/FreeCAD/pull/11677) et [Pull request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694)



### Autres améliorations de Draft 

-   Les [Draft Surfaces liées](Draft_Facebinder/fr.md) peuvent maintenant gérer les faces appartenant à des liens et les faces imbriquées dans des [Std Parts](Std_Part/fr.md). [Pull request #11081](https://github.com/FreeCAD/FreeCAD/pull/11081)
-   Certains paramètres ont été ajoutés à la commande [Draft Définir le style](Draft_SetStyle/fr.md). [Pull request #11593](https://github.com/FreeCAD/FreeCAD/pull/11593) et [Pull request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694)
-   Des paramètres ont également été ajoutés à la commande [Draft Appliquer le style](Draft_ApplyStyle/fr.md). [Pull request #11610](https://github.com/FreeCAD/FreeCAD/pull/11610)
-   Les marqueurs d\'aimantation, d\'édition et de suivi utilisent désormais la préférence de la [taille des marqueurs](Preferences_Editor/fr#Vue_3D.md). [Pull request #11688](https://github.com/FreeCAD/FreeCAD/pull/11688)



## Atelier FEM 

+++
| <img alt="" src=images/FEM_legend_labels_relnotes_0.22.PNG  style="width:320px;"> | La position des étiquettes de la légende des couleurs a été ajustée pour que celles du haut soient moins susceptibles d\'être couvertes par le cube de navigation. La police et la couleur par défaut des étiquettes ont été modifiées pour augmenter la visibilité et des préférences ont été ajoutées pour permettre la modification de la couleur et de la taille des étiquettes. [Pull request #10552](https://github.com/FreeCAD/FreeCAD/pull/10552) |
+++

+++
| <img alt="" src=images/FEM_stress_component_linearization_relnotes_0.22.png  style="width:320px;"> | La commande [FEM Graphique de linéarisation des critères](FEM_PostFilterLinearizedStresses/fr.md) peut désormais utiliser les composantes du tenseur des contraintes pour les calculs de critères linéarisés. Auparavant, seules les critères de von Mises, de Tresca et les contraintes principales (majeures/intermédiaires/mineures) pouvaient être utilisées à cette fin. [Pull request #11724](https://github.com/FreeCAD/FreeCAD/pull/11724) |
+++



### Autres améliorations de FEM 

-   Le menu **Modèle → Contraintes sans solveur** a été supprimé de l\'interface graphique. Les contraintes listées ne pouvaient pas être utilisées. [Pull request #10457](https://github.com/FreeCAD/FreeCAD/pull/10457) et [Pull request #10459](https://github.com/FreeCAD/FreeCAD/pull/10459)
-   Le mot « contrainte » a été supprimé des noms et des descriptions de la plupart des fonctions de l\'atelier FEM afin de garantir une nomenclature correcte. Les noms ont été modifiés de manière à correspondre aux normes de l\'industrie de l\'analyse par éléments finis et à les rendre intuitifs pour les nouveaux utilisateurs. [Pull request #10519](https://github.com/FreeCAD/FreeCAD/pull/10519) et [Pull request #10799](https://github.com/FreeCAD/FreeCAD/pull/10799)
-   De nouvelles icônes ont été ajoutées pour le [Solveur CalculiX standard](FEM_SolverCalculixCxxtools/fr.md), [Réglage du solveur](FEM_SolverControl/fr.md) et [Résolution](FEM_SolverRun/fr.md) pour une plus grande intuitivité.
-   Le solveur CalculiX (expérimental) a été supprimé de l\'interface graphique car il n\'est pas terminé et inutile pour le moment. [Pull request #10823](https://github.com/FreeCAD/FreeCAD/pull/10823)
-   La disposition de certains panneaux de tâches des outils de post-traitement a été améliorée afin de réduire la taille de l\'espace horizontal qu\'ils occupaient. [Pull request #11066](https://github.com/FreeCAD/FreeCAD/pull/11066)
-   Le panneau de tâches de [FEM Condition limite de température](FEM_ConstraintTemperature/fr.md) a été retravaillé pour résoudre des problèmes lors de l\'édition de cette fonction. [Pull request #11126](https://github.com/FreeCAD/FreeCAD/pull/11126)
-   Un ancien problème avec le [FEM Filtre d\'écrêtage selon une ligne](FEM_PostFilterDataAlongLine/fr.md) ne pouvant tracer que la magnitude et non les composantes vectorielles d\'une variable de sortie sélectionnée a finalement été corrigé. [Pull request #10992](https://github.com/FreeCAD/FreeCAD/pull/10992)
-   La [FEM Charge d\'effort](FEM_ConstraintForce/fr.md) et la [FEM Charge de pression](FEM_ConstraintPressure/fr.md) ont été révisées afin d\'améliorer leur fonctionnement du côté du code source. [Pull request #10935](https://github.com/FreeCAD/FreeCAD/pull/10935) et [Pull request #10923](https://github.com/FreeCAD/FreeCAD/pull/10923)
-   Le [FEM Données au point](FEM_PostFilterDataAtPoint/fr.md) a maintenant une propriété PointSize pour définir la taille du symbole du point pour plus de visibilité. [Pull request #11054](https://github.com/FreeCAD/FreeCAD/pull/11054)
-   Pour plus de clarté, la commande de [FEM Région de maillage FEM](FEM_MeshRegion/fr.md) a été renommée en *Mailler plus finement FEM* dans l\'interface graphique (le nom de la commande reste inchangé). [Pull request #11489](https://github.com/FreeCAD/FreeCAD/pull/11489)



## Exportation



## Matériau

+++
| <img alt="" src=images/Materials_relnotes_0.22.PNG  style="width:320px;"> | Le système de gestion des matériaux, y compris l\'éditeur, a été entièrement retravaillé. D\'autres améliorations à cet égard suivront. [Pull request #10690](https://github.com/FreeCAD/FreeCAD/pull/10690) |
+++

+++
| <img alt="" src=images/Appearance_preview_relnotes_0.22.png  style="width:320px;"> | L\'aperçu de l\'apparence a été ajouté pour montrer les matériaux de la même manière qu\'ils seront montrés dans les documents. [Pull request #11628](https://github.com/FreeCAD/FreeCAD/pull/11628) |
+++

## Mesh



### Autres améliorations de Mesh 



## Atelier OpenSCAD 



### Autres améliorations de OpenSCAD 



## Atelier Part 

+++
| <img alt="" src=images/Part_scale_relnotes_0.22.PNG  style="width:320px;"> | L\'outil [Part Échelle](Part_Scale/fr.md) a été ajouté pour faciliter la mise à l\'échelle des formes sans avoir à utiliser les outils de l\'atelier Draft. [Pull request #10583](https://github.com/FreeCAD/FreeCAD/pull/10583) |
+++

+++
| <img alt="" src=images/Part_Mirror_relnotes_0.22.png  style="width:320px;"> | [Part Miroir](Part_Mirror/fr.md) prend désormais en charge les objets de référence, tel qu\'un [Part Plan](Part_Plane/fr.md) pour définir un plan miroir arbitraire en plus des plans XY, XZ et YZ standard. [Pull request #11535](https://github.com/FreeCAD/FreeCAD/pull/11535) |
+++



### Autres améliorations de Part 

-   La propriété *Frenet* est désormais activée par défaut pour l\'outil [Part Balayage](Part_Sweep/fr.md) afin d\'éviter un problème de rendu courant. [Pull request #11590](https://github.com/FreeCAD/FreeCAD/pull/11590)



## Atelier PartDesign 

+++
| <img alt="" src=images/Pad_task_dialog_relnotes_0.22.png  style="width:320px;"> | Les panneaux de tâches de [Protrusion](PartDesign_Pad/fr.md) et de [Cavité](PartDesign_Pocket/fr.md) ont été améliorés (réorganisation des éléments de l\'interface utilisateur. L\'option **Sélectionner une face** est cachée lorsqu\'elle n\'est pas nécessaire et ainsi de suite). [Pull request #10392](https://github.com/FreeCAD/FreeCAD/pull/10392) |
+++

+++
| <img alt="" src=images/Pattern_offset_mode_relnotes_0.22.png  style="width:320px;"> | Le mode décalage a été ajouté à [Répétition linéaire](PartDesign_LinearPattern/fr.md) et [Répétition circulaire](PartDesign_PolarPattern.md). Le mode précédent a été renommé **Longueur totale**. [Pull request #10377](https://github.com/FreeCAD/FreeCAD/pull/10377) |
+++



### Autres améliorations de PartDesign 

-   L\'option *Générer un évidement vers l\'intérieur* est maintenant activée par défaut pour l\'outil [Évidement](PartDesign_Thickness/fr.md). [Pull request #7488](https://github.com/FreeCAD/FreeCAD/pull/7488)



## Atelier Path 



### Autres améliorations de Path 



## Module Plot 



## Atelier Points 



### Autres améliorations de Points 



## Atelier Sketcher 

+++
| <img alt="" src=images/Arc_helper_relnotes_0.22.png  style="width:320px;"> | L\'implémentation d\'une superposition de cercles pour les arcs (pour résoudre le problème des contraintes apparaissant loin d\'eux) a été complétée avec une commande pour les interchanger. [Pull request #9703](https://github.com/FreeCAD/FreeCAD/pull/9703) |
+++

   
  <img alt="" src=images/Contextual_dimension_relnotes_0.22.gif  style="width:320px;">Cliquez sur l\'image si l\'animation ne démarre pas.   La contrainte de dimension contextuelle a été ajoutée pour permettre un dimensionnement rapide et intuitif à l\'aide d\'un seul outil polyvalent. [Pull request #9810](https://github.com/FreeCAD/FreeCAD/pull/9810)
   

   
  <img alt="" src=images/Tool_parameters_relnotes_0.22.gif  style="width:320px;">Cliquez sur l\'image si l\'animation ne démarre pas.   Des paramètres d\'outils ont été ajoutés pour permettre la cotation en déplacement (lors du dessin de formes). En fonction du réglage des préférences \"On-View-Parameters\", ils peuvent être désactivés, réduits aux dimensions uniquement (pas de coordonnées initiales) ou entièrement activés. De plus, des modes ont été ajoutés pour les outils de forme. Ils peuvent être sélectionnés à l\'aide de la touche M ou d\'une liste déroulante dans le panneau des tâches. Certains outils disposent de paramètres supplémentaires sous la forme de cases à cocher dans le panneau des tâches et de raccourcis clavier supplémentaires. Actuellement, les nouvelles fonctionnalités sont disponibles pour les points, les lignes, les arcs, les ellipses, les rectangles, les polygones et les rainures. En cours de réalisation. [Pull request #11048](https://github.com/FreeCAD/FreeCAD/pull/11048), [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) et suivants
   

+++
| <img alt="" src=images/Offset_relnotes_0.22.png  style="width:320px;"> | Un outil de [décalage](Sketcher_Offset/fr.md) a été ajouté pour permettre le décalage de courbes. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

+++
| <img alt="" src=images/Three_point_rectangle_relnotes_0.22.png  style="width:320px;"> | Le mode [rectangle](Sketcher_CompCreateRectangles/fr.md) à trois points a été ajouté en deux versions : 3 coins, centre ou 2 coins. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

+++
| <img alt="" src=images/Arc_slot_relnotes_0.22.png  style="width:320px;"> | Un outil de rainure en arc a été ajouté avec deux modes (extrémités en arc et extrémités plates) pour permettre la création de rainures courbes. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

   
  <img alt="" src=images/Auto_horizontal-vertical_relnotes_0.22.gif  style="width:320px;">Cliquez sur l\'image si l\'animation ne démarre pas.   Une contrainte horizontale/verticale a été ajoutée. Elle applique automatiquement une contrainte horizontale si une ligne est plus proche de l\'orientation horizontale ou une contrainte verticale si elle est plus proche de l\'orientation verticale. [Pull request #11538](https://github.com/FreeCAD/FreeCAD/pull/11538)
   

+++
| <img alt="" src=images/Angle_radius_rendering_relnotes_0.22.png  style="width:320px;"> | Le rendu des contraintes d\'angle et de rayon a été amélioré. Les contraintes d\'angle ont maintenant des lignes d\'extension complètes. [Pull request #11507](https://github.com/FreeCAD/FreeCAD/pull/11507) |
+++

+++
| <img alt="" src=images/Polar_transform_relnotes_0.22.png  style="width:320px;"> | Un outil de transformation polaire a été ajouté pour permettre la rotation et les motifs circulaires des géométries de l\'esquisse. [Pull request #11264](https://github.com/FreeCAD/FreeCAD/pull/11264) |
+++



### Autres améliorations de Sketcher 

-   Le mode cadre a été ajouté pour l\'outil Rectangle. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   Deux nouveaux modes ont été ajoutés pour l\'outil Ligne : « Point, longueur, angle » et « Point, largeur, hauteur ». [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   Les icônes de [Géométrie de construction](Sketcher_ToggleConstruction/fr.md) et de [Contraintes pilotantes](Sketcher_ToggleDrivingConstraint/fr.md) ont été modifiées. Désormais, la première n\'est plus aussi similaire à [Copie carbone](Sketcher_CarbonCopy/fr.md) et les deux icônes de basculement changent lorsqu\'on clique dessus. [Pull request #11500](https://github.com/FreeCAD/FreeCAD/pull/11500)
-   Les icônes du Sketcher ont été révisées afin d\'unifier leur apparence (largeur des traits, couleurs et taille des points). [Pull request #11785](https://github.com/FreeCAD/FreeCAD/pull/11785)
-   Une unification optionnelle (désactivée par défaut) de [Contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md) et [Contrainte point sur objet](Sketcher_ConstrainPointOnObject/fr.md) a été introduite. [Pull request #11494](https://github.com/FreeCAD/FreeCAD/pull/11494)



## Atelier Spreadsheet 



### Autres améliorations de Spreadsheet 



## Atelier Start 

+++
| <img alt="" src=images/Start_page_template_buttons_new_relnotes_0.22.PNG  style="width:320px;"> | Une section **Nouveau fichier** comprenant un certain nombre de boutons de démarrage rapide a été ajoutée à la page de démarrage. [Pull request #10171](https://github.com/FreeCAD/FreeCAD/pull/10171) |
+++

+++
| <img alt="" src=images/Start_page_layout_relnotes_0.22.png  style="width:320px;"> | La page d\'accueil a été revue. Elle est désormais plus moderne et plus cohérente. [Pull request #10391](https://github.com/FreeCAD/FreeCAD/pull/10391) |
+++



### Autres améliorations de Start 

-   La page des préférences de l\'atelier Start a été réorganisée. [Pull request #10520](https://github.com/FreeCAD/FreeCAD/pull/10520)
-   Il y a maintenant une option **CSS personnalisé** pour la page de démarrage qui vous permet de personnaliser le style CSS de la page de démarrage à partir des préférences de l\'atelier Start. [Pull request #10520](https://github.com/FreeCAD/FreeCAD/pull/10520)
-   La préférence **Masquer les barres de défilement** a été supprimée. Les barres de défilement de la page d\'accueil prenent le style en fonction du thème et sont beaucoup plus fines. [Pull request #10520](https://github.com/FreeCAD/FreeCAD/pull/10520)
-   Il y a maintenant des préférences pour cacher et changer la taille des icônes des vignettes des fichiers sur la page d\'accueil. [Pull request #10410](https://github.com/FreeCAD/FreeCAD/pull/10410)



## Atelier Surface 



### Autres améliorations de Surface 



## Atelier TechDraw 

+++
| <img alt="" src=images/TechDraw_cosmetic_circle_relnotes_0.22.png  style="width:320px;"> | L\'outil [Cercle cosmétique](TechDraw_CosmeticCircle/fr.md) a été ajouté pour permettre la création de cercles cosmétiques en sélectionnant le centre et en saisissant le rayon. [Pull request #10763](https://github.com/FreeCAD/FreeCAD/pull/10763) |
+++

+++
| <img alt="" src=images/Arc_length_relnotes_0.22.PNG  style="width:320px;"> | L\'outil [Longueur d\'arc d\'arêtes](TechDraw_ExtensionArcLengthAnnotation/fr.md) a été ajouté pour créer des annotations de type dimensionnel de la longueur d\'arc d\'arêtes sélectionnées. [Pull request #11532](https://github.com/FreeCAD/FreeCAD/pull/11532) |
+++

+++
| <img alt="" src=images/Offset_vertex_relnotes_0.22.png  style="width:320px;"> | L\'outil [Sommets décalés](TechDraw_CommandAddOffsetVertex/fr.md) a été ajouté pour créer des sommets cosmétiques en décalage par rapport aux sommets sélectionnés. [Pull request #11655](https://github.com/FreeCAD/FreeCAD/pull/11655) |
+++



### Autres améliorations de TechDraw 

-   Les sections basées sur d\'autres sections utilisent désormais par défaut la forme originale (non coupée). Ceci peut être modifié dans les paramètres de la section pour utiliser la section précédente à la place. [Pull request #10281](https://github.com/FreeCAD/FreeCAD/pull/10281)
-   Les objets cosmétiques et les lignes centrales peuvent désormais être supprimés en les sélectionnant et en appuyant sur la touche Suppr. Auparavant, cela entraînait la suppression de la vue entière. [Pull request #10695](https://github.com/FreeCAD/FreeCAD/pull/10695) et [Pull request #10813](https://github.com/FreeCAD/FreeCAD/pull/10813)
-   Une nouvelle icône plus intuitive a été ajoutée pour l\'outil [Soudure](TechDraw_WeldSymbol/fr.md). [Pull request #10936](https://github.com/FreeCAD/FreeCAD/pull/10936)
-   Le comportement du mode point + arête de l\'outil [Cote de longueur](TechDraw_LengthDimension/fr.md) a été corrigé. [Pull request #10860](https://github.com/FreeCAD/FreeCAD/pull/10860)
-   Un état vérifié a été ajouté pour le bouton [Bascule des cadres](TechDraw_ToggleFrame/fr.md) afin qu\'un utilisateur puisse voir si le bouton est activé ou non. [Pull request #11240](https://github.com/FreeCAD/FreeCAD/pull/11240)
-   Le comportement de l\'outil [Apparence des lignes](TechDraw_DecorateLine/fr.md) a été amélioré. Maintenant, double-cliquer sur une ligne appelle cet outil. Et les styles de lignes sont correctement restaurés si l\'utilisateur appuie sur « Annuler ». Auparavant, il n\'y avait aucune différence entre appuyer sur « OK » et « Annuler ». [Pull request #11188](https://github.com/FreeCAD/FreeCAD/pull/11188)
-   La couleur et la transparence des faces peuvent désormais être définies par vue. [Pull request #11315](https://github.com/FreeCAD/FreeCAD/pull/11315)
-   Le mode multisélection a été ajouté et peut être activé dans les préférences. Dans ce mode, plusieurs sommets, arêtes et faces peuvent être sélectionnés en cliquant dessus avec le bouton gauche de la souris, sans avoir à maintenir la touche Ctrl enfoncée. [Pull request #11417](https://github.com/FreeCAD/FreeCAD/pull/11417)
-   [Surface](TechDraw_ExtensionAreaAnnotation/fr.md) peut maintenant calculer les surfaces de faces arbitraires. [Pull request #11473](https://github.com/FreeCAD/FreeCAD/pull/11473)
-   Les lignes non continues suivront désormais les normes ISO/ANSI au lieu du style des lignes de Qt. Une nouvelle préférence a été ajoutée pour sélectionner la norme. [Pull request #11594](https://github.com/FreeCAD/FreeCAD/pull/11594)
-   Le comportement de l\'outil [Cote axonométrique](TechDraw_AxoLengthDimension/fr.md) a été amélioré. Désormais, lors de la cotation d\'arêtes parallèles aux axes du système de coordonnées global, la valeur réelle (3D) est calculée automatiquement et insérée dans la propriété Format Spec (sous forme de texte). [Pull request #11678](https://github.com/FreeCAD/FreeCAD/pull/11678)
-   L\'outil [Position d\'une vue en coupe](TechDraw_ExtensionPositionSectionView/fr.md) peut maintenant être utilisé en sélectionnant une arête dans une vue de coupe et un sommet dans la vue source. [Pull request #11797](https://github.com/FreeCAD/FreeCAD/pull/11797)



## Atelier Web 



### Autres améliorations de Web 

## Compilation



## Limitations connues



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.22/fr
