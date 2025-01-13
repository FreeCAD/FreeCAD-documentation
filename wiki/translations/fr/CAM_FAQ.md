# CAM FAQ/fr
## Combien d\'axes l\'atelier CAM peut-il traiter? 

Pour le moment, CAM Workbench peut gérer jusqu\'à 3 axes de fraisage. Actuellement, les capacités du 4ème axe ne sont pas officiellement incluses mais il existe des [expérimentations](CAM_fourth_axis/fr.md). 

## L\'atelier CAM supporte-t-il l\'usinage au tour ? 

Actuellement, l\'atelier CAM ne prend pas directement en charge les opérations sur tour, mais l\'extension [TurningAddon](https://github.com/dubstar-04/TurningAddon) peut être installé et utilise la bibiliothèque Python [LibLathe](https://github.com/dubstar-04/LibLathe). Pour plus d\'informations, consultez [ce fil de discussion](https://forum.freecad.org/viewtopic.php?t=30563). 

## Pourquoi semble-t-il que, dans certains cas, l\'atelier CAM propose plus d\'une façon de décrire une opération? 

L\'atelier CAM fournit des outils pour répondre à de nombreuses opérations de fraisage et, comme FreeCAD est un logiciel libre, rien n\'empêche un utilisateur de créer ses propres fonctionnalités.

Dans le dessin 3D, il existe souvent plusieurs méthodes disponibles qui peuvent être avantageuses à utiliser pour des opérations Job différents. Dans certains cas, des combinaisons d\'opérations sont utilisées pour fournir un fraisage complet du Stock.

Un exemple habituel est que l\'opération Contour peut être générée depuis Edges ou Faces. Dans certains cas, il peut y avoir un avantage à utiliser l\'une ou l\'autre des méthodes. 

## Pourquoi l\'habillage d\'une opération modifie-t-il la position dans le flux de travail affiché dans la liste des opérations? 

Tous les ajouts au travail, y compris les modifications et les copies d\'opérations, sont ajoutés à la fin du flux de travail du travail. Si cela perturbe la séquence correcte du travail, elle doit être réorganisée dans l\'éditeur de travail-\>onglet Flux de travail. 

## Quelle est la différence entre Clearance Height et Safe Height? 

