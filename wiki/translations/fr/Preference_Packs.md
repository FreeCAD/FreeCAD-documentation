# Preference Packs/fr
{{TOCright}}

## Introduction

Un **kit de préférences** est un ensemble de préférences de l\'utilisateur ({{Version/fr|0.20}}) qui peut être installée comme une extension et appliquée comme un seul ensemble. N\'importe quel paramètre de l\'utilisateur qui peut être défini dans le fichier user.cfg peut être inclus dans un kit de préférences. L\'application d\'un kit de préférences définit toutes les variables du fichier CFG fourni sans modifier aucun autre paramètre utilisateur. Par exemple, ces kitx peuvent être utilisés pour créer des \"Thèmes\" en regroupant une feuille de style personnalisée avec un ensemble de préférences utilisateur qui définit les différentes couleurs et styles d\'éléments dans FreeCAD qui ne sont pas contrôlés par la feuille de style.

## Interface des kits de préférences 

La plupart des interactions de l\'utilisateur avec les kits de préférences installés se font via l\'onglet **Général** de la section **Paramètres généraux** de l\'[Éditeur des préférences](Preferences_Editor/fr.md)

<img alt="" src=images/PreferencePacks_MainInterface.png  style="width:400px;">

## Appliquer un kit installé 

Pour appliquer un kit de préférences, cliquez sur le bouton **Appliquer** à côté de son nom dans l\'onglet *Général* de [Réglage des préférences](Preferences_Editor/fr.md). Le cœur d\'un kit de préférences est un ensemble de préférences de l\'utilisateur. Lors de l\'application d\'un kit, chacune de ces préférences est modifiée à la valeur définie dans le kit. A titre facultatif, l\'auteur du kit peut avoir inclus une macro pré- et/ou post-application qui peut également être exécutée. Comme les kits peuvent potentiellement apporter des modifications importantes (et éventuellement indésirables) à vos préférences utilisateur, une sauvegarde horodatée de vos préférences d\'origine est effectuée et stockée dans **FREECAD_USER_DATA/SavedPreferencePacks/Backups**. Ces sauvegardes sont conservées pendant une semaine.

## Créer un nouveau kit 

Les kits peuvent être créés à la main ou lancés en utilisant le bouton **Save new...** dans l\'onglet *Général* de [Réglage des préférences](Preferences_Editor/fr.md). Cliquer sur le bouton affiche une boîte de dialogue demandant un nom pour le nouveau kit, et affiche un ensemble de cases à cocher permettant de ne stocker qu\'un sous-ensemble de préférences.

<img alt="" src=images/PreferencePacks_SaveNewPack.png  style="width:400px;">

En raison de la façon dont FreeCAD utilise les préférences en interne, seuls les éléments contenus dans ces fichiers modèles peuvent être enregistrés automatiquement en utilisant cette procédure. Les éléments non inclus dans les fichiers modèles doivent être inclus manuellement dans le fichier \*.cfg du kit. Il n\'y a pas de limite intégrée aux éléments de préférences qui peuvent être inclus dans un kit de préférences, mais il est fortement déconseillé aux auteurs de changer la langue de l\'utilisateur, ou de modifier la liste des fichiers récents, ou de changer quoi que ce soit lié à un état temporaire de l\'interface utilisateur (par exemple, la taille enregistrée d\'une fenêtre redimensionnable, etc).

### Détails du modèle 

Ces sections répertorient toutes les préférences contenues dans les modèles intégrés. Pour l\'instant, elles se concentrent sur les éléments liés à l\'apparence, mais les demandes de téléchargement et les suggestions du forum pour des inclusions supplémentaires sont les bienvenues. Les modules complémentaires installés peuvent également fournir leurs propres modèles (non documentés ici). Cliquez sur \"Développer\" à l\'extrême droite de chaque entrée pour voir la liste.


<div class="mw-collapsible mw-collapsed toccolours">

**Couleurs de Arch**


<div class="mw-collapsible-content">

