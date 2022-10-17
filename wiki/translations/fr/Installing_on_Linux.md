# Installing on Linux/fr
{{TOCright}}

## Présentation

L\'installation de FreeCAD sur les systèmes Linux les plus connus a maintenant été approuvée par la communauté, et FreeCAD devrait être directement disponible via le gestionnaire de paquets disponible sur votre distribution. L\'équipe FreeCAD propose également    *

-   Paquets \"officiels\" lorsque les nouvelles versions sont disponibles via [Paquets Snap](Ubuntu_Snap/fr.md), [AppImages](AppImage/fr.md), [Flatpaks](Flatpak/fr.md) et le [PPA](#Version_stable_du_PPA/fr.md).
-   Paquets expérimentaux ou \'bleeding edge\' sont disponibles via les dépôts quotidiens [PPA](#La_version_PPA_en_cours_de_d.C3.A9veloppement/fr.md), [AppImages](AppImage/fr.md), [Ubuntu Snaps](Ubuntu_Snap/fr.md).


<div class="mw-collapsible mw-collapsed toccolours">

## Ubuntu et systèmes dérivés 

De nombreuses distributions Linux sont basées sur Ubuntu et en partagent les dépôts. Outre les variantes officielles (Kubuntu, Lubuntu et Xubuntu), il existe des variantes non-officielles telles que Linux Mint, Voyager ou autres. Les options d\'installation (développez) ci-dessous devraient être compatibles avec ces systèmes.


<div class="mw-collapsible-content">

### Version officielle 

FreeCAD est disponible dans les dépôts officiels d\'Ubuntu et peut être installé via le {{MenuCommand/fr|Software Center}} ou depuis le terminal   *


```python
sudo apt install freecad
```


**Remarque   ***

le dépôt d\'Ubuntu peut être obsolète. Le paquetage peut prendre du retard par rapport au dernier code source stable. Dans ce cas, il est suggéré d\'installer le package à partir du PPA `-stable` ci-dessous. De plus, l\'installation du package `-daily` peut être effectuée pour tester la branche de développement.

### Version stable du PPA 

**Attention    *** Le PPA FreeCAD n\'est actuellement pas maintenu et [recherche des volontaires](https   *//forum.freecadweb.org/viewtopic.php?f=42&t=69055&start=20). Veuillez utiliser une alternative (snap, appimage) jusqu\'à ce que le problème soit résolu !

