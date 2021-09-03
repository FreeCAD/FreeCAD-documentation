


<div class="mw-translate-fuzzy">

FreeCAD 0.14 a été publié le 1er juillet 2014. Ceci est un résumé des changements les plus intéressants survenus dans FreeCAD depuis la dernière version. Voir [sur Mantis (en anglais)](http://www.freecadweb.org/tracker/changelog_page.php) pour la liste complète des changements. Versions plus anciennes : [0.13](Release_notes_013/fr.md) - [0.12](Release_notes_012/fr.md) - [0.11](Release_notes_011/fr.md)


</div>

<img alt="" src=images/Freecad_jeep.png  style="width:1024px;">


<center>

Modèle d\'une Jeep par Psicofil


</center>

## Général

### Migration du site {#migration_du_site}

Nous avons finalement déplacé toutes les applications web depuis [SourceForge](http://www.sourceforge.net) sur notre [propre domaine](http://www.freecadweb.org). La nouvelle page d\'accueil de FreeCAD se trouve à l\'adresse <http://www.freecadweb.org>, le wiki est maintenant à l\'adresse <http://www.freecadweb.org/wiki>, le système de suivi de bogues et de fonctionnalités est à cette adresse <http://www.freecadweb.org/tracker>, enfin le forum est à l\'adresse suivante : <http://forum.freecadweb.org>. Si vous aviez un compte sur une de ces applications quand elles étaient sur SourceForge alors vous pouvez récupérer votre identifant et mot de passe en suivant ces [instructions](http://forum.freecadweb.org/viewtopic.php?f=8&t=4942).

La seule partie de FreeCAD qui reste sur SourceForge est le dépôt Git, à la même adresse : <http://sourceforge.net/p/free-cad/code/ci/master/tree/> mais il y a aussi un miroir automatisé de ce code sur GitHub, à l\'adresse suivante : <http://github.com/FreeCAD/FreeCAD_sf_master>

Si vous n\'avez pas encore rencontré l\'incroyable communauté FreeCAD, payez-vous une visite sur le forum, et soyez impressionné par son talent, son énergie et son aide généreuse.

### Passage à PySide, FreeCAD est maintenant complètement LGPL {#passage_à_pyside_freecad_est_maintenant_complètement_lgpl}

En raison des nombreuses complications provoquées par le modèle de double-licence de FreeCAD (LGPL et GPL), certains des composants de FreeCAD (à savoir le noyau OpenCasCade) étant incompatibles avec tout code GPL, nous avons décidé de commuter tout le code GPL restant de FreeCAD à LGPL. En raison de cette opération, [PyQt](http://fr.wikipedia.org/wiki/PyQt) n\'est plus employé, et a été remplacé par [PySide](http://fr.wikipedia.org/wiki/PySide). Il n\'y a pas beaucoup de conséquences sur l\'écriture des scripts python, PyQt peut toujours être employé à l\'intérieur de FreeCAD.

Après avoir terminé notre passage à la LPGL, le projet OpenCasCade [aussi passé à la LPGL](http://www.opencascade.org/getocc/license/est), ce qui aurait résolu nos conflits de licence. Mais nous avons désormais un modèle de licence unifié et beaucoup plus clair qui devrait satisfaire toutes les distributions Linux les plus strictes.

### Modules d\'extension et projets parallèles : bibliothèque de Pièces, BOLTS, importateur Eagle {#modules_dextension_et_projets_parallèles_bibliothèque_de_pièces_bolts_importateur_eagle}

La dernière année a vu éclore quelques projets intéressants parallèles à FreeCAD. Une [bibliothèque de pièces](http://github.com/yorikvanhavre/FreeCAD-library) a été lancée par la communauté et croît peu à peu. Elle consiste en une collection de pièces réutilisables à ajouter à vos modèles FreeCAD. Elle peut être lancée et utilisée depuis FreeCAD à l\'aide d\'une macro.

[BOLTS](http://bolts-library.org/) est un autre projet similaire mais plus ambitieux encore. Il s\'agit aussi d\'une bibliothèque de pièces, mais construite à partir de scripts paramétriques, et capable de produire une vaste variété de pièces paramétriques. Même si BOLTS est une application indépendante, elle peut aussi être lancée depuis FreeCAD au moyen d\'une macro. L\'image ci-dessous montre BOLTS fonctionnant sous FreeCAD.

<img alt="" src=images/Freecad-bearing.png  style="width:1024px;">

Un autre projet externe intéressant est l\'[importeur EAGLE](http://sourceforge.net/projects/eaglepcb2freecad/), qui permet d\'importer des designs de circuits imprimés réalisés depuis plusieurs applications sous FreeCAD.

### Export WebGL {#export_webgl}

Depuis FreeCAD, vous pouvez maintenant exporter votre scène comme une page [WebGL](http://fr.wikipedia.org/wiki/WebGL) - HTML. Ce fichier inclut une visionneuse basée sur [three.js](http://threejs.org/) qui permet d\'inspecter la scène depuis le Web sans plugins, tant que vous le regardez avec un navigateur WebGL-compatible.

### Système d\'unités {#système_dunités}

Enfin, un système d\'[unités](units/fr.md) a été mis en œuvre à la base de FreeCAD, il est donc disponible pour tous les modules. Vous pouvez maintenant sélectionner un système d\'unités depuis les préférences. Les systèmes d\'unités disponibles incluent les millimètres, les mètres et les mesures US/impériales (pouces, pieds), mais davantage d\'unités devraient être bientôt disponibles. Une fois le système d\'unités sélectionné, la plupart des propriétés et des outils de FreeCAD utiliseront ces unités de préférence. Mais le système est très flexible, et dans la plupart des cas, vous pouvez combiner les unités autant que vous le voulez ; par exemple saisir des dimensions en pouces dans un document réglé en millimètres.

### Feuilles de style {#feuilles_de_style}

FreeCAD 0.14 devient encore plus personnalisable avec l\'ajout de [Feuilles de style](http://forum.freecadweb.org/viewtopic.php?f=8&t=4700&start=30) utilisées pour contrôler l\'image d\'arrière-plan de la fenêtre principale. L\'utilisateur n\'est plus coincé avec l\'arrière-plan en pierres grises. Presque n\'importe quelle image, photo ou tuile personnalisée peut être utilisée pour remplir l\'arrière-plan de la fenêtre principale de FreeCAD.

<img alt="" src=images/Style_Sheets.png  style="width:1024px;">

### Mode d\'affichage global {#mode_daffichage_global}

La barre d\'outils des vues standard bénéficie de nouveaux boutons pour facilement basculer l\'affichage de la vue 3D complète en mode filaire, ombré ou filaire ombré.

### Anticrénelage de la fenêtre 3D {#anticrénelage_de_la_fenêtre_3d}

De nouvelles options ont été ajoutées au système d\'anticrénelage de la vue 3D de FreeCAD, que vous trouverez dans les préférences. Si vous disposez d\'une bonne carte graphique, vous pouvez maintenant profiter d\'un anticrénelage de haute qualité sous FreeCAD.

## Pièce

### Lissage et Balayage {#lissage_et_balayage}

Les outils [Lissage](Part_Loft/fr.md) et [Balayage](Part_Sweep/fr.md) ont été améliorés et peuvent maintenant utiliser des objets de l\'atelier Draft comme profils.

### Décalage

Le nouvel outil [Décalage](Part_Offset/fr.md) créé des copies d\'une forme sélectionnée à une distance donnée de la forme initiale.

### Évidement

Un nouvel outil [Évidement](Part_Thickness/fr.md) génère une pièce évidée à partir d\'un solide, en donnant une épaisseur donnée à chacune de ses faces.

### Créer un composé {#créer_un_composé}

L\'[atelier Part](Part_Workbench/fr.md) comprend maintenant un outil [Créer un composé](Part_Compound/fr.md) qui vous permet de créer rapidement un objet composé d\'un ensemble de formes sélectionnées.

### Primitives

De nouvelles formes primitives ont été ajoutées à l\'outil [Création de primitives](Part_CreatePrimitives/fr.md) : des prismes, polygones réguliers et des spirales peuvent maintenant être créées facilement en saisissant quelques paramètres. En outre, plusieurs outils de l\'[atelier Draft](Draft_Module/fr.md) tirent parti de cette fonctionnalité et peuvent créer ces formes primitives en lieu et place des objets Draft correspondants, quand l\'option appropriée est sélectionnée dans les paramètres généraux de Draft.

![](images/Part_Create_Primitives1.jpeg )

### Outils de mesure {#outils_de_mesure}


<div class="mw-translate-fuzzy">

Un nouveau jeu d\'outils a été ajouté à l\'[atelier Part](Part_Workbench/fr.md). Vous pouvez sélectionner deux éléments (sommets, arêtes ou faces) pour afficher leur distance absolue et le long des axes X et Y.


</div>

## Part Design & Sketcher {#part_design_sketcher}

### Validateur d\'esquisse {#validateur_desquisse}


<div class="mw-translate-fuzzy">

L\'atelier [Sketcher](Sketcher_Workbench/fr.md) offre un nouvel outil [Valider l\'esquisse](Sketcher_ValidateSketch/fr.md) pour vous aider à valider une esquisse en trouvant les contraintes manquantes ou redondantes. Il peut également ajouter automatiquement certaines contraintes manquantes, afin de rendre votre esquisse entièrement contrainte.


</div>

### Générateur d\'engrenage {#générateur_dengrenage}


<div class="mw-translate-fuzzy">

Un [générateur d\'engrenage à profil en développante de cercle](PartDesign_InvoluteGear/fr.md) a été ajouté à l\'[atelier PartDesign](PartDesign_Workbench/fr.md) pour créer rapidement des engrenages à partir de quelques paramètres.


</div>

## Drawing (Mise en plan) {#drawing_mise_en_plan}

### Projections automatiques {#projections_automatiques}

L\'atelier Drawing (mise en plan) continue d\'être amélioré avec d\'excitantes nouvelles fonctionnalités. L\'outil « Insérer des vues orthogonales » permet de créer plusieurs vues projetées à la fois, et de gérer plus facilement leur emplacement. Une autre fonction-clé, les modèles de feuille peuvent maintenant contenir des données définissant les bordures et l\'emplacement du cartouche, ce qui confinera automatiquement les vues à l\'intérieur des bordures, tout en évitant l\'espace occupé par le cartouche.

<img alt="" src=images/DrawingWB.png  style="width:1024px;">

### Symboles

Un nouvel outil [symbole](Drawing_Symbol/fr.md) est maintenant disponible dans l\'atelier [Drawing (mise en plan)](Drawing_Module/fr.md), permettant de placer des objets SVG sur la feuille. Ces objets sont stockées dans le document FreeCAD, vous n\'avez donc pas à expédier le fichier SVG original si vous distribuez vos documents.

## Lancer de rayons {#lancer_de_rayons}

### Nouveaux outils de rendu {#nouveaux_outils_de_rendu}

<img alt="" src=images/Raytracing_example.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

L\'atelier de [Raytracing (lancer de rayon)](Raytracing_workbench/fr.md) a aussi reçu un peu d\'amour, et sa barre d\'outils a été retravaillée. Les anciens boutons qui produisaient manuellement des fichiers povray fragmentaires ont été enlevés (mais leurs outils correspondants se trouvent toujours dans le menu Lancer de rayon), et vous pouvez maintenant produire des rendus à peu près de la même façon que vous utilisez l\'atelier [Drawing](Drawing_workbench/fr.md) : vous créez un nouveau projet, lui assignez un modèle, puis le remplissez avec des vues de vos objets. Quand vous avez terminé, cliquez simplement sur le bouton « Rendre » ou exportez le projet dans un fichier prêt à rendre dans une autre application.


</div>


<div class="mw-translate-fuzzy">

Le système de[modèles Raytracing](Raytracing_workbench/fr#Modèles.md) a aussi été étendu, et les modèles sont maintenant plus facile à créer et manipuler.


</div>

Les scripts .pov produits par FreeCAD contiennent maintenant un ratio d\'aspect automatique. L\'utilisateur n\'a plus besoin de maintenir un ratio de 4:3 dans les réglages Raytracing ou d\'éditer manuellement la sortie pour modifier le ratio en vue d\'obtenir un rendu approprié. N\'importe quelles largeur et hauteur peuvent maintenant être saisies sans crainte que les objets rendus soient compressés ou étirés.

### Support de LuxRender {#support_de_luxrender}


<div class="mw-translate-fuzzy">

En même temps que le support pour [POV-Ray](http://fr.wikipedia.org/wiki/Pov-ray), l\'[atelier Raytracing workbench](Raytracing_workbench/fr.md) supporte maintenant aussi [LuxRender](http://fr.wikipedia.org/wiki/LuxRender). Alors que POV-Ray est un [moteur de lancer de rayon classique](http://fr.wikipedia.org/wiki/Lancer_de_rayon) qui lance des rayons depuis la caméra afin de trouver la couleur de chaque pixel d\'une image, LuxRender est un [moteur de rendu non biaisé](http://en.wikipedia.org/wiki/Unbiased_rendering). Les scènes prennent beaucoup plus de temps à rendre, mais produisent un éclairage bien plus réaliste.


</div>

## Tableur

Un nouveau [Tableur](Spreadsheet_Workbench/fr.md) a été ajouté à FreeCAD. Il permet de créer des [tableaux](Spreadsheet_Create/fr.md) qui contiennent des données tableur bidimensionnelles. Il propose aussi un éditeur, vous pouvez donc éditer le contenu d\'un tableau (le texte, les nombres et quelques formules simples sont supportés) ainsi qu\'un [contrôleur de cellule](Spreadsheet_Controller.md) qui peut parcourir le document à la recherche de certains types d\'objets, extraire une propriété de ceux-ci, et remplir un ensemble donné de cellules avec ces valeurs.

<img alt="" src=images/Arch_tutorial_53.jpg  style="width:1024px;">

## Draft (planche à dessin) {#draft_planche_à_dessin}

### Importation/exportation DWG {#importationexportation_dwg}

FreeCAD est maintenant capable d\'importer et d\'exporter le [format DWG](https://fr.wikipedia.org/wiki/.dwg), merci au logiciel gratuit et multi-plateforme [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter). Une fois qu\'il es installé et son chemin d\'accès défini dans les préférences de l\'atelier Draft, FreeCAD pourra l\'utiliser pour importer et exporter des fichiers DWG, en les convertissant d\'abord en DXF puis en utilisant la fonction importation/exportation de DXF de l\'atelier Draft. L\'importation et l\'exportation des fichier DWG ont par conséquent les même limitations que pour le [format DXF](Draft_DXF/fr.md).

### Draft vers Plan fonctionne avec les groupes {#draft_vers_plan_fonctionne_avec_les_groupes}


<div class="mw-translate-fuzzy">

L\'outil [Draft vers Mise en plan](Draft_Drawing.md), qui sert à placer des objets de type Draft sur une [Mise en plan](Drawing_Module/fr.md), peut maintenant être appliqué sur des groupes, permettant de créer moins d\'objets Vue sur une mise en plan. Avec une gestion intelligente des groupes d\'objets Draft, vous avez une façon simple de contrôler l\'apparence de plusieurs objets sur votre page.


</div>

### Cotations recodées {#cotations_recodées}


<div class="mw-translate-fuzzy">

L\'outil [Cote](Draft_Dimension/fr.md) a été complètement recodé: les cotes se comportent maintenant beaucoup mieux et elles ont gagné quelques nouvelles propriétés permettant de mieux les affiner, comme de plus belles flèches à taille variable, plus de contrôle sur la position du texte et la direction de la cote, et surtout un meilleur support de l\'atelier [Drawing (mise en plan)](Drawing_Module/fr.md). Vous pouvez maintenant placer des cotes sur n\'importe quel plan dans l\'espace 3D, et vous attendre à des résultats corrects quand vous les projetez sur une feuille de mise en plan avec l\'outil [Dessin](Draft_Drawing/fr.md).


</div>

<img alt="" src=images/Draft_dimensions_recode.jpg  style="width:1024px;">

### Hachures


<div class="mw-translate-fuzzy">

L\'[atelier Draft](Draft_Module/fr.md) propose aussi un nouveau « jouet » : les hachures. Sur des objets Draft spécifiques (ceux qui forment un profil fermé comme les polylignes fermées, les rectangles, les polygones réguliers et les cercles), il est maintenant possible d\'appliquer des hachures. À l\'heure actuelle, seulement quelques motifs de hachure par défaut sont disponibles, mais puisque ces motifs sont très facile à créer (il s\'agit de simples fichiers SVG) et que des motifs personnalisés peuvent déjà être ajouté par l\'utilisateur, la collection de base pourraît croître rapidement. Les objets Draft contenant un motif sont aussi pleinement supportés par l\'atelier [Drawing (mise en plan)](Drawing_Module/fr.md).


</div>

<img alt="" src=images/Draft_hatches.jpg  style="width:1024px;">

### Ellipses

Le support des [ellipses](Draft_Ellipse/fr.md) a été ajouté, l\'atelier Draft permet maintenant de dessiner des ellipses complètes ou partielles.

### Chanfrein

De la même façon que les congés qui sont apparus dans la [version 013](Release_notes_013/fr.md), les rectangles, les filaires et les polygones ont gagné une propriété chanfrein qui chanfreine leurs sommets. Le chanfrein est appliqué avec le congé, et les deux propriétés peuvent être utilisées simultanément, vous permettant de convertir un filaire simple en un objet complexe fait de plusieurs sections.

### Outils Mise à niveau et Rétrograder recodés {#outils_mise_à_niveau_et_rétrograder_recodés}

Les outils [Mise à niveau](Draft_Upgrade/fr.md) et [Rétrograder](Draft_Downgrade/fr.md) qui étaient auparavant des fragments hermétiques de magie dont vous ne pouviez jamais être sûr des résultats ont été recodés. Ils génèrent maintenant des messages beaucoup plus conviviaux, vous informant de ce qui a été produit et pourquoi. Ils sont maintenant accessibles par script python, pas seulement dans leur ensemble mais par leurs opérations internes ; vous pouvez donc précisément définir quel type de mise à niveau doit être effectué.

### Copie de face {#copie_de_face}


<div class="mw-translate-fuzzy">

Le nouvel outil [Facebinder](Draft_Facebinder/fr.md) effectue une opération très simple mais potentiellement très utile : il assemble un groupe de faces sélectionnées depuis différents objets, et créé un nouvel objet à partir de ces faces. Le nouvel objet conserve des liens avec les objets initiaux, donc tout changement de ceux-ci se reflète sur l\'objet Facebinder. Ceci devrait s\'avérer utile surtout pour les objets [architecturaux](Arch_Module/fr.md), en construisant de nouveaux objets à partir des faces de plusieurs autres objets.


</div>

### Texte surfacique {#texte_surfacique}

L\'outil [Draft ShapeString](Draft_ShapeString/fr.md) créé des objets planaires à partir d\'une chaîne de texte et d\'une police TrueType. Ces objets, contrairement aux annotations [Texte](Draft_Text/fr.md) communes, sont de vrais objets 3D, et peuvent donc être extrudés puis utilisés pour créer de la gravure ou autres objets 3D avec du texte en relief.

### Courbes de Bézier {#courbes_de_bézier}


<div class="mw-translate-fuzzy">

Un nouveau type de courbe accompagne désormais les [arcs de cercle](Draft_Arc/fr.md) et les [courbes BSpline](Draft_BSpline/fr.md) : les [courbes de Bézier](Draft_BezCurve/fr.md). Elles peuvent être créées en cliquant des points de la même manière que les autres objets Draft, mais vous pouvez ensuite les [éditer](Draft_Edit/fr.md) et modifier leurs points de contrôle, obtenant ainsi un contrôle très précis sur la forme de la courbe.


</div>

## Architecture

### Préréglages et profilés de structures {#préréglages_et_profilés_de_structures}

L\'outil [Structure](Arch_Structure/fr.md) a gagné plusieurs améliorations : il comporte maintenant des préréglages qui permettent de construire des poutres ou des colonnes basées sur des profils standards comme INP ou HEB, et un système de placement plus facile avec un mode spécial d\'[accrochage](Draft_Snap/fr.md). Vous pouvez maintenant également donner un chemin d\'extrusion aux éléments structurels afin de rendre possible des configurations avancés. Certaine des pièces offertes par [BOLTS](#Modules_d.27extension_et_projets_parall.C3.A8les_:_biblioth.C3.A8que_de_Pi.C3.A8ces.2C_BOLTS.2C_importateur_Eagle.md) peuvent aussi être directement créées comme des éléments structurels architecturaux.

### Préréglages des fenêtres {#préréglages_des_fenêtres}

L\'outil [Fenêtre](Arch_Window/fr.md) a également gagné un nouveau système de préréglages. Bien que toujours basé sur des esquisses, qui assurent la flexibilité maximale (pratiquement n\'importe quel type de fenêtre peut être facilement créé), de nouvelles fenêtres peuvent maintenant être créées à partir d\'une série de préréglages. Vous devez seulement choisir un préréglage, remplir quelques paramètres, et placer votre fenêtre sur un mur existant ou un élément structurel. Un croquis associé sera créé, qui sera éditable à n\'importe quelle moment.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:1024px;">

### Volumes

Un nouvel objet [Espace](Arch_Space/fr.md) est maintenant disponible, permettant de construire, annoter et calculer les espaces et les surfaces couvertes. Ces objets Espaces entourent toujours un volume solide, ainsi vous pouvez toujours connaître leur volume et surface couverte. Ils peuvent être construits à partir d\'une forme solide ou d\'un ensemble de faces.

### Murs multicouches {#murs_multicouches}

Les [Murs](Arch_Wall/fr.md) peuvent maintenant être multicouches à l\'aide d\'une astuce très simple : plusieurs murs peuvent partager la même ligne référence, en définissant la distance de décalage depuis la ligne de référence. Ceci permet, en conjonction avec les [ossatures](Arch_Frame/fr.md) de créer par exemple des murs complexes à ossature, ou des murs isolés. En outre, ces murs sont conscients de leurs « frères » (d\'autres murs basés sur une même ligne de référence) et toute fenêtre placée sur l\'un de ces murs passera également à travers des autres murs.

<img alt="" src=images/Screenshot_arch_multiwall.jpg  style="width:1024px;">

### Escaliers

Un nouvel outil [Escalier](Arch_Stairs/fr.md) permet de construire des escaliers complexes à partir de quelques paramètres. Pour l\'instant, seuls des escaliers droits sont disponibles, mais la liste grossira avec le temps. Ces escaliers proposent plusieurs paramètres de configuration, tels que la taille au plancher de l\'escalier, ou leur type de structure.

### Barres de renforcement {#barres_de_renforcement}

Les barres d\'armature sont introduites avec l\'outil [Barres d\'armature](Arch_Rebar/fr.md). Elles sont aussi basées sur des esquisses, ce qui assure une grande polyvalence. Elles sont créées en dessinant des diagrammes des barres sur les faces appropriées d\'[éléments structuraux](Arch_Structure/fr.md), puis en convertissant ces diagrammes en barres d\'armature.

<img alt="" src=images/Screenshot_arch_rebar.jpg  style="width:1024px;">

### Ossatures

Les ossatures sont abondamment utilisées en architecture : les rampes, systèmes structuraux, murs à ossature, etc. Le nouvel outil [Ossature](Arch_Frame/fr.md) permet de créer facilement toutes sortes d\'ossatures, en combinant un profil qui peut être n\'importe quel type de forme planaire extrudable comme des rectangles ou des cercles, et un agencement. Les agencements peuvent être dessinés dans l\'[atelier Sketcher](Sketcher_Workbench/fr.md). Ces ossatures peuvent ensuite être converties en murs ou en structure au besoin.

### Prise de cotes {#prise_de_cotes}

Un autre outil simple mais utile maintenant disponible dans l\'atelier Arch est la [Prise de cotes](Arch_Survey/fr.md). Dans ce mode, vous cliquez sur des sommets, des arêtes, des faces ou des objets complets pour obtenir leur hauteur, longueur, aire ou volume. Cette information est affichée sur le modèle, mais aussi copiée dans le presse-papiers, et colligée au format texte. Il est donc facile de la coller dans d\'autres applications et de vous procurer un flux de travail efficace pour la rédaction de liste de quantités.

### Tutoriel

Un nouveau [tutoriel](Arch_tutorial.md) de 35 pages décrit l\'atelier Arch dans tous ses détails, en suivant un exercice complet.

### Import/export du format IFC {#importexport_du_format_ifc}


<div class="mw-translate-fuzzy">

Beaucoup de travail a été accompli à la fois sur FreeCAD et [IfcOpenShell](http://www.ifcopenshell.org), qui est le logiciel gérant les fichiers IFC sous le module Arch. L\'utilisation d\'une [version de développement](http://github.com/aothms/IfcOpenShell) de IfcOpenShell, en plus de permettre un gain de performance spectaculaire lors de l\'importation de fichiers IFC de taille moyenne (enciron 50 Mo), permet également à FreeCAD d\'exporter des modèles au format IFC. Cette fonctionnalité, bien que toujours aux premiers stades de développement, peut déjà exporter des fichiers lisibles sans erreurs par les applications majeures supportant ce format.


</div>

## Liste complète {#liste_complète}

La liste complète des corrections de bogues et des nouvelles fonctionnalités peut être consultée sur <http://freecadweb.org/tracker/changelog_page.php>

[Category:News{{\#translation:}}](Category:News.md) [Category:Documentation{{\#translation:}}](Category:Documentation.md) [Category:Releases{{\#translation:}}](Category:Releases.md)
