---
- GuiCommand:/fr
   Name:Path Sanity
   Name/fr:Path Rechercher des erreurs
   MenuLocation:
   Workbenches:[Path](Path_Workbench/fr.md)
   Version:0.19
   SeeAlso:
---


</div>

## Description


<div class="mw-translate-fuzzy">

## Description {#description_1}

De nombreux utilisateurs de Path sont des amateurs et des bricoleurs. En tant que tels, ils utilisent leurs machines CNC pour exécuter [gcode](gcode.md) qu\'ils ont configuré et généré eux-mêmes. Ce n\'est pas le cas pour la plupart des utilisateurs professionnels/commerciaux. Dans les ateliers professionnels, différentes personnes sont responsables de la création du gcode (programmeurs CNC) à partir de ceux qui l\'exécutent sur les machines (opérateur CNC).


</div>


<div class="mw-translate-fuzzy">

Les amateurs exécutent généralement le gcode quelques minutes après le post-traitement et probablement seulement une ou deux fois. Chez un professionnel, un gcode éprouvé peut être exécuté plusieurs fois pendant des mois ou des années après sa création initiale.


</div>


<div class="mw-translate-fuzzy">

Un problème qui se pose dans un atelier CNC professionnel est qu\'il existe de nombreuses hypothèses faites par le programmeur qui ne sont PAS communiquées dans le gcode lui-même. Par exemple, le gcode peut appeler un outil \"T3\" mais à moins qu\'il ne soit commenté, le gcode ne dit pas à quel type d\'outil \"T3\" se réfère. On suppose simplement que T3 dans le système CAM est le même que T3 sur la machine. Il existe de nombreuses hypothèses comme celle-ci concernant la configuration de la machine, l\'outillage, le matériau, l\'orientation des pièces, etc. Même si le gcode est parfait, si l\'opérateur ne configure pas la machine avec les mêmes hypothèses, il peut planter.


</div>

Les ateliers commerciaux créent souvent un \'manuel d\'installation\' qui documente toutes ces hypothèses et donne aux opérateurs ce dont ils ont besoin pour configurer la machine et produire une pièce.


<div class="mw-translate-fuzzy">

[Path Sanity](Path_Sanity/fr.md) est l\'outil de l\'atelier Path pour générer ce type d\'informations. La sortie de la commande Path Sanity est un fichier html autonome avec des images intégrées. <img alt="Ci-dessus: exemple de rapport généré par Path Sanity" src=images/Sanity.jpg  style="width:400" height="600px;">


</div>

## À propos du rapport {#à_propos_du_rapport}

Autant que possible, le contenu est indépendant de FreeCAD. L\'opérateur CNC ne peut jamais utiliser FreeCAD, donc la terminologie propre à FreeCAD/Path prête à confusion. Le rapport comporte des sections distinctes et est formaté pour rendre la recherche des choses facile et prévisible.

### Part Information {#part_information}

Cette section donne un aperçu de ce qui est fait. Idéalement, l\'image doit montrer les objets de base. S\'il existe plusieurs objets de base, l\'image doit montrer comment ils s\'imbriquent.

### Run Summary {#run_summary}

Donne une vue rapide des hauteurs minimales et maximales et des temps de fonctionnement.

### Rough Stock {#rough_stock}

Détaille l\'objet Stock de la Tâche (Job). C\'est un domaine dans lequel Path bénéficierait d\'une certaine amélioration. Une propriété matérielle rudimentaire pour le stock serait utile ici et pourrait également être utilisée pour aider à suggérer des alimentations/vitesses.

### Tool Data {#tool_data}


<div class="mw-translate-fuzzy">

Contient des sous-sections pour chaque numéro d\'outil utilisé dans le travail. Il détaille ce que le programmeur suppose que l\'outil est et quelles opérations l\'utilisent. Cette section ne fonctionne qu\'avec le nouveau système de toolbit. C\'est un autre domaine où Path doit être amélioré. Plus précisément, les Toolbits ont besoin d\'attributs supplémentaires sur l\'outil comme le fabricant/l\'url/le numéro de pièce.


</div>

### Output


<div class="mw-translate-fuzzy">

Donne des détails sur où et quand le gcode a été post-traité. Il indique également si le travail comporte des arrêts facultatifs/obligatoires afin que l\'opérateur sache s\'il peut s\'éloigner de la machine en toute sécurité pendant une course.


</div>

### Coolant

Liquide de refroidissement

### Fixtures and Work-holding {#fixtures_and_work_holding}

Affiche les pièces dans le contexte de l\'enveloppe du stock et montre également l\'origine de la pièce.

### Squawks

Avertissements et erreurs détectés par [Path Rechercher des erreurs](Path_Sanity/fr.md). Ceux-ci peuvent ou non être des problèmes, mais ils sont notés pour une attention supplémentaire. Par exemple, si le même numéro d\'outil est utilisé pour différents outils, il s\'affichera comme une erreur. Si un contrôleur d\'outil n\'a pas d\'avance / vitesse configurée, il apparaîtra comme un avertissement. Il détectera également et avertira les contrôleurs d\'outils inutilisés. Path bénéficierait ici de la possibilité d\'ajouter des notes ou des avertissements arbitraires.

## Utilisation


<div class="mw-translate-fuzzy">

1.  Sélectionne un travail de chemin dans la [vue arborescente](Tree_view/fr.md)
2.  Appuyez sur le bouton <img alt="" src=images/Path_Sanity.svg  style="width:24px;"> [Path Sanity](Path_Sanity/fr.md).
    -   Les informations pertinentes sont collectées dans un dictionnaire python puis formatées au format asciidoc.
    -   Le fichier asciidoc est écrit sur le disque au même emplacement que le fichier qui sera post-traité.
    -   Un processus externe appelle asciidoctor pour lire l\'asciidoc et générer le html.
    -   Cela lancera automatiquement le navigateur Web du système pour afficher le rapport HTML autonome généré.


</div>

## Notez un ASCIIDOC et un Asciidoctor {#notez_un_asciidoc_et_un_asciidoctor}

Asciidoc est un format de balisage léger pour la création de notes, d\'articles, de livres, etc. Il est lisible par l\'homme et facilement traduit dans d\'autres formats.

Asciidoctor est un processeur de texte open-source rapide pour la conversion d\'asciidoc en HTML, PDF ou d\'autres formats. Il est disponible pour Linux, Windows et MacOS. Asciidoctor n\'est pas installé avec FreeCAD. Si vous utilisez Path Sanity sans installer Asciidoctor, le fichier source asciidoc sera généré mais le HTML résultant ne sera pas produit. [Site Asciidoctor](https://asciidoctor.org/)


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}} 
