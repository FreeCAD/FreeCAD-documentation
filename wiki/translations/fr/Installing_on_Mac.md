# Installing on Mac/fr





FreeCAD peut être installé sur macOS à partir d\'un paquet .dmg que vous pouvez glisser et déposer dans votre dossier Applications :


{{DownloadMacStable}}

et la weekly build (version instable) peut être téléchargée à partir de

<img alt="" src=images/Nightly.png  style="width:30px;">[Weekly](https://github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds)

Vous pouvez aussi utiliser un gestionnaire de paquets tel que HomeBrew pour maintenir votre logiciel à jour. Les instructions pour installer HomeBrew peuvent être consultées [ici](https://brew.sh/). Lorsque HomeBrew est installé, vous pouvez simplement installer FreeCAD 0.18.4 via votre terminal bash avec


```python
brew install --cask freecad
```

et pour utiliser la dernière version disponible (0.19pre) sur HomeBrew, vous pouvez exécuter


```python
brew install freecad
```

Si vous rencontrez des problèmes avec la formule HomeBrew Cask ou Formula, vous pouvez signaler [ici](https://github.com/FreeCAD/homebrew-freecad).

Cette page décrit comment installer FreeCAD. Elle inclue également les instructions de désinstallation. Une fois installé, vous pouvez [démarrer](Getting_started/fr.md) !

## Installation simple 

L\'installateur FreeCAD est fourni sous forme d\'application (.app) empaquetée dans un fichier d\'image disque.

Vous pouvez télécharger le tout dernier installateur depuis la page [Téléchargement](Download/fr.md). Après le téléchargement, montez simplement l\'image disque, puis glissez la dans le dossier \"Application\" ou un autre de votre choix.

![](images/mac_installer_1.png )

C\'est tout. Il suffit de cliquer sur l\'application pour lancer FreeCAD. Si vous avez un message \"FreeCAD ne peut pas être ouvert du fait qu\'il vient d\'un développeur non reconnu\", ouvrez le dossier d\'application, faites un clic droit sur l\'app puis cliquer sur \"ouvrir\" et accepter de lancer l\'application.

## Désinstallation

Il n\'y a actuellement pas de programme de désinstallation pour FreeCAD installé avec le package dmg. Pour supprimer complètement FreeCAD et tous les composants installés, faites glisser les fichiers et dossiers suivants vers la corbeille:

-   Sous /Applications :
    -   FreeCAD

Si vous avez installé FreeCAD avec homebrew, utilisez simplement la commande `brew uninstall freecad`. C\'est tout.






