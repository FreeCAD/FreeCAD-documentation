---
 GuiCommand:
   Name: Std AddonMgr
   Name/fr: Std Gestionnaire des extensions
   MenuLocation: Outils , Gestionnaire des extensions
   Workbenches: Tous
   Version: 0.17
   SeeAlso: External workbenches/fr, Macros/fr
---

# Std AddonMgr/fr

## Description

La commande **Std Gestionnaire des extensions** ouvre le gestionnaire des extensions. Avec le gestionnaire des extensions, vous pouvez installer et gérer des [ateliers externes](External_workbenches/fr.md), des [macros](Macros/fr.md) et des [kits de préférence](Preference_Packs/fr.md) fournis par la communauté FreeCAD. Par défaut, les extensions disponibles proviennent de deux dépôts, [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) et de la page [Liste des macros](Macros_recipes/fr.md). Si GitPython et git sont installés sur votre système, des macros supplémentaires seront chargées depuis [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/). Des dépôts personnalisés peuvent être ajoutés dans les [Préférences du gestionnaire des extensions](Preferences_Editor/fr#Gestionnaire_des_extensions.md).

En raison des modifications apportées à la plateforme GitHub en 2020, le gestionnaire des extensions ne fonctionne plus si vous utilisez la version 0.17 ou antérieure de FreeCAD. Vous devez passer à la version [0.18.5](https://github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) ou ultérieure. Alternativement, vous pouvez installer les extensions manuellement, voir [Remarques](#Remarques.md) ci-dessous.



## Utilisation

1.  Sélectionnez l\'option **Outils → <img src="images/Std_AddonMgr.svg" width=16px> Gestionnaire des extensions** du menu.
2.  Si vous utilisez le gestionnaire des extensions pour la première fois, une fenêtre de dialogue s\'ouvre pour vous avertir que les extensions du gestionnaire des extensions ne font pas officiellement partie de FreeCAD. Elle présente également plusieurs options relatives à l\'utilisation des données du gestionnaire des extensions. Réglez ces options à votre convenance et appuyez sur le bouton **OK** pour confirmer et continuer.
3.  La fenêtre de dialogue du gestionnaire des extensions s\'ouvre. Pour plus d\'informations, voir [Options](#Options.md).
4.  Si vous avez installé ou mis à jour un atelier, une nouvelle fenêtre de dialogue s\'ouvre pour vous informer que vous devez redémarrer FreeCAD pour que les modifications soient prises en compte.

## Options

<img alt="" src=images/AddonManager_Main.png  style="width:600px;">

1.  Le gestionnaire des extensions propose deux modèles d\'affichage : \"Condensé\" et \"Développé\". Dans la vue \"condensée\", chaque extension occupe une seule ligne, et sa description est tronquée pour s\'adapter à l\'espace disponible. La vue \"développée\" affiche des détails supplémentaires, davantage de texte de la description ainsi que des informations sur le mainteneur, plus de détails sur l\'installation, etc.
2.  Trois différents types d\'extensions sont pris en charge : des [ateliers](external_workbenches/fr.md), des [macros](macros/fr.md), et des [kits de préférences](Preference_Packs/fr.md). Vous pouvez choisir d\'afficher un seul type ou tous les types dans une seule liste.
3.  La liste peut être limitée pour n\'afficher que les paquets installés, que les paquets avec des mises à jour disponibles, ou que les paquets qui ne sont pas encore installés.
4.  La liste peut être filtrée, en recherchant un mot clé dans le titre, la description et les balises (la description et les balises doivent être spécifiées par le développeur de l\'extension dans les métadonnées de l\'extension). Le filtre peut même être une expression régulière, pour un contrôle plus fin du terme de recherche exact.
5.  La vue développée affiche les informations sur la version disponible, la description, les informations sur le responsable et les informations sur la version d\'installation, pour les paquets qui fournissent un fichier de [métadonnées du package](Package_Metadata/fr.md) (ou pour les macros avec métadonnées intégrées).
6.  Les données des extensions sont mises en cache localement, avec une fréquence de mise à jour du cache variable définie dans les préférences de l\'utilisateur.
7.  À tout moment, vous pouvez choisir de mettre à jour manuellement votre cache local pour voir les dernières mises à jour disponibles pour chaque extension.
8.  Les vérifications des mises à jour peuvent être configurées pour être automatiques, ou effectuées manuellement par un clic sur un bouton (configuré dans les préférences de l\'utilisateur). Si GitPython et git sont installés sur votre système, les informations de mise à jour sont récupérées à l\'aide de git. Sinon, les informations de mise à jour sont obtenues à partir de tout fichier de métadonnées présent.

Si vous cliquez sur une extension dans cette vue, la page des détails de l\'extension s\'affiche :

<img alt="" src=images/AddonManager_Details.png  style="width:600px;">

La page de détails présente des boutons permettant d\'installer, de désinstaller, de mettre à jour et de désactiver temporairement une extensions. Pour les extensions installées, elle indique la version installée en cours et la date d\'installation, et précise s\'il s\'agit de la version la plus récente disponible. Une fenêtre de navigateur Web intégrée affiche la page README de l\'extension (pour les environnements de travail et les kits de préférences) ou la page Wiki (pour les macros).



## Préférences

Les préférences du gestionnaire des extensions se trouvent dans [Réglage des préférences](Preferences_Editor/fr#Gestionnaire_des_extensions.md). {{Version/fr|0.20}}



## Tri par score 


{{Version/fr|1.0}}

Le gestionnaire des extensions permet de trier les extensions en fonction d\'un certain nombre de critères. La plupart d\'entre eux sont téléchargés directement à partir des serveurs de FreeCAD (qui les met en cache à partir de GitHub et du wiki FreeCAD), mais l\'un d\'entre eux, le \"Score\", n\'est pas du tout fourni par FreeCAD, et n\'apparaît comme une option que si le paramètre URL des scores est fourni dans les préférences.

L\'URL du score est un chemin d\'accès à un document distant au format JSON répertoriant les extensions et un certain \"score\". Le score peut être calculé de la manière souhaitée par le fournisseur de données, mais il doit s\'agir d\'une valeur entière, les scores les plus élevés étant \"meilleurs\" dans un certain sens. Toute extension non répertoriée se voit attribuer un score de zéro en interne. Le format du fichier est un dictionnaire JSON unique dont la clé est l\'URL de l\'extension (pour les ateliers et les kits de préférences) ou le nom de la macro (pour les macros). Voir [cette source de données](https://gist.githubusercontent.com/chennes/e8f60e80f16e6ffbd057dd47ca36ad2a/raw/7b118cca8e84444c3379919bbd744b99e6ef6711/addon_score_for_testing.json) pour un exemple (notez que le score correspond simplement à la longueur de la description de l\'extension et qu\'il n\'est destiné qu\'à des fins de test et de démonstration).



## Remarques

-   L\'utilisation des extensions n\'est pas limitée à la version FreeCAD à partir de laquelle ils ont été installés. Vous pourrez également les utiliser dans n\'importe quelle autre version de FreeCAD, prise en charge par l\'extension, que vous pourriez avoir sur votre système.
-   Les extensions disponibles dans le gestionnaire des extensions ne font pas partie du programme officiel FreeCAD et ne sont pas pris en charge par l\'équipe de développement principale de FreeCAD. Vous devez lire attentivement les informations fournies pour vous assurer que vous savez ce que vous installez.
-   Les rapports de bogues et les demandes de fonctionnalités doivent être adressés directement au créateur de l\'extension en visitant le site Web indiqué. De nombreux développeurs d\'extensions sont des utilisateurs réguliers du [forum de FreeCAD](https://forum.freecadweb.org) et peuvent également y être contactés.
-   Si le paquet [GitPython](https://github.com/gitpython-developers/GitPython) est installé sur votre ordinateur, le gestionnaire des extensions l\'utilisera, ce qui accélérera les téléchargements.
-   Vous pouvez également installer des extensions manuellement. Voir [Comment installer des ateliers supplémentaires](How_to_install_additional_workbenches/fr.md) et [Comment installer des macros](How_to_install_macros/fr.md).



## Informations pour les développeurs d\'extensions 

Voir [Extension](Addon/fr#Informations_pour_les_d.C3.A9veloppeurs.md)



## Script


{{Version/fr|0.21}}

Certaines fonctionnalités du gestionnaire des extensions sont conçues pour être accessibles via l\'API Python de FreeCAD. En particulier, une extension peut être installée, mise à jour et supprimée via l\'interface Python. La plupart des utilisations de cette API nécessitent de créer un objet avec au moins trois attributs : {{Incode|name}}, {{Incode|branch}} et {{Incode|url}}. Par exemple :


```python
class MyAddonClass:
    def __init__(self):
        self.name = "TestAddon"
        self.url = "https://github.com/Me/MyTestAddon"
        self.branch = "main"
my_addon = MyAddonClass()
```

Votre objet {{Incode|my_addon}} est maintenant prêt à être utilisé avec l\'API du gestionnaire des extensions.



### Utilisation de la ligne de commande (sans interface utilisateur) 

Si votre code doit installer ou mettre à jour une extension de manière synchrone (par exemple, sans interface graphique), le code peut être très simple :


```python
from addonmanager_installer import AddonInstaller
installer = AddonInstaller(my_addon)
installer.run()
```

Notez que ce code se bloque jusqu\'à ce qu\'il soit complet, donc vous ne devriez pas l\'exécuter sur le fil principal de l\'interface graphique. Pour le gestionnaire des extensions, \"install\" et \"update\" sont le même appel : si cette extension est déjà installée, et que git est disponible, il sera mis à jour via \"git pull\". Si elle n\'est pas installée ou a été installée via une méthode d\'installation non git, elle est téléchargée à partir de zéro (en utilisant git si disponible).

Pour désinstaller, utilisez :


```python
from addonmanager_uninstaller import AddonUninstaller
uninstaller = AddonUninstaller(my_addon)
uninstaller.run()
```



### Utilisation de l\'interface utilisateur 

Si vous prévoyez que votre code s\'exécute dans une interface graphique, ou que vous prenez en charge l\'exécution de la version complète de FreeCAD, il est préférable d\'exécuter votre installation dans un fil séparé non GUI, afin que l\'interface graphique reste réactive. Pour ce faire, vérifiez d\'abord si l\'interface graphique est en cours d\'exécution, et si c\'est le cas, créez un {{Incode|QThread}}. (n\'essayez pas de créer un {{Incode|QThread}} si l\'interface graphique n\'est pas active : ils nécessitent une boucle d\'événements active pour fonctionner).


```python
from PySide import QtCore
from addonmanager_installer import AddonInstaller

worker_thread = QtCore.QThread()
installer = AddonInstaller(my_addon)
installer.moveToThread(worker_thread)
installer.success.connect(installation_succeeded)
installer.failure.connect(installation_failed)
installer.finished.connect(worker_thread.quit)
worker_thread.started.connect(installer.run)
worker_thread.start() # Returns immediately
```

Définissez ensuite les fonctions {{Incode|installation_succeded}} et {{Incode|installation_failed}} à exécuter dans chaque cas. Pour la désinstallation, vous pouvez utiliser la même technique, bien qu\'elle soit généralement beaucoup plus rapide et qu\'elle ne bloque pas l\'interface graphique pendant très longtemps, donc en général il est plus sûr d\'utiliser directement le désinstalleur, comme indiqué ci-dessus.



---
⏵ [documentation index](../README.md) > Std AddonMgr/fr
