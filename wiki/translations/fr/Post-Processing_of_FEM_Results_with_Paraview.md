---
- TutorialInfo:/fr
   Topic:Post-traitement des résultats FEM avec Paraview
   Level:Intermédiaire
   Time:120 minutes
   Author:[http://www.freecadweb.org/wiki/index.php?title=User: HarryvL]
   FCVersion:0.19
   Files:[https://forum.freecadweb.org/download/file.php?id=103403 beam] et [https://forum.freecadweb.org/download/file.php?id=103557 wall] dans ce [https://forum.freecadweb.org/viewtopic.php?f=18&t=37253&start=10#p367734 fil du forum Freecad]
---

# Post-Processing of FEM Results with Paraview/fr





## Introduction

Certains messages et tutoriels sur le forum utilisent Paraview pour examiner et analyser les résultats de l\'<img alt="" src=images/_Workbench_FEM.svg  style="width:24px;"> [atelier FEM](FEM_Workbench/fr.md) de FreeCAD. Ce tutoriel explique les bases du transfert de données de l\'atelier FEM vers Paraview et montre certaines des options et des paramètres d\'affichage des données.



## Prérequis

-   FreeCAD utilisant une version compatible avec la version désignée de ce tutoriel.
-   [Paraview](https://www.paraview.org) sera téléchargé directement depuis son [site web](https://www.paraview.org/download/) ou votre gestionnaire de paquets préféré.
    -   Ce tutoriel est basé sur la version Paraview 5.8.0 pour Windows, qui était la version la plus récente au moment de la rédaction du tutoriel.
-   Les fichiers FreeCAD utilisés pour ce tutoriel sont disponibles dans [ici](https://forum.freecadweb.org/viewtopic.php?f=18&t=37253&start=10#p367734) et [ici](https://forum.freecadweb.org/viewtopic.php?f=18&t=37253&p=368315#p368315), fil de discussion FreeCAD.



## Transfert de données depuis l\'atelier FEM 

Dans l\'atelier FEM, mettez en surbrillance l\'objet CCX_Results. Ensuite, utilisez l\'option de menu **Fichier > Exporter > FEM result VTK (*.vtk *.vtu)** pour exporter les données VTK.



## Importation de données dans Paraview 

L\'écran de démarrage affiche un navigateur de pipeline vide. C\'est là que les objets de données VTK importés et les objets de filtre appliqués (pour la géométrie ou les données) seront visibles.

<img alt="" src=images/PVPic1.png  style="width:500px;">

Utilisez l\'option de menu **File > Open > *.vtk** pour ouvrir le fichier VTK généré avec l\'atelier FEM.

<img alt="" src=images/PVPic2.png  style="width:500px;">

Appuyez sur **Apply** dans l\'onglet des propriétés. Par défaut, cela affichera une vue de dessus (en regardant le long de l\'axe z) de la géométrie.

<img alt="" src=images/PVPic3.png  style="width:400px;"> \... <img alt="" src=images/PVPic0.png  style="width:550px;">

La géométrie grise peut être inspectée en faisant pivoter la vue. Le bouton gauche de la souris fait pivoter la géométrie, mais malheureusement d\'une manière difficile à contrôler (par rapport à FreeCAD). Pour obtenir une rotation prévisible, maintenez la touche **X**, **Y** ou **Z** enfoncée tout en faisant glisser la souris avec le bouton gauche de la souris enfoncé pour faire pivoter le modèle autour de X, Y ou Axe Z, respectivement.

<img alt="" src=images/PVPic5.png  style="width:500px;"> 

## Sauvegarde/état de chargement 

Plutôt que d\'enregistrer des données, Paraview stocke le statut (état) des actions effectuées sur l\'objet VTK importé. Par conséquent, pour enregistrer votre travail, utilisez l\'option de menu **File > Save State**. **REMARQUE**: il n\'y aura pas d\'avertissement lorsque vous quittez Paraview pour enregistrer l\'état et tout le travail peut être perdu à la sortie du programme.

Pour continuer là où vous vous étiez arrêté lors de la session précédente, utilisez **File > Load State**. Cela invite l\'utilisateur à spécifier un fichier VTK, ce qui signifie que les actions effectuées dans la dernière session peuvent également être appliquées à un nouveau fichier VTK. De cette façon, les données de différentes analyses de l\'atelier FEM peuvent être affichées exactement de la même manière, sans effort supplémentaire.



## Visualiser les résultats de l\'atelier FEM 

Paraview propose de nombreuses options et paramètres pour afficher les résultats. Nous allons d\'abord regarder l\'affichage des données d\'importation de base sur la géométrie d\'origine et voir ensuite comment appliquer des filtres pour modifier la géométrie. Enfin, nous utiliserons la calculatrice et les filtres d\'intégration pour dériver de nouveaux résultats en combinant les données d\'importation de base.



## Données de base affichées sur la géométrie d\'origine 

Étant donné que le navigateur de pipeline peut contenir plusieurs objets VTK et objets de filtre, vérifiez d\'abord que l\'objet VTK de droite est mis en surbrillance dans le navigateur de pipeline. Les sélections et les paramètres d\'affichage de cet objet VTK se trouvent désormais dans l\'onglet Propriétés. Pour vous assurer que tous les paramètres sont visibles et alignés avec ce didacticiel, appuyez sur le bouton Paramètres avancés (l\'icône de la roue dentée sur l\'image ci-dessous).

<img alt="" src=images/PVPic6.png  style="width:400px;">

Le premier paramètre que nous pouvons changer est la façon dont les données sont présentées sur la géométrie. Cela se fait dans le menu déroulant Représentation. Pour l\'instant, nous n\'utiliserons que l\'option Surface ou Wireframe.

<img alt="" src=images/PVPic7.png  style="width:400px;">

Jusqu\'à présent, aucun résultat n\'est affiché. Pour cela, nous devons changer l\'option de coloration. La valeur par défaut est Solid Color, mais le menu déroulant affiche toutes les données scalaires disponibles dans le fichier VTK importé.

<img alt="" src=images/PVPic8.png  style="width:400px;">

<img alt="" src=images/PVPic9.png  style="width:400px;">

Pour les besoins de ce tutoriel, nous avons choisi ReinforcementRatio_x, mais il est facile de le changer par n\'importe quel type de données.

La fenêtre RenderView affichera maintenant un iso-plot du type de données sélectionné et une légende de couleur de la plage de données.

<img alt="" src=images/PVPic10.png  style="width:700px;">

La légende des couleurs peut être déplacée à un emplacement plus pratique et changera d\'orientation à l\'approche des bords de la fenêtre.

<img alt="" src=images/PVPic11.png  style="width:700px;">

Il est également possible de contrôler les paramètres de la légende des couleurs de manière très détaillée en ouvrant la boîte de dialogue Modifier les propriétés de la légende des couleurs à partir de l\'onglet Propriétés (cliquez sur la dernière icône à droite).

<img alt="" src=images/PVPic12.png  style="width:400px;">

Cela ouvre la fenêtre suivante pour les paramètres de légende des couleurs.

<img alt="" src=images/PVPic13.png  style="width:400px;">

La coloration de la carte iso peut être contrôlée via l\'éditeur de carte de couleurs qui est activée en appuyant sur le bouton Edit de l\'onglet Propriétés:

<img alt="" src=images/PVPic12.png  style="width:300px;"> . <img alt="" src=images/PVPic15.png  style="width:300px;">

Le paramètre de discrétisation des couleurs est utile pour limiter le nombre de valeurs iso, créant ainsi des plages plus pratiques pour la conception. Le nombre de plages par défaut est 256, mais ici, le nombre est fixé à 10.

<img alt="" src=images/PVPic16.png  style="width:700px;"> 

## Application de filtres aux résultats de l\'atelier FEM 

Pour modifier les données de base ou la géométrie importée de l\'atelier FEM, des filtres peuvent être appliqués.

Ici, seuls les filtres Slice et Warp seront discutés. Les filtres permettant de créer des résultats composés à partir des données de base seront abordés dans la section suivante.

Pour appliquer le filtre Slice, mettez en surbrillance l\'objet VTK qui doit être tranché et appuyez sur l\'icône Slice. Vous pouvez également trouver le filtre Slice dans le menu Filters \> Alphabetical. Cela ajoute l\'objet filtre Slice au navigateur de pipeline et l\'emplacement dans l\'arborescence montre qu\'il est appliqué à l\'objet VTK. La position dans l\'arborescence est importante, car les filtres peuvent être appliqués à différents objets VTK ou même à d\'autres objets de filtre. L\'objet filtre ne peut pas être déplacé dans l\'arborescence pour modifier l\'objet auquel il s\'applique. L\'objet cible ne peut être modifié que par le menu (ou en cliquant avec le bouton droit) sur l\'option Edit \> Change Input.

<img alt="" src=images/PVPic17.png  style="width:700px;">

L\'emplacement et l\'orientation de la tranche peuvent être modifiés en faisant glisser la tranche et son vecteur normal avec la souris ou via l\'onglet Propriétés. Dans la figure ci-dessous, l\'origine de la tranche a été placée au centre de la poutre (au-dessus du support central) et la normale au plan pointe dans la direction x.

<img alt="" src=images/PVPic18.png  style="width:400px;">

Pour vous débarrasser des boîtes englobantes, désélectionnez Show Plane box en haut de la boîte de dialogue Paramètres du plan.

<img alt="" src=images/PVPic19.png  style="width:700px;">

Le filtre Warp by Vector peut être utilisé pour afficher la géométrie déformée. Mettez en surbrillance l\'objet VTK et appuyez sur l\'icône Warp by Vector. Cela ajoute le filtre au Pipeline Browser. Vous pouvez également rechercher le filtre dans le menu Filters \> Alphabetical. Sélectionnez ensuite Déplacement dans le menu déroulant Vectors de l\'onglet Propriétés et définissez un facteur d\'échelle approprié. N\'oubliez pas d\'appuyer sur le bouton Appliquer après avoir modifié les paramètres.

<img alt="" src=images/PVPic20.png  style="width:400px;"> . <img alt="" src=images/PVPic21.png  style="width:700px;">

La valeur de déplacement maximum est de 0,98 mm.

Pour afficher la géométrie déformée superposée à la géométrie non déformée, il suffit de rendre visible à la fois l\'objet VTK et l\'objet filtre Warp en cliquant sur l\'icône en forme d\'œil à côté. Dans l\'image suivante, le paramètre de représentation de l\'objet VTK a été modifié en filaire et l\'opacité réduite à 0,5 pour l\'empêcher d\'obscurcir la géométrie déformée.

<img alt="" src=images/PVPic22.png  style="width:700px;">

**REMARQUE**: à mesure que davantage d\'objets sont ajoutés au Pipeline Browser et que davantage de fenêtres d\'affichage sont ouvertes, il devient de plus en plus important de s\'assurer que le bon objet est sélectionné dans le Pipeline Browser et que la fenêtre de droite est mise au point lors de la modification de l\'onglet Propriétés. Sinon, beaucoup de temps peut être consacré à la recherche de la bonne propriété ou les modifications apportées aux propriétés peuvent ne pas prendre effet.



## Application de filtres pour dériver les résultats composés des données d\'importation de base 

Si nous voulons connaître la quantité d\'acier d\'armature dans la poutre dans son ensemble ou la quantité passant à travers une section particulière, nous devons effectuer l\'intégration (sommation sur la géométrie) des données de base.

Par exemple, le volume total des barres d\'armature dans la poutre s\'étendant dans la direction x est obtenu à partir de l\'intégrale `INTEGRATE(ReinforcementRatio_x * dx * dy * dz)` sur toute la géométrie et la surface totale de l\'acier d\'armature en cours d\'exécution bien qu\'une section efficace particulière du beam soit obtenue à partir de `INTEGRATE(ReinforcementRatio_x * dy * dz)` sur une tranche.

Dans Paraview, l\'intégration peut être effectuée avec un filtre d\'intégration. Ce filtre peut être appliqué à l\'ensemble de l\'objet VTK (le beam) ou à une tranche (la section transversale).

REMARQUE: en raison d\'une incompatibilité de l\'ordre des nœuds entre Freecad FEM et Paraview, l\'intégration sur un volume donne des résultats négatifs, c\'est-à-dire `INTEGRATE( 1.0 * dx * dy *dz)` = -Volume au lieu de + Volume.

Pour calculer les intégrales, nous devons appliquer un filtre d\'intégration, qui se trouve dans l\'élément de menu Filters \> Alphabetical. Mettez en surbrillance l\'objet VTK et appliquez le filtre.

<img alt="" src=images/PVPic23.png  style="width:700px;">

Appuyez sur le bouton **Apply** dans l\'onglet Propriétés et les résultats s\'ouvriront dans une fenêtre distincte à droite de l\'aperçu du rendu.

<img alt="" src=images/PVPic24.png  style="width:700px;">

Avant de ranger cela pour trouver le résultat souhaité, c\'est-à-dire `INTEGRATE(ReinforcementRatio_x * dx * dy * dz)`, voyons d\'abord comment nous pouvons contrôler où la fenêtre est placée et ce qu\'elle contient.

Fermez d\'abord la fenêtre SpreadSheetView qui s\'est ouverte à droite. Appuyez ensuite sur l\'icône de fractionnement horizontal dans la fenêtre Renderview et une nouvelle fenêtre s\'ouvrira avec un menu d\'options d\'affichage. Avant de sélectionner une option, assurez-vous que l\'objet de filtre d\'intégration est mis en surbrillance dans le Pipeline Browser.

<img alt="" src=images/PVPic25.png  style="width:700px;">

Pour afficher les résultats numériques, nous devons sélectionner SpreadSheet View au bas de la liste Create View. Cela génère une feuille de calcul de tous les résultats disponibles dans l\'objet VTK intégré sur le volume.

<img alt="" src=images/PVPic26.png  style="width:400px;">

Pour inspecter `INTEGRATE(ReinforcementRatio_x * dx * dy * dz)`, nous pouvons faire défiler vers la droite le tableau, mais nous pouvons également supprimer tous les résultats indésirables en les désélectionnant, c\'est-à-dire désélectionner toutes les colonnes et sélectionner **ReinforcementRatio_x**.

<img alt="" src=images/PVPic27.png  style="width:300px;"> . <img alt="" src=images/PVPic28.png  style="width:500px;">

Il ne nous reste plus qu\'une seule valeur dans le tableau des résultats de l\'intégration.

<img alt="" src=images/PVPic29.png  style="width:300px;">

Comme expliqué précédemment, c\'est la valeur négative de l\'intégrale que nous recherchons. Ainsi, le volume total indicatif d\'acier requis dans la direction x est de 2.27e+06 mm3 (= 2272 cm3) or 2272 cm3 \* 7.6 g/cm3 = 17267 g (= 17.3 kg). En pratique, le nombre sera plus élevé en raison de considérations pratiques (par exemple, les exigences d\'ancrage, les exigences minimales de renforcement, etc.). Néanmoins, ce résultat peut être utilisé pour comparer des conceptions conceptuelles

Ce qui précède était un exemple de l\'intégration d\'une variable directement exportée par l\'atelier FEM. Dans certains cas, nous pouvons vouloir combiner des variables VTK pour obtenir de nouveaux résultats. Cela peut être fait de plusieurs manières, mais ici je ne discuterai que des plus simples, c\'est-à-dire avec le Calculator Filter.

Par exemple, si nous voulons connaître le besoin total de renfort dans les trois directions de coordonnées, nous devons additionner ReinforcementRatio_x, ReinforcementRatio_y et ReinforcementRatio_z.

Le Calculator filter se trouve sous forme d\'icône à gauche de la barre de filtre ou via le menu Filters \> Alphabetical. Le nom de la variable résultante peut être entré dans le champ Nom du tableau de résultats. Ici, nous appelons le résultat Total_Reinforcement_Ratio. La formule peut être composée dans la zone située sous le champ Result Array Name. Les valeurs d\'entrée peuvent être sélectionnées dans le menu déroulant Scalars et peuvent être combinées dans une formule pour le résultat en utilisant les opérateurs donnés. Après avoir appuyé sur le bouton Apply, le résultat sera disponible en tant que nouvelle variable dans toutes les opérations suivantes (par exemple, un filtre d\'intégration) ou vues (par exemple RenderView ou SpreadSheetView, voir ci-dessous).

<img alt="" src=images/PVPic30.png  style="width:700px;">

Par exemple, nous pouvons maintenant appliquer le filtre d\'intégration à la nouvelle variable Total Reinforcement Ratio.

<img alt="" src=images/PVPic31.png  style="width:700px;">

Cela montre comment l\'exigence d\'armature totale se compare à celles des directions de coordonnées individuelles.



## Intégration sur une tranche 

Dans la section précédente, nous avons discuté du filtre d\'intégration et de son application à l\'ensemble de l\'objet VTK. Pour démontrer l\'intégration sur une tranche, nous allons dans cette section déterminer le besoin total de ferraillage et son centre de gravité pour la section centrale de la poutre. Le résultat final est illustré dans l\'image ci-dessous. L\'interaction de divers objets peut être inspectée dans le Pipeline Browser. Le filtre de tranche est appliqué à l\'objet poutre VTK et deux filtres Calculator sont appliqués au filtre de tranche pour dériver les nouvelles variables \"Reinforcement_ratio_x \* z\" et \"Reinforcement_ratio_x \* y\" des données de base. Ces variables doivent être intégrées pour déterminer le centre de gravité de l\'armature. Enfin, des filtres d\'intégration sont appliqués à chaque Calculator pour intégrer les résultats sur la tranche. Veuillez vous référer à la section précédente pour une présentation générale du filtre d\'intégration et de ses paramètres.

<img alt="" src=images/PVPicSlice1.png  style="width:700px;">

Appliquez les paramètres suivants dans l\'onglet Propriétés de l\'objet VTK:

  Paramètres de l\'onglet Propriétés   Commentaire
   
  Representation: Wireframe            Ainsi, la tranche est visible
  Coloring: ReinforcementRatio_x       Ou toute autre couleur
  Styling \> Line Width: 2             Ou tout autre paramètre qui donne un résultat agréable

<img alt="" src=images/PVPicSlice2.png  style="width:400px;">

Mettez ensuite en surbrillance l\'objet VTK et appliquez un filtre Slice (tranche) avec les paramètres suivants dans l\'onglet Propriétés:

  Paramètres de l\'onglet Propriétés             Commentaire
   
  Plane Parameters \> Show Plane: deselect       Supprimer les boîtes englobantes
  Plane Parameters \> Origin: 4000 / 100 / 200   Position de la section centrale
  Plane Parameters \> Normal: 1 /0 /0            Normale des points Slice dans la direction x
  Coloring: ReinforcementRatio_x                 Optionnel
  Styling \> Line Width: 2                       Ou tout autre paramètre qui donne un résultat agréable

<img alt="" src=images/PVPicSlice3.png  style="width:400px;">

\'\'\'Paramètres Calculator 1

Calculator 1 calcule la nouvelle variable ReinforcementRatio_x \* y qui doit être intégrée pour obtenir la coordonnée y du centre de gravité de l\'armature.

<img alt="" src=images/PVPicSlice4.png  style="width:400px;">

Après avoir appuyé sur Apply, une nouvelle variable nommée «ReinforcementRatio_x \* y» est disponible pour affichage ou traitement ultérieur.

\'\'\'Paramètres Calculator 2

Calculator 1 calcule la nouvelle variable ReinforcementRatio_x \* z qui doit être intégrée pour obtenir la coordonnée z du centre de gravité de l\'armature.

<img alt="" src=images/PVPicSlice5.png  style="width:400px;">

Après avoir appuyé sur Apply, une nouvelle variable nommée «ReinforcementRatio_x \* z» est disponible pour affichage ou traitement ultérieur.

Enfin, deux filtres d\'intégration sont appliqués, l\'un sur Calculator1 pour intégrer la variable ReinforcementRatio_x \* y et l\'autre sur Calculator2 pour intégrer ReinforcementRatio_x \* z. Chacun est affiché dans sa propre fenêtre avec SpreadSheetView sélectionné. La façon de désélectionner tous les autres résultats est expliquée plus haut.

<img alt="" src=images/PVPicSlice6.png  style="width:700px;">

Enfin, le centre de gravité peut être calculé à partir des résultats ci-dessus comme:

CoG_y = 55744,2 / 556,277 = 100,2 mm (valeur exacte: 100 mm)

CoG_z = 187144 / 556,277 = 336,4 mm (valeur exacte: 5/6 \* 400 mm)



## Intégration sur une ligne 

Pour démontrer la visualisation et l\'intégration des résultats sur une ligne, nous utilisons l\'exemple 2D d\'un mur épais tel qu\'introduit dans [ce fil de discussion FC](https://forum.freecadweb.org/viewtopic.php?f=18&t=33049). Le fichier FreeCAD pour cet exemple peut être téléchargé depuis [ce fil de discussion FC](https://forum.freecadweb.org/viewtopic.php?f=18&t=37253&start=10#p367734). Le but consiste à visualiser le rapport de ferraillage sur différentes sections verticales et à déterminer la zone requise d\'acier à partir de l\'intégration de ces résultats.

Les techniques introduites dans les sections précédentes de ce tutoriel ne seront pas répétées ici. Il est également important de noter à nouveau qu'au fur et à mesure que de nouveaux objets sont ajoutés au Pipeline Browser et que davantage de fenêtres d'affichage sont ouvertes, il devient de plus en plus important de s'assurer que le bon objet est sélectionné dans le Pipeline Browser et que la fenêtre de droite est mise en évidence lors des modifications de l\'onglet Propriétés. Sinon, beaucoup de temps peut être consacré à la recherche de la bonne propriété ou les modifications apportées aux propriétés peuvent ne pas prendre effet.

En commençant par l\'objet VTK importé de l\'atelier FEM, nous notons que les commandes Paraview fonctionnent légèrement différemment sur un objet bidimensionnel. Le bouton gauche de la souris fait glisser la géométrie et le bouton central de la souris la fait pivoter. Pour positionner la géométrie dans le plan d\'analyse (c\'est-à-dire x-y), appuyez sur l\'icône qui place la vue le long de l\'axe z négatif:

<img alt="" src=images/PVPicLine1.png  style="width:75px;">

Pour l\'image ci-dessous, la propriété Coloring de l\'onglet Propriétés de l\'objet VTK a été définie sur ReinforcementRatio_x.

Le seul objet supplémentaire requis pour visualiser une variable le long d\'une ligne droite est un filtre Plot Over Line. Ceci peut être activé à partir de la barre d\'icônes ou de l\'option de menu Filters \> Alphabetical.

Nous voulons ensuite afficher les exigences de renforcement horizontal dans la section verticale sous la colonne. Pour y parvenir de la manière illustrée ci-dessous, les paramètres suivants doivent être modifiés dans l\'onglet Propriétés du filtre Plot Over Line (assurez-vous que la fenêtre LineChartView et l\'objet Plot Over Line ont tous deux le focus)

  Paramètres de l\'onglet Propriétés                                     Commentaire
   
  Line Parameters \> Point 1: 4000 / 0 / 0                               Point en bas du mur sous la colonne
  Line Parameters \> Point 2: 4000 / 4000 / 0                            Point en haut du mur sous la colonne
  x Axis Parameters \> x Array Name: ReinforcementRatio_x                Affiche ReinforcementRatio_x sur l\'axe horizontal
  Series Parameters: tick "arc length" only                              Ceci est le paramètre de longueur le long de la ligne
  Title \> Chart Title: Mid Section                                      
  Annotation \> Show Legend: deselect                                    Inutile pour le choix actuel de l\'axe vertical
  Left Axis \> Left Axis Title: Height Across Beam                       
  Left Axis Range \> Use Custom Range: deselect                          Désélectionnez pour maximiser la plage de données le long de l\'axe
  Bottom Axis \> Bottom Axis Title: Reinforcement Ratio in x-Direction   
  Bottom Axis Range \> Use Custom Range: deselect                        Désélectionnez pour maximiser la plage de données le long de l\'axe

<img alt="" src=images/PVPicLine2.png  style="width:700px;">

Notez que la distance le long de la ligne (longueur d\'arc) est généralement sur l\'axe horizontal et la variable que nous voulons afficher (ici ReinforcementRatio_x) sur l\'axe vertical. Cependant, comme la section de mur dans cet exemple est verticale et que nous voulons voir les exigences de renforcement sur la hauteur du mur, il est plus naturel d\'inverser les axes. Cependant, cela se fait au détriment de beaucoup plus de changements dans les paramètres de l\'onglet Propriétés du filtre Plot Over Line.

Dans les deux images suivantes, seul l\'emplacement de la ligne a été modifié. Notez cependant que cette relocalisation modifiera automatiquement le paramètre Left Axis Range \> Use Custom Range pour «sélectionner». Cela peut signifier que le graphique ne tient pas correctement dans la fenêtre LineChartView. Il est donc nécessaire de désélectionner cette option à chaque changement de position de la ligne. Les autres paramètres sont conformes au tableau ci-dessus.

  Paramètres de l\'onglet Propriétés                Commentaire
   
  Line Parameters \> Point 1: 6700 / 0 / 0          Point au bas du mur sous le côté gauche de la découpe
  Line Parameters \> Point 2: 6700 / 4000 / 0       Point en haut du mur au-dessus du côté gauche de la découpe
  Title \> Chart Title: Section left of Cut-out     
  Left Axis Range \> Use Custom Range: deselect     Désélectionnez pour maximiser la plage de données le long de l\'axe
  Bottom Axis Range \> Use Custom Range: deselect   Désélectionnez pour maximiser la plage de données le long de l\'axe

<img alt="" src=images/PVPicLine3.png  style="width:700px;">

  Paramètres de l\'onglet Propriétés                Commentaire
   
  Line Parameters \> Point 1: 10950 / 0 / 0         Point en bas du mur sur le support droit
  Line Parameters \> Point 2: 10950 / 4000 / 0      Point en haut du mur sur le support droit
  Title \> Chart Title: Section at Support          
  Left Axis Range \> Use Custom Range: deselect     Désélectionnez pour maximiser la plage de données le long de l\'axe
  Bottom Axis Range \> Use Custom Range: deselect   Désélectionnez pour maximiser la plage de données le long de l\'axe

<img alt="" src=images/PVPicLine4.png  style="width:700px;">

Le besoin total de ferraillage horizontal dans la dernière coupe peut maintenant être simplement obtenu en appliquant un filtre d\'intégration à l\'objet Plot Over Line, c\'est-à-dire en surbrillance l\'objet Plot Over Line dans le Pipeline Browser et en ajoutant un filtre d\'intégration à partir de l\'option de menu Filters \> Alphabetical.

<img alt="" src=images/PVPicLine5.png  style="width:700px;">

De la manière habituelle, désélectionnez tout sauf le résultat ReinforcementRatio_x dans SpreadSheetView et lisez le résultat comme 23,11 mm2 / mm. Pour obtenir la section transversale totale de l\'acier, nous devons encore multiplier avec l\'épaisseur du mur, qui dans cet exemple est (impressionnant) 600 mm. Ainsi, la surface de coupe transversale totale de l\'acier traversant la section transversale près du support droit est de 23,11 \* 600 = 13866 mm2 = 139 cm2

Pour obtenir une distribution plus pratique des armatures, nous pourrions intégrer le graphique ci-dessus en plusieurs parties. Par exemple, si nous voulons connaître la section transversale requise de l\'acier dans les 400 mm supérieurs du mur, nous devons ajuster les propriétés de l\'objet Plot Over Line comme suit:

  Paramètres de l\'onglet Propriétés                Commentaire
   
  Line Parameters \> Point 1: 10950 / 3600 / 0      Point près du haut du mur sur le support droit
  Line Parameters \> Point 2: 10950 / 4000 / 0      Point en haut du mur sur le support droit
  Left Axis Range \> Use Custom Range: deselect     Désélectionnez pour maximiser la plage de données le long de l\'axe
  Bottom Axis Range \> Use Custom Range: deselect   Désélectionnez pour maximiser la plage de données le long de l\'axe

Cela donne le résultat suivant

<img alt="" src=images/PVPicLine6.png  style="width:700px;">

Le résultat pour les 400 mm supérieurs du mur est ainsi de 8,436 mm2 / mm. Les 10% supérieurs du mur nécessitent donc 8,44 / 23,11 \* 100% = 37% de l\'acier d\'armature.

Cette procédure pourrait être répétée pour diviser le mur en zones de renforcement constant.



## Représentation des résultats vectoriels avec le filtre Glyph 3D 

Jusqu\'à présent, nous n\'avons traité que des valeurs scalaires, comme le taux de renforcement et l\'amplitude du déplacement. La visualisation des résultats vectoriels, comme les vecteurs de contrainte principale, se fait avec Glyphs.

Revenons à l\'objet de données VTK pour la poutre avec support central et visualisons les vecteurs de contrainte principaux maximum et minimum.

Mettez en surbrillance l\'objet de données VTK dans le Pipeline Browser et sélectionnez le filtre Glyph dans la barre d\'icônes de filtre ou dans l\'option de menu Filter \> Alphabetical. Appliquez ensuite les paramètres suivants dans l\'onglet Propriétés de l\'objet Filtre Glyph (voir tableau et image):

  Paramètres de l\'onglet Propriétés                   Commentaire
   
  Glyph Source \> Glyph Type: Line                     Malheureusement, il n\'y a pas d\'option pour une flèche double face
  Orientation \> Orientation: Major Principal Stress   Le Glyph prend la direction principale de la contrainte
  Scale \> Scale Array: Major Principal Stress         La longueur de la ligne représentera l\'ampleur de la contrainte principale
  Scale \> Vector Scale Mode: Scale by Magnitude       
  Scale \> Scale Factor: 100                           Ou tout autre paramètre qui donne un résultat agréable
  Masking \> Glyph Mode: All Points                    Pour vous assurer que la contrainte dans chaque nœud est affichée
  Coloring \> Solid Color                              Une seule couleur donne une plus grande clarté du «flux de contraintes»
  Coloring \> Edit \> Green                            Ou tout autre paramètre qui donne un résultat agréable
  Styling \> Line Width \> 2                           Ou tout autre paramètre qui donne un résultat agréable

<img alt="" src=images/PVPic32.png  style="width:400px;">; <img alt="" src=images/PVPic33.png  style="width:400px;">

Si tout se passe bien, vous devriez voir le résultat suivant pour l\'exemple de fichier.

<img alt="" src=images/PVPic34.png  style="width:700px;">

Ajoutez ensuite un autre filtre Glyph avec les paramètres suivants pour la contrainte principale mineure (n\'oubliez pas de mettre d\'abord en surbrillance l\'objet de données VTK dans le Pipeline Browser):

  Paramètres de l\'onglet Propriétés                   Commentaire
   
  Glyph Source \> Glyph Type: Line                     Malheureusement, il n\'y a pas d\'option pour une flèche double face
  Orientation \> Orientation: Minor Principal Stress   Le Glyph prend la direction principale de la contrainte
  Scale \> Scale Array: Minor Principal Stress         La longueur de la ligne représentera l\'ampleur de la contrainte principale
  Scale \> Vector Scale Mode: Scale by Magnitude       
  Scale \> Scale Factor: 100                           Ou tout autre paramètre qui donne un résultat agréable
  Masking \> Glyph Mode: All Points                    Pour vous assurer que la contrainte dans chaque nœud est affichée
  Coloring \> Solid Color                              Une seule couleur donne une plus grande clarté du «flux de contraintes»
  Coloring \> Edit \> Red                              Ou tout autre paramètre qui donne un résultat agréable
  Styling \> Line Width \> 2                           Ou tout autre paramètre qui donne un résultat agréable

<img alt="" src=images/PVPic35.png  style="width:700px;">

Le résultat final montre les vecteurs de contrainte principaux majeurs et mineurs superposés à la poutre avec ReinforcementRatio_x.



## Exportation des résultats graphiques 

Pour exporter une fenêtre RenderView, mettez-la en surbrillance et utilisez l\'option de menu **File > Save Screenshot**


{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > Post-Processing of FEM Results with Paraview/fr
