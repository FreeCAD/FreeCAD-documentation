# Translating an external workbench/fr
Dans les notes suivantes, `"context"` doit être le nom de votre addon ou de votre atelier, par exemple, `"MySuperAddon"` ou `"DraftPlus"`, ou autre. Les majuscules ont leur importance ici : `"Context"` n\'est pas la même chose que `"context"` par exemple. Le contexte fait en sorte que toutes les traductions de votre code seront rassemblées sous le même nom, pour être plus facilement identifiées par les traducteurs. En d\'autres termes, ils sauront exactement à quel addon ou atelier appartient une chaîne de caractères particulière.

**Remarque** : Voici un script tout-en-un qui automatise la procédure complète mentionnée ci-dessous (il est tout de même conseillé de lire la procédure pour savoir ce que le script doit faire) : <https://github.com/yorikvanhavre/BIM_Workbench/blob/master/utils/updateTranslations.py>.

## Préparer les sources 

### Généralités

-   Ajouter un dossier `translations/`. Vous pouvez le nommer autrement, mais ce sera plus facile car c\'est la même chose dans FreeCAD. Dans ce dossier, vous placerez les fichiers `.ts` (les fichiers de traduction \"source\") et les fichiers `.qm` (fichiers de traduction compilés).
-   Seul le texte affiché pour l\'utilisateur dans l\'interface de FreeCAD doit être traduit. Le texte affiché uniquement dans la console Python ne doit pas être traduit.
-   Le texte qui s\'imprime dans la `FreeCAD.Console` est affiché dans la \"vue rapport\" et doit donc être traduit. La \"vue rapport\" est différente depuis la console Python.

### Dans chaque fichier Python .py 

-   Dans chaque fichier où vous devez traduire du texte, vous devez définir une fonction `translate()`. Vous pouvez utiliser le nom entièrement qualifié de Qt, mais c\'est un peu plus propre d\'utiliser :

:   
    
```python
    import FreeCAD
    translate = FreeCAD.Qt.translate
    
```
    

-   Tout le texte qui doit être traduit doit être traité par la fonction `translate()` :

:   
    
```python
    print("My text")
    
```
    





:   devient :





:   
    
```python
    print(translate("context", "My text"))
    
```
    





:   Sachez que `translate()` n\'est pas seulement une fonction normale : elle sert également de \"balise\" (tag) pour l\'utilitaire de traitement de texte `lupdate`, et doit donc être nommée exactement \"translate\". Le programme `lupdate` est un simple processeur de texte, il n\'exécute pas votre code. Vous devez passer des chaînes de caractères directement à la fonction `translate()` : vous ne pouvez pas passer de variables, de constantes, etc. Par exemple :





:   
    
```python
    # This works:
    FreeCAD.Console.PrintMessage(translate("context", "My text") + "\n")

    # This does not, lupdate only sees the word "a_variable", and doesn't know what that is:
    a_variable = "My text"
    FreeCAD.Console.PrintMessage(translate("context", a_variable ) + "\n")

    # But this works -- a_variable will contain the translated string:
    a_variable = translate("context", "My text")
    FreeCAD.Console.PrintMessage(a_variable  + "\n")
    
```
    





:   Ceci peut être utilisé partout : dans `print()`, dans `FreeCAD.Console.PrintMessage()`, dans les dialogues Qt, etc. Les fonctions `FreeCAD.Console` n\'ajoutent pas automatiquement le caractère de nouvelle ligne (`\n`), qui doit donc être ajouté à la fin si vous le souhaitez. Ce caractère n\'a pas besoin d\'être traduit non plus, il peut donc se trouver en dehors de la fonction de traduction :





:   
    
```python
    FreeCAD.Console.PrintMessage(translate("context", "My text") + "\n")
    
```
    

-   Si vous utilisez des fichiers `.ui` réalisés avec QtDesigner, vous n\'avez rien à faire de spécial avec eux.
-   Lorsque vous créez de nouveaux objets, ne traduisez pas le \"Name\" de l\'objet. Traduisez plutôt le \"Label\" de l\'objet. La différence est qu\'un \"Nom\" est unique ; il reste le même pendant toute la durée de vie de l\'objet ; en revanche, une \"Étiquette\" peut être modifiée par l\'utilisateur comme il le souhaite.
-   Lorsque vous créez des propriétés pour vos objets, ne traduisez pas le nom de la propriété. Mais placez la description dans `QT_TRANSLATE_NOOP` :

