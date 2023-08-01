---
- GuiCommand:/fr
   Name:Ship Hydrostatics
   Name/fr:Ship Hydrostatiques
   MenuLocation:Ship design → Hydrostatics
   Workbenches:[Ship](Ship_Workbench/fr.md)
   Shortcut:
   SeeAlso:
---

# Ship Hydrostatics/fr

## Description

Trace l\'hydrostatique du bateau.

<img alt="" src=images/FreeCAD-Ship-HydrostaticsCurves.png  style="width:800px;"> 
*Exemple de courbes hydrostatiques*

Le calcul hydrostatique est une étape critique de la conception d\'un bateau, il permet de comprendre les principaux paramètres de stabilité sous-jacents de la coque.

Il s\'agit en effet de données obligatoires pour que le bateau soit certifié par les sociétés de classification. Combinées aux informations sur les conditions de charge, elles fournissent les informations les plus fondamentales sur la stabilité du bateau.

L\'atelier Ship trace l\'hydrostatique en 3 groupes principaux. Dans tous ces groupes, la courbe Δ(T) (rapport entre le déplacement et le tirant d\'eau) est représentée. Bien que de nombreuses autres hydrostatiques puissent être envisagées, elles peuvent être dérivées de celles déjà fournies, qui sont documentées ci-dessous.

### Hydrostatique basée sur le volume 

Il y a 3 hydrostatiques (malgré Δ(T)) inclus dans cette catégorie :

-   Surface mouillée (WSA).
-   Moment d\'inclinaison du bateau de 1 cm (MCT).
-   Position longitudinale du centre de bouyance (XCB).

En tant que quantité de surface en contact avec l\'eau, la WSA est fortement liée à la dynamique du bateau, y compris la résistance du bateau et la tenue à la mer. De plus, la WSA fait partie du facteur de renormalisation de nombreux coefficients non dimensionnels du bateau, comme le coefficient de traînée :

$c_\mathrm d = \dfrac{F_\mathrm d}{\dfrac{1}{2} \rho u^2 S},$

avec $F_\mathrm d$ la force de traînée, $\rho$ la densité de l\'eau, $u$ la vitesse du bateau et $S$ le WSA.

Le MCT joue un rôle majeur dans la planification des conditions de charge, car il donne des informations sur l\'effet du déplacement de toute charge le long du bateau. Le MCT réel est calculé en fonction de la distance transversale entre le centre de gravité et le métacentre, GML, ce qui nécessite évidemment la position du centre de gravité. Toutefois, comme il s\'agit d\'une pratique courante en architecture navale, la distance entre ce métacentre et le centre de flottabilité, BML, est considérée comme similaire à cette GML ($GML / BML \simeq 1$). Veuillez noter que cela n\'est valable que pour la direction longitudinale ($GMT / BMT \neq 1$).

Parfois, le BML est préféré au MCT. Si c\'est votre cas, il vous suffit de faire une demande.

$BML = \dfrac{100 \,\, L \,\, MCT}{\Delta},$

avec $L$ la longueur en mètres et $\Delta$ le déplacement.

Le XCB indique de toute évidence l\'angle d\'inclinaison qui devrait permettre au bateau d\'avancer en fonction de la répartition du poids.

### Hydrostatique de la stabilité 

Ces hydrostatiques sont davantage liées à la stabilité transversale du bateau. Les hydrostatiques suivantes sont fournies par l\'atelier des bateaux :

-   Surface de flottaison/aire de flottaison (WP).
-   Distance entre la quille et le centre de bouée (KB).
-   Distance entre le centre de bouée et le métacentre (BMT)

La surface de flottaison est largement liée à ce que l\'on appelle la rigidité hydrostatique, ou en d\'autres termes la résistance présentée par le bateau à toute perturbation.

D\'autre part, le KB et le BMT sont des paramètres critiques pour déterminer la stabilité transversale du bateau pour les petits angles. En effet, lorsque le centre de gravité est défini (cela peut être fait avec les outils [Ship Poids](Ship_Weight/fr.md), [Ship Réservoir](Ship_Tank/fr.md) et [Ship Charge](Ship_LoadCondition/fr.md)), le principal paramètre de stabilité pour les petits angles peut être facilement calculé,

$GMT = KB + BMT - KG.$

Ce paramètre doit en effet avoir une valeur minimale qui dépend du type et de la taille du bateau, et sera donc interrogé par les sociétés de classification.

### Coefficients

Certains coefficients sont généralement pris en compte dès les premières étapes de la conception d\'un bateau pour évaluer la qualité de la surface du bateau, ou en d\'autres termes, son comportement hydrodynamique.

-   Coefficient de blocage (Cb).
-   Coefficient de flottement (Cf).
-   Coefficient de trame principale (Cm).

Cb est le rapport entre le volume de la partie immergée du bateau et le volume de sa boîte englobante, c\'est-à-dire la plus petite boîte pouvant contenir le bateau. Cm et Cf sont ses équivalents en 2D, devenant le rapport Cm entre la surface de la structure principale du bateau et sa boîte de délimitation, et Cf le rapport entre la surface du plan d\'eau et sa boîte de délimitation.

Alors que de grandes valeurs de Cb entraîneront inexorablement des bateaux inefficaces, avec des valeurs de Cb plus modérées, il est nécessaire de combiner les informations avec Cm et Cf. De grandes valeurs de Cf indiquent une grande empreinte à la surface de l\'eau, ce qui indique généralement une grande résistance du bateau due à la génération de vagues. Au contraire, plus Cm est grand, plus le volume du corps du bateau est concentré sur la partie centrale, et donc des formes fines peuvent être attendues à l\'avant et à l\'arrière, ce qui est généralement bon pour l\'hydrodynamique.

## Utilisation

Pour calculer la courbe des aires transversales, sélectionnez une **instance de bateau** (voir [Ship CreateShip](Ship_CreateShip/fr.md)), et lancez **Ship design → <img src="images/Ship_Hydrostatics.svg" width=16px> Hydrostatics**.

Le panneau des tâches s\'affiche. Vous devez sélectionner l\'angle d\'assiette ainsi que la plage de tirants d\'eau à prendre en compte. Vous pouvez également sélectionner le nombre d\'échantillons à prélever entre le tirant d\'eau minimum et maximum. Plus le nombre d\'échantillons est important, plus le calcul sera long.

Appuyez sur le bouton **Accept** lorsque vous êtes prêt, afin que le module bateau commence le calcul. Pendant le calcul, FreeCAD devient presque sans réponse. Il trace cependant les informations en temps réel, ainsi qu\'une barre de progression du processus. Vous pouvez passer à un autre onglet de tracé, ou arrêter le calcul en appuyant sur le bouton **Cancel**. Soyez patient car ces actions seront exécutées juste après la fin du calcul de l\'échantillon suivant.

## Tutoriels

-   [Tutoriel Construction navale S60](FreeCAD-Ship_s60_tutorial/fr.md)
-   [Tutoriel Construction navale S60 (II)](FreeCAD-Ship_s60_tutorial_(II)/fr.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Ship](Category_Ship.md) > Ship Hydrostatics/fr
