 {{TOCright}}

Cette page est une prolongation de la page [Help:Editing](Help:Editing.md) et donne des directives communes pour la rédaction et la mise à jour de la documentation du wiki FreeCAD. Elle résume plusieurs discussions et séances de réflexion.

## Avant de commencer 

-   Cette documentation wiki est basée sur [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki), le même logiciel qui alimente [Wikipedia](https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal). Si vous avez contribué à Wikipédia, la modification des pages du wiki FreeCAD devrait être facile.
-   Contrairement à Wikipédia, le wiki FreeCAD est protégé en écriture pour éviter les spams. Vous devez demander un compte [sur le forum](http://forum.freecadweb.org/viewtopic.php?f=21&t=6830).
-   Si vous n\'avez jamais utilisé de logiciel wiki auparavant, veuillez lire [Help:Editing](Help:Editing.md) pour vous familiariser avec le balisage utilisé.
-   Pour une utilisation avancée du logiciel wiki, voir [MediaWiki Aide:Sommaire](https://www.mediawiki.org/wiki/Help:Contents). Toutes les fonctionnalités de MediaWiki ne sont pas disponibles dans ce wiki FreeCAD, mais beaucoup le sont.
-   Nous aimons garder la documentation facile à lire, évitez donc d\'utiliser des fonctionnalités complexes. Rester simple.
-   Utilisez un bac à sable (sandbox) pour tester votre code, par exemple, [FreeCADDocu:Sandbox](FreeCADDocu:Sandbox.md) ou une page particulière avec votre nom [Sandbox:Yourname](Sandbox:Yourname.md). Les pages Sandbox doivent être placées dans la catégorie Sandbox. Cela se fait en ajoutant [[Category:Sandbox]] au bas du code du wiki.
-   Veuillez prendre connaissance des traductions. Le wiki FreeCAD utilise la prise en charge de la traduction automatisée pour fournir des pages dans de nombreuses langues. Pour chaque page, plusieurs versions linguistiques peuvent exister. Sur de nombreuses pages, vous verrez des balises telles que <translate>...</translate> et de nombreuses balises simples telles que . Ces dernières sont créées par le système de traduction, vous ne devez jamais les créer manuellement. Elles lient les titres et les paragraphes à leurs versions traduites. Vous ne devriez pas les changer car cela détruirait ces liens. Il est cependant bien de déplacer des paragraphes ou de modifier le libellé tant que les balises restent avec eux. Si vous supprimez un titre ou un paragraphe, vous devez également supprimer la balise qui lui appartient. Veuillez noter que les modifications apportées aux en-têtes et aux paragraphes existants affectent les traductions actuelles. Vos changements devraient en valoir la peine. Ne vous inquiétez pas lors de l\'ajout de nouveau matériel car le système ajoutera automatiquement de nouvelles balises après vos modifications. Pour plus d\'informations, consultez [Localisation](Localisation/fr.md) et la page d\'origine [Aide:Extension:Translate/Exemple de traduction de page](https://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example/fr).

## Directives générales 

### Descriptions concises 

Lorsque vous décrivez FreeCAD, essayez d\'être concis et précis et évitez les répétitions. Décrivez ce que FreeCAD *fait*, et non ce que FreeCAD *ne fait pas*. Évitez également les expressions familières telles que \"un petit nombre\". Utilisez \"quelques\" lorsqu\'il s\'agit d\'un nombre indéterminé, ou précisez la quantité exacte.

Mauvaise description
:   [Atelier PartDesign](PartDesign_Workbench/fr.md) : l\'atelier PartDesign est un atelier de conception de pièces qui vise à fournir des outils pour la modélisation de pièces solides complexes.





Bonne description
:   [Atelier PartDesign](PartDesign_Workbench/fr.md) : vise à fournir des outils pour la modélisation de pièces solides complexes.

### Informations centralisées 

Évitez de dupliquer les mêmes informations à différents endroits. Insérez les informations dans une nouvelle page et créez un lien vers cette page à partir d\'autres pages qui nécessitent ces informations.

N\'utilisez pas la transclusion de pages ([Help:Editing\#Templates and transcluding pages](Help:Editing#Templates_and_transcluding_pages.md)) car cela rend le wiki difficile à traduire. Utilisez uniquement les modèles décrits ci-dessous dans [Modèles](#Mod.C3.A8les.md).

### Style

Il existe un modèle pour styliser les commandes de menu, comme **Fichier → Sauvegarder**, un autre modèle pour styliser les touches sur lesquelles appuyer, comme **Shift**, un autre modèle pour afficher une valeur booléenne `True` etc\... Cela permet à la documentation d\'avoir une apparence cohérente et de pouvoir être traduite sans trop d\'effort. Veuillez vous familiariser avec la section [Modèles](#Mod.C3.A8les.md) avant d\'écrire des pages d\'aide.

### Indicateurs temporaires 

Si vous travaillez sur une grande page, il est conseillé de marquer la page comme travail en cours ou comme inachevée. Cela garantit que les administrateurs du wiki ne marquent pas votre page comme prête pour la traduction pendant que vous la modifiez encore.

Pour signaler une page, ajoutez soit  ou {{UnfinishedDocu}} en première ligne. Avec {UnfinishedDocu}}, vous invitez les autres à se joindre à vous pour terminer la page, tandis que {{Page in progress} indique que vous ferez le travail vous-même et que les autres doivent vous laisser du temps.

Une fois le travail terminé, n\'oubliez pas de retirer les avertissements!

## Exemples

Pour vous familiariser rapidement avec la structure et le style du wiki FreeCAD, consultez la page du modèle : [Modèle GuiCommand](GuiCommand_model/fr.md).


<div class="mw-collapsible mw-collapsed toccolours">

## Structure


<div class="mw-collapsible-content">

Le [Documentation pour utilisateurs](User_hub/fr.md) fournit une [Table des matières](Online_Help_Toc/fr.md). Ceci est utilisé comme référence principale pour créer automatiquement l\'aide hors ligne que vous pouvez atteindre à partir de FreeCAD ainsi que la documentation PDF hors ligne.

Le [Template:Docnav](Template:Docnav.md) est utilisé pour lier séquentiellement des pages, en suivant la structure de la [Table des matières de l\'aide en ligne](Online_Help_Toc/fr.md). Voir [Modèles](#Mod.C3.A8les.md) pour une liste de tous les modèles.

### Noms de page 

Les noms de page doivent être courts et utiliser la casse des phrases: tous les mots sauf le premier et les noms propres doivent être en minuscules. Il s\'agit du [style utilisé par Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Capital_letters#Headings,_headers,_and_captions) pour leurs articles.

Nom de page incorrect:
:   Construction Of AeroCompany Airplanes





Bon nom de page:
:   Construction of AeroCompany airplanes

Les noms des pages d\'atelier de premier niveau doivent avoir le format suivant : XYZ Workbench, où XYZ est le nom de l\'atelier, par exemple [PartDesign Workbench](PartDesign_Workbench.md). Et les noms des pages décrivant les commandes (ou outils) appartenant à un atelier doivent avoir ce format : Commande XYZ, par exemple [PartDesign Pad](PartDesign_Pad.md). Notez que vous devez utiliser le nom de la commande tel qu\'il apparaît dans le code source.

Une ancienne convention consistait à utiliser la casse : chaque mot devait commencer par une majuscule, sauf s\'il s\'agissait d\'articles, de prépositions, de conjonctions ou d\'autres particules grammaticales (par exemple, \'de\', \'sur\', \'dans\', \'a\', \'an\', \'et\'). De nombreuses pages existantes utilisent ce style, mais il est déconseillé de l\'utiliser pour les nouvelles pages. Ce point a été discuté dans le fil de discussion du forum [(Liens en minuscules) Utiliser un titre en minuscules pour une page wiki](https://forum.freecadweb.org/viewtopic.php?p=266029#p266029).

### En-têtes 

Comme les noms de pages, les titres de paragraphes doivent être courts et utiliser la casse des phrases. Vous ne devez pas utiliser les titres H1 (= Heading =) dans votre balisage wiki puisque le titre de la page est automatiquement ajouté comme titre principal H1.

### Liens

Vous devez utiliser le nom du lien d\'origine pour les liens dans la mesure du possible. Cela clarifie la page référencée dans la documentation imprimée ou hors ligne. Veuillez éviter les mots non significatifs pour le lien.

Mauvais lien
:   Pour plus d\'informations sur le dessin d\'objets 2D, cliquez sur [ici](Draft_Workbench/fr.md).





Bon lien
:   Pour plus d\'informations sur le dessin d\'objets 2D, consultez l\'[Atelier Draft](Draft_Workbench/fr.md).

Le format préféré pour un lien est:

[name of page](Name_of_page.md)

Traduit en:

[nom de la page](Name_of_page/fr.md)

Notez que pour la partie avant le caractère |, le lien réel, la casse est pertinente. Si le nom de votre page est Nom_de_page, le lien échouera si vous tapez Nom_de_page (P majuscule). Avant le caractère |, tous les espaces doivent être remplacés par des tirets bas (_). Ceci a pour but d\'aider les traducteurs qui utilisent un logiciel de traduction. Sans les traits de soulignement, le lien serait traduit par le logiciel, ce qui n\'est pas souhaitable.

Pour créer un lien vers un certain paragraphe, ajoutez un signe # et ses intitulés au nom de la page. Exemple :

[WikiPages](WikiPages#Links.md)

Traduit en:

[WikiPages](WikiPages/fr#Liens.md)

Dans la même page, vous pouvez omettre le nom de la page. Exemple:

[Links](#Links.md)

Pour créer un lien vers le haut de la page, vous pouvez utiliser:

</translate>{{Top}}<translate>

Ce modèle doit automatiquement afficher le texte correct en fonction de la langue de la page. Un lien vers le haut de la page est particulièrement utile pour les pages longues, car il permet à l\'utilisateur de revenir rapidement à la table des matières. Vous pouvez le placer à la fin de chaque paragraphe. Assurez-vous qu\'il y a une ligne vide avant et après le modèle.

Lien image
:   <img alt="Texte facultatif qui s\'affiche lorsque vous survolez l\'image\|link=Draft\_Wire" src=images/Draft_Wire.svg  style="width:24px;">.

Pour utiliser une image comme lien :

![](images/)

Lien image + lien texte
:   <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Polyligne](Draft_Wire/fr.md)

Si vous ne tenez pas compte du texte facultatif, le lien lui-même s\'affichera au survol de l\'image, ce qui est préférable et vous devez également ajouter un lien texte après le lien image :

![](images/)_[Draft_Polyligne](Draft_Wire/fr.md)

### Les pages atelier 

Une page d\'atelier de haut niveau devrait commencer par :

-   Une description de l\'utilisation de l\'atelier.
-   Une image pour illustrer la description.

Voir [Capture d\'écran](#Capture_d.27.C3.A9cran.md) pour les conventions sur l\'inclusion d\'images.

### Pages de commande 

Les pages de commandes décrivant les outils de l\'atelier ne doivent pas être trop longues, elles doivent seulement expliquer ce qu\'une commande peut faire et ce qu\'elle ne peut pas faire, et comment l\'utiliser. Les images et les exemples doivent être réduits au minimum. Les tutoriels peuvent développer la manière d\'utiliser l\'outil et fournir des détails étape par étape.

Veuillez vous référer à la page [Modèle GuiCommand](GuiCommand_model/fr.md) pour plus de détails

### Tutoriels

Un tutoriel bien rédigé doit permettre d\'apprendre comment obtenir rapidement certains résultats pratiques. Il ne doit pas être trop long, mais doit inclure suffisamment d\'instructions étape par étape et d\'images pour guider l\'utilisateur. Au fur et à mesure de l\'évolution de FreeCAD, les tutoriels peuvent devenir obsolètes, il est donc important de mentionner la version de FreeCAD utilisée dans, ou requise pour, un tutoriel.

Pour des exemples, consultez la page [Tutoriels](Tutorials/fr.md).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Modèles


<div class="mw-collapsible-content">

Le style des pages du wiki FreeCAD est réalisé grâce à l\'utilisation de modèles ([Help:Editing\#Templates\_and\_transcluding\_pages](Help:Editing#Templates_and_transcluding_pages.md)). Ils garantissent une apparence standardisée pour toutes les pages et permettent également de modifier le style du wiki. Vous pouvez voir la liste complète des modèles définis en accédant à [Special:PrefixIndex/Template:](Special:PrefixIndex/Template:.md). Mais veuillez n\'utiliser que les modèles figurant dans les tableaux ci-dessous. Vous ne devez utiliser directement les balises HTML que dans des cas très particuliers.

Cliquez sur le lien du modèle pour voir les instructions d\'utilisation d\'un modèle et voir son implémentation. Les modèles sont une fonctionnalité puissante du logiciel MediaWiki. Vous devez être un utilisateur expérimenté de wiki si vous souhaitez proposer des ajouts et des modifications aux modèles existants. S\'ils ne sont pas correctement mis en œuvre, les modèles rendent difficile la traduction des pages dans d\'autres langues. Leur utilisation doit donc être limitée au formatage du texte et la transclusion des pages doit être évitée. Voir [MediaWiki Help:Templates](https://www.mediawiki.org/wiki/Help:Templates) pour en savoir plus.

### Modèles simples 

#### Modèles de style simples 

+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Modèle                                                                                                        | Apparence                              | Description                                                                                                                                                                                                                                                                                                                 |
+===============================================================================================================+========================================+=============================================================================================================================================================================================================================================================================================================================+
| [Top](Template:Top.md)                                                                                |                         | Utilisez-le pour ajouter un lien en haut de la page.                                                                                                                                                                                                                                                                        |
|                                                                                                               | {{Top}}                                |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Emphasis](Template:Emphasis.md)                                                                      |                         | Utilisez-le pour mettre en valeur un élément de texte.                                                                                                                                                                                                                                                                      |
|                                                                                                               | **emphasis**                  |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [KEY](Template:KEY.md)                                                                                |                         | Utilisez-le pour indiquer une touche du clavier qui doit être enfoncée.                                                                                                                                                                                                                                                     |
|                                                                                                               | **Alt**                            |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ASCII](Template:ASCII.md)                                                                            |                         | Utilisez-le pour indiquer une touche ascii dans une image (.svg) qui doit être utilisée. Vous devez donner le caractère souhaité ou le numéro du code ascii du caractère.                                                                                                                                                   |
|                                                                                                               | {{ASCII|A}}                            |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Button](Template:Button.md)                                                                          |                         | Utilisez-le pour indiquer un bouton de l\'interface utilisateur graphique sur lequel il faut appuyer.                                                                                                                                                                                                                       |
|                                                                                                               | **Cancel**                      |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [RadioButton](Template:RadioButton.md)                                                                |                         | Utilisez-le pour indiquer un bouton radio dans l\'interface utilisateur graphique qui doit être {{RadioButton|TRUE|Selected}} ou {{RadioButton|FALSE|Not}}.                                                                                                                                     |
|                                                                                                               | {{RadioButton|Option}}                 |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [CheckBox](Template:CheckBox.md)                                                                      |                         | Utilisez-le pour indiquer une case à cocher dans l\'interface utilisateur graphique qui doit être {{CheckBox|TRUE|Checked}} ou {{CheckBox|FALSE|Not}}.                                                                                                                                          |
|                                                                                                               | {{CheckBox|Option}}                    |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [SpinBox](Template:SpinBox.md)                                                                        |                         | Utilisez-le pour indiquer une spinbox dans l\'interface utilisateur graphique qui doit être modifiée.                                                                                                                                                                                                                       |
|                                                                                                               | {{SpinBox|1.50}}                       |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ComboBox](Template:ComboBox.md)                                                                      |                         | Utilisez-le pour indiquer une combobox dans l\'interface utilisateur graphique qui doit être modifiée.                                                                                                                                                                                                                      |
|                                                                                                               | {{ComboBox|Menu 1}}                    |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [FALSE](Template:FALSE.md), [false](Template:false.md)                                        |                         | Utilisez-le pour indiquer une valeur booléenne fausse, par exemple, en tant que propriété dans l\'[Éditeur de propriétés](Property_editor/fr.md). Il s\'agit d\'un raccourci. Comme il s\'agit d\'une valeur, préférez Template [Value](Template:Value.md) {{Value|false}}                    |
|                                                                                                               | `False`                              |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               | , {{false}}              |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [TRUE](Template:TRUE.md), [true](Template:true.md)                                            |                         | Utilisez-le pour indiquer une valeur booléenne vraie, par exemple, en tant que propriété dans l\'[Éditeur de propriétés](Property_editor/fr.md). Il s\'agit d\'un raccourci. Comme il s\'agit d\'une valeur, préférez Template [Value](Template:Value.md) {{Value|true}}                      |
|                                                                                                               | `True`                               |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               | , {{true}}               |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [MenuCommand](Template:MenuCommand.md)                                                                |                         | Utilisez-le pour indiquer l\'emplacement d\'une commande dans un menu particulier.                                                                                                                                                                                                                                          |
|                                                                                                               | **File → Save**            |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [FileName](Template:FileName.md)                                                                      |                         | Utilisez-le pour indiquer le nom d\'un fichier ou d\'un répertoire.                                                                                                                                                                                                                                                         |
|                                                                                                               | {{FileName|File name}}                 |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [SystemInput](Template:SystemInput.md)                                                                |                         | Utilisez-le pour indiquer le texte d\'entrée tapé par l\'utilisateur.                                                                                                                                                                                                                                                       |
|                                                                                                               | {{SystemInput|Type this text}}         |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [SystemOutput](Template:SystemOutput.md)                                                              |                         | Utilisez-le pour indiquer la sortie de texte du système.                                                                                                                                                                                                                                                                    |
|                                                                                                               | {{SystemOutput|Output text}}           |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Incode](Template:Incode.md)                                                                          |                         | Utilisez-le pour inclure du code source en ligne avec une police monospace. Il doit tenir sur une seule ligne.                                                                                                                                                                                                              |
|                                                                                                               | `import FreeCAD`              |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [PropertyView](Template:PropertyView.md)                                                              |                         | Utilisez-le pour indiquer une propriété de vue dans l\'[Éditeur de propriétés](Property_editor/fr.md). Des exemples de propriétés de vue incluent {{emphasis|Line Color}}, {{emphasis|Line Width}}, {{emphasis|Point Color}}, {{emphasis|Point Size}}, etc. |
|                                                                                                               | **Color**                 |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [PropertyData](Template:PropertyData.md)                                                              |                         | Utilisez-le pour indiquer une propriété Data dans l\'[Éditeur de propriétés](Property_editor/fr.md). Les propriétés de données sont différentes selon les types d\'objets.                                                                                                                                          |
|                                                                                                               | **Position**              |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Properties Title](Template:Properties_Title.md) / [TitleProperty](Template:TitleProperty.md) |                         | Utilisez-le pour indiquer le titre d\'un groupe de propriétés dans l\'[Éditeur de propriétés](Property_editor/fr.md). Le titre ne sera pas inclus dans la table des matières automatique.                                                                                                                           |
|                                                                                                               | {{Properties_Title|Base}}              |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Obsolete](Template:Obsolete.md)                                                                      |                         | Utilisez-le pour indiquer qu\'une fonctionnalité est devenue obsolète dans la version de FreeCAD spécifiée.                                                                                                                                                                                                                 |
|                                                                                                               | {{Obsolete|0.19}}                      |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Version](Template:Version.md)                                                                        |                         | Utilisez-le pour indiquer qu\'une fonctionnalité a été introduite dans la version de FreeCAD spécifiée.                                                                                                                                                                                                                     |
|                                                                                                               | <small>(v0.18)</small>                        |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [VersionMinus](Template:VersionMinus.md)                                                              |                         | Utilisez-le pour indiquer qu\'une fonctionnalité est disponible dans la version de FreeCAD spécifiée et les versions antérieures.                                                                                                                                                                                           |
|                                                                                                               | {{VersionMinus|0.16}}                  |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [VersionPlus](Template:VersionPlus.md)                                                                |                         | Utilisez-le pour indiquer qu\'une fonctionnalité est disponible dans la version de FreeCAD spécifiée et les versions ultérieures.                                                                                                                                                                                           |
|                                                                                                               | <small>(v0.17)</small>                    |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ColoredText](Template:ColoredText.md)                                                                |                         | Utilisez ce modèle pour colorer l\'arrière-plan, le texte, ou l\'arrière-plan et le texte. ([ColoredText](Template:ColoredText.md) page pour plus d\'exemples)                                                                                                                                                      |
|                                                                                                               | {{ColoredText|Colored Text}}           |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ColoredParagraph](Template:ColoredParagraph.md)                                                      |                         | Utilisez ce modèle pour colorer le fond, le texte, ou le fond et le texte d\'un paragraphe entier. La page [ColoredParagraph](Template:ColoredParagraph.md) pour plus d\'exemples)                                                                                                                                  |
|                                                                                                               | {{ColoredParagraph|Colored Paragraph}} |                                                                                                                                                                                                                                                                                                                             |
|                                                                                                               |                                     |                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Modèles complexes 

