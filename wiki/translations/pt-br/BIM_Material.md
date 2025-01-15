---
 GuiCommand:
   Name: BIM Material
   MenuLocation: Manage , Material
   Workbenches: BIM_Workbench
---

# BIM Material/pt-br


</div>



## Descrição


<div lang="en" dir="ltr" class="mw-content-ltr">

Shows the **BIM material** dialog. The dialog allows to quickly and easily perform material-related operations, with extra focus on efficient working with many objects and many materials.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Create new [material](Arch_SetMaterial.md) or [multimaterial](Arch_MultiMaterial.md)
2.  Attribute an existing material or multimaterial to selected object(s).


</div>

<img alt="" src=images/BIM_materials_screenshot.png  style="width:600px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*The materials manager*


</div>



## Utilização


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  (Optionally) select one or more objects
2.  Press the **<img src="images/BIM_Material.svg" width=16px> [Material](BIM_Material.md)** button in the toolbar.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   If there is no existing material in the active document, the material manager window is not displayed, and a [new material](Arch_SetMaterial.md) will be created.
-   If there is at least one material or multimaterial in the document, the Materials Manager window will open.


</div>



## Ferramentas de gerenciamento de materiais 

O gerenciador de materiais permite:


<div lang="en" dir="ltr" class="mw-content-ltr">

-   **Search materials by name**: Use the search box
-   **Assign a material to the selected object(s)**: Pressing OK with a material selected will assign it to the selected object(s)
-   **Create a [material](Arch_SetMaterial.md)**: Press the **Create new material** button
-   **Create a [multimaterial](Arch_MultiMaterial.md)**: Press the **Create new multi-material** button
-   **Delete a material**: Select a material and right-click a material and choose \"Delete\"
-   **Delete unused materials**: Press the **Delete unused** button. All materials that are not used by any object will be removed
-   **Merge duplicate materials**: Press the **Merge duplicates** button. Merges the materials with exact same names (ex. Concrete and Concrete) or exact same names with a numeric suffix (ex. Concrete and Concrete001) together
-   **Rename a material**: Right-click a material and choose \"Rename\"
-   **Duplicate a material**: Right-click a material and choose \"Duplicate\". This will create a full, independent copy of the chosen material with same settings
-   **Merge two materials together**: Right-click a material and choose \"Merge to\...\", then select another material. The first one will be removed, and all objects that were using the first one will be assigned the second one


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">





</div>



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Material/pt-br
