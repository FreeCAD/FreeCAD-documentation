# Analysis of reinforced concrete with FEM/fr
{{TutorialInfo/fr
|Topic=Béton armé avec FEM
|Level=Intermédiaire
|Time=60 minutes
|Author=_, [https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=18062 HarryvL]
|FCVersion=0.19 ou suivantes
|Files=
}}

## Contexte

L\'atelier FEM offre la possibilité d\'estimer le niveau de ferraillage requis dans une structure en béton afin d\'éviter une rupture fragile sous tension ou par cisaillement.

<img alt="" src=images/Femconcrete_Wall_3D_rx_PSS.png  style="width:700px;">

Ceci est effectué avec la méthode décrite dans [\"Computation of reinforcement for solid concrete\", P.C.J. Hoogenboom and A. de Boer, HERON Vol. 53 (2008) No. 4](http://heronjournal.nl/53-4/3.pdf). Il s\'agit essentiellement d\'une routine de post-traitement pour Calculix, qui calcule les principales contraintes de traction dans le béton à partir d\'une analyse élastique et les utilise pour déterminer le ferraillage minimal requis dans les trois directions de coordonnées pour éviter les ruptures. Dans l\'analyse, il est supposé que le béton ne peut pas supporter de contraintes de traction, alors que l\'acier est utilisé à sa capacité maximale (c\'est-à-dire qu\'il prend en compte toute la contrainte).

Le renforcement requis est exprimé en termes de rapport de renforcement. C\'est le rapport de l\'acier à la surface du béton. Par exemple, un rapport de ferraillage de 0,01 dans la direction x (rx = 0,01) signifie que la section totale des barres de ferraillage s\'étendant dans la direction x doit être égale à 1% de la surface de la section en béton traversée. Une section hypothétique de 1 m x 1 m devrait dans ce cas contenir 0,01 m2 d\'acier, ce qui pourrait être obtenu en utilisant 90 barres d\'armature de 12 mm de diamètre chacune (surface d\'acier = 90 \* PI \* (0,012)\^2 / 4 = 0,0102 m\^2). Si le rapport de renforcement requis sur cette section transversale en béton est uniforme, les barres pourraient être placées sur une grille d\'équidistance de 9 x 10 avec un entraxe d\'environ 10 cm. Il s'agit toujours d'un chiffre pratique dans lequel il reste suffisamment d'espace entre les barres pour permettre au béton de passer et d'assurer un remplissage de haute qualité. Des valeurs beaucoup plus élevées conduiraient à une grille de renforcement très dense avec des problèmes potentiels de qualité, tandis que des valeurs beaucoup plus basses pourraient entraîner de grandes fissures de tension dans la section transversale entre les barres. Dans la pratique, le ratio typique va de 0,002 à 0,02 (= 0,2% à 2%). Vous trouverez des informations supplémentaires dans les codes de conception.

Si le rapport de renforcement requis n\'est pas uniforme sur toute la section, la section peut être divisée pragmatiquement en sous-sections avec un rapport plus ou moins uniforme et un renforcement appliqué à ces sections. Un exemple sera donné plus tard.

En guise de mise en garde, la conception d\'une structure en béton sûre et durable requiert bien plus que ce que l\'atelier FEM peut actuellement fournir. Par exemple, la méthode ne calcule pas la largeur des fissures (importante pour la durabilité et la fonctionnalité), ni les déformations précises (les résultats FEM pour le béton sont simplement linéaires-élastiques), et ne tient pas compte des exigences en matière d\'ancrage des armatures (qui entraîneraient une augmentation des taux de renforcement requis dans les zones d\'ancrage). De plus, il ne prévoit pas non plus l\'écrasement du béton (bien que l\'indication de cela puisse être obtenue en traçant la contrainte de Mohr-Coulomb - voir plus loin), ce qui pourrait signifier que le béton se ruine avant que le renfort ne cède, entraînant une défaillance fragile de la structure globale. Cette limitation et d\'autres signifient que la fonctionnalité béton de FEM ne peut être utilisée que pour évaluer des conceptions conceptuelles, tandis que les décisions de conception détaillées critiques pour la sécurité et les performances devraient être laissées à des professionnels qualifiés.

## Géométrie du modèle, charges et supports 

Bien que la routine béton de FEM n\'exige aucun critère supplémentaire en matière de géométrie, de charges et de supports, il convient de garder à l'esprit que des angles vifs et un support sur une arête ou un sommet peuvent introduire des concentrations de contraintes qui conduiront à des taux de renforcement extrêmement élevés et irréalistes à ces endroits ou à leur proximité.

## Paramètres des matériaux 

L\'atelier FEM dispose d\'un matériau spécifique pour les matériaux renforcés, qui combine un matériau de matrice (par exemple le béton) et un matériau de renforcement (par exemple de l\'acier). Pour l\'analyse du béton armé avec FEM, les paramètres suivants doivent être spécifiés au minimum :

pour le béton :

   - Module de Young (utilisé dans l'analyse Calculix pour calculer les déformations élastiques et les contraintes)
   - coefficient de Poisson (idem)
   - résistance à la compression unidirectionnelle (utilisée lors du post-traitement dans FEM pour calculer la contrainte de Mohr Coulomb en tant qu'indicateur de rupture par écrasement ou de cisaillement dans le béton)
   - angle de frottement (idem)

pour l\'acier :

   - limite d'élasticité (utilisée lors du post-traitement dans FEM pour calculer les taux de renforcement)

Veuillez noter que trois types d'analyses sont effectuées : 1) Une analyse élastique utilisant Calculix (utilisant uniquement les paramètres élastiques du béton) ; 2) une étape de post-traitement pour analyser le ferraillage requis (en utilisant uniquement la limite d\'élasticité de l\'acier) et 3) le calcul de la contrainte de Mohr Coulomb (en utilisant uniquement les paramètres de résistance du béton, à savoir la résistance à la compression unidirectionnelle et l\'angle de frottement). La contrainte de Mohr Coulomb peut être examinée dans le pipeline VTK.

## Application

Dans la suite de cet article, quelques cas pratiques seront analysés pour discuter de l\'application de la méthode.

### Poutre simplement supportée avec une charge uniforme 

Une poutre en béton de 4,0 x 0,1 x 0,3 m est chargée par son propre poids et par une charge répartie de 100 kN (25 kN/m).

Les paramètres des matériaux sont les suivants :

pour le béton :

   - module de Young = 32 GPa (par défaut selon Calculix pour le béton)
   - coefficient de Poisson = 0,17 (par défaut selon Calculix pour le béton)
   - résistance à la compression unidirectionnelle = 30 MPa (béton type C30/37)
   - angle de frottement = 30 degrés

pour l\'acier :

   - limite d'élasticité = 500 MPa

Le poids spécifique du béton est de 24 kN/m\^3

L\'armature requise dans la direction x est très importante (5,4%) et dépasse les pourcentages maximum typiques autorisés par le code pour éviter toute défaillance fragile. Les fortes contraintes de cisaillement au niveau des appuis obligent également à un renforcement important :

<img alt="" src=images/Pre_Stressed_Beam_2_Weight_Load_RR_x_0.054.jpg  style="width:700px;">

Le graphique de Mohr Coulomb montre que la poutre est effectivement sujette à l\'écrasement du côté comprimé (contrainte de Mohr Coulomb \> 0.0), comme on pouvait s\'y attendre avec un pourcentage de renforcement très élevé :

<img alt="" src=images/Pre_Stressed_Beam_2_Weight_Load_MC.jpg  style="width:700px;">

Le rapport de renforcement et la contrainte de Mohr Coulomb indiquent que nous avons un problème et qu\'il est nécessaire de repenser notre conception. Les solutions potentielles consistent à augmenter les dimensions de la poutre ou à utiliser du béton précontraint. Plus de détails peuvent être trouvés dans le post suivant : <https://forum.freecadweb.org/viewtopic.php?f=18&t=28821&start=10#p235003>

### Poutre avec support à mi-portée 

Une poutre en béton de 8,0 x 0,2 x 0,4m est chargée par son propre poids et par une charge répartie de 160 kN (20 kN/m).

Les paramètres matériels sont les suivants :

pour le béton :

   - module de Young = 32 GPa (par défaut selon Calculix pour le béton)
   - coefficient de Poisson = 0,17 (par défaut selon Calculix pour le béton)
   - résistance à la compression unidirectionnelle = 25 MPa (béton type B25)
   - angle de frottement = 30 degrés

pour l\'acier :

   - limite d'élasticité = 286 MPa (réduite de 500 MPa pour tenir compte d'un coefficient de sécurité de 1,75)

Le poids spécifique du béton est de 24 kN/m\^3

Le tracé ParaView du fichier VTK exporté montre que l\'exigence de ferraillage est la plus grande en haut de la poutre près du support central. C\'est ici que se produit le moment de flexion le plus élevé. Le taux de renforcement maximal est de 0,02 dans la partie supérieure de la plage pratique indiquée précédemment :

<img alt="" src=images/Beam_with_Central_Support_rx_full.png  style="width:700px;">

La section d'acier requise sur le support central peut être obtenue avec un filtre d'intégration ParaView appliqué à la section médiane de la poutre :

<img alt="" src=images/CoG_Reinforcement.png  style="width:700px;">

Le panneau au bas de cette image montre que la surface totale d\'acier requise pour cette section est de 389,6 mm\^2. Comme une barre de renforcement de diamètre 12 mm a une section de 113 mm\^2, cela signifie que 4 barres seraient nécessaires, ce qui correspond à une section de 452 mm\^2. Celles-ci devraient être placés près du sommet de la poutre, tout en maintenant une couverture en béton suffisante. Le centre de gravité théorique du ferraillage peut être trouvé par intégration :

   CoG_y = Integrale (rx * y dy dz) / Integrale (rx dy dz)    
   
   CoG_z = Integrale (rx * z dy dz) / Integrale (rx dy dz)

Ces intégrales peuvent également être déterminées avec ParaView et donner pour le cas présent (voir les panneaux du bas dans l\'image ci-dessus) :

   CoG_y = 38961 / 389.6 = 100.0 mm
   
   CoG_z = 134917 / 389.6 = 346.3 mm

ce qui correspond, comme prévu, au milieu de la largeur près du sommet.

La nécessité de renforcement énoncée ci-dessus s'accorde bien avec celle obtenue avec les méthodes traditionnelles :

<https://forum.freecadweb.org/viewtopic.php?f=18&t=28821&start=20#p235063>

Enfin, une vérification des contraintes de Mohr Coulomb est à effectuer pour vérifier le potentiel d\'écrasement du béton. Pour cette vérification, la résistance à la compression caractéristique du béton (25 MPa) doit être divisée par un coefficient de matériau approprié (\> 1,0).

### Mur en cisaillement avec une charge uniforme 

Un mur de 4,0 x 2,0 x 0,15 m est soutenu par deux colonnes de 0,5 m de large. Ce mur est chargé par son propre poids et par une charge répartie de 1,0MN sur son sommet.

Les paramètres des matériaux sont les suivants :

pour le béton :

   - module de Young = 32 GPa (par défaut selon Calculix pour le béton)
   - coefficient de Poisson = 0,17 (par défaut selon Calculix pour le béton)
   - résistance à la compression unidirectionnelle = 20 MPa
   - angle de frottement = 30 degrés

pour l\'acier :

   - limite d'élasticité = 286 MPa

Le poids spécifique du béton est de 24 kN/m\^3

Le rapport de renforcement horizontal atteint un maximum de 0,014 (1,4%) près de la section centrale inférieure du mur et le rapport de renforcement vertical est au maximum de 0,008 (0,8%) vers les angles du mur avec les colonnes, où les contraintes de cisaillement sont les plus élevées :

<img alt="" src=images/Wall_3D.jpg  style="width:1000px;">

L\'image ci-dessus montre les zones de ferraillage à ratio constant possibles pour la conception de ce ferraillage. Bien qu\'un pourcentage d\'armature minimal de 0,2% ait été choisi, il sera difficile d\'atteindre une valeur aussi faible dans la pratique, étant donné que l\'espacement ne doit pas dépasser une limite pratique (environ 300 mm). Même avec une grille de renforcement légère avec des barres de 10 mm (section = 78 mm\^2), le rapport de renforcement serait alors de 2 \* 78 / (150 \* 300) = 0,0035 (0,35%). (Remarque : le facteur 2 découle du fait que la grille sera placée sur les deux faces du mur). Si nous ajoutons une barre supplémentaire à la grille (divisant par deux la distance), le rapport de ferraillage doublerait à 0,7% et une de plus donnerait environ 1%. Ainsi, la plupart des exigences en matière de renforcement pourraient être satisfaites en commençant par une grille de d = 10 mm espacée de 300x300 mm et en ajoutant des barres horizontalement ou verticalement, selon les besoins. Cela couvrirait tout sauf l\'exigence au bas du mur, où nous pourrions ajouter 3 barres d = 12mm, donnant un rapport de renforcement horizontal de 3 \* 113mm\^2 / (150mm \* 150mm) = 0,015 (1,5%). Ici, on suppose que la hauteur de la zone inférieure est de 150 mm. Alternativement, nous pourrions choisir 2 barres de 16 mm de diamètre, ce qui donnerait le même taux de renforcement pour une zone de 180 mm de hauteur.

Enfin, une analyse des contraintes de Mohr Coulomb montre qu'aucun concassage de béton n'apparait dans le mur. <https://forum.freecadweb.org/viewtopic.php?f=18&t=28821&start=10#p234673>

### Poutre encastrée avec ouverture 

Le Guide du praticien FIB sur la modélisation par éléments finis des structures en béton armé contient un exemple de conception d\'une poutre en béton encastrée avec ouverture. L\'exemple est utilisé dans ce rapport pour illustrer la méthode \"Strut-and-Tie\". Ici, les résultats seront comparés à ceux obtenus avec l'atelier FEM de FreeCAD.

Les dimensions de la poutre sont 11,0 x 4,0 x 0,6m et elle est contrainte au sommet par une charge répartie de 120 kN/m et une autre de 5000 kN introduite par une colonne de 1 m de large. La résistance à la compression pondérée du béton est de 0,75 x 0,6 x fc = 0,45 \* 35 = 15,8 MPa et la limite d\'élasticité pondérée de l\'acier d\'armature est de 315 MPa.

Les coefficients de renforcement et les principales contraintes du béton (compression uniquement) dérivés de FreeCAD sont indiqués ci-dessous :

<img alt="" src=images/FIB_Deep_Concrete_Beam_1.png  style="width:1000px;">

Le renforcement horizontal requis (en rouge ci-dessous) est déterminé par l\'intégration du rapport de renforcement horizontal sur les coupes verticales intéressantes (en bas en noir). Ceci est fait en utilisant un filtre d\'intégration Paraview.

<img alt="" src=images/FIB_Reinforcement(2).jpg  style="width:700px;">

L\'encart de la figure ci-dessus montre une comparaison des exigences de renforcement (en mm\^2 d\'acier) déterminées avec FreeCAD par rapport à celles du rapport FIB.

Le tableau suivant montre comment l'intégration sur les lignes intéressantes fonctionne dans Paraview :

<img alt="" src=images/FIB_Reinforcement_ry.jpg  style="width:700px;">

Enfin, un graphique des contraintes principales de compression et de traction montre comment les contraintes circulent dans la poutre.

<img alt="" src=images/FIB_Beam_Stresses_and_Cables.jpg  style="width:700px;">

Le modèle de contrainte de traction suggère un concept alternatif utilisant des câbles de précontrainte (superposés en blanc). Ce concept est développé dans le post suivant : <https://forum.freecadweb.org/viewtopic.php?f=18&t=33049>

## En relation 

-   [FEM et béton](FEM_Concrete/fr.md)


{{Tutorials navi

}} {{FEM Tools navi}}

---
[documentation index](../README.md) > Analysis of reinforced concrete with FEM/fr