Ces modèles requièrent davantage de paramètres d\'entrée ou produisent un bloc de texte d\'un format particulier.

+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Modèle                                                                                           | Apparence                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                   |
+==================================================================================================+==============================================================================================================================+===============================================================================================================================================================================================================================================================================================================================================+
| [Prettytable](Template:Prettytable.md)                                                   | Ce tableau                                                                                                                   | Utilisez-le pour formater des tableaux comme celui-ci. Des propriétés de tableaux supplémentaires peuvent être ajoutées.                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Caption](Template:Caption.md)                                                           |                                                                                                                    | Utilisez-le pour ajouter une explication sous une image. Elle peut être alignée à gauche ou au centre.                                                                                                                                                                                                                                        |
|                                                                                                  | <div style="width:400px;">                                                                                                   |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                               |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  | *Une légende pour une image*                                                                                       |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                    |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  | </div>                                                                                                                       |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  | .                                                                                                                            |                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Clear](Template:Clear.md)                                                               |                                                                                                                              | Utilisez-le pour effacer des colonnes. Suivez la définition du modèle pour une explication détaillée. Il est souvent utilisé pour empêcher le texte de déborder à côté d\'images sans rapport.                                                                                                                                                |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Code](Template:Code.md)                                                                 |                                                                                                               | Utilisez-le pour inclure des exemples de code multi-lignes avec une police monospace. Le langage par défaut est Python, mais d\'autres langages peuvent être spécifiés.                                                                                                                                                                       |
|                                                                                                  | 
```pythonimport FreeCAD```                                                                                                 |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           | Le code [Python](Python/fr.md) doit adhérer aux recommandations générales établies par [PEP8: Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/). En particulier, les parenthèses doivent immédiatement suivre le nom de la fonction et un espace doit suivre une virgule. Cela rend le code plus lisible.       |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Fake heading](Template:Fake_heading.md)                                                 |                                                                                                               | Utilisez-le pour créer un titre qui ne sera pas automatiquement inclus dans la table des matières.                                                                                                                                                                                                                                            |
|                                                                                                  | {{Fake heading|Heading|2}}                                                                                                   |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [GuiCommand](Template:GuiCommand.md)                                                     | See [GuiCommand model](GuiCommand_model.md)                                                                          | UUtilisez-le pour créer une boîte contenant des informations utiles pour documenter les commandes de l\'atelier (outils).                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [TutorialInfo](Template:TutorialInfo.md)                                                 | Voir par exemple [Tutoriel de modélisation de base](Basic_modeling_tutorial/fr.md).                                  | Utilisez-le pour créer une boîte contenant des informations utiles pour documenter les [tutoriels](Tutorials/fr.md).                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Macro](Template:Macro.md)                                                               | Voir par exemple [Macro FlattenWire](Macro_FlattenWire/fr.md).                                                       | Utilisez-le pour créer une boîte contenant des informations utiles pour documenter les [macros](Macros/fr.md).                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Docnav](Template:Docnav.md)                                                             |                                                                                                               | Utilisez-le pour créer une barre avec les mots \"suivant\", \"précédent\" et \"index\" et les liens appropriés, ce qui est utile pour placer les pages dans un ordre particulier.                                                                                                                                                             |
|                                                                                                  |                                                                                 |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [VeryImportantMessage](Template:VeryImportantMessage.md)                                 |                                                                                                               | Utilisez-le pour créer une boîte en surbrillance contenant un message très important. Utilisez-le avec parcimonie, uniquement pour indiquer des problèmes majeurs dans la fonctionnalité du logiciel, l\'abandon d\'outils, etc.                                                                                                              |
|                                                                                                  | {{VeryImportantMessage|Important Message}}                                                                                   |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Page in progress](Template:Page_in_progress.md)                                         |                                                                                                               | Utilisez cette option pour les pages qui sont toujours en cours ou qui sont en train d\'être retravaillées. N\'oubliez pas de le supprimer lorsque la page est prête.                                                                                                                                                                         |
|                                                                                                  | {{Page in progress|Page in progress}}                                                                                        |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [UnfinishedDocu](Template:UnfinishedDocu.md)                                             |                                                                                                               | Utilisez-le pour créer une boîte en surbrillance indiquant une page de documentation inachevée.                                                                                                                                                                                                                                               |
|                                                                                                  | {{UnfinishedDocu}}                                                                                                           |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Softredirect](Template:Softredirect.md)                                                 |                                                                                                                              | Utilisez-la à la place de la redirection normale, lorsque vous redirigez vers une page spéciale (comme Media: ou Category:), auquel cas la redirection normale est désactivée.                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Quote](Template:Quote.md)                                                               |                                                                                                               | Utilisez-le pour créer un encadré de texte avec une citation et une référence littérale.                                                                                                                                                                                                                                                      |
|                                                                                                  | {{Quote|text=Cry "Havoc" and let slip the dogs of war.|sign=William Shakespeare|source=''Julius Caesar'', act III, scene I}} |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                  |                                                                                                                           |                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Userdocnavi](Template:Userdocnavi.md), [Powerdocnavi](Template:Powerdocnavi.md) |                                                                                                                              | Utilisez-les pour créer des boîtes de navigation pour la documentation utilisateur, la documentation pour les utilisateurs expérimentés et la documentation pour les développeurs. Cela permet de passer rapidement d\'une section à l\'autre de la documentation. Ils placent également la page correspondante dans la catégorie appropriée. |
+--------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Illustrations


