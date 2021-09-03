


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}


<div class="mw-translate-fuzzy">


{{VeryImportantMessage|[Voir la page originale en anglais](Arch_Concept.md).}}

Cette page est une tentative de recueil d\'idées sur la conception paramétrique dans le domaine de l\'architecture, pour la construction du module **Arch**. Comme il est un peu différent de celui du domaine de l\'ingénierie mécanique, je tiens à définir un peu mieux les concepts, avant de penser à la façon de l\'appliquer \... N\'hésitez pas à ajouter vos idées !


</div>

## Programmes similaire {#programmes_similaire}

-   [Revit](http://fr.wikipedia.org/wiki/Revit)

-   [Archicad](http://fr.wikipedia.org/wiki/ArchiCAD)

-   [Generative Components](http://en.wikipedia.org/wiki/Generative_Components)

## Formats de fichiers {#formats_de_fichiers}

-   [STEP](http://fr.wikipedia.org/wiki/Standard_pour_l'échange_de_données_de_produit) - pleinement fonctionnel dans FreeCAD

-   [IFC](http://fr.wikipedia.org/wiki/Industry_Foundation_Classes)
    -   <http://forge.osor.eu/plugins/wiki/index.php?id=175&type=g> et IFC sdk
    -   <http://www.bimserver.org/>
    -   <http://konstruct.nl/parsing-ifc-stepexpress-files-in-python-and-s>

## Concepts généraux {#concepts_généraux}

-   FreeCAD est parfait pour cette tâche. La conception avec des objets paramétriques, permet de réduire considérablement le seul vrai problème que je vois dans FreeCAD qui est, le traitement de milliers d\'objets. Tout le reste est déjà présent, comme les types d\'objets personnalisés, les propriétés personnalisées, etc . . . La principale difficulté est, la conception d\'un modèle général pour faire face à l\'interaction entre les objets, depuis que FreeCAD a introduit un graphe de dépendance spécialement conçu à cette fin est potentiellement un plus.

-   [BIM](http://fr.wikipedia.org/wiki/Building_Information_Modeling) (Building Information Modeling) est un concept inventé par un groupe de constructeurs et éditeurs de logiciels de conception paramétrique, principalement [Autodesk](http://fr.wikipedia.org/wiki/Autodesk). Cela signifie que vous ne projetez pas un bâtiment en dessinant, mais en insérant des informations (paramètriques). Le rôle du logiciel serait alors, de produire le dessin automatiquement. Ce sont à mon avis ~~des histoires~~ très discutable et seulement un concept \"publicitaire\". Même dans les logiciels de BIM les plus avancés comme (Revit, Archicad et Microstation GC), vous ne pouvez pas vous soustraire à l\'acte de dessiner, sauf, si vous voulez tuer toute créativité. Le but ici, n\'est pas de tout automatiser, mais de garder une souplesse créative.

-   La conception paramétrique **Génie mécanique** est généralement basée sur l\'historique des modifications et la résolution des contraintes. Ces deux notions ont beaucoup moins d\'importance dans la conception de bâtiments, puisque vous revenez rarement dans les étapes de la construction que vous avez faite (elles sont généralement très simple), et le maintien des contraintes comme l\'horizontalité, l\'angle ou la distance, même si elles sont utiles, ne sont pas aussi importantes que dans la conception mécanique.

-   **Arch conception paramétrique** est basée sur des archétypes : mur, porte/fenêtre, toiture, dalle, poutre, qui sont les archétypes de base. En dehors d\'eux, ce que vous aurez surtout, ce sont des dérivés personnels.

-   Il est fait ici, un usage intensif de l\'assemblage : par exemple plusieurs fenêtres sont regroupées pour former un mur-rideau.

-   La clé, est la relation : Les éléments sont rarement très complexes et relèvent beaucoup plus de travaux de modélisation, mais, ils doivent souvent être transformés par juxtaposition ou inclusion d\'autres éléments. Par exemple, un mur n\'est rien d\'autre qu\'une simple extrusion, mais il doit se connecter à d\'autres murs, ou faire un trou quand une fenêtre est insérée. Comment construire ce modèle relation, et, comment et ou le stocker, c\'est là le grand problème.

-   Un problème de pratiquement tous les logiciels de modélisation paramétriques est, que les bâtiments dépendent beaucoup de ces objets archétypes. La création de nouvelles bibliothèques d\'éléments, est extrêmement difficile dans [Archicad](http://fr.wikipedia.org/wiki/ArchiCAD) ou beaucoup plus facile dans [Revit](http://fr.wikipedia.org/wiki/Revit), mais il y a toujours quelques problèmes, problèmes de communications importants entre **pièces paramétriques** et **pièces non-paramétriques**. Fondamentalement, vous profiterez de tout le potentiel du logiciel si vous utilisez des pièces qui sont faites spécialement pour ce travail. Par exemple la transformation d\'un simple solide dans un mur est extrêmement difficile.

-   Un document sur ​​Autodesk Revit : cet article **[parametric\_building\_modeling](http://images.autodesk.com/adsk/files/bim_parametric_building_modeling_jan07_1_.pdf)** est surtout une publicité en faveur de Revit, et plusieurs concepts sont à mon humble avis sans importance, comme, \"générer\" un dessins 2D et avoir la possibilité de modifier le modèle en 2D, mais c\'est de toute façon une option intéressante.

-   La vitesse de calcul des objets n\'est pas à mon humble avis, un très gros problème. La modification d\'un objet ne devrait pas affecter de nombreux autres objets, et il est généralement fait dans une phase d\'ajustements, de sorte qu\'il n\'est pas si important d\'avoir des mises à jour aussi rapides que l\'éclair. Une chose très importante, est de toujours sauvegarder la forme finale de l\'objet, de sorte que l\'ouverture des modèles enregistrés ne devraient pas exiger trop de calculs. Avant l\'enregistrement, tout doit toujours être recalculé.

-   L\'outil de la section **state-of-the-art** est très important. Les plans d\'étages, des élévations, des coupes, des plafonds, tous, sont des outils **BIM** similaires, car ils sont [axonométriques](http://fr.wikipedia.org/wiki/Perspective_axonométrique)/[orthographique](http://fr.wikipedia.org/wiki/Projection_orthographique) **aux plans de coupes**, à travers le modèle BIM.

-   Il y a un problème d\'annotation : Où placer les dimensions ? sur le modèle ? directement sur la feuille .svg ? pas très pratique \... Ce point doit davantage être étudié. Les dimensions feront partie d\'une couche qui peut être activée/désactivée sur les parcelles. En outre, puisque les parcelles sont faites à une échelle spécifique, les dimensions seront réduites pour correspondre à l\'échelle choisie ou, par une autre, choisie par l\'utilisateur.

-   Un \"bâtiment paramétrique\" doit être interprété comme un ensemble d\'objets relationnels compatibles avec l**\'Archétype-based** ainsi que d\'autres, non-basés sur l**\'Archétype**. La transformation d\'un objet à partir d\'une catégorie à une autre devrait être possible, et tous, doivent se comporter de la même manière dans une coupe et les changements d\'échelle.

-   Un système pour créer, si possible graphiquement de nouveaux composants et assemblages : L\'assemblage pourrait fonctionner comme un \"**sous-modèle**\" qui peut être inséré/importé/lié à un modèle **[BIM](http://fr.wikipedia.org/wiki/Building_Information_Modeling)**. De cette façon, un sous-modèle peut être, mis à jour/changé et reflèté automatiquement dans le modèle **BIM** (si le sous-modèle est \"lié\", s\'il est \"importé\", alors, l\'utilisateur peut choisir de \"mettre à jour\" le modèle et de tenir compte de la dernière version du sous-modèle, sinon, il restera avec la dernière importation/insersion).

-   Un mode d\'édition : on peut donc modifier la forme originale qui a généré l\'objet.


<div class="mw-translate-fuzzy">

## Les archétypes {#les_archétypes}

-   Tous les **Archétypes** doivent toujours se comporter comme des objets de programmation orientée objet. Vous pouvez faire une nouvelle classe basée sur une autre classe.
-   Tous les **Archétypes** devraient être en mesure d\'interagir avec un objet commun. Pour cela, probablement les objets communs devraient posséder des propriétés personnalisées.
-   Les murs doivent être définis par un simple fil (wire) (qui pourrait être extrudé horizontalement, puis verticalement), une forme plane (auquel serait tout simplement ajoutée une épaisseur) ou un solide (qui ne ferait rien). Le résultat serait toujours un solide. Ses paramètres ne varieraient donc, qu\'au moment de la création et en fonction de vos données.
-   Les murs doivent se connecter en traversant/touchant les murs.
-   Les murs pourraient être fait de différentes couches (de matériaux): Matériaux mêmes en relation entre eux.
-   Les murs n\'ont pas vraiment besoin d\'un outil de dessin : Vous les faites facilement par la conversion de quelque chose d\'autre. Mais dans ce cas, le module projet pourrait avoir une \"double ligne\" d\'outils.
-   Les portes et fenêtres sont des objets très simples, leurs paramètres ne concernent que leurs aspect interne. Mais ils doivent avoir une «boîte» qui crée des trous dans d\'autres objets.
-   Les poutres et les dalles sont toutes aussi simples, mais en fonction de leurs matériaux, elles doivent être en mesure de se connecter à d\'autres dalles, poutres et murs.
-   Les poutres et dalles peuvent également être assemblées en un seul élément \"structurel\". Il y a beaucoup de piliers, tous ont pu être définis de la même manière que les murs, par un fil (wire), une forme ou un solide. Ils pourraient même être basés sur la même base que les murs \...
-   Les toits, sont un type spécial d\'objet, pas très intéressants de fait, mais utile, car il est délicat de calculer un toit manuellement. Fondamentalement, vous avez besoin de créer une forme basée sur un contour et une inclinaison. Cela devrait être facile à faire, et, étendu plus tard à d\'autres types de toits.
-   Les Assemblages doivent être définis plus loin : Ils sont essentiellement constitués d\'autres pièces, qui pourraient être n\'importe quoi, des formes, des fenêtres, etc .. et, des propriétés personnalisées, telles que la répétition de tableau, la déformation (suivre une forme ?), etc\...
-   Site Builder : est un ensemble d\'outils spéciaux qui doivent gérer la création du site et des mises à jour. Cette boîte à outils doit être compatible avec d\'autres grands terrains/sites modelers Open Source et les applications **GIS** (comme GRASS). SiteBuilder permettra la création d\'un site basé sur les courbes topographiques et la manipulation facile de mises à jour du site. Cela permettra de créer facilement : des trottoirs, des coupes de trottoirs, des bordures et des routes, l\'aménagement paysager, des parkings avec tout le nécessaire d'égouttage, systèmes d\'écoulement des eaux, etc . . . La base de données générée permettra d\'estimer les déblais et remblais ainsi que les autres informations nécessaires pour faire le site résidentiel. SiteBuilder sera également utile pour générer l\'excavation nécessaire à un projet.


</div>

## Archetypes (types d\'objets) {#archetypes_types_dobjets}

### Wall ([Murs](Arch_Wall/fr.md) <img alt="" src=images/Arch_Wall.png  style="width:16px;">) {#wall_murs_arch_wall.png}

Wall (mur) est un élément de construction vertical qui suit un chemin sur un niveau défini (premier étage, troisième étage, etc) ou est extrudé horizontalement sur une surface verticale. Les murs sont faits de plusieurs couches (chaque matériaux avec une épaisseur spécifique et propriétés thermiques), et permettre des ouvertures (résultat de soustractions) ou annexes (union). Lorsque deux murs différents se croisent, l\'utilisateur peut sélectionner l\'option pour relier les deux murs (avec une structure similaire). Tous les paramètres d\'un mur sont disponibles pour les futurs calculs thermique et de structure, ils peuvent ainsi générer des rapports (projet de loi de matériaux). Donc, pour un mur, les zones, les faces, les volumes, les quantités de matériaux, etc sont directement insérés dans le cahier des charges et d\'estimation des coûts.

Comme mentionné précédemment, les murs de **BIM** sont définis par une ligne/polyligne/etc. qui représente l\'\"axe\" de la paroi. Cette ligne peut être alignée avec la face extérieure de la paroi, la face intérieure du mur, ou le centre du mur, ou si l\'utilisateur veut choisir de le personnalisé et le définir. Les murs ont plusieurs paramètres qui les définissent : niveau de paroi dans lequel il est placé (c\'est à dire, premier étage, sous-sol, cinquième étage, etc..) - Largeur - Hauteur - Composition.

Le niveau dans lequel les murs sont placés, nécessite une insertion préalable de ce \"niveau\" par l\'utilisateur. Une fois qu\'un niveau est inséré dans le modèle BIM, cela crée automatiquement une section horizontale, qui générera à son tour une \"feuille\", c\'est-à-dire une fois que j\'insère un niveau appelé \"Premier étage\" à la hauteur 0.00 qui sectionne automatiquement tous les éléments visibles à ce niveau à cette hauteur (plus et moins haut et bas afin que les portes / fenêtres / ouvertures soient visibles dans ce plan). Les niveaux et les élévations ont un concept similaire, dans la mesure où ils sont tous deux des \"plans de coupe\" situés dans une certaine position / rotation dans l\'espace 3D.

Les murs permettent des insertions de bibliothèques telles que : portes, fenêtres, murs-rideaux, et d\'autres objets personnalisés qui nécessitent une ouverture dans le mur, uniquement si une ouverture est nécessaire, et peut être insérée.

### Door/Window ([Portes/Fenêtres](Arch_Window/fr.md) <img alt="" src=images/Arch_Window.png  style="width:16px;">) (Insertion d\'élements) {#doorwindow_portesfenêtres_arch_window.png_insertion_délements}

Les portes et fenêtres sont vraiment identiques, ce sont des objets qui peuvent avoir un grand nombre de paramètres pour définir leurs forme.
Un volume invisible est utilisé pour découper des ouvertures à travers la parois réceptrice.
Il sont généralement insérés dans un mur, mais pas toujours. Car il peuvent varier énormément, ils devraient être faciles à concevoir.

### Roof (Toits) {#roof_toits}

Le toit est tout simplement un moyen pratique de calculer les intersections des pentes du toit.

### Slab (Dalles) {#slab_dalles}

La dalle est horizontale, fabriquée à partir de l\'extrusion verticale d\'un fil fermé ou d\'une face, le matériel doit se connecter à d\'autres éléments de la structure, et peut avoir un certain nombre d\'annexes (union) ou des trous (soustraction), et les couches (matériaux). Les surfaces horizontales et le volume doivent être calculés

### Beam/Pillar ([Poutres/Pilier](Arch_Structure/fr.md) <img alt="" src=images/Arch_Structure.png  style="width:16px;">) (éléments structurels) {#beampillar_poutrespilier_arch_structure.png_éléments_structurels}

Un fil fermé (wire) ou une face extrudée dans n\'importe quelle direction, peut avoir un certain nombre d\'annexes (union) ou de trous (soustraction).

### Assemblages

Un groupe de fenêtres qui peuvent être mis en forme dans son ensemble

## Mécanismes génériques {#mécanismes_génériques}

-   **Dépendances** : les fenêtres doivent savoir sur quels murs ils sont insérés, les murs doivent savoir quelle fenêtre ils contiennent, etc .. (Voir la partie booléenne)
-   **Joints** : les murs doivent savoir quels autres murs se connectent à eux et se connecter correctement à l\'ensemble des matériaux. Le déplacement d\'un mur doit donc recalculer les murs voisins, et établir un tableau des types communs possibles.
-   **Catégorie Edge** : certains bords ne doivent pas être établis quand ils sont entre 2 objets de même matière. Marquez les bords et choisir plus tard comment les réutiliser.
-   **Groupement automatique** : Les objets d\'un certain type vont automatiquement dans des groupes spécifiques.
-   **Créateur de Fenêtres** : Une façon simple de concevoir des fenêtres paramétriques, basée sur les profils.

### Analyse énergétique {#analyse_énergétique}

-   Le programme bâtiment doit avoir les performances appropriées, qui doivent servir aussi bien à des situations géographiques particulière. Par exemple, un projet unique peut être construit à Miami, Floride (US) ou Francfort (Allemagne) ou Sydney (Australie). Cependant, il se produira avec de grandes différences. Ce qui est approprié pour un emplacement dans une certaine zone, peut-être inapproprié pour un autre emplacement. Les dessins et modèles que nous générons avec **FCBIM** devraient être « **testés** » et, surveiller leurs comportement en terme de consommation d\'énergie. Pour le moment, il y a peu d\'outils qui permettent de voir les performances énergétiques des bâtiments [(Energy Performance of Buildings)](http://fr.wikipedia.org/wiki/Directive_pour_la_performance_énergétique_des_bâtiments). Les programmes principaux Freeware/Open Source : EnergyPlus, OpenStudio (ont une interface graphique pour EnergyPlus) et ESP-r.

### Simulation avancée {#simulation_avancée}

La récolte de la lumière du jour est l\'une des approches de base en matière de conception durable. Beaucoup de conceptions modernes tournent le dos à la lumière naturelle et aboutissent à des solutions indésirables pour les êtres humains. Aux États-Unis un grand nombre de bâtiments créent le soi-disant syndrome des bâtiments malsains, qui conduisent à des problèmes de santé pour les personnes qui vivent et travaillent dans ces bâtiments. L\'utilisation de la lumière du jour atténue en partie ce problème. **FCBIM** devrait intégrer des outils qui permettent des simulations de jour, peut-être [Radiance](http://fr.wikipedia.org/wiki/Radiosité) ou [LuxRender](http://fr.wikipedia.org/wiki/LuxRender) ou YAF (a) ray.

### HVAC et la ventilation naturelle {#hvac_et_la_ventilation_naturelle}

-   Outils pour insérer dessiner et calculer [HVAC](http://fr.wikipedia.org/wiki/Chauffage,_ventilation_et_climatisation) et permettent de calculer l\'utilisation de la ventilation naturelle. Peut-être que [OpenFOAM](http://fr.wikipedia.org/wiki/OpenFOAM) sera un candidat dans ce domaine, et viendra compléter FCBIM.

## Capture et acquisition de connaissances {#capture_et_acquisition_de_connaissances}

L\'effort pour créer un module qui permettra à FreeCAD de fournir une modélisation de bâtiment contemporain avec les informations d\'environnement (BIM) est en cours. L\'effort est orienté pour porter ses capacités et les comparer à des systèmes de modélisation d\'architecture plus matures tels que [Revit](http://fr.wikipedia.org/wiki/Revit). Nous reconnaissons les limites dans les implémentations disponibles de BIM dont l\'un, est l\'ignorance de la connaissance du bâtiment. Pour cette raison, nous poursuivons également un objectif parallèle, pour développer les capacités qui permettront d\'acquérir des connaissances telles que FreeCAD créé principalement dans le stade de la conception, mais aussi plus loin dans la phase de conception détaillée. Dans les sections suivantes, nous documentons les capacités qui ne sont pas si fréquentes dans les outils disponibles, mais que nous croyons plus appropriés et efficaces de capturer l\'acquisition de connaissances et d\'informations, de la conception à la démolition. Les sections suivantes fournissent des spécifications et des directives concernant **le pourquoi** d\'une partie de ces efforts. Nous allons fournir **le comment** progresser dans nos efforts. Inutile de dire, que les choses vont changer ou être modifiées pour que notre compréhension et la mise en oeuvre se rassemblent.

### Descriptions des procédures pour identifier les objets {#descriptions_des_procédures_pour_identifier_les_objets}

La session commence dès la conception du bâtiment sur le site où le concepteur établit la direction du nord, et, introduit les obligations appropriées, selon le cahier des charges applicable au bâtiment dans la région désignée ou la localité. Après cela, l\'empreinte (tracé) du nouveau bâtiment est établi.

#### Objet 1: Terrain à bâtir {#objet_1_terrain_à_bâtir}

Il n\'y a qu\'un seul chantier dans un projet. Cet objet (projet) doit être créé dès que la décision de conception de la maison est faite par le concepteur. Il devrait exister une forme de conteneur (car il isole les espaces. Nous en verrons plus sur cela plus tard) avec des côtés, une hauteur et une base. Les pièces peuvent alors être définies de manière interactive en termes de longueur et d\'angle (direction). Au besoin, il devrait également être possible d\'ajouter ou de retirer les côtés. Bien que le fond soit créé à plat, il peut également être redéfini avec des contours afin d\'obtenir une pente appropriée. Le fond (base) est la seule partie du site qui doit être visible.

#### Objet 2: Direction du Nord {#objet_2_direction_du_nord}

La direction du nord est un objet qui établit l\'angle dans la direction du **nord vrai**. Il s\'agit d\'une partie du site qui le rend déterminant pour situer les vents dominants, le mouvement du soleil, etc \...

#### Objet 3: Le recul {#objet_3_le_recul}

Il s\'agit de distances entre les limites du site qui sont requis par le code. Ils font partie du site, mais nécessitent certains paramètres afin de déterminer où sont les limites et quelles sont les distances. Par exemple le retrait de la limite côté rue, peut être différente de la marge de recul à partir d\'un côté de la limite d\'un site voisin. Cette information peut être fournie de manière interactive, mais avec la direction **nord-établie**, il est possible pour le concepteur de saisir ces informations lors de la collecte des exigences relatives à la conception. La marge de recul, comme le site, est un type d**\'objet conteneur**.

#### Object 4: Niveaux du Bâtiment {#object_4_niveaux_du_bâtiment}

À ce stade, la surface du bâtiment a été mise en place. Cette surface représente le premier niveau du bâtiment. Le niveau du bâtiment est un objet qui permet d\'intégrer les différents systèmes de construction. Des exemples de systèmes de construction sont, l\'architecture, structure, électricité, etc \...
Le niveau du bâtiment, comme le chantier de construction, est une forme de conteneur. Il peut y avoir un ou plusieurs niveaux qui sont généralement empilés les uns sur les autres en partant du bas. Le premier niveau est établi après la désignation du revers pour toutes les limites du site. Des niveaux supplémentaires peuvent être créés, mais seul l\'élévation du fond est modifiée puisque les limites de ces niveaux sont invisibles.

#### Object 5: Espace du Bâtiment {#object_5_espace_du_bâtiment}

L\'espace du bâtiment est défini par les fonctions principales de l\'édifice comme un espace pour dormir, manger, se détendre, travailler, etc , les espaces sont créés et regroupés à l\'intérieur des niveaux. Il existe différents types d\'espaces qui fournissent les fonctions appropriées dans différents types de bâtiments. Par exemple, dans un type de bâtiment résidentiel, il existe 4 grands types, Chambres à coucher, salle de séjour, cuisine (salle à manger) et le garage.

#### Object 6: Objets dans l\'espace du Bâtiment {#object_6_objets_dans_lespace_du_bâtiment}

Cela représente tout ce qui peut être situé dans un espace. Chaque objet connaît fondamentalement ses exigences. Par exemple pour décrire une zone d\'assise, un objet avec au moins une surface au sol, un empattement et une hauteur maximale sera nécessaire.

#### Object 7: Conteneur dans le bâtiment {#object_7_conteneur_dans_le_bâtiment}

La plupart des objets décrits à ce jour sont des types conteneurs. Les conteneurs utilisent une surface et sont limités par les extrémités. Il y a le fond , la hauteut et les bords. Deux conteneurs peuvent partager une limite latérale. Lorsque ce partage se produit, le partage du côté d\'un objet remplace les différents côtés de chacun des conteneurs participants. Il établit un lien entre les deux conteneurs et rend possible leur communication. Par exemple, quand il y a un côté partagé entre une chambre et un espace de service comme une salle de bains et une chambre à coucher, de ce côté, certaines exigences de traitement sont nécessaires pour réduire le bruit, et éviter les inondations de la chambre. Chaque forme dans un conteneur a une limite. Une forme est un objet conteneur, qui peut avoir les descriptions nécessaires ou les propriétés de matériaux typiques dans la construction de bâtiments.

### Diagramme d\'objets {#diagramme_dobjets}

Le schéma suivant illustre la relation entre tous les objets décrits à ce jour.

<img alt="Objects for capturing building knowledge" src=images/BldgComponents.png  style="width:800px;">

[Category:Roadmap{{\#translation:}}](Category:Roadmap.md)
