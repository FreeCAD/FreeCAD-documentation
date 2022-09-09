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


<div class="mw-translate-fuzzy">

La commande **Gestionnaire d\'Addons** ouvre le gestionnaire de modules complémentaires. Avec le Gestionnaire d\'Addons, vous pouvez installer et gérer [ateliers complémentaires](external_workbenches/fr.md) et des [macros](macros/fr.md) fournis par la communauté FreeCAD. Les ateliers et les macros disponibles proviennent de deux dépôts [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) et [FreeCAD-macros](https   *//github.com/FreeCAD/FreeCAD-macros/) et à partir de la page [Liste des macros](Macros_recipes/fr.md).


</div>


<div class="mw-translate-fuzzy">

En raison des modifications apportées à la plate-forme GitHub en 2020, le gestionnaire de modules complémentaires ne fonctionne plus si vous utilisez des versions de FreeCAD inférieure ou égale à 0.17. Vous devez passer à la version [0.18.5](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) ou à une version récente [0.19](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.19_pre). Vous pouvez également installer les addons manuellement, voir [Remarques](#Remarques.md) ci-dessous.


</div>

## Utilisation


<div class="mw-translate-fuzzy">

1.  Sélectionnez l\'option **Outils → <img src="images/Std_AddonMgr.svg" width=16px> Gestionnaire d'Addons** dans le menu.
2.  Si vous utilisez le gestionnaire d\'extensions pour la première fois, une boîte de dialogue s\'ouvrira pour vous avertir que les extensions du gestionnaire d\'Addons ne font pas officiellement partie de FreeCAD. Appuyez sur le bouton **OK** pour confirmer et continuer.
3.  La boîte de dialogue Addons s\'ouvre. Pour plus d\'informations, voir [Options](#Options.md).
4.  Le bouton **<img src="images/Button_valid.svg" width=16px> Tout mettre à jour** ne fonctionne pas pour le moment.
5.  Appuyez sur le bouton **<img src="images/Process-stop.svg" width=16px> Fermer** pour fermer la boîte de dialogue.
6.  Si vous avez installé ou mis à jour un plan de travail, une nouvelle boîte de dialogue s\'ouvre vous informant que vous devez redémarrer FreeCAD pour que les modifications prennent effet.


</div>

## Options

<img alt="" src=images/AddonManager_Main.png  style="width   *600px;">

1.  The Addon manager provides two view layouts   * \"Condensed\" and \"Expanded\". In \"Condensed\" view, each addon takes a single line, and its description is truncated to fit the available space. \"Expanded\" shows additional details, including more of the description text as well as maintainer information, more installation details, etc.
2.  Three different types of addons are supported   * [workbenches](external_workbenches.md), [macros](macros.md), and [preference packs](Preference_Packs.md). You can choose to show just one type, or all of them in a single list.
3.  The list can be limited to show just installed packages, just packages with available updates, or just packages that are not yet installed.
4.  The list can be filtered, searching for a keyword in the title, description, and tags (description and tags must be specified by the addon developer in their addon\'s metadata). The filter can even be a regular expression, for fine-grained control of the exact search term.
5.  The expanded view shows available version information, description, maintainer information, and installation version information, for packages that provide a [package metadata](Package_Metadata.md) file (or for macros with embedded metadata).
6.  Addon data is cached locally, with a variable cache update frequency set in the user preferences.
7.  At any time you can choose to manually update your local cache to see the latest updates available for each addon.
8.  Update checks may be set up to be automatic, or done manually via a button click (configured in user preferences). If GitPython and git are installed on your system then update information is fetched using git. If not, then update information is obtained from any present metadata file.

Clicking on an addon in this view brings up the addon\'s Details page   *

<img alt="" src=images/AddonManager_Details.png  style="width   *600px;">

The details page shows buttons allowing installing, uninstalling, updating, and temporarily disabling an addon. For installed addons it lists the currently installed version and the installation date, and whether that is the most recent version available. Below is an embedded web browser window showing the addon\'s README page (for workbenches and preference packs), or Wiki page (for macros).

## Preferences

The preferences for the Addon manager can be found in the [Preferences Editor](Preferences_Editor#Addon_Manager.md). <small>(v0.20)</small> 

## Remarques


<div class="mw-translate-fuzzy">

-   L\'utilisation des addons n\'est pas limitée à la version FreeCAD à partir de laquelle ils ont été installés. Vous pourrez également les utiliser dans n\'importe quelle autre version de FreeCAD, prise en charge par l\'addon, que vous pourriez avoir sur votre système.
-   Les modules complémentaires disponibles dans le gestionnaire de modules complémentaires ne font pas partie du programme officiel FreeCAD et ne sont pas pris en charge par l\'équipe de développement principale de FreeCAD. Vous devez lire attentivement les informations fournies pour vous assurer que vous savez ce que vous installez.
-   Les rapports de bogues et les demandes de fonctionnalités doivent être adressés directement au créateur de l\'addon en visitant le site Web indiqué. De nombreux développeurs d\'extensions sont des utilisateurs réguliers du [forum de FreeCAD](https   *//forum.freecadweb.org) et peuvent également y être contactés.
-   Si le package [GitPython](https   *//github.com/gitpython-developers/GitPython) est installé sur votre ordinateur, le gestionnaire d\'extensions s\'en servira, ce qui accélérera les téléchargements.
-   Vous pouvez également installer des modules complémentaires manuellement. Voir [Comment installer des ateliers supplémentaires](How_to_install_additional_workbenches/fr.md) et [Comment installer des macros](How_to_install_macros/fr.md).


</div>

## Informations pour les développeurs 

See [Addon](Addon#Information_for_developers.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std AddonMgr/fr