<div class="mw-collapsible-content">

Les images et les captures d\'écran sont nécessaires pour produire une documentation complète de FreeCAD. Elles sont particulièrement utiles pour illustrer les exemples et les tutoriels. Les images doivent être affichées dans leur taille originale, afin de présenter suffisamment de détails et d\'être lisibles si elles contiennent du texte. Les images [Bitmap](Bitmap/fr.md) ne doivent pas être redimensionnées.

Évitez les images animées (GIF) dans les pages d\'aide générales. Les animations et les vidéos doivent être réservées aux tutoriels qui ne sont pas destinés à être utilisés comme documentation PDF hors ligne.

Les images peuvent être téléchargées via la page [Téléverser un fichier](Special:Upload.md).

### Nom

Donnez des noms significatifs à vos images. Si vous avez une image qui présente les caractéristiques d\'une commande particulière, vous devez utiliser le nom de cette commande avec `_exemple` à la fin. Par exemple, pour la commande [Draft Offset](Draft_Offset.md), l\'image doit s\'appeler `Draft_Offset_exemple.jpg`.

### Capture d\'écran 

Les tailles recommandées pour les captures d\'écran sont :

-   Native 400x200 (ou width=400 et height\<=200), pour les pages [Modèle GuiCommand](GuiCommand_model/fr.md), pour permettre à l\'image de tenir dans la partie gauche de la page, et pour les autres captures d\'écran standard.
-   Native 600x400 (ou width=600 et height\<=400), pour les pages [Modèle GuiCommand](GuiCommand_model/fr.md), lorsque vous avez vraiment besoin d\'une image plus grande, tout en permettant à l\'image de tenir dans la partie gauche de la page, et pour d\'autres instantanés standard.
-   Native 1024x768 (ou largeur=1024 et hauteur\<=768), uniquement pour les images en plein écran.
-   Des tailles plus petites sont possibles pour l\'affichage des détails.
-   Évitez les images de plus grande résolution, car elles ne seront pas très portables sur d\'autres types d\'écrans ou sur la documentation PDF imprimée.