-   Preferences/Mod/Arch/WallColor
-   Preferences/Mod/Arch/StructureColor
-   Preferences/Mod/Arch/RebarColor
-   Preferences/Mod/Arch/WindowColor
-   Preferences/Mod/Arch/WindowGlassColor
-   Preferences/Mod/Arch/PanelColor
-   Preferences/Mod/Arch/ColorHelpers
-   Preferences/Mod/Arch/defaultSpaceColor


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Couleurs de la console**


<div class="mw-collapsible-content">

-   Preferences/OutputWindow/colorText
-   Preferences/OutputWindow/colorLogging
-   Preferences/OutputWindow/colorWarning
-   Preferences/OutputWindow/colorError


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Couleurs de Draft**


<div class="mw-collapsible-content">

-   Preferences/Mod/Draft/constructioncolor
-   Preferences/Mod/Draft/gridTransparency
-   Preferences/Mod/Draft/gridColor
-   Preferences/Mod/Draft/snapcolor


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Couleurs de l\'éditeur**


<div class="mw-collapsible-content">

-   Preferences/Editor/Text
-   Preferences/Editor/Bookmark
-   Preferences/Editor/Breakpoint
-   Preferences/Editor/Keyword
-   Preferences/Editor/Comment
-   Preferences/Editor/Block comment
-   Preferences/Editor/Number
-   Preferences/Editor/String
-   Preferences/Editor/Character
-   Preferences/Editor/Class name
-   Preferences/Editor/Define name
-   Preferences/Editor/Operator
-   Preferences/Editor/Python output
-   Preferences/Editor/Python error
-   Preferences/Editor/Current line highlight


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Police de l\'éditeur**


<div class="mw-collapsible-content">

-   Preferences/Editor/FontSize
-   Preferences/Editor/Font


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Mise en page de la fenêtre principale**


<div class="mw-collapsible-content">

-   Preferences/MainWindow/DockWindows/Std_SelectionView
-   Preferences/MainWindow/DockWindows/Std_ComboView
-   Preferences/MainWindow/DockWindows/Std_ReportView
-   Preferences/MainWindow/DockWindows/Std_PythonView
-   Preferences/MainWindow/DockWindows/Std_TreeView
-   Preferences/MainWindow/DockWindows/Std_PropertyView
-   Preferences/MainWindow/DockWindows/Std_DAGView
-   Preferences/MainWindow/Toolbars/File
-   Preferences/MainWindow/Toolbars/Workbench
-   Preferences/MainWindow/Toolbars/Macro
-   Preferences/MainWindow/Toolbars/View
-   Preferences/MainWindow/Toolbars/Structure
-   Preferences/MainWindow/Toolbars/Navigation


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Couleurs de Path**


<div class="mw-collapsible-content">

-   Preferences/Mod/Path/DefaultNormalPathColor
-   Preferences/Mod/Path/DefaultRapidPathColor
-   Preferences/Mod/Path/DefaultPathMarkerColor
-   Preferences/Mod/Path/DefaultExtentsColor
-   Preferences/Mod/Path/DefaultProbePathColor
-   Preferences/Mod/Path/DefaultHighlightPathColor
-   Preferences/Mod/Path/DefaultBBoxSelectionColor
-   Preferences/Mod/Path/DefaultBBoxNormalColor


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Couleurs de Sketcher**


<div class="mw-collapsible-content">

-   Preferences/View/SketchEdgeColor
-   Preferences/View/SketchVertexColor
-   Preferences/View/EditedEdgeColor
-   Preferences/View/EditedVertexColor
-   Preferences/View/ConstructionColor
-   Preferences/View/ExternalColor
-   Preferences/View/InvalidSketchColor
-   Preferences/View/FullyConstrainedColor
-   Preferences/View/InternalAlignedGeoColor
-   Preferences/View/FullyConstraintElementColor
-   Preferences/View/FullyConstraintConstructionElementColor
-   Preferences/View/FullyConstraintInternalAlignmentColor
-   Preferences/View/FullyConstraintConstructionPointColor
-   Preferences/View/ConstrainedIcoColor
-   Preferences/View/NonDrivingConstrDimColor
-   Preferences/View/ConstrainedDimColor
-   Preferences/View/ExprBasedConstrDimColor
-   Preferences/View/DeactivatedConstrDimColor
-   Preferences/View/CursorTextColor
-   Preferences/View/CursorCrosshairColor
-   Preferences/View/CreateLineColor


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Couleurs de Start**


