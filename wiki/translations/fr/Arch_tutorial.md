# Arch tutorial/fr




{{TutorialInfo/fr
|Topic=Modélisation
|Level=Intermédiaire
|Author=[Yorik](User:Yorik.md)
|FCVersion=0.14
}}

![](images/Arch_tutorial_00.jpg )

## Introduction

Le but de ce tutoriel est de vous donner les bases pour travailler avec l\'atelier [Architecture](Arch_Workbench/fr.md). Je vais essayer d\'être le plus simple possible ainsi vous n\'avez pas besoin d\'expérience précédente avec FreeCAD, mais un peu d\'expérience avec la 3D ou des applications de modélisation de type [BIM](http://fr.wikipedia.org/wiki/Building_Information_Modeling) vous sera utile. Dans tous les cas vous devez vous préparer à faire des recherches plus approfondies sur le fonctionnement de FreeCAD dans la [documentation de FreeCAD](Main_Page/fr.md). La page [Premiers pas](Getting_started/fr.md) est à lire absolument si vous n\'avez jamais essayé FreeCAD. Parcourez aussi notre section [tutoriels](tutorials/fr.md) et sur [youtube](http://www.youtube.com/results?search_query=freecad) vous pouvez trouver plein d\'autres tutoriels vidéos.

Le but de l\'atelier [Arch](Arch_Workbench/fr.md) est d\'offrir une solution de travail complète de type [BIM](http://fr.wikipedia.org/wiki/Building_Information_Modeling) à l\'intérieur de FreeCAD. Comme il est toujours en développement ne vous attendez pas à retrouver les mêmes niveaux d\'outils que des solutions commerciales comme [Revit](http://fr.wikipedia.org/wiki/Revit) ou [ArchiCAD](http://fr.wikipedia.org/wiki/ArchiCAD) mais d\'un autre coté, FreeCAD étant employé dans une portée beaucoup plus grande que ces applications, l\'atelier [Arch](Arch_Workbench/fr.md) tire des bénéfices considérables des autres disciplines que FreeCAD possède, et offre quelques caractéristiques rarement vues dans des applications traditionnelles de BIM.

Voici, par exemple, quelques caractéristiques intéressantes de l\'atelier [Arch](Arch_Workbench/fr.md) de FreeCAD que vous trouverez difficilement dans d\'autres applications de type BIM :

-   Les objets architecturaux sont toujours des solides. Grâce au puissant passé mécanique de FreeCAD, nous avons appris l\'importance de toujours travailler avec les objets solides. Ceci assure un déroulement des opérations sans erreur, et des opérations booléennes très fiables. Comme la coupe des objets 3D avec un plan 2D, afin d\'extraire des sections, est également une opération booléenne, vous pouvez immédiatement voir l\'importance de ce point.

-   Les objets architecturaux peuvent avoir n\'importe quelle forme. Il n\'y a aucune restriction. Les murs n\'ont pas besoin d\'être verticaux, les dalles n\'ont pas besoin de ressembler à des dalles. N\'importe quel objet solide peut toujours devenir n\'importe quel objet architectural. Les choses très complexes, habituellement difficiles à définir dans d\'autres applications BIM, comme courber des dalles et devenir un mur (oui Zaha Hadid, c\'est de vous que nous parlons), ne présentent aucun problème particulier dans FreeCAD.

Toute la puissance de FreeCAD est à votre portée. Vous pouvez concevoir les objets architecturaux avec n\'importe quel autre outil de FreeCAD, tel que l\'atelier [Part Design](PartDesign_Workbench/fr.md), et quand ils sont prêts, les convertir en objets architecturaux. Ils conserveront toujours leur historique de modélisation, et restent totalement éditables. L\'atelier [Arch](Arch_Workbench/fr.md) hérite également d\'une grande partie des fonctionnalités de l\'[atelier Draft](Draft_Workbench/fr.md), comme [l\'aimantation](Draft_Snap/fr.md) et [le plan de travail](Draft_SelectPlane/fr.md).

-   L\'atelier [Arch](Arch_Workbench/fr.md) est très compatible avec l\'atelier [Mesh](Mesh_Workbench/fr.md). Vous pouvez facilement concevoir un modèle architectural dans une application basée sur des mailles comme [Blender](http://fr.wikipedia.org/wiki/Blender) ou [SketchUp](http://fr.wikipedia.org/wiki/Sketchup) et l\'importer dans FreeCAD. Si vous faites attention à la qualité de votre modèle et que ses objets sont bien des formes solides alors il vous suffira d\'un clic pour les transformer en objets architecturaux.

A l\'heure où j\'écris ceci l\'atelier [Arch](Arch_Workbench/fr.md) comme le reste de FreeCAD, souffre de quelques limitations. La plupart sont déjà en cours d\'étude et tendent à disparaître dans un futur proche.

-   FreeCAD n\'est pas une application 2D. Il est fait pour la 3D. Il y a suffisamment d\'outils pour dessiner et éditer des objets 2D avec les ateliers [Draft](Draft_Workbench/fr.md) et [Sketcher](Sketcher_Workbench/fr.md), mais ce n\'est pas fait pour traiter de très gros (et parfois très mal dessinés) fichiers 2D. Vous pouvez importer des fichiers 2D mais ne vous attendez pas à de grandes performances si vous souhaitez continuer à travailler dessus en 2D. Vous voilà prévenu.

-   Pas de support des matériaux. FreeCAD disposera d\'un système complet [Materiaux](Material/fr.md), capable de définir des matériaux très complexes, avec tous les avantages que vous pouvez attendre (propriétés personnalisées, familles de matériaux, représentation et propriétés d\'aspect visuel, etc.) et l\'atelier [Arch](Arch_Workbench/fr.md) va bien sûr l\'utiliser quand il sera prêt.