Vous ne devriez pas dépendre d\'une configuration personnalisée de votre bureau ou de votre système d\'exploitation lorsque vous créez des captures d\'écran et vous devriez utiliser les défauts visuels de l\'interface FreeCAD chaque fois que possible.

Pour créer une capture d\'écran, vous pouvez utiliser les options fournies par votre système d\'exploitation, ou l\'une de ces macros : <img alt="" src=images/Snip.png  style="width:24px;"> [Macro Snip](Macro_Snip/fr.md) et <img alt="" src=images/Macro_Screen_Wiki.png  style="width:24px;"> [Macro Screen Wiki](Macro_Screen_Wiki/fr.md).

### Texte

Pour faciliter la traduction de la documentation, essayez d\'éviter les captures d\'écran contenant du texte. Si vous ne pouvez pas l\'éviter, envisagez de prendre des captures d\'écran distinctes de l\'interface et de la [Vue 3D](3D_view/fr.md). L\'image de la vue 3D peut être réutilisée dans chaque traduction, tandis qu\'un traducteur peut prendre une capture d\'écran de l\'interface localisée si nécessaire.

### Icônes et illustrations 

Référez-vous à la page [Graphisme](Artwork/fr.md) pour toutes les illustrations et icônes qui ont été créées pour FreeCAD, et qui peuvent également être utilisées dans les pages de documentation. Si vous souhaitez contribuer aux icônes, veuillez lire les [Recommandations pour la charte graphique](Artwork_Guidelines/fr.md).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

