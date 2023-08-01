---
- GuiCommand:
   Name:Plot Axes
   Name/fr:Plot Axes
   MenuLocation:Plot - Configurer les axes‏‎
   Workbenches:[Plot](Plot_Workbench/fr.md)
---

# Plot Axes/fr

## Description

Le module standard graphique fournit déjà un outil de base pour contrôler les axes du tracé <img alt="" src=images/Matplotlib_edit_subplot.png  style="width:24px;"> mais cet outil est clairement insuffisant lorsque des tracés multi-axes doivent être manipulés, comme c\'est le cas dans le [Tutoriel graphique à plusieurs axes](Plot_MultiAxes_tutorial/fr.md). Pour surmonter cette limitation, vous pouvez installer l\'<img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [atelier Plot](Plot_Workbench/fr.md) en utilisant le [Gestionnaire des extensions](Std_AddonMgr/fr.md), ainsi un outil plus complet pour éditer les axes du tracé sera disponible.

<img alt="" src=images/Plot_MultiAxes_Example.png  style="width:600px;">

## Utilisation

Sélectionnez l\'onglet du graphique que vous souhaitez modifier, puis lancez cet outil.

Il est fortement recommandé de commencer à mettre à l\'échelle l\'ensemble du graphique afin d\'être sûr qu\'il tiendra dans l\'espace disponible. Pour cela, activez l\'option **Appliquer à tous les axes**.

![Apply to all axes](images/Apply_To_All_Axes.png ) 
*Sélecteur pour la commande Appliquer à tous les axes*

Ensuite, vous pouvez mettre à l\'échelle l\'ensemble du graphique pour l\'adapter à la zone visible, en utilisant les quatre curseurs suivants

![Plot area controlling sliders](images/Plot_Axes_Sliders.png ) 
*Curseurs pour mettre à l'échelle le graphique*

Lorsque vous êtes satisfait de la taille générale du tracé, vous pouvez désélectionner **Appliquer à tous les axes** et affiner chaque ensemble d\'axes indépendamment. Il suffit de sélectionner l\'ensemble des axes que vous souhaitez modifier en haut de la page.

![Plot axes selector](images/Plot_Axes_Active.png ) 
*Sélecteur pour l'ensemble des axes à éditer*.

Vous pouvez à nouveau utiliser les curseurs pour contrôler la zone couverte par ce ce graphique secondaire. Vous pouvez également contrôler l\'emplacement des points et des titres pour l\'axe X et l\'axe Y.

![Plot axes position editor](images/Plot_Axes_Position.png ) 
*Éditeur de positions pour les axes sélectionnés*

Plus précisément, vous pouvez définir si l\'axe X est affiché en dessous ou au dessus du tracé, ainsi que si l\'axe Y est affiché à gauche ou à droite du tracé. Vous pouvez même définir le décalage des deux axes par rapport à la ligne de base du tracé.

Enfin, vous pouvez définir les valeurs minimales et maximales prises en compte pour chaque ensemble d\'axes, ce que l\'on appelle le zoom.

![Plot zoom editor](images/Plot_Axes_Zoom.png ) 
*Editeur des valeurs minimales et maximales considérées*





{{Plot_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > [Addons](Category_Addons.md) > [Plot](Plot_Workbench.md) > Plot Axes/fr
