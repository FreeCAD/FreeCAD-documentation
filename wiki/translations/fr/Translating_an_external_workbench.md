# Translating an external workbench/fr
Dans les notes suivantes, `"context"` doit être le nom de votre addon ou de votre atelier, par exemple, `"MySuperAddon"` ou `"DraftPlus"`, etc. Ce contexte permet de regrouper toutes les traductions de votre code sous le même nom, afin qu\'elles soient plus facilement identifiables par les traducteurs. C\'est-à-dire qu\'ils sauront exactement à quel addon ou atelier une chaîne particulière appartient.

**Remarque** : Voici un script tout-en-un qui automatise la procédure complète mentionnée ci-dessous (il est tout de même conseillé de lire la procédure pour savoir ce que le script doit faire) : <https://github.com/yorikvanhavre/BIM_Workbench/blob/master/utils/updateTranslations.py>.

## Préparer les sources 

### Généralités

-   Ajouter un dossier `translations/`. Vous pouvez le nommer autrement, mais ce sera plus facile car c\'est la même chose dans FreeCAD. Dans ce dossier, vous placerez les fichiers `.ts` (les fichiers de traduction \"source\") et les fichiers `.qm` (fichiers de traduction compilés).
-   Seul le texte affiché pour l\'utilisateur dans l\'interface de FreeCAD doit être traduit. Le texte affiché uniquement dans la console Python ne doit pas être traduit.
-   Le texte imprimé sur `FreeCAD.Console` apparaît dans la \"Vue Rapport\" et doit donc être traduit. La \"vue Rapport\" est différente depuis la console Python.

### Dans chaque fichier Python .py 