## Traductions


<div class="mw-collapsible-content">

D\'avis général, la page de référence dans le wiki est la page anglaise, qui doit être créée en premier. Si vous souhaitez modifier ou ajouter du contenu à une page, vous devez d\'abord le faire sur la page en anglais et une fois la mise à jour terminée, portez la modification sur la page traduite.

Le wiki FreeCAD prend en charge une extension de traduction qui permet de gérer plus facilement les traductions entre les pages; pour plus de détails, voir [Localisation Traduire le wiki](Localisation/fr#Traduire_le_wiki_FreeCAD.md).

D\'autres ressources utiles sont :

-   [Liste des codes ISO 639-1](https://fr.wikipedia.org/wiki/Liste_des_codes_ISO_639-1) pour identifier le code à deux lettres d\'une langue particulière vers laquelle vous souhaitez traduire.
-   [Google Translate](http://translate.google.com/) pour obtenir de l\'aide sur les traductions.
-   [Deepl translator](https://www.deepl.com/translator) pour obtenir de l\'aide sur les traductions.

## Quelques conseils pour les traducteurs 

### Traduire le GuiCommand 

    {{GuiCommand
    |Name=FEM EquationFluxsolver
    |MenuLocation=Solve → Equation fluxsolver
    |Workbenches=[FEM](Fem_Workbench.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM tutorial](FEM_tutorial.md)
    }}

Traduit en:

    {{GuiCommand/fr
    |Name=FEM EquationFluxsolver
    |Name/fr=FEM EquationFluxsolver
    |MenuLocation=Solveur → Equation fluxsolver
    |Workbenches=[Atelier FEM](Fem_Workbench/fr.md)
    |Shortcut=**F** **S**
    |Version=0.17
    |SeeAlso=[FEM tutoriel](FEM_tutorial/fr.md)
    }}

### Traduire les navi 

    {{FEM_Tools_navi}}

Traduit en:

    {{FEM_Tools_navi/fr}}

### Traduire les liens 

    [Part Module](Part_Module.md)

Traduit en:

    [Atelier Pièces](Part_Module/fr.md)

### Traduire les Docnav 

    

Traduit en:

    

Exemple avec des icônes :

    

Traduit en:

    


</div>


</div>

## Créer, renommer et supprimer des pages 

### Créer des pages 

Avant de créer une nouvelle page, vous devez d\'abord vérifier si une page similaire existe déjà. Si c\'est le cas, il est généralement préférable d\'éditer cette page existante. En cas de doute, veuillez d\'abord ouvrir un sujet sur le forum [Wiki](https://forum.freecadweb.org/viewforum.php?f=21).

Pour créer une nouvelle page, effectuez l\'une des opérations suivantes :

-   Visitez l\'URL avec le nom de page souhaité, par exemple : https://wiki.freecadweb.org/My_new_page et cliquez sur \'créer cette page\'.
-   Faites une recherche wiki sur le nom de la page et cliquez sur le texte rouge dans \'Créer la page \"Ma nouvelle page\" sur ce wiki!\'.

### Renommer les pages 

FreeCAD étant un projet en développement permanent, il est parfois nécessaire de réviser le contenu du wiki. Si les noms des commandes sont modifiés dans le code source, les pages wiki qui les documentent doivent également être renommées. Cette opération ne peut être effectuée que par les administrateurs du wiki. Pour les informer, ouvrez un sujet dans le forum [Wiki](https://forum.freecadweb.org/viewforum.php?f=21) et indiquez l\'opération de renommage nécessaire dans ce formulaire :

    old name         new name
    Old_page_name_1  New_page_name_1
    Old_page_name_2  New_page_name_2
    ...

### Supprimer les fichiers et les pages 

Si vous devez supprimer un fichier, allez sur sa page (https://www.freecadweb.org/wiki/File:***.***) et modifiez-la. Peu importe que la page soit vide ou non, ajoutez ceci comme premier élément : {{Delete}} et directement en dessous, décrivez pourquoi la page doit être supprimée. En outre, ouvrez un sujet dans le forum [Wiki](https://forum.freecadweb.org/viewforum.php?f=21).

Pour les pages, la procédure est la même.

## Discussion

Le [sous-forum Wiki](http://forum.freecadweb.org/viewforum.php?f=21) du [forum FreeCAD](https://forum.freecadweb.org) offre un espace dédié pour discuter des sujets relatifs au wiki, de l\'apparence du wiki et de tout autre sujet lié au wiki. Posez-y vos questions et faites-y des suggestions.

## Terminologie - Règles de dénomination 

### En anglais 

Voir [Glossaire](Glossary/fr.md).

### Autres langues 

-   [Italiano](Italian_Translation.md)
-   [Français](French_Translation.md)
-   [Deutsch](German_Translation.md)

[Category:Documentation{{\#translation:}}](Category:Documentation.md) [Category:Wiki{{\#translation:}}](Category:Wiki.md) [Category:Wiki Documentation{{\#translation:}}](Category:Wiki_Documentation.md) [Category:Administration{{\#translation:}}](Category:Administration.md)
