# Path FAQ/fr
## Combien d\'axes l\'atelier Path peut-il traiter? 

Pour le moment, en version 0.18, l\'atelier Path peut gérer jusqu\'à 3 axes. Actuellement, les capacités du 4ème axe sont en cours de développement pour la prochaine version officielle, avec certaines opérations de l\'atelier Path déjà mises à niveau vers le statut de base du 4ème axe.

[En haut](#top.md)

## Pourquoi semble-t-il que, dans certains cas, l\'atelier Path propose plus d\'une façon de décrire une opération? 

L\'atelier Path fournit des outils permettant de réaliser de nombreuses opérations de fraisage, d\'autres étant en élaboration et comme FreeCAD est à code ouvert, rien n\'empêche les utilisateurs de créer leurs propres fonctionnalités.

Dans le dessin 3D, il existe souvent plusieurs méthodes disponibles qui peuvent être avantageuses à utiliser pour des opérations Job différents. Dans certains cas, des combinaisons d\'opérations sont utilisées pour fournir un fraisage complet du Stock.

Un exemple habituel est que l\'opération Contour peut être générée depuis Edges ou Faces. Dans certains cas, il peut y avoir un avantage à utiliser l\'une ou l\'autre des méthodes.

[En haut](#top.md)

## Pourquoi l\'habillage d\'une opération modifie-t-il la position dans le flux de travail affiché dans la liste des opérations? 

Tous les ajouts au travail, y compris les modifications et les copies d\'opérations, sont ajoutés à la fin du flux de travail du travail. Si cela perturbe la séquence correcte du travail, elle doit être réorganisée dans l\'éditeur de travail-\>onglet Flux de travail.

[En haut](#top.md)

## Quelle est la différence entre Clearance Height et Safe Height? 

Des informations plus détaillées sont disponible sur [Modèle: Profondeurs/Hauteurs](Template:Depths/Heights/fr.md).

[En haut](#top.md)

## Quelle est l\'utilisation habituelle de SetupSheet? 

Le SetupSheet est un masque de saisie dédié, contenu dans un Job, modifié dans la vue Property, seulement accessible depuis Path workbench. Il fournit une méthode pour configurer les éléments d\'un Job en utilisant les Values et les Expressions du SetupSheet aux utilisateurs experts.

Les entrées courantes pour Depths, Heights, et Tool Controllers comprennent:

1.  Final Depth Expression \-- OpFinalDepth
2.  Start Depth Expression \-- OpStartDepth
3.  Step Down Expression \-- Defaults to OpToolDiameter. Cette expression est utilisée à chaque Operation pour calculer les valeurs par défaut de descente (Step down) en fonction du diamètre de l\'outil (Tool) défini dans le gestionnaire d\'outils (Tool controller) associé.
4.  Clearance Height Expression \-- StartDepth+SetupSheet.ClearanceHeightOffset
5.  Clearance Height Offset Value \-- Contient la valeur utilisée dans Expressions
6.  Safe Height Expression \-- StartDepth+SetupSheet.SafeHeightOffset
7.  Safe Height Offset Value \-- Contient la valeur utilisée dans Expressions
8.  Horizontal Rapid Value \-- Fournit la valeur par défaut utilisée pour renseigner le taux d\'avance horizontale rapide (Horizontal Rapid Feed) pour tous les gestionnaires d\'outils.
9.  Vertical Rapid Value \-- Fournit la valeur par défaut utilisée pour renseigner le taux d\'avance verticale rapide (Vertical Rapid Feed) pour tous les gestionnaires d\'outils.

Cela permet d\'avoir de la flexibilité. Par exemple, les expressions par défaut sont fournies mais peuvent être modifiées par l\'utilisateur. La modification peut même réduire l\'équation par défaut à une Value si cela convient à l\'utilisateur.

[En haut](#top.md)

## Quelle est l\'utilisation habituelle de Job Templates? 

Job templates permet de sauvegarder les définitions de Job les plus communes et de les réutiliser pour les Jobs avec une configuration similaire.

[En haut](#top.md)

## Combien d\'objets de base sont pris en charge par l\'atelier Path? 

La prise en charge n\'existe que pour un seul objet de base. Pour créer des trajectoires pour plusieurs solides dans un seul travail, vous pouvez créer un composé à partir de ces solides et l\'utiliser comme objet de base pour le travail.

[En haut](#top.md)

## Pourquoi une opération ne produit-elle pas de résultats utilisables? 

Il existe une multitude de raisons qui peuvent faire qu\'une opération individuelle ne génère aucun résultat.

Une fréquente raison est que la géométrie de l\'outil définie dans le contrôleur d\'outils sélectionné pour l\'opération est trop grande pour s\'adapter à la géométrie sélectionnée sur le modèle 3D de l\'opération.

Sachez que cela se présente généralement sous la forme d\'un mouvement rapide vers le point de départ de l\'opération, complété par un mouvement rapide en Z vers la géométrie choisie pour définir l\'opération, puis par un retour à la hauteur de transit rapide.

Un autre malentendu courant est qu\'une opération de contour ne produit pas de trajectoires, alors que l\'opération de l\'éditeur de contour-\>Cut Side est \"Inside\", par défaut, et que le fait d\'activer la viabilité du modèle 3D permet de les voir.

[En haut](#top.md)

## L\'atelier Path peut-il effectuer des fraisages de surface en 3D? 

Oui, Path fournit des Operations de fraisage de surfaces 3D. Cela necessite l\'installation d\'OpenCamLibrary, un module Open Source d\'un fournisseur extérieur, dans le répertoire des fichiers de Macros.

OpenCamLibrary n\'est pas intégrée à FreeCAD pour s\'assurer qu\'aucune violation de licence ne se produise.

[En haut](#top.md)

## Que dois-je faire si les stratégies d\'opération par défaut ne répondent pas à mes besoins? 

Pour les Pocket Operations, le point de départ (Start Point) par défaut est en XYZ = 000 et est toujours validé mais il peut aussi être configuré dans la fenêtre Property. Les Operations Pocket et Facing sont pré-selectionnées en Climb plutôt qu\'en Cut Mode conventionnel dans l\'onglet Operation.

Pour les opérations de style Contour, l\'onglet Opération comporte une entrée \"Direction\" qui peut être configurée comme CW (sens horaire) ou CCW (anti sens horaire), ce qui définit la direction de la coupe. Pour référence :

1.  Cut Side = Extérieur, Cut Direction = CCW, coupe de montée
2.  Côté coupe = extérieur, direction de la coupe = CW, coupe conventionnelle
3.  Côté coupe = intérieur, sens de coupe = CW, coupe conventionnelle

Côté de coupe = intérieur, direction de la coupe = CCW, coupe de montée

Les points de départ peuvent être activés et configurés dans la fenêtre d\'affichage des propriétés.

Dans les opérations FaceMill, la tolérance de matériau peut être spécifiée, permettant le surdébit pour les valeurs positives et le sous-débit pour les valeurs négatives.

Dans les opérations de contour et de poche, le décalage supplémentaire sert le même objectif.

Ces entrées sont utiles, car elles permettent des fonctionnalités telles que

1.  Définir les passes d\'ébauche, en conjonction avec les champs de saisie des profondeurs.
2.  Spécifier la surcoupe pour les opérations de surfaçage.
3.  Les caractéristiques inférieures au diamètre de l\'outil, qui doivent être affrontées, peuvent bénéficier de la spécification d\'une coupe du contour extérieur avec une valeur négative de décalage supplémentaire.

Il convient de faire preuve d\'une grande prudence lors de la spécification des tolérances et des décalages de matériaux, au risque d\'effectuer des coupes non souhaitées dans le stock.

[En haut](#top.md)

## Que dois-je faire si une opération génère plus de mouvements verticaux que ce que mon poste peut tolérer? 

Les opérations telles que [Poche 3D](Path_Pocket_3D/fr.md), [Poche](Path_Pocket_Shape/fr.md) et [Surfaçage](Path_MillFace/fr.md) mais pas les opérations de contour, ont une option de configuration pour maintenir l\'outil vers le bas, dans l\'onglet Données de la vue Propriétés.

[En haut](#top.md)

## Comment puis-je laisser des attaches pour maintenir mes travaux de fraisage? 

L\'atelier Path fournit des [Attaches](Path_DressupTag/fr.md) à cette fin.

[En haut](#top.md)

## Qu\'est-ce qu\'un post-processeur? 

Le [post-processeur](Path_Post/fr.md) est utilisé pour adapter le code de sortie aux contrôleurs CNC cibles pour diverses machines dans leur langage en G-Code.

[En haut](#top.md)

## Puis-je modifier un post-processeur existant ou créer mon propre post-processeur? 

Les post-processeurs sont des scripts Python et sont enregistrés dans le chemin du fichier Macro. Ils sont destinés à être modifiés, ou utilisés comme modèle pour le développement ultérieur de post-processeurs.

[En haut](#top.md)

## Je ne veux utiliser qu\'un seul post-processeur. Puis-je en faire le post-processeur par défaut ou masquer les autres options? 

Oui, les [préférences de Path](Path_Preferences/fr.md) ont une section pour les post-processeurs où vous pouvez sélectionner les post-processeurs à afficher et sélectionner un post par défaut.

[En haut](#top.md)

## Comment puis-je définir les unités métriques/impériales pour mon objet trajectoire? 

Les unités du modèle 3D sont définies dans le menu déroulant Système utilisateur de l\'onglet Édition-\>Préférences\...\>Général-\>Unités.

Le paramètre des unités qui configure la façon dont la fraiseuse cible interprète le code G du travail est défini dans le post-processeur de sortie, qui insère une commande G20 ou G21 en code G pour indiquer les pouces ou les millimètres, respectivement.

Le post-processeur est également configuré pour les unités/seconde ou les unités/minute. S\'il est réglé sur Unités/Minute, la vitesse d\'avance du code interne du code G de l\'atelier Path est multipliée par 60.

Les disparités entre le modèle 3D et les paramètres du post-processeur sont probablement à l\'origine d\'erreurs d\'un facteur 60 pour la vitesse d\'avance et d\'un facteur 25,4 pour la distance.

[En haut](#top.md)

## Comment puis-je simuler mes stratégies de fraisage? 

Un simulateur volumétrique permet de visualiser le résultat de la découpe des géométries d\'outils incluses dans les opérations de travail sur le stock.

Si les lignes de trajectoire cachent le résultat de la simulation, leur visibilité doit être désactivée avant la simulation.

[En haut](#top.md)

## Quelle est la signification des couleurs des lignes des trajectoires? 

Les couleurs des lignes Path sont définies dans l\'onglet Édition-\>Préférence\...-\>Path-\>GUI\--\>Couleurs par défaut. Les couleurs par défaut incluent :

1.  Vert pour les trajectoires normales.
2.  Rouge pour les trajectoires rapides.
3.  Jaune pour les trajectoires sondées.

[En haut](#top.md)

## Comment puis-je activer/désactiver la visibilité des lignes des trajectoires? 

L\'atelier Path permet de contrôler l\'affichage des lignes des trajectoires en faisant basculer la visibilité de la tâche en la sélectionnant dans la [vue combinée](Combo_view/fr.md). La visibilité des opérations individuelles ou des groupes d\'opérations peut ensuite être modifiée à partir de la vue combinée.

[En haut](#top.md)

## Comment puis-je vérifier que ma séquence de code G est correcte? 

Par défaut, la sortie du post-processeur est affichée dans une fenêtre avant d\'être enregistrée. Cet outil, ainsi que le simulateur de FAO de trajectoire, permet d\'examiner le travail avant de le traiter sur une machine CNC. L\'outil d\'inspection du code G vous permet d\'inspecter le code G interne de Path pour chaque opération, ce qui permet de vérifier si la sortie du post-processeur reflète ce qui est défini dans l\'opération.

La liste des opérations du panneau Vue combinée affiche l\'ordre dans lequel les opérations seront traitées dans le travail. Si les opérations sont correctes, mais qu\'elles ne sont pas dans l\'ordre souhaité, vous pouvez les ajuster en double-cliquant sur la liste des opérations et en faisant glisser les opérations vers leur emplacement correct, ou en double-cliquant sur l\'éditeur de tâches et en sélectionnant l\'onglet Workflow, puis en utilisant les flèches Haut/Bas sur les opérations sélectionnées pour les trier.

[En haut](#top.md)

## Pourquoi mon post-processeur ne produit-il pas un code G correct pour les opérations insérées à l\'aide de la commande Partial-\>Custom? 

Communément, la commande Custom G-Code parce que le format est toujours en Unités/seconde, il peut causer des erreurs de facteur de 60 pour les cibles de machines CNC qui fonctionnent en Unités/minute.

[En haut](#top.md)

## Pourquoi les modifications apportées aux valeurs de placement dans la vue Propriétés ne semblent pas fonctionner correctement dans l\'atelier Path? 

\"Path contient aussi une propriété de Placement. Changer la valeur de ce placement modifiera la position dans la vue 3D, bien que l\'information Path elle-même, ne soit pas modifiée. La transformation est purement visuelle. Cela vous permet, par exemple, de créer un Path autour d\'une face qui a une orientation particulière sur votre modèle, qui n\'aura pas la même orientation que la matière première que vous positionnerez sur votre CNC.

Néanmoins, Path Compounds peut utiliser le Placement de ses enfants (voir ci-dessous).\"

[Path Ecrire un script](Path_scripting/fr.md).

[En haut](#top.md)

## Pourquoi l\'atelier Path de mon installation semble manquer de fonctionnalités que je vois dans les messages du forum d\'autres utilisateurs? 

Par défaut, la fonctionnalité Expérimentale est masquée dans l\'atelier Path.

[En haut](#top.md)

## Pourquoi les vidéos Youtube postées par les développeurs de l\'atelier Path semblent-elles désynchronisées par rapport à l\'atelier Path? 

L\'atelier Path a changé radicalement de FreeCAD v0.16 à v0.17, et toutes les vidéos postées avant le 1er janvier 2018 sont très susceptibles de contenir des informations qui ne sont plus en phase avec la v0.17 de l\'atelier Path de FreeCAD.

[En haut](#top.md)

## Pourquoi les arcs ne sont pas ronds mais sont constitués d\'un ensemble de lignes droites? 

Il s\'agit seulement un problème d\'affichage de la trajectoire. Vous pouvez modifier cela dans les préférences : chargez l\'atelier Path.

1.  ouvrez Préférences-\>Path-\>Job Preferences
2.  réglez les valeurs de *Default Geometry Tolerance* et *Default Curve Accuracy* à de petites valeurs mais pas à 0, par exemple à 0.01mm.
3.  confirmez le changement
4.  redémarrez FreeCAD.

[En haut](#top.md)





{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path FAQ/fr