:   
    
```python
    obj.addProperty("App::PropertyBool", "MyProperty", "PropertyGroup", QT_TRANSLATE_NOOP("App::Property", "This is what My Property does"))
    
```
    





:   N\'utilisez pas votre propre `"context"` dans ce cas précis. Gardez `"App::Property"`.

-   Ne traduisez pas le texte des opérations sur les documents effectuées à l\'aide de la fonction `Document.openTransaction()`.

### Dans InitGui.py 

-   Ajouter la ligne suivante en haut du fichier :

:   
    
```python
    def QT_TRANSLATE_NOOP(context, text):
        return text
    
```
    





:   La macro `QT_TRANSLATE_NOOP` ne fait rien, mais elle marque les textes qui seront repris plus tard par l\'utilitaire `lupdate`. Nous ne l\'utilisons que dans des cas particuliers où FreeCAD s\'occupe lui-même de tout.

-   Pour traduire les noms des menus et des barres d\'outils, utilisez le mot `"Workbench"` comme contexte :

:   
    
```python
    self.appendMenu(QT_TRANSLATE_NOOP("Workbench", "My menu"), [list of commands, ...])
    self.appendToolbar(QT_TRANSLATE_NOOP("Workbench", "My toolbar"), [list of commands, ...])
    
```
    

-   Ajoutez le chemin vers votre dossier `translations/` dans la fonction Initialized :

:   
    
```python
    FreeCADGui.addLanguagePath("/path/to/translations")
    
```
    





:   Le fichier `InitGui.py` n\'a pas d\'attribut **file**, il n\'est donc pas facile de trouver l\'emplacement relatif du dossier des traductions. Une façon simple de contourner ce problème est de faire en sorte qu\'il importe un autre fichier du même dossier, et de faire dans ce fichier :





:   
    
```python
    FreeCADGui.addLanguagePath(os.path.join(os.path.dirname(__file__), "translations"))
    
```
    

### À l\'intérieur de chaque classe de commande de FreeCAD 

-   Ajouter la ligne suivante en haut du fichier :

:   
    
```python
    def QT_TRANSLATE_NOOP(context, text):
        return text
    
```
    

-   Traduisez les `'MenuText'` et `'Tooltip'` de la commande comme ceci :

:   
    
```python
    def GetResources(self):
        return {'Pixmap'  : "path/to/icon.svg"),
                'MenuText': QT_TRANSLATE_NOOP("CommandName", "My Command"),
                'ToolTip' : QT_TRANSLATE_NOOP("CommandName", "Describes what the command does"),
                'Accel'   : "Shift+A"
        }
    
```
    





:   où `"CommandName"` est le nom de la commande, défini par :





:   
    
```python
    FreeCADGui.addCommand('CommandName', My_Command_Class())
    
```
    

## Rassemblez toutes les chaînes de votre module 

-   Vous aurez besoin des outils `lupdate`, `lconvert`, `lrelease` et `pylupdate` installés sur votre système. Dans les distributions Linux, ils sont généralement fournis dans des paquets nommés `pyside-tools` ou `pyside2-tools`. Sur certains systèmes, `lupdate` est nommé `lupdate4` ou `lupdate5` ou `lupdate-qt4` ou similaire. Idem pour les autres outils. Vous pouvez utiliser la version Qt4 ou Qt5 à votre choix.
-   Si vous avez des fichiers `.ui`, vous devez d\'abord exécuter `lupdate` :

:   
    
```python
    lupdate *.ui -ts translations/uifiles.ts
    
```
    





:   Cette méthode est récursive et trouvera les fichiers `.ui` dans toute la structure de votre répertoire.

-   Si vous avez des fichiers `.py`, vous devez aussi exécuter `pylupdate` :

:   
    
```python
    pylupdate *.py -ts translations/pyfiles.ts
    
```
    