Les archives de packages personnels (PPA) pour la version stable de FreeCAD sont gérées par la communauté FreeCAD sur Launchpad. Le dépôt Launchpad est appelé [versions stables de FreeCAD](https   *//launchpad.net/~freecad-maintainers/+archive/freecad-stable).

#### Interface graphique 

Pour installer le PPA stable depuis l\'interface graphique (GUI)   *

   *   1\. Accédez à **Logiciel Ubuntu → Logiciels et mises à jour → Sources de logiciels → Autres logiciels**.
   *   2\. Cliquez sur **Ajouter**, puis copiez et collez la ligne suivante

       *   
        
```python
        ppa   *freecad-maintainers/freecad-stable
        
```
        





   *   3\. Ajoutez la source, fermez la boîte de dialogue et rechargez vos sources de logiciels, si nécessaire.

Vous pouvez maintenant trouver et installer la dernière version stable de FreeCAD à partir du **Ubuntu Software Center**.

#### Commandes en ligne 

Pour installer le PPA stable via l\'interface de ligne de commande (CLI)   *

   *   1\. Ajoutez le PPA à vos sources de logiciels   *

       *   
        
```python
        sudo add-apt-repository ppa   *freecad-maintainers/freecad-stable
        
```
        





   *   2\. Récupérer les listes de paquets mis à jour   *

       *   
        
```python
        sudo apt update
        
```
        





   *   3\. Ensuite, installez FreeCAD avec sa documentation hors ligne   *

       *   
        
```python
        sudo apt install freecad freecad-doc
        
```
        


**Remarque   ***

en raison de problèmes d\'empaquetage, dans certaines versions d\'Ubuntu, le paquet `freecad-doc` est entré en collision avec l\'installation de FreeCAD ou de l\'une de ses dépendances. Si c\'est le cas, supprimez le package `freecad-doc` et installez uniquement le package `freecad`. Si le package `freecad-doc` n\'existe pas, ignorez-le.

#### Vérification de l\'installation 

   *   4\. Une fois que vous avez ajouté le PPA stable à vos sources en utilisant l\'une des méthodes ci-dessus, le package `freecad` installera cette version de PPA sur celle fournie par le dépôt Ubuntu Universe. Vous pouvez voir les versions disponibles avec la commande `apt-cache` suivante   *
   *   
    
```python
    apt-cache policy freecad
    
```
    





   *   La sortie devrait ressembler à ce qui suit (bien sûr, les informations de version varieront)   *


```python
freecad   *
  Installed   * (none)
  Candidate   * 2   *0.18.4+dfsg1~201911060029~ubuntu18.04.1
  Version table   *
     2   *0.18.4+dfsg1~201911060029~ubuntu18.04.1 500
        500 http   *//ppa.launchpad.net/freecad-maintainers/freecad-stable/ubuntu bionic/main amd64 Packages
     0.16.6712+dfsg1-1ubuntu2 500
        500 http   *//archive.ubuntu.com/ubuntu bionic/universe amd64 Packages
ubuntu@ubuntu   *~$ apt-cache policy freecad-doc
```


   *   5\. Exécutez la version stable (PPA) de FreeCAD à partir de l\'interface graphique (GUI) ou par la commande en ligne (CLI). Cette dernière méthode est la suivante   *
   *   
    
```python
    ./freecad
    
```
    

### La version PPA en cours de développement 

Comme FreeCAD est en développement constant, vous souhaiterez peut-être installer le package **daily** pour suivre les dernières améliorations et corrections de bogues. Le dépôt est également hébergé sur Launchpad et s\'appelle [freecad-daily](https   *//launchpad.net/~freecad-maintainers/+archive/freecad-daily).

Cette version est compilée quotidiennement à partir du dépôt officiel maître. Attention, bien qu\'elle contienne de nouvelles fonctionnalités et corrections de bugs, elle peut aussi avoir des bugs plus récents et être instable.

Ajoutez le daily PPA à vos sources logicielles, mettez à jour les listes de packages et installez le daily package   * 
```python
sudo add-apt-repository ppa   *freecad-maintainers/freecad-daily
sudo apt-get update
sudo apt-get install freecad-daily
```

Chaque jour, vous pouvez mettre à jour la dernière version en cours   * 
```python
sudo apt-get update
sudo apt-get install freecad-daily
```


**Remarque   ***

dans certains cas, le nouveau code ou les dépendances ajoutés à FreeCAD provoqueront des erreurs d\'empaquetage. Si cela se produit, le daily package ne peut pas être généré tant que les responsables ne résolvent pas les problèmes manuellement. Si vous souhaitez continuer à tester le dernier code, vous devez obtenir le code source et compiler directement FreeCAD; pour des instructions, voir [compilation](compiling/fr.md).

Exécutez la version daily (PPA) de FreeCAD   *

   *   
    
```python
    freecad-daily
    
```
    


**Remarque   ***

il est possible d\'installer les paquets `-stable` et `-daily` dans le même système. Cela est utile si vous souhaitez utiliser une version stable et pouvoir toujours tester les dernières fonctionnalités en développement. Notez que l\'exécutable pour la version quotidienne est `freecad-daily`, mais pour la version stable, il s\'agit simplement de `freecad`.


</div>


</div>

## Debian et autre dérivés de Debian 

Depuis la version Debian Lenny, FreeCAD est disponible depuis les dépôts Debian et peut être installé par Synaptic ou simplement par    *


```python
sudo apt-get install freecad
```


<div class="mw-collapsible mw-collapsed toccolours">

## OpenSUSE

FreeCAD est généralement installé avec YAST (abbr. Yet another Setup Tool), l'outil de configuration et de configuration du système d'exploitation Linux, ou dans n'importe quel terminal/console (les droits en mode root sont requis) avec   *

   *   
    
```python
    zypper install FreeCAD
    
```
    


**Remarque   ***

Cette procédure ne couvre que l\'installation des versions du programme FreeCAD **stables** officiellement publiées en fonction des liens installés vers les dépôts de packages de programmes de votre version de système d\'exploitation. Le package openSUSE *peut être obsolète* car le package peut être en retard sur le dernier code source stable. Dans ce cas, il est suggéré d\'installer le package manuellement à partir des dépôts sources indiqués ci-dessous (Expand).


<div class="mw-collapsible-content">

Un vaste programme de version pour les versions de packages FreeCAD est proposé. Veuillez visiter pour un aperçu   *

**[Aperçu sur les dépôts sur openSUSE](https   *//software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=FreeCAD)**

Généralement, pour sélectionner la bonne distribution openSUSE, il est nécessaire de cliquer sur le bouton **View**.

### Stable

La version stable du package   * [Dépôts stables sur openSUSE](https   *//software.opensuse.org/package/FreeCAD). La version de distribution openSUSE correcte doit être sélectionnée dans la partie inférieure de la page Web.

Remarque   * openSUSE propose plusieurs options lors du téléchargement de FreeCAD. Pour afficher ces options, visitez [Aperçu sur les dépôts stables sur openSUSE](https   *//software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=FreeCAD).

### Développement

Les dernières versions de développement AKA **unstable**   * [Liste des dépôts instables sur openSUSE](https   *//software.opensuse.org/download.html?project=science%3Aunstable&package=FreeCAD)

Il est recommandé de récupérer les paquets binaires directement. Sélectionnez ensuite la distribution appropriée pour votre OS openSUSE installé.


</div>


</div>

## Gentoo

FreeCAD peut être compilé ou installé simplement avec cette commande   *


```python
emerge freecad
```


<div class="mw-collapsible mw-collapsed toccolours">

## Fedora

FreeCAD est inclus dans les packages officiels de Fedora depuis Fedora 20. Il peut être installé par ligne de commande en faisant   *


```python
sudo dnf install freecad
```


<div class="mw-collapsible-content">

Sur les versions précédentes de Fedora, c'était   *


```python
sudo yum install freecad
```

Les gestionnaires de paquets d\'interface graphique peuvent également être utilisés. Rechercher \"freecad\". La version officielle du paquet a tendance à être en retard sur les versions de FreeCAD. [Package   * freecad](http   *//rpms.remirepo.net/rpmphp/zoom.php?rpm=freecad) affiche les versions incluses dans les référentiels Fedora dans le temps et les versions.

Des versions plus récentes peuvent être obtenues en téléchargeant l'un des fichiers [.AppImage](https   *//github.com/FreeCAD/FreeCAD/releases/)Les versions du logiciel sont dans les dépôts de github et fonctionnent très bien sur Fedora.

Si vous souhaitez obtenir les dernières versions en cours de développement, FreeCAD est également disponible sur [copr](https   *//copr.fedorainfracloud.org/groups/g/freecad/coprs/). Pour installer la version, dans un terminal, tapez   *


```python
sudo dnf copr enable @freecad/nightly
sudo dnf install freecad
```

Cela laisse le copr dépôt reste actif.


```python
sudo dnf upgrade
```

La commande ci-dessus ou l\'équivalent mettra à jour vers la dernière version de FreeCAD avec les mises à jour de n'importe quel autre dépôt actif. Si vous voulez quelque chose d\'un peu plus stable, vous pouvez désactiver \@freecad/nightly à nouveau après l'installation initiale. Le copr dépôt ne conserve que les versions des 2 dernières semaines. Ce n\'est pas une solution si vous voulez choisir une version particulière plus ancienne.

Des instructions sont également disponibles sur [compiler FreeCAD vous-même](Compile_on_Linux/fr.md), y compris un script spécifiquement pour Fedora. Avec une modification mineure, pour extraire le commit spécifique du git, n\'importe quelle version depuis FreeCAD 0.15 peut être construite sur n\'importe quelle distribution depuis Fedora 21.


</div>


</div>

## Arch

Installer FreeCAD sur Arch Linux et ses dérivés (ex. Manjaro)   *


```python
pacman -S freecad
```

## Autres

Si votre distribution Linux offre FreeCAD mais qu\'elle n\'est pas documentée sur cette page, merci de nous le dire sur le [forum](http   *//forum.freecadweb.org/viewforum.php?f=21)!

Plusieurs paquets FreeCAD non-officiels sont disponibles sur Internet, par exemple pour Slackware ou Fedora. Une recherche Internet peut donner quelques résultats.

### Installation sous d\'autres systèmes Linux/Unix 

De nombreuses distributions Linux courantes incluent maintenant un FreeCAD précompilé dans les packages standard. C\'est souvent obsolète, mais c\'est un endroit pour commencer. Vérifiez les gestionnaires de paquets standard pour votre système. L\'une des listes de commandes (partielles) suivantes pourrait installer la version officielle de FreeCAD pour votre distribution à partir du terminal. Ceux-ci ont probablement besoin de privilèges d\'administrateur.


```python
apt-get install freecad
dnf install freecad
emerge freecad
slackpkg install freecad
yum install freecad
zypper install freecad
pacman -Sy freecad
```

Le nom du paquet est sensible à la casse, donc essayez \"FreeCAD\" ainsi que \"freecad\". Si cela ne fonctionne pas pour vous, soit parce que votre gestionnaire de paquets n\'a pas de version FreeCAD précompilée disponible, soit parce que la version disponible est trop ancienne pour vos besoins, vous pouvez essayer d\'installer les paquets [Flatpak](Flatpak/fr.md) ou [Snap](Ubuntu_Snap/fr.md) (ceux-ci fonctionnent sur la plupart des distributions Linux x86_64) ou essayer de télécharger l\'un des programmes suivants [.AppImage](https   *//github.com/FreeCAD/FreeCAD/releases/) disponibles à partir du dépôt github. Elles ont également tendance à fonctionner sur la plupart des distributions Linux x86_64, sans installation particulière. Assurez-vous simplement que le fichier téléchargé est marqué comme exécutable, puis exécutez-le.

Si cela ne suffit toujours pas et que vous ne pouvez pas localiser une autre source d\'un paquet précompilé, vous devrez [compiler FreeCAD vous-même](Compile_on_Linux/fr.md).

## Etape suivante 

Une fois FreeCAD installé, il est temps de [commencer](Getting_started/fr.md)!







[Category   *Common Questions](Category_Common_Questions.md) [Category   *Developer Documentation](Category_Developer_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [Developer Documentation](Category_Developer Documentation.md) > Installing on Linux/fr