<div class="mw-collapsible-content">

-   Preferences/Mod/Start/BackgroundColor1
-   Preferences/Mod/Start/BackgroundTextColor
-   Preferences/Mod/Start/PageColor
-   Preferences/Mod/Start/PageTextColor
-   Preferences/Mod/Start/BoxColor
-   Preferences/Mod/Start/LinkColor
-   Preferences/Mod/Start/BackgroundColor2


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Couleurs de TechDraw**


<div class="mw-collapsible-content">

-   Preferences/Mod/TechDraw/Decorations/SectionColor
-   Preferences/Mod/TechDraw/Decorations/CenterColor
-   Preferences/Mod/TechDraw/Decorations/VertexColor
-   Preferences/Mod/TechDraw/Decorations/HighlightColor
-   Preferences/Mod/TechDraw/Colors/Hatch
-   Preferences/Mod/TechDraw/Colors/Background
-   Preferences/Mod/TechDraw/Colors/PreSelectColor
-   Preferences/Mod/TechDraw/Colors/HiddenColor
-   Preferences/Mod/TechDraw/Colors/SelectColor
-   Preferences/Mod/TechDraw/Colors/NormalColor
-   Preferences/Mod/TechDraw/Colors/CutSurfaceColor
-   Preferences/Mod/TechDraw/Colors/GeomHatch
-   Preferences/Mod/TechDraw/Colors/FaceColor
-   Preferences/Mod/TechDraw/Colors/ClearFace


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

**Couleurs de la fenêtre**


<div class="mw-collapsible-content">

-   Preferences/View/BacklightColor
-   Preferences/View/BackgroundColor
-   Preferences/View/BackgroundColor2
-   Preferences/View/BackgroundColor3
-   Preferences/View/BackgroundColor4
-   Preferences/View/Simple
-   Preferences/View/Gradient
-   Preferences/View/UseBackgroundColorMid
-   Preferences/View/HighlightColor
-   Preferences/View/SelectionColor
-   Preferences/View/DefaultShapeColor
-   Preferences/View/RandomColor
-   Preferences/TreeView/TreeEditColor
-   Preferences/TreeView/TreeActiveColor
-   Preferences/MainWindow/TiledBackground
-   Preferences/MainWindow/StyleSheet


</div>


</div>

### Structure du kit de préférence 

