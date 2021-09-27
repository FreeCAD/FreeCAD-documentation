# Render project/fr
**(2020) Cette page fait référence à une tentative de mise à jour de l'[Atelier Raytracing](Raytracing_Workbench/fr.md), proposé vers 2012. Son auteur d'origine n'ayant jamais terminé la mise en œuvre, ces informations sont obsolètes et ne doivent pas être considérées comme actuelles.

Un nouveau développement est en cours dans l'[https://github.com/FreeCAD/FreeCAD-render Atelier Render], un remplacement complet en Python pour l'[Atelier Raytracing](Raytracing_Workbench/fr.md).

Malgré cette page mentionnant le "module Render", ce n'est pas le même projet que le nouvel [https://github.com/FreeCAD/FreeCAD-render Atelier Render].
**

## Vue d\'ensemble 


{{TOCright}}

Le module Render offre un moyen simple et direct de créer rapidement un rendu sur les pièces FreeCAD. Sa philosophie repose sur un système de modèles vous permettant de visualiser votre travail plus efficacement. Le module Render a pour objectif de cacher le processus complexe des rendus à l\'utilisateur afin que vous puissiez vous préoccuper de la conception des pièces.

Le **module Render**, est conçu pour fonctionner avec plusieurs types de rendu, mais actuellement, seul **[LuxRender](http://www.luxrender.net/en_GB/index)** est pris en charge.

Le fonctionnement s\'effectue comme suit :

-   Créez une fonctionnalité Render.

-   Sélectionnez les objets, et, modèles désirés.

-   Attribuez les matériaux, des objets visibles dans votre document.

-   Position de l\'appareil photo

-   Prévisualisation du rendu

Une brève description des outils dans le module Render :

### Fonctionnalités de Render 

Les fonctionnalités de Render, contiennent les informations qui seront transmises à la caméra, aux paramètres de rendu, aux matériaux, et, aussi ce qui doit être utilisé par le plugin. Cela signifie que vous pouvez créer beaucoup de caractéristiques différentes, de matériaux différents, de réglages d\'appareils, qui sont indépendants les uns des autres. Les fonctions prennent également tout le contrôle, sur le processus de rendu.

### Matériaux de Render 

Chaque matériau de Render est basé sur des matériaux contenu dans des bibliothèques, qui sont stockées dans des Fichiers .XML séparés. Ces matériaux de Render peuvent être attribués à des propriétés telles que, la couleur, la brillance, et, d\'autres paramètres. Ces matériaux sont ensuite attachés à un objet dans le document.





**Actuellement, pour utiliser le nouvel atemier Render, vous devez être en mesure de compiler la branche en développement.**

### Utiliser le module Render : 

Première chose, allez sur le dépôt suivant [raytracing](https://github.com/mrlukeparry/FreeCAD_sf_master/tree/raytracing), et, cherchez la branche \'Render\'. Assurez-vous ensuite que vous pouvez la compiler.

Télécharger ou installer le dernier Lux Render 1.2.1 pour votre système à partir de [luxrender](http://www.luxrender.net/en_GB/download), et, assurez vous qu\'il fonctionne correctement.

Ouvrez FreeCAD, et, démarrez l\'atelier Raytracing workbench. Vous devez donner le \"chemin exécutable\" pour rendre Lux Render accessible. Il peut être défini dans Edit → Preferences → Raytracing. Le chemin de l\'exécutable luxconsole doit être défini.

![](images/luxRenderExecPath.png )

Créez vos pièces au sein de FreeCAD. Puis retournez dans l\'atelier Raytracing, et, créez une \'fonction Render\'. Une nouvelle fenêtre de tâches s\'affiche :

![](images/renderTaskView.png )

Lorsque vous créez une fonction Render, la position actuelle, et, la caméra utilisée dans votre fenêtre 3D, sont enregistrées. Vous pouvez librement repositionner, et, cliquer sur \'Save Camera\', pour enregistrer l\'état actuel de la caméra dans la fonction.

Vous pouvez définir d\'autres paramètres de rendu :

#### Render Preset 

Les préréglages de Render sont spécifiques aux plugin de rendu qui sont utilisés. Ils changent le processus de rendu, afin d\'améliorer la qualité de la sortie, ou la vitesse à laquelle la sortie est générée. Avec Lux Render, \'MLT Unbiased\', produit des résultats de bonne qualité dans un délai raisonnable. \'Direct Lighting Preview\' produit un résultat rapide, mais de faible qualité.

#### Render Template 

Les modèles Render sont actuellement spécifiques au plugin de rendu. En sélectionnant un modèle, il générera une scène prédéfinie, telle que l\'éclairage, la géométrie avec vos pièces à l\'intérieur. Actuellement, \'Lux Classic\' fonctionne correctement et produit des résultats satisfaisants. Il tentera de calculer la scène en fonction de la position de votre caméra et de la taille globale des pièces visibles.

### Lancer un Render 

Une fois que les paramètres de la fonction ont été définis, vous pouvez lancer la scène. Par exemple, voyez la photo exemple. Toutes les pièces qui ne sont pas visibles dans le document ne figureront pas dans le Render.

![](images/Example.png )

Le bouton \'Preview Window\' actionnera le rendu dans la fenêtre 3D actuelle. Le bouton \'Preview\' utilise la position enregistrées de la caméra ainsi que la taille de sortie. Seul un extrait à la fois peut être exécuté par la fonction, mais, vous pouvez exécuter plusieurs processus de rendu.

![](images/renderButtons.png )

Après avoir démarré un **rendu**, une nouvelle fenêtre s\'affiche. Pendant qu\'elle est exportée, et, selon sa complexité, le chargement par le programme de rendu externe, peut prendre plusieurs secondes, pour que votre scène soit créée. Un écran de chargement apparaît.

![](images/loading.png )

Si le processus de rendu est réussi, la sortie sera automatiquement affichée. Vous pouvez librement déplacer l\'image, de zoomer, et, dé-zoomer.

![](images/sceneOutput.png )

### Unbiased Rendering 

En fait, le programme de rendu simule des rayons lumineux qui \'rebondissent\' dans une scène. Lorsque cette lumière frappe une caméra, elle est visible à l\'écran. Au fil du temps, d\'autres rayons frappent la caméra et une image se forme. Au début, l\'image sera bruyante car la lumière n\'a pas atteint la caméra.

Lorsque vous êtes satisfait de la sortie, appuyez sur \'Stop Render\'. Vous pouvez maintenant enregistrer l\'image (actuellement stocké dans un format .png)

![](images/unbiasedRendering.png )

#### Vitesse de rendu 

Les processus de rendu sont généralement exécutés sur le processeur. Le temps pris pour un résultat satisfaisant, dépend de la taille de la sortie de la scène, le nombre, la complexité des matériaux utilisés, les rayons lumineux, et, des performances globales de votre système. Un aperçu rapide d\'une simple pièce peut prendre une minute, alors qu\'une sortie de haute qualité peut prendre plusieurs heures.

### Rattacher des matériaux 

Assurez vous que êtes actuellement en mode édition pour la fonction de rendu. Cliquez sur Add materials dans la barre d\'outils. Une liste de documents dans la bibliothèque apparaît dans la fenêtre des tâches. Vous pouvez les faire défiler, en faisant glisser la liste, ou en utilisant la roulette de la souris.

![](images/materialSelection.png )

Pour rattacher un matériau à un objet de votre document, faites glisser l\'icône matériau et déposez-la sur un élément dans la vue 3D.

![](images/materialDragNDrop.png )

Si le matériau possède des propriétés modifiables telles que la couleur, une nouvelle boîte de dialogue apparaît dans la vue des tâches. Sinon, la vue de la tâche revient à la vue Render Feature.

![](images/materialProperties.png )

Lorsque vous êtes satisfait, de la définition des propriétés, cliquez sur \'Save\'.

Tous les matériaux à l\'intérieur d\'une fonction de rendu, sont affichés dans la vue liste. Ceux-ci peuvent être sélectionnés, et, ou, supprimés. Si le matériau a une propriété, il peut être modifié, en double cliquant dessus.

![](images/materialListView.png )

## Liens

Voir aussi [Tutoriel Raytracing](Raytracing_tutorial/fr.md)


 

_ _ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > Render project/fr