-   Si vous avez exécuté les deux opérations, vous devez maintenant unifier ces deux fichiers en un seul :

:   
    
```python
    lconvert -i translations/uifiles.ts translations/pyfiles.ts -o translations/MyModule.ts
    
```
    

-   Vérifiez le contenu des trois fichiers `.ts` pour vous assurer qu\'ils contiennent les chaînes de caractères, puis vous pouvez supprimer `pyfiles.ts` et `uifiles.ts`.
-   Vous pouvez faire tout cela dans un script bash comme celui-ci :

:   
    
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

certaines plates-formes comme Crowdin peuvent s\'intégrer à GitHub et effectuer automatiquement tout le processus à partir des points 2, 3 et 4. Pour cela, vous ne pouvez pas utiliser le compte FreeCAD Crowdin ; vous devrez créer votre propre compte.

## Fusionner les traductions 

Une fois que votre fichier `.ts` a été traduit, même partiellement, vous pouvez télécharger les traductions à partir du site :

-   Vous téléchargerez généralement un fichier `.zip` contenant un `.ts` par langue
-   Placez tous les fichiers `.ts` traduits, ainsi que votre fichier `.ts` de base, dans le dossier `translations/`

## Compiler les traductions 

Maintenant, lancez le programme `lrelease` sur chaque fichier que vous avez:


```python
lrelease "translations/Draft_de.ts"
lrelease "translations/Draft_fr.ts"
lrelease "translations/Draft_pt-BR.ts"
```

Vous pouvez automatiser le processus:


```python
for f in translations/*_*.ts
do
    lrelease "translations/$f"
done
```

Vous devriez trouver un fichier `.qm` pour chaque fichier `.ts` traduit. Les fichiers `.qm` sont ceux qui seront utilisés par Qt et FreeCAD au moment de l\'exécution.

C\'est tout ce dont vous avez besoin. Notez que certaines parties de votre atelier ne peuvent pas être traduites à la volée si vous décidez de changer de langue. Si tel est le cas, vous devrez redémarrer FreeCAD pour que la nouvelle langue prenne effet.

## Tester les traductions 

