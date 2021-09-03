 {{TOCright}}


{{Fake heading|sub=4|< Retour à [FreeCAD comment importer exporter](FreeCAD_Howto_Import_Export/fr.md)}}

## Pourquoi est-il difficile de prendre en charge les fichiers DWG dans FreeCAD? 

Le **format DWG est un format de fichier binaire fermé** (propriétaire) qui n\'est pas directement pris en charge par FreeCAD. Il faut d\'abord un convertisseur de fichier tiers externe pour convertir puis importer la conversion dans FreeCAD pour l\'utiliser.

Veuillez noter qu\'à l\'heure actuelle, il est impossible d\'importer des fichiers DWG 3D dans FreeCAD. Les données 3D sont intégrées dans le format binaire .SAT (ACIS), qui est propriétaire et non-documenté.

## De quoi ai-je besoin pour pouvoir importer des fichiers DWG? 

### Convertisseur ODA (anciennement convertisseur Teigha) 

-   Page d\'accueil : <https://www.opendesign.com/guestfiles/oda_file_converter>
-   licence : freeware
-   optionnel, utilisé pour permettre l\'importation et l\'exportation de fichiers DWG

Le Convertisseur ODA est un petit utilitaire disponible gratuitement qui permet de convertir plusieurs versions de fichiers DWG et DXF. FreeCAD peut l\'utiliser pour permettre l\'importation et l\'exportation DWG, en convertissant de manière transparente les fichiers DWG au format DXF , puis FreeCAD utilise son importateur DXF standard pour importer le contenu du fichier. Les restrictions de l\'[importateur DXF](Draft_DXF/fr.md) s\'appliquent.

#### Installation

L\'installation se fait sur toutes les plate-formes en téléchargeant et en installant le logiciel disponible sur <https://www.opendesign.com/guestfiles/oda_file_converter>. Si après l\'installation l\'utilitaire n\'est pas trouvé automatiquement par FreeCAD, vous pourriez avoir besoin de donner le chemin de l\'exécutable du convertisseur manuellement, pour ce faire allez dans le menu Édition → Préférences → Importer-Exporter → DWG et renseignez le chemin d'accès.

