# Installing Helpfile/fr
{{TOCright}}

## Extension d\'aide 

**Remarque    *** les fichiers d\'aide hors ligne de FreeCAD, décrits ci-dessous, sont en cours de retrait. Le système d\'aide de FreeCAD est maintenant géré par l\'[extension Help](https   *//github.com/yorikvanhavre/FreeCAD-Help), que vous pouvez installer via le [Gestionnaire des extensions](Std_AddonMgr/fr.md). L\'extension Help permet d\'accéder à la documentation en ligne, sans avoir besoin de télécharger quoi que ce soit, ou à une copie téléchargeable hors ligne de la documentation, qui peut également être installée via le Gestionnaire des extensions.

## Fichiers d\'aide FreeCAD 

La documentation hors-ligne de FreeCAD est générée à l\'aide de scripts à partir du wiki FreeCAD. Elle a actuellement atteint une taille dépassant les 220 MB. Ces gros fichiers ne font pas partie des installateurs et exécutables de FreeCAD, mais peuvent être installé séparément selon les explications qui suivent.

Les traductions par la communauté sont encouragées et la documentation hors ligne est désormais disponible en français et en italien. D\'autres langues peuvent être à différents stades d\'avancement.

## Télécharger les fichiers d\'aide 

Une documentation hors-ligne fonctionnelle consiste en au moins deux fichiers    * le fichier d\'aide à la configuration Qt **freecad.qhc** et le fichier d\'aide Qt compressé **freecad.qch**. Ils sont rassemblés dans une archive ZIP.

Les fichiers d\'aide peuvent être téléchargés ici    * <https   *//github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD.0_19.Offline.Doc.7z>

Dans le futur ils pourront être installés depuis FreeCAD avec le <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md).

Les fichiers d\'aide ont toujours les mêmes noms    * **freecad.qhc** et **freecad.qch**. Pour avoir différentes versions des fichiers d\'aide, ils doivent être installés dans des répertoires différents. Dans le cas d\'un téléchargement manuel, il suffit de stocker localement le fichier zip et d\'extraire l\'archive dans le répertoire voulu.

## Enregistrer la documentation 

Le système de documentation de FreeCAD utilise Qt Assistant. Vous devriez d\'abord installer ce programme, si vous ne l\'avez pas.

L'organisation réelle de l'aide hors ligne permet à un seul fichier d'aide d'être actif. Il n\'est donc pas possible d\'avoir des fichiers d\'aide dans différentes langues accessibles à partir de FreeCAD en même temps.

Afin de rendre une autre documentation FreeCAD active, les étapes suivantes doivent être appliquées    *

-   Dans FreeCAD, cliquer sur le menu **Aide → Aide**. Le programme Qt Assistant devrait s\'ouvrir.
-   Dans Qt Assistant, cliquer sur le menu **Édition → Préférences**.
-   Dans le dialogue de préférences, cliquer sur l\'onglet **Documentation**.
-   Dans la liste *Documentation référencée*, sélectionner `org.freecad.usermanual` puis cliquer sur le bouton **Supprimer**.
-   Fermer la fenêtre de dialogue avec **OK**, mais ne fermez pas Qt Assistant. C\'est important, sinon un autre fichier d\'aide ne pourra pas être enregistré.
-   Ouvrir à nouveau le dialogue de préférences depuis le menu **Édition → Préférences**.
-   Cliquer sur l\'onglet Documentation puis cliquer sur le bouton **Add...**
-   Dans la fenêtre d\'ouverture de fichiers, naviguer vers le répertoire contenant le fichier d\'aide voulu et sélectionner **freecad.qch**.
-   Fermer la fenêtre de dialogue puis confirmer votre sélection. Dans l\'onglet **Documentation** des préférences, une ligne avec `org.freecad.usermanual` devrait maintenant apparaître.
-   Fermer les **Préférences** en cliquant sur le bouton **OK**.
-   Vous devriez maintenant avoir la nouvelle documentation disponible dans Qt Assistant, et elle sera disponible dans FreeCAD.

## Remarque à propos d\'Ubuntu 

Des difficultés peuvent survenir lors de la tentative d\'installation des packages de documentation sur Ubuntu (par exemple, `freecad-doc` ou `freecad-daily-doc`). Si c\'est le cas, l\'exécution des étapes suivantes vous permettra d\'avoir une documentation hors ligne.

-   Téléchargez les fichiers d\'aide **freecad.qhc** et **freecad.qch** sur <https   *//github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD.0_19.Offline.Doc.7z> et extrayez-les à l\'aide de 7zip.
-   Vous pouvez également obtenir les versions de développement des fichiers d\'aide **freecad.qhc** et **freecad.qch** à partir de [GitHub](https   *//github.com/FreeCAD/FreeCAD/tree/master/src/Doc). Vous devrez [concaténer](http   *//man7.org/linux/man-pages/man1/cat.1.html) les fichiers .part ensemble    * `cat freecad.qch.part00 freecad.qch.part01 freecad.qch.part02 freecad.qch.part03 > freecad.qch`.
-   Avec les privilèges d\'administrateur (par exemple, `sudo`), copiez ou déplacez **freecad.qhc** et **freecad.qch** vers **/usr/share/doc/freecad-doc/**. Si vous utilisez `freecad-daily`, ce sera **/usr/share/doc/freecad-daily-doc/** à la place.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Installing Helpfile/fr
