# Release notes 0.20/fr
{{TOCright}}

**FreeCAD 0.20** a été publié le **14 juin 2022**, téléchargez le depuis la page [Téléchargement](Download/fr.md). Cette page liste toutes les nouvelles fonctionnalités et les changements.

Les notes de versions plus anciennes de FreeCAD sont disponibles dans la [Liste des fonctionnalités](Feature_list/fr#Notes_de_versions.md).

   
  ![](images/FreeCAD_highlight_relnotes_0.20.gif )   *Modèle d\'un moteur à courant continu type 775 par l\'utilisateur \"jimmihenry\", voir [Users Showcase](https   *//forum.freecadweb.org/viewtopic.php?p=551765#p551765).Le modèle a été réalisé entièrement avec la version hebdomadaire [development snapshots](https   *//github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds) de FreeCAD 0.20. Les images de l\'animation graphique ont été réalisées avec la macro FreeCAD [ Screen Wiki](Macro_Screen_Wiki/fr.md). Le GIF animé a été créé à l\'aide de [GIMP](https   *//fr.wikipedia.org/wiki/GIMP). Pour les notes de version, il a été recadré et redimensionné à l\'aide de [ezgif](https   *//ezgif.com/crop).*
   

## Généralités

### freecad.org

Nous sommes heureux que le projet [KiCAD](https   *//www.kicad.org/), par le biais de [KiCAD services corp.](https   *//www.kipro-pcb.com/), nous ait sponsorisé le nom de domaine freecad.org. Tous les sites Web de FreeCAD sont désormais disponibles sous [freecadweb.org](https   *//freecadweb.org) et [freecad.org](https   *//freecad.org).

### Suivi des bogues/problèmes 

Le système de suivi des bogues de FreeCAD a été déplacé sur GitHub    * <https   *//github.com/FreeCAD/FreeCAD/issues>.

**Remarque    *** Seuls les rapports de bogue ayant fait l\'objet d\'une discussion préalable sur le forum seront pris en considération. Les rapports sans cela seront fermés.

### Nouveau système d\'aide 

Le système d\'aide a été réécrit et mis à jour pour afficher des informations provenant directement de notre [Wiki](User_hub/fr.md). Le système repose désormais sur l\'[addon Help](https   *//github.com/FreeCAD/FreeCAD-Help). Lors de votre première utilisation de l\'outil [Aide](Std_Help/fr.md) ou de l\'outil [Std Qu\'est-ce que c\'est?](Std_WhatsThis/fr.md), il vous sera demandé de l\'installer.

## Interface utilisateur 

+++
| ![](images/Navi_Cube_relnotes_0.20.gif ) | Le cube de navigation a été retravaillé    *                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                | -   Il y a maintenant des faces de bord pour faire pivoter la vue 3D de 45°.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                | -   Une nouvelle préférence [Tourner au plus près](Preferences_Editor/fr#Navigation.md) a été introduite. Si elle est sélectionnée, la vue 3D est tournée vers la position logique la plus proche, basée sur l\'orientation courante du cube, lorsqu\'une face du cube est cliquée. Si vous ne cliquez pas sur une face, vous obtiendrez toujours la même rotation. Pour voir la différence, essayez la même séquence de clics que dans l\'animation, avec et sans l\'option *Tourner au plus près*. |
|                                                                | -   En cliquant sur le nouveau bouton rond dans le coin supérieur droit, vous pouvez rapidement passer à la vue arrière de la scène en cours.                                                                                                                                                                                                                                                                                                                                                                |
|                                                                | -   La taille du cube peut maintenant être ajustée avec la préférence [Taille du cube](Preferences_Editor/fr#Navigation.md).                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                | [Discussion sur le forum](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=52118), [Pull request \#4502](https   *//github.com/FreeCAD/FreeCAD/pull/4502).                                                                                                                                                                                                                                                                                                                                                      |
+++

   
  ![](images/Improved_tooltips_relnotes_0.20.gif )   Des infobulles affichent désormais le nom de la commande dans le titre, ce qui permet aux nouveaux utilisateurs de rechercher plus facilement de l\'aide. À la fin de l\'infobulle, le nom de la commande \"interne\" est ajouté entre parenthèses    * *(Std\_WhatsThis)*. C\'est également le nom de la page qui documente la commande dans le Wiki. [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=34&t=58747), [Pull request \#4978](https   *//github.com/FreeCAD/FreeCAD/pull/4978).
   

   
  ![](images/Std_UserEditMode_relnotes_0.20.gif )   La nouvelle commande [Std Mode d\'édition](Std_UserEditMode/fr.md) permet à l\'utilisateur de choisir le mode d\'édition qui sera utilisé lorsqu\'il double-cliquera sur un objet dans la [Vue en arborescence](Tree_view/fr.md). Cliquez sur l\'image à gauche pour voir une animation de la sélection. Si le mode d\'édition sélectionné n\'est pas applicable, le mode d\'édition par défaut de l\'objet est utilisé à la place. [Pull request \#5110](https   *//github.com/FreeCAD/FreeCAD/pull/5110).
   

+++
| ![](images/Dependencies-selection_relnotes_0.20.png ) | Le menu contextuel de la [Vue en arborescence](Tree_view/fr.md) contient une nouvelle entrée **Ajouter des objets dépendants à la sélection**. |
|                                                                                          | [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=13566), [Pull request \#4133](https   *//github.com/FreeCAD/FreeCAD/pull/4133).                              |
|                                                                                          |                                                                                                                                                                                  |
|                                                                                          | Dans l\'image, l\'objet *Hole001* a été sélectionné et ensuite ses                                                                                                               |
|                                                                                          | dépendances ont été ajoutées à la sélection via le menu contextuel.                                                                                                              |
+++

+++
| <img alt="" src=images/Part_SectionCut_example_relnotes_0.20.png  style="width   *200px;"> | Le nouvel outil [Coupe](Part_SectionCut/fr.md) permet d\'obtenir des coupes non creuses et également persistantes de pièces et d\'assemblages. |
|                                                                                                         | [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=27&t=52441), [Pull request \#4118](https   *//github.com/FreeCAD/FreeCAD/pull/4118).   |
+++

### Autres améliorations de l\'interface utilisateur 

-   Il est maintenant possible d\'utiliser le séparateur décimal appartenant à la langue spécifiée pour l\'interface de FreeCAD. Par exemple, sur un Windows allemand, lorsque vous définissez la langue de l\'interface à **English** et que vous sélectionnez la nouvelle option **Use selected language number format**, le point sera utilisé comme séparateur décimal. Voir les [Préférences](Preferences_Editor/fr#G.C3.A9n.C3.A9ral.md). [Pull request \#6364](https   *//github.com/FreeCAD/FreeCAD/pull/6364)**Remarque**    * Pour les simulations [FEM](FEM_Workbench/fr.md), l\'utilisation du point comme séparateur décimal est fortement recommandée pour obtenir des résultats corrects.
-   Deux nouveaux modes de navigation à la souris ont été ajoutés. L\'un basé sur [OpenSCAD](Mouse_navigation/fr#Mode_OpenSCAD.md), l\'autre sur [TinkerCAD](Mouse_navigation/fr#Mode_TinkerCAD.md). [Discussion du forum OpenSCAD](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=60975), [Discussion du forum TinkerCAD](https   *//forum.freecadweb.org/viewtopic.php?p=544639#p544376), [commit 1](https   *//github.com/FreeCAD/FreeCAD/commit/a1c9ab658c), [commit 2](https   *//github.com/FreeCAD/FreeCAD/commit/ef100d55e9d50), [commit 3](https   *//github.com/FreeCAD/FreeCAD/commit/549e5b5650).
-   Il est maintenant possible de faire un panoramique de la vue du [Graphique de dépendance](Std_DependencyGraph/fr.md) avec la souris. [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=34791), [pull request \#4638](https   *//github.com/FreeCAD/FreeCAD/pull/4638).
-   \* Correction d\'un problème où l\'utilisation de périphériques à stylet (par exemple, la tablette Wacom) était lente au point d\'être complètement inutilisable. [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=45046), [Pull request \#4687](https   *//github.com/FreeCAD/FreeCAD/pull/4687).
-   Le système de coordonnées dans la vue 3D peut être redimensionné dans les préférences dans la section [Affichage → Vue 3D](Preferences_Editor/fr#Vue_3D.md). [Pull request \#5182](https   *//github.com/FreeCAD/FreeCAD/pull/5182)
-   Un nouveau paramètre dans [Préférences → Général](Preferences_Editor/fr#G.C3.A9n.C3.A9ral.md) permet de substituer le séparateur décimal du pavé numérique par le séparateur de la locale appropriée s\'ils sont différents. [Pull request \#3256](https   *//github.com/FreeCAD/FreeCAD/pull/3256) [Pull request \#5150](https   *//github.com/FreeCAD/FreeCAD/pull/5150) [Pull request 5203](https   *//github.com/FreeCAD/FreeCAD/pull/5203)
-   Il est désormais possible de définir la touche **Retour arrière** comme une touche de raccourci autonome sans avoir à spécifier une nouvelle touche modificatrice. [Pull request \#5428](https   *//github.com/FreeCAD/FreeCAD/pull/5428)

## Noyau et API 

### Noyau

   
  <img alt="" src=images/Object_selection_relnotes_0.20.png  style="width   *384px;">   Lorsque vous utilisez **Édition → Copier** ou **Édition → Dupliquer la sélection** pour un objet avec des dépendances, il existe un nouveau bouton **Utiliser les sélections d'origine** dans le dialogue de sélection d\'objet. Cliquez sur ce bouton pour copier/dupliquer uniquement les objets que vous avez sélectionnés à l\'origine avant d\'ouvrir le dialogue, en ignorant les dépendances et en ne tenant pas compte des actions que vous avez pu effectuer pendant que le dialogue était ouvert, comme cocher ou décocher certaines cases. L\'effet est le même que si vous aviez décoché toutes les cases à côté des objets que vous n\'aviez pas sélectionnés à l\'origine et appuyé sur OK. Remarque    * il convient d\'être particulièrement prudent lorsque vous copiez/dupliquez des pages TechDraw. Il est recommandé de copier/dupliquer également tous les enfants de la page (modèles, vues, dimensions, etc.). Sinon, les modifications apportées à une page auront également un impact sur l\'autre page. Par exemple, la suppression d\'une vue sur une page entraîne sa suppression de l\'autre page, ou la suppression d\'une page entraîne la suppression de tout son contenu sur l\'autre page.
   

   
  <img alt="" src=images/PrefPacks_relnotes_0.20.png  style="width   *384px;">   Un nouveau type d\'extension appelé [Kits de préférence](Preference_Packs/fr.md) a été ajouté, permettant à un sous-ensemble du fichier de préférences d\'un utilisateur (user.cfg) d\'être sauvegardé, distribué et facilement appliqué par d\'autres utilisateurs. Les kits de préférences peuvent être utilisés pour distribuer des \"thèmes\", par exemple, en permettant à un développeur d\'inclure à la fois une feuille de style Qt pour les widgets ainsi qu\'un ensemble d\'autres couleurs et styles pour les éléments de l\'interface utilisateur qui ne peuvent pas être définis à l\'aide d\'une feuille de style (par exemple, les couleurs du texte dans l\'éditeur Python ou la vue des rapports, etc.) Tout ce qui peut être configuré via un fichier user.cfg peut être défini à l\'aide d\'un kit de préférences. [Discussion sur le forum](https   *//forum.freecadweb.org/viewtopic.php?f=17&t=62477)
   

   
  <img alt="" src=images/Autoload_relnotes_0.20.png  style="width   *384px;">   Le panneau de préférences \"Ateliers\" a été modifié pour permettre de \"charger automatiquement\" les ateliers au démarrage de FreeCAD.
   

Sous Linux, l\'emplacement par défaut des fichiers de configuration, de données et du cache de FreeCAD a été modifié pour suivre [XDG Base Directory Specification](https   *//specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html). Voici une comparaison de l\'ancien et du nouvel emplacement    *

  Description                 Ancien emplacement   Nouvel emplacement            Valeur par défaut
     
  Fichiers de configuration   \$HOME/.FreeCAD      \$XDG\_CONFIG\_HOME/FreeCAD   \$HOME/.config/FreeCAD
  Fichiers de données         \$HOME/.FreeCAD      \$XDG\_DATA\_HOME/FreeCAD     \$HOME/.local/share/FreeCAD
  Fichiers du cache           /tmp                 \$XDG\_CACHE\_HOME/FreeCAD    \$HOME/.cache/FreeCAD

Si vous souhaitez continuer à utiliser les anciens emplacements, vous pouvez démarrer FreeCAD avec l\'option `--keep-deprecated-paths`.

### API

FreeCAD a reçu de nombreuses nouvelles fonctions de l\'API en Python    *


<div class="mw-collapsible mw-collapsed toccolours">

#### Nouvelles API en Python 


<div class="mw-collapsible-content">

-   *ChFi2d\_AnaFilletAlgoPy*    * Un algorithme analytique pour le calcul des congés. [commit f94ab3ec](https   *//github.com/FreeCAD/FreeCAD/commit/f94ab3ec)
-   *ChFi2d\_ChamferAPIPy*    * Algorithme qui crée un chanfrein entre deux arêtes linéaires. [commit 30f8015e7](https   *//github.com/FreeCAD/FreeCAD/commit/30f8015e7)

-   *Circle2dPy   *   *getCircleCenter*    * Récupérer le centre du cercle défini par trois points. [commit 3dc91fa2](https   *//github.com/FreeCAD/FreeCAD/commit/3dc91fa2)

-   *ComplexGeoDataPy   *   *applyRotation*    * Applique une rotation supplémentaire au placement. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy   *   *applyTranslation*    * Applique une translation supplémentaire au placement. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy   *   *countSubElements*    * Retourne le nombre d\'éléments d\'un type. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy   *   *getElementTypes*    * Retourne une liste de types d\'éléments. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy   *   *getFaces*    * Retourne un tuple de points et de triangles avec une précision donnée. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy   *   *getLines*    * Retourne un tuple de points et de lignes avec une précision donnée. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy   *   *getLinesFromSubelement*    * Retourne les sommets et les lignes d\'un sous-élément. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy   *   *getPoints*    * Retourne un tuple de points et de normales avec une précision donnée. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)
-   *ComplexGeoDataPy   *   *transformGeometry*    * Applique une transformation à la géométrie sous-jacente. [commit 32592de8](https   *//github.com/FreeCAD/FreeCAD/commit/32592de8)

-   *ControlPy   *   *showModelView*    * Affiche la vue du modèle. [commit 033bf619](https   *//github.com/FreeCAD/FreeCAD/commit/033bf619)

-   *DocumentPy   *   *clearDocument*    * Efface tout le document. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy   *   *getFileName*    * Pour un document standard, retourne la propriété du nom du fichier. Pour un document temporaire, retourne son répertoire transitoire. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy   *   *getProgramVersion*    * Récupère la version du programme avec lequel un fichier de projet a été créé. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy   *   *isClosable*    * Vérifie si le document peut être fermé. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy   *   *isSaved*    * Vérifie si le document est enregistré. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy   *   *isTouched*    * Vérifie si un objet est dans l\'état touché. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy   *   *mustExecute*    * Vérifie si un objet doit être recalculé. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy   *   *purgeTouched*    * Purge l\'état touché de tous les objets. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)
-   *DocumentPy   *   *setClosable*    * Définit un drapeau (flag) qui permet ou interdit de fermer un document. [commit 526dc1a0](https   *//github.com/FreeCAD/FreeCAD/commit/526dc1a0)

-   *DrawPagePy   *   *requestPaint*    * Peint une page TechDraw. [commit 79f9fb68](https   *//github.com/FreeCAD/FreeCAD/commit/79f9fb68)

-   *HLRBRep\_AlgoPy*    * Pour accéder à la suppression des lignes cachées de Part (HLR). [commit 73a98671](https   *//github.com/FreeCAD/FreeCAD/commit/73a98671)
-   *HLRBRep\_PolyAlgoPy*    * Pour accéder à la suppression des polylignes cachées de Part (HLR). [commit ea85cf5e](https   *//github.com/FreeCAD/FreeCAD/commit/ea85cf5e)
-   *HLRToShapePy*    * Pour accéder à la suppression des lignes cachées (HLR) de Part. [commit 73a98671](https   *//github.com/FreeCAD/FreeCAD/commit/73a98671)
-   *PolyHLRToShapePy*    * Pour accéder à la suppression des polylignes cachées (HLR) de Part. [commit ea85cf5e](https   *//github.com/FreeCAD/FreeCAD/commit/ea85cf5e)

-   *MDIViewPy   *   *printPdf*    * Imprime un PDF. [commit c93031da](https   *//github.com/FreeCAD/FreeCAD/commit/c93031da)
-   *MDIViewPy   *   *printPreview*    * Imprime un aperçu. [commit c93031da](https   *//github.com/FreeCAD/FreeCAD/commit/c93031da)
-   *MDIViewPy   *   *printView*    * Imprime une vue. [commit c93031da](https   *//github.com/FreeCAD/FreeCAD/commit/c93031da)
-   *MDIViewPy   *   *redoActions*    * Refait les actions. [commit c93031da](https   *//github.com/FreeCAD/FreeCAD/commit/c93031da)
-   *MDIViewPy   *   *undoActions*    * Annule les actions. [commit c93031da](https   *//github.com/FreeCAD/FreeCAD/commit/c93031da)

-   *PrecisionPy*    * Pour accéder à la précision définie par le noyau d\'OpenCascade. [commit 20b86e55](https   *//github.com/FreeCAD/FreeCAD/commit/20b86e55)

-   *PropertyContainerPy   *   *setDocumentationOfProperty*    * Définit la chaîne de documentation d\'une propriété dynamique de cette classe. [commit 8cf3cf33](https   *//github.com/FreeCAD/FreeCAD/commit/8cf3cf33)
-   *PropertyContainerPy   *   *setGroupOfProperty*    * Fixe le nom du groupe d\'une propriété dynamique. [commit 8cf3cf33](https   *//github.com/FreeCAD/FreeCAD/commit/8cf3cf33)

-   *PythonWorkbenchPy   *   *reloadActive*    * Recharge l\'atelier actif après avoir modifié les menus ou les barres d\'outils. [commit 0bbc253d](https   *//github.com/FreeCAD/FreeCAD/commit/0bbc253d)

-   *RotationPy   *   *fromEuler*    * Définit les angles d\'Euler d\'une rotation ou obtient les angles d\'Euler dans une séquence donnée pour une rotation. [commit 951a0be9](https   *//github.com/FreeCAD/FreeCAD/commit/951a0be9)
-   *RotationPy   *   *toEulerAngles*    * Obtient les angles d\'Euler dans une séquence donnée pour cette rotation\... [commit c1454dfb](https   *//github.com/FreeCAD/FreeCAD/commit/c1454dfb)

-   *SpreadsheetViewPy*    * Pour accéder aux feuilles de tableur. [commit 6e713628](https   *//github.com/FreeCAD/FreeCAD/commit/6e713628)

-   *UnitsApi   *   *sToNumber*    * Convertit une quantité ou un flottant en une chaîne de caractères. [commit befbd95d](https   *//github.com/FreeCAD/FreeCAD/commit/befbd95d)

-   *View3DInventorPy   *   *getCornerCrossSize*    * Retourne la taille de la croix de l\'axe du coin en cours d\'utilisation. [commit 9d15df29](https   *//github.com/FreeCAD/FreeCAD/commit/9d15df29)
-   *View3DInventorPy   *   *setPopupMenuEnabled*    * Active le menu popup. [commit 9def811a](https   *//github.com/FreeCAD/FreeCAD/commit/9def811a)
-   *View3DInventorPy   *   *isCornerCrossVisible*    * Retourne la visibilité de la croix de l\'axe du coin. [commit 9d15df29](https   *//github.com/FreeCAD/FreeCAD/commit/9d15df29)
-   *View3DInventorPy   *   *isPopupMenuEnabled*    * Retourne si le menu popup est activé. [commit 9def811a](https   *//github.com/FreeCAD/FreeCAD/commit/9def811a)
-   *View3DInventorPy   *   *projectPointToLine*    * Projette le point 2d donné sur une ligne. [commit b6527a70](https   *//github.com/FreeCAD/FreeCAD/commit/b6527a70)
-   *View3DInventorPy   *   *setCornerCrossSize*    * Définit la taille de la croix de l\'axe du coin. [commit 9d15df29](https   *//github.com/FreeCAD/FreeCAD/commit/9d15df29)
-   *View3DInventorPy   *   *setCornerCrossVisible*    * Définit la visibilité de la croix de l\'axe du coin. [commit 9d15df29](https   *//github.com/FreeCAD/FreeCAD/commit/9d15df29)

-   *ViewProviderSpreadsheetPy*    * Pour gérer les cellules des feuilles de tableur. [commit 16bbe123](https   *//github.com/FreeCAD/FreeCAD/commit/16bbe123) et [commit 093f15dc](https   *//github.com/FreeCAD/FreeCAD/commit/093f15dc)


</div>

#### API en Python modifiées 

-   *MeshObject   *   *trim(base, normal)* a été changé en *MeshPy   *   *trimByPlane(base, normal)*    * Découpe le maillage avec un plan donné. [commit 837de28e](https   *//github.com/FreeCAD/FreeCAD/commit/837de28e)


</div>

## Gestionnaire d\'Addon 

   
  <img alt="" src=images/AddonManagerExpanded_relnotes_0.20.png  style="width   *400px;">   Le [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) a été modifié pour prendre en charge la distribution des packs de préférences et pour afficher les informations contenues dans les métadonnées d\'un addon. Le gestionnaire d\'addons comprend également une prise en charge améliorée des addons dont le code source est situé à plusieurs emplacements d\'hébergement git différents. La prise en charge de la mise en réseau a été améliorée afin de fournir une gestion plus robuste des connexions SSL et une prise en charge des proxys nécessitant une authentification. La prise en charge a été ajoutée pour ajouter automatiquement des boutons de macro à la barre d\'outils après l\'installation, pour désactiver les modules complémentaires sans les supprimer et pour changer la branche git d\'un module complémentaire qui est extraite. Enfin, l\'interface utilisateur a été modifiée pour améliorer la recherche et l\'affichage des différents filtres de liste.
   

## Atelier Arch 

++++
| <img alt="" src=images/ArchWindow_Placement_1r_relnotes_0.20.png  style="width   *250px;"> | <img alt="" src=images/ArchWindow_Placement_2r_relnotes_0.20.png  style="width   *250px;"> | **Atelier SketchArch**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                         |                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                         |                                                                                                         | Grâce à <img alt="" src=images/Attach_in_SketchArch.svg  style="width   *20px;"> [Attach Feature](https   *//github.com/paullee0/FreeCAD_SketchArch), il est désormais possible de placer une <img alt="" src=images/Arch_Window.svg  style="width   *20px;"> [Fenêtre](Arch_Window/fr.md) et un <img alt="" src=images/Arch_Equipment.svg  style="width   *20px;"> [Équipement](Arch_Equipment/fr.md) de manière paramétrique et intuitive par rapport aux <img alt="" src=images/Arch_Wall.svg  style="width   *20px;"> [Murs](Arch_Wall/fr.md). Pour utiliser cette fonctionnalité, il faut installé l\'<img alt="" src=images/SketchArch_Workbench.svg  style="width   *20px;"> [atelier SketchArch](https   *//github.com/paullee0/FreeCAD_SketchArch) expérimental externe. [Add-on et ReadMe sur Github](https   *//github.com/paullee0/FreeCAD_SketchArch) (Pas encore disponible dans le [Gestionnaire d\'Addon](Std_AddonMgr/fr.md)). |
|                                                                                                         |                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                         |                                                                                                         | [Discussion sur le forum](https   *//forum.freecadweb.org/viewtopic.php?f=23&t=50802)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
++++

+++
| <img alt="" src=images/NewArchStructureProperties_relnotes_0.20.jpg  style="width   *250px;"> | **Nouvelles propriétés pour les objets Arch Structure**    *                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               | **BasePerpendicularToTool**    * crée une copie de la Base (profil d\'extrusion) au début de l\'outil (chemin d\'extrusion) et la place perpendiculairement au premier bord de l\'outil. C\'est la même chose que de fixer la Base avec MapMode=NormalToEdge, mais c\'est automatique et cela permet de réutiliser le même objet Base pour plusieurs structures. Lorsque BasePerpendicularToTool = True, d\'autres propriétés contrôlent le placement de la Base par rapport à l\'axe de l\'outil. Elles sont présentées dans l\'image ci-jointe.                                          |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               | -   **ToolOffsetFirst** et **ToolOffsetLast**    * étendent/découpent la structure au début et à la fin respectivement (la longueur réelle de la structure est disponible dans la propriété ComputedLength en lecture seule).                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                               | -   **BaseRotation**    * fait tourner la Base (la rotation se fait autour du point \"(0,0)\" de la base qui est le centre pour [Arch Profilés](Arch_Profile/fr.md), l\'origine pour les esquisses et généralement le premier point pour [Draft Polylignes](Draft_Wire/fr.md)).                                                                                                                                                                                                                                                                                            |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                               | -   **BaseOffsetX** et **BaseOffsetY**    * déplacent la Base (profil d\'extrusion).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                               | -   **BaseMirror**    * miroir de la Base (profil d\'extrusion).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               | Une nouvelle commande **Create multiple Arch Structure** a également été ajoutée. Elle utilise le premier objet sélectionné comme Base, et crée des objets Arch Structures pour chaque bord des autres objets sélectionnés. Ensuite, les propriétés de chaque objet Structure peuvent être ajustées dans l\'éditeur de propriétés. Cette commande a été ajoutée pour le flux de travail avec une esquisse maître (il y a un risque de problème de dénomination topologique à moins de créer une copie non-paramétrique de l\'esquisse maître ou d\'utiliser la version de Realthunder). |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               | La prise en charge des *données 2D* telles que le tracé, les hachures, les textes et les dimensions est maintenant activée dans l\'importation et l\'exportation IFC, ce qui contribue à rendre le format IFC de plus en plus adapté au travail traditionnel de CAO 2D. Un effort similaire est en cours dans [BlenderBIM](https   *//blenderbim.org). D\'autres améliorations du mode de travail 2D sont documentées [dans ce fil de discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?p=563067#p563067).                                                                   |
|                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                               | [Discussion sur le forum](https   *//forum.freecadweb.org/viewtopic.php?f=23&t=43228&start=60), [Pull request \#3229](https   *//github.com/FreeCAD/FreeCAD/pull/3229)                                                                                                                                                                                                                                                                                                                                                                                                                        |
+++

## Atelier Draft 

-   Une case à cocher **Global** a été ajoutée au panneau des tâches de nombreuses commandes de dessin. Le fait de la cocher permet de saisir des coordonnées dans le système de coordonnées global même si le [plan de travail](Draft_SelectPlane/fr.md) n\'est pas aligné avec le plan XY global.

-   La commande <img alt="" src=images/Draft_Hatch.svg  style="width   *24px;"> [Draft Hachure](Draft_Hatch/fr.md) a été introduite. Elle crée des hachures sur les faces d\'un objet sélectionné à l\'aide de motifs provenant de fichiers PAT d\'AutoCAD.

-   La commande <img alt="" src=images/Draft_AddNamedGroup.svg  style="width   *24px;"> [Draft Nommer un groupe](Draft_AddNamedGroup/fr.md) a été introduite. La commande<img alt="" src=images/Draft_AddToGroup.svg  style="width   *24px;"> [Draft Déplacer vers un groupe](Draft_AddToGroup/fr.md) a été étendue avec la même fonctionnalité.

-   Le travail sur la commande <img alt="" src=images/Draft_SetStyle.svg  style="width   *24px;"> [Draft Définir le style](Draft_SetStyle/fr.md), toujours en cours dans FreeCAD version 0.19, a été terminé.

-   Une option d\'édition par double-clic a été ajoutée pour <img alt="" src=images/Draft_Text.svg  style="width   *24px;"> [Draft Texte](Draft_Text/fr.md). Elle ouvre le même panneau de tâches d\'édition que celui utilisé lors de la création d\'un texte.

-   Pour <img alt="" src=images/Draft_Dimension.svg  style="width   *24px;"> [Draft Dimensions](Draft_Dimension/fr.md), la {{Value|arch}} **Unit Override** pour les dimensions architecturales impériales a été introduite.

-   Les objets <img alt="" src=images/Draft_Shape2DView.svg  style="width   *24px;"> [Draft Vue 2D d\'une forme](Draft_Shape2DView/fr.md) ont maintenant une propriété **Auto Update**. La définition de cette propriété à {{False}} peut s\'avérer utile si un document contient de nombreux objets *Draft Vue 2D d\'une forme* ou s\'ils sont complexes.

-   Il est maintenant possible d\'inverser une [Draft Polyligne](Draft_Wire/fr.md) via le menu contextuel <img alt="" src=images/Draft_Edit.svg  style="width   *24px;"> [Draft Éditer](Draft_Edit/fr.md). [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=23&t=58643&start=20), [Pull request \#4811](https   *//github.com/FreeCAD/FreeCAD/pull/4811).

### Autres améliorations de Draft 

-   Correction de [Draft Aimantation Grille](Draft_Snap_Grid/fr.md) lorsque le curseur se trouve sur une face. [Discussion du forum](https   *//forum.freecad.org/viewtopic.php?f=23&t=62274). [Git commit](https   *//github.com/FreeCAD/FreeCAD/commit/1761eb8ce).

-   Les nouveaux [Draft Textes](Draft_Text/fr.md) sont désormais alignés sur le [plan de travail](Draft_SelectPlane/fr.md), [Pull request \#5092](https   *//github.com/FreeCAD/FreeCAD/pull/5092).

-   La prise en charge de deux convertisseurs DWG a été ajoutée    * [LibreDWG](https   *//www.gnu.org/software/libredwg) et [QCAD pro](https   *//qcad.org/en/qcad-command-line-tools#dwg2dwg). Voir [Préférences d\'Import Export](Import_Export_Preferences/fr#DWG.md) et [FreeCAD et l\'importation DWG](FreeCAD_and_DWG_Import/fr.md) pour plus d\'informations.

## Atelier FEM 

   
  <img alt="" src=images/FEM_Z88-settings_relnotes_0.20.png  style="width   *384px;">Les nouveaux paramètres Z88 et leurs valeurs par défaut                                                                                               Le [solveur Z88](FEM_SolverZ88/fr.md) est maintenant entièrement utilisable. Vous pouvez spécifier la méthode de solveur et modifier les paramètres de mémoire. Les nouvelles valeurs par défaut vous permettent également d\'effectuer directement des simulations complexes. [commit d035bbc1ca et suivants](https   *//github.com/FreeCAD/FreeCAD/commit/d035bbc1ca)
  <img alt="" src=images/FEM_buckling-analysis_relnotes_0.20.gif  style="width   *384px;">Résultat d\'une analyse de flambage linéaire.Cliquez sur l\'image pour voir l\'animation.                                     Il est maintenant possible d\'effectuer des analyses de flambage en utilisant le solveur [Calculix](FEM_SolverCalculixCxxtools/fr.md). [Pull request \#4379](https   *//github.com/FreeCAD/FreeCAD/pull/4379)
  <img alt="" src=images/FEM_Gmsh-MeshSizeFromCurvature_relnotes_0.20.png  style="width   *384px;">Effet de \"la taille du maillage à partir de la courbure\". À gauche    * réglé sur 12, à droite    * désactivé                 Il existe une nouvelle propriété pour le mailleur [Gmsh](FEM_MeshGmshFromShape/fr.md). Le nombre d\'éléments de maillage par $2\pi$ fois le rayon de la courbure peut être spécifié. La valeur par défaut est 12 et pour obtenir un maillage plus fin aux petits coins ou trous, cette valeur peut être augmentée pour de meilleurs résultats. Cette fonctionnalité nécessite Gmsh 4.8 ou plus récent. [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=56401), [Pull request \#4596](https   *//github.com/FreeCAD/FreeCAD/pull/4596)
  <img alt="" src=images/FEM_Gmsh-RecombinationAlgorithm_relnotes_0.20.png  style="width   *384px;">Effet de l\'algorithme de recombinaison. À gauche    * en utilisant *Simple*, à droite    * en utilisant *Simple full-quad*   FreeCAD permet maintenant de sélectionner un algorithme ainsi que la recombinaison de maillage 3D pour le mailleur [Gmsh](FEM_MeshGmshFromShape/fr.md). Pour plus de détails sur la recombinaison des éléments de maillage, [FEM Maillage MEF à partir d\'une forme avec Gmsh](FEM_MeshGmshFromShape/fr#Recombinaison_d.27.C3.A9l.C3.A9ments.md). [Pull request \#4706](https   *//github.com/FreeCAD/FreeCAD/pull/4706)
   

### Autres améliorations de FEM 

-   **Important    *** A partir de cette version, FreeCAD utilisera les [unités SI](https   *//fr.wikipedia.org/wiki/Syst%C3%A8me_international_d%27unit%C3%A9s) (m, kg, s, K, A, mol, cd) pour écrire les fichiers d\'entrée du [solveur Elmer](FEM_SolverElmer/fr.md) (*case.sif* et *mesh.nodes*). Ceci est indépendant du [système d\'unités](Preferences_Editor/fr#Unit.C3.A9s.md) utilisé par FreeCAD.
-   **Important    *** A partir de cette version, l\'échelle des [résultats](FEM_PostPipelineFromResult/fr.md) et de leurs [filtres](FEM_Workbench/fr#Menu_   *_R.C3.A9sultats.md) utilisera les unités SI (m, kg, s, K, A, mol, cd). Ainsi, le déplacement est donné en mètre, la contrainte en Pascal. Ceci s\'applique à tous les [systèmes d\'unités](Preferences_Editor/fr#Unit.C3.A9s.md) dérivés du SI de FreeCAD .
-   Le maillage avec le solveur [Calculix](FEM_SolverCalculixCxxtools/fr.md) utilise désormais tous les cœurs du processeur. [Pull request \#6374](https   *//github.com/FreeCAD/FreeCAD/pull/6374)
-   Le maillage avec [Gmsh](FEM_MeshGmshFromShape/fr.md) utilise désormais tous les cœurs du CPU. [Pull request \#6370](https   *//github.com/FreeCAD/FreeCAD/pull/6370)
-   L\'ordre des éléments des maillages [Gmsh](FEM_MeshGmshFromShape/fr.md) peut être modifié via la boîte de dialogue de maillage. [Pull request \#4660](https   *//github.com/FreeCAD/FreeCAD/pull/4660)
-   Le filtre de résultat [Données du filtre d\'écrêtage du point](FEM_PostFilterDataAtPoint/fr.md) fonctionne maintenant réellement    * On obtient des informations à partir des mailles de résultat en cliquant dessus ou en spécifiant une coordonnée de maille.
-   Une nouvelle contrainte a été ajoutée    * **Modèle → Contraintes mécaniques → [<img src=images/FEM_ConstraintCentrif.svg style="width   *16px"> [Constrainte centrifuge](FEM_ConstraintCentrif/fr.md)**. [Pull request \#4738](https   *//github.com/FreeCAD/FreeCAD/pull/4738)
-   Un nouveau solveur a été ajouté    * **Solveur → [<img src=images/FEM_SolverMystran.svg style="width   *16px"> [Solveur Mystran](FEM_SolverMystran/fr.md)**. De nombreux commits.
-   Une nouvelle contrainte a été ajoutée    * **Modèle → Contraintes géométriques → [<img src=images/FEM_ConstraintSpring.svg style="width   *16px"> [Contrainte ressort](FEM_ConstraintSpring/fr.md)**. [Pull request \#4982](https   *//github.com/FreeCAD/FreeCAD/pull/4982)
-   Il est maintenant possible d\'avoir des [pipelines de résultats](FEM_PostPipelineFromResult/fr.md) avec plusieurs filtres, où certains prennent d\'autres filtres en entrée, et d\'autres prennent les résultats directement dans le pipeline. [commit 708a300b](https   *//github.com/FreeCAD/FreeCAD/commit/708a300b)
-   Les cartes de matériaux peuvent désormais contenir des valeurs de conductivité électrique. [Pull request \#4647](https   *//github.com/FreeCAD/FreeCAD/pull/4647)
-   Cartes de matériaux ajoutées pour l\'azote et l\'argon. [Pull request \#4649](https   *//github.com/FreeCAD/FreeCAD/pull/4649)
-   Ajout de la prise en charge des algorithmes de maillage *\"HXT\"* (3D) et *\"Packing Parallelograms\"* (2D) de [Gmsh](FEM_MeshGmshFromShape/fr.md). [Pull request \#4654](https   *//github.com/FreeCAD/FreeCAD/pull/4654)
-   Permet de spécifier un algorithme pour la propriété *\"Optimisation d\'ordre élevé\"* de [Gmsh](FEM_MeshGmshFromShape/fr#Propriétés.md). [Pull request \#4705](https   *//github.com/FreeCAD/FreeCAD/pull/4705)
-   Les matériaux solides non linéaires à durcissement simple peuvent désormais avoir un nombre arbitraire de limites d\'élasticité. [Pull request \#5024](https   *//github.com/FreeCAD/FreeCAD/pull/5024)
-   Ajout/suppression modale d\'entités géométriques aux contraintes agissant aux limites. [Pull request \#5117](https   *//github.com/FreeCAD/FreeCAD/pull/5117)
-   La plupart des dialogues de contraintes FEM se comportent désormais de manière uniforme et offrent les mêmes fonctionnalités de sélection des objets 3D. [Pull request \#5391](https   *//github.com/FreeCAD/FreeCAD/pull/5391)

## Exportation

-   DXF    * Le bloc d\'unité manquant a été ajouté au fichier header14.rub. [Pull request \#5793](https   *//github.com/FreeCAD/FreeCAD/issues/5793)

## Atelier Mesh 

### Amélioration du support des éléments NASTRAN GRID 

L\'outil d\'importation de Mesh supporte maintenant l\'élément \"GRID\*\" de haute précision. L\'élément \"GRID\" de précision standard a également été amélioré et supporte maintenant les entrées numériques délimitées par des espaces ainsi que les entrées à largeur de champ fixe, conformément à la documentation du format NASTRAN95.

### Autres améliorations de Mesh 

Correction des faux négatifs lors des tests d\'auto-intersection lorsque les facettes sont coplanaires    * [Pull request \#5002](https   *//github.com/FreeCAD/FreeCAD/pull/5002).

## Atelier OpenSCAD 

L\'interopérabilité avec OpenSCAD a été améliorée, en ajoutant le support de plusieurs opérations manquantes dans les versions précédentes (extrusion linéaire avec rotations, extrusions rotatives). Plusieurs opérations ont été modifiées pour fournir des équivalents d\'objets FreeCAD améliorés, en particulier pour les extrusions torsadées. La génération de surfaces à partir de données discrètes a été modifiée pour donner des résultats plus proches de ceux d\'OpenSCAD, plutôt que des surfaces cannelées.

De nouvelles options ont été ajoutées pour supporter l\'exécution de FreeCAD, OpenSCAD, ou les deux, dans des environnements de bacs à sable tels que les AppImages et les paquets Snap    * les données peuvent maintenant être transférées vers et depuis OpenSCAD via le mécanisme standard de répertoire temporaire, via un répertoire temporaire spécifié par l\'utilisateur auquel les deux exécutables ont accès, ou, nouveauté d\'OpenSCAD 2021.1, via un mécanisme de \"stdout pipe\", contournant entièrement les fichiers temporaires.

+++
| <img alt="" src=images/OpenSCAD_AddElement_relnotes_0.20.png  style="width   *384px;"> | Les options suivantes ont été ajoutées au panneau des tâches de la fonction [Ajout d\'un élément OpenSCAD](OpenSCAD_AddOpenSCADElement/fr.md)    * |
|                                                                                                 |                                                                                                                                                         |
|                                                                                                 | Load - charger un fichier scad                                                                                                                        |
|                                                                                                 | Save - sauvegarder un fichier scad                                                                                                                    |
|                                                                                                 | Refresh - mise à jour de la vue FreeCAD                                                                                                               |
|                                                                                                 | Clear - effacer la saisie de texte                                                                                                                    |
|                                                                                                 |                                                                                                                                                         |
|                                                                                                 | Une nouvelle boîte de dialogue donne des informations sur les erreurs d\'OpenSCAD.                                                                      |
+++

## Atelier Part 

   
  <img alt="" src=images/Part_Extrusion-inner-structures_relnotes_0.20.png  style="width   *384px;">Extrusion conique d\'une esquisse avec une structure interne.   L\'[extrusion](Part_Extrude/fr.md) conique de structures internes donne désormais des résultats utilisables. Auparavant, les structures internes étaient extrudées comme si elles étaient autonomes et ne faisaient pas partie d\'une structure. [Pull request \#5367](https   *//github.com/FreeCAD/FreeCAD/pull/5367)
   

### Autres améliorations de Part 

-   La boîte de dialogue pour éditer des [Cylindres](Part_Cylinder/fr.md) permet maintenant de spécifier un angle relatif à la normale du plan d\'attache choisi. De cette façon, on peut créer des cylindres obliques. [Pull request \#4708](https   *//github.com/FreeCAD/FreeCAD/pull/4708)
-   L\'outil [Définir les couleurs](Part_FaceColors/fr.md) permet maintenant aussi de définir la transparence (*canal Alpha*) des faces. Cette transparence peut être [exportée](Import_Export/fr.md), ce qui permet par exemple de créer des fichiers STEP avec des pièces transparentes.
-   Les commandes suivantes prennent désormais en charge App   *   *Links    * [Lissage](Part_Loft/fr.md), [Balayage](Part_Sweep/fr.md), [Extrusion](Part_Extrude/fr.md), [Révolution](Part_Revolve/fr.md), [Inverser les formes](Part_ReverseShapes/fr.md), [Miroir](Part_Mirror/fr.md), [Décalage 2D](Part_Offset2D/fr.md), [Décalage 3D](Part_Offset/fr.md), [Vérifier la géométrie](Part_CheckGeometry/fr.md), [Surface réglée](Part_RuledSurface/fr.md), [Coupes](Part_CrossSections/fr.md), et [Évidement](Part_Thickness/fr.md). [Pull request \#6478](https   *//github.com/FreeCAD/FreeCAD/pull/6478)

## Atelier PartDesign 

+++
| <img alt="" src=images/PD_Pad-Length-along-reference_relnotes_0.20.gif  style="width   *384px;">Extrusion le long d\'une arête du modèle.Cliquez sur l\'image pour voir l\'animation.                                                                                           | Il y a une nouvelle option pour [extruder](PartDesign_Pad/fr.md) le long de la direction d\'un bord dans le modèle 3D. [Pull request \#4685](https   *//github.com/FreeCAD/FreeCAD/pull/4685)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+++
| <img alt="" src=images/PartDesign_Chamfer_Face_Selection_relnotes_0.20.png  style="width   *384px;">                                                                                                                                                                                                        | Lorsque la distance et l\'angle sont spécifiés dans l\'outil [Chanfrein](PartDesign_Chamfer/fr.md) et que des faces sont sélectionnées, la distance sera appliquée le long des faces sélectionnées. De même, si deux distances sont spécifiées, la taille à 1 sera appliquée le long de la face sélectionnée. Ce comportement peut être remplacé par l\'autre face en utilisant le bouton de changement de direction. [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=19&t=62084), [Pull request \#5039](https   *//github.com/FreeCAD/FreeCAD/pull/5039).                                                                                                                                                                                                                                                                                                                   |
+++
| <img alt="" src=images/PartDesign_Loft_Vertex_relnotes_0.20.png  style="width   *384px;">.Un lissage avec plusieurs sections, la dernière étant un sommet.                                                                                                                                           | Il est désormais possible de créer un [Lissage additif](PartDesign_AdditiveLoft/fr.md) ou [Lissage soustractif](PartDesign_SubtractiveLoft/fr.md), ou un [Balayage additif](PartDesign_AdditivePipe/fr.md) ou [Balayage soustractif](PartDesign_SubtractivePipe/fr.md) vers ou depuis un sommet [Vertex](Glossary/fr#V.md) d\'une esquisse ou d\'un corps. Cela permet de créer des pyramides par exemple.**Note**    * Les sommets des esquisses sont créés en tant que géométrie de construction. Pour les utiliser comme points d\'extrémité de lissages, vous devez d\'abord [les changer en géométrie normale](Sketcher_ToggleConstruction/fr.md). [Pull request \#5170](https   *//github.com/FreeCAD/FreeCAD/pull/5170) (pour les lissages), [Pull request \#5193](https   *//github.com/FreeCAD/FreeCAD/pull/5193) (pour les balayages) |
+++
| <img alt="" src=images/PD_Pad-Taper-angle_relnotes_0.20.png  style="width   *384px;">Une cavité conique dans une protrusion non conique.                                                                                                                                                                 | Les boîtes de dialogue de [Protrusion](PartDesign_Pad/fr.md) et de [Cavité](PartDesign_Pocket/fr.md) propose de définir un angle d\'effilement pour l\'extrusion. [Pull request \#5357](https   *//github.com/FreeCAD/FreeCAD/pull/5357)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+++
| <img alt="" src=images/PD_Pocket-direction_relnotes_0.20.gif  style="width   *384px;">Cavité selon différentes directions.Cliquez sur l\'image pour voir l\'animation.                                                                                                                    | Il est maintenant possible de spécifier la direction pour l\'[extrusion](PartDesign_Pocket/fr.md) de la cavité. [Pull request \#5164](https   *//github.com/FreeCAD/FreeCAD/pull/5164)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+++
| <img alt="" src=images/PartDesign_Cylinder_direction_relnotes_0.20.png  style="width   *384px;">                                                                                                                                                                                                                | La boîte de dialogue pour éditer un [Cylindre](PartDesign_AdditiveCylinder/fr.md) (additif et soustractif) permet maintenant de spécifier un angle par rapport à la normale du plan d\'attache choisi. De cette façon, on peut créer des cylindres obliques. [Pull request \#4708](https   *//github.com/FreeCAD/FreeCAD/pull/4708)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+++
| <img alt="" src=images/PartDesign_Helix_Growth_relnotes_0.20.png  style="width   *384px;">.                                                                                                                                                                                                                       | La fonction [Hélice](PartDesign_AdditiveHelix/fr.md) a le nouveau mode **Hauteur-Tours-Croissance** pour créer des spirales plates. [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=19&t=56378) [Pull request \#4590](https   *//github.com/FreeCAD/FreeCAD/pull/4590)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+++
| <img alt="" src=images/PartDesign_Islands-Extrude_relnotes_0.20.png  style="width   *384px;">Une seule protrusion et une seule [Révolution](PartDesign_Revolution/fr.md) avec des profils imbriqués. La protrusion de base n\'est là que pour garantir que la pièce soit un seul solide. | Toutes les fonctions de PartDesign qui peuvent extruder des esquisses peuvent désormais gérer les esquisses avec des profils imbriqués qui forment des îles. Par exemple, il est possible de [faire tourner](PartDesign_Revolution/fr.md) une esquisse constituée de 3 cercles imbriqués avec le même point central.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                    | **Remarque**    * L\'extrusion de profils imbriqués ne fonctionne que si le résultat est toujours un seul corps. [Pull request \#6381](https   *//github.com/FreeCAD/FreeCAD/pull/6381)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+++
| <img alt="" src=images/PD_Pad-Length-alog-direction_relnotes_0.20.gif  style="width   *384px;">Effet de la nouvelle option \"Longueur le long de la normale de l\'esquisse\".Cliquez sur l\'image pour voir l\'animation.                                                        | Nouvelle option pour [extruder](PartDesign_Pad/fr.md) d\'une certaine longueur le long de la direction. La longueur est mesurée le long de la normale de l\'esquisse ou le long de la direction personnalisée. [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=17&t=50466), [Pull request \#3893](https   *//github.com/FreeCAD/FreeCAD/pull/3893)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+++
| <img alt="" src=images/PartDesign_Hole_thread_relnotes_0.20.PNG  style="width   *384px;">                                                                                                                                                                                                                              | La fonction [Perçage](PartDesign_Hole/fr.md) peut désormais modéliser de véritables filets. [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=34&t=54240), [Pull request \#4274](https   *//github.com/FreeCAD/FreeCAD/pull/4274)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+++
|                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+++

### Autres améliorations de PartDesign 

-   Avec la fonction [Hélice](PartDesign_AdditiveHelix/fr.md), on peut désormais utiliser la normale de l\'esquisse comme axe. [Pull request \#5199](https   *//github.com/FreeCAD/FreeCAD/pull/5199)
-   La fonction [Pignon](PartDesign_Sprocket/fr.md) permet désormais de créer également des pignons normalisés ISO. [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=44525#p478369) [Pull request \#4478](https   *//github.com/FreeCAD/FreeCAD/pull/4478)
-   Les fonctions [Lissage](PartDesign_AdditiveLoft/fr.md) et [Balayage](PartDesign_AdditivePipe/fr.md) permettent désormais d\'utiliser les faces du corps pour les sections. [Pull request \#5155](https   *//github.com/FreeCAD/FreeCAD/pull/5155)
-   Il est désormais possible de sélectionner plusieurs faces avant d\'ouvrir la boîte de dialogue de [Protrusion](PartDesign_Pad/fr.md) ou [Cavité](PartDesign_Pocket/fr.md). Dans ce cas, la première face sélectionnée sera utilisée pour déterminer la direction par défaut de la protrusion/cavité. [commit d34a5616](https   *//github.com/FreeCAD/FreeCAD/commit/d34a5616a2b38c96ad05f9a0763ba7504dfb814d)
-   Il est possible de décaler les [Sous formes liées](PartDesign_SubShapeBinder/fr.md) si elles sont basées sur des arêtes, des lignes ou des faces. [Pull request \#6338](https   *//github.com/FreeCAD/FreeCAD/pull/6338)
-   Les [Sous formes liées](PartDesign_SubShapeBinder/fr.md) possède maintenant la propriété *Refine* comme tous les autres objets PartDesign. [Pull request \#6550](https   *//github.com/FreeCAD/FreeCAD/pull/6550)
-   Dans les boîtes de dialogue de [Chanfrein](PartDesign_Chamfer/fr.md) et de [Congé](PartDesign_Fillet/fr.md), tous les bords d\'un corps peuvent être sélectionnés via le menu contextuel en mode Ajout. [Pull request \#5269](https   *//github.com/FreeCAD/FreeCAD/pull/5269)
    Lorsque vous avez sélectionné un objet 3D avant de cliquer sur l\'icône pour créer un congé ou un chanfrein, tous les bords de l\'objet seront automatiquement sélectionnés. [Pull request \#5328](https   *//github.com/FreeCAD/FreeCAD/pull/5328)
-   Les boîtes de dialogue de [Chanfrein](PartDesign_Chamfer/fr.md) et [Congé](PartDesign_Fillet/fr.md) disposent désormais chacune d\'une nouvelle case à cocher *Utiliser tous les bords*, qui est liée à la propriété Use All Edges de ces objets. Lorsque la case est cochée, la propriété est définie à True. Lorsqu\'elle n\'est pas cochée, la propriété est définie à False. Lorsque Use All Edges est True, il y a une protection contre le [problème de dénomination topologique](Topological_naming_problem/fr.md) car alors tous les bords de l\'objet de base sont utilisés, quel que soit le nombre de bords. [Pull request \#5340](https   *//github.com/FreeCAD/FreeCAD/pull/5340)
-   La sélection du plan lors de l\'[ajout d\'une nouvelle esquisse](PartDesign_NewSketch/fr.md) peut désormais se faire d\'un simple clic dans la vue 3D. [Pull request](https   *//github.com/FreeCAD/FreeCAD/pull/5408) [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=19&t=65020)
-   Lorsqu\'un outil PartDesign est exécuté sans corps actif, FreeCAD propose désormais d\'activer un corps ou d\'en créer un nouveau. [Pull request \#4949](https   *//github.com/FreeCAD/FreeCAD/pull/4949)
-   L\'outil [Définir les couleurs](Part_FaceColors/fr.md) est désormais également disponible depuis l\'atelier de PartDesign.

## Atelier Path 

-   La fonctionnalité Extensions a été ajoutée à l\'opération [Adaptatif](Path_Adaptive/fr.md). [Pull request \#4388](https   *//github.com/FreeCAD/FreeCAD/pull/4388)
-   L\'opération [Hélice](Path_Helix/fr.md) a été remaniée et la propriété Extra offset lui a été ajoutée. [Pull request \#5405](https   *//github.com/FreeCAD/FreeCAD/pull/5405)
-   La vérification si le schéma en cours utilise les minutes pour l\'expression de vitesse et l\'avertissement approprié ont été ajoutés. [Pull request \#6357](https   *//github.com/FreeCAD/FreeCAD/pull/6357)
-   Les filets externes ont été ajoutés à l\'opération de fraisage de filets. [Pull request \#6485](https   *//github.com/FreeCAD/FreeCAD/pull/6485)
-   La stabilité de la gravure sur les esquisses a été améliorée. [Pull request \#6394](https   *//github.com/FreeCAD/FreeCAD/pull/6394)
-   La visibilité des objets Parcours a été rendue plus naturelle. [Pull request \#4911](https   *//github.com/FreeCAD/FreeCAD/pull/4911)

## Module Plot 

-   FreeCAD fournit maintenant le module Plot par défaut, de sorte que tout autre module/atelier peut créer des tracés sans nécessiter d\'outils externes [Pull request \#4971](https   *//github.com/FreeCAD/FreeCAD/pull/4971).

## Atelier Sketcher 

   
  <img alt="" src=images/SketcherSplitExample2_relnotes_0.20.png )                                                  Nouvelle fonction ![](images/Sketcher_Split.svg  style="width   *24px;"> [Diviser une arête](Sketcher_Split/fr.md) pour diviser les lignes ou les arcs existants. [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=9&t=55412) [Pull request \#4420](https   *//github.com/FreeCAD/FreeCAD/pull/4420)
  <img alt="" src=images/SketcherCreateRoundedRectangleExample_relnotes_0.20.png )                  Nouvel outil ![](images/Sketcher_CreateOblong.svg  style="width   *24px;"> [Rectangle arrondi](Sketcher_CreateOblong/fr.md) pour créer des rectangles aux coins arrondis. [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=17&t=59210) [Main Pull request \#4835](https   *//github.com/FreeCAD/FreeCAD/pull/4835)
  <img alt="" src=images/SketcherCreateCenteredRectangleExample_relnotes_0.20.png  style="width   *384px;">   Nouvel outil <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width   *24px;"> [Rectangle centré](Sketcher_CreateRectangle_Center/fr.md) pour définir des rectangles via un point central. [Main commit](https   *//github.com/FreeCAD/FreeCAD/commit/8b4acf11c2caf53cc1cb8dccd8bb6de8516f4492)
  <img alt="" src=images/Radiam_anim_relnotes_0.20.gif )                                                                      Nouvelle fonction ![](images/Sketcher_ConstrainRadiam.svg  style="width   *24px;"> [Contrainte automatique rayon/diamètre](Sketcher_ConstrainRadiam/fr.md) permet d\'assigner automatiquement un poids sur le pôle B-spline, un diamètre sur un cercle complet ou un rayon sur un arc. Support de la multi-sélection comme outils de diamètre/rayon. [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=57584&start=20#p509485) [Main Pull request \#4855](https   *//github.com/FreeCAD/FreeCAD/pull/4855)
  <img alt="" src=images/SketcherRemoveAxesAlignmentResult_relnotes_0.20.png )                          Nouvel outil de contrainte ![](images/Sketcher_RemoveAxesAlignment.svg  style="width   *24px;"> [Supprimer l\'alignement des axes](Sketcher_RemoveAxesAlignment/fr.md) pour supprimer l\'alignement des axes tout en essayant de préserver la relation de contrainte de la sélection. [Main commit](https   *//github.com/FreeCAD/FreeCAD/commit/3c593a33cedc3e6a42928d9087f8a160852cc685)
  \| ![](images/SketcherSnapSlot_relnotes_0.20.gif )                                                     [Sketcher Rainure](Sketcher_CreateSlot/fr.md) peut être contraint horizontalement ou verticalement soit en l\'aimantant manuellement avec la touche **Ctrl**, soit en utilisant l\'option *Auto contraintes* de Sketcher. [Pull request \#5200](https   *//github.com/FreeCAD/FreeCAD/pull/5200)
  <img alt="" src=images/SketcherBSplineInsertKnot_relnotes_0.20.gif )                                          Nouvel outil ![](images/Sketcher_BSplineInsertKnot.svg  style="width   *24px;"> [Insérer un nœud](Sketcher_BSplineInsertKnot/fr.md) pour insérer un nœud dans une B-spline existante. [Pull request \#5311](https   *//github.com/FreeCAD/FreeCAD/pull/5311) et [Pull request \#6356](https   *//github.com/FreeCAD/FreeCAD/pull/6356)
   

### Autres améliorations de Sketcher 

-   Prise en charge de l\'Ajustement remanié. [Pull Request](https   *//github.com/FreeCAD/FreeCAD/pull/4330) [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=54441)
-   Le comportement de l\'outil <img alt="" src=images/Sketcher_CreateSlot.svg  style="width   *24px;"> [Rainure](Sketcher_CreateSlot/fr.md) a changé. Les rainures peuvent maintenant être créées en définissant le centre des deux demi-cercles. [Pull request \#4843](https   *//github.com/FreeCAD/FreeCAD/pull/4843) [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=17&t=59243&p=508658#p508658)
-   L\'automatisation de la visibilité permet d\'ouvrir Sketcher dans une [Vue en section](Sketcher_ViewSection/fr.md) lors de l\'entrée en mode édition. [Pull request \#4742](https   *//github.com/FreeCAD/FreeCAD/pull/4742) [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=57056)
-   L\'automatisation de la visibilité permet de forcer la caméra en [Vue orthographique](Std_OrthographicCamera/fr.md) lorsqu\'on rentre dans le mode édition. [Pull request \#4778](https   *//github.com/FreeCAD/FreeCAD/pull/4778) [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=44747).
-   Option permettant d\'afficher le nom de la contrainte dimensionnelle et d\'utiliser un format personnalisé pour celui-ci. [Pull request](https   *//github.com/FreeCAD/FreeCAD/pull/4966) [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?t=61153)
-   Lors de l\'esquisse d\'un [arc à 3 points](Sketcher_Create3PointArc/fr.md) avec Autoconstraint activé, une [contrainte tangente](Sketcher_ConstrainTangent/fr.md) est proposée pour les 3 points lors du survol d\'une ligne/courbe. [Pull request \#4945](https   *//github.com/FreeCAD/FreeCAD/pull/4945) [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=60596&p=520217#p520209).
-   Les contraintes de rayon/diamètre sont affichées en utilisant une rotation angulaire pour faciliter la visualisation. L\'angle et le caractère aléatoire optionnel sont réglables par l\'utilisateur grâce aux paramètres documentés dans le [Réglage fin](Fine-tuning/fr.md). [Pull request \#4934](https   *//github.com/FreeCAD/FreeCAD/pull/4934) [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=60370)
-   Il est maintenant possible de fixer l\'angle de la direction lors de l\'utilisation de l\'outil [Réseau rectangulaire](Sketcher_RectangularArray/fr.md). [commitc9eaa239](https   *//github.com/FreeCAD/FreeCAD/commit/c9eaa239) [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?p=535691#p535691)
-   Il est maintenant possible de fixer l\'angle de la direction lors de l\'utilisation des outils [Clone](Sketcher_Clone/fr.md), [Copier](Sketcher_Copy/fr.md) et [Déplacer](Sketcher_Move/fr.md). [commit](https   *//github.com/FreeCAD/FreeCAD/commit/6e4a09f569cf) [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=62799)
-   En cliquant avec le bouton droit de la souris sur une esquisse dans l\'arborescence, vous obtiendrez désormais une entrée de menu contextuel \"Éditeur de pièce jointe\" qui ouvre la [boîte de dialogue d\'Ancrage](Part_EditAttachment/fr.md) pour modifier la pièce jointe. [commit c3511ba2f0](https   *//github.com/FreeCAD/FreeCAD/commit/c3511ba2f0)
-   La sélection des contraintes est désactivée lors de l\'utilisation d\'un outil de géométrie ou de contrainte. Elle peut également être désactivée manuellement à tout moment en appuyant sur la touche **Maj**. [Pull request \#5398](https   *//github.com/FreeCAD/FreeCAD/pull/5398) [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=65465)
-   Un filtre d\'affichage polyvalent a été ajouté dans le panneau de tâches de Sketcher pour faciliter la gestion de la visibilité des contraintes [Discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=17&t=60569).
-   Il est désormais possible de définir le degré d\'une B-Spline ([Pull request \#6463](https   *//github.com/FreeCAD/FreeCAD/pull/6463)) et d\'annuler le dernier point de contrôle défini ([Pull request \#6476](https   *//github.com/FreeCAD/FreeCAD/pull/6476)) au moment de la création.
-   Révision des raccourcis par défaut afin de supprimer les raccourcis conflictuels et de rendre les raccourcis plus faciles à mémoriser. [Discussion sur le forum](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=41272) ; Captures d\'écran des raccourcis pour les [contraintes](https   *//wiki.freecadweb.org/images/0/0c/Sketcher_Shortcuts_v0.20_Screenshot_Constraints.png), la [géometrie](https   *//wiki.freecadweb.org/images/4/48/Sketcher_Shortcuts_v0.20_Screenshot_Geometry.png) et [divers outils](https   *//wiki.freecadweb.org/images/9/90/Sketcher_Shortcuts_v0.20_Screenshot_variousTools.png).

## Atelier Spreadsheet 

   
  <img alt="" src=images/Spreadsheet-Preferences-Spreadsheet_relnotes_0.20.png )        L\'atelier a maintenant des ![](images/Std_DlgPreferences.svg  style="width   *24px;"> [Préférences](Spreadsheet_Preferences/fr.md). Elles sont utilisées par les commandes <img alt="" src=images/Spreadsheet_Import.svg  style="width   *16px;"> [Spreadsheet Importer](Spreadsheet_Import/fr.md) et <img alt="" src=images/Spreadsheet_Export.svg  style="width   *16px;"> [Spreadsheet Exporter](Spreadsheet_Export/fr.md). [Pull request \#5073](https   *//github.com/FreeCAD/FreeCAD/pull/5073)
  <img alt="" src=images/Spreadsheet_configuration_table_relnotes_0.20.png  style="width   *384px;">   Il est désormais possible de configurer les [tables de configuration](Spreadsheet_Workbench/fr#Tables_de_configuration.md). De cette façon, on peut définir différents jeux de paramètres pour la même pièce. Fait partie du [Pull request \#2862](https   *//github.com/FreeCAD/FreeCAD/pull/2862).
  ![](images/Spreadsheet_binding-dialog.png )                                                      Les cellules peuvent désormais être [liées à d\'autres cellules](Spreadsheet_Workbench/fr#Liaison_cellulaire.md) de la même feuille de calcul ou d\'une feuille différente. Fait partie du [Pull request \#2862](https   *//github.com/FreeCAD/FreeCAD/pull/2862).
   

### Autres améliorations de Spreadsheet 

-   Dans le menu contextuel des lignes/colonnes, il est désormais possible de spécifier la position lors de l\'insertion de lignes/colonnes. [Pull request \#4704](https   *//github.com/FreeCAD/FreeCAD/pull/4704).
-   Importation XLSX (utilisée par [Std Importer](Std_Import/fr.md))    * Ajout du support des fonctions Partie entière par défaut (floor) et Partie entière supérieure (ceil). [Pull request \#5015](https   *//github.com/FreeCAD/FreeCAD/pull/5015).
-   Amélioration de la navigation en utilisant les touches **Tab** et **Entrée**.
-   Amélioration de l\'interface pour couper et coller des blocs de cellules.

## Atelier TechDraw 

   
  <img alt="" src=images/TechDraw_ExtensionExample_relnotes_0.20.png  style="width   *384px;">   Plus de 30 nouveaux outils, appelés [Extensions](TechDraw_Workbench/fr#Extensions.md), sont désormais disponibles. Ils offrent de nouvelles fonctionnalités cosmétiques pour améliorer les dessins.
   

### Autres améliorations de TechDraw 

-   Il est désormais possible de [Copier](TechDraw_ShareView/fr.md) et [Déplacer](TechDraw_MoveView/fr.md) des [Vues](TechDraw_Workbench/fr#Vues.md) entre de pages.
-   Lorsqu\'il y a plusieurs [Pages](TechDraw_PageDefault/fr.md) et que l\'on veut ajouter une [Vue](TechDraw_View/fr.md), un [Groupe de projections](TechDraw_ProjectionGroup/fr.md) etc., il y a maintenant un dialogue pour demander à quelle page la vue doit être ajoutée. [Pull request \#5309](https   *//github.com/FreeCAD/FreeCAD/pull/5309).
-   Un nouveau spécificateur de format *%w* a été ajouté pour afficher le nombre donné de chiffres après le point et supprimer les zéros de à la fin. [Pull request \#5401](https   *//github.com/FreeCAD/FreeCAD/pull/5401).
-   Le nouveau spécificateur de format *%w* est maintenant la valeur par défaut. La préférence de spécification de format a été déplacée de l\'onglet Avancé à l\'onglet Dimension. [Pull request \#6504](https   *//github.com/FreeCAD/FreeCAD/pull/6504).
-   Des hachures diagonales inversées ont été ajoutées pour l\'outil [Hachures géométriques](TechDraw_GeometricHatch/fr.md). [Pull request \#6429](https   *//github.com/FreeCAD/FreeCAD/pull/6429).
-   Il existe une nouvelle option pour afficher une grille dans une [page](TechDraw_PageDefault/fr.md). Plusieurs [préférences](TechDraw_Preferences/fr#Grille.md) connexes ont été introduites. [Pull request \#6465](https   *//github.com/FreeCAD/FreeCAD/pull/6465).
-   L\'affichage des unités dans les dimensions a été corrigé conformément aux normes. Le symbole du degré est toujours présent pour la valeur de la dimension et les tolérances, les autres unités n\'apparaissent que si ShowUnits est défini. L\'unité apparaît immédiatement après la valeur de la dimension sauf s\'il y a une tolérance, alors elle apparaît après la tolérance. [Pull request \#6581](https   *//github.com/FreeCAD/FreeCAD/pull/6581)

## Web

Qt WebEngine est maintenant considéré comme l\'option par défaut au lieu de Qt WebKit.

## Ateliers externes 


**Remarque    ***

ce sont les nouveaux ateliers créés dans ce cycle de développement ou les anciens ateliers qui ont reçu des mises à jour. Voir les [Ateliers externes](External_workbenches/fr.md) pour plus d\'ateliers pouvant être installés et couvrant une grande variété de sujets. Si vous souhaitez voir votre atelier ajouté, rejoignez le [forum](https   *//forum.freecadweb.org/index.php) et présentez votre code.

### A2plus

Plusieurs fonctions permettant de visualiser, d\'inspecter et de modifier les contraintes existantes ont été ajoutées. Il est désormais possible de mettre en évidence les contraintes à l\'aide d\'une étiquette, de supprimer temporairement une contrainte ou d\'exécuter le solveur uniquement pour une contrainte particulière.

Pour plus d\'informations, voir [la description du traitement des contraintes](A2plus_Workbench/fr#Traitement_des_contraintes.md).

### Assembly3

+++
| <img alt="" src=images/Asm3_relnotes_0.20.jpg  style="width   *384px;">     | L\'atelier Assembly3 est disponible (depuis mars 2022) par le biais du [Gestionnaire d\'Addon](Std_AddonMgr/fr.md). Cela permet d\'installer et de gérer facilement les dépendances externes de l\'atelier.                                                                                                                            |
|                                                                       |                                                                                                                                                                                                                                                                                                                                                |
|                                                                       | Assembly3 permet de créer des assemblages de corps différents contenus dans un seul fichier ou dans plusieurs documents en exploitant toute la puissance du système de liens de FreeCAD. Apprenez-en plus sur [App Links](App_Link/fr.md) dans cette [présentation vidéo](https   *//www.youtube.com/watch?v=yTDkJ7JZAWs) de Realthunder. |
|                                                                       |                                                                                                                                                                                                                                                                                                                                                |
|                                                                       | L\'atelier Assembly3 utilise [SolveSpace](https   *//solvespace.com) comme solveur.                                                                                                                                                                                                                                                               |
|                                                                       |                                                                                                                                                                                                                                                                                                                                                |
|                                                                       | Une documentation complète est disponible sur la page principale [Assembly3](Assembly3/fr.md) du wiki de FreeCAD ou sur le site GitHub de Realthunder [wiki Assembly3](https   *//github.com/realthunder/FreeCAD_assembly3/wiki).                                                                                                         |
+++
| <img alt="" src=images/Asm3_1_relnotes_0.20.jpg  style="width   *384px;"> | **Principales fonctionnalités    ***                                                                                                                                                                                                                                                                                                              |
|                                                                       |                                                                                                                                                                                                                                                                                                                                                |
|                                                                       | -   Solveur dynamique/interactif    * déplacez les pièces avec la souris pendant que le solveur contraint le mouvement.                                                                                                                                                                                                                           |
|                                                                       | -   Liens    * utilisez une seule pièce plusieurs fois dans un assemblage.                                                                                                                                                                                                                                                                        |
|                                                                       | -   Liens externes    * permet d\'utiliser des pièces provenant de documents externes.                                                                                                                                                                                                                                                            |
|                                                                       | -   Assemblages hiérarchiques    * permet la création de sous-assemblages.                                                                                                                                                                                                                                                                        |
|                                                                       | -   Gel des assemblages    * les assemblages qui ne doivent pas rester dynamiques peuvent être exclus des calculs et sont considérés comme des géométries fixes par le solveur asm3.                                                                                                                                                              |
|                                                                       | -   Et bien plus encore.                                                                                                                                                                                                                                                                                                                       |
+++

### Assembly4

   
  <img alt="" src=images/A4_veriant-beam_relnotes_0.20.png  style="width   *384px;">Longueur différente d\'une poutre comme variante.                                          Nouvelle fonctionnalité permettant d\'ajouter des variantes. Il s\'agit de [liens](App_Link/fr.md) vers une pièce avec des paramètres variables, ce qui signifie que vous pouvez insérer la même pièce plusieurs fois, et ajuster les paramètres de chaque instance. Pour plus d\'informations, consultez [ce fil du forum](https   *//forum.freecadweb.org/viewtopic.php?p=538666#p538666).
  <img alt="" src=images/A4_veriant-animation_relnotes_0.20.gif  style="width   *384px;">Un assemblage animé.Cliquez sur l\'image pour voir l\'animation.   Les animations peuvent être exportées au format MP4 et GIF.
   

### FCGear

L\'[atelier FCGear](FCGear_Workbench/fr.md) a reçu quelques améliorations    *

-   Pour les engrenages à développante, le diamètre extérieur (ou pointe) et le diamètre de la racine sont exposés en tant que propriétés ([détails](https   *//github.com/looooo/freecad.gears/pull/69)).
-   Les objets engrenages sont maintenant [attachables](Part_EditAttachment/fr.md). ([détails](https   *//github.com/looooo/freecad.gears/pull/72)).
-   Les objets engrenages peuvent désormais être utilisés comme des fonctions additives dans les corps de PartDesign ([détails](https   *//github.com/looooo/freecad.gears/pull/74)).
-   La création d\'objets engrenages apparaît désormais dans la pile d\'annulation ([détails](https   *//github.com/looooo/freecad.gears/pull/83)).

### Plot

-   Le [module Plot](Plot_Workbench/fr.md) a été supprimé de l\'atelier car il est désormais fourni par FreeCAD.

### Ship

L\'[Atelier Ship](Ship_Workbench/fr.md) est de nouveau opérationnel !

-   Un nouvel outil pour calculer le [tirant d\'eau et l\'angle d\'assiette](https   *//github.com/FreeCAD/freecad.ship#static-sink-and-trim) a été ajouté.
-   Un nouvel outil pour calculer les [opérateurs d\'amplitude de réponse](https   *//github.com/FreeCAD/freecad.ship#raos) a été ajouté en plus de [capytaine](https   *//github.com/mancellin/capytaine).

## Compilation

Depuis cette version, FreeCAD ne peut être compilé qu\'avec Qt 5.x et Python 3.x. La version de Python la moins bien supportée est 3.6.9 selon [ce fil de discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=62701).

Pour compiler FreeCAD voir les instructions pour [Windows](Compile_on_Windows/fr.md), [Linux](Compile_on_Linux/fr.md) et [MacOS](Compile_on_MacOS/fr.md).

Les systèmes d\'exploitation pris en charge sont    *

-   Windows 7, 8, 10 et 11
-   Linux Ubuntu Bionic Beaver (18.04) et Focal Fossa (20.04)
-   MacOS    * 10.12 Sierra ou plus récent

## Limitations connues 

### Windows 32 bits 

Depuis FreeCAD 0.19, nous ne supportons plus officiellement Windows 32 bits. FreeCAD pourrait fonctionner sur ces systèmes, mais aucun support n\'est donné.

### Bureau distant sous Windows 

Selon les capacités graphiques OpenGL d\'un ordinateur, il se peut que l\'on rencontre un plantage lors de l\'exécution de FreeCAD via le bureau à distance. Pour résoudre ce problème, mettez à jour votre pilote OpenGL. Si cela ne vous aide pas    *

-   Téléchargez [cette bibliothèque OpenGL](https   *//downloads.fdossena.com/geth.php?r=mesa64-latest) pour Windows 64 bits et extrayez-la.
-   Renommez le fichier DLL en *opengl32sw.dll* et copiez-le dans le sous-dossier *bin* du dossier d\'installation de FreeCAD (écrasez la DLL existante).

[Category   *News](Category_News.md) [Category   *Documentation](Category_Documentation.md) [Category   *Releases](Category_Releases.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.20/fr