Bien que le noyau de la plupart des kits de préférences soit un seul fichier de configuration, en raison de leur conception pour la distribution, une structure auxiliaire est également nécessaire. Quatre fichiers de base définissent un kit, disposés dans la structure de répertoire suivante (pour un kit de préférence nommé \"SamplePreferencePack\") :

-   package.xml
-   SamplePreferencePack/
    -   SamplePreferencePack.cfg
    -   pre.FCMacro
    -   post.FCMacro

Le fichier des [Métadonnées du package](Package_Metadata/fr.md), package.xml, définit le nom du kit de préférences et vous permet d\'attribuer d\'autres éléments de métadonnées tels qu\'un numéro de version, des informations sur l\'auteur et des balises (qui sont affichées dans l\'interface principale sous forme de liste séparée par des virgules). Pour un kit de préférences enregistré à l\'aide de l\'interface graphique comme expliqué ci-dessus, un seul fichier package.xml est créé dans le répertoire **FREECAD_USER_DATA/SavedPreferencePacks/**. Ce fichier est utilisé pour décrire les détails tels que le nom et les balises de tous les kits de préférences enregistrés par l\'utilisateur. Pour modifier le nom ou les étiquettes d\'un kit, ce fichier doit être édité manuellement avec un éditeur de texte. Il peut également fournir un modèle pour les packs de préférences distribués : l\'auteur d\'un kit distribué peut choisir de commencer par sauvegarder un kit localement, puis de copier le sous-répertoire du kit et ce fichier global package.xml comme point de départ, en modifiant le fichier package.xml copié pour ne référencer que le kit en cours de distribution.

D\'autres fichiers peuvent également être inclus dans une distribution, en fonction de ce qui est requis pour le kit. Un kit de préférences bien produit conçu pour distribuer un thème visuel appelé \"DarkSide\" pour FreeCAD pourrait ressembler à ceci :

-   package.xml
-   resources/
    -   icons/
        -   DarkSide.svg
-   DarkSide/
    -   DarkSide.cfg
    -   DarkSide.qss

Notez l\'omission des fichiers *pre.FCMacro* et *post.FCMacro*, qui sont souvent inutiles, ainsi que l\'inclusion d\'une icône (destinée à être affichée par le <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md)), et l\'inclusion d\'un fichier qss (qui sera ensuite référencé dans le fichier de données de configuration *DarkSide.cfg*).

Les fichiers pré- et post-macro sont des macros FreeCAD Python standard, et peuvent contenir toutes les commandes valables dans une telle macro. Si la macro pre.FCMacro génère une exception (de quelque type que ce soit), l\'application du kit de préférences est annulée. Si la post.FCMacro génère une exception (de quelque type que ce soit), l\'application du kit est annulée à l\'aide de la sauvegarde effectuée avant son application. Par exemple, ces macros peuvent être utilisées pour demander à l\'utilisateur d\'accepter la licence, ou pour vérifier qu\'il est satisfait de l\'état final de son système après application.

Le fichier package.xml pour ce kit d\'exemple pourrait être :

    <?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    <package format="1" xmlns="https://wiki.freecad.org/Package_Metadata">
      <name>DarkSide Theme Package</name>
      <description>A preference pack including a stylesheet and other GUI color information for a Dark mode.</description>
      <version>1.0.0</version>
      <maintainer email="chennes@pioneerlibrarysystem.org">Chris Hennes</maintainer>
      <license file="LICENSE">GPLv3</license>
      <url type="repository" branch="main">https://github.com/chennes/DarkSideThemePackage</url>
      <icon>resources/icons/DarkSide.svg</icon>

      <content>
        <preferencepack>
          <name>DarkSide</name>
          <description>Dark mode color scheme</description>
          <tag>color</tag>
          <tag>stylesheet</tag>
          <tag>dark</tag>
          <file>DarkSide.qss</file>
        </preferencepack>
      </content>

    </package>

### Inclure des modèles dans votre extension 

De nombreuses extensions comportent des informations de préférence spécifiables par l\'utilisateur qui sont ajoutées au fichier user.cfg. L\'auteur d\'une extension peut également choisir de fournir un fichier modèle de kit de préférences qui répertorie les variables de configuration de l\'utilisateur pouvant être enregistrées automatiquement à l\'aide de la méthode \"Save new pack\" décrite ci-dessus. Pour inclure ces fichiers modèles, les auteurs d\'addons doivent créer un sous-répertoire dans leur paquet appelé \"PreferencePackTemplates\" ou \"preference_pack_templates\". Ce dossier doit contenir un ou plusieurs fichiers \*.cfg : chacun doit être un fichier XML user.cfg valide et bien formé contenant une ou plusieurs variables de configuration définies sur leurs valeurs par défaut. Le nom du fichier doit refléter son objectif, par exemple \"colors.cfg\", \"active_tabs.cfg\", etc. Cet ensemble de fichiers sera présenté à l\'utilisateur lorsqu\'il enregistrera un nouveau kit de préférences, chaque fichier recevant une entrée cochable dans la liste des éléments à enregistrer. Le nom du fichier est utilisé pour générer l\'entrée de l\'interface utilisateur, les caractères de soulignement étant remplacés par des espaces (et l\'extension étant omise).

## Distribuer un kit 

Les kits de préférences sont distribués de manière identique aux [ateliers externes](External_workbenches/fr.md) par le biais du <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md). Pour installer un kit manuellement, utilisez git pour cloner le dépôt du kit dans votre répertoire de données FreeCAD ((entrez `App.getUserAppDataDir()` dans la [console Python](Python_console/fr.md) pour obtenir ce chemin)), dans un sous-répertoire appelé \"Preference Packs\".

Voir aussi [Kits de préférences privés](Private_Preference_Packs/fr.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Developer Documentation](Category_Developer Documentation.md) > Preference Packs/fr
