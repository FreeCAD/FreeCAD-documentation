---
- GuiCommand   */fr
   Name   *Std AddonMgr
   Name/fr   *Std Gestionnaire d'Addons 
   MenuLocation   *Outils → Gestionnaire d'Addons
   Workbenches   *Tous
   Version   *0.17
   SeeAlso   *[Ateliers externes](External_workbenches/fr.md), [Macros](Macros/fr.md)
---

# Std AddonMgr/fr

## Description

La commande **Gestionnaire d\'Addons** ouvre le gestionnaire de modules complémentaires. Avec le Gestionnaire d\'Addons, vous pouvez installer et gérer [ateliers complémentaires](external_workbenches/fr.md) et des [macros](macros/fr.md) fournis par la communauté FreeCAD. Les ateliers et les macros disponibles proviennent de deux dépôts [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) et [FreeCAD-macros](https   *//github.com/FreeCAD/FreeCAD-macros/) et à partir de la page [Liste des macros](Macros_recipes/fr.md).

Les addons marqués par {{emphasis|Python 2 uniquement}} ne fonctionneront pas dans FreeCAD version 0.19 ou supérieure.

En raison des modifications apportées à la plate-forme GitHub en 2020, le gestionnaire de modules complémentaires ne fonctionne plus si vous utilisez des versions de FreeCAD inférieure ou égale à 0.17. Vous devez passer à la version [0.18.5](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) ou à une version récente [0.19](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.19_pre). Vous pouvez également installer les addons manuellement, voir [Remarques](#Remarques.md) ci-dessous.

![](images/Std_AddonMgr_dialog.png ) 
*Boîte de dialogue du Gestionnaire d'Addons*

## Utilisation

1.  Sélectionnez l\'option **Outils → <img src="images/Std_AddonMgr.svg" width=16px> Gestionnaire d'Addons** dans le menu.
2.  Si vous utilisez le gestionnaire d\'extensions pour la première fois, une boîte de dialogue s\'ouvrira pour vous avertir que les extensions du gestionnaire d\'Addons ne font pas officiellement partie de FreeCAD. Appuyez sur le bouton **OK** pour confirmer et continuer.
3.  La boîte de dialogue Addons s\'ouvre. Pour plus d\'informations, voir [Options](#Options.md).
4.  Le bouton **<img src="images/Button_valid.svg" width=16px> Tout mettre à jour** ne fonctionne pas pour le moment.
5.  Appuyez sur le bouton **<img src="images/Process-stop.svg" width=16px> Fermer** pour fermer la boîte de dialogue.
6.  Si vous avez installé ou mis à jour un plan de travail, une nouvelle boîte de dialogue s\'ouvre vous informant que vous devez redémarrer FreeCAD pour que les modifications prennent effet.

## Options

La boîte de dialogue Addons comporte deux onglets à gauche, l\'un répertoriant les ateliers disponibles et l\'autre répertoriant les macros disponibles. Le panneau d\'information sur la droite affichera la page d\'accueil de l\'addon sélectionné.

### Désinstaller

1.  Sélectionnez un module complémentaire installé dans l\'onglet <img alt="" src=images/Folder.svg  style="width   *16px;"> **Ateliers** ou dans l\'onglet <img alt="" src=images/Applications-python.svg  style="width   *16px;"> **Macros**.
2.  Appuyez sur le bouton **<img src="images/Delete.svg" width=16px> Désinstaller la sélection**.

### Installer/mettre à jour 

1.  Sélectionnez un module complémentaire dans l\'onglet <img alt="" src=images/Folder.svg  style="width   *16px;"> **Ateliers** ou dans l\'onglet <img alt="" src=images/Applications-python.svg  style="width   *16px;"> **Macros**.
2.  Appuyez sur le bouton **<img src="images/Edit_OK.svg" width=16px> Installer/mettre à jour la sélection**.
3.  Si vous souhaitez ajouter une macro à une barre d\'outils personnalisée, n\'oubliez pas de télécharger manuellement le fichier image d\'icône, si disponible, en cliquant sur le lien sur la page d\'accueil dans le panneau d\'informations. Voir [Personnalisation de l\'interface](Interface_Customization/fr#Barre_d.27outils.md).
4.  Pour modifier la position d\'un atelier complémentaire dans la liste des [Ateliers](Std_Workbench/fr.md), voir [Personnalisation de l\'interface](Interface_Customization/fr#Ateliers.md).

### Configuration

1.  Appuyez sur le bouton **<img src="images/Preferences-general.svg" width=16px> Configurer...**.
2.  La boîte de dialogue des options du gestionnaire d\'extensions s\'ouvre.
3.  Cochez éventuellement la case {{CheckBox|TRUE|Rechercher automatiquement les mises à jour au démarrage (nécessite GitPython)}}.
4.  Ajoutez éventuellement des dépôts à la liste **Dépôts personnalisés**. Les modules complémentaires de ces référentiels seront ajoutés sur l\'onglet <img alt="" src=images/Folder.svg  style="width   *16px;"> **Ateliers** ou l\'onglet <img alt="" src=images/Applications-python.svg  style="width   *16px;"> **Macros**.
5.  Choisissez éventuellement les paramètres du proxy.
6.  Appuyez sur le bouton **OK** ou sur le **Annuler** pour fermer la boîte de dialogue.

## Remarques

-   L\'utilisation des addons n\'est pas limitée à la version FreeCAD à partir de laquelle ils ont été installés. Vous pourrez également les utiliser dans n\'importe quelle autre version de FreeCAD, prise en charge par l\'addon, que vous pourriez avoir sur votre système.
-   Les modules complémentaires disponibles dans le gestionnaire de modules complémentaires ne font pas partie du programme officiel FreeCAD et ne sont pas pris en charge par l\'équipe de développement principale de FreeCAD. Vous devez lire attentivement les informations fournies pour vous assurer que vous savez ce que vous installez.
-   Les rapports de bogues et les demandes de fonctionnalités doivent être adressés directement au créateur de l\'addon en visitant le site Web indiqué. De nombreux développeurs d\'extensions sont des utilisateurs réguliers du [forum de FreeCAD](https   *//forum.freecadweb.org) et peuvent également y être contactés.
-   Si le package [GitPython](https   *//github.com/gitpython-developers/GitPython) est installé sur votre ordinateur, le gestionnaire d\'extensions s\'en servira, ce qui accélérera les téléchargements.
-   Vous pouvez également installer des modules complémentaires manuellement. Voir [Comment installer des ateliers supplémentaires](How_to_install_additional_workbenches/fr.md) et [Comment installer des macros](How_to_install_macros/fr.md).

## Informations pour les développeurs 

Si vous avez développé un atelier ou une macro et souhaitez l\'inclure dans le gestionnaire des Addons, lisez la procédure à suivre dans les pages des dépôts ([FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) et [FreeCAD-macros](https   *//github.com/FreeCAD/FreeCAD-macros/)). Si vous ajoutez votre macro à la [Liste des macros](Macros_recipes/fr.md), il n\'y a rien d\'autre à faire, elle sera automatiquement sélectionnée par le gestionnaire Addon.

### Ateliers en Python 

Pour les ateliers Python, vous n\'avez pas besoin d\'une approbation spécifique pour que votre atelier soit ajouté au gestionnaire d\'addons. De plus, comme votre module d\'extension ne fait pas partie du code source de FreeCAD, vous pouvez choisir la licence qui vous convient. Si vous demandez que votre atelier soit ajouté à la liste par défaut du gestionnaire d\'addons (nous n\'ajouterons aucun nouvel atelier sans une demande de ses auteurs), soit en le demandant sur le forum, soit en ouvrant un problème sur le dépôt [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/), votre code restera sur votre propre dépôt git, nous l\'ajouterons simplement comme un sous-module au dépôt [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/). Bien sûr, avant d\'ajouter votre atelier, nous y jetterons un coup d\'œil et nous nous assurerons qu\'il n\'y a rien de potentiellement problématique. Pour plus de détails sur la structuration de votre addon, y compris des informations sur les métadonnées utilisées par le gestionnaire d\'addons, voir [Création d\'atelier](Workbench_creation/fr.md).

### Ateliers C++ 

Si vous développez un atelier en C++, il ne peut pas être exécuté directement par les utilisateurs et doit d\'abord être compilé. Vous avez alors deux options, soit vous fournissez vous-même les versions pré-compilées de votre atelier pour les différents systèmes d\'exploitation, soit vous devez demander à ce que votre code soit fusionné dans le code source de FreeCAD. Pour cela, vous devez utiliser la licence LGPL (ou une licence entièrement compatible comme celle du MIT ou BSD) et présenter vos nouveaux outils à la communauté dans le [forum de FreeCAD](https   *//forum.freecadweb.org) pour être examiné. Une fois que votre code a été testé et approuvé, vous devez créer une nouvelle branche dans le dépôt FreeCAD, si ce n'est pas encore fait, y insérer votre code et ouvrir une demande de retrait (pull request) afin que votre branche soit fusionnée dans le dépôt principal.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std AddonMgr/fr