1.  Basculez FreeCAD vers une langue que vous avez traduite (par exemple l\'Allemand)
2.  Chargez la traduction dans FreeCAD, par exemple `FreeCADGui.addTranslationPath("/path/to/the/folder/containing/qmfile")`
3.  Tester quelque chose, par exemple `FreeCAD.Qt.translate("your context", "some string")`

Résultat : Cela devrait vous donner la traduction allemande. Si cela fonctionne bien, alors la configuration de base est correcte. Alors nous pouvons regarder autre chose. Par exemple, les noms des commandes devraient toujours utiliser un contexte spécial qui est le nom de la commande telle qu\'elle est enregistrée dans FreeCAD.

### Remarques importantes 

-   Assurez-vous que vous utilisez un \*contexte\* et une \*chaîne\* qui se trouvent réellement dans le fichier ts/qm bien sûr.

## Script pratique 

Yorik maintient un script pratique pour l\'atelier BIM, qui peut rassembler, charger et télécharger des fichiers ts. Vous pouvez simplement copier et adapter ce script à votre atelier :

<https://github.com/yorikvanhavre/BIM_Workbench/blob/master/utils/updateTranslations.py>

## Détails techniques et utilisation avancée 

Dans les exemples ci-dessus, deux fonctions distinctes sont utilisées : `translate()` et `QT_TRANSLATE_NOOP`. Vous pouvez également rencontrer `|tr()` et `QT_TR_NOOP`, qui fournissent automatiquement l\'argument \"context\" en fonction de l\'emplacement de l\'appel. Ces deux paires de fonctions sont fondamentalement différentes.


`translate()`

et `tr()` accomplissent deux tâches distinctes : au moment de l\'exécution, elles effectuent la traduction réelle de la chaîne qui leur est passée en chaîne traduite finale. Ceci est vrai qu\'on leur fournisse une chaîne littérale, une variable ou une constante : la recherche est dynamique et en temps réel pendant l\'exécution du code. Toutefois, elles fournissent une fonction supplémentaire hors temps d\'exécution : elles sont reconnues par l\'utilitaire `pylupdate`. Si (et seulement si) elles contiennent une chaîne de caractères littérale, cette chaîne est extraite par l\'utilitaire. SEULS les chaînes de caractères sont extraites par `pylupdate`. Si une variable est passée, elle est ignorée par l\'utilitaire `pylupdate`. Qt essaiera de fournir une traduction au moment de l\'exécution, mais cela ne fonctionnera que si un autre morceau de code a appelé une des fonctions de traduction avec la chaîne littérale qui doit être traduite, afin que `pylupdate` puisse l\'extraire. Notez que le code contenant la chaîne littérale ne doit jamais être exécuté, il doit simplement exister en tant que ligne de code dans un fichier quelque part : `pylupdate` n\'effectue aucune analyse ou exécution de code, il effectue simplement une recherche et une extraction de chaîne.

En revanche, `QT_TRANSLATE_NOOP` et `QT_TR_NOOP` ne font rien du tout à l\'exécution : ce sont des \"no-ops\" littérales et sont complètement ignorées par le code en cours d\'exécution. Leur seule utilité est de marquer une chaîne littérale pour qu\'elle soit extraite par `pylupdate` : il est inutile de placer une variable dans un appel à l\'une de ces fonctions, cela n\'aura aucun effet. Elles sont utilisées dans les cas où `translate()` ou `tr()` seront appelées avec une variable contenant le texte à traduire. Par exemple, tout code utilisé pour créer une commande ou une propriété utilisera une fonction de type NOOP autour du texte ou de l\'info-bulle du menu de la commande, ou de la docstring de la propriété : à l\'exécution, lorsque FreeCAD affiche ces éléments à l\'utilisateur, il appelle `translate()` : les chaînes littérales doivent avoir été extraites par `pylupdate` au moment de la création, par exemple :


```python
def GetResources(self):
    return {'Pixmap'  : "path/to/icon.svg",
            'MenuText': QT_TRANSLATE_NOOP("CommandName", "My Command"),
            'ToolTip' : QT_TRANSLATE_NOOP("CommandName", "Describes what the command does"),
            'Accel'   : "Shift+A"
    }
```

Dans cette utilisation, au moment de l\'exécution, le dictionnaire renvoyé par cette fonction est littéralement :


```python
{ 
    'Pixmap'  : "path/to/icon.svg",
    'MenuText': "My Command",
    'ToolTip' : "Describes what the command does",
    'Accel'   : "Shift+A"
}
```

Il n\'y a aucune référence à un quelconque type d\'information de traduction. Lorsque FreeCAD affiche réellement ces informations à l\'utilisateur, le pseudo-code est le suivant :


```python
for command in commands:
    resources = command.GetResources()
    menu_text = translate(resources['MenuText'])
```

Dans ce cas, `lupdate` ne peut pas extraire de chaîne de caractères de l\'appel à `translate()` car il fait référence à une variable. Ainsi, `lupdate` ignore cet appel, mais au moment de l\'exécution, Qt recherche la chaîne qui lui est passée. Tant que quelque part dans le code, il y a un appel à l\'une des fonctions de traduction avec une chaîne littérale correspondante (dans ce cas, dans la fonction `GetResources()`), cet appel de traduction réussira.

Pour vérifier que les chaînes de caractères attendues sont extraites, vous pouvez exécuter manuellement la commande `pylupdate` :


```python
pylupdate myfile.py -ts outfile.ts
```

Le fichier `outfile.ts` contiendra l\'ensemble des chaînes de caractères qui sont téléchargées vers CrowdIn pour être traduites.

## Références importantes 

-   Pourquoi et comment traduire les fonctions `openCommand()` ([fil de discussion](https://forum.freecadweb.org/viewtopic.php?f=10&t=55869))

## Pages en relation 

-   [Ateliers externes](External_workbenches/fr.md)
-   [Localisation](Localisation/fr.md)
-   Pour plus d\'informations faites vos demandes ici sur le forum : [Translating external workbenches](https://forum.freecadweb.org/viewtopic.php?f=10&t=36413).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Translating an external workbench/fr
