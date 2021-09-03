


{{TOCright}}

## Introduction

Les **Macros** sont un moyen pratique de reproduire des actions complexes dans FreeCAD. Vous enregistrez simplement les actions au fur et à mesure que vous les effectuez, puis vous les enregistrez sous un nom et les relancez quand vous le souhaitez. Étant donné que les macros sont en réalité une liste de commandes [Python](Python/fr.md), vous pouvez également les modifier et créer des scripts très complexes.

Alors que les scripts Python ont normalement l\'extension `.py`, les macros FreeCAD doivent avoir l\'extension `.FCMacro`. Une collection de macros écrites par des utilisateurs expérimentés se trouve sur la page [Macros](Macros_recipes/fr.md).

Voyez la [Documentation pour utilisateurs expérimentés](Power_users_hub/fr.md) pour en savoir plus sur le langage de programmation [Python](Python/fr.md) et sur l\'écriture de macros. En particulier, vous devriez commencer par ces pages :

-   [Introduction à Python](Introduction_to_Python/fr.md)
-   [Tutoriel de script Python](Python_scripting_tutorial/fr.md)
-   [FreeCAD : Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md)

## Fonctionnement

Activez la sortie de la console dans le menu **Edition → Préférences → Général → Macro → Montrer les commandes du script dans la console Python**. Vous verrez que dans FreeCAD, chaque action que vous effectuez, comme appuyer sur un bouton, génère une commande Python. Ces commandes sont ce qui peut être enregistré dans une macro. L\'outil principal pour créer des macros est la barre d\'outils des macros : ![](images/Macros_toolbar.jpg ). Vous y avez 4 boutons : Enregistrer, arrêter l\'enregistrement, éditer et lire la macro actuelle.

C\'est très simple à utiliser : appuyez sur le bouton d\'enregistrement, il vous sera demandé de donner un nom à votre macro, puis effectuez quelques actions. Lorsque vous avez terminé, cliquez sur le bouton Arrêter l\'enregistrement et vos actions seront enregistrées. Vous pouvez maintenant accéder à la boîte de dialogue de macro avec le bouton d\'édition.

![](images/Macros.png ) *Interface listant les macros disponibles dans le système*

Vous pouvez y gérer vos macros, les supprimer, les modifier, les dupliquer, les installer ou en créer de nouvelles à partir de zéro. Si vous modifiez une macro, elle sera ouverte dans une fenêtre d\'éditeur où vous pourrez apporter des modifications à son code. De nouvelles macros peuvent être installées en utilisant le bouton {{button|Addons...}}, qui relie au [Gestionnaire d\'Addon](AddonManager/fr.md).

## Exemple

Appuyez sur le bouton d\'enregistrement, donnez un nom, disons \"cylindre 10x10\", puis dans l\'[Atelier Part](Part_Workbench/fr.md), créez un cylindre de rayon=10 et de hauteur=10. Ensuite, appuyez sur le bouton \"arrêter l\'enregistrement\". Dans la boîte de dialogue d\'édition des macros, vous pouvez voir le code python qui a été enregistré et si vous le souhaitez, y apporter des modifications. Pour exécuter votre macro, appuyez simplement sur le bouton Exécuter de la barre d\'outils pendant que votre macro est dans l\'éditeur. Votre macro est toujours enregistrée sur le disque, donc toute modification que vous apportez, ou toute nouvelle macro que vous créez, sera toujours disponible au prochain démarrage de FreeCAD.

## Personnalisation

Bien sûr il n\'est pas pratique de charger une macro dans l\'éditeur pour l\'utiliser. FreeCAD fournit de bien meilleures façons d\'utiliser votre macro, comme lui attribuer un raccourci clavier ou mettre une entrée dans le menu. Une fois votre macro créée, tout cela peut être fait via le menu **Outils → Personnaliser**.

![](images/Macros_config.jpg )

De cette façon vous pouvez faire de votre macro un véritable outil, comme n\'importe quel outil FreeCAD standard. Ceci, combiné à la puissance des scripts python dans FreeCAD, permet d\'ajouter facilement vos propres outils à l\'interface.

Allez sur [Personnaliser la barre d\'outils](Customize_Toolbars/fr.md) pour une description plus complète.

## Création de macros sans enregistrement 

Vous pouvez également copier / coller directement du code python dans une macro, sans enregistrer d\'action au niveau de l\'interface utilisateur (GUI). Créez simplement une nouvelle macro, modifiez-la et collez votre code. Vous pouvez ensuite enregistrer votre macro de la même manière que vous enregistrez un document FreeCAD. La prochaine fois que vous lancerez FreeCAD, la macro apparaîtra avec l\'intitulé \"Macros installées\" du menu Macro.

Allez sur [Comment installer des Macros](How_to_install_macros/fr.md) pour une description plus détaillée.

## Les dépôts de Macros 

Il existe deux emplacements principaux pour les macros. Le premier est le dépôts des macros officielles évalués par des pairs sur [GitHub](https://github.com/FreeCAD/FreeCAD-macros). La deuxième est la page [Liste des macros](Macros_recipes/fr.md) à partir de laquelle vous pouvez choisir des macros utiles à ajouter à votre installation FreeCAD. Les macros des deux référentiels peuvent être installées via le [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) directement depuis FreeCAD.

## Informations supplémentaires 

-   [Exécuter une macro au démarrage](Macro_at_Startup/fr.md)
-   [Installer des ateliers supplémentaires](Installing_more_workbenches/fr.md)

## Tutoriels

Vous pouvez installer manuellement des extensions, cependant, il est beaucoup plus facile d\'utiliser simplement le [Gestionnaire d\'Addon](Std_AddonMgr/fr.md).

-   [Comment installer des Macros](How_to_install_macros/fr.md)
-   [Comment installer des ateliers supplémentaires](How_to_install_additional_workbenches/fr.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md) [Category:Macros{{\#translation:}}](Category:Macros.md)
