# Installing on Windows/fr
<div class="mw-translate-fuzzy">

Vous pouvez installer FreeCAD sous Windows en téléchargeant l'un des programmes d'installation ci-dessous:


</div>


{{DownloadWindowsStable}}


<div class="mw-translate-fuzzy">

Après avoir téléchargé le fichier .exe (NSIS Installer), double-cliquer dessus pour lancer le processus d\'installation.


</div>


<div class="mw-translate-fuzzy">

Vous trouverez ci-dessous plus d\'informations sur certaines options techniques. Néanmoins, la plupart des utilisateurs n\'ont pas besoin de plus que les fichiers .exe ci-dessus. Dirigez-vous vers [Démarrer avec FreeCAD](Getting_started/fr.md) une fois l\'installation terminée.


</div>

## Installer simplement avec l\'installateur NSIS 

La meilleure façon d**\'installer FreeCAD sur Windows** est d\'utiliser le package d\'installation téléchargeable ci-dessus. Cette page décrit l\'utilisation et les caractéristiques de *NSIS Installer* pour plus d\'options sur l\'installation.

Si vous souhaitez télécharger la version de développement (risque d'instabilité), allez sur la page [Download](Download/fr.md).

## Chocolatey

Cependant, il est fortement recommandé d\'utiliser un gestionnaire de paquets tel que Chocolatey pour maintenir votre logiciel à jour. Vous pouvez installer Chocolatey en suivant [ces instructions](https://chocolatey.org/install) puis ouvrir un terminal PowerShell en tant qu'administrateur et exécuter :


```python
choco install freecad
```

de temps en temps, vous pouvez mettre à jour votre logiciel avec


```python
choco upgrade freecad
```

pour obtenir la dernière version disponible sur le référentiel Chocolatey. S\'il y a des problèmes avec le paquet Chocolatey, vous pouvez contacter les responsables sur [cette page](https://chocolatey.org/packages/freecad).

## Installation en ligne de commande 

Avec l\'utilitaire en ligne de commande *msiexec.exe*, des fonctionnalités supplémentaires sont disponibles, comme l\'installation non-interactive et l\'installation administrative. Voir les exemples ci-dessous.

### Installation non-interactive 

Avec la commande suivante :


```python
msiexec /i FreeCAD<version>.msi
```

L\'installation peut être programmée. Des paramètres additionnels peuvent être ajoutés à la fin de la ligne de commande, par exemple


```python
msiexec /i FreeCAD-2.5.msi TARGETDIR=R:\FreeCAD25
```

### Interface utilisateur réduite 

Le niveau d\'interface affichable par l\'installeur peut être réglé avec les options /q :

-   /qn - Pas d\'interface
-   /qb - Interface basique - affiche une barre de progression seulement avec le boutton Annulation
-   /qb! - Comme /qb, mais masque le bouton Cancel (Annuler)
-   /qr - Interface réduite - affiche tous les dialogues qui ne nécessitent pas d\'interaction de l\'utilisateur (saute tous les dialogues modaux)
-   /qn+ - Comme /qn, mais affiche le dialogue \"Completed\" (Complété) à la fin
-   /qb+ - Comme /qb, mais affiche le dialogue \"Completed\" à la fin
-   /qn+ - Comme /qn, mais affiche le dialogue \"Completed\" à la fin.

### Répertoire de destination 

La propriété TARGETDIR détermine le répertoire racine de l\'installation FreeCAD. Par exemple, un disque d\'installation différent peut être spécifié par


```python
TARGETDIR=R:\FreeCAD25
```

La valeur TARGETDIR par défaut est \[WindowsVolume\\Programm Files\\\]FreeCAD.

### Installation pour tous les usagers 

L\'ajout de


```python
ALLUSERS=1
```

produit une installation pour tous les usagers. Par défaut, l\'installation non-interactive (/i) n\'installe le paquet que pour l\'utilisateur courant (l\'utilisateur opérant l\'installation). Une installation interactive propose un dialogue réglé par défaut à « tous les utilisateurs » si l\'utilisateur a les privilèges suffisants.

### Sélection de fonctionnalités 

Un certain nombre de propriétés permet la sélection des fonctionnalités à installer, réinstaller, ou supprimer. Le jeu de fonctionnalités de l\'installeur FreeCAD est

-   DefaultFeature - installe le logiciel proprement dit plus les bibliothèques principales
-   Documentation - installe la documentation
-   Source code - installe les sources
-   \... ToDo

De plus, « ALL » spécifie toutes les fonctionnalités. Toutes les fonctionnalités dépendent de DefaultFeature. De ce fait, l\'installation de n\'importe quelle fonctionnalité installe automatiquement la fonctionnalité par défaut. Les propriétés suivantes contrôlent les fonctionnalités à installer ou désinstaller :

-   ADDLOCAL - liste des fonctionnalités à installer sur la machine locale
-   REMOVE - liste des fonctionnalités à désinstaller de la machine locale
-   ADDDEFAULT - liste des fonctionnalités ajoutées dans leurs configurations par défaut (qui est locale pour toutes les fonctionnalités FreeCAD)
-   REINSTALL - liste des fonctionnalités à réinstaller/réparer
-   ADVERTISE - liste des fonctions pour lesquelles une installation prévue doit être effectuée

Il existe quelques propriétés supplémentaires. Consultez la documentation MSDN pour plus de détails.

Avec ces options, l\'ajout de


```python
ADDLOCAL=Extensions
```

installe l\'interpréteur lui-même et enregistre les extensions mais n\'installe rien d\'autre.

## Désinstallation

FreeCAD peut être désinstallé avec


```python
msiexec /x FreeCAD<version>.msi
```

Il n\'est pas nécessaire d\'avoir sous la main le fichier MSI pour la désinstallation. Alternativement, le paquet ou le code produit peut aussi être spécifié. Vous trouverez le code produit en consultant les propriétés du raccourci de désinstallation que FreeCAD installe dans le menu Démarrer.

## Installation administrative 

Avec


```python
msiexec /a FreeCAD<version>.msi
```

une installation \"administrative\" (réseau) peut être initiée. Les fichiers sont décompressés dans le répertoire cible (qui doit être un répertoire réseau), mais aucune autre modification n\'est apportée au système local. En outre, un autre fichier msi (plus petit) est généré dans le répertoire cible que les clients peuvent ensuite utiliser pour effectuer une installation locale (les versions futures pourront également proposer de garder certaines fonctionnalités sur le lecteur réseau).

Il n\'y a pas à ce jour d\'interface pour les installations administratives. Le répertoire de destination doit donc être renseigné en ligne de commande.

Il n\'y a pas de procédure de désinstallation spécifique - supprimer simplement le répertoire de destination s\'il n\'est plus utilisé par aucun client.

## Advertisement

Avec


```python
msiexec /jm FreeCAD<version>.msi
```

Il est possible, en principe, de « publiciser » FreeCAD à une machine (ou à un utilisateur avec /ju). Les icônes apparaîtront dans le menu Démarrer et les extensions seront enregistrées sans que le logiciel ne soit installé. La première utilisation d\'une fonctionnalité conduira à l\'installation de celle-ci.

L\'installeur FreeCAD ne supporte à l\'heure actuelle que la publicité des entrées du menu Démarrer mais pas de raccourcis.

## Installation automatisée sur un groupe de machines 

À l\'aide des stratégies de groupes Windows, il est possible d\'automatiser l\'installation de FreeCAD sur un groupe de machines. Pour ce faire, effectuez les étapes suivantes :

1.  Connectez-vous au contrôleur de domaine
2.  Copiez le fichier MSI vers un dossier partagé dont l\'accès est accordé à toutes les machines cibles.
3.  Ouvrez le composant logiciel MMC « Active Directory users and computers »
4.  Naviguez vers le groupe d\'ordinateurs sur lesquels FreeCAD doit être installé
5.  Ouvrez les Propriétés
6.  Ouvrez les stratégies de groupe
7.  Ajoutez une nouvelle stratégie, puis modifiez-la
8.  Dans Computer Configuration/Software Installation, sélectionnez New/Package
9.  Sélectionnez le fichier MSI à travers le chemin réseau
10. En option, sélectionnez que vous désirez que FreeCAD soit désinstaller si l\'ordinateur quitte le champ d\'application de la stratégie.

La propagation des stratégies de groupe nécessite typiquement du temps pour déployer le paquet de façon fiable. Tous les postes devraient être redémarrés.

## Installation sous Linux à l\'aide de CrossOver Office 

Il est possible d\'installer la version Windows de FreeCAD sur un système Linux à l\'aide de *CXOffice 5.0.1*. Exécutez *msiexec* depuis la ligne de commande de CXOffice, en considérant que le paquet d\'installation est situé dans le répertoire \"software\" qui est assigné à la lettre de disque \"Y:\" :


```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

FreeCAD s\'exécute, mais il a été reporté que l\'affichage OpenGL ne fonctionne pas, comme pour d\'autres programmes fonctionnant sous _, par ex. Google _.

---
[documentation index](../README.md) > Installing on Windows/fr
