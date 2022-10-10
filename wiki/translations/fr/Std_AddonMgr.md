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

La commande **Std Gestionnaire d\'Addons** ouvre le gestionnaire d\'addons. Avec le gestionnaire d\'addons vous pouvez installer et gérer les [ateliers complémentaires](external_workbenches/fr.md), des [macros](macros/fr.md) et des [kits de préférence](Preference_Packs/fr.md) fournis par la communauté FreeCAD. Par défaut, les addons disponibles proviennent de deux dépôts, [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) et la page [Liste des macros](Macros_recipes/fr.md). Si GitPython et git sont installés sur votre système, des macros supplémentaires seront chargées depuis [FreeCAD-macros](https   *//github.com/FreeCAD/FreeCAD-macros/). Des dépôts personnalisés peuvent être ajoutés dans les [Préférences du gestionnaire d\'addons](Preferences_Editor/fr#Gestionnaire_d.27Addons.md).

En raison des modifications apportées à la plateforme GitHub en 2020, le gestionnaire d\'addons ne fonctionne plus si vous utilisez la version 0.17 ou antérieure de FreeCAD. Vous devez passer à la version [0.18.5](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) ou ultérieure. Alternativement, vous pouvez installer les addons manuellement, voir [Remarques](#Remarques.md) ci-dessous.

## Utilisation

1.  Sélectionnez l\'option **Outils → <img src="images/Std_AddonMgr.svg" width=16px> Gestionnaire d'Addons** dans le menu.
2.  Si vous utilisez le gestionnaire d\'addons pour la première fois, une boîte de dialogue s\'ouvre pour vous avertir que les extensions du gestionnaire d\'Addons ne font pas officiellement partie de FreeCAD. Elle présente également plusieurs options relatives à l\'utilisation des données du gestionnaire d\'addons. Réglez ces options à votre convenance et appuyez sur le bouton **OK** pour confirmer et continuer.
3.  La boîte de dialogue du gestionnaire d\'addons s\'ouvre. Pour plus d\'informations, voir [Options](#Options.md).
4.  Si vous avez installé ou mis à jour un atelier, une nouvelle boîte de dialogue s\'ouvre pour vous informer que vous devez redémarrer FreeCAD pour que les modifications soient prises en compte.

## Options

<img alt="" src=images/AddonManager_Main.png  style="width   *600px;">

1.  Le gestionnaire d\'Addons propose deux modèles d\'affichage    * \"Condensé\" et \"Développé\". Dans la vue \"condensée\", chaque addon occupe une seule ligne, et sa description est tronquée pour s\'adapter à l\'espace disponible. La vue \"développée\" affiche des détails supplémentaires, davantage de texte de la description ainsi que des informations sur le mainteneur, plus de détails sur l\'installation, etc.
2.  Trois différents types d\'addons sont pris en charge    * des [ateliers](external_workbenches/fr.md), des [macros](macros/fr.md), et des [kits de préférences](Preference_Packs/fr.md). Vous pouvez choisir d\'afficher un seul type ou tous les types dans une seule liste.
3.  La liste peut être limitée pour n\'afficher que les paquets installés, que les paquets avec des mises à jour disponibles, ou que les paquets qui ne sont pas encore installés.
4.  La liste peut être filtrée, en recherchant un mot clé dans le titre, la description et les balises (la description et les balises doivent être spécifiées par le développeur de l\'addon dans les métadonnées de l\'addon). Le filtre peut même être une expression régulière, pour un contrôle plus fin du terme de recherche exact.
5.  La vue développée affiche les informations sur la version disponible, la description, les informations sur le responsable et les informations sur la version d\'installation, pour les paquets qui fournissent un fichier de [métadonnées du package](Package_Metadata/fr.md) (ou pour les macros avec métadonnées intégrées).
6.  Les données des addons sont mises en cache localement, avec une fréquence de mise à jour du cache variable définie dans les préférences de l\'utilisateur.
7.  À tout moment, vous pouvez choisir de mettre à jour manuellement votre cache local pour voir les dernières mises à jour disponibles pour chaque addon.
8.  Les vérifications des mises à jour peuvent être configurées pour être automatiques, ou effectuées manuellement par un clic sur un bouton (configuré dans les préférences de l\'utilisateur). Si GitPython et git sont installés sur votre système, les informations de mise à jour sont récupérées à l\'aide de git. Sinon, les informations de mise à jour sont obtenues à partir de tout fichier de métadonnées présent.

Si vous cliquez sur un addon dans cette vue, la page des détails de l\'addon s\'affiche    *

<img alt="" src=images/AddonManager_Details.png  style="width   *600px;">

La page de détails présente des boutons permettant d\'installer, de désinstaller, de mettre à jour et de désactiver temporairement un addon. Pour les addons installés, elle indique la version installée en cours et la date d\'installation, et précise s\'il s\'agit de la version la plus récente disponible. Une fenêtre de navigateur Web intégrée affiche la page README de l\'addon (pour les environnements de travail et les kits de préférences) ou la page Wiki (pour les macros).

## Préférences

Les préférences du gestionnaire d\'addons se trouvent dans [Réglage des préférences](Preferences_Editor/fr#Gestionnaire_d.27Addons.md). {{Version/fr|0.20}}

## Remarques

-   L\'utilisation des addons n\'est pas limitée à la version FreeCAD à partir de laquelle ils ont été installés. Vous pourrez également les utiliser dans n\'importe quelle autre version de FreeCAD, prise en charge par l\'addon, que vous pourriez avoir sur votre système.
-   Les modules complémentaires disponibles dans le gestionnaire de modules complémentaires ne font pas partie du programme officiel FreeCAD et ne sont pas pris en charge par l\'équipe de développement principale de FreeCAD. Vous devez lire attentivement les informations fournies pour vous assurer que vous savez ce que vous installez.
-   Les rapports de bogues et les demandes de fonctionnalités doivent être adressés directement au créateur de l\'addon en visitant le site Web indiqué. De nombreux développeurs d\'extensions sont des utilisateurs réguliers du [forum de FreeCAD](https   *//forum.freecadweb.org) et peuvent également y être contactés.
-   Si le paquet [GitPython](https   *//github.com/gitpython-developers/GitPython) est installé sur votre ordinateur, le gestionnaire d\'addons l\'utilisera, ce qui accélérera les téléchargements.
-   Vous pouvez également installer des modules complémentaires manuellement. Voir [Comment installer des ateliers supplémentaires](How_to_install_additional_workbenches/fr.md) et [Comment installer des macros](How_to_install_macros/fr.md).

## Informations pour les développeurs 

Voir [Addon](Addon/fr#Informations_pour_les_d.C3.A9veloppeurs.md)





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std AddonMgr/fr
