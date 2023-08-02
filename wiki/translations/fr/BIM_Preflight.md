---
- GuiCommand:Addon/fr
   Name: BIM Preflight
   Name/fr: BIM Contrôle en amont
   Workbenches: Image:IFC.svg BIM Workbench/fr
   Addon: BIM
   MenuLocation: Manage -> Preflight check
---

# BIM Preflight/fr

## Description

<img alt="" src=images/BIM_preflight_screenshot.png  style="width:1024px;">

FreeCAD étant une plate-forme de modélisation très souple, les exigences sont très faibles. Vous pouvez essentiellement modéliser et organiser votre modèle BIM comme vous le souhaitez, en utilisant tous les outils offerts par FreeCAD, à la fois à partir de l\'atelier BIM et d\'autres ateliers. Le format IFC, cependant, a des exigences strictes, et d\'autres applications BIM qui peuvent lire des fichiers IFC apportent souvent des limitations supplémentaires car elles ont plus que souvent des difficultés avec certaines entités ou la façon dont certains objets sont modélisés.

L\'outil de contrôle en amont BIM vous permet d\'effectuer plusieurs tests sur votre modèle pour vérifier sa compatibilité avec les normes IFC et les meilleures pratiques et vous aider à détecter les éventuels problèmes que vous pourriez vouloir résoudre.

Les résultats de la plupart des tests fournis par cet outil sont facultatifs, ce qui signifie que vous pouvez choisir d\'exporter votre modèle même en cas d\'échec. Vous êtes le seul à évaluer si vous avez besoin du test pour réussir ou non. Nous avons fait de notre mieux pour fournir des informations fiables afin de vous aider à prendre une décision.

## Utilisation

-   Avoir un modèle ouvert dans FreeCAD, avec au moins quelques objets
-   Vous pouvez sélectionner des objets avant de lancer les tests, auquel cas vous avez la possibilité d\'effectuer le test uniquement sur les objets sélectionnés
-   Appuyez sur le bouton **Test All** pour effectuer tous les tests ou uniquement les boutons correspondant aux tests individuels.
-   Une fois les tests terminés, appuyer sur un bouton **Failed** vous donnera des informations supplémentaires pour vous aider à décider si cela vous concerne ou non.

## Tests intégrés 

-   **Run all tests**: Exécute tous les tests les uns après les autres

### Tests d\'installation de FreeCAD 

-   **IFC4 support**: Teste si le système d\'importation/exportation IFC de FreeCAD fonctionne correctement et si le format IFC4 est disponible (nécessite une version à jour de [IfcOpenShell](Arch_IFC/fr.md)) et activé dans les préférences.

### Tests d\'organisation du projet 

-   **Project hierarchy**: Le format IFC nécessite au moins un [Bâtiment](Arch_Building/fr.md) et il est également courant d\'avoir un [site](Arch_Site/fr.md) et au moins un [Etage](Arch_BuildingPart/fr.md). Ce test vérifie s\'ils sont présents dans le modèle
-   **Buildings**: vérifie que tous les bâtiments trouvés dans le modèle font partie d\'un [site](Arch_Site/fr.md)
-   **Levels**: vérifie que tous les [Etages](Arch_BuildingPart/fr.md) (étages du bâtiment) trouvés dans le modèle sont bien d\'un bâtiment
-   **Objects structure**: Vérifie que tous les objets trouvés dans le modèle font partie d\'un niveau

### Objets et tests de propriétés 

-   **Undefined objects**: vérifie s\'il y a des objets dans le modèle qui ne sont pas des objets BIM et seront donc exportés sans les propriétés BIM complètes
-   **Solids**: vérifie que tous les objets du modèle ont une géométrie solide valide
-   **Explicit quantities**: vérifie que tous les objets avec des propriétés de longueur, largeur ou hauteur sont [marqués pour l\'exportation explicite](BIM_IfcQuantities/fr.md) de ces quantités
-   **Common Properties sets**: vérifie que tous les objets BIM de types communs (mur, porte, etc \...) ont le jeu de propriétés \"common\" correspondant appliqué (Pset_WallCommon, Pset_DoorCommon, etc.)
-   **Property sets integrity**: vérifie que tous les Psets courants (Pset_WallCommon, Pset_DoorCommon, etc.) trouvés dans le modèle incluent toutes et uniquement les propriétés définies par les normes IFC
-   **Materials**: vérifie que tous les objets BIM ont un matériau
-   **Standards**: vérifie que tous les objets BIM ont un [code standard](BIM_Classification/fr.md)

### Tests de compatibilité 

-   **Extrusions**: vérifie que tous les objets BIM sont des extrusions linéaires
-   **Standard cases**: vérifie que tous les [murs](Arch_Wall/fr.md) et [éléments de structure](Arch_Structure/fr.md) sont des cas standard, tels que définis par le schéma IFC
-   **Tiny lines**: vérifie qu\'aucun segment de ligne dans le modèle n\'est inférieur à 1/32\", la longueur minimale que Revit est capable de gérer\...
-   **IfcRectangleProfileDef**: vérifie que l\'option d\'exporter des profils rectangulaires en tant que IfcRectangleProfileDef est désactivée, car Revit (oui, encore une fois) ne peut pas importer cette entité.

## Tests personnalisés 

L\'outil de contrôle en amont vous permet également d\'écrire des tests personnalisés, qui seront ajoutés après les outils intégrés dans la boîte de dialogue Contrôle en amont, et exécutés lorsque vous utilisez le bouton **Run all tests**. Ces tests sont écrits en Python. Ils se composent de fonctions simples dans un ou plusieurs fichiers Python. Vous pouvez effectuer toutes les opérations que vous souhaitez à l\'intérieur de ces fonctions, elles doivent simplement réussir ou échouer, et en cas d\'échec, afficher un message informant l\'utilisateur de ce qui a échoué.

Vous pouvez écrire plusieurs tests dans un seul fichier Python ou diviser en plusieurs fichiers, selon vos préférences. Ces fichiers doivent être placés dans \$USERAPPDATA/BIM/Preflight et peuvent recevoir n\'importe quel nom (assurez-vous d\'utiliser des noms très uniques pour ne pas entrer en conflit avec un module Python intégré. Le dossier \$USERAPPDATA dépend de votre plate-forme/système d\'exploitation (généralement \$HOME/.FreeCAD sous linux/mac, /users/YOUR USER/Application Data/roaming/FreeCAD sous windows) et peut également être trouvé en tapant ceci dans la console Python de FreeCAD:

FreeCAD.getUserAppDataDir()

À l\'intérieur de chaque fichier Python, les tests sont des fonctions simples qui ne prennent aucun argument et renvoient soit True si le test a réussi, soit une chaîne de texte qui sera montrée à l\'utilisateur si le test a échoué.

Un fichier de test typique serait comme ceci, qui devrait être nommé quelque chose comme \"myCustomTest.py\" et placé dans \$USERAPPDATA/BIM/Preflight:

import FreeCAD
# The name of your test. You can give the functions any name
# you want, the important is the description text below
def myCustomTest():
   # This describes what your test does. For example,
   # here, it checks that there is at least one object in the document.
   # This text will appear next to the button in the Preflight tool
   """Checks that the document contains at least one object"""
   doc = FreeCAD.ActiveDocument
   objects = doc.Objects
   if len(objects) >= 1:
       result = True
   else:
       result = "This document contains no object"
   # The function must return either True or a string of
   # text if the test failed. The string or text will be displayed
   # to the user when they press the "Failed" button.
   return result



---
⏵ [documentation index](../README.md) > BIM Preflight/fr
