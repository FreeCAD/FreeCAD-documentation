# Add Workbench to Addon Manager
## Introduction

These are step-by-step instructions on how to add a Python workbench to the [Addon Manager](Std_AddonMgr.md).

Requirements:

-   A local git repository.
-   A remote git repository. Supported git hosts are [GitHub](https://github.com), [GitLab](https://about.gitlab.com/), [Framagit](https://framagit.org/public/projects) and [Debian Salsa](https://salsa.debian.org/public).
-   Git must be installed.

## Enable developer mode 

1.  Open the [Preferences Editor](Preferences_Editor.md): select the **Edit → <img src="images/Std_DlgPreferences.svg" width=16px> Preferences...** option from the menu.
2.  Select the **<img src="images/Std_AddonMgr.svg" width=16px> Addon Manager** option in the left bar.
3.  On the **Addon manager options** tab check the **Addon developer mode** checkbox. This will enable the **Developer tools...** button in the Addon Manager.
4.  Press the **OK** button to close the Preferences Editor.

## Create the package.xml file 

1.  Open the [Addon Manager](Std_AddonMgr.md): select the **Tools → <img src="images/Std_AddonMgr.svg" width=16px> Addon manager** option from the menu.
2.  Press the **Developer tools...** button.
3.  The **Addon Developer Tools** dialog opens.
    <img alt="" src=images/Addon_Manager_Addon_Developer_Tools_Dialog.png  style="width:350px;">
4.  Enter the following:
    -   
        **Path to Addon**
        
        : The path to the local git repository.

    -   
        **Addon Name**
        
        : This will appear in the listings of the Addon Manager.

    -   
        **Description**
        
        : Idem.

    -   
        **Version**
        
        : Idem.

    -   
        **Repository URL**
        

    -   
        **Primary branch**
        

    -   
        **README URL**
        
        : Recommended.

    -   
        **Icon**
        
        : The icon must be part of the repository.
5.  Press the **<img src="images/List-add.svg" width=16px>** button at the bottom of the dialog.
6.  The **Content Item** dialog opens.
    <img alt="" src=images/Addon_Manager_Content_Item_Dialog.png  style="width:350px;">
7.  The **Content type** should be set to {{Value|Workbench}}.
8.  Check the **This is the only item in the Addon** checkbox.
9.  Enter the **Workbench class name**. This is the class name specified in the **InitGui.py** file.
10. For the **Subdirectory** enter {{Value|./}}.
11. Press the **OK** button to close the dialog.
12. Press the **Save** button to close the **Addon Developer Tools** dialog and save the **package.xml** file.
13. Press the **<img src="images/Process-stop.svg" width=16px> Close** button to close the Addon Manager.
14. Push the created file to your remote repository.

## Add the workbench to the .gitmodules file 

1.  Fork <https://github.com/FreeCAD/FreeCAD-addons>.
2.  Create a new branch.
3.  Edit the **.gitmodules** file to include your new Addon, in alphabetical order.
4.  Push the new branch to GitHub.
5.  Submit a Pull Request to the FreeCAD-Addons repository with the new **.gitmodules** file.

## See also 

-   [Workbench creation](Workbench_creation.md)
-   [Package Metadata](Package_Metadata.md): Detailed information about the **package.xml** file.



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Add Workbench to Addon Manager
