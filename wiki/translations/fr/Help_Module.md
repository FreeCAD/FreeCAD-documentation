# Help Module/fr
## Description

Le module Aide est responsable du traitement de toutes les demandes de documentation et de son affichage. Jusqu\'à la version 0.21 de FreeCAD, le module Aide est disponible sous la forme d\'une [extension](Std_AddonMgr/fr.md), après quoi il a été inclus dans FreeCAD. Il n\'y a aucun problème à laisser l\'extension installée après la version 0.21.

Le module Aide fournit une page de préférences sous le menu **Édition → Préférences → Général → Aide**, qui permet de spécifier :

-   La source de la documentation : la documentation peut être récupérée à partir d\'emplacements en ligne tels que le [wiki officiel de FreeCAD](https://wiki.freecad.org) (par défaut) ou le [conversion par Markdown](https://github.com/FreeCAD/FreeCAD-documentation), ou à partir d\'un emplacement hors ligne, tel qu\'un dossier où la documentation peut être téléchargée avec le [gestionnaire des extensions](Std_AddonMgr/fr.md).

-   La façon dont la documentation doit être affichée : dans le navigateur de votre bureau, dans une boîte de dialogue séparée, ancrable, qui vous permet par exemple de garder la documentation affichée pendant que vous travaillez (c\'est utile pour les tutoriels), ou dans un nouvel onglet FreeCAD. Notez que dans la version 1.0, les 2ème et 3ème options nécessitent des composants PySide Web. Si ces composants sont manquants, la 1ère option sera utilisée à la place.

-   Un fichier css alternatif : il n\'est utilisé que lorsque vous utilisez les sources Markdown ou hors ligne ci-dessus, et vous permet de personnaliser le style de la documentation.



## Script

Le module Aide consiste essentiellement en un [seul module Python](https://github.com/FreeCAD/FreeCAD/blob/main/src/Mod/Help/Help.py). Sa principale utilisation est la fonction {{Incode|show}}. Il peut récupérer une URL, un fichier local (Markdown ou html) ou trouver une page automatiquement à partir des paramètres définis dans **Préférences → Général → Aide**.

Peu importe ce que vous fournissez, le système reconnaîtra si le contenu est HTML ou Markdown et le rendra de manière appropriée.

Utilisation basique :


```python
import Help
Help.show("Draft Line")
Help.show("Draft_Line")  # fonctionne avec des espaces ou des traits de soulignement
Help.show("https://wiki.freecadweb.org/Draft_Line")
Help.show("https://gitlab.com/freecad/FreeCAD-documentation/-/raw/main/wiki/Draft_Line.md")
Help.show("/home/myUser/.FreeCAD/Documentation/Draft_Line.md")
Help.show("http://myserver.com/myfolder/Draft_Line.html")
```



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External%20Workbenches.md) > [Help](Help_Workbench.md) > Help Module/fr
