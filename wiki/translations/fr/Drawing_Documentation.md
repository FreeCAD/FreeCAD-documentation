# Drawing Documentation/fr
Cette page documente le module de dessin de jcc242. Il inclut des fichiers et des fonctionnalités sur lesquels il travaille actuellement et qui peuvent ne pas encore être dans la branche principale. La source de ces fichiers est sur [son Github](https://github.com/jcc242/FreeCAD) mais faites attention car il est pour le moment très instable!

## Base (Mod/Drawing) 

### gdtsvg.py

Script Python génère des extraits svg pour des éléments tels que des symboles gd & t, des symboles de dimension et des éléments de base svg tels que des lignes, des cercles et des chemins.

Il a plusieurs fichiers qui ne font pas vraiment beaucoup de choses. Exécutez DrawingTest.py pour créer un groupe d'icônes svg dans le répertoire icon qui affiche différentes icônes dans le fichier gdtsvg.py. settingslist.py, dimesettings et convert.py sont tous déconseillés pour les méthodes de paramétrage plus anciennes et doivent probablement être supprimés à mesure que la branche de dessin se fusionne en maître.

### DrawingAlgos.py

Crée des lignes svg à partir d\'une liste de sommets, prend en charge les bords cachés et visibles. Devrait probablement être fusionné avec gdtsvg.py à l'échéance du fichier.

#### createSVG

Accepte la pièce en tant qu\'argument, projette la pièce dans des lignes à partir de l\'objet Drawing.project, puis dessine et crée le svg pour chaque ligne.

## App

Contient le backend du module de dessin.

### AppDrawing.cpp

Initialise les différents espaces de noms, modules et éléments utilisés dans le module de dessin. Lance une erreur s\'il ne peut pas charger le module Part.

### DrawingExport.cpp

Deux classes: SVGOutput et DXFOutput. Ils contiennent tous deux des méthodes pour afficher le code dans leur langue respective. Nécessite généralement un objet de la typedef appropriée, et parfois des informations d\'identifiant supplémentaires.

### FeatureClip.cpp

Les méthodes Callback (?) pour l\'interface de découpage des fonctionnalités, semble-t-il. Appelées seules, elles créeront le chemin du clip. Si ShowFrame.getValue est défini sur TRUE, il affiche également la bordure de l\'image.

### FeaturePage.cpp

Gère les vues.

onChanged() pour faire des choses quand les propriétés sont modifiées.

execute() pour recalculer une vue de fonctionnalité, selon le cas. Il semble avoir des outils pour vérifier les textes modifiables et sauvegarder les dessins. Demande plus de recherche.

getEditableTextsFromTemplate() pour récupérer le texte qui peut être édité par FreeCAD depuis un fichier SVG.

### FeatureProjection.cpp

Aplatit l\'objet en une image 2D?

### FeatureView.cpp

Définit les propriétés des vues.

### FeatureViewAnnotation.cpp

Définit les propriétés des annotations (juste du texte à l'heure actuelle), dispose d'une méthode d\'exécution pour mettre à jour le texte s\'il est modifié/déplacé.

### FeatureViewPart.cpp

Constructeur pour ajouter des propriétés. Obtient des trucs d\'aspect pour les parties projetées.

### PageGroup.cpp

Ajoute simplement une propriété pour une liste de pages, pas grand chose d\'autre.

### Precompiled.cppp

Simplement #inclus \"PreCompiled.h\"

### ProjectionAlgos.cpp

Le constructeur exécute simplement la méthode execute() pour mettre à jour ses données.

invertY: puisque SVG effectue son axe y vers l'arrière par rapport à tous les autres systèmes de coordonnées du monde, nous devons l'inverser lors de la conversion d'une pièce FreeCAD en projection SVG pour la vue de dessin.

getSVG: récupère le code SVG à partir du logiciel DrawingExport. Formats dépendant du type de ligne (masqués ou non et autres éléments, à comprendre\...).

getDXF: identique à getSVG à l\'exception du format DXF.

## Gui - interface graphique 

### AppDrawingGui.cpp

Initialise l'interface graphique.

### AppDrawingGuiPy.cpp

Fournit des interfaces d\'ouverture, d\'importation et d\'exportation? Il semblerait que ce soit accessible en Python.

### Command.cpp

Gère les commandes (à partir de la barre d'outils?) telles que la création de nouveaux dessins et autres choses. Il semble que cela gère les appels QT depuis le clic sur le bouton jusqu'à la commande à utiliser, par exemple. Cliquez sur le bouton CmdDrawingOrthoViews pour afficher l\'interface graphique Ortho Views dans la boîte de dialogue de la tâche.

### DrawingView.cpp

Fais un tas de trucs qt de l\'interface graphique. Besoin de lire plus à ce sujet.

### TaskDialog.cpp

Crée la boîte de dialogue des tâches sur le côté et y accède probablement à partir de l\'arborescence, le cas échéant.

### TaskOrthoViews.cpp

Crée le dialogue des tâches pour placer les vues orthogonales !

Effectue beaucoup de calculs pour savoir où positionner les choses (calculs automatiques aussi, semble-t-il).

Prend l\'input de l\'interface graphique TaskOrthoViews et fait des choses avec elle. Utilise la méthode de l\'héritage unique dont on parle [sur le site web de qt](http://doc.qt.digia.com/qt/designer-using-a-ui-file.html).

### ViewProviderPage.cpp

Le Constructeur ajoute quelques propriétés pour les trucs de vue. Le Destructeur ne fait rien. Attache quelque chose (attache quoi? attache la vue à la page?) définit et obtient des modes d\'affichage (quels sont les modes d\'affichage ? que font-ils et quelles sont les options possibles?) Est-ce que quelque chose au sujet de la mise à jour d\'une sorte de données a un menu contextuel qui dit \"Show drawing\"? Besoin de comprendre ce que cela signifie. A un truc pour double-cliquer pour sélectionner la vue (je pense?)

showDrawingView semble faire un peu de travail sur les réglages: récupère le document courant, définit l\'icône et le titre de la fenêtre, l\'ajoute à la fenêtre principale (de FreeCAD?).

### ViewProviderView.cpp

Il ne semble pas faire grand-chose, mais je suis sûr que c\'est important.

### Workbench.cpp

Ajoute les icônes aux barres d\'outils et autres.

# Flux de travail 

## Flux du programme 

CanvasView est l\'objet QGraphicsScene et DrawingView traite une liste de FeatureView qui sont liés par référence dans /App/FeatureViewPage. DrawingView sélectionne alors la classe QGraphicsItem appropriée (QGraphicsItemViewPart ou QGraphicsItemViewDimension) et appelle ensuite une fonction dans CanvasView pour la créer et l\'ajouter à la scène.

## Ajouter des commandes à l\'atelier de dessin 

4 étapes simples :

1.  Ajouter une classe à Command.cpp. Suivez les autres pour un exemple de formatage.
2.  Ajoutez un titre, une icône, une infobulle, etc., puis suivez les classes existantes dans command.cpp.
3.  Ajoutez votre classe au bas de Command.cpp
4.  Ajoutez vos informations dans Workbench.cpp, cela indiquera à FreeCAD/Drawing module où placer les icônes définies dans command.cpp dans l\'interface freecad réelle (les barres d\'outils, menus déroulants, etc.)

{{Drawing Tools navi}}



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Drawing](Category_Drawing.md) > Drawing Documentation/fr