Pour plus de détails, voir \[<https://wiki.freecadweb.org/wiki/index.php?title=Dxf_Importer_Install/fr#Troisi.C3.A8me_.C3.A9tape_>: ce tutoriel\].

#### Utilisation

Le programme peut être utilisé en ligne de commande ou avec l\'interface graphique. N\'oubliez pas de convertir les fichiers DWG au format ASCII.

Le format de la ligne de commande est :

1.  Dossier d\'entrée désigné
2.  Dossier de sortie désigné
3.  Version de la sortie {\"ACAD9\",\"ACAD10\",\"ACAD12\", \"ACAD13\",\"ACAD14\", \"ACAD2000\",\"ACAD2004\", \"ACAD2007\",\"ACAD2010\"}
4.  Type de sortie fichier {\"DWG\", \"DXF\", \"DXB\"}
5.  Dossier d\'entrée récursif {\"0\", \"1\"}
6.  Audit de chaque fichier {\"0\", \"1\"}
7.  \[optionnel\] Filtre de fichiers en entrée (par défaut : \"\*.DWG ; \*.DXF\")

**Exemple pour Linux**
TeighaFileConverter \"/home/DWG-data\" \"/home/DXF-data\" \"ACAD2010\" \"DXF\" \"0\" \"1\" \"test.dwg\" Le deuxième numéro (audit) doit être 1 sinon cela ne fonctionnera pas.

**Exemple pour Windows**
\"C:\\Program Files\\ODA\\Teigha File Converter 3.08.2\\TeighaFileConverter.exe\" \"Path-To-Input-Directory\" \"Path-To-Output-Directory\" \"ACAD2010\" \"DXF\" \"0\" \"1\" \"Name-Of-A-Test-File.dwg\"

### Atelier CADExchanger 

L\'installation de l\'atelier CADExchanger permet de travailler avec des fichiers DWG grâce à l\'intégration avec le produit de conversion de fichiers commercial payant [CADExchanger](https://cadexchanger.com/). Suivez simplement les instructions du [dépôt GitHub](https://github.com/yorikvanhavre/CADExchanger). Vous pouvez discuter de cet atelier sur [son fil de discussion](https://forum.freecadweb.org/viewtopic.php?f=9&t=22227&p=462421).

Pour le moment, la méthode CADExchanger est la seule qui permet de travailler avec des fichiers DWG 3D, en les convertissant dans d\'autres formats 3D.

## FreeCAD v0.19 et LibreDWG 

Depuis la version 0.19, FreeCAD n\'a plus besoin du convertisseur ODA et peut utiliser directement libreDWG. Sachez que, puisque libreDWG est un travail en cours, en fonction de votre dossier, les résultats peuvent ne pas être les mêmes.

-   page d\'accueil: <https://www.gnu.org/software/libredwg/>
-   licence: GPLv2 ou version ultérieure
-   facultatif, utilisé pour activer l\'importation et l\'exportation de fichiers DWG

GNU LibreDWG est une bibliothèque C libre pour gérer les fichiers DWG. Elle vise à remplacer gratuitement les bibliothèques SDK de l\'Open Design Alliance Drawings.

## Installation 

### Versions AppImage 

LibreDWG est inclus dans la v 0.19\_pre appimages [1](https://forum.freecadweb.org/viewtopic.php?f=8&t=39827&start=20#p372933)

### Windows

LibreDWG peut être configuré pour fonctionner sous Windows en téléchargeant et en décompressant le [binaire pré-compilé Windows](https://github.com/LibreDWG/libredwg/releases) et [en ajoutant le dossier au chemin système de vos versions Windows](https://duckduckgo.com/?t=ffab&q=how+to+add+a+folder+to+your+windows+system+path).

### Systèmes Linux/Unix 

git clone [https://git.savannah.gnu.org/git/libredwg.git](https://git.savannah.gnu.org/git/libredwg.git)
cd libredwg
mkdir build
cd build
cmake ..
make
make install (ou utiliser checkinstall, ou simplement localiser & copier l'utilitaire dwg2dxf dans le chemin de vos exécutables, il sera alors autodétecté par FreeCAD)

### openSUSE

Pour éviter les problèmes d\'exécution du programme, vous devez utiliser le paquetage LibreDWG compilé pour la distribution openSUSE OS installée. LibreDWG est généralement installé avec **YAST** (abréviation de Yet another Setup Tool), l\'outil d\'installation et de configuration du système d\'exploitation Linux.

L\'utilisateur plus expérimenté obtient d\'abord un aperçu des paquets possibles fournis. **Remarque:** openSUSE a plusieurs options à choisir lors du téléchargement de LibreDWG. Pour voir ces options, allez sur [Survey of provided LibreDWG packages on openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=libredwg).

Pour les ordinateurs de bureau, les ordinateurs portables et les serveurs Intel ou AMD 64 bits, la version (x86\_64) est à choisir. Ainsi, **libredwg0** et **libredwg-tools** sont le bon choix à installer.

Il est recommandé de récupérer les paquets binaires directement. Sélectionnez ensuite la distribution appropriée pour votre OS openSUSE installé.

Dans n\'importe quel terminal/console (droits root requis), l\'installation s\'effectuera avec :

:   
    
```python
    zypper install libredwg0 libredwg-tools
    
```
    

Ensuite, chaque importation de fichier \*.dwg devrait fonctionner correctement.

## Quelles sont les alternatives? 

### DoubleCAD XT 

Il y a aussi DoubleCAD XT (https://www.turbocad.com/content/doublecad-xt-v5). Ce programme est libre d\'utilisation pour une utilisation personnelle ou commerciale. Vous devez vous enregistrer pour recevoir le code d\'activation via E-Mail. Ce programme ne fonctionne que sous Windows. À noter qu\'il ne semble pas avoir été mis à jour depuis des années.

### NanoCAD 5.0 

Il y a aussi nanoCAD 5.0 (https://nanocad.com/products/nanoCAD/download/). Le programme est gratuit pour un usage personnel et commercial. Il demande une inscription gratuite pour recevoir un code d\'activation par e-mail. Ce programme est sous Windows uniquement.

### Exporter ses fichiers AutoCAD dans un format reconnu de FreeCAD 

Exportez votre fichier AutoCAD dans un des nombreux formats reconnu par FreeCAD, à savoir DXF R12 ou R14, SVG et si votre version le supporte IGES. Toutes ces versions sont de meilleures alternatives au format DWG lorsque vous utilisez FreeCAD.

Il est important de savoir que, contrairement à ce que l\'on croit, il n\'y a pas de différence entre le contenu d\'un fichier enregistré dans les formats DWG ou DXF, à condition de travailler avec la même version (ex. DWG 2014 vs 2014 DXF). Les deux formats sont maintenus par Autodesk, et ils utilisent tous deux exactement les mêmes caractéristiques. La différence est que le fichier DWG est fermé (fichier codé) tandis que le fichier DXF est ouvert (fichier texte).

## Que puis-je faire pour aider ? 

### Promouvoir l\'utilisation des formats alternatifs 

Autrement dit, n\'acceptez plus des travaux effectués au format DWG. Dans la pratique, c\'est plus facile à dire qu\'à faire. Pourtant, ce ne serait pas une mauvaise pratique pour les utilisateurs et les partisans de FreeCAD d\'éviter d\'utiliser le format DWG chaque fois que c\'est possible.

### Utiliser la bibliothèque LibreDWG et rapporter des bogues 

Dans la version de développement comme mentionné ci-dessus, vous pouvez passer du convertisseur ODA propriétaire à la bibliothèque du logiciel libre LibreDWG pour les fichiers DWG (et DXF). Veuillez le faire et signaler tout problème que vous rencontrez.


 

[Category:File\_Formats{{\#translation:}}](Category:File_Formats.md) [Category:Common Questions{{\#translation:}}](Category:Common_Questions.md)