-   Dans chaque fichier où vous devez traduire du texte, vous devez définir une fonction `translate()`. Un moyen simple consiste à utiliser celui de [l\'atelier Draft](Draft_Workbench/fr.md) :


```python
from DraftTools import translate
```

A partir de FreeCAD 0.19, le module FreeCAD définit également une fonction de traduction (translate()), il est préférable d\'utiliser celle-ci : 
```python
from FreeCAD.Qt import translate
```

-   Tout le texte devant être traduit doit être passé à travers la fonction `translate()`.


```python
print("Mon texte")
```

devient 
```python
print(translate("context", "Mon texte"))
```

Ceci peut être utilisé n'importe où : dans `print()`, dans `FreeCAD.Console.PrintMessage()`, dans les boîtes de dialogue Qt, etc. Les fonctions `FreeCAD.Console` n'ajoutent pas automatiquement le caractère de nouvelle ligne (`\n`) ; vous pouvez l\'ajouter à la fin si vous le souhaitez. Ce caractère n\'a pas non plus besoin de traduction, il peut donc être en dehors de la fonction de traduction : 
```python
FreeCAD.Console.PrintMessage(translate("context", "My text") + "\n")
```

-   Si vous utilisez des fichiers `.ui` créés avec QtDesigner il n\'y a rien d'autre à fait avec eux.
-   Lors de la création de nouveaux objets, ne traduisez pas le \"Name\" de l\'objet. Traduisez plutôt le \"Label\" de l\'objet. La différence est qu\'un \"Name\" est unique ; il reste le même pendant toute la vie de l\'objet ; alors qu\'un \"Label\" peut être modifiée par l\'utilisateur à sa guise.
-   Lors de la création de propriétés pour vos objets, ne traduisez pas le nom de la propriété. Mais placez la description à l\'intérieur de `QT_TRANSLATE_NOOP`:


```python
obj.addProperty("App::PropertyBool", "MyProperty", "PropertyGroup", QT_TRANSLATE_NOOP("App::Property", "C'est ce que ma propriété fait"))
```

N\'utilisez pas votre propre `"context"` dans ce cas particulier. Conservez `"App::Property"`.

-   Ne traduisez pas le texte des transactions de document effectuées avec `Document.openTransaction()`

### Dans InitGui.py 

-   Ajoutez la ligne suivante, près du haut du fichier :


```python
def QT_TRANSLATE_NOOP(scope, text):
    return text
```

-   Pour traduire les noms de menu :


```python
self.appendMenu(QT_TRANSLATE_NOOP("context", "My menu"), [list of commands, ...])
```

-   La macro `QT_TRANSLATE_NOOP` ne fait rien, mais marque les textes qui seront lus ultérieurement par l\'utilitaire `lupdate`. Comme il ne fait rien, nous ne l\'utilisons que dans des cas particuliers où FreeCAD s\'occupe de tout.
-   Ajoutez le chemin d\'accès à votre dossier `translations/` dans la fonction initialisée :


```python
FreeCADGui.addLanguagePath("/path/to/translations")
```

Le fichier `InitGui.py` n\'a pas d\'attribut **fichier**. Il est donc difficile de trouver l\'emplacement relatif du dossier de traductions. Un moyen facile de contourner ce problème consiste à importer un autre fichier à partir du même dossier, puis dans ce fichier, par 
```python
FreeCADGui.addLanguagePath(os.path.join(os.path.dirname(__file__), "translations"))
```

### À l\'intérieur de chaque classe de commande de FreeCAD 

-   Ajoutez la ligne suivante, près du haut du fichier : 
```python
    def QT_TRANSLATE_NOOP(context, text):
        return text
    
```
-   Traduisez les `'MenuText'` et `'Tooltip'` de la commande comme ceci :


```python
def GetResources(self):
    return {'Pixmap'  : "path/to/icon.svg"),
            'MenuText': QT_TRANSLATE_NOOP("CommandName", "My Command"),
            'ToolTip' : QT_TRANSLATE_NOOP("CommandName", "Describes what the command does"),
            'Accel'   : "Shift+A"
    }
```

Où `"CommandName"` est le nom de la commande, défini par 
```python
FreeCADGui.addCommand('CommandName',My_Command_Class())
```

## Rassemblez toutes les chaînes de votre module 

-   Vous aurez besoin des outils `lupdate`, `lconvert`, `lrelease` et `pylupdate` installés sur votre système. Dans les distribution Linux, ils viennent généralement avec des paquets nommés `pyside-tools` ou `pyside2-tools`. Sur certains systèmes `lupdate` est nommé `lupdate4` ou `lupdate5` ou `lupdate-qt4`. Même chose pour les autres outils. Vous pouvez généralement utiliser la version qt4 ou qt5 à votre choix.
-   Si vous avez des fichiers `.ui`, vous devez d'abord exécuter `lupdate` :


```python
lupdate *.ui -ts translations/uifiles.ts
```

Ceci est récursif et trouvera des fichiers `.ui` dans toute la structure de vos répertoires.

-   Si vous avez des fichiers `.py`, vous devez également exécuter `pylupdate` :


```python
pylupdate *.py -ts translations/pyfiles.ts
```

-   Si vous avez exécuté les deux opérations, vous devez maintenant unifier ces deux fichiers en un :


```python
lconvert -i translations/uifiles.ts translations/pyfiles.ts -o translations/MyModule.ts
```

-   Vérifiez le contenu des trois fichiers `.ts` pour vous assurer qu\'ils contiennent les chaînes, puis supprimez `pyfiles.ts` et `uifiles.ts`.
-   Vous pouvez tout faire dans un script bash comme ceci :


```python
#!/bin/sh
lupdate *.ui -ts translations/uifiles.ts
pylupdate *.py -ts translations/pyfiles.ts
lconvert -i translations/uifiles.ts translations/pyfiles.ts -o translations/MyModule.ts
rm translations/pyfiles.ts
rm translations/uifiles.ts
```

## Envoyer le fichier .ts à une plateforme de traduction 

Il est temps de faire traduire votre fichier `.ts`. Vous pouvez choisir de créer un compte sur une plateforme de traduction publique telle que [Crowdin](https://crowdin.com/) ou [Transifex](https://www.transifex.com/), ou vous pouvez bénéficier de notre [compte FreeCAD existant sur Crowdin](https://crowdin.com/project/freecad-addons), qui compte déjà de nombreux utilisateurs et qui a donc plus de chance de faire traduire votre fichier rapidement par des personnes connaissant FreeCAD.

Si vous souhaitez héberger votre fichier sur le compte FreeCAD Crowdin, contactez [Yorik](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68) sur le [forum FreeCAD](https://forum.freecadweb.org/).


**Note:**

certaines plates-formes comme Crowdin peuvent s\'intégrer à GitHub et effectuer automatiquement tout le processus à partir des points 2, 3 et 4. Pour cela, vous ne pouvez pas utiliser le compte FreeCAD Crowdin ; vous devrez configurer vôtre propre compte.

## Fusionner les traductions 

Une fois que votre fichier `.ts` a été traduit, même partiellement, vous pouvez télécharger les traductions à partir du site :

-   Vous téléchargerez généralement un fichier `.zip` contenant un `.ts` par langue
-   Placez tous les fichiers `.ts` traduits, ainsi que votre fichier `.ts` de base, dans le dossier `translations/`

## Compiler les traductions 

Maintenant, lancez le programme `lrelease` sur chaque fichier que vous avez. 
```python
lrelease "translations/Draft_de.ts"
lrelease "translations/Draft_fr.ts"
lrelease "translations/Draft_pt-BR.ts"
```

Vous pouvez automatiser le processus 
```python
for f in translations/*_*.ts
do
    lrelease "translations/$f"
done
```

Vous devriez trouver un fichier `.qm` pour chaque fichier `.ts` traduit. Les fichiers `.qm` sont ceux qui seront utilisés par Qt et FreeCAD au moment de l\'exécution.

C\'est tout ce dont vous avez besoin. Notez que certaines parties de votre atelier ne peuvent pas être traduites à la volée si vous décidez de changer de langue. Si tel est le cas, vous devrez redémarrer FreeCAD pour que la nouvelle langue prenne effet.

## Tester les traductions 

1.  Basculez FreeCAD dans une langue que vous avez traduite (ex. Allemand)
2.  Chargez la traduction dans FreeCAD, ex. `FreeCADGui.addTranslationPath("/path/to/the/folder/containing/qmfile")`
3.  Tester quelque chose, ex. `FreeCAD.Qt.translate("your context", "some string")`

Résultat : Cela devrait vous donner la traduction allemande. Si cela fonctionne bien, alors la configuration de base est correcte. Alors nous pouvons regarder autre chose. Par exemple, les noms des commandes devraient toujours utiliser un contexte spécial qui est le nom de la commande telle qu\'elle est enregistrée dans FreeCAD.

### Remarques importantes 

-   Assurez-vous que vous utilisez un \*contexte\* et une \*chaîne\* qui se trouvent réellement dans le fichier ts/qm bien sûr.

## Script pratique 

Yorik maintient un script pratique pour l\'atelier BIM, qui peut rassembler, charger et télécharger des fichiers ts. Vous pouvez simplement copier et adapter ce script à votre atelier :

<https://github.com/yorikvanhavre/BIM_Workbench/blob/master/utils/updateTranslations.py>

## Références importantes 

-   Pourquoi et comment traduire les fonctions `openCommand()` ([fil de discussion](https://forum.freecadweb.org/viewtopic.php?f=10&t=55869))

## Pages associées 

-   [Ateliers externes](External_workbenches/fr.md)
-   [Localisation](Localisation/fr.md)
-   Pour plus d\'informations faites vos demandes ici sur le forum [Translating external workbenches](https://forum.freecadweb.org/viewtopic.php?f=10&t=36413)


 

_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Translating an external workbench/fr
