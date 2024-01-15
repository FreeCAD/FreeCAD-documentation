# Installing on Mac/fr
FreeCAD peut être installé sur macOS à partir d\'un paquet .dmg que vous pouvez glisser-déposer dans votre dossier Applications, voir la page [Téléchargement](Download/fr.md).

Si vous souhaitez télécharger une version de développement, pouvant être instable, voir la page [Weekly builds download](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds).

Vous pouvez aussi utiliser un gestionnaire de paquets tel que HomeBrew pour maintenir votre logiciel à jour. Les instructions pour installer HomeBrew peuvent être consultées [ici](https://brew.sh/). Lorsque HomeBrew est installé, vous pouvez simplement installer FreeCAD via votre terminal bash avec


```python
brew install --cask freecad
```

et pour utiliser la dernière version disponible sur HomeBrew, vous pouvez exécuter


```python
brew install freecad
```

Si vous rencontrez des problèmes avec la formule HomeBrew Cask ou Formula, vous pouvez signaler [ici](https://github.com/FreeCAD/homebrew-freecad).

Cette page décrit comment installer FreeCAD. Elle inclue également les instructions de désinstallation. Allez à [Démarrer](Getting_started/fr.md) une fois l\'installation terminée.



## Installation simple 

L\'installateur FreeCAD est fourni sous forme d\'application (.app) empaquetée dans un fichier d\'image disque.

Vous pouvez télécharger le tout dernier installateur depuis la page [Téléchargement](Download/fr.md). Après le téléchargement, montez simplement l\'image disque, puis glissez la dans le dossier \"Application\" ou un autre de votre choix.

![](images/mac_installer_1.png )

C\'est tout. Il suffit de cliquer sur l\'application pour lancer FreeCAD. Si vous avez un message \"FreeCAD ne peut pas être ouvert du fait qu\'il vient d\'un développeur non reconnu\", ouvrez le dossier d\'application, faites un clic droit sur l\'app puis cliquer sur \"ouvrir\" et accepter de lancer l\'application.



## Désinstallation

Il n\'y a actuellement pas de programme de désinstallation pour FreeCAD installé avec le package dmg. Pour supprimer complètement FreeCAD et tous les composants installés, faites glisser les fichiers et dossiers suivants vers la corbeille:

-   Dans le répertoire Applications :
    -   /Applications/FreeCAD.app
-   Dans le répertoire Home de l\'utilisateur
    -   \$HOME/Library/Application Support/FreeCAD
    -   \$HOME/Library/Preferences/FreeCAD
    -   \$HOME/Library/Preferences/com.freecad.FreeCAD.plist
    -   \$HOME/Library/Caches/FreeCAD

Si vous avez installé FreeCAD avec homebrew, utilisez la commande `brew uninstall freecad` pour désinstaller /Applications/FreeCAD.app. Les fichiers et répertoires associés dans le Home de l\'utilisateur devront encore être supprimés manuellement.



---
⏵ [documentation index](../README.md) > Installing on Mac/fr
