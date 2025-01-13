---
 TutorialInfo:r
   Topic: Analyse par éléments finis
   Level: Débutant
   Time: Non applicable
   Author: https://www.freecad.org/wiki/index.php?title=User:NewJoker NewJoker
   FCVersion: 1.0 ou plus récente
   SeeAlso: FEM_Workbench/fr
---

# FEM Geometry Preparation and Meshing/fr







## Contexte

La préparation de la géométrie et le maillage sont des éléments cruciaux du prétraitement des simulations utilisant la méthode des éléments finis (FEM). Bien que les logiciels de simulation facilement accessibles et connectés à un environnement CAO (comme l\'[atelier FEM](FEM_Workbench/fr.md) dans FreeCAD) rendent tentante la réalisation immédiate d\'analyses sur de nouvelles conceptions, il est très important de se rappeler que la FEM est une méthode avancée et qu\'elle nécessite une géométrie et un maillage correctement préparés afin de fournir des résultats raisonnables et précis. La vieille règle [*garbage in, garbage out*](https://fr.wikipedia.org/wiki/GIGO) est particulièrement importante ici. Il existe également d\'autres paramètres cruciaux dont la précision de la FEM dépend fortement (tels que les propriétés des matériaux et les conditions aux limites), mais les premières étapes et certaines des sources de problèmes les plus courantes sont la préparation de la géométrie et le maillage, dont il est question sur cette page.



## Types de géométrie utilisés pour la méthode des éléments finis dans FreeCAD 

-   Lignes (polylignes) : pour les analyses avec des éléments de poutre
-   Surfaces : pour les analyses avec des éléments de coque et des éléments 2D (contraintes et déformations planes et axisymétriques)
-   Solides : pour les analyses avec des éléments solides



## Choix du type de géométrie 

Bien que la plupart des conceptions soient constituées de solides, il est souvent fortement recommandé d\'utiliser des polylignes ou des surfaces pour les éléments finis si la structure le permet :

-   Si une pièce est mince (longue et fine) et en forme de poutre et a une section transversale régulière de l\'un des types de section de poutre actuellement supportés (rectangulaire, circulaire ou tube), elle doit être analysée à l\'aide d\'éléments de poutre (à moins qu\'il n\'y ait des formes spécifiques de charge, de réponse ou des détails géométriques inévitables qui invalident cette supposition). Fondamentalement, il faut dessiner une ligne centrale (des conseils sur la manière de l\'extraire d\'une géométrie solide existante peuvent être trouvés dans [ce fil de discussion](https://forum.freecad.org/viewtopic.php?t=81589)) et appliquer une [section de poutre](FEM_ElementGeometry1D/fr.md) appropriée avec une éventuelle [rotation](FEM_ElementRotation1D/fr.md). Il n\'y a pas de règle unique dictant quand les éléments de poutre peuvent être utilisés, mais il est souvent conseillé que les dimensions de la section transversale soient \< 1/10 de la longueur de la pièce pour que l\'hypothèse de la poutre soit valide.

<img alt="" src=images/FEM_beam_model.JPG  style="width:600px;">



*Pièce mince convenant à l'analyse avec des éléments de poutre - axe central mis en évidence*

-   Si une pièce a des parois minces (comme les pièces en tôle), elle doit être analysée à l\'aide d\'éléments de coque (sauf si des résultats de contact précis sont nécessaires ou si certaines limites des éléments de coque sont rencontrées). Ce point est très important et souvent négligé. Pour obtenir des résultats précis (en particulier en cas de flexion), il faut quelques éléments (au moins 3 à 5) dans la direction de l\'épaisseur. Dans le cas de pièces à parois minces, cela se traduit généralement par de grandes mailles (en particulier lorsque des tétraèdres sont utilisés, car les éléments hexaédriques ne peuvent pas être générés dans FreeCAD) et un coût de calcul élevé - puissance informatique élevée et long temps de résolution. Pour obtenir une géométrie adaptée à l\'analyse avec des éléments coques, il faut dessiner une surface médiane de la pièce (des conseils sur la manière de l\'extraire d\'une géométrie solide existante peuvent être trouvés dans [ce fil de discussion](https://forum.freecad.org/viewtopic.php?t=67505), [celui-ci](https://forum.freecad.org/viewtopic.php?t=71821) et [celui-ci](https://forum.freecad.org/viewtopic.php?t=81834)) et appliquer une [épaisseur](FEM_ElementGeometry2D/fr.md) appropriée. Là encore, il n\'y a pas de règle unique, mais il est généralement recommandé que l\'épaisseur soit \< 1/10 d\'une dimension globale typique (longueur/largeur) pour que l\'hypothèse de la coque soit valide.

<img alt="" src=images/FEM_shell_model.JPG  style="width:600px;">



*Pièce à paroi mince adaptée à l'analyse avec des éléments de coque - mise en évidence de la surface médiane*

-   Dans certains cas, les analyses 2D sont également possibles et peuvent être activées en définissant la propriété **Model Space** du [solveur CalculiX](FEM_SolverCalculixCxxtools/fr.md) :
    -   contrainte plane : pour les pièces minces qui peuvent être simplifiées en surfaces planes représentant le profil d\'extrusion (l\'épaisseur est définie de la même manière que pour les coques), sont chargées et se déforment uniquement dans le plan et ont une contrainte nulle dans la direction hors du plan. Seuls deux degrés de liberté sont disponibles : la translation en X et en Y. Dans ce cas, les surfaces doivent se situer sur le plan XY. Cette approche est assez courante. Par exemple, une plaque mince soumise à une tension peut être analysée de cette manière.
    -   déformation dans le plan : pour les pièces épaisses qui peuvent être simplifiées en surfaces planes représentant le profil d\'extrusion (l\'épaisseur est définie de la même manière que pour les coquilles), sont chargées et se déforment uniquement dans le plan et ont une déformation nulle dans les directions hors du plan. Seuls deux degrés de liberté sont disponibles : la translation en X et en Y. Dans ce cas, les surfaces doivent être situées sur le plan XY. Cette approche n\'est pas très courante. Par exemple, un long barrage, un mur ou un tuyau soumis à une pression uniforme sur toute sa longueur peut être analysé de cette manière.
    -   axisymétrique : pour les pièces qui peuvent être simplifiées en surfaces planes représentant le profil tournant (l\'épaisseur n\'a pas d\'importance ici) et qui sont chargées uniformément sur toute la circonférence. Seuls deux degrés de liberté sont disponibles : la translation radiale et la translation axiale. Les surfaces doivent être situées sur le plan XY, à droite de l\'axe Y. Cette approche est très courante. Par exemple, certains récipients sous pression, les supports en caoutchouc, les bagues, les joints, les brides et même les assemblages boulonnés (en considérant le filetage comme axisymétrique) peuvent être analysés de cette manière.

Il convient de rappeler que les éléments poutre, coque, contrainte/déformation plane et axisymétrique utilisés dans CalculiX ne sont pas de véritables éléments de ce type (ils n\'utilisent pas les formulations d\'éléments classiques connues dans la littérature et dans d\'autres logiciels), ils sont étendus en interne aux solides. Néanmoins, leur utilisation est recommandée dans les cas susmentionnés.



## Validité de la géométrie 

La géométrie utilisée pour la simulation par éléments finis doit être valide. Plus important encore, il ne doit pas y avoir d\'intersections. Il s\'agit d\'un problème courant qui survient souvent lorsque des assemblages sont modélisés sans contraintes appropriées entre les pièces. L\'outil [Part Coupe persistante](Part_SectionCut/fr.md) peut aider à trouver de telles interférences entre les pièces. Bien entendu, l\'outil [Part Union](Part_Fuse/fr.md) peut aider à les résoudre si elles sont intentionnelles. D\'autres problèmes liés à la géométrie (tels que les géométries non pliantes, les arêtes ou faces redondantes, etc.) doivent également être résolus avant de procéder au maillage. L\'outil [Part Vérifier la géométrie](Part_CheckGeometry/fr.md) peut être utile, mais les contrôles visuels sont également importants. Lors de la préparation d\'une simulation utilisant des éléments solides et en cas de doute quant à savoir si la pièce est réellement solide ou s\'il s\'agit simplement d\'une coque fermée, les outils susmentionnés (Part Coupe persistante et l\'onglet *Contenu de la forme* de Part Vérifier la géométrie) peuvent permettre de clarifier la situation.



## Simplification de la géométrie 

Les designs préparés dans les logiciels de CAO sont généralement trop détaillés pour être adaptées aux simulations par éléments finis. Dans de nombreux cas, il est nécessaire de les simplifier au préalable. Cette étape est souvent négligée, mais elle est très importante car il peut être difficile d\'obtenir un bon maillage lorsque la pièce est trop détaillée et même si un tel maillage est finalement obtenu, il peut être très dense, ce qui entraîne des temps de résolution déraisonnables. Il faut donc toujours examiner la conception et essayer de la simplifier autant que possible, en ne laissant que les caractéristiques géométriques qui peuvent avoir un impact significatif sur les résultats (résistance/rigidité) et qui ne peuvent donc pas être ignorées. Les caractéristiques suivantes sont généralement omises

-   les petits congés et chanfreins,
-   petits trous,
-   autres petits détails,
-   soudures,
-   boulons, filetages,
-   les éléments décoratifs (logos, gravures).

L\'outil [Part Supprimer la fonction](Part_Defeaturing/fr.md) et l\'[extension Defeaturing](Defeaturing_Workbench/fr.md) peuvent être utiles pour simplifier les pièces pour les simulations.

<img alt="" src=images/FEM_bracket_original.PNG  style="width:400px;">



*Géométrie originale du support*

<img alt="" src=images/FEM_bracket_simplified.PNG  style="width:400px;">



*Géométrie du support simplifiée en utilisant uniquement l'outil Part Supprimer la fonctionnalité*

Dans le cas des assemblages (plus d\'informations à ce sujet dans l\'une des sections suivantes), certaines pièces peuvent souvent être exclues des simulations et remplacées par des conditions aux limites comme si elles étaient attachées aux pièces à analyser. Cette approche est valable si les pièces exclues sont significativement plus rigides (en termes de rigidité structurelle, en tenant compte non seulement de l\'élasticité du matériau mais aussi de la géométrie de la pièce) que les pièces à analyser auxquelles elles étaient connectées. En effet, les conditions aux limites fixes introduisent de la rigidité (comme si la pièce analysée était attachée à un composant infiniment rigide) et les supports flexibles comme les éléments ressorts ne sont pas disponibles dans l\'atelier FEM de FreeCAD lorsque l\'on utilise CalculiX (Elmer a un [FEM Ressort](FEM_ConstraintSpring/fr.md)).

La simplification de la géométrie pour la simulation par éléments finis peut également impliquer de la couper dans l\'un des plans de symétrie afin d\'utiliser l\'hypothèse de symétrie plane dans l\'analyse. Cette hypothèse n\'est valable que lorsque tous les aspects suivants du modèle présentent une symétrie dans un plan donné :

-   géométrie,
-   charges,
-   conditions aux limites,
-   réponse (il faut être prudent avec les analyses de fréquence/flexion utilisant la symétrie - on n\'obtiendra pas de formes de mode antisymétriques).

L\'utilisation de la symétrie (1/2, 1/4 ou 1/8 du modèle) est recommandée dans la mesure du possible, car elle permet de réduire considérablement le coût de calcul de l\'analyse. Un autre avantage est qu\'elle élimine certains mouvements des corps rigides, ce qui facilite la contrainte de la pièce. Une condition limite de symétrie doit être appliquée aux faces appartenant au plan de coupe :

-   la translation dans la direction normale au plan de symétrie doit être bloquée pour les pièces solides,
-   la translation dans la direction normale au plan de symétrie et les rotations autres qu\'autour de l\'axe normal au plan de symétrie doivent être bloquées pour les pièces de coque et de poutre.

La force appliquée doit être correctement réduite si le plan de symétrie coupe la région à laquelle la force est appliquée (sans importance lorsque la charge de pression est utilisée).

<img alt="" src=images/FEM_symmetric_vessel.JPG  style="width:400px;">



*Modèle de 1/8 d'un récipient sous pression cylindrique avec des conditions limites de symétrie et une charge de pression interne*

Un autre type de symétrie, moins courant, disponible dans FreeCAD FEM est la symétrie cyclique. Elle peut être définie à l\'aide de la [contrainte de liaison](FEM_ConstraintTie/fr#Symétrie_cyclique.md) et permet d\'analyser un seul secteur représentatif d\'une structure constituée de tels motifs circulaires autour d\'un axe. L\'hypothèse est que les conditions aux limites et les charges présentent également cette forme de symétrie. Des charges tangentielles peuvent être appliquées et la torsion peut donc être simulée de cette manière. Cependant, une [charge centrifuge](FEM_ConstraintCentrif/fr.md) est généralement utilisé avec la symétrie cyclique. Cette approche peut être utilisée par exemple pour les rotors, les arbres, les turbines, les ventilateurs et les volants d\'inertie.



## Partitionnement de la géométrie 

Le partitionnement est une division de la géométrie en segments plus petits. Dans d\'autres logiciels, il est généralement utilisé pour permettre le maillage hexagonal, mais dans FreeCAD, il peut être utile pour d\'autres raisons. La principale application du partitionnement est lorsqu\'une charge (ou une condition limite) doit être appliquée uniquement à une région sélectionnée de la surface de la pièce. La façon la plus simple d\'y parvenir est de créer une esquisse avec un contour approprié sur cette face et d\'utiliser l\'outil [Part Fragments booléens](Part_BooleanFragments/fr.md) pour diviser la face avec l\'esquisse. Une autre raison d\'utiliser le partitionnement est lorsque plusieurs matériaux doivent être appliqués à une seule pièce (sans avoir à utiliser plusieurs pièces connectées entre elles). Dans ce cas, le partitionnement peut être effectué à l\'aide d\'un [plan](PartDesign_Plane/fr.md) et de l\'outil Fragments booléens en mode *Compsolid*. Le partitionnement peut également être utilisé pour créer des régions pour [mailler plus finement](FEM_MeshRegion/fr.md).

<img alt="" src=images/FEM_partition.JPG  style="width:400px;">



*Pièce avec une cloison de séparation pour l'application d'une charge ou d'une condition limite*



## Assemblage de géométries 

L\'une des principales limitations actuelles de l\'atelier FEM est que les maillages multiples ne sont pas pris en charge. En pratique, cela signifie qu\'il n\'est pas possible de mailler chaque pièce de l\'assemblage individuellement, puis de connecter les pièces avec les contraintes appropriées pour l\'analyse. Il est donc nécessaire de créer un objet unique contenant toutes les pièces de l\'assemblage et de le mailler. Il existe plusieurs options différentes, toutes basées sur les [Part Outils booléens](Part_Workbench/fr#Barres_d'outils_des_booléens.md). Le choix dépend de l\'effet désiré : si chaque pièce/volume et leurs limites doivent être sélectionnables (par exemple pour l\'affectation de matériaux ou les définitions des conditions limites agissant sur les faces internes) ou non :

-   [Part Union](Part_Fuse/fr.md) : fusionne les pièces, rendant impossible leur sélection individuelle, par exemple pour les définitions de matériaux,
-   [Part Composé](Part_Compound/fr.md) : crée un objet composé, ce qui permet de sélectionner chaque pièce,
-   [Part Connecter](Part_JoinConnect/fr.md) : fonctionne comme Part Union, mais fusionne les parties, ce qui rend impossible leur sélection individuelle,
-   [Part Fragments booléens](Part_BooleanFragments/fr.md) : fonctionne comme Part Composé, ce qui permet de sélectionner chaque partie.

Il est important de mentionner que si les pièces se touchent, un maillage continu sera créé sur l\'objet booléen et aucune contrainte ne sera nécessaire pour la simulation. S\'il y a un petit espace entre les pièces (ou une intersection à l\'intérieur d\'un Part Composé), le maillage ne sera pas continu et des contraintes comme la [Contrainte de liaison](FEM_ConstraintTie/fr.md) ou la [Contrainte de contact](FEM_ConstraintContact/fr.md) seront nécessaires. L\'exécution d\'une analyse en fréquence est un bon moyen de révéler si le maillage est continu ou non. Si les pièces ne sont pas connectées, les premières formes des modes avec déformation visualisées à l\'aide du [filtre des déformations](FEM_PostFilterWarp/fr.md) montreront une séparation, les pièces \"s\'envoleront\".

<img alt="" src=images/FEM_modal_separation.JPG  style="width:400px;">



*La forme du premier mode d'une analyse de fréquence visualisée avec le filtre des déformations - deux cubes avec un petit écart initial ont été analysés.*

La sélection des régions internes (faces/volumes) peut s\'avérer délicate. Elle peut être nécessaire pour l\'application de différents matériaux, charges ou conditions aux limites (en particulier dans les analyses thermiques et électromagnétiques). Plusieurs méthodes sont possibles :

-   activer [plan de coupe](Std_ToggleClipPlane/fr.md) pour la sélection et le choix des faces internes,
-   masquer l\'objet booléen, ne montrer qu\'une des parties auxquelles il a été appliqué et la sélectionner,
-   sélectionner un autre objet externe et éditer la propriété *References* dans l\'onglet *Données* d\'un élément d\'analyse donné (nécessite la spécification manuelle du numéro de l\'objet géométrique).



## Les bases du maillage 

Un maillage trop grossier est l\'une des sources les plus courantes d\'inexactitudes et d\'autres problèmes dans les simulations par éléments finis. Il s\'agit souvent d\'une erreur partielle des paramètres du maillage automatique. Ils génèrent généralement des maillages très grossiers et inadaptés lorsque la taille des éléments n\'est pas spécifiée manuellement, mais laissée avec une valeur par défaut. Il faut toujours connaître les dimensions approximatives de la pièce, en particulier la taille du plus petit élément pertinent (l\'outil [Std Mesurer](Std_Measure/fr.md) peut être utilisé pour la trouver) et spécifier la taille maximale appropriée de l\'élément en fonction de celle-ci. Il existe également un réglage de la taille minimale des éléments qui peut empêcher la création d\'éléments trop petits autour de petites caractéristiques géométriques, ce qui peut conduire à des maillages inutilement denses (et parfois même à un plantage ou à un gel de FreeCAD lorsqu\'on essaie de générer de tels maillages). D\'une manière générale, il est préférable de commencer par un maillage plus grossier (moins long à générer), de voir à quoi il ressemble (une certaine expérience est nécessaire) et de l\'affiner si nécessaire. Il est souvent judicieux d\'utiliser un maillage dense uniquement autour des zones d\'intérêt (endroits présentant des gradients/concentrations de contraintes importants - encoches) et un maillage relativement grossier à l\'écart de ces zones. De cette manière, le nombre d\'éléments peut être considérablement réduit, ce qui permet de diminuer les temps de résolution. L\'amélioration du maillage local est défini à l\'aide de [FEM Mailler plus finement](FEM_MeshRegion/fr.md).

<img alt="" src=images/FEM_default_mesh.PNG  style="width:400px;">



*Par défaut, maillage trop grossier*

<img alt="" src=images/FEM_globally_refined_mesh.PNG  style="width:400px;">



*Maillage amélioré globalement*

<img alt="" src=images/FEM_locally_refined_mesh.PNG  style="width:400px;">



*Maillage amélioré localement*

Le choix du type d\'élément n\'est pas facile et dépend de nombreux facteurs, mais la règle générale est que les éléments hexaédriques et quadrilatéraux sont préférables aux éléments tétraédriques et triangulaires. Cependant, les géométries complexes ne peuvent pas être maillées avec des éléments hexaédriques et FreeCAD ne peut pas les générer correctement (uniquement en utilisant l\'algorithme de subdivision du maillage Gmsh, mais ses résultats ne sont pas ceux que l\'on attendrait d\'un maillage hexagonal). Les maillages quadratiques ou à dominante quadratique peuvent être générés normalement sur les surfaces, voir [ce fil de discussion](https://forum.freecad.org/viewtopic.php?t=20351)). Les éléments hexaédriques peuvent être importés à partir de maillages externes comme [Gmsh](https://gmsh.info) et utilisés dans l\'atelier FEM comme le montre [cette vidéo](https://www.youtube.com/watch?v=vylt24G7qj4&t=932s).

Le choix de l\'ordre des éléments (premier ou second) dépend des conditions d\'analyse, mais dans la plupart des cas, les éléments de second ordre sont préférables. Ceci est particulièrement vrai pour les éléments triangulaires et tétraédriques, leurs versions de premier ordre (linéaires) ne sont normalement pas recommandées pour un usage régulier et ne devraient être utilisées que comme éléments de remplissage dans des régions de faible importance. Cependant, comme FreeCAD ne peut pas générer correctement d\'éléments hexaédriques, les tétraèdres linéaires peuvent être utilisés dans certains cas, si les maillages sont suffisamment denses. En particulier lors d\'analyses avec une [contrainte de contact](FEM_ConstraintContact/fr.md).



## Jacobiens négatifs 

Si les règles ci-dessus sont respectées (notamment en ce qui concerne la validité de la géométrie, le defeaturing et la sélection de la taille des éléments), le maillage devrait être généré correctement. Cependant, dans certains cas, la géométrie ne peut pas être trop simplifiée, ou la procédure de modélisation est appropriée mais conduit quand même à des arêtes et des faces de petite taille. Dans ce cas, le maillage avec des éléments de second ordre peut échouer en raison de jacobiens négatifs. La raison en est que les maillages doivent suivre le modèle CAO et placer les nœuds médians des éléments de second ordre sur la géométrie. Dans le cas de formes plus complexes, les éléments peuvent être tellement étirés qu\'ils deviennent inversés. Le jacobien est l\'une des mesures de qualité de maillage les plus courantes. Il représente l\'écart de l\'élément par rapport à la forme idéale. Elle devient négative lorsque l\'élément se retourne (devient inversé), soit en raison d\'une déformation importante au cours de l\'analyse (non prise en compte ici), soit en raison des problèmes de maillage susmentionnés. Les jacobiens négatifs dans l\'atelier FEM de FreeCAD peuvent être signalés par Gmsh ou par CalculiX. Leurs emplacements dans le maillage sont mis en évidence lorsque les analyses CalculiX sont soumises en utilisant le bouton [Lancer les calculs du solveur](FEM_SolverRun/fr.md). Les conseils suivants peuvent aider à les éliminer :

-   Définir la propriété *Second Order Linear* du [maillage de Gmsh](FEM_MeshGmshFromShape/fr.md) à *true*, ceci a pour résultat que les nœuds du milieu des éléments de second ordre sont simplement ajoutés au milieu des bords droits (initialement) des éléments de premier ordre, sans les attacher à la géométrie et résout le problème dans la plupart des cas,
-   Utiliser Netgen au lieu de Gmsh. Netgen est connu pour être moins sujet aux problèmes de jacobiens négatifs mais ne les signale pas non plus, de sorte que l\'utilisateur ne peut s\'en rendre compte qu\'au moment de soumettre l\'analyse,
-   Réduire davantage la taille des éléments,
-   Exporter la géométrie, essayer de la mailler dans l\'interface graphique de Gmsh ou Netgen (NGSolve) ou dans un autre maillage autonome (comme Salome_Meca). Ces outils ont des fonctions supplémentaires qui peuvent aider à se débarrasser des jacobiens négatifs (par exemple, Gmsh a ce que l\'on appelle des \"outils d\'ordre élevé\"),
-   Utiliser des éléments de premier ordre. Cela ne doit être fait qu\'en dernier recours car les tétraèdres de premier ordre sont connus pour leur imprécision.

Indépendamment de ces conseils, il est important de souligner une fois de plus que les jacobiens négatifs sont généralement dus à des approches de modélisation désordonnées et à un manque de préparation de la géométrie pour l\'analyse (ce qui est particulièrement courant avec les modèles STEP téléchargés à partir de divers sites web). Même si le maillage est finalement généré dans de tels cas, les résultats risquent d\'être de mauvaise qualité (rappelons la règle GIGO mentionnée dans le premier paragraphe). Par conséquent, le nettoyage de la géométrie et la préparation pour la FEM devraient toujours être la priorité.



## Études sur la convergence des maillages 

Les études de convergence de maillage sont recommandées dans tous les projets sérieux nécessitant des résultats précis. En effet, les résultats peuvent changer considérablement et s\'approcher des valeurs correctes lorsque le maillage est affiné. L\'approche suivante doit être utilisée :

1.  Après avoir obtenu les premiers résultats et les avoir notés (généralement la contrainte de von Mises maximale, la contrainte de von Mises à un endroit donné et le déplacement maximal), affiner le maillage (globalement ou mieux localement avec [FEM Mailler plus finement](FEM_MeshRegion/fr.md)) et réexécuter la simulation.
2.  Vérifiez les résultats et notez leurs nouvelles valeurs. S\'ils diffèrent significativement des résultats initiaux, affinez encore le maillage et relancez l\'analyse.
3.  Répétez le processus si les résultats changent encore (généralement en augmentant) de manière significative avec l\'affinement du maillage.

Il est généralement utile de créer un graphique avec un résultat donné en fonction de la densité du maillage. De cette façon, il est plus facile de remarquer quand les résultats commencent à converger. La différence acceptable dans les résultats entre deux exécutions est généralement de l\'ordre de quelques pour cent (par exemple, moins de 5 %).

Dans certains cas, il peut arriver que la contrainte maximale augmente indéfiniment, quelle que soit la densité du maillage. Un tel effet non physique est connu sous le nom de singularité de contrainte. Il peut se produire pour les raisons suivantes

-   les forces concentrées appliquées aux modèles de solides et de coques,
-   conditions limites appliquées à des points (nœuds individuels),
-   angles vifs,
-   contact survenant dans un coin.

Les moyens typiques de traiter les singularités de contrainte sont les suivants :

-   appliquer des charges et des conditions aux limites à de petites zones plutôt qu\'à des points - voir la section sur le partitionnement ci-dessus,
-   ajouter de petits filets aux angles vifs (une exception à la règle qui consiste à omettre les petits filets lors de la simplification de la géométrie pour les éléments finis),
-   inclure la plasticité dans le comportement du matériau pour permettre la redistribution des contraintes et limiter les contraintes aux valeurs autorisées par la définition de la plasticité tout en observant le niveau approprié de déformation (déformation plastique),
-   ignorer les singularités et lire les contraintes loin d\'elles si possible (sur la base du principe de St. Venant).

<img alt="" src=images/FEM_mesh_convergence.PNG  style="width:400px;">



*Tracés de convergence de maillage typiques :<br>
- le déplacement ('''courbe verte''') converge rapidement,<br>
- la contrainte maximale au niveau d'une entaille comme un trou ('''courbe bleue''') nécessite davantage d'itérations de raffinement du maillage pour converger, <br>
- tandis que la contrainte maximale au niveau d'un angle aigu avec une condition limite fixe ('''courbe rouge''') ne converge pas du tout. Une singularité de contrainte se produit et un petit congé devrait être ajouté et la connexion devrait être modélisée de manière plus réaliste et plus flexible pour éviter ce comportement.<br>*


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Geometry Preparation and Meshing/fr
