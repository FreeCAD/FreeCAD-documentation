# Add Workbench to Addon Manager/ru
{{TOCright}}



## Вступление

Данная страница содержит пошаговую инструкцию позволяющую добавить Python верстак в [Менеджер дополнений](Std_AddonMgr/ru.md).

Требуется:

-   Наличие локального git репозитория.
-   Наличие удаленного git репозитория. Поддерживаемые git хостинги: [GitHub](https://github.com), [GitLab](https://about.gitlab.com/), [Framagit](https://framagit.org/public/projects) и [Debian Salsa](https://salsa.debian.org/public).
-   Git должен быть установлен локально.



## Активация режима для разработчиков 

1.  Откройте [Редактор настроек](Preferences_Editor/ru.md): через пункт меню **Правка → <img src="images/Std_DlgPreferences.svg" width=16px> Настройки...**.
2.  Выберите раздел **<img src="images/Std_AddonMgr.svg" width=16px> Менеджер дополнений** в панели слева.
3.  На в кладке **Настройки менеджера дополнений** включите флажок **Режим разработчика дополнений**. Это сделает доступной кнопку **Инструменты разработчика...** в Менеджере дополнений.
4.  Нажмите кнопку **OK** для закрытия Редактора настроек.



## Создание package.xml файла 

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



## Добавление верстака в .gitmodules файл 

1.  Сделайте Fork <https://github.com/FreeCAD/FreeCAD-addons> репозитория.
2.  Создайте новую ветвь.
3.  Отредактируйте файл **.gitmodules**, добавьте в него ваше дополнение (Addon) в алфавитном порядке.
4.  Сделайте Push в новую ветку GitHub.
5.  Отправьте Pull Request с изменениями в FreeCAD-Addons репозиторий с измененным **.gitmodules** файлом.



## Смотрите также 

-   [Workbench creation](Workbench_creation.md)
-   [Package Metadata](Package_Metadata.md): Detailed information about the **package.xml** file.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [Developer Documentation](Category_Developer Documentation.md) > Add Workbench to Addon Manager/ru
