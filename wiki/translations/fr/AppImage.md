# AppImage/fr
**Depuis le 7 juillet 2019, la communauté FreeCAD observe que le téléchargement d'AppImages à partir de Github semble s'arrêter avant la fin du téléchargement. Nous ne savons pas pourquoi cela se produit. Si cela se produit pour vous, essayez de télécharger à nouveau. Il se pourrait que vous deviez faire plusieurs essais. Une pratique recommandée consiste à utiliser la [https   *//www.freecadweb.org/wiki/AppImage/fr#Mise_à_jour_automatique fonction de mise à jour automatique] AppImage, qui restaurera le téléchargement à partir de l'endroit où il a échoué.**


{{TOCright}}

## Qu\'est ce que AppImage ? 

![](images/AppImage-logo.png ) **Packager une fois et l'exécuter partout. Permet d'être utilisé sur les principales distributions Linux.**

AppImage est un \"paquet binaire universel\" destiné à distribuer une application quel que soit la distribution Linux. En savoir plus à ce sujet en lisant la [page d\'accueil Appimage](https   *//appimage.org) et [AppImage sur Wikipédia](https   *//fr.wikipedia.org/wiki/AppImage)

Pour l\'exécuter, commencez par le rendre exécutable, puis tapez le chemin d\'accès relatif ou complet.


```python
chmod +x FreeCAD_xxx-x86_64.AppImage
./FreeCAD_xxx-x86_64.AppImage
```

Pour les autres types d\'installation, voir [Téléchargements](Download/fr.md).

## AppImages de FreeCAD 


**'''Remarque   *''' Les builds de développement sont maintenant hébergés sur le repo github [https   *//github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds '''FreeCAD-Bundle'''].<br/>Si les liens de téléchargement ci-dessous ne fonctionnent pas, veuillez télécharger manuellement les fichiers à partir du précédent lien, la section "Assets".**

  Stable                                                                                                                Development
   
  ![](images/AppImage-logo.png ) [v0.20](https   *//github.com/FreeCAD/FreeCAD-Bundle/releases/tag/0.20)   ![](images/AppImage-logo.png ) [Weekly build](https   *//github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds)

     * style=\"text-align   * center; font-size   * 150%; \| Available FreeCAD AppImages \|+

**Remarques importantes    ***

-   Le développement se fait quotidiennement et rapidement, le lien de mise à jour d\'AppImage est une cible en mouvement.
-   Le lien de développement ci-dessus devrait être à jour car il est mis à jour via un script.
-   De nombreux utilisateurs du forum utilisent la version de développement.
-   Il peut être exécuté sur le même système en parallèle avec une autre version de FreeCAD.
-   Les utilisateurs utilisent la version en cours de développement pour tirer parti des dernières fonctionnalités et corrections de bugs (FreeCAD ayant un cycle de publication long). Ils l\'utilisent également pour tester et trouver des bugs susceptibles d\'améliorer le développement de FreeCAD.

#### Mot de mise en garde obligatoire 

Pour l\'essentiel, la version de développement est stable mais il est bien sûr important d\'ajouter la déclaration obligatoire pour pouvoir l\'utiliser à vos risques et périls. Bien que la plupart des gens qui utilisent des sauvegardes et « sauvegardent souvent » s\'en sortent plutôt bien.

## Mise à jour automatique 

AppImage dispose d\'un moyen intelligent et économique de mise à jour. Il calcule la différence entre la nouvelle AppImage et l\'ancienne et ne téléchargera que les modifications entre leurs versions. En théorie, l\'utilisateur ne téléchargera qu\'environ 15% à la fois par rapport à une AppImage entièrement nouvelle.

La mise à jour automatique s\'effectue via plusieurs méthodes optionnelles. Il existe actuellement 4 méthodes, 2 via l\'interface graphique (GUI) et 2 via l\'interface en ligne-de-commande/terminal (CLI).

### Mise à jour expérimentale 

Grâce aux efforts de plusieurs développeurs clés, il y a un [effort continu](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=44324) pour intégrer une fonctionnalité permettant une **mise à jour automatique de l\'AppImage dans FreeCAD**. À partir de FC 0.19.21514, il existe maintenant une section AppImage trouvée via **Edition → Préférences → AppImage**. Veuillez tester cette fonctionnalité et faire part de votre expérience par la [discussion du forum](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=44324).

### Méthode graphique 1 (officielle) 

Ceci est l\'application officielle de l\'interface graphique AppImageUpdate.

1.  Télécharger [AppImageUpdate-x86\_64.AppImage](https   *//github.com/AppImage/AppImageUpdate/releases/download/continuous/AppImageUpdate-x86_64.AppImage).
2.  Rendez-le exécutable en faisant un clic droit sur le fichier en allant dans les propriétés et \"Exécuter en tant qu\'exécutable\".
3.  Double-cliquez sur l\'icône AppImage. Une boîte de dialogue apparaîtra et vous serez invité à spécifier quelle AppImage vous souhaitez mettre à jour.
4.  Spécifiez le chemin d\'accès à votre AppImage existante.
5.  Une fois que AppImage est mis à jour, appuyez sur le bouton **Run updated AppImage**.

### Méthode graphique 2 (non officielle) 

Il s\'agit d\'une version non officielle de l\'AppImageUpdate nommée   * **AppImageUpdater**. Elle est encore en développement (au moment de l\'édition de ce wiki) mais néanmoins très agréable à utiliser.

1.  Télécharger [AppImageUpdater-\*-x86\_64.AppImage](https   *//github.com/antony-jr/AppImageUpdater/releases/tag/continuous)
2.  Le rendre exécutable   * 
```pythonchmod +x AppImageUpdater*-x86_64.AppImage```
3.  Exécutez-le   * 
```pythonsource AppImageUpdater*-x86_64.AppImage```
4.  Trouvez votre FreeCAD AppImage actuelle et faites-la glisser sur AppImageUpdater

Résultat   * suivez les invites AppImageUpdater.

### Méthode 1 par lignes de commande (officielle) 

Exécutez les instructions suivantes dans votre terminal    *


```python
wget https   *//github.com/AppImage/AppImageUpdate/releases/download/continuous/appimageupdatetool-x86_64.AppImage
chmod +x ./appimageupdatetool-x86_64.AppImage
./appimageupdatetool.AppImage path/to/old/FreeCAD.AppImage
chmod +x path/to/updated/FreeCAD.AppImage
./path/to/updated/FreeCAD.AppImage
```

Remarques   *

-   Les noms de fichiers seront uniques car les informations de version y sont incorporées. Les instructions ci-dessus sont simplifiées pour plus de commodité.
-   Exécutez `./appimageupdatetool-x86_64.AppImage --help` pour en savoir plus sur les fonctionnalités telles que `--remove-old`, `--overwrite` et `--self-update`.
-   Il existe également une version i386. Voir la page [Version d\'AppImageUpdate](https   *//github.com/AppImage/AppImageUpdate/releases).

A faire   * partager un script qui peut être ajouté comme un alias ou un tâche Cron.

### Méthode 2 par lignes de commande (non officielle) 

De la même manière que les méthodes graphiques ayant une approche officielle et non officielle pour télécharger AppImages, il en va de même pour la ligne de commande. Il s\'agit d\'une option de ligne de commande tierce plus élégante pour télécharger AppImages.

1.  Télécharger [appimageupdater-\*-x86\_64.AppImage](https   *//github.com/antony-jr/AppImageUpdater/releases/tag/continuous-cli)
2.  Rendez le exécutable    * 
```pythonchmod +x appimageupdater*-x86_64.AppImage```
3.  Lancer le    * 
```pythonsource appimageupdater*-x86_64.AppImage /path/to/old/FreeCAD-AppImage.AppImage```

**Resultat**    * Met à jour le fichier AppImage spécifié s\'il existe une mise à jour.

# Expérimental

## Correction du fichier zsync AppImage 

Il peut arriver qu\'une AppImage ne se mette pas à jour parce que son fichier cible a changé d\'une manière ou d\'une autre. Au lieu de télécharger une toute nouvelle appimage, il est possible de réécrire le fichier zsync qui est utilisé par l\'AppImage pour télécharger le delta. Plus d\'informations sont disponibles sur <https   *//github.com/antony-jr/appimage-update-info-writer>.

Cette section nécessite plus de détails.

## Téléchargement via Bittorrent 

L\'équipe chargée du packaging de FreeCAD est en train d\'être explorée (grâce au travail d\'Antony-jr) la possibilité de télécharger un delta d\'appimage de FreeCAD via bittorrent. La question du dépôt se trouve sur <https   *//github.com/FreeCAD/FreeCAD-Bundle/issues/49>

# Section pour les développeurs 


**Remarque   ***

cette section est destinée aux développeurs.

## Dépaqueter AppImages 

Un aspect très pratique de FreeCAD est qu'une grande partie est programmé en [Python](Python/fr.md) ce qui n'a pas besoin d'être compilée manuellement comme en C++. En gros, un fichier Python peut être modifié et, au redémarrage de FreeCAD, ces modifications seront intégrées à l\'application. Un développeur peut rapidement travailler sur la dernière version de FreeCAD en utilisant cette technique et une AppImage. De plus, utiliser AppImage ne modifie en aucune façon l\'environnement de votre système, c\'est-à-dire que rien n\'est installé et aucune variable d\'environnement n\'est modifiée.

### Modifier AppImages 

Une AppImage incorpore un système de fichiers dans celui-ci avec tout le nécessaire pour exécuter l\'application. Pour le modifier, le système de fichiers doit être extrait.


```python
./FreeCAD_xxx.AppImage --appimage-extract
cd squashfs-root/
```

Ouvrez maintenant les fichiers source Python requis dans votre éditeur de code, modifiez-les et enregistrez-les. Puis éxecutez l\'application.


```python
./AppRun
```

### Rempaqueter AppImages 

Si vous avez modifié le code et souhaitez maintenant repackager AppImage avec vos dernières modifications, utilisez la commande [appimagetool-x86\_64](https   *//github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage) sur le système de fichiers extraits.


```python
cd ..
wget "https   *//github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"
chmod +x appimagetool-x86_64.AppImage
./appimagetool-x86_64.AppImage squashfs-root
```

## AppImages personnalisées 

Grâce au travail de **realthunder**, auteur de [App Link](App_Link/fr.md) et [Atelier Assembly3](Assembly3_Workbench/fr.md), il est possible de créer des AppImages personnalisées à l\'aide d\'un ensemble de scripts.

Cela rend très pratique la publication d\'images pour une branche spécifique du code source que d\'autres peuvent tester. Bien que AppImages ne fonctionne que sur Linux, les scripts de realthunder permettent de générer des AppImages également sur Windows et MacOS.

Le dépôt de ces scripts se trouve à [realthunder/FreeCADMakeImage](https   *//github.com/realthunder/FreeCADMakeImage). Veuillez lire le [Readme.md](https   *//github.com/realthunder/FreeCADMakeImage/blob/master/Readme.md) pour plus de détails.

## En relation 

-   Paquets [Snap](Ubuntu_Snap/fr.md).
-   Paquets [Flatpak](Flatpak/fr.md).



[Category   *Packaging](Category_Packaging.md) [Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Testing](Category_Testing.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > [Testing](Category_Testing.md) > AppImage/fr
