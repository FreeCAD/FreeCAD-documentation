# <img alt="SpaceNavigator de 3Dconnexion" src=images/SpaceNavigator.jpg  style="width:200px;"> 3Dconnexion input devices/fr






## Installation des drivers 

### Linux

FreeCAD prend en charge les drivers du projet [Spacenav](http://spacenav.sourceforge.net/). Il s\'agit d\'un projet visant à créer un pilote open-source, qui est compatible avec les pilotes propriétaires de 3Dconnexion.



#### Installer à partir d\'un dépôt 

##### Ubuntu


```python
sudo apt-get install spacenavd
```

Notez cependant que la version 0.6 disponible sur Ubuntu 20.04 (et probablement les plus anciennes) ne semble pas fonctionner. Vous devez alors compiler spacenavd à partir des sources comme expliqué ci-dessous.

##### Fedora


```python
sudo yum install spacenavd
```

##### Debian


```python
apt-get install spacenavd libspnav-dev
```

Spacenav a besoin de ces permissions :

:   
    
```python
    cp ~/.Xauthority /root/
    
```
    

Redémarrez spnavd et FreeCAD :

:   
    
```python
    /usr/bin/spnavd_ctl x11 stop
    /usr/bin/spnavd_ctl x11 start
    
```
    

##### openSUSE


```python
sudo zypper install spacenavd
```



#### Compilation des sources Spacenav 

Ceci est recommandé si votre distribution est une version obsolète.

-   Téléchargez les fichiers suivants :
    -   [spacenavd](https://sourceforge.net/projects/spacenav/files/latest/download) (dernière version)
    -   [libspnav](https://sourceforge.net/projects/spacenav/files/spacenav%20library%20%28SDK%29/) (pour la dernière version libspnav)
    -   [spnavcfg](https://sourceforge.net/projects/spacenav/files/spacenavd%20config%20gui/) (pour la dernière version libspnav)
-   Décompressez les archives dans un dossier dans votre répertoire home.
-   Entrez le répertoire spacenavd-x.x et exécutez les commandes suivantes :

:   
    
```python
    ./configure
    make
    
```
    

-   Si cela réussit, exécutez les commandes suivantes **en tant que root** (ou avec le préfixe sudo).

:   
    
```python
    make install
    ./setup_init
    /etc/init.d/spacenavd start
    
```
    

-   Ceci installe le démon spacenav, le configure pour qu\'il se charge automatiquement au démarrage du système et le démarre sans avoir à redémarrer.
-   Il est maintenant temps de vérifier que votre appareil est correctement détecté. Une fois votre appareil débranché, exécutez la commande suivante, puis branchez-le.

:   
    
```python
    tail -n100 -f /var/log/spnavd.log 
    
```
    

-   Si la sortie ressemble à ceci, vous pouvez continuer.

:   
    
```python
    Device detection, parsing /proc/bus/input/devices
    trying alternative detection, querying /dev/input/eventX device names...
      trying "/dev/input/event1" ... Power Button
      trying "/dev/input/event2" ... 3Dconnexion SpaceNavigator
    using device: /dev/input/event2
    device name: 3Dconnexion SpaceNavigator
    
```
    

-   Maintenant, entrez dans le répertoire nommé libspnav-x.x.x et exécutez les commandes suivantes :

:   
    
```python
    ./configure
    make
    
```
    

-   Si make échoue avec l\'erreur suivante : \...

:   
    
```python
    fatal error: gtk/gtk.h: No such file or directory
    
```
    

-   \... vous devrez alors installer **libgtkmm-2.4-dev**. Voici la procédure sous Ubuntu :

:   
    
```python
    sudo apt-get install libgtkmm-2.4-dev
    
```
    

-   Lorsque make s\'est terminée correctement, exécutez la commande suivante **en tant que root** (ou avec le préfixe sudo).

:   
    
```python
    make install
    
```
    

-   Regardez dans le répertoire libspnav-x.x.x/examples/. Si vous voulez tester votre appareil, compilez et exécutez l\'un de ces deux exemples.

-   Suivez la même procédure pour compiler et installez **spnavcfg**. Assurez-vous de lancer spnavcfg en tant que root sinon aucun paramètre ne sera sauvegardé !



#### Démarrer spacenavd en tant que service systemd au démarrage 

Si vous souhaitez démarrer spacenavd au démarrage en utilisant systemd, procédez comme suit :

-   Allez dans le répertoire où vous clonez le dépôt spacenavd (à la racine du dépôt)
-   \"sudo cp contrib/systemd/spacenavd.service /usr/lib/systemd/system/spacenavd-local.service\".
-   \"sudo systemctl enable spacenavd-local.service\".
-   \"sudo systemctl start spacenavd-local.service\", si vous voulez le démarrer tout de suite.

Ceci n\'est nécessaire que pour l\'installation à partir de la source.



#### Redémarrer spacenavd 

Si parfois SpaceNavigator ne fonctionne plus, il est bon de redémarrer le pilote. Pour le redémarrer, allez dans le terminal et exécutez :


```python
sudo xhost +
sudo /etc/init.d/spacenavd restart
```

Après ceci, redémarrez FreeCAD. Sur certaines distributions, cela est nécessaire à chaque démarrage (boot).



#### Problèmes connus 

Un utilisateur a signalé ce qui suit sur le [forum](https://forum.freecadweb.org/viewtopic.php?p=341327#p341327) :

  Le démon 0.6 Spacenav n'a pas pu ouvrir le fichier de configuration/etc/spnavrc : aucun fichier ou répertoire de ce type. En utilisant les valeurs par défaut.
  ajout d'un appareil.
  nom du périphérique: 3Dconnexion SpacePilot
  using device: /dev/input/event5
  Aucun protocole spécifié
  Impossible d'ouvrir l'affichage X11 ":0.0"

La solution de contournement qui a fonctionné pour eux :


```python 
sudo cp ~/.Xauthority /root/
sudo spnavd_ctl x11 start
sudo systemctl restart spacenavd 
```

### MacOS

Les périphériques d\'entrée 3Dconnexion sont pris en charge sous macOS, à condition que FreeCAD soit compilé et utilisé avec un système sur lequel les pilotes 3Dconnexion sont installés. Vous pouvez avoir besoin de 3DxWare 10.7.2 ou plus pour macOS 12 Monterey.

### Windows

A partir de la version 0.13, la souris 3D est supportée sous Windows. Les pilotes 3Dconnexion doivent être installés. Dans la version 1.0 de FreeCAD, une [nouvelle intégration avec les périphériques 3Dconnexion](https://github.com/FreeCAD/FreeCAD/pull/12929) a été introduite. S\'il est compilé avec cette intégration, seul le matériel récent est pris en charge : pour prendre en charge des périphériques plus anciens, les utilisateurs devront s\'auto-compiler avec la variable cMake FREECAD_3DCONNEXION_SUPPORT réglée sur \"Raw Input\". Les utilisateurs de Windows doivent savoir que le pilote de 3Dconnexion (et non le code de FreeCAD) contient un paquet de télémétrie qui communique à 3Dconnexion des informations sur le logiciel installé.



#### Problèmes connus 

-   Dans la version 1.0 et ultérieure, la modification des paramètres dans la fenêtre de configuration de 3DX peut ne pas avoir les résultats escomptés ([issue](https://github.com/FreeCAD/FreeCAD/issues/14044)). Pour résoudre ce problème :
    1.  Arrêtez le pilote (en exécutant Stop 3DxWare).
    2.  Allez dans **..<user>\AppData\Roaming\3Dconnexion\3DxWare\Cfg** et supprimez le fichier **FreeCAD.xml**.
    3.  Démarrez le pilote (en exécutant Start 3DxWare).
    4.  Lancez FreeCAD et vérifiez si vous pouvez modifier les paramètres de [mouvement de la souris Spaceball](#Mouvement_de_la_souris_Spaceball.md).



## Configurer FreeCAD 


{{VersionPlus/fr|1.0}}

: le manipulateur 3Dconnexion peut être configuré par son pilote (logiciel 3DxWare).


{{VersionMinus/fr|0.21}}

: si une Spaceball est détectée, les onglets suivants de la [fenêtre de dialogue de personnalisation](Interface_Customization/fr.md) peuvent être utilisés pour modifier les paramètres :

<img alt="" src=images/Spaceball_Motion.png  style="width:450px;"> <img alt="" src=images/Spaceball_Buttons.png  style="width:450px;">



### Mouvement de la souris Spaceball 

Dans cet onglet vous avez la possibilité de mettre en place certains paramètres de la souris dans l\'espace général. Ils comprennent :

-   Global Sensitivity : curseur avec possibilité de régler la sensibilité globale
-   Dominant : si vous activez le mode Dominant, seul les axes avec déplacements plus élevés seront considérés
-   Flip YZ : cette option vous permet d\'inverser les axes Y et Z sur la souris 3D
-   Enable Translations : un moyen facile d\'activer/désactiver les traductions
-   Enable Rotations : un moyen facile d\'activer/désactiver les rotations
-   Calibrate : vous permet d\'étalonner space navigator. Il est enfoncé alors que le navigateur d\'espace n\'est pas déplacé.
-   Set To Default : supprime tous les paramètres et leur affecte les paramètres par défaut.

Pour chaque axes, vous avez d\'autres possibilités de définition :

-   Enabled : activer/désactiver les axes
-   Reverse : inverser le mouvement sur les axes
-   Sensitivity : possibilité de définir la sensibilité du curseur



### Boutons de la souris Spaceball 

Lorsque vous ouvrez cet onglet pour la première fois, il sera vide, et, non disponible. Pour l\'activer, vous devez appuyer sur un des boutons de votre space mouse. Une fois que vous l\'avez fait, la liste des boutons s\'affiche sur le côté gauche, et, la liste des commandes sera disponible sur le côté droit.

Pour connecter certaines commandes à un bouton, sélectionnez le bouton sur le panneau de gauche et, la commande sur le panneau de droite. Pour effacer la commande d\'un bouton, appuyez sur \"Clear\".



### Dépannage

Vérifiez si votre installation de FreeCAD est liée à la bibliothèque spacenav. La meilleure façon de le vérifier est de lancer FreeCAD à partir de la ligne de commande du terminal `FreeCAD --log-file /tmp/freecad.log` et refermez-le immédiatement. Ouvrez ensuite le fichier **/tmp/freecad.log** et recherchez les messages suivants :


`Connected to spacenav daemon`

ou


`Couldn't connect to spacenav daemon. Please ignore if you don't have a spacemouse.`

Si aucun de ces messages n\'apparaît, c\'est que votre version de FreeCAD n\'est pas liée à la bibliothèque spacenav. Si le premier message apparaît, cela fonctionne. Le dernier message signifie qu\'il y a probablement un problème avec le démon spacenav.



## En relation 

-   Fil de discussion du forum [spacenav on Windows](https://forum.freecadweb.org/viewtopic.php?f=3&t=51023)
-   Fil de discussion du forum [Space navigator axis confusion](https://forum.freecadweb.org/viewtopic.php?f=8&t=57188).



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User%20Documentation.md) > [3rd Party](Category_3rd%20Party.md) > 3Dconnexion input devices/fr
