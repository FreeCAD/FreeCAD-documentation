# ModernUI Workbench/fr
}

<img alt="Icône de l\'atelier ModernUI" src=images/ModernUI_workbench_icon.svg  style="width   *128px;">


{{TOCright}}

## Introduction

L\'[atelier ModernUI](ModernUI_Workbench/fr.md) est un [Atelier externe](External_workbenches.md) qui remplace l\'interface utilisateur standard. Il possède des fonctionnalités modernes telles que    *

-   Chaque atelier a son onglet ruban.
-   L\'onglet ruban **Modern UI** remplace le menu de niveau supérieur.
-   L\'activation de l\'onglet du ruban d\'un atelier fait apparaître des groupes d\'outils de l\'atelier.
-   Les panneaux tels que la [Vue combinée](Combo_view/fr.md) sont réduits/agrandis au passage de la souris.

## Références

-   Auteur    * Hakan Seven
-   Code source sur github    * [Code source Modern-UI](https   *//github.com/HakanSeven12/Modern-UI)

## Limites et dépannage 

-   Si vous rencontrez un comportement inattendu, essayez d\'abord de désinstaller puis de réinstaller l\'atelier ModernUI.
-   L\'atelier est principalement testé en anglais et peut présenter un comportement inattendu dans d\'autres langues.
-   L\'installation d\'autres ateliers après l\'installation de ModernUI peut poser des problèmes.

## Installation

Installer le avec le <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md).

Remarque    * pour désinstaller, vous devez créer une macro et l\'exécuter. Si vous n\'êtes pas sûr de vous, envisagez de ne pas l\'installer.

### Exécution de Modern UI dans un répertoire autonome 

Pour tester facilement Modern UI sans interférer avec votre configuration standard, vous pouvez le contenir dans un répertoire séparé. La désinstallation de Modern UI s\'effectue alors simplement en supprimant le répertoire. {{Version/fr|0.19}}

#### Linux

Par exemple    *

    $ mkdir modernUI  # new directory that contains Modern UI
    $ cd modernUI
    $ HOME="$PWD" FREECAD_USER_HOME="$PWD" FreeCAD_0.19.AppImage

Lorsque vous démarrez FreeCAD comme cela pour la première fois, vous avez une nouvelle configuration par défaut. Maintenant installez (et configurez) Modern UI. Ceci est essentiellement une [version *portable* de FreeCAD](Download/fr#Note_aux_utilisateurs_de_GNU.2FLinux.md).

Au lieu d\'utiliser la ligne de commande, vous pouvez également [créer une icône de bureau dédiée](Start_up_and_Configuration/fr#D.C3.A9marrage_de_FreeCAD_.C3.A0_partir_du_bureau.md).

#### Windows

Il n\'y a pas encore d\'instructions dédiées pour Windows, cependant, c\'est très similaire à [créer une version portable de FreeCAD sur un support USB](Start_up_and_Configuration/fr#D.C3.A9marrage_de_FreeCAD_.C3.A0_partir_d.27un_medium_USB.md).

## Désinstaller

Des instructions détaillées sont disponibles sur [GitHub](https   *//github.com/HakanSeven12/Modern-UI#uninstallation).

La séquence de désinstallation est la suivante    *

1.  Désinstaller avec le <img alt="" src=images/AddonManager.svg  style="width   *24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md).
2.  Redémarrez FreeCAD.
3.  Créez une macro avec ce code    *```python
    from PySide2 import QtCore, QtGui, QtWidgets
    mw = FreeCADGui.getMainWindow()
    mw.menuBar().show()
     
    WBList = FreeCADGui.listWorkbenches()
    for WB in WBList   *
        FreeCADGui.activateWorkbench(WB)
        for tb in mw.findChildren(QtWidgets.QToolBar)   *
            tb.show()
    
```
4.  Exécuter la macro.
5.  Redémarrez FreeCAD.

## Liens

-   Forum FreeCAD    * <https   *//forum.freecadweb.org/viewtopic.php?f=34&t=44937>
-   Rapport de bogues    * <https   *//github.com/HakanSeven12/Modern-UI>
-   Patreon (pour soutenir l\'auteur)    * <https   *//www.patreon.com/HakanSeven12>




[Category   *External_Workbenches](Category_External_Workbenches.md) [Category   *Addons](Category_Addons.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > [Addons](Category_Addons.md) > ModernUI Workbench/fr