-   Support préliminaire de [IFC](http://fr.wikipedia.org/wiki/Industry_Foundation_Classes). Vous pouvez dès à présent [importer des fichiers IFC](Arch_IFC/fr.md), tout à fait sûrement, si [IfcOpenShell](http://ifcopenshell.org) est installé sur votre système, mais l\'exportation n\'est toujours pas officiellement supportée. Ceci est en cours de développement des deux côtés des promoteurs de FreeCAD et d\'IfcOpenShell, et à l\'avenir nous pouvons nous attendre à un support complet d\'IFC.

-   La plupart des outils Arch sont encore en développement. Cela signifie que les outils \"magiques\" qui créent des géométries complexes automatiquement, comme [Toiture](Arch_Roof/fr.md) ou [Escaliers](Arch_Stairs/fr.md) ne peuvent créer que certains types d\'objets, et que les outils qui ont des pré-réglages, comme [Arch\_Structure](Arch_Structure/fr.md) ou [Arch\_Window](Arch_Window/fr.md), n\'ont que quelques pré-réglages disponibles. Ceux ci devraient s'étoffer au fil du temps bien sûr.

-   [La relation entre les objets](Assembly_project/fr.md) dans FreeCAD n\'est toujours pas officiellement disponible. De ce fait, la relation entre une fenêtre et son mur hôte est implémentée dans l\'atelier [Arch](Arch_Workbench/fr.md) de manière temporaire (et parfois limitée). Beaucoup d\'autres possibilités devraient arriver quand la fonctionnalité sera pleinement disponible.

-   [Les unités](Units/fr.md) sont en cours d'implémentation dans FreeCAD, ce qui vous permettra de travailler avec n\'importe quelles unités que vous souhaitez (même les unités impériales, à ce sujet vous pouvez être éternellement reconnaissant envers Jürgen, le parrain et initiateur de FreeCAD). Mais pour le moment l\'atelier [Architecture](Arch_Workbench/fr.md) ne les supporte toujours pas. Vous devez le considérer « sans unités ».


{{Note|FreeCAD version 0.14 requis|Ce tutoriel a été réalisé avec [FreeCAD version 0.14](Release_notes_014/fr.md). Vous aurez besoin au moins de cette version pour le suivre. Les versions plus anciennes pourraient ne pas contenir tous les outils nécessaires ou certaines options risquent de ne pas être présentes.}}

## Déroulement type des opérations 

L\'atelier [Arch](Arch_Workbench/fr.md) est principalement fait pour deux sortes d'opérations :

-   Construire son modèle avec une application rapide, basée sur les maillages comme [Blender](http://fr.wikipedia.org/wiki/Blender) ou [SketchUp](http://fr.wikipedia.org/wiki/Sketchup), et l\'importer dans FreeCAD pour en extraire des plans et des coupes. FreeCAD est fait pour de la modélisation de précision, et même plus précis que ce qui est attendu dans la modélisation architecturale ; construire son modèle directement dans FreeCAD peut devenir lourd et lent. C\'est pour cette raison qu\'un tel déroulement d\'opérations prend un réel avantage. Il est décrit dans [cet article](http://betlibre.wood3dservices.fr/index.php?article21/atelier-architecture-de-freecad) sur le blog de RockN. Si vous prenez soin de modéliser correctement et précisément le projet (propre, avec des solides, des maillages non multiples), ce déroulement d\'opération vous donnera les mêmes performances et précisions que les autres programmes.

-   Construire son modèle directement dans FreeCAD. C\'est ce que je souhaite vous présenter dans ce tutoriel. Nous allons utiliser essentiellement trois ateliers : [Arch](Arch_Workbench/fr.md), bien sûr, mais aussi, l\'atelier [Draft](Draft_Workbench/fr.md), dont les outils sont directement intégrés à l\'atelier Architecture donc il n\'y a pas besoin de basculer d\'un atelier à l\'autre, et enfin l\'atelier [Sketcher](Sketcher_Workbench/fr.md). De façon pratique, vous pouvez faire comme je le fais habituellement, c\'est-à-dire créer une barre d\'outils personnalisée dans votre atelier Arch, avec Outils → Personnaliser, et ajouter les outils du sketcher que vous utilisez souvent. Voici mon banc de travail Arch \"personnalisé\" :

![](images/Arch_tutorial_01.jpg )

Dans ce tutoriel, nous allons modéliser le bâtiment en 3D à partir de plans 2D que nous avons téléchargés sur le net, dont nous allons extraire des éléments 2D comme des vues en plans, des coupes ou des élévations.

## Préparation

Au lieu de créer un projet à partir de zéro, prenons un exemple de projet à modéliser, cela nous économisera du temps. J\'ai choisi ce magnifique bâtiment d\'un architecte réputé,[Vilanova Artigas](http://en.wikipedia.org/wiki/Jo%C3%A3o_Batista_Vilanova_Artigas) (voir une série de [photos](http://www.leonardofinotti.com/projects/architects-second-house/image/40409-130405-010d) par Leonardo Finotti), parce qu\'il est près de là où j\'habite, c\'est un magnifique exemple d\'architecture moderne et originale de Sao Paulo, et les fichiers DWG sont [facilement disponibles](http://www.bibliocad.com/library/second-house-vilanova-artigas_72926#).

Nous utiliserons les dessins 2D DWG obtenus à partir du lien ci-dessus (vous devez vous inscrire sur le site ci-dessus pour le télécharger, mais c\'est gratuit, ou prenez directement une version DXF [ici](http://yorik.uncreated.net/archive/scripts/artigas.dxf)) comme base pour construire notre modèle. La première chose à faire est donc de télécharger le fichier, de le décompresser et d\'ouvrir le fichier DWG à l\'intérieur avec une application DWG telle que [DraftSight](http://www.3ds.com/products-services/draftsight/overview/). Vous pouvez également le convertir au format DXF à l\'aide d\'un utilitaire gratuit tel que le [Convertisseur de fichiers ODA](https://www.opendesign.com/guestfiles/oda_file_converter). Si vous avez installé le convertisseur ODA (et son chemin d\'accès défini dans les paramètres de préférences Arch), FreeCAD est également [ capable d\'importer directement des fichiers DWG](Draft_DXF.md). Comme ces fichiers peuvent parfois être de mauvaise qualité et très lourds, il est généralement préférable de les ouvrir au préalable avec une application de CAO 2D et d\'y faire le ménage.

Ici, j\'ai, enlevé tous les dessins de détails, les blocs de texte et les calques, fait un \"nettoyage\" (\"purge\" dans AutoCAD) pour enlever toutes les entités inutilisées, réorganiser les sections dans une position logique dans la vue en plan, et déplacé le tout au point (0,0). Après ça, notre fichier peut être ouvert proprement avec FreeCAD. Regardez les différentes options disponibles dans Édition → Préférences → Draft → Import/Export, elles peuvent affecter comment (et à quelle vitesse) les DXF/DWG sont importés.

Voici comment le fichier s\'affiche lorsqu'il est ouvert dans FreeCAD. J\'ai aussi changé l\'épaisseur des murs (le contenu du groupe \"muros\") et j\'ai inversé quelque portes qui ont été importées avec une mauvaise échelle selon X, avec l\'outil [Draft Scale](Draft_Scale/fr.md) :

![](images/Arch_tutorial_02.jpg )

[L\'importateur de DXF](Draft_DXF.md) (qui prend aussi en compte les fichiers DWG en les convertissant tout simplement en DXF), groupe les objets importés par calque. Il n\'y a pas de calques dans FreeCAD mais il y a des [groupes](Std_Group/fr.md). Les [groupes](Std_Group/fr.md) offrent un comportement similaire aux calques pour organiser les objets du fichier, mais ils n\'ont pas de propriété spécifique, comme les calques dans AutoCAD qui s\'appliquent à leur contenu. Ils peuvent être imbriqués les uns dans les autres par simple glisser-déposer de la souris. La première chose que vous pourriez faire, c\'est de créer des nouveaux [groupes](Std_Group/fr.md) (dans la [vue arborescente](Document_structure/fr.md) : clic droit sur l\'icône du document, créer un groupe, clic droit dessus, et le renommer en \"plans 2d de base\"). Sélectionnez tous les objets et glissez les dans ce nouveau groupe.

## Construire les murs 

Comme la plupart des objets de l\'[Atelier Arch](Arch_Workbench/fr.md), les [murs](Arch_Wall/fr.md) peuvent être fabriqués à partir d\'une grande variété d\'autres objets : [lignes](Draft_Line/fr.md), [polylignes](Draft_Wire/fr.md), [Sketcher](Sketcher_Workbench/fr.md), faces ou solides (et même à partir de rien ; dans ce cas ils sont définis par leur hauteur, largeur et longueur). La géométrie résultante du mur dépend de la géométrie de l\'objet de base, et des propriétés que vous complétez comme l\'épaisseur ou la hauteur. Comme vous pourriez le deviner, un mur basé sur une ligne emploiera cette ligne en tant que sa ligne d\'alignement, alors qu\'un mur basé sur une face emploiera cette face en tant que son empreinte de base, et un mur basé sur un solide adoptera simplement la forme de ce solide. Ceci permet à n\'importe quelle forme imaginable de devenir un mur.

Il y a plusieurs stratégies possibles pour créer les murs dans FreeCAD. Une possibilité est de créer un étage complet avec le [sketcher](Sketcher_Workbench/fr.md), puis d\'en faire un seul et énorme mur. Cette technique fonctionne mais n\'autorise qu\'une seule épaisseur de mur pour tout l\'étage. Vous pouvez aussi fabriquer une ligne pour chaque pan de mur. Enfin on peut aussi, et c\'est ce que nous allons utiliser ici, faire un mix des deux : Nous allons créer quelques [polylignes](Draft_Wire/fr.md) par dessus les plans importés, un pour chaque type de mur.

![](images/Arch_tutorial_03.jpg )

Comme vous pouvez le voir, j\'ai dessiné en rouge les lignes qui vont devenir les murs en béton (une [recherche d\'images](http://www.google.com/search?tbm=isch&q=casa+artigas+brooklin) de la maison peut vous aider à cerner ses différents types de murs), ceux en vert correspondent aux murs extérieurs en briques et ceux en bleu sont les parois intérieures. Les lignes passent à travers les portes elles seront insérées par la suite et l\'ouverture se fera automatiquement. Les murs peuvent aussi être alignés à gauche, à droite ou au centre de la ligne de base, donc il n\'y a pas d\'importance à dessiner la ligne de base d\'un coté ou de l\'autre. J\'ai aussi pris soin d\'éviter les croisements autant que possible, car notre modèle sera plus précis de cette manière. Mais on s\'occupera des intersections plus tard.

Quand c\'est fait, placez toutes ces lignes dans un nouveau [groupe](Group/fr.md) si vous le souhaitez, sélectionnez chacune de ces lignes une par une, et sélectionnez l\'outil [Arch Mur](Arch_Wall/fr.md) pour construire un mur pour chaque ligne. Vous pouvez aussi sélectionner toutes les lignes à la fois. Après ça, et après avoir corrigé l\'épaisseur (les murs extérieurs mesurent 25 cm d\'épaisseur et les murs intérieurs 15 cm) et quelques alignements, nos murs sont prêts :

![](images/Arch_tutorial_04.jpg )

Nous pourrions aussi avoir à construire nos murs à partir de zéro. Si vous appuyez sur le bouton [Arch Mur](Arch_Wall/fr.md) sans avoir sélectionné d\'objet, vous serez en mesure de cliquer sur deux points de l\'écran pour tracer un mur. L\'outil mur tracera en réalité une ligne puis construira un mur sur celle-ci. J\'ai trouvé plus didactique de vous montrer comment les choses fonctionnent.

Avez-vous remarqué que j\'ai pris grand soin d\'empêcher les murs de se croiser ? Cela nous évitera des maux de tête par la suite, par exemple si nous exportons notre travail vers d\'autres applications, qui pourraient ne pas aimer ça. J\'ai seulement une intersection, où j\'étais trop paresseux pour dessiner deux petits segments de lignes, et ai dessiné une grande ligne traversant une autre. Ceci doit être corrigé. Heureusement, tous les objets Arch ont une super fonctionnalité : ils peuvent être ajoutés les uns aux autres. Cette action a pour effet d\'unir leurs géométries, mais ils resteront toujours modifiables séparément par la suite. Pour ajouter un de nos murs traversant à l\'autre, il suffit d\'en sélectionner un, puis de sélectionner l\'autre en maintenant **CTRL**, puis d\'appuyer sur l\'outil [Ajouter](Arch_Add/fr.md) :

![](images/Arch_tutorial_05.jpg )

Sur la gauche il y a deux murs qui se croisent. Sur la droite, le résultat après avoir ajouté l\'un à l\'autre.


{{Note | Une remarque importante sur les objets paramétriques|Il y a quelque chose d' important à prendre en considération. Comme vous pouvez le voir, dans FreeCAD, tout est paramétrique : Notre nouveau mur "uni" est constitué de deux parois, chacune basée sur une base de référence. Lorsque vous les développez dans l'[arborescence](Document_structure/fr.md), vous pouvez voir toute la chaîne de dépendances. Comme vous pouvez l'imaginer, ce petit jeu peut rapidement devenir très complexe. En outre, si vous savez déjà comment travailler avec l'atelier [Sketcher](Sketcher_Workbench/fr.md), vous pourriez avoir voulu dessiner les lignes de base avec des esquisses contraintes. Cette complexité a un coût : elle augmente de façon exponentielle le nombre de calculs que FreeCAD doit effectuer pour maintenir la géométrie de votre modèle à jour. Alors, pensez-y, n'ajoutez pas inutilement de la complexité lorsque ce n'est pas nécessaire. Gardez un bon équilibre entre les objets simples et complexes, et gardez ces derniers pour les cas où vous en avez vraiment besoin.}}

Par exemple, je pourrais avoir dessiné toutes mes lignes de base sans me soucier de ce qui traverse quoi, et arranger les choses avec l\'outil [ Ajouter](Arch_Add/fr.md) par la suite. Mais de cette manière, j\'augmente grandement la complexité de mon modèle, sans en tirer le moindre avantage. Il vaut mieux faire les choses correctement dès le début, et garder chaque pièce géométrique aussi simple que possible.

Maintenant que nos murs sont bons, nous devons élever leur hauteur, jusqu\'à ce qu\'ils croisent le toit. Ensuite, puisque l\'objet paroi ne peut toujours pas être coupé automatiquement par les toits (cela se produira un jour) nous allons construire un objet \"factice\", qui suit la forme du toit, pour le soustraire de nos murs.

Tout d\'abord, en regardant nos dessins 2D, nous pouvons voir que le point plus haut du toit est 5.6m au-dessus du sol. Donc, nous allons donner à tous nos murs une hauteur de 6m, ainsi nous nous assurons qu\'ils seront réduits par notre volume de toit factice. Pourquoi 6m et non 5,6, me demanderez-vous? Eh bien, si vous avez déjà travaillé avec des opérations booléennes (additions, soustractions, intersections), vous devez déjà savoir que ces opérations n\'aiment généralement pas beaucoup les situations de coïncidence \"face-sur-face\". Ils préfèrent nettement des objets qui se coupent franchement. De cette manière, nous assurons des opérations aussi sûres que possible.

Pour augmenter la hauteur de nos murs, il suffit de tous les sélectionner (n\'oubliez pas celui que nous avons ajouté à l\'autre) dans l\'arborescence, et modifiez la valeur de leur propriété \'height\' (hauteur).

Avant de faire notre toit et de couper les murs, nous allons faire les objets restants qui devront être coupés : Les murs du studio du haut, et les colonnes. Les murs du studio sont faits de la même façon que nous l\'avons fait, sur le plan de l\'étage supérieur, mais ils seront élevés à partir de l\'altitude 2,6 m. Nous allons donc leur donner la hauteur nécessaire de sorte que leur sommet atteigne 6m, il faut rajouter 3,4 m. Une fois cela fait, hissons nos murs à 2.6m du sol : Sélectionnez les deux murs, mettez-vous en vue frontale (Affichage → Vues standard → avant), appuyez sur le bouton [Déplacer](Draft_Move/fr.md) , sélectionner un premier point, puis entrez 0, 2.6, 0 comme coordonnées, et appuyez sur Entrée. Vos objets ont maintenant sauté à 2,6 m de haut :

![](images/Arch_tutorial_06.jpg )


{{Note|À propos de coordonnées|Les objets [Draft](Draft_Workbench/fr.md) , et la plupart des objets [Arch ](Arch_Workbench/fr.md) aussi, obéissent à un système de Draft appelé [plans de travail](Draft_SelectPlane/fr.md). Ce système définit un plan 2D où les prochaines opérations auront lieu. Si vous ne le spécifiez pas, ce plan de travail s'adapte à la vue actuelle. C'est pourquoi nous sommes passés en vue frontale, et vous voyez que nous avons indiqué un mouvement en X de 0 et en Y de 2,6. Nous aurions aussi pu forcer le plan de travail à rester sur le terrain, en utilisant l'outil [Plans de travail](Draft_SelectPlane/fr.md). Ensuite, nous aurions entré  un déplacement en X de 0, en Y de 0 et en  Z de 2,6. }}

.

Maintenant déplaçons nos murs horizontalement, à leur emplacement correct. Puisque que nous avons des points d\'ancrage c\'est plus facile : Sélectionnez les deux murs, appuyez sur l\'outil [Déplacer](Draft_Move/fr.md), et déplacez-les d\'un point à l\'autre :

![](images/Arch_tutorial_07.jpg )

Enfin, j\' ai changé la couleur de certains murs pour une couleur brique (c\'est tellement plus facile de faire la différence), et j\'ai fait une petite correction : Certains murs ne vont pas jusqu\'au toit, mais s\'arrêtent à une hauteur de 2,60 m. J\'ai corrigé la hauteur de ces murs.

## Elever la structure 

Maintenant, puisque nous devons réduire nos murs avec un volume à soustraire, nous devrions aussi bien vérifier si il n\'y a pas d\'autres objets qui devront être coupés de cette façon. Il existe certaines colonnes. C\'est une bonne occasion de présenter un second objet arch : l[Arch Structure](Arch_Structure/fr.md). Les objets Structure se comportent plus ou moins comme les murs, mais ils ne sont pas faits pour suivre une ligne de base. Au contraire, ils préfèrent travailler à partir d\'un profil, qui est extrudé (le long d\'une ligne de profil ou non). Tout objet plat peut être un profil pour une structure, avec une seule exigence : ils doivent former une forme fermée.

Pour nos colonnes, nous allons utiliser une autre stratégie qu\'avec les murs. Au lieu de \"dessins\" au-dessus du plan 2D, nous allons utiliser directement les objets de celles-ci : les cercles représentent les colonnes dans la vue en plan. En théorie, nous pourrions simplement sélectionner l\'un d\'eux, et appuyez sur le bouton [Arch Structure](Arch_Structure/fr.md). Cependant, si nous faisons cela, nous produisons un objet structurel \"vide\". C\'est parce que vous ne pouvez jamais être trop sûr de savoir comment des objets sont dessinés dans le fichier DWG, et souvent ce ne sont pas des formes fermées. Donc, avant de les transformer en colonnes réelles, nous allons les transformer en surfaces, en utilisant l\'outil [Mise à niveau](Draft_Upgrade/fr.md) deux fois sur les cercles. La première fois pour les convertir en fils fermés (polylignes), la deuxième fois pour convertir ces fils en surfaces. Cette deuxième étape n\'est pas obligatoire, mais, si vous avez une surface, vous êtes sûr à 100% qu\'elle est fermée (sinon une surface ne peut pas être faite).

Après avoir converti nos colonnes en surfaces, nous pouvons utiliser l\'outil [Arch Structure](Arch_Structure/fr.md) sur elles, et régler la hauteur (certaines ont 6m, d\'autres seulement 2.25m de haut) :

![](images/Arch_tutorial_08.jpg )

Sur l\'image ci-dessus, vous pouvez voir deux colonnes qui sont encore telles qu\'elles se trouvaient dans le fichier DWG, deux qui ont été mises à niveau sur des faces, et deux qui ont été transformées en objets structurels et leur hauteur réglée à 6m et 2.25m.

Notez que les différents objets Arch (les murs, les structures et tous les autres objets que nous allons découvrir) partagent tous beaucoup de choses entre eux (par exemple tous peuvent être ajoutés l\'un à l\'autre, comme nous l\'avons vu avec des murs, et chacun d\'eux peut être converti en un autre type). Donc, ce n\'est plus une question de goût, nous aurions pu aussi faire nos colonnes avec l\'outil Mur, et les convertir si nécessaire. En fait, certains de nos murs sont des murs de béton, nous pourrions voulons les convertir en structures plus tard.

## Soustractions

Maintenant, il est temps de construire notre volume à soustraire. Le moyen le plus facile sera d\'élaborer son profil par dessus la vue en coupe. Ensuite, nous allons le faire pivoter et le placer à sa position correcte. Vous voyez pourquoi j\'ai placé les coupes et élévations comme ça avant de commencer ? Ce sera très facile de dessiner cet élément à cet endroit, puis de le déplacer à sa position correcte sur le modèle.

Dessinons un volume, plus grand que le toit, qui sera soustrait de nos murs. Pour ce faire, j\'ai dessiné deux lignes sur le dessus de la base du toit, puis je les ai étendues un peu avec l\'outil [Draft Trimex](Draft_Trimex/fr.md). Puis, j\'ai dessiné un [fil (wire)](Draft_Wire/fr.md), en cliquant sur ces lignes, et en allant bien au-dessus de nos six mètres. J\'ai aussi dessiné une ligne bleue au niveau du sol (0.00), qui sera l\'axe de rotation.

<img alt="" src=images/Arch_tutorial_09.jpg  style="width:1024px;">

Maintenant, c\'est la partie difficile : Nous allons utiliser l\'outil [Draft Rotation](Draft_Rotate/fr.md) pour faire tourner notre profil de 90 degrés dans la bonne position pour être extrudé. Pour ce faire, nous devons d\'abord changer le [Plan de travail](Draft_SelectPlane/fr.md) pour le plan YZ. Une fois cela fait, la rotation va se passer dans ce plan. Mais si nous faisons comme nous l\'avons fait un peu plus tôt, et fixons notre point de vue sur la vue latérale, il sera difficile de voir et de sélectionner notre profil et de savoir où est le point de base autour duquel il doit tourner, n\'est-ce pas ? Alors, nous devons régler manuellement le plan de travail : Appuyez sur le bouton [Plan de travail](Draft_SelectPlane/fr.md) (il est dans l\'onglet \"tâches\" de l\'arborescence), et mettez-le à YZ (qui est le plan «de côté»). Une fois que vous avez défini le plan de travail à la main, comme ça, il ne sera pas changé en fonction de votre point de vue. Vous pouvez maintenant orienter la direction d\'observation jusqu\'à ce que vous ayez une bonne perception de toutes les choses que vous devez sélectionner. Pour passer le plan de travail de nouveau en mode \"automatique\" plus tard, appuyez à nouveau sur la touche [Plan de travail](Draft_SelectPlane/fr.md) et et réglez-le sur \"None\".

Maintenant, la rotation sera facile à faire : Sélectionnez le profil, appuyez sur le bouton [Draft Rotation](Draft_Rotate/fr.md) , cliquez sur un point de la ligne bleue, entrez 0 comme angle de départ (start Angle), et 90 comme rotation :

<img alt="" src=images/Arch_tutorial_10.jpg  style="width:1024px;">

Maintenant, tout ce que nous devons faire est de déplacer le profil un peu plus près du modèle (définir le plan de travail XY si nécessaire), et de l\'extruder. Cela peut être fait soit avec l\'outil [Part Extrude](Part_Extrude/fr.md), ou [Draft Trimex](Draft_Trimex/fr.md), c\'est à dire qui a le pouvoir caché pour extruder les surfaces. Assurez-vous que l\'extrusion est plus grande que tous les murs dont il sera soustrait, pour éviter des situations de coïncidence face-sur-face :

<img alt="" src=images/Arch_tutorial_11.jpg  style="width:1024px;">

Maintenant, vient l\' action contraire de l\'outil [Arch Ajouter](Arch_Add/fr.md): [Supprimer](Arch_Remove/fr.md). Comme vous l\'aurez deviné, cela rend également un objet un enfant de l\'autre, mais sa forme est soustraite de l\'objet hôte, au lieu d\'être unie. Donc, maintenant, les choses sont simples : Sélectionnez le volume à soustraire (je l\'ai renommé \"Roof volume to subtract\" (Volume de toit à soustraire) dans l\'arborescence afin qu\'il soit facile à repérer), CTRL + sélectionnez un mur et appuyez sur le bouton [Arch Supprimer](Arch_Remove/fr.md) . Vous verrez qu\'après la soustraction, le volume à soustraire a disparu à la fois de la vue 3D et de l\'arborescence. C\'est parce qu\'il a été marqué comme enfant du mur, et \"avalé\" par ce mur. Sélectionnez le mur, développez-le dans l\'arborescence, il y a notre volume.

Maintenant, sélectionnez le volume dans l\'arborescence, CTRL + sélectionnez le mur suivant, appuyez sur [Supprimer](Arch_Remove/fr.md). Répétez l\'opération pour les prochains murs jusqu\'à ce que vous ayez tout coupé correctement :

<img alt="" src=images/Arch_tutorial_12.jpg  style="width:1024px;">

Rappelez-vous que pour les deux outils [Ajouter](Arch_Add/fr.md) et [ Supprimer](Arch_Remove/fr.md), l\'ordre de sélection des objets est important. L\'hôte est toujours le dernier, comme dans \"Supprimer X de Y\" ou \"Ajouter X à Y\".


{{Note | Une note sur les additions et soustractions | 
Les objets Arch qui  supportent additions et soustractions (tous exceptés les objets d'aides "visuels" : tels que les axes) gardent la trace des objets en ayant deux propriétés respectivement, "Additions", et "Soustractions", qui contiennent une liste de liens pour ajouter ou soustraire d'autres objets . Un objet commun peut être dans la liste de plusieurs autres objets, comme c'est le cas de notre volume de soustraction ici. Chacun des pères voudra l'avaler dans l'arborescence, cependant, il sera généralement "vivant" en dernier. Mais vous pouvez toujours modifier ces listes pour tout objet, en double-cliquant dessus dans l'arborescence, quand FreeCAD est en mode d'édition. Appuyez sur la touche Échappement pour sortir du mode édition.}}

## Faire les toits 

Maintenant, tout ce que nous avons à faire pour compléter la structure, c\'est de faire le toit et les petites dalles intérieures. Encore une fois, le plus simple est de dessiner leurs profils par dessus la section, avec l\'outil [Filaire](Draft_Wire/fr.md). Ici j\'ai dessiné trois profils les uns sur les autres (je les ai écartés dans l\'image ci-dessous pour mieux les voir). Le vert sera utilisé pour les bords latéraux de la dalle du toit, puis le bleu pour les parties latérales, et les rouges pour la partie centrale, qui se trouve au-dessus du bloc de la salle de bain :

<img alt="" src=images/Arch_tutorial_13.jpg  style="width:1024px;">

Ensuite, il faut répéter l\'opération de rotation ci-dessus, pour faire pivoter les objets dans une position verticale, puis les déplacer aux endroits appropriés, et copier certains d\'entre eux qui devront être extrudés à deux reprises, avec l\' outil [Déplacer](Draft_Move/fr.md), avec la touche ALT enfoncée, qui crée des copies au lieu de déplacer l\'objet réel. J\'ai également ajouté deux autres profils pour les parois latérales de l\'ouverture de la salle de bains.

<img alt="" src=images/Arch_tutorial_14.jpg  style="width:1024px;">

Lorsque tout est en place, il suffit d\'utiliser l\'outil [Draft Trimex](Draft_Trimex/fr.md) pour extruder les profils, puis de convertir les résultats en objets [Arch Structure](Arch_Structure/fr.md).

<img alt="" src=images/Arch_tutorial_15.jpg  style="width:1024px;">

Après cela, nous pouvons voir certains problèmes qui se posent : deux des colonnes de droite sont trop courtes (elles devraient atteindre le toit), et il y a un écart entre la dalle et les murs du studio à l\'extrême droite (le symbole de niveau 2,60 sur la vue en coupe était évidemment faux). Merci aux objets paramétriques, tout cela est très facile à résoudre : Pour les colonnes, il faut juste changer leur hauteur à 6m, aller chercher votre volume de toit à soustraire dans l\'arborescence, et le soustraire aux colonnes. Pour les murs, c\' est encore plus facile : les déplacer un peu vers le bas. Comme le volume de soustraction continue au même endroit, la géométrie de la paroi s\'adapte automatiquement.

Maintenant une dernière chose doit être résolue, il y a une petite dalle dans la salle de bains, qui coupe certains murs. Réparons cela en créant un nouveau volume de soustraction, et en le soustrayant de ces murs. Une autre caractéristique de l\'outil [Draft Trimex](Draft_Trimex/fr.md), que nous utilisons pour extruder des profils, est qu\'il peut également extruder une seule face d\'un objet existant. Cela crée un nouvel objet séparé, il n\'y a donc aucun risque de «dommage» pour l\'autre objet. Donc, nous pouvons sélectionner la face de base de la petite dalle (regarder par-dessous le modèle, vous la verrez), puis appuyer sur le bouton [Draft Trimex](Draft_Trimex/fr.md) et l\'extruder bien au-dessus des toits. Ensuite, la soustraire des deux murs intérieurs de la salle de bains avec l\'outil [Supprimer](Arch_Remove/fr.md) :

<img alt="" src=images/Arch_tutorial_16.jpg  style="width:1024px;">

## Planchers, Escaliers et Cheminée, 

Maintenant, notre structure est complète, nous avons juste quelques petits objets à faire.

### la cheminée 

Commençons par la cheminée. Maintenant, vous savez déjà comment cela fonctionne, non ? Dessinez des [Draft Filaires ](Draft_Wire/fr.md) fermés, déplacez-les vers le haut à leur hauteur correcte avec l\'outil [Déplacer](Draft_Move/fr.md), extrudez-les avec l\'outil [Draft Trimex](Draft_Trimex/fr.md) , convertissez le plus gros en [Arch Structure](Arch_Structure/fr.md), et soustrayez les plus petits. Remarquez le tube de cheminée qui n\'était pas dessiné sur la vue en plan, mais j\' ai trouvé sa position en faisant glisser les lignes bleues à partir des vues en coupe.

<img alt="" src=images/Arch_tutorial_17.jpg  style="width:1024px;">

### les planchers 

Les planchers ne sont pas bien représentés dans les dessins de base. Lorsque l\'on regarde les sections, on ne peut pas connaître l\'emplacement ni l\'épaisseur des dalles de plancher. Je vais donc supposer que les murs sont assis sur le dessus des blocs de fondation, au niveau 0,00, et que là se trouvent les dalles du plancher, posées sur ces blocs, de 15cms d\'épaisseur. Ainsi, les dalles de plancher ne s\'exécutent pas sous les parois, mais autour d\'elles. Nous pourrions le faire en créant une grande dalle rectangulaire puis en soustrayant les murs, mais n\' oubliez pas, les opérations de soustraction nous coûtent. Il vaut mieux procéder par petits morceaux, ce sera \"moins gourmand\" en termes de calcul, et donc, si nous le faisons intelligemment, pièce par pièce, ceci sera également utile pour calculer les surfaces au sol plus tard :

<img alt="" src=images/Arch_tutorial_18.jpg  style="width:1024px;">

Une fois les fils dessinés, il suffit de les transformer en [Arch structures](Arch_Structure/fr.md), et de leur donner une hauteur de 0.15 :

<img alt="" src=images/Arch_tutorial_19.jpg  style="width:1024px;">

### Les Escaliers 

Maintenant les escaliers. Faisons connaissance avec le prochain outil Arch, les [Escaliers](Arch_Stairs/fr.md). Cet outil est encore à un stade très précoce de développement, au moment où j\' écris, donc n\'en attendez pas trop de lui. Mais il est déjà très utile pour faire des escaliers simples, droits. Un concept important à savoir : l\'outil escalier est pensé pour construire un escalier à partir d\'un plancher plat jusqu\'à un mur. En d\'autres termes, vu de haut, l\'objet escaliers occupe exactement l\'espace qu\'il occupe sur la vue en plan, de sorte que la dernière contre-marche n\'est pas dessinée (mais elle est bien sûr prise en compte dans le calcul des hauteurs).

Dans ce cas, j\'ai préféré construire les escaliers sur la vue en coupe, parce que nous aurons besoin de nombreuses mesures qui sont plus faciles à obtenir à partir de ce point de vue. Ici, j\'ai dessiné quelques lignes directrices rouges, puis deux lignes bleues qui seront la base de nos deux pièces d\'escaliers, et deux fils vert fermés, qui formeront les parties manquantes. Maintenant, sélectionnez la première ligne bleue, appuyez sur l\'outil [Escaliers](Arch_Stairs/fr.md), définissez le nombre de marches à 5, la hauteur à 0,875, la largeur à 1,30, le type de structure à \"massive\" et l\'épaisseur de la structure à 0,12. Répétez l\'opération pour l\'autre pièce.

Enfin, extrudez les deux fils verts de 1.30, puis tournez-les et déplacez-les à la bonne position :

<img alt="" src=images/Arch_tutorial_20.jpg  style="width:1024px;">

Sur la vue en élévation, dessinez (puis tournez) la bordure :

<img alt="" src=images/Arch_tutorial_21.jpg  style="width:1024px;">

Puis remettez tout en place :

<img alt="" src=images/Arch_tutorial_22.jpg  style="width:1024px;">

N\'oubliez pas également de couper la colonne qui traverse les escaliers, parce que dans BIM c\'est toujours mauvais d\'avoir des objets qui se croisent. Nous construisons comme dans le monde réel, ne l\'oubliez pas, où les objets solides ne peuvent pas se croiser. Ici, je ne voulais pas soustraire la colonne directement à partir de l\'escalier (sinon l\'objet colonne serait avalé par les objets escaliers dans l\'arborescence, et je n\'aimais pas ça), j\'ai donc pris la face sur laquelle la colonne a été construite, et extrudé à nouveau. Cette nouvelle extrusion a été ensuite soustraite de l\'escalier.

Bien ! Tout le travail dur est désormais fait, allons-y avec le travail très dur!

## Portes et fenêtres 

[Arch Fenêtres](Arch_Window/fr.md) sont des objets très complexes. Ils sont utilisés pour fabriquer toutes sortes d\'objets \"insérés\", tels que des fenêtres ou des portes. Oui, dans FreeCAD, les portes sont juste un type spécial de fenêtre, en réalité aussi, non? L\'outil [Fenêtre](Arch_Window/fr.md) peut être encore un peu difficile à utiliser aujourd\'hui, mais considérez cela comme un compromis, car il a été construit pour une puissance maximale. Presque n\'importe quel type de fenêtre sortie de votre imagination peut être produit avec lui. Mais comme l\'outil va s\'enrichir de plus de pré-configurations, cette situation devrait certainement s\'améliorer à l\'avenir.

L\'objet [Arch Fenêtre](Arch_Window/fr.md) fonctionne comme ceci : Il est basé sur un modèle 2D, n\'importe quel objet 2D, mais de préférence une [esquisse](Sketcher_Workbench/fr.md), qui contient des filaires fermés (polylignes). Ces fils définissent les différentes parties de la fenêtre : cadres extérieurs, cadres intérieurs, panneaux de verre, panneaux solides, etc. L\'objet fenêtre a alors une propriété qui stocke quoi faire avec chacun de ces filaires : extruder, placer à un certain décalage, etc. Enfin, une fenêtre peut être insérée dans un objet hôte comme un mur ou une structure, et il va automatiquement créer un trou dedans. Ce trou sera calculé par extrusion du plus grand fil figurant dans le modèle 2D.

Il y a deux façons de créer ces objets dans FreeCAD : en utilisant une pré-configuration, ou en dessinant la fenêtre à partir de zéro. Nous allons voir ici les deux méthodes. Mais rappelez-vous que la méthode avec pré-configuration ne fait rien d\'autre que la création de la mise en page de l\'objet et la définition des extrusions nécessaires pour vous.

### Utilisation des pré-configurations 

En appuyant sur l\'outil [Arch Fenêtre](Arch_Window/fr.md) sans objet sélectionné, vous êtes invités, soit à choisir un tracé 2D, soit à utiliser l\'une des pré-configurations. Nous allons utiliser la pré-configuration «Porte simple\" pour placer la porte d\'entrée principale de notre modèle. Donnez-lui une largeur de 1 m, une hauteur de 2,45 m, une taille de 0,15 m de W1, et laissez les autres paramètres à 0.05m. Puis cliquez sur le coin inférieur gauche de la paroi, et votre nouvelle porte est créée :

<img alt="" src=images/Arch_tutorial_23.jpg  style="width:1024px;">

Vous remarquerez que votre nouvelle porte n\'apparaît pas dans l\'arborescence. C\'est parce que, par l\'accrochage à un mur, nous avons indiqué quel mur est l\'objet hôte. Par conséquent, elle a été \"avalée\" par la paroi. Mais un clic droit sur elle → Aller à la sélection qui se trouve dans l\'arbre la révèle.

Dans ce cas, comme notre fenêtre n\'est pas insérée dans n\'importe quel mur (l\'ouverture était déjà là), nous pourrions aussi bien détacher notre fenêtre de son mur hôte. Ceci est fait en double-cliquant sur le mur hôte dans l\'arborescence pour entrer dans son mode d\'édition. Là, vous verrez la fenêtre dans son groupe \"soustractions\". Il suffit de sélectionner la fenêtre, appuyez sur le bouton \"supprimer l\'élément\", puis \"OK\". Notre fenêtre a été retirée de son mur hôte, et se trouve maintenant au bas de l\'arborescence.

Nous avons une deuxième porte, exactement la même que celle-ci, un peu sur la gauche. Au lieu de créer une nouvelle porte à partir de zéro, nous avons deux façons de faire une copie de la précédente : En utilisant l\'outil [Draft Déplacer](Draft_Move/fr.md), avec la touche ALT enfoncée, qui, comme vous le savez déjà, copie un objet au lieu de le déplacer. Ou, mieux encore, nous pouvons utiliser l\'outil [Draft Clone](Draft_Clone/fr.md) . L\'outil clone produit un \"clone\" d\'un objet sélectionné, que vous pouvez déplacer, mais qui conserve la forme de l\'objet original. Si l\'objet d\'origine change, le clone change aussi.

Donc, tout ce que nous devons faire maintenant est de sélectionner la porte, appuyer sur l\'outil [Draft Clone](Draft_Clone/fr.md) , puis déplacer le clone à sa position correcte avec l\'outil [Déplacer](Draft_Move/fr.md).

### Organiser votre modèle 

<img alt="" src=images/Arch_tutorial_24.jpg  style="width:400px;">

Maintenant il serait judicieux de faire un peu de ménage. Puisque nous avons déjà deux fenêtres, c\'est le bon moment pour faire un peu de nettoyage dans l\'arborescence : Créez un nouveau [groupe](Std_Group/fr.md), renommez le en \"fenêtres\", et déposez les deux fenêtres dans ce groupe. Je recommande aussi de séparer d\'autres éléments de cette façon, comme les murs et les structures. Puisque vous pouvez également créer des [groupes](Std_Group/fr.md) à l\'intérieur des groupes, vous pouvez organiser plus tard, par exemple en plaçant tous les éléments qui forment le toit dans un groupe distinct, il est alors facile de le montrer ou le cacher (basculer un groupe visible ou invisible fait la même chose avec tous les objets à l\'intérieur).

L\'[Atelier Arch](Arch_Workbench/fr.md) dispose de quelques outils supplémentaires pour organiser votre modèle : le [Site](Arch_Site/fr.md), [Bâtiment](Arch_Building/fr.md) et l\'[Étage\|](Arch_Floor/fr.md). Ces trois objets sont basés sur le groupe standard de FreeCAD, de sorte qu\'ils se comportent exactement comme les groupes, mais ils ont quelques propriétés supplémentaires. Par exemple, les [Étages](Arch_Floor/fr.md) ont la possibilité de définir et de gérer la hauteur des murs et des structures contenus, et quand ils sont déplacés, tout leur contenu est déplacé aussi.

Mais ici, puisque nous avons un seul bâtiment avec un seul (et demi) étage, il n\'y a pas de réel besoin d\'utiliser ces objets, nous allons donc nous en tenir à de simples groupes.




Maintenant, revenons au travail. Masquez le groupe de toit, afin que nous puissions mieux voir à l\'intérieur, et commutez le Mode d\'Affichage des objets de l\'étage à filaire (ou utilisez l\'outil [Bascule le mode d\'affichage](Draft_ToggleDisplayMode/fr.md) ) afin que nous puissions encore nous accrocher à eux, tout en voyant le plan qui est dessous. Mais vous pouvez également désactiver les étages entièrement, puis placer vos portes au niveau 0, et les élever de 15 cm avec l\'outil [Déplacer](Draft_Move/fr.md) .

Plaçons les portes intérieures. Utilisez à nouveau la \"Porte simple\" préréglée, faites des portes de 1.00m et 0.70m de large x 2,10 m de haut, avec la taille de W1 de 0.1m. Assurez-vous que vous vous accrochez à la bonne paroi lorsque vous les placez, afin qu\'elles créent automatiquement un trou dans le mur. S\' il est difficile de les placer correctement, vous pouvez les placer dans un lieu plus facile, à l\'angle du mur, par exemple, puis les déplacer. Le «trou» se déplacer en même temps.

Si par erreur, vous avez mis une fenêtre dans le mauvais mur, il est facile de la corriger : Retirez la fenêtre du groupe \"Soustraction\" du mur hôte en mode d\'édition, comme nous l\'avons vu ci-dessus, puis ajoutez-la au groupe \"de soustraction\" du mur correct, par la même méthode, ou, tout simplement, en utilisant l\'outil [Supprimer](Arch_Remove/fr.md).

Après un peu de travail, toutes nos portes sont là :

<img alt="" src=images/Arch_tutorial_25.jpg  style="width:1024px;">

Après un coup d'œil de plus près à la vue d\'élévation, j\'ai détecté maintenant une autre erreur : Le haut des murs de briques n\'est pas aussi à 2.60m, mais de 17.5cm inférieur, c\'est-à-dire à 2.425m. Heureusement, les fenêtres pré-configurées ont une souplesse : Vous pouvez modifier les dimensions générales (largeur et hauteur) de leurs propriétés. Donc, nous allons changer leur hauteur à 2,425 - 0,15, c\'est-à-dire 2,275. La seconde fenêtre, car c\'est un clone de la première, va s\'adapter automatiquement. C\'est essentiellement là qu\'apparait la vraie magie de la conception paramétrique.

Maintenant nous pouvons regarder les choses vraiment intéressantes : Comment concevoir vos propres fenêtres personnalisées.

### Création fenêtres personnalisées 

Comme je l\'ai expliqué auparavant, les objets [Fenêtres](Arch_Window/fr.md) sont créés à partir de représentations 2D, en éléments fermés (polylignes, cercles, rectangles, n\'importe quoi). Puisque les objets [Draft](Draft_Workbench/fr.md) ne peuvent pas détenir plus d\'un de ces éléments, l\'outil préféré pour dessiner les fenêtres est l\'atelier [Sketcher](Sketcher_Workbench/fr.md). Malheureusement, avec l\'atelier Sketcher, il n\'est pas possible de s\'aimanter à des objets externes comme avec l\'atelier Draft, ce qui serait utile ici, puisque nos élévations sont déjà établies. Heureusement, il existe un outil pour convertir les objets Draft en esquisses : L\'outil [Draft vers esquisse](Draft_Draft2Sketch/fr.md).

Alors, commençons par construire notre première disposition de fenêtre. Je l\'ai dessinée sur la façade, en utilisant plusieurs [rectangles](Draft_Rectangle/fr.md) : Un pour la ligne extérieure, et 4 pour les lignes intérieures. Je me suis arrêté avant la porte, parce que, rappelez-vous, notre porte a déjà un cadre là :

<img alt="" src=images/Arch_tutorial_26.jpg  style="width:1024px;">

Ensuite, sélectionnez tous les rectangles, et appuyez sur la touche [Draft vers esquisse](Draft_Draft2Sketch/fr.md) (et supprimer les rectangles, car cet outil ne supprime pas les objets originaux, en cas de problème). Puis, avec la nouvelle esquisse sélectionnée, appuyez sur l\'outil [Fenêtre](Arch_Window/fr.md):

<img alt="" src=images/Arch_tutorial_27.jpg  style="width:1024px;">

L\'outil permet de détecter que la disposition a un filaire externe et plusieurs filaires intérieurs, et vous propose automatiquement une configuration par défaut : Un cadre, fait en soustrayant les filaires intérieurs du filaire extérieur, extrudé par 1m. Nous allons changer cela, en entrant le mode d\'édition de la fenêtre, en double-cliquant dessus dans l\'arborescence :

Vous verrez une composante \"par défaut\", qui a été créée automatiquement par l\'outil Fenêtre, qui utilise les cinq filaires (en soustrayant toujours les autres du plus grand), et a une valeur d\'extrusion 1. Nous allons changer sa valeur d\'extrusion pour 0,1, pour correspondre à ce que nous avons utilisé dans les portes.

Ensuite, nous allons ajouter quatre nouveaux panneaux vitrés, chacun utilisant un seul filaire, et leur donner une extrusion de 0,01, et un décalage de 0,05, de sorte qu\'ils sont placés au milieu du cadre. C\'est à cela que votre fenêtre ressemblera lorsque vous aurez terminé :

<img alt="" src=images/Arch_tutorial_28.jpg  style="width:1024px;">

Je suppose maintenant que vous devez avoir compris la puissance de ce système : Toute combinaison de cadres et panneaux de forme quelconque est possible. Si vous pouvez le tracer en 2D, il peut exister comme un objet 3D valide.

Maintenant, nous allons dessiner les autres pièces, puis nous mettrons tout en place ensemble. Mais d\'abord. nous devons faire quelques corrections au dessin 2D de base, parce que certaines lignes sont clairement absentes, là où les fenêtres rencontrent les escaliers. Nous pouvons corriger ceci par un décalage de 2.5cm avec l\'outil [Décalage](Draft_Offset/fr.md) (avec ALT enfoncée bien sûr, pour copier nos lignes au lieu de les déplacer). Maintenant, nous pouvons dessiner la mise en page de notre fenêtre, avec [Filaires](Draft_Wire/fr.md), puis la convertir en esquisse, et en faire une fenêtre.

Après avoir fait cela plusieurs fois (je l\'ai fait en 4 morceaux séparés, mais c\'est à vous de décider), nous avons notre façade complète.

<img alt="" src=images/Arch_tutorial_29.jpg  style="width:1024px;">

Maintenant, comme avant, c\'est juste une question de rotation des pièces, et de déplacement à leur position correcte:

<img alt="" src=images/Arch_tutorial_30.jpg  style="width:1024px;">

Dernière pièce manquante : un segment de mur qui ne figurait pas sur la vue en plan, que nous devons ajouter. Nous avons plusieurs options pour ce faire ; j\' ai choisi de tracer une ligne sur le plan de masse, puis de la déplacer jusqu\'à la bonne hauteur, et enfin de créer un mur avec elle. Ensuite, nous devons aussi aller \"pêcher\" notre volume de soustraction de toit (il doit être dans la dernière colonne), puis le soustraire. Maintenant ce côté de l\'immeuble est prêt :

<img alt="" src=images/Arch_tutorial_31.jpg  style="width:1024px;">

Prêt ? Pas tout à fait. Regardez l\'image ci-dessus, nous avons fait nos portes avec un cadre de 5cm, (c\'est la valeur par défaut de la présélection). Mais les autres fenêtres ont des cadres de 2.5cm. Cela doit être corrigé.

### Édition des fenêtres 

Nous avons déjà vu comment construire et mettre à jour les composants de la fenêtre, via le mode d\'édition de la fenêtre, mais nous pouvons aussi modifier l\'esquisse sous-jacente. Les fenêtres prédéfinies ne sont pas différentes des fenêtres personnalisées, le seul outil [Fenêtre](Arch_Window/fr.md) crée l\'esquisse sous-jacente pour vous. Sélectionnez notre objet porte (l\'original, pas la copie, ne l\'oubliez pas, nous avons fait un clone), et déployez-le dans l\'arborescence. C\'est notre esquisse. Double-cliquez dessus pour passer en mode d\'édition.

l\'[atelier Sketcher](Sketcher_Workbench/fr.md) est un outil extrêmement puissant. Il ne possède pas certaines des facilités de [Draft](Draft_Workbench/fr.md), telles que rupture ou plans de travail, mais il a de nombreux autres avantages. Dans FreeCAD vous utiliserez fréquemment l\'une ou l\'autre en fonction des besoins. La caractéristique la plus importante de l\'atelier Sketcher est la possibilité de contraintes. Ces contraintes vous permettent de corriger automatiquement la position de certains éléments par rapport à d\'autres. Par exemple, vous pouvez forcer un segment à toujours être à la verticale, ou à toujours être à une certaine distance d\'un autre.

Lorsque nous éditons notre esquisse de la porte, nous pouvons voir qu\'elle est faite sur une esquisse totalement contrainte :

<img alt="" src=images/Arch_tutorial_32.jpg  style="width:1024px;">

Maintenant, il suffit de modifier les distances de 5 cm entre la ligne extérieure et la ligne intérieure, en double-cliquant dessus, et en changeant leur valeur à 2,5 cm . Après avoir cliqué sur le bouton \"OK\", notre porte (et son clone) ont été mis à jour.

## Travailler sans support 2D 

Jusqu\'à présent, notre travail a été relativement facile, parce que nous avions les dessins 2D sous-jacents pour fonder nos travaux. Mais maintenant, nous devons faire la façade opposée et l\'atrium de verre, et les choses se compliquent : Le dessin de la façade opposée a beaucoup de choses fausses, ne représente pas l\'atrium du tout, et nous n\'avons tout simplement pas de dessin pour les murs intérieurs de l\'atrium. Nous aurons donc besoin d\'inventer un certain nombre de choses nous-mêmes. Veillez à consulter [reference pictures](http://www.pedrokok.com.br/2010/02/residencia-artigas-sao-paulo-sp/img_8265-533px/) pour comprendre comment les choses sont faites. Ou faites-le comme vous le souhaitez !

Une chose que nous pouvons déjà faire : dupliquer la fenêtre compliquée de l\'escalier avec l\'outil [Draft Déplacer](Draft_Move/fr.md), parce que c\'est la même des deux côtés :

<img alt="" src=images/Arch_tutorial_33.jpg  style="width:1024px;">

Notez qu\'ici, j\'ai préféré reproduire avec l\'outil [Déplacer](Draft_Move/fr.md) au lieu d\'utiliser un [clone](Draft_Clone/fr.md), parce que le clone ne supporte pas actuellement les différentes couleurs à l\'intérieur des objets. La différence est que le clone est une copie de la forme finale de l\'objet d\'origine, tandis que si vous copiez un objet, vous créez un nouvel objet et lui donnez toutes les propriétés de celui d\'origine (donc aussi son esquisse de base et sa définition des composants de la fenêtre, qui sont toutes deux stockées en tant que propriétés).

Maintenant, nous devons attaquer les parties qui ne sont pas dessinées partout. Commençons par le mur de verre entre le salon et l\'atrium. Il sera plus facile de le dessiner sur la vue d\'élévation, parce que nous aurons la bonne hauteur du toit. Une fois que vous êtes en vue de dessus, vous pouvez faire pivoter la vue dans le menu Affichage → Vues standard → Rotation gauche ou à droite, jusqu\'à ce que vous obteniez une vue confortable pour travailler, comme ceci :

<img alt="" src=images/Arch_tutorial_34.jpg  style="width:1024px;">

Notez comment sur l\'image ci-dessus, j\'ai fait une ligne à partir du modèle de la section de gauche, pour obtenir la largeur exacte de la fenêtre. Puis, j\'ai reproduit cette largeur sur la vue en élévation et divisé en quatre pièces. Puis j\'ai construit une fenêtre principale, plus quatre autres fenêtres pour les portes coulissantes. L\'atelier Esquisses (sketcher) a parfois des difficultés avec des filaires qui se chevauchent, c\'est pourquoi j\'ai préféré les garder séparés comme ceci :

<img alt="" src=images/Arch_tutorial_35.jpg  style="width:1024px;">

Après les rotations nécessaires, tout s\'enclenche parfaitement en place :

<img alt="" src=images/Arch_tutorial_36.jpg  style="width:1024px;">

Nous avons encore besoin de quelque pièce d\'angle là. Un petit truc utile avec l\'outil [Plan de travail](Draft_SelectPlane/fr.md), si vous avez une face sélectionnée lorsque vous appuyez sur le bouton, le plan de travail correspondra à cette face (au moins sa position, et si la face est de forme rectangulaire, il essaie également de faire correspondre ses axes). C\'est utile pour dessiner des objets 2D directement sur le modèle, comme ici, nous pouvons dessiner un rectangle à extruder directement à sa position correcte :

<img alt="" src=images/Arch_tutorial_37.jpg  style="width:1024px;">

Puis nous allons faire les deux morceaux restants. L\'un est facile, c\'est une copie de ce qui est de l\'autre côté, ainsi nous pouvons simplement utiliser le dessin 2D :

<img alt="" src=images/Arch_tutorial_38.jpg  style="width:1024px;">

L\'autre est un peu difficile, en regardant les photos, on voit qu\'il a beaucoup de divisions verticales, comme les fenêtres des escaliers. Par chance (ou très bonne conception de Vilanova Artigas), la largeur de notre fenêtre, de 4.50m, est exactement la même que la fenêtre des escaliers. Nous pouvons utiliser exactement la même division : 15 morceaux de 30 cm. Ici j\'ai utilisé l\'outil [Draft Réseau orthogonal](Draft_OrthoArray/fr.md) pour copier les deux lignes 15 fois et j\'ai dessiné des rectangles par dessus :

<img alt="" src=images/Arch_tutorial_39.jpg  style="width:1024px;">

Une fois cela fait, nous pouvons créer notre fenêtre avec la même méthode que nous connaissons déjà. Une autre petite astuce utile, au cas où vous ne l\'auriez pas trouvée : Lors de l\'édition d\'une fenêtre, si vous changez le nom d\'un composant, il crée en fait un duplicata de celui-ci. Donc, pour créer les 15 panneaux de verre intérieurs, au lieu de cliquer 15 fois sur le bouton \"ajouter\" et de remplir 15 fois les données, vous pouvez juste continuer à en éditer une, et changer son nom et son filaire, il va créer une copie à chaque fois.

Après que la fenêtre ait été pivotée et amenée à son emplacement, l\'atrium est complet :

<img alt="" src=images/Arch_tutorial_40.jpg  style="width:1024px;">

## Éditions et correctifs 

Maintenant, quand nous regardons notre élévation arrière, et la comparons avec le plan, nous voyons qu\'il y a des différences qui doivent être corrigées. A savoir, les fenêtres des chambres sont plus petites que ce que j\'ai d\'abord pensé, et nous aurons besoin d\'ajouter d\'autres murs. Afin de le faire correctement, certains planchers doivent être coupés :

<img alt="" src=images/Arch_tutorial_41.jpg  style="width:1024px;">

Nous avons bien sûr plusieurs façons de le faire, faire un volume de soustraction serait un moyen facile, mais ce serait ajouter une complexité inutile au modèle. Mieux vaut modifier le filaire de base de chaque plancher. C\'est là que l\'outil [Modifier](Draft_Edit/fr.md) entre en action. En développant ces planchers dans l\'arborescence, puis en rendant leurs filaires de base visibles, nous pouvons double-cliquer dessus pour passer en mode édition. Là, nous pouvons déplacer leurs points, ou ajouter ou supprimer des points. Avec cela, l\'édition de nos plaques de sol devient facile.

<img alt="" src=images/Arch_tutorial_42.jpg  style="width:1024px;">

Après un peu plus de sueur (la personne qui a fait ces dessins est devenue sans doute assez paresseuse quand elle fit cette dernière élévation, beaucoup est mal dessiné), nous avons enfin notre maison complète :

<img alt="" src=images/Arch_tutorial_43.jpg  style="width:1024px;">

Notez le tube de cheminée, qui est fait d\'un cercle que j\'ai utilisé pour faire un trou dans le bloc de la cheminée, que j\'ai extrudé, puis converti en un tube avec l\'outil [décalage](Part_Offset/fr.md).


{{Note|Problèmes dans les objets|
Parfois un objet peut vous faire avoir des problèmes. Par exemple, l'objet qui était basé dessus a été supprimé, et l'objet ne peut donc pas recalculer sa forme. Ceux-ci vous sont généralement présentés par un petit signe rouge sur leur icône, et/ou un avertissement dans la fenêtre de sortie. Il n'existe aucune recette générique pour résoudre ces problèmes, car ils peuvent avoir de nombreuses origines. Mais, la meilleure façon de les résoudre est souvent de les supprimer, et, si vous n'avez pas supprimé leurs objets de base, les recréer.}}

## Sorties

Maintenant, après tout le travail acharné que nous avons réalisé pour construire ce modèle, vient la récompense : Que pouvons-nous faire ? Fondamentalement, c\'est le grand avantage de travailler avec BIM, tous nos besoins architecturaux traditionnels, tels que les dessins 2D (plans, coupes, etc.), les rendus réalistes, et les calculs (estimations de quantités, etc.) peuvent tous être extraits du modèle. Et, mieux encore, mis à jour à chaque modification du modèle. Je vais vous montrer ici comment obtenir ces différents documents.

### Préparations

Avant de commencer à exporter des choses, il est intéressant de faire un constat : Comme vous l\'avez vu, notre modèle est de plus en plus complexe, avec beaucoup de relations entre les objets. Cela peut rendre lourdes les opérations de calcul ultérieures, telles que la coupe à travers le modèle. Un moyen rapide et magique de \"simplifier\" radicalement votre modèle, est de supprimer toutes cette complexité, en l\'exportant vers le Format [STEP](http://en.wikipedia.org/wiki/ISO_10303-21). Ce format préservera toute la géométrie, mais rejettera toutes les relations et les constructions paramétriques, ne gardant que la forme finale. Lorsque vous réimporterez ce fichier STEP dans FreeCAD, vous obtiendrez un modèle qui n\'a pas de relation, et une taille de fichier beaucoup plus petite. Pensez-y comme un fichier \"de sortie\", que vous pouvez mettre à jour à tout moment à partir de votre fichier \"maître\" :

<img alt="" src=images/Arch_tutorial_44.jpg  style="width:1024px;">

### Exportation vers IFC et autres applications 

<img alt="" src=images/Arch_tutorial_45.jpg  style="width:400px;">

Une des choses très fondamentales dont vous avez besoin lorsque vous travaillez avec BIM est de pouvoir importer et exporter des fichiers [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) . C\'est encore un travail en cours dans FreeCAD. Le Format [IFC](Arch_IFC/fr.md) est déjà pris en charge, et l\'importation de fichiers IFC dans FreeCAD est déjà assez fiable. L\'exportation est encore au stade expérimental, et compte actuellement de nombreuses limitations. Cependant, les choses vont en s\'améliorant et nous devrions obtenir l\'exportation correcte IFC très bientôt.

[ export IFC](Arch_IFC/fr.md) nécessite très peu de configuration, une fois que les bibliothèques de logiciels nécessaires sont installées. Vous avez seulement besoin de recréer la structure du bâtiment, qui est nécessaire dans tous les fichiers IFC, en ajoutant un [ Bâtiment](Arch_Building/fr.md) à votre fichier, puis un [ Plancher](Arch_Floor/fr.md), puis en déplaçant tous les groupes d\'objets qui composent votre modèle en eux. Assurez-vous que vous enlevez votre géométrie de construction (tous les trucs 2D que nous avons dessinés) de la structure pour vous éviter de faire un fichier IFC inutilement lourd.

Une autre chose à régler, est de vérifier le \"Rôle\"\" des d\'éléments structurels. Puisque l\'IFC n\'a aucun élément structurel \"générique\", comme FreeCAD, nous avons besoin de leur attribuer des rôles (colonne, poutre, etc \...) pour que l\'exportateur sache quel élément créer dans le fichier IFC.

Dans ce cas, nous avons besoin de l\'ensemble de notre système architectural, donc l\'exportateur IFC peut savoir si un objet doit être exporté comme un mur ou une colonne, de sorte que nous utilisons notre modèle «maître», et non pas notre modèle \"de sortie\".

Une fois cela fait, sélectionnez simplement votre objet de construction, et choisissez le format \"Industry Foundation Classes\". L\'exportation vers des applications non BIM, comme [1](http://www.sketchup.com/Sketchup) est également facile, vous avez plusieurs formats d\'exportation à votre disposition, tels que [Collada](Arch_DAE/fr.md), STEP, IGES ou OBJ.




### Rendu

FreeCAD dispose également d\'un module de rendu, l\'atelier [Raytracing](Raytracing_Workbench/fr.md). Cet atelier prend actuellement en charge deux moteurs de rendu, [PovRay](http://www.povray.org/) et [LuxRender](http://www.luxrender.net). Puisque FreeCAD n\'est pas conçu pour un rendu d\'image, les caractéristiques que l\'atelier Raytracing vous offre sont quelque peu limitées. Le meilleur plan d\'action lorsque vous voulez faire un rendu correct, est d\'exporter votre modèle dans un format basé sur les mailles comme OBJ ou STL, et de l\'ouvrir dans une application plus adaptée pour faire un rendu comme [blender](http://www.blender.org). L\'image ci-dessous a été rendue avec le moteur de rendu de blender :

<img alt="" src=images/Arch_tutorial_47.jpg  style="width:1024px;">

Mais pour un rendu rapide, l\'atelier \[\[RayTracing Workbench\]/fr\|RayTracing\] peut déjà faire du bon travail, tout en ayant l\'avantage d\'être très simple à configurer, grâce à son système de modèles. Il s\'agit d\'un rendu intégralement réalisé à l\'intérieur de FreeCAD, avec le moteur Luxrender, qui utilise le modèle \"indoor\".

<img alt="" src=images/Arch_tutorial_48.jpg  style="width:1024px;">

L\'atelier de Raytracing vous offre encore un contrôle très limité sur les matériaux, mais l\'éclairage et les environnements sont définis dans les modèles, afin qu\'ils puissent être entièrement personnalisés.

### Dessins 2D 

Certes, l\'utilisation la plus importante de la BIM (modélisation des informations du bâtiment) est de produire des dessins en 2D automatiquement. Ceci est fait dans FreeCAD avec l\'outil [Plan de Coupe](Arch_SectionPlane/fr.md). Cet outil vous permet de placer un objet Plan de Coupe dans la vue 3D, que vous pouvez orienter pour produire des plans, coupes et élévations. Les plans de coupe doivent savoir quels objets ils doivent considérer, aussi une fois que vous en avez créé un, vous devez ajouter des objets avec l\'outil [Ajouter](Arch_Add/fr.md). Vous pouvez ajouter des objets individuels, ou, plus commodément, un groupe, un étage ou un bâtiment entier. Cela vous permet de changer facilement la portée d\'un certain plan de coupe plus tard, en ajoutant ou en supprimant des objets vers/de ce groupe. Toute modification de ces objets se reflète dans les vues produites par le plan de coupe.

Le plan de coupe produit automatiquement des vues coupées des objets qu\'il traverse. En d\'autres termes, pour produire des vues extérieures, il vous suffit de placer le plan de coupe à l\'extérieur de vos objets.

<img alt="" src=images/Arch_tutorial_49.jpg  style="width:1024px;">

Les plans de coupe peuvent produire deux sorties différentes : des objets [Part](Part_Workbench/fr.md) qui vivent dans le même document que votre modèle 3D, ou des [vues de dessin](Drawing_Workbench/fr.md), conçues pour être utilisées sur une feuille de dessin produite par l\'[Atelier Drawing](Drawing_Workbench/fr.md). Chacun de ces éléments se comporte différemment et présente ses propres avantages.

**Vues des Formes**

Cette sortie est produite en utilisant l\'outil [Draft Shape2DView](Draft_Shape2DView/fr.md) (projection 2D) à partir d\'un plan de coupe présélectionné. Vous produisez une vue 2D du modèle directement dans l\'espace 3D, comme sur l\'image ci-dessus. Le principal avantage ici est que vous pouvez travailler dessus en utilisant les outils de l\'atelier [Draft](Draft_Workbench/fr.md) (ou tout autre outil standard de FreeCAD), de sorte que vous pouvez ajouter des textes, des dimensions, symboles, etc :

<img alt="" src=images/Arch_tutorial_50.jpg  style="width:1024px;">

Sur l\'image ci-dessus, deux [projections 2D](Draft_Shape2DView/fr.md) ont été produites pour chaque section, une montrant tout, l\'autre ne montrant que les lignes de coupe. Cela nous permet de lui donner une épaisseur de ligne différente et d\'activer l\'option hachures. Ensuite, les dimensions, les textes et les symboles ont été ajoutés, et quelques blocs DXF ont été importés pour représenter les meubles. Ces vues sont alors faciles à exporter au format DXF ou DWG et à ouvrir dans votre application de CAO 2D favorite, comme [LibreCAD](http://www.librecad.org), où vous pourrez continuer à les travailler :

<img alt="" src=images/Arch_tutorial_51.jpg  style="width:1024px;">

Notez que certaines fonctionnalités ne sont pas encore prises en charge par loutil [export DXF/DWG](Draft_DXF/fr.md) de sorte que le résultat dans votre logiciel 2D peut différer un peu. Par exemple, dans l\'image ci-dessus, j\'ai dû refaire les hachures, et corriger la position de certains textes de cotes. Si vous placez vos objets dans des groupes différents dans FreeCAD, ceux-ci deviennent des couches (calques) dans votre application de CAO 2D.

**Dessin de vues**

L\'autre type de sortie qui peut être produit à partir de [Plans de coupes](Arch_SectionPlane/fr.md) est une [vue de dessin](Drawing_Workbench/fr.md). Ces vues sont obtenues en utilisant l\'outil [Draft Feuille de dessin](Draft_Workbench/fr.md) à partir d\'un plan de coupe présélectionné. Cette méthode a une grande limitation par rapport à la précédente : vous avez des possibilités limitées pour modifier les résultats, et en ce moment, des choses comme le dimensionnement ou le hachurage ne sont pas encore supportées nativement.

D\'autre part, le résultat final étant plus facile à manipuler, et les possibilités graphiques du format SVG étant immenses, à l\'avenir, ce sera sans doute la méthode préférée. À l\'heure actuelle, cependant, vous obtiendrez de meilleurs résultats en utilisant la méthode précédente.

<img alt="" src=images/Arch_tutorial_52.jpg  style="width:1024px;">

Sur l\'image ci-dessus, la géométrie est la sortie directe du plan de coupe, mais certains autres objets Draft ont été ajoutés, tels que les dimensions et les polygones hachurés, et un autre objet de vue avec la même échelle et les valeurs de décalage ont été produits à partir d\'eux avec l\'outil [Feuille de dessin](Draft_Drawing/fr.md). A l\'avenir, ces opérations seront effectuées directement sur la page de dessin, laissant votre modèle totalement propre.

### Extraction du métré 

C\'est une autre tâche très importante qui doit être réalisée dans un modèle BIM. Dans FreeCAD, les choses se présentent bien car son moteur OpenCasCade prend déjà en compte le calcul de longueurs, surfaces et volumes pour tous les objets créés. Tant que tous les objets [Arch](Arch_Workbench/fr.md) sont des solides, vous pourrez en obtenir le volume.

**Utiliser les tableurs**

Pour remplir une feuille de calcul avec les valeurs extraites du modèle, l\'outil Arch\_Schedule peut être utilisé.

![](images/Arch_schedule_example03.jpg )

**Le mode relevé**

Une autre manière d\'examiner votre modèle et d\'extraire des valeurs, est d\'utiliser le mode [Arch\_Survey](Arch_Survey/fr.md). Dans ce mode, vous pouvez cliquer sur des points, des bords, des faces ou le double-cliquer pour choisir les objets entiers, et vous obtenez respectivement l\'affichage dans le modèle de l\'altitude, la longueur, l\'aire ou le volume. De plus la valeur est copiée dans le presse-papiers, ainsi vous pouvez facilement sélectionner et coller des valeurs dans une autre application ouverte.

<img alt="" src=images/Arch_tutorial_54.jpg  style="width:1024px;">

## Conclusion

J\'espère que ce tutoriel vous aura donné un bon aperçu des outils disponibles. Pensez à consulter la documentation des ateliers [Arch](Arch_Workbench/fr.md) et [Draft](Draft_Workbench/fr.md) pour plus de détails (il y a plus d\'outils que décrits dans ce tutoriel), et plus généralement le reste de la [documentation FreeCAD ](Main_Page/fr.md). Passez voir le [forum](http://forum.freecadweb.org) aussi, la plupart des problèmes peuvent être résolus en un rien de temps (pensez à lire les règles du forum et postez bien vos informations FreeCAD). Enfin suivez le [blog de Yorik (en)](http://yorik.uncreated.net/guestblog.php?tag=freecad).

Le fichier créé durant ce tutoriel peut être téléchargé [ici](http://yorik.uncreated.net/archive/projects/casa_artigas.fcstd).


{{Tutorials navi

}}  