Des informations plus détaillées sont disponible ici [Hauteurs et profondeurs](CAM_Workbench/fr#Hauteurs_et_profondeurs.md). 

## Quelle est l\'utilisation habituelle de SetupSheet? 

La [feuille de configuration](CAM_SetupSheet/fr.md) est une feuille de calcul spécifique, contenue dans une tâche, modifié dans la vue Propriétés, seulement accessible depuis l\'atelier CAM. Elle fournit une méthode pour configurer les éléments d\'une tâche en utilisant des valeurs et des expressions de la [feuille de configuration](CAM_SetupSheet/fr.md) aux utilisateurs experts.

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

## Quelle est l\'utilisation habituelle de Job Templates? 

Job templates permet de sauvegarder les définitions de Job les plus communes et de les réutiliser pour les Jobs avec une configuration similaire. 

## Combien d\'objets de base sont pris en charge par l\'atelier CAM? 

La prise en charge n\'existe que pour un seul objet de base. Pour créer des trajectoires pour plusieurs solides dans un seul travail, vous pouvez créer un composé à partir de ces solides et l\'utiliser comme objet de base pour le travail. 

## Pourquoi une opération ne produit-elle pas de résultats utilisables? 

Il existe une multitude de raisons qui peuvent faire qu\'une opération individuelle ne génère aucun résultat.

Une fréquente raison est que la géométrie de l\'outil définie dans le contrôleur d\'outils sélectionné pour l\'opération est trop grande pour s\'adapter à la géométrie sélectionnée sur le modèle 3D de l\'opération.

Sachez que cela se présente généralement sous la forme d\'un mouvement rapide vers le point de départ de l\'opération, complété par un mouvement rapide en Z vers la géométrie choisie pour définir l\'opération, puis par un retour à la hauteur de transit rapide.

Un autre malentendu courant est qu\'une opération de contour ne produit pas de trajectoires, alors que l\'opération de l\'éditeur de contour-\>Cut Side est \"Inside\", par défaut, et que le fait d\'activer la viabilité du modèle 3D permet de les voir. 

## L\'atelier CAM peut-il effectuer des fraisages de surface en 3D? 

Oui, CAM fournit des Operations de fraisage de surfaces 3D. Cela necessite l\'installation d\'OpenCamLibrary, un module open source dans le répertoire des fichiers de Macros.

OpenCamLibrary n\'est pas intégrée à FreeCAD pour s\'assurer qu\'aucune violation de licence ne se produise. 

## Que dois-je faire si les stratégies d\'opération par défaut ne répondent pas à mes besoins? 

Pour les Pocket Operations, le point de départ (Start Point) par défaut est en XYZ = 000 et est toujours validé mais il peut aussi être configuré dans la fenêtre Property. Les Operations Pocket et Facing sont pré-selectionnées en Climb plutôt qu\'en Cut Mode conventionnel dans l\'onglet Operation.

Pour les opérations de style Contour, l\'onglet Opération comporte une entrée \"Direction\" qui peut être configurée comme CW (sens horaire) ou CCW (anti sens horaire), ce qui définit la direction de la coupe. Pour référence :

1.  Cut Side = Extérieur, Cut Direction = CCW, coupe de montée
2.  Côté coupe = extérieur, direction de la coupe = CW, coupe conventionnelle
3.  Côté coupe = intérieur, sens de coupe = CW, coupe conventionnelle
4.  Côté de coupe = intérieur, direction de la coupe = CCW, coupe de montée

Les points de départ peuvent être activés et configurés dans la fenêtre d\'affichage des propriétés.

Dans les opérations FaceMill, la tolérance de matériau peut être spécifiée, permettant le surdébit pour les valeurs positives et le sous-débit pour les valeurs négatives.

Dans les opérations de contour et de poche, le décalage supplémentaire sert le même objectif.

Ces entrées sont utiles, car elles permettent des fonctionnalités telles que

1.  Définir les passes d\'ébauche, en conjonction avec les champs de saisie des profondeurs.
2.  Spécifier la surcoupe pour les opérations de surfaçage.
3.  Les caractéristiques inférieures au diamètre de l\'outil, qui doivent être affrontées, peuvent bénéficier de la spécification d\'une coupe du contour extérieur avec une valeur négative de décalage supplémentaire.

Il convient de faire preuve d\'une grande prudence lors de la spécification des tolérances et des décalages de matériaux, au risque d\'effectuer des coupes non souhaitées dans le stock. 

## Que dois-je faire si une opération génère plus de mouvements verticaux que ce que mon poste peut tolérer? 

Les opérations telles que [Poche 3D](CAM_Pocket_3D/fr.md), [Poche](CAM_Pocket_Shape/fr.md) et [Surfaçage](CAM_MillFace/fr.md) mais pas les opérations de contour, ont une option de configuration pour maintenir l\'outil vers le bas, dans l\'onglet Données de la vue Propriétés. 

## Comment puis-je laisser des attaches pour maintenir mes travaux de fraisage? 

L\'atelier CAM fournit des [Attaches](CAM_DressupTag/fr.md) à cette fin. 

## Qu\'est-ce qu\'un post-processeur? 

Le [post-processeur](CAM_Post/fr.md) est utilisé pour adapter le code de sortie aux contrôleurs CNC cibles pour diverses machines dans leur langage en G-Code. 

## Puis-je modifier un post-processeur existant ou créer mon propre post-processeur? 

Les post-processeurs sont des scripts Python et sont enregistrés dans le chemin du fichier Macro. Ils sont destinés à être modifiés, ou utilisés comme modèle pour le développement ultérieur de post-processeurs. 

## Je ne veux utiliser qu\'un seul post-processeur. Puis-je en faire le post-processeur par défaut ou masquer les autres options? 

Oui, les [préférences de CAM](CAM_Preferences/fr.md) ont une section pour les post-processeurs où vous pouvez sélectionner les post-processeurs à afficher et sélectionner un post par défaut. 

## Comment puis-je définir les unités métriques/impériales pour mon objet trajectoire? 

Les unités du modèle 3D sont définies dans le menu déroulant Système utilisateur de l\'onglet Édition-\>Préférences\...\>Général-\>Unités.

Le paramètre des unités qui configure la façon dont la fraiseuse cible interprète le code G du travail est défini dans le post-processeur de sortie, qui insère une commande G20 ou G21 en code G pour indiquer les pouces ou les millimètres, respectivement.

Le post-processeur est également configuré pour les unités/seconde ou les unités/minute. S\'il est réglé sur Unités/Minute, la vitesse d\'avance du code interne du code G de l\'atelier CAM est multipliée par 60.

Les disparités entre le modèle 3D et les paramètres du post-processeur sont probablement à l\'origine d\'erreurs d\'un facteur 60 pour la vitesse d\'avance et d\'un facteur 25,4 pour la distance. 

## Comment puis-je simuler mes stratégies de fraisage? 

Un simulateur volumétrique permet de visualiser le résultat de la découpe des géométries d\'outils incluses dans les opérations de travail sur le stock.

Si les lignes de trajectoire cachent le résultat de la simulation, leur visibilité doit être désactivée avant la simulation. 

## Quelle est la signification des couleurs des lignes des trajectoires? 

Les couleurs des lignes de CAM sont définies dans l\'onglet Édition -\> Préférence\... -\> CAM -\> GUI -\> Couleurs par défaut. Les couleurs par défaut incluent :

1.  Vert pour les trajectoires normales.
2.  Rouge pour les trajectoires rapides.
3.  Jaune pour les trajectoires sondées.


{{Top}}



## Comment puis-je activer/désactiver la visibilité des lignes des trajectoires? 

L\'atelier CAM permet de contrôler l\'affichage des lignes des trajectoires en faisant basculer la visibilité de la tâche en la sélectionnant dans la [vue combinée](Combo_view/fr.md). La visibilité des opérations individuelles ou des groupes d\'opérations peut ensuite être modifiée à partir de la vue combinée. 

## Comment puis-je vérifier que ma séquence de code G est correcte? 

Par défaut, la sortie du post-processeur est affichée dans une fenêtre avant d\'être enregistrée. Cet outil, ainsi que le simulateur de FAO de parcours, permet d\'examiner le travail avant de le traiter sur une machine CNC. L\'outil d\'inspection du code G vous permet d\'inspecter le code G interne de CAM pour chaque opération, ce qui permet de vérifier si la sortie du post-processeur reflète ce qui est défini dans l\'opération.

La liste des opérations du panneau Vue combinée affiche l\'ordre dans lequel les opérations seront traitées dans le travail. Si les opérations sont correctes, mais qu\'elles ne sont pas dans l\'ordre souhaité, vous pouvez les ajuster en double-cliquant sur la liste des opérations et en faisant glisser les opérations vers leur emplacement correct, ou en double-cliquant sur l\'éditeur de tâches et en sélectionnant l\'onglet Workflow, puis en utilisant les flèches Haut/Bas sur les opérations sélectionnées pour les trier. 

## Pourquoi mon post-processeur ne produit-il pas un code G correct pour les opérations insérées à l\'aide de la commande Partial-\>Custom? 

Communément, la commande Custom G-Code parce que le format est toujours en Unités/seconde, il peut causer des erreurs de facteur de 60 pour les cibles de machines CNC qui fonctionnent en Unités/minute. 

## Pourquoi les modifications apportées aux valeurs de placement dans la vue Propriétés ne semblent pas fonctionner correctement dans l\'atelier CAM? 

Un parcours contient aussi une propriété de Placement. Changer la valeur de ce placement modifiera la position dans la vue 3D, bien que l\'information du parcours elle-même, ne soit pas modifiée. La transformation est purement visuelle. Cela vous permet, par exemple, de créer un parcours autour d\'une face qui a une orientation particulière sur votre modèle, qui n\'aura pas la même orientation que la matière première que vous positionnerez sur votre CNC.

Néanmoins, Path Compounds peut utiliser le Placement de ses enfants (voir ci-dessous).\"

[CAM Ecrire un script](CAM_scripting/fr.md). 

## Pourquoi l\'atelier CAM de mon installation semble manquer de fonctionnalités que je vois dans les messages du forum d\'autres utilisateurs? 

Par défaut, la fonction Expérimentale est masquée dans l\'atelier CAM. 

## Pourquoi les vidéos Youtube postées par les développeurs de l\'atelier CAM semblent-elles désynchronisées par rapport à l\'atelier CAM? 

L\'atelier CAM a changé radicalement de FreeCAD v0.16 à v0.17, et toutes les vidéos postées avant le 1er janvier 2018 sont très susceptibles de contenir des informations qui ne sont plus en phase avec la v0.17 de l\'atelier CAM de FreeCAD. 

## Pourquoi les arcs ne sont pas ronds mais sont constitués d\'un ensemble de lignes droites? 

Il s\'agit seulement un problème d\'affichage du parcours. Vous pouvez modifier cela dans les préférences : chargez l\'atelier CAM.

1.  ouvrez Préférences -\> CAM -\> Préférences des tâches
2.  réglez les valeurs de *Tolérance des géométries par défaut* et *Précision des courbes par défaut* à de petites valeurs mais pas à 0, par exemple à 0.01mm.
3.  confirmez le changement
4.  redémarrez FreeCAD.


{{Top}}





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM FAQ/fr
