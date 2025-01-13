# Release notes 1.0/fr
**FreeCAD 1.0** a été publié le **18 novembre 2024**. Vous pouvez l\'obtenir depuis la page [Téléchargement](Download/fr.md). Cette page liste toutes les nouvelles fonctionnalités et changements.

Les notes de versions plus anciennes de FreeCAD sont disponibles dans la [liste des notes de versions](Feature_list/fr#Notes_de_versions.md).



## En mémoire de : Bradley McLean (bgbsww) 

Bien que nous soyons ravis de vous présenter cette nouvelle version, nous sommes également tristes d\'annoncer que notre ami et développeur prolifique de FreeCAD [bgbsww](https://github.com/bgbsww) est décédé quelques semaines avant la sortie de cette version. Il était l\'un des principaux architectes de l\'effort de correction du nommage topologique, a écrit beaucoup de code et de tests supplémentaires, et était devenu le spécialiste du TNP de FreeCAD. Il a également aidé pratiquement tous les autres développeurs à s\'adapter au nouvel algorithme. Cette version lui est dédiée.



## Général

+++
| <img alt="" src=images/TNP_fix_relnotes_1.0.PNG  style="width:320px;"> | Le très vieux problème du [Problème de dénomination topologique](Topological_naming_problem/fr.md) a finalement été corrigé grâce aux efforts conjoints et au travail acharné de plusieurs développeurs. L\'[algorithme de Realthunder](https://github.com/realthunder/FreeCAD_assembly3/wiki/Topological-Naming-Algorithm) a été soigneusement implémentée et améliorée pour fonctionner dans la version maître de FreeCAD. Le projet a duré plus d\'un an, et la mise en œuvre initiale a été finalisée avec la PR suivante qui intègre les améliorations. Le problème de dénomination topologique n\'est pas complètement résolu et d\'autres améliorations seront apportées dans la prochaine version. [Pull request #13705](https://github.com/FreeCAD/FreeCAD/pull/13705) |
+++

   
  <img alt="" src=images/AssemblyExample_relnotes_1.0.png  style="width:320px;">.   FreeCAD dispose d\'un nouvel [atelier Assembly](Assembly_Workbench/fr.md) intégré. Il est basé sur ce que nous appelions *[l\'autre FreeCAD](https://www.askoh.com/freecad/what_is_freecad/index.html)*, un autre logiciel également nommé FreeCAD, comportant des capacités de simulation de mouvement. Il fut créé en même temps que le nôtre. Le portage a été effectué par l\'auteur lui-même, [Dr. Aik-Siong Koh](https://www.askoh.com). Grâce à cette avancée spectaculaire, les deux FreeCAD sont enfin unis. Lisez ci-dessous pour [plus d\'informations](#Atelier_Assembly.md). [Pull request #10427](https://github.com/FreeCAD/FreeCAD/pull/10427)
   

+++
| <img alt="" src=images/Freecad.svg  style="width:320px;"> | FreeCAD a un nouveau logo. Le lauréat a été sélectionné parmi 5 finalistes. Des directives d\'utilisation et un kit de logo sont disponibles sur la page [FreeCAD brand guidelines page](https://fpa.freecad.org/handbook/process/logo.html). [Pull request #14284](https://github.com/FreeCAD/FreeCAD/pull/14284) |
+++



## Interface utilisateur 

+++
| <img alt="" src=images/Rotation_Center_Indicator_relnotes_1.0.gif  style="width:320px;"> | Un indicateur de centre de rotation a été ajouté. Cet indicateur s\'affiche lorsque la vue a pivoté en faisant glisser la souris. Il peut être désactivé dans les préférences. Il est également possible de régler sa couleur, sa transparence et sa taille. [Pull request #9909](https://github.com/FreeCAD/FreeCAD/pull/9909) et [Pull request #10790](https://github.com/FreeCAD/FreeCAD/pull/10790) |
+++

   
  <img alt="" src=images/Selection_filters_relnotes_1.0.gif  style="width:320px;">.Cliquez sur l\'image si l\'animation ne démarre pas.   Des [filtres](Part_SelectFilter/fr.md) ont été ajoutés, facilitant la sélection des sommets, des arêtes et des faces. [Pull request #10271](https://github.com/FreeCAD/FreeCAD/pull/10271)
   

+++
| <img alt="" src=images/Tasks_Dockable_relnotes_1.0.png  style="width:320px;"> | Pour plus de flexibilité, le panneau des tâches est désormais un widget autonome. Il peut être [ancré](Combo_view#Dock_Task_panel_on_top_of_Combo_view.md) au-dessus de la vue combinée pour obtenir la disposition compacte des versions précédentes. [Pull request #10681](https://github.com/FreeCAD/FreeCAD/pull/10681) et [Pull request #10848](https://github.com/FreeCAD/FreeCAD/pull/10848) |
+++

+++
| <img alt="" src=images/Transform_tool_relnotes_1.0.png  style="width:320px;"> | L\'apparence de l\'outil de déplacement [Transformer](Std_TransformManip/fr.md) a été améliorée. Il dispose maintenant aussi d\'un ensemble d\'outils de déplacement des objets le long des 3 plans par défaut. [Pull request #10706](https://github.com/FreeCAD/FreeCAD/pull/10706) |
+++

+++
| <img alt="" src=images/Overlay_relnotes_1.0.png  style="width:320px;"> | La fonction de Realthunder permettant la superposition des widgets d\'ancrage (transparence de la vue en arborescence et des tâches) a été ajoutée. [Pull request #7888](https://github.com/FreeCAD/FreeCAD/pull/7888) |
+++

+++
| <img alt="" src=images/Light_source_relnotes_1.0.png  style="width:320px;"> | La position de la source lumineuse peut désormais être définie dans les préférences (*Préférences → Affichage*). [Pull request #11146](https://github.com/FreeCAD/FreeCAD/pull/11146) et [Pull request #15877](https://github.com/FreeCAD/FreeCAD/pull/15877) |
+++

+++
| <img alt="" src=images/Preference_tree_relnotes_1.0.png  style="width:320px;"> | La fenêtre Préférences a été redessinée pour remplacer les onglets par une vue arborescente. [Pull request #11018](https://github.com/FreeCAD/FreeCAD/pull/11018) |
+++

+++
| <img alt="" src=images/TabBar_relnotes_1.0.png  style="width:320px;"> | Un sélecteur d\'atelier pour la barre d\'onglets a été ajouté. Il peut être activé et configuré dans *Préférences → Ateliers*. [Pull request #12270](https://github.com/FreeCAD/FreeCAD/pull/12270) |
+++

+++
| <img alt="" src=images/Unified_measurement_relnotes_1.0.PNG  style="width:320px;"> | Un nouvel [outil de mesure universel](Std_Measure/fr.md) a été ajouté, remplaçant les anciens [outils de mesure de Part](Part_Workbench/fr#Mesure.md). [Pull request #9750](https://github.com/FreeCAD/FreeCAD/pull/9750) et suivant |
+++

   
  <img alt="" src=images/Normal_view_relnotes_1.0.gif  style="width:320px;">Cliquez sur l\'image si l\'animation ne démarre pas.   L\'outil [Aligner sur la sélection](Std_AlignToSelection/fr.md) a été ajouté, ce qui permet de saisir des vues normales aux faces ou suivant des directions d\'arêtes. [Pull request #13906](https://github.com/FreeCAD/FreeCAD/pull/13906)
   



### Autres améliorations de l\'interface utilisateur 

-   Un système d\'unités de projet a été introduit. [Pull request #9521](https://github.com/FreeCAD/FreeCAD/pull/9521)
-   L\'outil [Coupe persistante](Part_SectionCut/fr.md) fonctionne maintenant aussi dans une vue en perspective. [Pull request #10143](https://github.com/FreeCAD/FreeCAD/pull/10143)
-   Une option permettant de trier les ateliers par ordre alphabétique (disponible après un clic droit dans *Préférences → Ateliers*) a été ajoutée. [Pull request #10363](https://github.com/FreeCAD/FreeCAD/pull/10363)
-   Un filtre **Rechercher un fichier** et un filtre **Rechercher dans les fichiers** ont été ajoutés à la fenêtre de dialogue de [Std Exécuter une macro](Std_DlgMacroExecute/fr.md). [Pull request #10714](https://github.com/FreeCAD/FreeCAD/pull/10714)
-   Le [menu Affichage](Std_View_Menu/fr.md) et la barre d\'outils de l\'Affichage ont été révisés. [Pull request #10761](https://github.com/FreeCAD/FreeCAD/pull/10761)
-   Le bouton stop a été supprimé de la [barre d\'outils des macros](Macros/fr.md). Le bouton [Enregistrer](Std_DlgMacroRecord/fr.md) est désormais remplacé par un bouton d\'arrêt lorsque l\'enregistrement est en cours. [Pull request #10836](https://github.com/FreeCAD/FreeCAD/pull/10836)
-   Le bouton de réinitialisation dans les Préférences affiche maintenant un menu avec des options pour réinitialiser les paramètres à différents niveaux : tous, dans le groupe actuel ou dans l\'onglet actuel. [Pull request #10688](https://github.com/FreeCAD/FreeCAD/pull/10688) et [Pull request #11038](https://github.com/FreeCAD/FreeCAD/pull/11038)
-   Le module d\'Aide a été fusionné de sorte qu\'il n\'est plus nécessaire de télécharger une extension pour l\'utiliser. [Pull request #11008](https://github.com/FreeCAD/FreeCAD/pull/11008)
-   Des préférences pour personnaliser le thème utilisé ont été ajoutées. [Pull request #10238](https://github.com/FreeCAD/FreeCAD/pull/10238)
-   Les paramètres de sélection par défaut ont été modifiés pour faciliter la sélection des objets dans la fenêtre 3D. [Pull request #11187](https://github.com/FreeCAD/FreeCAD/pull/11187)
-   Un système d\'unités en mètres seulement nommé **Mètre décimal** a été ajouté car le système MKS (m/kg/s/degré) n\'entraîne pas toujours l\'affichage des dimensions en mètres - les millimètres sont toujours utilisés pour les valeurs inférieures à 0,1 m alors que pour certaines applications (par exemple le génie civil) un système d\'unités qui change l\'affichage de toutes les dimensions en mètres est utile. [Pull request #11365](https://github.com/FreeCAD/FreeCAD/pull/11365)
-   Des tailles de marqueurs supplémentaires (20, 25 et 30px) ont été ajoutées aux *Préférences → Affichage → Vue 3D → Taille des marqueurs* afin d\'aider les utilisateurs d\'écrans 4K. [Pull request #11524](https://github.com/FreeCAD/FreeCAD/pull/11524)
-   Une option *Basculer la transparence* a été ajoutée au menu Affichage et au menu contextuel pour activer ou désactiver rapidement la transparence des objets sélectionnés. [Pull request #10805](https://github.com/FreeCAD/FreeCAD/pull/10805)
-   Une commande Verrouiller les barres d\'outils a été ajoutée. Elle permet de verrouiller ou de déverrouiller les positions des barres d\'outils. Elle est disponible dans le menu Affichage et dans le menu contextuel de la barre d\'outils. [Pull request #11596](https://github.com/FreeCAD/FreeCAD/pull/11596)
-   La couleur de la forme par défaut a été ajustée pour améliorer l\'apparence des modèles. [Pull request #12380](https://github.com/FreeCAD/FreeCAD/pull/12380) et [Pull request #12488](https://github.com/FreeCAD/FreeCAD/pull/12488)
-   Les éléments dans les conteneurs de pièces et de groupes peuvent maintenant être triés par glisser-déposer. [Pull request #12293](https://github.com/FreeCAD/FreeCAD/pull/12293)
-   Les icônes de visibilité (symbole de l\'œil) sont ajoutées aux objets de l\'arborescence si l\'option Afficher l\'icône de visibilité est cochée dans *Préférences → Affichage → Interface utilisateur*. [Pull request #12298](https://github.com/FreeCAD/FreeCAD/pull/12298)
-   Un statut de [figeage](Std_ToggleFreeze/fr.md) (option *Activer/désactiver le figeage* dans le menu contextuel de la [vue en arborescence](Tree_view/fr.md)) a été ajouté, permettant de désactiver le comportement paramétrique d\'un objet (de sorte qu\'il ne change pas même si les objets dont il dépend changent). [Pull request #12580](https://github.com/FreeCAD/FreeCAD/pull/12580)
-   Une propriété *Supprimé* a été ajoutée pour désactiver temporairement une fonction. Actuellement, elle est cachée dans l\'atelier PartDesign (cliquez avec le bouton droit de la souris dans l\'[éditeur de propriétés](Property_editor/fr.md) et sélectionnez *Afficher tout* pour la voir) jusqu\'à ce que la correction du [problème de dénomination topologique](Topological_naming_problem/fr.md) soit terminée. [Pull request #12096](https://github.com/FreeCAD/FreeCAD/pull/12096) et [Pull request #12412](https://github.com/FreeCAD/FreeCAD/pull/12412)
-   Les animations de navigation ont été améliorées. Les animations utilisent maintenant une fonction de facilitation et ont une durée fixe qui peut être modifiée dans *Préférences → Affichage → Navigation*. [Pull request #10881](https://github.com/FreeCAD/FreeCAD/pull/10881) et [Pull request #12205](https://github.com/FreeCAD/FreeCAD/pull/12205)
-   Les boutons pour les vues par défaut sont maintenant regroupés sous un seul bouton. Les boutons individuels sont toujours disponibles dans la barre d\'outils supplémentaire *Vues individuelles*. [Pull request #12878](https://github.com/FreeCAD/FreeCAD/pull/12878)
-   Le nom du document actif est maintenant également affiché dans la barre de titre de la fenêtre. [Pull request #12035](https://github.com/FreeCAD/FreeCAD/pull/12035)
-   Une commande pour afficher le panneau de l\'[éditeur de propriétés](Property_editor/fr.md) a été ajoutée. [Pull request #12024](https://github.com/FreeCAD/FreeCAD/pull/12024)
-   L\'intégration des périphériques 3Dconnexion avec FreeCAD sous Windows a été améliorée. [Pull request #12929](https://github.com/FreeCAD/FreeCAD/pull/12929)
-   Une fonction de mesure rapide a été ajoutée. Elle utilise la [barre d\'état](Status_bar/fr.md) pour afficher les principales informations de mesure (longueur des arêtes, surface des faces, distance/angle entre les points/arêtes et rayon des arêtes circulaires/faces cylindriques) concernant la sélection en cours dans la vue 3D. [Pull request #12217](https://github.com/FreeCAD/FreeCAD/pull/12217)
-   Les barres d\'outils peuvent désormais être glissées et déposées dans les barres d\'état et de menu. [Pull request #13571](https://github.com/FreeCAD/FreeCAD/pull/13571)
-   Un bouton *Recharger la feuille de style* a été ajouté pour faciliter le développement des feuilles de style. Il ne fait partie d\'aucune barre d\'outils par défaut, il doit être ajouté manuellement depuis *Outils → Personnaliser → Barres d\'outils → Vue*. [Pull request #13982](https://github.com/FreeCAD/FreeCAD/pull/13982)
-   Les icônes des documents (y compris celles de [Ouvrir](Std_Open/fr.md) et [Enregistrer](Std_Save/fr.md), entre autres) ont été améliorées et unifiées. [Pull request #13865](https://github.com/FreeCAD/FreeCAD/pull/13865)
-   L\'icône [Std Tout afficher](Std_ViewFitAll/fr.md) a été remplacée pour plus de clarté. [Pull request #14180](https://github.com/FreeCAD/FreeCAD/pull/14180)
-   Plusieurs icônes (telles que [Std Nouveau](Std_New/fr.md)) ont été améliorées. [Pull request #14278](https://github.com/FreeCAD/FreeCAD/pull/14278), [Pull request #14434](https://github.com/FreeCAD/FreeCAD/pull/14434) et [Pull request #14154](https://github.com/FreeCAD/FreeCAD/pull/14154)
-   Les icônes des en-têtes des panneaux de tâches Sketcher et PartDesign ont été améliorées. [Pull request #13968](https://github.com/FreeCAD/FreeCAD/pull/13968)
-   En mode [FreeCAD sans GUI](Headless_FreeCAD/fr.md), la console interactive Python propose désormais la complétion par tabulation, à condition que le module [readline](https://docs.python.org/3/library/readline.html) soit disponible. [Pull request #14213](https://github.com/FreeCAD/FreeCAD/pull/14213)
-   Une option permettant d\'afficher les noms internes dans l\'arborescence a été ajoutée. Elle est désactivée par défaut et peut être activée dans *Préférences → Affichage → Interface utilisateur → Masquer les noms internes*. [Pull request #14237](https://github.com/FreeCAD/FreeCAD/pull/14237)
-   Le bouton Aide a été supprimé des Préférences car il n\'était pas fonctionnel. [Pull request #14695](https://github.com/FreeCAD/FreeCAD/pull/14695)
-   Les feuilles de style par défaut ont été améliorées de manière significative et sont désormais proposées dans deux variantes autres que classique - clair et sombre. [Pull request #13772](https://github.com/FreeCAD/FreeCAD/pull/13772)
-   Les pages Thème et Interface utilisateur du groupe Affichage des préférences ont été réorganisées et combinées. Certaines préférences ont été déplacées vers la nouvelle page Avancé. [Pull request #14974](https://github.com/FreeCAD/FreeCAD/pull/14974)
-   Les préférences de vérification et d\'amélioration cosmétique de Part/PartDesign sont désormais activées par défaut. [Pull request #14406](https://github.com/FreeCAD/FreeCAD/pull/14406)
-   Un nouveau paramètre a été ajouté **BaseApp/Preferences/Bitmaps/Theme/UseIconTheme** (booléen) : mis à true pour forcer Qt à utiliser les icônes du thème d\'icônes du système. La valeur par défaut est false pour que FreeCAD utilise ses propres icônes. Cela n\'affecte pas les autres mécanismes de thème d\'icônes de Qt tels que les boîtes de dialogue du système, les boutons et autres. Ceux-ci devraient toujours utiliser les icônes du thème du système. [Pull request #16018](https://github.com/FreeCAD/FreeCAD/pull/16018).
-   Les informations sur les feuilles de style, les thèmes et les QtStyle sont maintenant incluses dans *Aide → À propos de FreeCAD*. [Pull request #16281](https://github.com/FreeCAD/FreeCAD/pull/16281)
-   L\'écran d\'accueil est maintenant sélectionné aléatoirement au démarrage à partir de plusieurs images, y compris des modèles d\'utilisateurs et des présentations de certaines extensions. [Pull request #16071](https://github.com/FreeCAD/FreeCAD/pull/16071)
-   Un mode sans échec a été ajouté et peut être activé via *Aide → Redémarrer en mode sans échec*. Il désactive temporairement les configurations de l\'utilisateur, les modules complémentaires, les thèmes et autres personnalisations pour exécuter FreeCAD dans un état de \"réinitialisation d\'usine\" pour le débogage. [Pull request #16858](https://github.com/FreeCAD/FreeCAD/pull/16858)



## Changement de format des fichiers 

Bien que des précautions aient été prises pour garantir que les fichiers créés avec la nouvelle version 1.0 puissent encore être ouverts dans les versions antérieures de FreeCAD, certaines nouvelles fonctionnalités introduites dans la version 1.0 ne peuvent pas être comprises par les versions antérieures. Elles peuvent entraîner la rupture des modèles sauvegardés avec la version 1.0 ou présenter des problèmes lorsqu\'ils sont ouverts dans des versions antérieures de FreeCAD. Voici un résumé des problèmes que vous pourriez rencontrer et leur solution. La communauté du forum peut également vous aider à résoudre les problèmes de compatibilité.

-   la propriété **Attachment** a été renommée **AttachmentSupport**. Cela signifie que les fonctions reposant sur cette propriété (notamment les modèles utilisant l\'extension Assembly4) devront être corrigées pour être ouvertes dans une version antérieure de FreeCAD. Une [macro est disponible ici](Macro_Convert_021/fr.md) pour corriger ces fichiers.



## Noyau et API 



### Noyau

-   Les fonctions vectorielles de [Vector API](Vector_API/fr.md) peuvent maintenant être utilisées dans des [Expressions](Expressions/fr.md). [Pull request #8603](https://github.com/FreeCAD/FreeCAD/pull/10237).
-   L\'éditeur en Python prend désormais en compte l\'indentation de la ligne précédente lorsque l\'on appuie sur la touche Entrée. [Pull request #11356](https://github.com/FreeCAD/FreeCAD/pull/11356).
-   Le nom de la propriété contenant le(s) objet(s) de référence d\'une pièce jointe a changé de **Support** à **AttachmentSupport**. [Pull request #12714](https://github.com/FreeCAD/FreeCAD/pull/12714).
-   Un conteneur de propriétés, App::VarSet, a été introduit comme fonctionnalité de base. Un VarSet permet aux utilisateurs de définir des propriétés qui peuvent être utilisées dans les modèles tout comme les alias de feuilles de calcul et les autres conteneurs de propriétés précédents (Dynamic Data, Path PropertyBags et Assembly 4 Variables). [Pull Request #12135](https://github.com/FreeCAD/FreeCAD/pull/12135)

### API



#### Nouvelles API en Python 

-    {{Incode|getUpDirection}}: permet d\'obtenir la direction vers le haut d\'une vue View3DInventor. [Pull request #10060](https://github.com/FreeCAD/FreeCAD/pull/10060)



#### API en Python changée 

-   Pour sauvegarder/restaurer des données personnalisées à partir d\'une fonction en Python, les méthodes jusque là appelées {{Incode|__getstate__}}/{{Incode|__setstate__}} ont été renommées en {{Incode|dumps}}/{{Incode|loads}}. Ceci est dû à des changements internes à Python-3.11. [Pull request #10769](https://github.com/FreeCAD/FreeCAD/pull/10769) et [Pull request #12243](https://github.com/FreeCAD/FreeCAD/pull/12243).

## Start

L\'atelier Start a été remplacé par une page Start, une application basée sur des QtWidgets. Elle peut être affichée en utilisant l\'option *Aide → Start*. [Pull request #13134](https://github.com/FreeCAD/FreeCAD/pull/13134)

Les deux premiers pull requests mentionnés ci-dessous appartiennent à l\'atelier Start mais ont influencé la conception de la page Start.

+++
| <img alt="" src=images/Start_page_template_buttons_new_relnotes_1.0.png  style="width:320px;"> | Une section **Nouveau fichier** comprenant un certain nombre de boutons de démarrage rapide a été ajoutée à la page de démarrage. [Pull request #10171](https://github.com/FreeCAD/FreeCAD/pull/10171) |
+++

+++
| <img alt="" src=images/Start_page_layout_relnotes_1.0.png  style="width:320px;"> | La page d\'accueil a été revue. Elle est désormais plus moderne et plus cohérente. [Pull request #10391](https://github.com/FreeCAD/FreeCAD/pull/10391) |
+++

+++
| <img alt="" src=images/First_start_relnotes_1.0.png  style="width:320px;"> | Un widget simple au démarrage a été ajouté et sera étendu dans un futur proche. [Pull request #13650](https://github.com/FreeCAD/FreeCAD/pull/13650) |
+++



## Atelier Assembly 

+++
| <img alt="" src=images/Assembly_relnotes_1.0.png  style="width:320px;"> | Un [atelier Assembly](Assembly_Workbench/fr.md) intégré a finalement été ajouté à FreeCAD. Il utilise le [solveur d\'Ondsel](https://github.com/Ondsel-Development/OndselSolver) open-source. Les fonctions de base (joints) sont déjà disponibles. D\'autres développements sont en cours. [Pull request #10427](https://github.com/FreeCAD/FreeCAD/pull/10427), [Pull request #10764](https://github.com/FreeCAD/FreeCAD/pull/10764), [Pull request #12406](https://github.com/FreeCAD/FreeCAD/pull/12406) et plus encore. |
+++



### Autres améliorations d\'Assembly 

-   Une [vue éclatée](Assembly_CreateView/fr.md) a été ajoutée. [Pull request #12419](https://github.com/FreeCAD/FreeCAD/issues/12419)
-   Les icônes d\'Assembly ont été mises à jour et les fonctions expérimentales sont mises à disposition. [Pull request #13866](https://github.com/FreeCAD/FreeCAD/pull/13866)
-   Les liaisons d\'angle, perpendiculaire et parallèle ont été ajoutées. [Pull request #14008](https://github.com/FreeCAD/FreeCAD/pull/14008)
-   Une fonction de [nomenclature](Assembly_CreateBom/fr.md) a été ajoutée. [Pull request #14198](https://github.com/FreeCAD/FreeCAD/pull/14198)
-   La prise en charge du code permettant d\'atténuer le [problème de dénomination topologique](Topological_naming_problem/fr.md) a été ajoutée. [Pull request #14674](https://github.com/FreeCAD/FreeCAD/pull/14674)
-   La prise en charge des sous-ensembles amovibles a été ajoutée. Les sous-assemblages ajoutés à un assemblage parent peuvent être définis comme rigides (une unité solide) ou amovibles (permettant le mouvement de chaque composant). Des étapes manuelles sont nécessaires pour les sous-ensembles ajoutés au cours du cycle de développement avant la fusion de cette fonction. Ces assemblages devront être supprimés et réajoutés à leur assemblage parent. [Pull request #15629](https://github.com/FreeCAD/FreeCAD/pull/15629)



## Atelier BIM 

+++
| <img alt="" src=images/bim_relnotes_1.0.png  style="width:320px;"> | L\'atelier Arch a finalement été fusionné avec [BIM](BIM_Workbench/fr.md), devenant ainsi le nouvel atelier BIM. Ce nouvel atelier BIM conserve tous les outils d\'Arch et en ajoute quelques autres. Il apporte de nombreuses améliorations à l\'ensemble du flux de travail BIM et de la conception architecturale, ainsi que de meilleurs outils de configuration et de gestion, plus un meilleur support IFC. [Pull request #13783](https://github.com/FreeCAD/FreeCAD/pull/13783) |
+++



### Autres améliorations de BIM 

-   Venant de l\'atelier BIM, certains outils Arch \"tout-en-un\" ont été divisés en différents cas d\'utilisation. L\'outil [Arch Partie de bâtiment](Arch_BuildingPart/fr.md) a été divisé en deux outils : [BIM Bâtiment](Arch_Building/fr.md) et [BIM Niveau](Arch_Floor/fr.md). L\'outil [Arch Structure](Arch_Structure/fr.md) a été divisé en [BIM Colonne](BIM_Column/fr.md), [BIM Poutre](BIM_Beam/fr.md) et [BIM Dalle](BIM_Slab/fr.md). L\'outil [Arch Fenêtre](Arch_Window/fr.md) a été divisé en [BIM Fenêtre](Arch_Window/fr.md) et [BIM Porte](BIM_Door/fr.md). En interne, ces outils produisent toujours le même objet, mais avec des types IFC différents et des préréglages appliqués. [Pull request #13783](https://github.com/FreeCAD/FreeCAD/pull/13783)
-   [NativeIFC](https://github.com/yorikvanhavre/FreeCAD-NativeIFC) a également été fusionné dans le nouvel atelier BIM. Avec NativeIFC, vous pouvez désormais travailler sur des fichiers IFC dans FreeCAD de manière native, sans plus de traduction vers et depuis le format de fichier FreeCAD. Plus d\'informations sur la page [NativeIFC](NativeIFC/fr.md). [Pull request #13783](https://github.com/FreeCAD/FreeCAD/pull/13783)
-   La commande [Arch Couper selon un plan](Arch_CutPlane/fr.md) a été améliorée. Elle prend désormais en compte l\'imbrication et les liens et la sélection est plus souple. Les arêtes peuvent également être sélectionnés, ce qui rend la commande Arch Couper suivant une ligne obsolète. [Pull request #11254](https://github.com/FreeCAD/FreeCAD/pull/11254) et [Pull request #11792](https://github.com/FreeCAD/FreeCAD/pull/11792)
-   Les préférences de BIM ont été vérifiées et améliorées. Les pages de [réglage des préférences](Preferences_Editor/fr.md) ont une nouvelle présentation. [Pull request #11940](https://github.com/FreeCAD/FreeCAD/pull/11940) et [Pull request #12038](https://github.com/FreeCAD/FreeCAD/pull/12038)
-   Un préréglage *Ouverture seulement* a été ajouté à la commande [Arch Fenêtre](Arch_Window/fr.md). [Pull request #12209](https://github.com/FreeCAD/FreeCAD/pull/12209)
-   L\'objet [Arch Toit](Arch_Roof/fr.md) a maintenant une propriété *Subvolume*. Cela permet d\'utiliser un objet solide personnalisé comme volume de soustraction pour un toit. [Pull request #12346](https://github.com/FreeCAD/FreeCAD/pull/12346)
-   De plus, pour un objet [Arch Toit](Arch_Roof/fr.md) qui utilise un objet solide comme *Base*, un volume de soustraction approprié est maintenant automatiquement généré. Tout comme un toit en fil de fer, un tel toit peut être soustrait des murs d\'un bâtiment avec [Arch Supprimer](Arch_Remove/fr.md). [Pull request #13221](https://github.com/FreeCAD/FreeCAD/pull/13221)
-   L\'outil [Arch Référence externe](Arch_Reference/fr.md) a été mis à jour : les objets de référence peuvent maintenant utiliser le contenu entier d\'un fichier au lieu de devoir choisir une partie, le support des fichiers DXF et IFC a été ajouté. [Pull request #13287](https://github.com/FreeCAD/FreeCAD/pull/13287)
-   FreeCAD a maintenant un nouveau fichier d\'exemple BIM. [Pull request #14937](https://github.com/FreeCAD/FreeCAD/pull/14937)
-   Le nouvel atelier BIM offre également une série de nouveaux outils de gestion, pour vous aider à configurer votre projet ou à gérer en masse les propriétés IFC de vos objets. Pour en savoir plus, consultez la page de l\'[atelier BIM](BIM_Workbench/fr.md).
-   [IfcOpenShell](IfcOpenShell/fr.md), un autre logiciel libre nécessaire pour travailler avec les fichiers IFC dans FreeCAD, est maintenant inclus dans tous les paquets d\'installation officiels proposés par l\'équipe FreeCAD. Si vous obtenez FreeCAD à partir d\'un fournisseur tiers, comme votre distribution Linux, où IfcOpenShell n\'est pas encore un paquetage officiel, l\'atelier BIM offre un outil utilitaire pour télécharger et installer IfcOpenShell. Et si vous n\'avez pas besoin d\'IFC, l\'atelier BIM fonctionne toujours à 100% sans IfcOpenShell.
-   Les barres d\'outils et les menus de l\'atelier BIM ont été retravaillés. [Pull request #14087](https://github.com/FreeCAD/FreeCAD/pull/14087)



## Atelier CAM 

-   L\'atelier Path s\'appelle désormais CAM. [Pull request #12665](https://github.com/FreeCAD/FreeCAD/pull/12665)



### Autres améliorations de CAM 

-   L\'usinage au repos a été réimplémenté pour prendre en compte le G-code des opérations précédentes (au lieu d\'utiliser les éléments internes des opérations de zone). Cela permet de prendre en charge l\'usinage au repos dans les opérations de [surface](CAM_Area/fr.md) après les opérations de non surface (notamment Adaptive). [Pull request #11939](https://github.com/FreeCAD/FreeCAD/pull/11939)
-   La compensation de la hauteur d\'outil G43 a été ajoutée au post-processeur CAM centroïde. [Pull request #12652](https://github.com/FreeCAD/FreeCAD/pull/12652)
-   Une option *Retrait de l\'avance* a été ajoutée aux paramètres de l\'opération de perçage pour l\'alésage et le perçage. [Pull request #13254](https://github.com/FreeCAD/FreeCAD/pull/13254)
-   Un nouveau simulateur CAM basé sur des fonctions OpenGL de bas niveau (plus rapide et plus précis) a été ajouté. [Pull request #13884](https://github.com/FreeCAD/FreeCAD/pull/13884) et [Pull request #15597](https://github.com/FreeCAD/FreeCAD/pull/15597).
-   L\'opération [Gravure en V](CAM_Vcarve/fr.md) a été retravaillée pour inclure des fonctions communément disponibles dans d\'autres logiciels de FAO (Descente, Passe de finition, Optimisation du mouvement de la tête et Méthode débogage de Voronoï) permettant d\'améliorer drastiquement la qualité de la surface sculptée tout en augmentant la vitesse de sculpture jusqu\'à 50%. [Pull request #14093](https://github.com/FreeCAD/FreeCAD/pull/14093)
-   Les modèles de matériaux d\'usinabilité ont été ajoutés ainsi que plusieurs matériaux. [Pull request #14460](https://github.com/FreeCAD/FreeCAD/pull/14460), [Pull request #15910](https://github.com/FreeCAD/FreeCAD/pull/15910) et [Pull request #16021](https://github.com/FreeCAD/FreeCAD/pull/16021)



## Atelier Draft 

-   Une option de justification et plusieurs propriétés connexes ont été ajoutées à [Draft Forme à partir d\'un texte](Draft_ShapeString/fr.md). [Pull request #10233](https://github.com/FreeCAD/FreeCAD/pull/10233)
-   Les [dimensions radiales](Draft_Dimension/fr#Utilisation_pour_une_dimension_radiale.md) n\'affichent plus qu\'une seule flèche. [Pull request #10655](https://github.com/FreeCAD/FreeCAD/pull/10655)
-   Une propriété *Oblique Angle* a été ajoutée à [Draft Forme à partir d\'un texte](Draft_ShapeString/fr.md). [Pull request #10783](https://github.com/FreeCAD/FreeCAD/pull/10783)
-   La prise en charge des hyperliens a été ajoutée. Les hyperliens, vers des fichiers locaux et distants et des URL, des [Draft Textes](Draft_Text/fr.md) et [Draft Étiquettes](Draft_Label/fr.md) peuvent être ouverts à partir de leur menu contextuel de la [vue en arborescence](Tree_view/fr.md) ou de la [vue 3D](3D_view/fr.md). [Pull request #10878](https://github.com/FreeCAD/FreeCAD/pull/10878)
-   Le code de [Draft Plan de travail](Draft_SelectPlane/fr.md) a été retravaillé. Il y a maintenant un plan de travail par vue 3D. [Pull request #11010](https://github.com/FreeCAD/FreeCAD/pull/11010)
-   La fonction d\'historique et les options d\'alignement de la commande [Draft Plan de travail](Draft_SelectPlane/fr.md) ont été améliorées. [Pull request #11062](https://github.com/FreeCAD/FreeCAD/pull/11062)
-   Le comportement de la [grille](Draft_ToggleGrid/fr.md) a été amélioré. Sa visibilité est désormais stockée par vue 3D. Lors du passage à un autre atelier, toutes les grilles sont masquées (un paramètre [réglage fin](Fine-tuning/fr.md) est disponible pour désactiver cela). [Pull request #11336](https://github.com/FreeCAD/FreeCAD/pull/11336)
-   Les préférences de Draft ont été vérifiées et améliorées. Certaines préférences ont été ajoutées, des préférences obsolètes ont été supprimées. Les pages de l\'[éditeur de propriétés](Property_editor/fr.md) ont une nouvelle mise en page et affichent les unités le cas échéant. Il n\'est plus nécessaire de redémarrer FreeCAD après avoir modifié une préférence de Draft. [Pull request #11379](https://github.com/FreeCAD/FreeCAD/pull/11379), [Pull request #11503](https://github.com/FreeCAD/FreeCAD/pull/11503), [Pull request #11512](https://github.com/FreeCAD/FreeCAD/pull/11512), [Pull request #11550](https://github.com/FreeCAD/FreeCAD/pull/11550), [Pull request #11579](https://github.com/FreeCAD/FreeCAD/pull/11579), [Pull request #11585](https://github.com/FreeCAD/FreeCAD/pull/11585), [Pull request #11677](https://github.com/FreeCAD/FreeCAD/pull/11677), [Pull request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694) et [Pull request #16603](https://github.com/FreeCAD/FreeCAD/pull/16603).
-   Un nouveau paramètre *Délai de la souris* a été ajouté aux préférences générales de Draft. S\'il est différent de zéro (la valeur par défaut est 1 s), après avoir saisi un nombre dans l\'un des champs de saisie du panneau des tâches, le mouvement de la souris sera désactivé, et ne modifiera donc pas la valeur du champ de saisie, pendant un certain temps en seconde. La définition d\'une valeur très élevée désactive pratiquement le mouvement de la souris jusqu\'à ce que la commande soit terminée. [Pull request #12624](https://github.com/FreeCAD/FreeCAD/pull/12624)
-   Un bouton permettant de changer rapidement la couleur de la grille a été ajouté au panneau des tâches de la commande [Draft Plan de travail](Draft_SelectPlane/fr.md). [Pull request #13051](https://github.com/FreeCAD/FreeCAD/pull/13051)
-   Une propriété *Fuse* a été ajoutée à [Draft Réseau de points](Draft_PointArray/fr.md), [Draft Réseau selon une courbe](Draft_PathArray/fr.md) et Draft PathTwistedArrays. [Pull request #13172](https://github.com/FreeCAD/FreeCAD/pull/13172) et [Pull request #13191](https://github.com/FreeCAD/FreeCAD/pull/13191)
-   Le bouton de la commande [Bascule de la grille](Draft_ToggleGrid/fr.md) se comporte maintenant comme un bouton de basculement, fournissant un retour visuel de l\'état de la grille (visible ou caché). [Pull request #14452](https://github.com/FreeCAD/FreeCAD/pull/14452)



### Autres améliorations de Draft 

-   Les [Surfaces liées](Draft_Facebinder/fr.md) peuvent maintenant gérer les faces appartenant à des liens et les faces imbriquées dans des [Std Parts](Std_Part/fr.md). [Pull request #11081](https://github.com/FreeCAD/FreeCAD/pull/11081)
-   Plusieurs paramètres ont été ajoutés à la commande [Définir le style](Draft_SetStyle/fr.md). [Pull request #11593](https://github.com/FreeCAD/FreeCAD/pull/11593), [Pull request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694) et [Pull request #13914](https://github.com/FreeCAD/FreeCAD/pull/13914)
-   Des paramètres ont également été ajoutés à la commande [Appliquer le style](Draft_ApplyStyle/fr.md). [Pull request #11610](https://github.com/FreeCAD/FreeCAD/pull/11610) et [Pull request #13914](https://github.com/FreeCAD/FreeCAD/pull/13914)
-   Les marqueurs d\'aimantation, d\'édition et de suivi utilisent désormais la préférence de la [taille des marqueurs](Preferences_Editor/fr#Vue_3D.md), [Pull request #11688](https://github.com/FreeCAD/FreeCAD/pull/11688) et [Pull request #16603](https://github.com/FreeCAD/FreeCAD/pull/16603)
-   Certaines icônes de Draft ont été modifiées pour améliorer leur apparence. [Pull request #13585](https://github.com/FreeCAD/FreeCAD/pull/13585)
-   [Draft Calque](Draft_Layer/fr.md) a été mis à jour pour le nouveau système de prise en compte des matériaux. Il a maintenant une propriété *Shape Appearance* et une propriété *Override Shape Appearance Children*. [Pull request #13949](https://github.com/FreeCAD/FreeCAD/pull/13949)
-   [Draft Congé](Draft_Fillet/fr.md) peut maintenant être appliqué aux arcs. [Pull request #14774](https://github.com/FreeCAD/FreeCAD/pull/14774)



## Atelier FEM 

+++
| <img alt="" src=images/FEM_better_legend_labels_relnotes_1.0.JPG  style="width:320px;"> | La position des étiquettes de la légende des couleurs a été ajustée pour que celles du haut soient moins susceptibles d\'être couvertes par le cube de navigation. La police et la couleur par défaut des étiquettes ont été modifiées pour augmenter la visibilité et des préférences ont été ajoutées pour permettre la modification de la couleur et de la taille des étiquettes. [Pull request #10552](https://github.com/FreeCAD/FreeCAD/pull/10552) |
+++

+++
| <img alt="" src=images/FEM_stress_component_linearization_relnotes_1.0.png  style="width:320px;"> | La commande [FEM Graphique de linéarisation des critères](FEM_PostFilterLinearizedStresses/fr.md) peut désormais utiliser les composantes du tenseur des contraintes pour les calculs de critères linéarisés. Auparavant, seules les critères de von Mises, de Tresca et les contraintes principales (majeures/intermédiaires/mineures) pouvaient être utilisées à cette fin. [Pull request #11724](https://github.com/FreeCAD/FreeCAD/pull/11724) |
+++

+++
| <img alt="" src=images/Cyclic_symmetry_relnotes_1.0.jpg  style="width:320px;"> | La prise en charge de la symétrie cyclique via la [contrainte de liaison](FEM_ConstraintTie/fr.md) dans CalculiX a été ajoutée, rendant possible l\'analyse de modèles avec une symétrie périodique de rotation en utilisant un seul secteur répétitif. [Pull request #12289](https://github.com/FreeCAD/FreeCAD/pull/12289) |
+++

+++
| <img alt="" src=images/2D_analyses_relnotes_1.0.png  style="width:320px;"> | La prise en charge des analyses 2D (contraintes planes, déformations planes et axisymétriques) a été ajoutée au [solveur CalculiX](FEM_SolverCalculixCxxtools/fr.md). Elles sont configurées de la même manière que les simulations avec des éléments de coque, mais il y a quelques restrictions supplémentaires décrites sur la page wiki mentionnée ci-dessus. La nouvelle option *Model Space* doit être configurée correctement. [Pull request #12562](https://github.com/FreeCAD/FreeCAD/pull/12562) |
+++

+++
| <img alt="" src=images/Hex_subdivision_relnotes_1.0.png  style="width:320px;"> | En tant que première étape vers la prise en charge des éléments hexaédriques, leur génération à l\'aide de la technique de subdivision de Gmsh est désormais possible grâce à la nouvelle propriété *Subdivision Algorithm* de Gmsh. Elle peut également être utilisée pour créer des éléments quadrilatéraux. [Pull request #12698](https://github.com/FreeCAD/FreeCAD/pull/12698) |
+++

+++
| <img alt="" src=images/Pipeline_colors_relnotes_1.0.png  style="width:320px;"> | De nouvelles propriétés d\'affichage ont été ajoutées aux objets du pipeline de résultats. La couleur et la largeur des arêtes des maillages peuvent maintenant être modifiées pour le mode d\'affichage *Surface avec arêtes*. La taille des nœuds peut être modifiée pour le mode *Nœuds*. Il y a également un paramètre de transparence pour tous les modes. [Pull request #13066](https://github.com/FreeCAD/FreeCAD/pull/13066) |
+++

++++
| <img alt="" src=images/Constraint_suppress_relnotes_1.0.png  style="width:320px;"> | Les contraintes FEM peuvent désormais être désactivées (clic droit sur une contrainte et sélection de *Désactiver*) et donc ignorées par les solveurs. | De cette façon, il est possible de modifier la configuration de l\'analyse sans avoir à supprimer les contraintes qui ne sont pas nécessaires. [Pull request #12359](https://github.com/FreeCAD/FreeCAD/pull/12359) |
++++

+++
| <img alt="" src=images/Rigid_body_relnotes_1.0.JPG  style="width:320px;"> | La prise en charge de la [contrainte de corps rigide](FEM_ConstraintRigidBody/fr.md) de CalculiX a été ajoutée, ce qui permet enfin de simuler la torsion de composants arbitraires et d\'appliquer des charges à distance, entre autres. [Pull request #13900](https://github.com/FreeCAD/FreeCAD/pull/13900) |
+++



### Autres améliorations de FEM 

-   Le menu *Modèle → Contraintes sans solveur* a été supprimé de l\'interface graphique. Les contraintes listées ne pouvaient pas être utilisées. [Pull request #10457](https://github.com/FreeCAD/FreeCAD/pull/10457) et [Pull request #10459](https://github.com/FreeCAD/FreeCAD/pull/10459)
-   Le mot *contrainte* a été supprimé des noms et des descriptions de la plupart des fonctions de l\'atelier FEM afin de garantir une nomenclature correcte. Les noms ont été modifiés de manière à correspondre aux normes de l\'industrie de l\'analyse par éléments finis et à les rendre intuitifs pour les nouveaux utilisateurs. [Pull request #10519](https://github.com/FreeCAD/FreeCAD/pull/10519) et [Pull request #10799](https://github.com/FreeCAD/FreeCAD/pull/10799)
-   De nouvelles icônes ont été ajoutées pour le [Solveur CalculiX standard](FEM_SolverCalculixCxxtools/fr.md), [Réglage du solveur](FEM_SolverControl/fr.md) et [Résolution](FEM_SolverRun/fr.md) pour une plus grande intuitivité. Ses exemples ont également été supprimés. [Pull request #10823](https://github.com/FreeCAD/FreeCAD/pull/10823) et [Pull request #12876](https://github.com/FreeCAD/FreeCAD/pull/12876)
-   Le solveur CalculiX (expérimental) a été supprimé de l\'interface graphique car il n\'est pas terminé et inutile pour le moment. [Pull request #10823](https://github.com/FreeCAD/FreeCAD/pull/10823)
-   La disposition de certains panneaux de tâches des outils de post-traitement a été améliorée afin de réduire la taille de l\'espace horizontal qu\'ils occupaient. [Pull request #11066](https://github.com/FreeCAD/FreeCAD/pull/11066)
-   Le panneau de tâches de [FEM Condition limite de température](FEM_ConstraintTemperature/fr.md) a été retravaillé pour résoudre des problèmes lors de l\'édition de cette fonction. [Pull request #11126](https://github.com/FreeCAD/FreeCAD/pull/11126)
-   Un ancien problème avec le [FEM Filtre d\'écrêtage selon une ligne](FEM_PostFilterDataAlongLine/fr.md) ne pouvant tracer que la magnitude et non les composantes vectorielles d\'une variable de sortie sélectionnée a finalement été corrigé. [Pull request #10992](https://github.com/FreeCAD/FreeCAD/pull/10992)
-   La [FEM Charge d\'effort](FEM_ConstraintForce/fr.md) et la [FEM Charge de pression](FEM_ConstraintPressure/fr.md) ont été révisées afin d\'améliorer leur fonctionnement du côté du code source. [Pull request #10935](https://github.com/FreeCAD/FreeCAD/pull/10935) et [Pull request #10923](https://github.com/FreeCAD/FreeCAD/pull/10923)
-   Le [FEM Données au point](FEM_PostFilterDataAtPoint/fr.md) a maintenant une propriété PointSize pour définir la taille du symbole du point pour plus de visibilité. [Pull request #11054](https://github.com/FreeCAD/FreeCAD/pull/11054)
-   Pour plus de clarté, la commande de [FEM Mailler plus finement](FEM_MeshRegion/fr.md) a été renommée en *Mailler plus finement* dans l\'interface graphique (le nom de la commande reste inchangé). [Pull request #11489](https://github.com/FreeCAD/FreeCAD/pull/11489)
-   La magnitude de l\'accélération de la gravité peut maintenant être modifiée en utilisant les propriétés de [FEM Charge de gravité](FEM_ConstraintSelfWeight/fr.md). [Pull request #12044](https://github.com/FreeCAD/FreeCAD/pull/12044)
-   [Contrainte de contact](FEM_ConstraintContact/fr.md) et [Contrainte de liaison](FEM_ConstraintTie/fr.md) ont été améliorées de manière significative. La rigidité du contact utilise maintenant la bonne unité et la valeur de la pente de contact peut être spécifiée pour le frottement dans le contact. De plus, l\'ajustement du jeu peut être spécifié pour le contact tandis que la contrainte de liaison peut avoir l\'ajustement activé ou désactivé. [Pull request #12133](https://github.com/FreeCAD/FreeCAD/pull/12133)
-   PaStiX et Pardiso ont été ajoutés aux [solveurs matriciels de CalculiX](FEM_SolverCalculixCxxtools/fr#Propriétés.md) supportés. Ce sont les solveurs ccx les plus rapides mais la possibilité de les utiliser dépend de la version binaire de CalculiX et des bibliothèques additionnelles disponibles. [Pull request #12478](https://github.com/FreeCAD/FreeCAD/pull/12478)
-   La propriété *Beam Reduced Integration* (fixée à *true* par défaut) a été ajoutée aux [paramètres du solveur CalculiX](FEM_SolverCalculixCxxtools/fr.md). Elle permet un schéma d\'intégration réduit pour les éléments de type poutre, rendant possible l\'utilisation de la section de type poutre tubulaire et éliminant les problèmes de précision dans les analyses avec plasticité, entre autres. [Pull request #12513](https://github.com/FreeCAD/FreeCAD/pull/12513)
-   L\'outil inachevé [Ensemble de nœuds](FEM_CreateNodesSet/fr.md) a été supprimé de l\'interface graphique. Il ne pouvait pas être utilisé. [Pull request #12611](https://github.com/FreeCAD/FreeCAD/pull/12611)
-   La procédure d\'analyse Vérification du maillage de CalculiX génère désormais correctement le maillage des résultats. [Pull request #12612](https://github.com/FreeCAD/FreeCAD/pull/12612)
-   Le panneau des tâches précise que le diamètre utilisé pour la section de tuyau est le diamètre extérieur. [Pull request #12609](https://github.com/FreeCAD/FreeCAD/pull/12609)
-   La propriété *Beam Shell Result Output 3D* du [solveur CalculiX](FEM_SolverCalculixCxxtools/fr.md) est maintenant définie à *true* par défaut pour fournir des résultats pour les éléments de type poutre et fournir des résultats significatifs pour les éléments de type coque. [Pull request #12493](https://github.com/FreeCAD/FreeCAD/pull/12493)
-   Les symboles des fonctions d\'analyse sont désormais correctement positionnés lorsque le corps (ou le conteneur de pièce) a eu modifié sa propriété de placement. [Pull request #12527](https://github.com/FreeCAD/FreeCAD/pull/12527)
-   [Charge de pression](FEM_ConstraintPressure/fr.md) fonctionne désormais correctement pour les coques, quel que soit le réglage des groupes de maillage. Ce paramètre peut être modifié dans les préférences. [Pull request #12437](https://github.com/FreeCAD/FreeCAD/pull/12437)
-   L\'écrouissage simple dans [FEM Matériau mécanique non linéaire](FEM_MaterialMechanicalNonlinear/fr.md) a été renommé en écrouissage isotrope. De plus, l\'écrouissage cinématique a été ajouté. [Pull request #12666](https://github.com/FreeCAD/FreeCAD/pull/12666)
-   La non-linéarité géométrique n\'est plus automatiquement activée et requise lorsqu\'un matériau non-linéaire est utilisé. Il s\'agit de formes indépendantes de non-linéarité. [Pull request #12703](https://github.com/FreeCAD/FreeCAD/pull/12703)
-   Les maillages mixtes composés d\'éléments triangulaires et quadrilatéraux sont désormais affichés correctement dans le pipeline de résultats. [Pull request #12740](https://github.com/FreeCAD/FreeCAD/pull/12740)
-   La propriété *Output Frequency* a été ajoutée aux [paramètres du solveur CalculiX](FEM_SolverCalculixCxxtools/fr.md). Elle définit la fréquence d\'écriture des sorties par incréments. [Pull request #12672](https://github.com/FreeCAD/FreeCAD/pull/12672)
-   Les éléments quadrilatéraux de second ordre peuvent maintenant être générés. Auparavant, le paramètre Gmsh d\'ordre 2 générait des éléments quadrilatéraux d\'ordre 1 en raison de l\'absence d\'une commande Gmsh *SecondOrderIncomplete* qui est maintenant utilisée en interne. Ces éléments peuvent également être utilisés pour les analyses 2D. [Pull request #12698](https://github.com/FreeCAD/FreeCAD/pull/12698) et [Pull request #12774](https://github.com/FreeCAD/FreeCAD/pull/12774)
-   La détermination de l\'orientation de la section transversale d\'un élément de type poutre a été partiellement corrigée. En raison d\'un bogue dans la version actuelle de CalculiX, il peut encore y avoir des problèmes avec certaines orientations. [Pull request #12833](https://github.com/FreeCAD/FreeCAD/pull/12833)
-   Les exemples Cantilever FEM sur la page de démarrage ont été mis à jour et un nouvel exemple utilisant des éléments 1D a été ajouté. [Pull request #12871](https://github.com/FreeCAD/FreeCAD/pull/12871)
-   Le format dans lequel FreeCAD écrit la [charge d\'effort](FEM_ConstraintForce/fr.md) est maintenant compatible avec le format CalculiX, éliminant les rares problèmes avec des nombres trop longs. [Pull request #12932](https://github.com/FreeCAD/FreeCAD/pull/12932)
-   Il est maintenant possible d\'exporter les [résultats du pipeline](FEM_PostPipelineFromResult/fr.md) au format VTK. [Pull request #12987](https://github.com/FreeCAD/FreeCAD/pull/12987)
-   De nouvelles propriétés de contrôle de l\'incrémentation ont été ajoutées aux [paramètres du solveur CalculiX](FEM_SolverCalculixCxxtools/fr.md). Actuellement, en plus de la taille de l\'incrément initial et de la périodicité de l\'étape, on peut spécifier la taille minimale et maximale de l\'incrément. De plus, la propriété *Itérations Thermo Mech Maximum* a été renommée en *Itérations Maximum* car elle peut maintenant être utilisée pour les analyses statiques (non thermomécaniques) également. [Pull request #12662](https://github.com/FreeCAD/FreeCAD/pull/12662)
-   L\'\[\[FEM_ElementGeometry2D/fr\|épaisseur par défaut d\'éléments\] 2D\] a été changée de 20 mm à 1 mm, ce qui est plus logique dans la pratique. [Pull request #13077](https://github.com/FreeCAD/FreeCAD/pull/13077)
-   De nombreuses icônes de FEM ont été améliorées de manière significative afin de réduire leur similarité et de rendre plus clair ce que font les outils. [Pull request #13130](https://github.com/FreeCAD/FreeCAD/pull/13130)
-   La propriété *Thermo Mech Type* a été ajoutée aux [paramètres du solveur CalculiX](FEM_SolverCalculixCxxtools/fr.md). Elle permet de passer d\'une analyse thermomécanique classique (couplée) à une analyse découplée ou à une analyse de pur transfert de chaleur. [Pull request #13296](https://github.com/FreeCAD/FreeCAD/pull/13296)
-   La propriété *Taille minimum* a été ajoutée au [mailleur Netgen](FEM_MeshNetgenFromShape/fr.md) afin d\'éviter la génération d\'éléments trop petits lors du maillage de géométries plus complexes. [Pull request #12794](https://github.com/FreeCAD/FreeCAD/pull/12794)
-   Un ancien problème avec une propriété d\'échelle de symbole non fonctionnelle pour les contraintes FEM a finalement été corrigé et la propriété *Scale* peut maintenant être utilisée pour ajuster la taille des symboles d\'une contrainte sélectionnée. [Pull request #13274](https://github.com/FreeCAD/FreeCAD/pull/13274)
-   La mise à l\'échelle automatique des contraintes FEM a été améliorée pour mieux gérer les objets très petits et très grands. [Pull request #13586](https://github.com/FreeCAD/FreeCAD/pull/13586)
-   [Charge de flux de chaleur](FEM_ConstraintHeatflux/fr.md) dispose désormais d\'un mode de flux de chaleur par rayonnement pour modéliser le rayonnement de la surface vers l\'environnement. [Pull request #13466](https://github.com/FreeCAD/FreeCAD/pull/13466)
-   Quelques propriétés inutilisées du symbole de contrainte View ont été supprimées. [Pull request #13569](https://github.com/FreeCAD/FreeCAD/pull/13569)
-   De nouvelles propriétés d\'affichage (dont la principale est *Mode couleur*) ont été ajoutées aux objets de maillage FEM afin que les paramètres personnalisés de couleur et de transparence pour les maillages puissent être sauvegardés et restaurés. [Pull request #13698](https://github.com/FreeCAD/FreeCAD/pull/13698)
-   Maintenant, seul le dernier filtre ajouté sous chaque objet du pipeline de résultats est visible par défaut. [Pull request #13820](https://github.com/FreeCAD/FreeCAD/pull/13820)
-   Les astuces du panneau de tâches de plusieurs contraintes ont été modifiées afin de refléter les règles de sélection de la géométrie pour ces contraintes. [Pull request #13921](https://github.com/FreeCAD/FreeCAD/pull/13921) et [Pull request #14002](https://github.com/FreeCAD/FreeCAD/pull/14002)
-   La prise en charge des résultats de flux de chaleur provenant d\'analyses thermomécaniques a été ajoutée au pipeline de résultats. [Pull request #14019](https://github.com/FreeCAD/FreeCAD/pull/14019)
-   L\'[affichage des variables de sortie](FEM_ConstraintSectionPrint/fr.md) a été amélioré, en ajoutant la prise en charge des résultats de flux de chaleur et de contrainte de traînée (pas encore disponible car les analyses de fluides 3D avec CalculiX n\'ont pas encore été implémentées). [Pull request #14046](https://github.com/FreeCAD/FreeCAD/pull/14046)
-   [Source de chaleur du corps](FEM_ConstraintBodyHeatSource/fr.md) peut maintenant être utilisé avec CalculiX et a deux modes d\'entrée : taux de dissipation \[W/kg\] et puissance totale \[W\]. [Pull request #14417](https://github.com/FreeCAD/FreeCAD/pull/14417)
-   Les propriétés de rotation du [Système de coordonnées locales](FEM_ConstraintTransform/fr.md) ont été remplacées par une seule propriété *Rotation* pour des raisons de cohérence. [Pull request #14353](https://github.com/FreeCAD/FreeCAD/pull/14353)
-   Un outil [Effacer des éléments](FEM_CreateElementsSet/fr.md) a été ajouté pour permettre de cacher des éléments d\'un maillage sélectionné avec un polygone. [Pull request #11492](https://github.com/FreeCAD/FreeCAD/pull/11492)
-   Les trois exemples FEM sur la page de démarrage ont été remplacés par un seul, contenant les trois variantes du modèle de poutre cantilever (1D, 2D et 3D) dans les conteneurs de [groupe](Std_Group/fr.md). [Pull request #15786](https://github.com/FreeCAD/FreeCAD/pull/15786)
-   Les propriétés redondantes *Fix* et les cases à cocher de [FEM Condition limite de déplacement](FEM_ConstraintDisplacement/fr.md) ont été supprimées. [Pull request #15531](https://github.com/FreeCAD/FreeCAD/pull/15531)
-   Le comportement des boutons Annuler dans les panneaux de tâches des mailleurs [Gmsh](FEM_MeshGmshFromShape/fr.md) et [Netgen](FEM_MeshNetgenFromShape/fr.md) a été corrigé afin qu\'ils puissent être utilisés pour interrompre le maillage en cours, ce qui est particulièrement important lorsqu\'une estimation initiale de la taille des éléments est trop faible. De plus, le mailleur Netgen a été implémenté, ce qui permet enfin de l\'utiliser sur tous les systèmes, y compris Linux. [Pull request #16515](https://github.com/FreeCAD/FreeCAD/pull/16515) et [Pull request #16433](https://github.com/FreeCAD/FreeCAD/pull/16433)
-   L\'algorithme 2D *Quasi-structured Quad* manquant dans le mailleur Gmsh a été ajouté ainsi que d\'autres corrections. [Pull request #15624](https://github.com/FreeCAD/FreeCAD/pull/15624)



## Atelier Material 

+++
| <img alt="" src=images/Materials_relnotes_1.0.png  style="width:320px;"> | Le système de gestion des matériaux, y compris l\'éditeur, a été entièrement retravaillé. D\'autres améliorations à cet égard suivront. [Pull request #10690](https://github.com/FreeCAD/FreeCAD/pull/10690) |
+++

+++
| <img alt="" src=images/Appearance_preview_relnotes_1.0.png  style="width:320px;"> | L\'aperçu de l\'apparence a été ajouté pour montrer les matériaux de la même manière qu\'ils seront montrés dans les documents. [Pull request #11628](https://github.com/FreeCAD/FreeCAD/pull/11628) |
+++

+++
| <img alt="" src=images/Material_appearance_relnotes_1.0.jpg  style="width:320px;"> | Le nouveau système de matériaux est maintenant utilisé pour les propriétés d\'apparence. [Pull request #13294](https://github.com/FreeCAD/FreeCAD/pull/13294) |
+++



### Autres améliorations de Material 

-   Des boîtes de dialogue permettant de visualiser les propriétés d\'apparence et de matériau d\'un objet ont été ajoutées et sont disponibles en tant qu\'outils *Inspecter l\'apparence* et *Inspecter le matériau*. [Pull request #13967](https://github.com/FreeCAD/FreeCAD/pull/13967)



## Atelier Part 

+++
| <img alt="" src=images/Part_scale_relnotes_1.0.png  style="width:320px;"> | L\'outil [Part Échelle](Part_Scale/fr.md) a été ajouté pour faciliter la mise à l\'échelle des formes sans avoir à utiliser les outils de l\'atelier Draft. [Pull request #10583](https://github.com/FreeCAD/FreeCAD/pull/10583) |
+++

+++
| <img alt="" src=images/Part_Mirror_relnotes_1.0.png  style="width:320px;"> | [Part Objet en miroir](Part_Mirror/fr.md) prend désormais en charge les objets de référence, tel qu\'un [Part Plan](Part_Plane/fr.md) pour définir un plan miroir arbitraire en plus des plans XY, XZ et YZ standard. [Pull request #11535](https://github.com/FreeCAD/FreeCAD/pull/11535) |
+++



### Autres améliorations de Part 

-   La propriété *Frenet* est désormais activée par défaut pour l\'outil [Part Balayage](Part_Sweep/fr.md) afin d\'éviter un problème de rendu courant. [Pull request #11590](https://github.com/FreeCAD/FreeCAD/pull/11590)
-   Un nouveau [mode d\'ancrage](Part_EditAttachment/fr#Modes_d'ancrage.md) appelé *Intersection* a été ajouté au dispositif ligne. Il permet de trouver l\'intersection de deux faces planes. [Pull request #12328](https://github.com/FreeCAD/FreeCAD/pull/12328)
-   L\'outil [Part Projeter sur une surface](Part_ProjectionOnSurface/fr.md) est maintenant paramétrique. [Pull request #13158](https://github.com/FreeCAD/FreeCAD/pull/13158)
-   Toutes les icônes de Part utilisent maintenant le thème bleu et les primitives utilisent la même icône pour la barre d\'outils et la vue en arborescence. [Pull request #14074](https://github.com/FreeCAD/FreeCAD/pull/14074)
-   La commande [Créer une esquisse](Sketcher_NewSketch/fr.md) a été ajoutée à la barre d\'outils et au menu de Part car des opérations telles que l\'extrusion utilisent généralement des esquisses en entrée. [Pull request #14318](https://github.com/FreeCAD/FreeCAD/pull/14318)
-   Un nouveau [mode d\'ancrage](Part_EditAttachment/fr#Modes_d'ancrage.md) appelé *XY parallèle au plan* a été ajouté au dispositif plan et dispositif 3D. Il permet d\'obtenir un accrochage similaire à *XY de l\'objet*, mais avec le plan XY translaté pour passer par un sommet sélectionné. Contrairement au mode d\'accrochage *Translater l\'origine*, il ne déplace pas l\'origine dans une esquisse/2D. Il peut être utilisé avec les plans d\'origine, les plans de référence et les esquisses, mais aussi avec tout objet ayant une propriété *Placement*. [Pull request #14372](https://github.com/FreeCAD/FreeCAD/pull/14372)



## Atelier PartDesign 

+++
| <img alt="" src=images/Revolve_options_relnotes_1.0.png  style="width:320px;"> | Des modes supplémentaires ont été ajoutés aux fonctions [Révolution](PartDesign_Revolution/fr.md) et [Rainure](PartDesign_Groove/fr.md), vers la première/dernière face, jusqu\'à la face et deux dimensions. [Pull request #7193](https://github.com/FreeCAD/FreeCAD/pull/7193) |
+++

+++
| <img alt="" src=images/Pad_task_dialog_relnotes_1.0.png  style="width:320px;"> | Les panneaux de tâches de [Protrusion](PartDesign_Pad/fr.md) et de [Cavité](PartDesign_Pocket/fr.md) ont été améliorés (réorganisation des éléments de l\'interface utilisateur. L\'option **Sélectionner une face** est cachée lorsqu\'elle n\'est pas nécessaire et ainsi de suite). [Pull request #10392](https://github.com/FreeCAD/FreeCAD/pull/10392) |
+++

+++
| <img alt="" src=images/Pattern_offset_mode_relnotes_1.0.png  style="width:320px;"> | Le mode décalage a été ajouté à [Répétition linéaire](PartDesign_LinearPattern/fr.md) et [Répétition circulaire](PartDesign_PolarPattern.md). Le mode précédent a été renommé **Longueur totale**. [Pull request #10377](https://github.com/FreeCAD/FreeCAD/pull/10377) |
+++

+++
| <img alt="" src=images/Single_solid_rule_relnotes_1.0.PNG  style="width:320px;"> | Une prise en charge expérimentale pour plusieurs solides dans un [corps](PartDesign_Body/fr.md) a été ajoutée. Elle peut être activée dans les préférences (pour les nouveaux corps) ou dans les propriétés d\'un corps existant. [Pull request #13960](https://github.com/FreeCAD/FreeCAD/pull/13960) |
+++

+++
| <img alt="" src=images/Pad_up_to_shape_relnotes_1.0.PNG  style="width:320px;"> | Le mode *Jusqu\'à la forme* a été ajouté pour les protrusions et les cavités, permettant de les terminer sur plusieurs faces, contrairement au mode *Jusqu\'à la face* qui ne permet de sélectionner qu\'une seule face. [Pull request #11392](https://github.com/FreeCAD/FreeCAD/pull/11392) et [Pull request #14433](https://github.com/FreeCAD/FreeCAD/pull/14433) |
+++



### Autres améliorations de PartDesign 

-   L\'option *Générer un évidement vers l\'intérieur* est maintenant activée par défaut pour l\'outil [Évidement](PartDesign_Thickness/fr.md). [Pull request #7488](https://github.com/FreeCAD/FreeCAD/pull/7488)
-   Les points de référence changent désormais de couleur lorsqu\'ils sont mis en évidence ou sélectionnés (comme les autres points de référence). [Pull request #12439](https://github.com/FreeCAD/FreeCAD/pull/12439)
-   Les icônes de PartDesign ont été légèrement améliorées pour plus de cohérence. [Pull request #13109](https://github.com/FreeCAD/FreeCAD/pull/13109)
-   Une propriété *Désactiver* a été ajoutée pour désactiver temporairement une fonction. [Pull request #12096](https://github.com/FreeCAD/FreeCAD/pull/12096) et [Pull request #12412](https://github.com/FreeCAD/FreeCAD/pull/12412)
-   Les barres d\'outils de PartDesign ont été mises à jour : les référentiels et les actions basées sur les esquisses sont désormais regroupés, [Part Vérifier la géométrie](Part_CheckGeometry/fr.md) a été ajouté à la barre d\'outils et au menu. Les barres d\'outils ont été divisées en plusieurs barres individuelles pour permettre de les réorganiser. [Pull request #13833](https://github.com/FreeCAD/FreeCAD/pull/13833)
-   Un nouveau mode *Transformer le corps* a été ajouté aux outils de miroir et de motif de PartDesign, permettant de transformer la forme de l\'élément de base au lieu de chaques formes des outils des éléments additifs et soustractifs. [Pull request #12589](https://github.com/FreeCAD/FreeCAD/pull/12589)
-   La fenêtre de dialogue de l\'outil [Perçage](PartDesign_Hole/fr.md) a été améliorée. [Pull request #14031](https://github.com/FreeCAD/FreeCAD/pull/14031)
-   L\'outil [Migrer](PartDesign_Migrate/fr.md) a été supprimé de l\'interface graphique car il n\'était utile que pour les migrations entre des versions qui sont maintenant très obsolètes. [Pull request #15196](https://github.com/FreeCAD/FreeCAD/pull/15196)



## Atelier Sketcher 

+++
| <img alt="" src=images/Arc_helper_relnotes_1.0.png  style="width:320px;"> | L\'implémentation d\'une superposition de cercles pour les arcs (pour résoudre le problème des contraintes apparaissant loin d\'eux) a été complétée avec une [commande pour les interchanger](Sketcher_ArcOverlay/fr.md). [Pull request #9703](https://github.com/FreeCAD/FreeCAD/pull/9703) |
+++

   
  <img alt="" src=images/Contextual_dimension_relnotes_1.0.gif  style="width:320px;">Cliquez sur l\'image si l\'animation ne démarre pas.   Un outil de contrainte contextuelle de [Dimension](Sketcher_Dimension/fr.md) a été ajouté pour permettre un dimensionnement rapide et intuitif à l\'aide d\'un seul outil polyvalent. [Pull request #9810](https://github.com/FreeCAD/FreeCAD/pull/9810)
   

   
  <img alt="" src=images/Tool_parameters_relnotes_1.0.gif  style="width:320px;">Cliquez sur l\'image si l\'animation ne démarre pas.   Des [paramètres d\'outils](Sketcher_Workbench#On-View-Parameters/fr.md) ont été ajoutés pour permettre l\'ajout de dimensions lors du dessin des formes. En fonction du réglage des préférences de Paramètres dans la vue, ils peuvent être désactivés, réduits aux dimensions uniquement (pas de coordonnées initiales) ou entièrement activés. De plus, des modes ont été ajoutés pour les outils de forme. Ils peuvent être sélectionnés à l\'aide de la touche M ou d\'une liste déroulante dans le panneau des tâches. Certains outils disposent de paramètres supplémentaires sous la forme de cases à cocher dans le panneau des tâches et de raccourcis clavier supplémentaires. Actuellement, les nouvelles fonctions sont disponibles pour les points, les lignes, les arcs, les ellipses, les rectangles, les polygones, les rainures et les B-splines. [Pull request #11048](https://github.com/FreeCAD/FreeCAD/pull/11048), [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) et suivants
   

+++
| <img alt="" src=images/Offset_relnotes_1.0.png  style="width:320px;"> | Un outil de [décalage](Sketcher_Offset/fr.md) a été ajouté pour permettre le décalage de courbes. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

+++
| <img alt="" src=images/Three_point_rectangle_relnotes_1.0.png  style="width:320px;"> | Le mode [rectangle](Sketcher_CompCreateRectangles/fr.md) à trois points a été ajouté en deux versions : 3 coins, centre ou 2 coins. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

+++
| <img alt="" src=images/Arc_slot_relnotes_1.0.png  style="width:320px;"> | Un outil de [rainure en arc](Sketcher_CreateArcSlot/fr.md) a été ajouté avec deux modes (extrémités en arc et extrémités plates) pour permettre la création de rainures courbes. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

   
  <img alt="" src=images/Auto_horizontal-vertical_relnotes_1.0.gif  style="width:320px;">Cliquez sur l\'image si l\'animation ne démarre pas.   Une [contrainte horizontale/verticale](Sketcher_ConstrainHorVer/fr.md) a été ajoutée. Elle applique automatiquement une contrainte horizontale si une ligne est plus proche de l\'orientation horizontale ou une contrainte verticale si elle est plus proche de l\'orientation verticale. [Pull request #11538](https://github.com/FreeCAD/FreeCAD/pull/11538)
   

+++
| <img alt="" src=images/Angle_radius_rendering_relnotes_1.0.png  style="width:320px;"> | Le rendu des contraintes d\'angle et de rayon a été amélioré. Les contraintes d\'angle ont maintenant des lignes d\'extension complètes. [Pull request #11507](https://github.com/FreeCAD/FreeCAD/pull/11507) |
+++

+++
| <img alt="" src=images/Polar_transform_relnotes_1.0.png  style="width:320px;"> | Un outil de [transformation polaire](Sketcher_Rotate/fr.md) a été ajouté pour permettre la rotation et les motifs circulaires des géométries de l\'esquisse. [Pull request #11264](https://github.com/FreeCAD/FreeCAD/pull/11264) |
+++

   
  <img alt="" src=images/Sketcher_copy-cut-paste_relnotes_1.0.gif  style="width:320px;">Cliquez sur l\'image si l\'animation ne démarre pas.   Il est désormais possible de copier/couper et coller une géométrie d\'esquisse (avec des contraintes) en utilisant les raccourcis clavier habituels : Ctrl+C, Ctrl+X et Ctrl+V. Non seulement à l\'intérieur d\'une même esquisse, mais aussi entre différentes esquisses ou même différentes instances de FreeCAD. La géométrie est copiée sous forme de commandes Python, de sorte qu\'elle peut être utilisée d\'autres manières (par exemple, partagée sur le forum). [Pull request #11537](https://github.com/FreeCAD/FreeCAD/pull/11537)
   

+++
| <img alt="" src=images/Scale_transform_relnotes_1.0.png  style="width:320px;"> | Un outil de [transformation de mise à l\'échelle](Sketcher_Scale/fr.md) a été ajouté, permettant de mettre à l\'échelle la géométrie dans l\'esquisse en utilisant un point central sélectionné et un facteur d\'échelle ou deux points de référence. [Pull request #11265](https://github.com/FreeCAD/FreeCAD/pull/11265) |
+++

   
  <img alt="" src=images/B-spline_tangency_relnotes_1.0.gif  style="width:320px;">Cliquez sur l\'image si l\'animation ne démarre pas.   La tangence au bord des B-splines a été ajoutée, éliminant le besoin d\'utiliser les points d\'extrémité et divers contournements à la place. [Pull request #11853](https://github.com/FreeCAD/FreeCAD/pull/11853)
   

+++
| <img alt="" src=images/Sketcher_translate_relnotes_1.0.png  style="width:320px;"> | Les outils de [répétition linéaire](Sketcher_RectangularArray/fr.md), [déplacement](Sketcher_Move/fr.md), [Copie](Sketcher_Copy/fr.md) et [clonage](Sketcher_Clone/fr.md) ont été remplacés par un seul outil [Déplacer/dupliquer](Sketcher_Translate/fr.md). [Pull request #11267](https://github.com/FreeCAD/FreeCAD/pull/11267) |
+++

+++
| <img alt="" src=images/Sketcher_chamfer_relnotes_1.0.png  style="width:320px;"> | Un outil [Chanfrein](Sketcher_CreateChamfer/fr.md) a été ajouté avec une option permettant de passer en mode [Congé](Sketcher_CreateFillet/fr.md). De plus, il n\'y a plus d\'outil séparé pour les congés préservant l\'angle. Une option *Conserver le coin* (cochée par défaut) a été ajoutée à l\'outil [Congé](Sketcher_CreateFillet/fr.md). [Pull request #12898](https://github.com/FreeCAD/FreeCAD/pull/12898) |
+++

   
  <img alt="" src=images/New_symmetry_relnotes_1.0.gif  style="width:320px;">Cliquez sur l\'image si l\'animation ne démarre pas.   L\'outil [Symétriser](Sketcher_Symmetry/fr.md) a été retravaillé. Il fonctionne désormais en présélectionnant la géométrie et en choisissant une ligne ou un point autour duquel la géométrie sera symétrisée. Un aperçu est affiché et le comportement de l\'outil peut être contrôlé par les paramètres de l\'outil. [Pull request #11853](https://github.com/FreeCAD/FreeCAD/pull/11853)
   

   
  <img alt="" src=images/Auto_midpoint_relnotes_1.0.gif  style="width:320px;">Cliquez sur l\'image si l\'animation ne démarre pas.   La [Contrainte symétrique](Sketcher_ConstrainSymmetric/fr.md) est désormais applicable automatiquement lorsque le point médian d\'une ligne est choisi. [Pull request #13147](https://github.com/FreeCAD/FreeCAD/pull/13147)
   

+++
| <img alt="" src=images/Sketcher_arc_length_relnotes_1.0.png  style="width:320px;"> | La [Contrainte de distance](Sketcher_ConstrainDistance/fr.md) peut maintenant être utilisée pour les contraintes de longueur d\'arc (l\'arc circulaire doit être présélectionné). [Pull request #12602](https://github.com/FreeCAD/FreeCAD/pull/12602) |
+++

+++
| <img alt="" src=images/Point_color_relnotes_1.0.png  style="width:320px;"> | La couleur de rendu des points est maintenant différente selon qu\'il s\'agit d\'un point normal/terminal (blanc, maintenant créé par défaut lors de l\'utilisation de l\'outil [Point](Sketcher_CreatePoint/fr.md)), d\'un point de construction/centre (bleu) ou d\'un point coïncidant avec un autre (rouge). [Pull request #13098](https://github.com/FreeCAD/FreeCAD/pull/13098) |
+++

   
  <img alt="" src=images/Trim_drag_relnotes_1.0.gif  style="width:320px;">Cliquez sur l\'image si l\'animation ne démarre pas.   L\'outil [Ajuster](Sketcher_Trimming/fr.md) peut maintenant être utilisé en mode *maintenir et faire glisser*. [Pull request #13188](https://github.com/FreeCAD/FreeCAD/pull/13188)
   



### Autres améliorations de Sketcher 

-   Le mode cadre a été ajouté pour l\'outil Rectangle. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   Deux nouveaux modes ont été ajoutés pour l\'outil Ligne : « Point, longueur, angle » et « Point, largeur, hauteur ». [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   Les icônes de [Géométrie de construction](Sketcher_ToggleConstruction/fr.md) et de [Contraintes pilotantes](Sketcher_ToggleDrivingConstraint/fr.md) ont été modifiées. Désormais, la première n\'est plus aussi similaire à [Copie carbone](Sketcher_CarbonCopy/fr.md) et les deux icônes de basculement changent lorsqu\'on clique dessus. [Pull request #11500](https://github.com/FreeCAD/FreeCAD/pull/11500)
-   Les icônes du Sketcher ont été révisées afin d\'unifier leur apparence (largeur des traits, couleurs et taille des points). [Pull request #11785](https://github.com/FreeCAD/FreeCAD/pull/11785)
-   Un nouvel outil de contrainte [Coïncidence unifiée](Sketcher_ConstrainCoincidentUnified/fr.md) a été introduit. Cet outil combine les outils de contrainte de [Coïncidence](Sketcher_ConstrainCoincident/fr.md) et de [Point sur objet](Sketcher_ConstrainPointOnObject/fr.md). [Pull request #11494](https://github.com/FreeCAD/FreeCAD/pull/11494)
-   Le rendu des contraintes d\'angle d\'arc, d\'angle de ligne et de distance d\'arc a été amélioré. [Pull request #12012](https://github.com/FreeCAD/FreeCAD/pull/12012)
-   Les types d\'arêtes peuvent maintenant être personnalisés non seulement en changeant la couleur mais aussi le motif et la taille. Cela permet par exemple de créer des lignes de construction en pointillés. [Pull request #11996](https://github.com/FreeCAD/FreeCAD/pull/11996)
-   Le menu du clic droit est maintenant contextuel et inclut également les commandes B-spline. [Pull request #11884](https://github.com/FreeCAD/FreeCAD/pull/11884) et [Pull request #11973](https://github.com/FreeCAD/FreeCAD/pull/11973)
-   Un double-clic sur une arête sélectionne désormais toute la géométrie qui lui est liée. [Pull request #11925](https://github.com/FreeCAD/FreeCAD/pull/11925)
-   Les barres d\'outils de Sketcher ont été légèrement réorganisées dans un souci de clarté et de cohérence. [Pull request #13407](https://github.com/FreeCAD/FreeCAD/pull/13407) et [Pull request #13763](https://github.com/FreeCAD/FreeCAD/pull/13763)
-   Les icônes des outils [Copie carbone](Sketcher_CarbonCopy/fr.md) ont été améliorées pour une meilleure visibilité. [Pull request #15074](https://github.com/FreeCAD/FreeCAD/pull/15074)



## Atelier Spreadsheet 



### Autres améliorations de Spreadsheet 

-   Double-cliquer sur une feuille de calcul dans la vue en arborescence permet désormais de basculer vers cet atelier. [Pull request #13137](https://github.com/FreeCAD/FreeCAD/pull/13137)
-   Les icônes de Spreadsheet ont été améliorées. [Pull request #13996](https://github.com/FreeCAD/FreeCAD/pull/13996)



## Atelier TechDraw 

+++
| <img alt="" src=images/TechDraw_cosmetic_circle_relnotes_1.0.png  style="width:320px;"> | L\'outil [Cercle cosmétique](TechDraw_CosmeticCircle/fr.md) a été ajouté pour permettre la création de cercles cosmétiques en sélectionnant le centre et en saisissant le rayon. [Pull request #10763](https://github.com/FreeCAD/FreeCAD/pull/10763) |
+++

+++
| <img alt="" src=images/Arc_length_relnotes_1.0.png  style="width:320px;"> | L\'outil [Longueur d\'arc d\'arêtes](TechDraw_ExtensionArcLengthAnnotation/fr.md) a été ajouté pour créer des annotations de type dimensionnel de la longueur d\'arc d\'arêtes sélectionnées. [Pull request #11532](https://github.com/FreeCAD/FreeCAD/pull/11532) |
+++

+++
| <img alt="" src=images/Offset_vertex_relnotes_1.0.png  style="width:320px;"> | L\'outil [Sommets décalés](TechDraw_CommandAddOffsetVertex/fr.md) a été ajouté pour créer des sommets cosmétiques en décalage par rapport aux sommets sélectionnés. [Pull request #11655](https://github.com/FreeCAD/FreeCAD/pull/11655) |
+++

+++
| <img alt="" src=images/Broken_view_relnotes_1.0.png  style="width:320px;"> | L\'outil [Vue interrompue](TechDraw_BrokenView/fr.md) a été ajouté pour représenter facilement les objets longs. [Pull request #13331](https://github.com/FreeCAD/FreeCAD/pull/13331) |
+++

   
  <img alt="" src=images/Techdraw_smart_dimension_relnotes_1.0.gif  style="width:320px;">Cliquez sur l\'image si l\'animation ne démarre pas.   Un nouvel outil de dimension contextuel a été ajouté, basé sur [celui introduit dans Sketcher](Sketcher_Dimension/fr.md). [Pull request #13525](https://github.com/FreeCAD/FreeCAD/pull/13525)
   



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
-   L\'outil [Positionner une vue en coupe](TechDraw_ExtensionPositionSectionView/fr.md) peut maintenant être utilisé en sélectionnant une arête dans une vue de coupe et un sommet dans la vue source. [Pull request #11797](https://github.com/FreeCAD/FreeCAD/pull/11797)
-   L\'outil [Répétition](TechDraw_ExtensionInsertRepetition/fr.md) permet d\'insérer un nombre de fonctions répétées, a été ajouté. [Pull request #12509](https://github.com/FreeCAD/FreeCAD/pull/12509)
-   Des améliorations mineures mais importantes ont été apportées à l\'utilisation : un double-clic sur la page TechDraw permet désormais d\'accéder à cet atelier et l\'outil TechDraw Déplacer une vue a été remplacé par un simple glisser-déposer dans la [vue en arborescence](Tree_view/fr.md). Les outils TechDraw Ajout vue dans une fenêtre de rognage et TechDraw Suppression vue d\'une fenêtre de rognage ont également été remplacés par un simple glisser-déposer dans l\'arborescence. [Pull request #13063](https://github.com/FreeCAD/FreeCAD/pull/13063)
-   L\'outil [Projection de forme](TechDraw_ProjectShape/fr.md) a été supprimé de TechDraw car il provenait de l\'ancien atelier Drawing et n\'avait rien à voir avec une page TechDraw. [Pull request #13655](https://github.com/FreeCAD/FreeCAD/pull/13655)
-   L\'outil [Vue](TechDraw_View/fr.md) a été amélioré afin qu\'il puisse gérer plus de types d\'objets et de paramètres. Cela a permis de supprimer les outils suivants de la barre d\'outils : [Vue d\'un objet Spreadsheet](TechDraw_SpreadsheetView/fr.md), [Vue d\'un objet Arch](TechDraw_ArchView/fr.md), [Symbole](TechDraw_Symbol/fr.md), [Image](TechDraw_Image/fr.md) et [Groupe de projections](TechDraw_ProjectionGroup/fr.md). [Pull request #13219](https://github.com/FreeCAD/FreeCAD/pull/13219)
-   L\'aimantation a été ajoutée pour permettre l\'alignement automatique des vues et des dimensions. L\'aimantation peut être temporairement désactivée à l\'aide du modificateur de touche Alt. [Pull request #13659](https://github.com/FreeCAD/FreeCAD/pull/13659)
-   La gestion des cosmétiques a été améliorée de diverses manières. [Pull request #14216](https://github.com/FreeCAD/FreeCAD/pull/14216)
-   De nombreuses icônes de TechDraw ont été améliorées. [Pull request #14873](https://github.com/FreeCAD/FreeCAD/pull/14873) et suivants.
-   Le panneau des tâches de l\'outil [Symbole de finition de surface](TechDraw_SurfaceFinishSymbols/fr.md) a été considérablement amélioré visuellement. [Pull request #16147](https://github.com/FreeCAD/FreeCAD/pull/16147)



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.0/fr
