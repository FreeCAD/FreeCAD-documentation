# Preferences Editor/zh-cn
## Introduction


<div class="mw-translate-fuzzy">

FreeCAD的首选项系统位于**Edit menu → Preferences**。


</div>


<div class="mw-translate-fuzzy">

FreeCAD中的功能被分为不同的模块，每个模块负责实现一种特定[workbench](Workbenches.md)的具体工作。 FreeCAD采用的是延迟加载方式，意即只有当需要使用特定组件时才会进行加载。您在FreeCAD的工具栏中选择工作台时可能会注意到这一点，因为在加载工作台及其所有组件时需要花费一点儿时间。在进行首选项设置时也是如此。


</div>

To preserve resources, FreeCAD does not automatically load all available workbenches. See [Workbenches](#Workbenches.md) for more information. For a list of workbench related preferences see [Workbench related preferences](#Workbench_related_preferences.md).


<div class="mw-translate-fuzzy">

在没有加载任何模块时，您可以访问两个配置部分，分别用于应用通用设置（general）与显示设置（display）。当您使用特定的工作台时，便会在新选项卡中显示对应工作台的首选项设置，并在**Import-Export**新加部分显示该工作台所支持的文件格式。


</div>


<div class="mw-translate-fuzzy">

点击首选项左下角的**Reset**按钮，即可将FreeCAD中的**所有**首选项设置还原为其默认值。


</div>

Some advanced preferences can only be changed in the [Parameter editor](Std_DlgParameter.md). The [Fine-tuning](Fine-tuning.md) page lists some of them.

This page has been updated for version 1.0.




<div class="mw-translate-fuzzy">

## 通用设置


</div>


<div class="mw-translate-fuzzy">

本首选项部分包含6个选项卡：


</div>

In {{VersionMinus|0.21}} the seventh page, Help, is only available if the [Help Addon](https://github.com/FreeCAD/FreeCAD-Help) has been [installed](Std_AddonMgr.md).



### 常规

<img alt="" src=images/Preferences_General_Page_General.png  style="width:400px;">


<div class="mw-translate-fuzzy">

在*General*选项卡中，您可以指定下列内容：


</div>


<div class="mw-translate-fuzzy">

+++
| 名称                                             | 描述                                                                                                                                                                                                                                                                         |
+==================================================+==============================================================================================================================================================================================================================================================================+
|                                   | 选择FreeCAD的用户界面语言                                                                                                                                                                                                                                                    |
| **更改语言**                         |                                                                                                                                                                                                                                                                              |
|                                               |                                                                                                                                                                                                                                                                              |
+++
|                                   | 指定有多少最近用过的文件显示在recent files列表中                                                                                                                                                                                                                             |
| **最近文件列表大小**                 |                                                                                                                                                                                                                                                                              |
|                                               |                                                                                                                                                                                                                                                                              |
+++
|                                   | 如果选中此复选框，则FreeCAD的主窗口背景将默认由以下图片填充：<img alt="" src=images/Background.png  style="width:64px;">                                                                                                                                                                |
| **启用平面背景**                     | 本选项只有在**样式表：**/*No style sheet*被选中时才会生效。                                                                                                                                                                                        |
|                                               | 将图片加入到下列路径中的**Gui/Images**文件夹下即可改变贴图内容                                                                                                                                                                                        |
|                                                  | \[<https://www.howtogeek.com/318177/what-is-the-appdata-folder-in-windows/> **%APPDATA%]/FreeCAD** (在Windows上),                                                                                                                                     |
|                                                  | **$HOME/.FreeCAD** (在Linux上) or                                                                                                                                                                                                                     |
|                                                  | **$HOME/Library/Preferences/FreeCAD** (在MacOS上)。                                                                                                                                                                                                   |
|                                                  | 将图片文件命名为**background.png**，再依次取消/选中本选项来查看效果。                                                                                                                                                                                 |
|                                                  |                                                                                                                                                                                                                                                                              |
|                                                  |                                                                                                                                                                                                                                                                    |
|                                                  | </div>                                                                                                                                                                                                                                                                       |
|                                                  |                                                                                                                                                                                                                                                                           |
|                                                  | Optionally, imported files can be excluded from this list, and exported files can be included. See [Fine-tuning](Fine-tuning.md).                                                                                                                                    |
+++
|                                   | If checked, the background of FreeCAD\'s main window will by default consist of tiles of this image: <img alt="" src=images/Background.png  style="width:64px;">                                                                                                                        |
| **Enable tiled background**          |                                                                                                                                                                                                                                                                              |
|                                               | This option only has an effect if no **Style sheet** is selected.                                                                                                                                                                                  |
|                                                  |                                                                                                                                                                                                                                                                              |
|                                                  | The image can be changed by adding the folders **Gui/Images** in the folder:                                                                                                                                                                          |
|                                                  |                                                                                                                                                                                                                                                                              |
|                                                  |                                                                                                                                                                                                                                                               |
|                                                  | **[https://www.howtogeek.com/318177/what-is-the-appdata-folder-in-windows/ %APPDATA%]/FreeCAD**                                                                                                                                                                     |
|                                                  |                                                                                                                                                                                                                                                                           |
|                                                  | (on Windows),                                                                                                                                                                                                                                                                |
|                                                  |                                                                                                                                                                                                                                                                              |
|                                                  |                                                                                                                                                                                                                                                               |
|                                                  | **$HOME/.FreeCAD**                                                                                                                                                                                                                                                  |
|                                                  |                                                                                                                                                                                                                                                                           |
|                                                  | (on Linux) or                                                                                                                                                                                                                                                                |
|                                                  |                                                                                                                                                                                                                                                                              |
|                                                  |                                                                                                                                                                                                                                                               |
|                                                  | **$HOME/Library/Preferences/FreeCAD**                                                                                                                                                                                                                               |
|                                                  |                                                                                                                                                                                                                                                                           |
|                                                  | (on macOS).                                                                                                                                                                                                                                                                  |
|                                                  |                                                                                                                                                                                                                                                                              |
|                                                  | Place a file named **background.png** in the **Images** folder, and uncheck/check this option to see the changed file.                                                                                                         |
+++
|                                   | If checked, a splash screen is shown when starting FreeCAD.                                                                                                                                                                                                                  |
| **Enable splash screen at start up** |                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                    |
|                                                  | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                             |
|                                                  |                                                                                                                                                                                                                                                                           |
+++
|                                   | 选择样式表。样式表定义了FreeCAD用户界面的外观。                                                                                                                                                                                                                              |
| **样式表：**                         |                                                                                                                                                                                                                                                                              |
|                                               |                                                                                                                                                                                                                                                                              |
+++
|                                   | 选择工具栏图标的大小。                                                                                                                                                                                                                                                       |
| **工具栏图标大小**                   |                                                                                                                                                                                                                                                                              |
|                                               |                                                                                                                                                                                                                                                                              |
+++
|                                   | 选择FreeCAD开启后将直接打开的工作台。                                                                                                                                                                                                                                        |
| **启动后自动加载模块**               |                                                                                                                                                                                                                                                                              |
|                                               |                                                                                                                                                                                                                                                                              |
+++
|                                   | 如果选中此项, 则在FreeCAD开启时展示启动画面。                                                                                                                                                                                                                                |
| **打开软件启动界面**                 | 可通过向**%APPDATA%/FreeCAD**（ %APPDATA%是用户在操作系统中为FreeCAD指定的应用文件夹）添加**Gui/Images**文件夹来修改启动画面。将作为启动画面的图像命名为**splash_image.png**并重启FreeCAD即可看到效果。 |
|                                               |                                                                                                                                                                                                                                                                              |
+++
|                                   | 利用此选项可实现在Python控制台中令超出一行中的文本自动换行。利用**View → Panels → Python console**菜单来开启Python控制台。                                                                                                                         |
| **启用自动换行**                     |                                                                                                                                                                                                                                                                              |
|                                               |                                                                                                                                                                                                                                                                              |
+++


</div>



### 文档

<img alt="" src=images/Preferences_General_Page_Document.png  style="width:400px;">


<div class="mw-translate-fuzzy">

在*Document*选项卡中，您可以指定以下内容：


</div>


<div class="mw-translate-fuzzy">

+++
| 名称                                               | 描述                                                                                                                                                                                                                                                                               |
+====================================================+====================================================================================================================================================================================================================================================================================+
|                                     | 如果选中此选项，FreeCAD将在启动时创建一个新文档。                                                                                                                                                                                                                                  |
| **启动时创建新文档**                   |                                                                                                                                                                                                                                                                                    |
|                                                 |                                                                                                                                                                                                                                                                                    |
+++
|                                     | 指定**FCStd**文件的压缩级别。**FCStd**文件为ZIP压缩文件。因此，您可以将其后缀**.FCStd**改为**.zip**，并用ZIP归档程序来打开它们。                                                       |
| **Document save compression level**    |                                                                                                                                                                                                                                                                                    |
|                                                 |                                                                                                                                                                                                                                                                                    |
+++
|                                     | 如果选中此选项，所有文档的更改情况将被保存下来，因此即可实现undone/redone。                                                                                                                                                                                                        |
| **在文档上使用撤消/重做**              |                                                                                                                                                                                                                                                                                    |
|                                                 |                                                                                                                                                                                                                                                                                    |
+++
|                                     | 指定可以记录多少次Undo/Redo操作。                                                                                                                                                                                                                                                  |
| **最大撤消/重做步数**                  |                                                                                                                                                                                                                                                                                    |
|                                                 |                                                                                                                                                                                                                                                                                    |
+++
|                                     | 如果存在恢复文件，则FreeCAD将在开启时自动运行此文件进行恢复。此法可对程序崩溃时的文件进行恢复。                                                                                                                                                                                    |
| **在启动时运行自动恢复**               |                                                                                                                                                                                                                                                                                    |
|                                                 |                                                                                                                                                                                                                                                                                    |
+++
|                                     | 指定多久写一次恢复文件。                                                                                                                                                                                                                                                           |
| **每次都保存自动恢复信息**             |                                                                                                                                                                                                                                                                                    |
|                                                 |                                                                                                                                                                                                                                                                                    |
+++
|                                     | 如果选中此选项，在保存文档时，也将存储一份项目的缩略图。此缩略图将显示在[启动工作台](Start_Workbench.md)中的最近打开文件列表中。                                                                                                                                           |
| **保存文件时同时保存缩略图到项目文件** |                                                                                                                                                                                                                                                                                    |
|                                                 |                                                                                                                                                                                                                                                                                    |
+++
|                                     | 如果选中此选项，则会将FreeCAD程序的logo ![24px](images/FreeCAD-logo.svg)添加至缩略图中。此选项仅在开启**保存文件时同时保存缩略图到项目文件**选项后才会生效。                                                                                    |
| **将程序徽标添加到生成的缩略图**       |                                                                                                                                                                                                                                                                                    |
|                                                 |                                                                                                                                                                                                                                                                                    |
+++
|                                     | 如果选中此选项，在保存文档时也会保留备份文件。您可以指定保留备份文件的数量。这些文件中保存的是此前（previously）的文档版本。第一个备份文件的后缀为 **.FCStd1**, 第二个后缀为**.FCStd2**，并以此类推。                                |
| **保存文档时要保留的最大备份文件数**   |                                                                                                                                                                                                                                                                                    |
|                                                 |                                                                                                                                                                                                                                                                                    |
+++
|                                     | 如果选中此选项，则不同的对象可以使用相同的标签/名称。例如，同一文档中的不同零件与features可用相同的名字。                                                                                                                                                                          |
| **在一个文档中允许重复的对象标签**     |                                                                                                                                                                                                                                                                                    |
|                                                 |                                                                                                                                                                                                                                                                                    |
+++
|                                     | 创建的所有文档均采用此指定的作者名。对于匿名作者而言，作者名字的区域为空白内容。若开启了**保存时的设置**选项，则在保存文件时将*Last modified by*的内容设置为此作者名。可通过**File → Project information**菜单来查看该文本域。 |
| **作者姓名**                           |                                                                                                                                                                                                                                                                                    |
|                                                 |                                                                                                                                                                                                                                                                                    |
+++
|                                     | 将创建的所有文档都指定为此公司名称。                                                                                                                                                                                                                                               |
| **公司**                               |                                                                                                                                                                                                                                                                                    |
|                                                 |                                                                                                                                                                                                                                                                                    |
+++
|                                     | 为新文档所指定的默认许可证。对于预定义的许可证而言，**许可证网址**将自动做出对应的设置。而针对自定义许可证或特殊许可证来讲，可选择\'Other（其他）\'项。                                                                                                  |
| **默认许可证**                         |                                                                                                                                                                                                                                                                                    |
|                                                 |                                                                                                                                                                                                                                                                                    |
+++
|                                     | 指定URL来描述**默认许可证**中所选的许可证。                                                                                                                                                                                                              |
| **许可证网址**                         |                                                                                                                                                                                                                                                                                    |
|                                                 |                                                                                                                                                                                                                                                                                    |
+++


</div>



### 选择

<img alt="" src=images/Preferences_General_Page_Selection.png  style="width:400px;">

On this page you can specify the following:

+++
| Name                                                                                              | Description                                                                                                                                                                                                                                                         |
+===================================================================================================+=====================================================================================================================================================================================================================================================================+
|                                                                                    | If checked, [3D view](3D_view.md) preselection is turned on and the specified color will be used for it. Preselection means that for example edges of objects will be highlighted while hovering over them with the mouse to indicate they can be selected. |
| **Enable preselection**                                                               |                                                                                                                                                                                                                                                                     |
|                                                                                                |                                                                                                                                                                                                                                                                     |
+++
|                                                                                    | If checked, 3D view selection is turned on and the specified color is used for it. If not checked, objects can only be selected in the [Tree view](Tree_view.md).                                                                                           |
| **Enable selection**                                                                  |                                                                                                                                                                                                                                                                     |
|                                                                                                | Note that objects created while this option is not checked will have their **Selectable** property set to `False`. With that value they are not selectable in the 3D view, even if this option is checked again.         |
+++
|                                                                                    | Sets the area for picking elements in the [3D view](3D_view.md). Larger value makes it easier to pick things, but can make some small features impossible to select.                                                                                        |
| **Pick radius (px)**                                                                  |                                                                                                                                                                                                                                                                     |
|                                                                                                |                                                                                                                                                                                                                                                                     |
+++
|                                                                                    | Enables the [Tree view SyncView mode](Std_TreeSyncView.md).                                                                                                                                                                                                 |
| **Auto switch to the 3D view containing the selected item**                           |                                                                                                                                                                                                                                                                     |
|                                                                                                |                                                                                                                                                                                                                                                                     |
+++
|                                                                                    | Enables the [Tree view SyncSelection mode](Std_TreeSyncSelection.md).                                                                                                                                                                                       |
| **Auto expand tree item when the corresponding object is selected in 3D view**        |                                                                                                                                                                                                                                                                     |
|                                                                                                |                                                                                                                                                                                                                                                                     |
+++
|                                                                                    | Enables the [Tree view PreSelection mode](Std_TreePreSelection.md).                                                                                                                                                                                         |
| **Preselect the object in 3D view when mouse over the tree item**                     |                                                                                                                                                                                                                                                                     |
|                                                                                                |                                                                                                                                                                                                                                                                     |
+++
|                                                                                    | Enables the [Tree view RecordSelection mode](Std_TreeRecordSelection.md).                                                                                                                                                                                   |
| **Record selection in tree view in order to go back/forward using navigation button** |                                                                                                                                                                                                                                                                     |
|                                                                                                |                                                                                                                                                                                                                                                                     |
+++
|                                                                                    | Each [Tree view](Tree_view.md) item will get a checkbox. This is for example useful for selecting multiple items on a touchscreen.                                                                                                                          |
| **Add checkboxes for selection in document tree**                                     |                                                                                                                                                                                                                                                                     |
|                                                                                                |                                                                                                                                                                                                                                                                     |
+++

### Cache

<img alt="" src=images/Preferences_General_Page_Cache.png  style="width:400px;">

These preferences are related to the cache directory where FreeCAD stores temporary files.

On this page you can specify the following:

+++
| Name                                                | Description                                                                                                                                 |
+=====================================================+=============================================================================================================================================+
|                                      | Shows the path of the cache directory. Use the **![16px](images/Document-open.svg)** button to browse the directory.    |
| **Location (read-only)**                |                                                                                                                                             |
|                                                  |                                                                                                                                             |
+++
|                                      | Controls the frequency with which the directory size is checked. The options are:                                                           |
| **Check periodically at program start** |                                                                                                                                             |
|                                                  | -   **Always**                                                                                                                              |
|                                                     | -   **Daily**                                                                                                                               |
|                                                     | -   **Weekly**                                                                                                                              |
|                                                     | -   **Monthly**                                                                                                                             |
|                                                     | -   **Yearly**                                                                                                                              |
|                                                     | -   **Never**                                                                                                                               |
+++
|                                      | Specifies the maximum size of the directory. You will be notified if a check is performed and the size exceeds this value. The options are: |
| **Cache size limit**                    |                                                                                                                                             |
|                                                  | -   **100 MB**                                                                                                                              |
|                                                     | -   **300 MB**                                                                                                                              |
|                                                     | -   **500 MB**                                                                                                                              |
|                                                     | -   **1 GB**                                                                                                                                |
|                                                     | -   **2 GB**                                                                                                                                |
|                                                     | -   **3 GB**                                                                                                                                |
+++
|                                      | Shows the current size of the directory, if available. Press the **Check now...** button to update the value.          |
| **Current cache size**                  |                                                                                                                                             |
|                                                  |                                                                                                                                             |
+++

### Notification Area 

<img alt="" src=images/Preferences_General_Page_Notification_Area.png  style="width:400px;">

These preferences control the Notification Area and its notifications.

On this page (<small>(v0.21)</small> ) you can specify the following:

+++
| Name                                                | Description                                                                                                |
+=====================================================+============================================================================================================+
|                                      | If checked, the Notification Area will appear in the status bar.                                           |
| **Enable Notification Area**            |                                                                                                            |
|                                                  |                                                                                                            |
+++
|                                      | If checked, non-intrusive notifications will appear next to the Notification Area in the status bar.       |
| **Enable non-intrusive notifications**  |                                                                                                            |
|                                                  |                                                                                                            |
+++
|                                      | If checked, errors intended for developers will appear in the Notification Area.                           |
| **Debug errors**                        |                                                                                                            |
|                                                  |                                                                                                            |
+++
|                                      | If checked, warnings intended for developers will appear in the Notification Area.                         |
| **Debug warnings**                      |                                                                                                            |
|                                                  |                                                                                                            |
+++
|                                      | Maximum duration during which notifications are shown (unless mouse buttons are clicked).                  |
| **Maximum Duration**                    |                                                                                                            |
|                                                  |                                                                                                            |
+++
|                                      | Minimum duration (idem).                                                                                   |
| **Minimum Duration**                    |                                                                                                            |
|                                                  |                                                                                                            |
+++
|                                      | Maximum number of notifications shown simultaneously.                                                      |
| **Maximum Number of Notifications**     |                                                                                                            |
|                                                  |                                                                                                            |
+++
|                                      | Width of the Notification Area in pixels.                                                                  |
| **Notification width**                  |                                                                                                            |
|                                                  |                                                                                                            |
+++
|                                      | If checked, open notifications will disappear when another window is activated.                            |
| **Hide when other window is activated** |                                                                                                            |
|                                                  |                                                                                                            |
+++
|                                      | If checked, notifications will not appear if the FreeCAD window is not the active window.                  |
| **Do not show when inactive**           |                                                                                                            |
|                                                  |                                                                                                            |
+++
|                                      | The maximum number of messages kept in the list. Set to 0 for no limit.                                    |
| **Maximum Messages (0 &#61; no limit)** |                                                                                                            |
|                                                  |                                                                                                            |
+++
|                                      | If checked, notifications will be removed from the message list when the **Maximum Duration** has elapsed. |
| **Auto-remove User Notifications**      |                                                                                                            |
|                                                  |                                                                                                            |
+++

### Report view 

<img alt="" src=images/Preferences_General_Page_Report_view.png  style="width:400px;">

These preferences control the behavior of the [Report view](Report_view.md). This panel can be opened using the **View → Panels → Report view** menu option.

The Report view uses the same font settings as the [Macro editor](#Editor.md).

On this page you can specify the following:


<div class="mw-translate-fuzzy">

+++
| 名称                                               | 描述                                                                                                                                                                              |
+====================================================+===================================================================================================================================================================================+
|                                     | If checked, normal messages will be recorded. They will be displayed in the [Report view](Report_view.md) with the color set in **正常的消息**. |
| **Record normal messages**             |                                                                                                                                                                                   |
|                                                 |                                                                                                                                                                                   |
+++
|                                     | If checked, log messages will be recorded. They will be displayed in the [Report view](Report_view.md) with the color set in **日志信息**.      |
| **记录日志**                           |                                                                                                                                                                                   |
|                                                 |                                                                                                                                                                                   |
+++
|                                     | If checked, warnings will be recorded. They will be displayed in the [Report view](Report_view.md) with the color set in **警告**.              |
| **记录警告**                           |                                                                                                                                                                                   |
|                                                 |                                                                                                                                                                                   |
+++
|                                     | If checked, error messages will be recorded. They will be displayed in the [Report view](Report_view.md) with the color set in **错误**.        |
| **记录错误**                           |                                                                                                                                                                                   |
|                                                 |                                                                                                                                                                                   |
+++
|                                     | If checked, the [Report view](Report_view.md) will be shown automatically when an error is recorded                                                                       |
| **错误时显示报表视图**                 |                                                                                                                                                                                   |
|                                                 |                                                                                                                                                                                   |
+++
|                                     | If checked, the [Report view](Report_view.md) will be shown automatically when a warning is recorded                                                                      |
| **在警告时显示报告视图**               |                                                                                                                                                                                   |
|                                                 |                                                                                                                                                                                   |
+++
|                                     | If checked, the [Report view](Report_view.md) will be shown automatically when a normal message is recorded                                                               |
| **Show report view on normal message** |                                                                                                                                                                                   |
|                                                 |                                                                                                                                                                                   |
+++
|                                     | If checked, the [Report view](Report_view.md) will be shown automatically when a log message is recorded                                                                  |
| **在日志消息中显示报告视图**           |                                                                                                                                                                                   |
|                                                 |                                                                                                                                                                                   |
+++
|                                     | If checked, each message and warning will receive a timecode                                                                                                                      |
| **Include a timecode for each entry**  |                                                                                                                                                                                   |
|                                                 |                                                                                                                                                                                   |
+++
|                                     | Specification of the font color for normal messages                                                                                                                               |
| **正常的消息**                         |                                                                                                                                                                                   |
|                                                 |                                                                                                                                                                                   |
+++
|                                     | Specification of the font color for log messages                                                                                                                                  |
| **日志信息**                           |                                                                                                                                                                                   |
|                                                 |                                                                                                                                                                                   |
+++
|                                     | Specification of the font color for warning messages                                                                                                                              |
| **警告**                               |                                                                                                                                                                                   |
|                                                 |                                                                                                                                                                                   |
+++
|                                     | Specification of the font color for error messages                                                                                                                                |
| **错误**                               |                                                                                                                                                                                   |
|                                                                                                                                                                         |
|                                                    | </div>                                                                                                                                                                            |
|                                                    |                                                                                                                                                                                |
|                                                    |                                                                                                                                                                         |
|                                                    | <div class="mw-translate-fuzzy">                                                                                                                                                  |
|                                                    |                                                                                                                                                                                |
+++
|                                     | If checked, internal Python output will be redirected from the [Python console](Python_console.md) to the [Report view](Report_view.md)                           |
| **将 Python 内部输出重定向到报告视图** |                                                                                                                                                                                   |
|                                                 |                                                                                                                                                                                   |
+++
|                                     | If checked, internal Python error messages will be redirected from the [Python console](Python_console.md) to the [Report view](Report_view.md)                   |
| **将 Python 内部错误重定向到报告视图** |                                                                                                                                                                                   |
|                                                 |                                                                                                                                                                                   |
+++


</div>

### Help

<img alt="" src=images/Preferences_General_Page_Help.png  style="width:400px;">

On this page you can specify the following:

+++
| Name                              | Description                                                                                                                                                                                                                     |
+===================================+=================================================================================================================================================================================================================================+
|                    | Specifies the source of the Help files. The options are:                                                                                                                                                                        |
| **Source**            |                                                                                                                                                                                                                                 |
|                                | -                                                                                                                                                                                                                |
|                                   |     **FreeCAD Wiki (online)**                                                                                                                                                                                       |
|                                   |                                                                                                                                                                                                                              |
|                                   |     :                                                                                                                                                                                                                           |
|                                   |                                                                                                                                                                                                                                 |
|                                   | -                                                                                                                                                                                                                |
|                                   |     **Markdown version (online)**                                                                                                                                                                                   |
|                                   |                                                                                                                                                                                                                              |
|                                   |     :                                                                                                                                                                                                                           |
|                                   |                                                                                                                                                                                                                                 |
|                                   | -                                                                                                                                                                                                                |
|                                   |     **GitHub (online)**                                                                                                                                                                                             |
|                                   |                                                                                                                                                                                                                              |
|                                   |     : Cannot be selected.                                                                                                                                                                                                       |
|                                   |                                                                                                                                                                                                                                 |
|                                   | -                                                                                                                                                                                                                |
|                                   |     **Custom location**                                                                                                                                                                                             |
|                                   |                                                                                                                                                                                                                              |
|                                   |     : Enter the path where the downloaded FreeCAD documentation can be found. To download the documentation select the *offline-documentation* addon from the Workbenches list in the [Addon Manager](Std_AddonMgr.md). |
|                                   |                                                                                                                                                                                                                                 |
|                                   |                                                                                                                                                                                                                  |
|                                   | **Translation suffix**                                                                                                                                                                                              |
|                                   |                                                                                                                                                                                                                              |
|                                   | : For the Wiki option and the Markdown option a [language suffix](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) can be specified. Use for example {{Value|fr}} for the French translation.               |
+++
|                    | Specifies where the documentation should be displayed. The options are:                                                                                                                                                         |
| **Display**           |                                                                                                                                                                                                                                 |
|                                | -                                                                                                                                                                                                                |
|                                   |     **In your default web browser**                                                                                                                                                                                 |
|                                   |                                                                                                                                                                                                                              |
|                                   |     : The documentation is displayed in the default web browser.                                                                                                                                                                |
|                                   |                                                                                                                                                                                                                                 |
|                                   | -                                                                                                                                                                                                                |
|                                   |     **In a FreeCAD tab**                                                                                                                                                                                            |
|                                   |                                                                                                                                                                                                                              |
|                                   |     : The documentation is displayed on a new tab in the [Main view area](Main_view_area.md). <small>(v1.0)</small> : Can no longer be used.                                                                     |
|                                   |                                                                                                                                                                                                                                 |
|                                   | -                                                                                                                                                                                                                |
|                                   |     **In a separate, embeddable, dialog**                                                                                                                                                                           |
|                                   |                                                                                                                                                                                                                              |
|                                   |     : The documentation is displayed in a separate dialog. This dialog can be docked on top of the [Combo view](Combo_view.md) for example. <small>(v1.0)</small> : Can no longer be used.                       |
+++
|                    | Specifies an optional custom stylesheet. Not used for the Wiki.                                                                                                                                                                 |
| **Custom stylesheet** |                                                                                                                                                                                                                                 |
|                                |                                                                                                                                                                                                                                 |
+++

## Display

This preferences group has six standard pages: 3D View, Light Sources, UI, Navigation, Colors and Advanced. A seventh page, Mesh view, is added if the [Mesh Workbench](Mesh_Workbench.md) has been loaded.



### 三维视图

<img alt="" src=images/Preferences_Display_Page_3D_View.png  style="width:400px;">

On this page you can specify the following:

+++
| Name                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+=======================================================+=================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
|                                        | If checked, the main coordinate system will be shown in the lower right corner of the [3D view](3D_view.md). The **Relative size** defines the size of the representation as a percentage of the view size (the minimum of its height and width). The **Letter color** defines the color of the axis letters.                                                                                                                                                                                                                       |
| **Show coordinate system in the corner**  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+++
|                                        | If checked, the axis cross will be shown by default in the [3D view](3D_view.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Show axis cross by default**            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+++
|                                        | If checked, the time needed for the last operation and the resulting [frame rate](https://en.wikipedia.org/wiki/Frame_rate) will be shown in the lower left corner of the [3D view](3D_view.md).                                                                                                                                                                                                                                                                                                                                                                                        |
| **Show counter of frames per second**     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+++
|                                        | If checked, [OpenGL](https://en.wikipedia.org/wiki/OpenGL) will use the CPU instead of the GPU. This option is useful for troubleshooting graphics card and driver problems. Changing this option requires a restart of the application.                                                                                                                                                                                                                                                                                                                                                        |
| **Use software OpenGL**                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+++
|                                        | If checked, [Vertex Buffer Objects](https://en.wikipedia.org/wiki/Vertex_Buffer_Object) (VBO) will be used. A VBO is an [OpenGL](https://en.wikipedia.org/wiki/OpenGL) feature that provides methods for uploading vertex data (position, normal vector, color, etc.) to the graphics card. VBOs offer substantial performance gains because the data resides in the graphics memory rather than the system memory and so it can be rendered directly by the GPU. For more background info see [Understanding OpenGL Objects](https://www.haroldserrano.com/blog/understanding-opengl-objects). |
| **Use OpenGL VBO (Vertex Buffer Object)** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+++
|                                        | \"Render Cache\" or \"Render Acceleration\" is explained in more detail in [FreeCAD assembly3 render-caching](https://github.com/realthunder/FreeCAD_assembly3/wiki/Link#render-caching). The options are:                                                                                                                                                                                                                                                                                                                                                                                      |
| **Render Cache**                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                    | -   **Auto**: Let Coin3D decide where to cache (default).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                       | -   **Distributed**: Manually turn on cache for all view provider root nodes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                       | -   **Centralized**: Manually turn off cache in all nodes of all view providers, and only cache at the scene graph root node. This offers the fastest rendering speed, but slower response to any scene changes.                                                                                                                                                                                                                                                                                                                                                                                |
+++
|                                        | Specifies if and what type of [multisample anti-aliasing](https://en.wikipedia.org/wiki/Multisample_anti-aliasing) is used                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Anti-Aliasing**                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+++
|                                        | Specifies the render type of transparent objects. The options are:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Transparent objects**                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                    | -   **One pass**: Rendering is done in one pass (default). This can lead to triangular artifacts. If these occur the type **Backface pass** can be used to avoid them.                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                       | -   **Backface pass**: Rendering is done in two passes. Back-facing polygons are rendered in the first pass and front-facing polygons in the second pass.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+++
|                                        | Specifies the size of [vertices](Glossary#Vertex.md) (points) in the [Sketcher Workbench](Sketcher_Workbench.md). The clickable area of points can be additionally enlarged by increasing the **Pick radius**.                                                                                                                                                                                                                                                                                                                                        |
| **Marker size**                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+++
|                                        | Specifies the eye-to-eye distance used for stereo projections. The specified value is a factor that will be multiplied with the [bounding box](Property_editor#View.md) size of the 3D object that is currently displayed.                                                                                                                                                                                                                                                                                                                                                              |
| **Eye to eye distance for stereo modes**  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+++
|                                        | If checked, backlight is enabled with the defined color. Backlight is used for rendering the back sides of faces. Usually, you don\'t see them in solids, unless you slice one with a clipping plane, or if the faces aren\'t oriented correctly. It is only used for objects whose Lighting property (on the View tab) is set to **One side**. If disabled, the back side of the faces of those objects will be black. The related **Intensity** setting specifies the intensity of the backlight.                                                                   |
| **Backlight color**                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+++
|                                        | Specifies the camera projection type. The options are:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Camera type**                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                    | -   **Perspective rendering**: Objects will appear in a [perspective projection](Std_PerspectiveCamera.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                       | -   **Orthographic rendering**: Objects will be appear in an [orthographic projection](Std_OrthographicCamera.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+++

### Light Sources 


<small>(v1.0)</small> 

<img alt="" src=images/Preferences_Display_Page_Light_Sources.png  style="width:400px;">

On this page you can specify the following:

+++
| Name                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+==============================+=================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
|               | If checked, the objects in the [3D view](3D_view.md) are lit by a directional light source and the specified color will be used for it. Without this all objects appear as solid black.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Light source** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+++
|               | Move the slider to change the intensity of the light.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Intensity**    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+++
|               | The preview shows the XY plane and a sphere, indicating the light source, connected by a line to a cone, indicating the direction. All elements in the preview, the sphere, the small cone directly attached to it, the line and the large cone, can be dragged to change the direction of the light. For more precision the direction vector can be set by specifying the **x**, **y** and **z** values or the **q0** - **q3** [quaternion](https://en.wikipedia.org/wiki/Quaternion) values. You can zoom the preview in and out with the buttons in the lower left corner. |
| **Direction**    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+++

### UI


<small>(v1.0)</small> 

<img alt="" src=images/Preferences_Display_Page_UI.png  style="width:400px;">



### 导航栏

<img alt="" src=images/Preferences_Display_Page_Navigation.png  style="width:400px;">

On this page you can specify the following:

+++
| Name                                             | Description                                                                                                                                                                                                                                                                                                                                                                                            |
+==================================================+========================================================================================================================================================================================================================================================================================================================================================================================================+
|                                   | If checked, the [Navigation cube](Navigation_Cube.md) is shown in the [3D view](3D_view.md).                                                                                                                                                                                                                                                                                           |
| **Navigation cube**                  |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                               |                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                  | **Steps by turn**                                                                                                                                                                                                                                                                                                                                                                          |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                  | defines the number of steps required for a full rotation when using the Navigation cube rotation arrows.                                                                                                                                                                                                                                                                                               |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                  | If **Rotate to nearest** is checked, the 3D view is rotated to the nearest most logical position, based on the current orientation of the cube, when a cube face is clicked. Else clicking a face will always result in the same rotation.                                                                                                                                   |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                  | **Cube size**                                                                                                                                                                                                                                                                                                                                                                              |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                  | defines the size of the cube.                                                                                                                                                                                                                                                                                                                                                                          |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                  | **Color**                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                  | sets the base color for all elements. <small>(v0.21)</small>                                                                                                                                                                                                                                                                                                                                    |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                  | **Corner**                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                  | defines where the Navigation cube is displayed in the [3D view](3D_view.md). The options are:                                                                                                                                                                                                                                                                                                  |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                  | -   **Top left**                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                  | -   **Top right**                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                  | -   **Bottom left**                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                  | -   **Bottom right**                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                  | **Font name**                                                                                                                                                                                                                                                                                                                                                                              |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                  | specifies the font used for the cube\'s texts. <small>(v0.21)</small>                                                                                                                                                                                                                                                                                                                           |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                  | **Opacity when inactive**                                                                                                                                                                                                                                                                                                                                                                  |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                  | Opacity of the Navigation cube when not hovered by the mouse. <small>(v1.0)</small>                                                                                                                                                                                                                                                                                                             |
+++
|                                   | If checked, the rotation center of the view is shown when dragging. The **Sphere size** and the **Color and transparency** of the indicator can be specified.                                                                                                                                                                                      |
| **Rotation center indicator**        |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                               |                                                                                                                                                                                                                                                                                                                                                                                                        |
| <small>(v1.0)</small>                     |                                                                                                                                                                                                                                                                                                                                                                                                        |
+++
|                                   | Specifies a [mouse navigation style](Mouse_navigation.md). To see the details of each style, select it and then press the **Mouse...** button.                                                                                                                                                                                                                            |
| **3D Navigation**                    |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                               |                                                                                                                                                                                                                                                                                                                                                                                                        |
+++
|                                   | Specifies the rotation orbit style used when in rotation mode. The options are:                                                                                                                                                                                                                                                                                                                        |
| **Orbit style**                      |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                               | -   **Turntable**: Moving the mouse will divide the rotation in steps, rotations around the different axes are performed sequentially.                                                                                                                                                                                                                                                                 |
|                                                  | -   **Trackball**: Rotations around the different axes are performed simultaneously.                                                                                                                                                                                                                                                                                                                   |
|                                                  | -   **Free Turntable**: Like **Trackball**, but if possible the rotation axis is kept collinear with the global 3D view axis. <small>(v0.21)</small>                                                                                                                                                                                                                                            |
+++
|                                   | Defines the rotation center. The options are:                                                                                                                                                                                                                                                                                                                                                          |
| **Rotation mode**                    |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                               | -   **Window center**                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                  | -   **Drag at cursor**                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                  | -   **Object center**                                                                                                                                                                                                                                                                                                                                                                                  |
+++
|                                   | Specifies the camera orientation for new documents. This setting is also used by the [Std ViewHome](Std_ViewHome.md) command.                                                                                                                                                                                                                                                                  |
| **Default camera orientation**       |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                               |                                                                                                                                                                                                                                                                                                                                                                                                        |
+++
|                                   | Affects the initial camera zoom level for new documents. The value you set is the diameter of a sphere that fits in the [3D view](3D_view.md). The default is 100 mm. It also sets the initial size of origin features (base planes in new [PartDesign Bodies](PartDesign_Body.md) and [Std Parts](Std_Part.md)).                                                              |
| **Camera zoom**                      |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                               |                                                                                                                                                                                                                                                                                                                                                                                                        |
+++
|                                   | If checked, zoom operations will be performed at the position of the mouse pointer. Otherwise zoom operations will be performed at the center of the current view. The **Zoom step** defines how much will be zoomed. A zoom step of **1** means a factor of 7.5 for every zoom step.                                                                                        |
| **Zoom at cursor**                   |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                               |                                                                                                                                                                                                                                                                                                                                                                                                        |
+++
|                                   | If checked, the direction of zoom operations will be inverted.                                                                                                                                                                                                                                                                                                                                         |
| **Invert zoom**                      |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                               |                                                                                                                                                                                                                                                                                                                                                                                                        |
+++
|                                   | If checked, and **3D Navigation** is set to **Gesture**, the tilting gesture will be disabled for pinch-zooming (two-finger zooming).                                                                                                                                                                                                                                        |
| **Disable touchscreen tilt gesture** |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                               |                                                                                                                                                                                                                                                                                                                                                                                                        |
+++
|                                   | If checked, view rotations and zooms, except those invoked by mouse actions, are animated. The **Animation duration** can be specified.                                                                                                                                                                                                                                      |
| **Animations**                       |                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                               |                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                  | **Enable spinning animations**                                                                                                                                                                                                                                                                                                                                                             |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                  | if checked, and if **3D Navigation** is set to **CAD**, rotations invoked by the mouse can be animated as well. If the mouse is moved while the scroll wheel and the right mouse button are pressed, the view is rotated. If one keeps the mouse moving while releasing the right mouse button, the rotation will continue. To end this animation left-click with the mouse. |
+++



### 颜色

<img alt="" src=images/Preferences_Display_Page_Colors.png  style="width:400px;">

On this page you can specify the following:

+++
| Name                                | Description                                                                                                                                                                                                                                                                                                                                                       |
+=====================================+===================================================================================================================================================================================================================================================================================================================================================================+
|                      | If selected, the background of the [3D view](3D_view.md) will have the specified color.                                                                                                                                                                                                                                                                   |
| **Simple color**        |                                                                                                                                                                                                                                                                                                                                                                   |
|                                  |                                                                                                                                                                                                                                                                                                                                                                   |
+++
|                      | If selected, the background of the [3D view](3D_view.md) will have a vertical color gradient defined by the specified **Top** and **Bottom** colors. if enabled, a **Middle** color can also be specified. Press the **<img src="images/Button_sort.svg" width=16px>** button (<small>(v0.21)</small> ) to switch the top and bottom colors. |
| **Linear gradient**     |                                                                                                                                                                                                                                                                                                                                                                   |
|                                  |                                                                                                                                                                                                                                                                                                                                                                   |
+++
|                      | If selected, the background of the [3D view](3D_view.md) will have a radial color gradient defined by the specified **Central** and **End** colors. if enabled, a **Midway** color can also be specified. Press the **<img src="images/Button_sort.svg" width=16px>** button to switch the central and end colors.                                  |
| **Radial gradient**     |                                                                                                                                                                                                                                                                                                                                                                   |
|                                  |                                                                                                                                                                                                                                                                                                                                                                   |
| <small>(v0.21)</small>       |                                                                                                                                                                                                                                                                                                                                                                   |
+++
|                      | Specifies the background color for objects in the tree view that are currently edited.                                                                                                                                                                                                                                                                            |
| **Object being edited** |                                                                                                                                                                                                                                                                                                                                                                   |
|                                  |                                                                                                                                                                                                                                                                                                                                                                   |
+++
|                      | Specifies the background color for active containers in the tree view. For example an [active PartDesign Body](PartDesign_Body#Active_Status.md) will get this color.                                                                                                                                                                                     |
| **Active container**    |                                                                                                                                                                                                                                                                                                                                                                   |
|                                  |                                                                                                                                                                                                                                                                                                                                                                   |
+++
|                      | The color used for the labels of the color bar. The color bar is used in the [Mesh Workbench](Mesh_Workbench.md) and [FEM Workbench](FEM_Workbench.md).                                                                                                                                                                                           |
| **Label text color**    |                                                                                                                                                                                                                                                                                                                                                                   |
|                                  |                                                                                                                                                                                                                                                                                                                                                                   |
+++
|                      | The size of those labels.                                                                                                                                                                                                                                                                                                                                         |
| **Label text size**     |                                                                                                                                                                                                                                                                                                                                                                   |
|                                  |                                                                                                                                                                                                                                                                                                                                                                   |
+++

### Advanced


<small>(v1.0)</small> 

<img alt="" src=images/Preferences_Display_Page_Advanced.png  style="width:400px;">



### 网格视图

<img alt="" src=images/Preferences_Display_Page_Mesh_view.png  style="width:400px;">

This page is only available if the [Mesh Workbench](Mesh_Workbench.md) has been loaded.

On this page you can specify the following:

+++
| Name                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                          |
+======================================================================+======================================================================================================================================================================================================================================================================================================================================================================================================================================+
|                                                       | Specifies the default face color.                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Default mesh color**                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+++
|                                                       | Specifies the default line color.                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Default line color**                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+++
|                                                       | Specifies the default mesh transparency.                                                                                                                                                                                                                                                                                                                                                                                             |
| **Mesh transparency**                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+++
|                                                       | Specifies the default line transparency.                                                                                                                                                                                                                                                                                                                                                                                             |
| **Line transparency**                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+++
|                                                       | If checked, the default value for the **Lighting** property is {{value|Two side}} instead of {{value|One side}}. {{value|Two side}} means the color of the interior side of faces is the same as the color of the exterior side. {{value|One side}} means their color is either the [backlight color](#3D_View.md), if enabled, or black. |
| **Two-side rendering**                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+++
|                                                       | If checked, the default value for the **Selection Style** property is {{value|BoundBox}} instead of {{value|Shape}}. {{value|BoundBox}} means a highlighted bounding box is displayed if meshes are highlighted or selected. {{value|Shape}} means the shape itself is then highlighted.                                                          |
| **Show bounding-box for highlighted or selected meshes** |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+++
|                                                       | If checked, [Phong shading](https://en.wikipedia.org/wiki/Phong_shading) is used, otherwise flat shading. Shading defines the appearance of surfaces. With flat shading the surface normals are not defined per vertex. This leads to an unrealistic appearance for curved surfaces. While Phong shading leads to a more realistic, smoother appearance.                                                                             |
| **Define normal per vertex**                             |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+++
|                                                       | The crease angle is a threshold angle between two faces. It can only be set if the option **Define normal per vertex** is used.                                                                                                                                                                                                                                                                            |
| **Crease angle**                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                   | :   If face angle ≥ crease angle, facet shading is used.                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      | :   If face angle \< crease angle, smooth shading is used.                                                                                                                                                                                                                                                                                                                                                                           |
+++

## Workbenches

This preferences group has a single page: Available Workbenches.

### Available Workbenches 

<img alt="" src=images/Preferences_Workbenches_Page_Available_Workbenches.png  style="width:400px;">

These preferences control workbench loading.

On this page you can specify the following:

+++
| Name                                             | Description                                                                                                                                                                                                                                                                                                                                                            |
+==================================================+========================================================================================================================================================================================================================================================================================================================================================================+
|                                   | The list displays all installed workbenches. The list can be reordered by drag and drop (<small>(v0.21)</small> ) and sorted by right-clicking the list and selecting **Sort alphabetically** (<small>(v1.0)</small> ). The order of the list also determines the order of the [Workbench selector](Std_Workbench.md). |
| **Workbench list**                   |                                                                                                                                                                                                                                                                                                                                                                        |
|                                               | -                                                                                                                                                                                                                                                                                                                                                       |
|                                                  |     <small>(v0.21)</small>                                                                                                                                                                                                                                                                                                                                                    |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                  |     : **First checkbox in each row**: If checked, the workbench will be available in the Workbench selector in the next FreeCAD session. The start up workbench cannot be unchecked. Unchecked workbenches are moved to the bottom of the list.                                                                                              |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                        |
|                                                  | -                                                                                                                                                                                                                                                                                                                                                       |
|                                                  |     **Auto-load**                                                                                                                                                                                                                                                                                                                                          |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                  |     : If checked, the workbench will auto-load when FreeCAD starts. Loading more workbenches will make the start up slower, but switching between workbenches that have already been loaded is faster.                                                                                                                                                                 |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                        |
|                                                  | -                                                                                                                                                                                                                                                                                                                                                       |
|                                                  |     **Load**                                                                                                                                                                                                                                                                                                                                                    |
|                                                  |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                  |     : Press this button to load the workbench in the current FreeCAD session.                                                                                                                                                                                                                                                                                          |
+++
|                                   | The workbench that is activated when FreeCAD starts.                                                                                                                                                                                                                                                                                                                   |
| **Start up workbench**               |                                                                                                                                                                                                                                                                                                                                                                        |
|                                               |                                                                                                                                                                                                                                                                                                                                                                        |
+++
|                                   | The options are:                                                                                                                                                                                                                                                                                                                                                       |
| **Workbench selector type**          |                                                                                                                                                                                                                                                                                                                                                                        |
|                                               | -   **ComboBox**: Workbenches can be selected from a dropdown list.                                                                                                                                                                                                                                                                                                    |
| <small>(v1.0)</small>                     | -   **TabBar**: Workbenches can be selected from a tab bar. This takes fewer clicks than the previous option, but takes up more screen space.                                                                                                                                                                                                                          |
+++
|                                   | The options are:                                                                                                                                                                                                                                                                                                                                                       |
| **Workbench selector items style**   |                                                                                                                                                                                                                                                                                                                                                                        |
|                                               | -   **Icon & Text**                                                                                                                                                                                                                                                                                                                                                    |
| <small>(v1.0)</small>                     | -   **Icon**                                                                                                                                                                                                                                                                                                                                                           |
|                                                  | -   **Text**                                                                                                                                                                                                                                                                                                                                                           |
+++
|                                   | If checked, FreeCAD will remember and restore the workbench that was active for each tab in the [Main view area](Main_view_area.md).                                                                                                                                                                                                                           |
| **Remember active workbench by tab** |                                                                                                                                                                                                                                                                                                                                                                        |
|                                               |                                                                                                                                                                                                                                                                                                                                                                        |
+++

## Python

This preferences group (<small>(v0.21)</small> ) has three pages: Macro, General and Editor.



### 宏

<img alt="" src=images/Preferences_Python_Page_Macro.png  style="width:400px;">

On this page you can specify the following:


<div class="mw-translate-fuzzy">

+++
| 名称                                       | 描述                                                                                                                                                                                                                                                                |
+============================================+=====================================================================================================================================================================================================================================================================+
|                             | If checked, variables defined by macros are created as local variables, otherwise as global Python variables                                                                                                                                                        |
| **在本地环境中运行宏**         |                                                                                                                                                                                                                                                                     |
|                                         |                                                                                                                                                                                                                                                                     |
+++
|                             | Specification of the path for macro files                                                                                                                                                                                                                           |
| **宏路径**                     |                                                                                                                                                                                                                                                                     |
|                                         |                                                                                                                                                                                                                                                                     |
+++
|                             | If checked, [recorded macros](Std_DlgMacroRecord.md) will also contain user interface commands                                                                                                                                                              |
| **录制图形用户界面命令**       |                                                                                                                                                                                                                                                                     |
|                                         |                                                                                                                                                                                                                                                                     |
+++
|                             | If checked, [recorded macros](Std_DlgMacroRecord.md) will also contain user interface commands, but as comments. This is useful if you don\'t want to execute these commands when running the macro, but do want to see what has been done while recording. |
| **录制为注释**                 |                                                                                                                                                                                                                                                                     |
|                                         |                                                                                                                                                                                                                                                                     |
+++
|                             | If checked, the commands executed by macro scripts are shown in the Python console. This console is shown using the **View → Panels → Python console** menu option.                                                                       |
| **在Python控制台显示脚本**     |                                                                                                                                                                                                                                                                     |
|                                         |                                                                                                                                                                                                                                                                     |
+++
|                             | Controls the number of recent macros to display in the menu                                                                                                                                                                                                         |
| **Size of recent macros list** |                                                                                                                                                                                                                                                                     |
|                                         |                                                                                                                                                                                                                                                                     |
+++
|                             | Controls the number of recent macros that get dynamically assigned shortcuts                                                                                                                                                                                        |
| **快捷方式计数**               |                                                                                                                                                                                                                                                                     |
|                                         |                                                                                                                                                                                                                                                                     |
+++
|                             | Controls which keyboard modifiers are used for the shortcuts, example **Ctrl+Shift+** creates shortcuts in the form of **Ctrl+Shift+1**, **Ctrl+Shift+2**, etc.                                                                                                     |
| **键盘编辑器**                 |                                                                                                                                                                                                                                                                     |
|                                         |                                                                                                                                                                                                                                                                     |
+++


</div>

### General

<img alt="" src=images/Preferences_Python_Page_General.png  style="width:400px;">

These preferences control the behavior of the [Python console](Python_console.md). This console can be opened using the **View → Panels → Python console** menu option.

Note that the color and font settings for the console are defined on the [Editor](#Editor.md) page.

On this page you can specify the following:

+++
| Name                                                          | Description                                                                                                                  |
+===============================================================+==============================================================================================================================+
|                                                | If checked, words will be wrapped if they exceed the available horizontal space in the console.                              |
| **Enable word wrap**                              |                                                                                                                              |
|                                                            |                                                                                                                              |
+++
|                                                | If checked, the cursor will have a block shape.                                                                              |
| **Enable block cursor**                           |                                                                                                                              |
|                                                            |                                                                                                                              |
+++
|                                                | If checked, Python history is saved across sessions.                                                                         |
| **Save history**                                  |                                                                                                                              |
|                                                            |                                                                                                                              |
+++
|                                                | The interval at which the profiler runs when there is Python code running (to keep the GUI responding). Set to 0 to disable. |
| **Python profiler interval (milliseconds)**       |                                                                                                                              |
|                                                            |                                                                                                                              |
| <small>(v1.0)</small>                                  |                                                                                                                              |
+++
|                                                | Used for package installation with pip and debugging with debugpy. Autodetected if needed and not specified.                 |
| **Path to external Python executable (optional)** |                                                                                                                              |
|                                                            |                                                                                                                              |
+++



### 编辑器

<img alt="" src=images/Preferences_Python_Page_Editor.png  style="width:400px;">


<div class="mw-translate-fuzzy">

编辑器首选项设置影响的是宏编辑器的行为。此编辑器可通过**Macro → Macros...  → Edit/Create**菜单打开。
**请注意:** 这里的颜色和字体设置也会影响到[Python](https://en.wikipedia.org/wiki/Python_(programming_language))控制台。此控制台可通过**View → Panels → Python console**菜单打开。


</div>

The color and font settings are also used by the [Python console](Python_console.md). The font settings are also used by the [Report view](Report_view.md).


<div class="mw-translate-fuzzy">

在*Editor*选项卡中，您可以指定以下内容：


</div>


<div class="mw-translate-fuzzy">

+++
| 名称                          | 描述                                                                                                                                                                                                                                       |
+===============================+============================================================================================================================================================================================================================================+
|                | 选择代码类型。此处的颜色与字体设置将应用于所选的代码类型。可以从**Preview**框中预览效果。                                                                                                                                                  |
| **Display Items** |                                                                                                                                                                                                                                            |
|                            |                                                                                                                                                                                                                                            |
+++
|                | 指定应用于所选代码类型的字体系列（font family）。                                                                                                                                                                                          |
| **字体族**        |                                                                                                                                                                                                                                            |
|                            |                                                                                                                                                                                                                                            |
+++
|                | 指定应用于所选代码类型的字体大小。                                                                                                                                                                                                         |
| **大小**          |                                                                                                                                                                                                                                            |
|                            |                                                                                                                                                                                                                                            |
+++
|                | 若开启此项，将显示代码行号。                                                                                                                                                                                                               |
| **启用行号**      |                                                                                                                                                                                                                                            |
|                            |                                                                                                                                                                                                                                            |
+++
|                | 指定一个tab符占多少空格位置。若将此值设置为\'6\'，则多次按下**Tab**键后，将根据当前光标位置，依次跳至其后的第7个字符、第13个字符或第19个字符等处。只有在选中**保留制表符**后，本选项才可生效。 |
| **制表符长度**    |                                                                                                                                                                                                                                            |
|                            |                                                                                                                                                                                                                                            |
+++
|                | 指定在按下**Tab**键后将会插入多少个空格。只有在选中**插入空格**后，本选项才会生效。                                                                                                            |
| **缩进大小**      |                                                                                                                                                                                                                                            |
|                            |                                                                                                                                                                                                                                            |
+++
|                | 如果选择本项，则按下**Tab**键将插入占空为**制表符长度**的tab符。                                                                                                                               |
| **保留制表符**    |                                                                                                                                                                                                                                            |
|                            |                                                                                                                                                                                                                                            |
+++
|                | 如果选择本项，则按下**Tab**键将插入数量为**缩进大小**的空格符。                                                                                                                                |
| **插入空格**      |                                                                                                                                                                                                                                            |
|                            |                                                                                                                                                                                                                                            |
+++


</div>

## Addon Manager 

This preferences group has a single page: Addon manager options.

### Addon manager options 

<img alt="" src=images/Preferences_Addon_Manager_Page_Addon_manager_options.png  style="width:400px;">

These preferences control the behavior of the [Addon manager](Std_AddonMgr.md).

On this page you can specify the following:

+++
| Name                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                 |
+=========================================================================+=============================================================================================================================================================================================================================================================================================================================================================================+
|                                                          | If checked, the Addon manager will check for updates when it is launched. Git must be installed for this to work.                                                                                                                                                                                                                                                           |
| **Automatically check for updates at start (requires git)** |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                             |
+++
|                                                          | If checked, macro metadata is downloaded for display in the Addon manager\'s main addon listing. This data is cached locally.                                                                                                                                                                                                                                               |
| **Download Macro metadata (approximately 10MB)**            |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                             |
+++
|                                                          | Controls the frequency with which the locally cached addon availability and metadata information is updated. The options are:                                                                                                                                                                                                                                               |
| **Cache update frequency**                                  |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      | -   **Manual (no automatic updates)**                                                                                                                                                                                                                                                                                                                                       |
|                                                                         | -   **Daily**                                                                                                                                                                                                                                                                                                                                                               |
|                                                                         | -   **Weekly**                                                                                                                                                                                                                                                                                                                                                              |
+++
|                                                          | If checked, addons without a license are not included in the listing.                                                                                                                                                                                                                                                                                                       |
| **Hide Addons without license**                             |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                             |
| <small>(v1.0)</small>                                            |                                                                                                                                                                                                                                                                                                                                                                             |
+++
|                                                          | If checked, addons with a Free/Libre license not published by the [Free Software Foundation](https://www.fsf.org/licensing) are not included in the listing.                                                                                                                                                                                                                |
| **Hide Addons with non-FSF Free/Libre license**             |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                             |
| <small>(v1.0)</small>                                            |                                                                                                                                                                                                                                                                                                                                                                             |
+++
|                                                          | If checked, addons with a license not approved by the [Open Source Initiative](https://opensource.org/licenses) are not included in the listing.                                                                                                                                                                                                                            |
| **Hide Addons with non-OSI-approved license**               |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                             |
| <small>(v1.0)</small>                                            |                                                                                                                                                                                                                                                                                                                                                                             |
+++
|                                                          | If checked, addons marked as \"Python 2 Only\" are not included in the listing. These addons are unlikely to work in the current FreeCAD version.                                                                                                                                                                                                                           |
| **Hide Addons marked Python 2 Only**                        |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                             |
+++
|                                                          | If checked, addons marked as \"Obsolete\" are not included in the listing.                                                                                                                                                                                                                                                                                                  |
| **Hide Addons marked Obsolete**                             |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                             |
+++
|                                                          | If checked, addons that require a newer FreeCAD version are not included in the listing.                                                                                                                                                                                                                                                                                    |
| **Hide Addons that require a newer version of FreeCAD**     |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                             |
+++
|                                                          | Custom repositories can be specified here.                                                                                                                                                                                                                                                                                                                                  |
| **Custom repositories**                                     |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      | To add a repository press the **<img src="images/List-add.svg" width=16px>** button. Both the **Repository URL** and the **Branch**, typically {{Value|master}} or {{Value|main}}, must be specifies in the dialog that opens. <small>(v0.21)</small>                          |
|                                                                         |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                         | To remove a repository select it in the list and press the **<img src="images/List-remove.svg" width=16px>** button. <small>(v0.21)</small>                                                                                                                                                                                                                    |
+++
|                                                          | The Addon manager includes experimental support for proxies requiring authentication, set up as user-defined proxies.                                                                                                                                                                                                                                                       |
| **Proxy**                                                   |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                             |
+++
|                                                          | The URL for the Addon Score data. See [Std AddonMgr](Std_AddonMgr#Sorting_by_score.md) for formatting and hosting details.                                                                                                                                                                                                                                          |
| **Score source URL**                                        |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                             |
| <small>(v1.0)</small>                                            |                                                                                                                                                                                                                                                                                                                                                                             |
+++
|                                                          | The Addon manager attempts to determine the git executable. To override this selection, the path to the executable can be set here.                                                                                                                                                                                                                                         |
| **Path to git executable (optional)**                       |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                             |
| <small>(v0.21)</small>                                           |                                                                                                                                                                                                                                                                                                                                                                             |
+++
|                                                          | If checked, the Addon manager provides an interface on the addon\'s details screen that allows switching which git branch is currently checked out. This is intended for advanced users only, as it is possible that a non-primary-branch version of an addon may result in instability and compatibility issues. Git must be installed for this to work. Use with caution. |
| **Show option to change branches (requires git)**           |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                             |
+++
|                                                          | If checked, git downloads are disabled.                                                                                                                                                                                                                                                                                                                                     |
| **Disable git (fall back to ZIP downloads only)**           |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                             |
| <small>(v0.21)</small>                                           |                                                                                                                                                                                                                                                                                                                                                                             |
+++
|                                                          | If checked, Addon manager options intended for developers of addons are activated.                                                                                                                                                                                                                                                                                          |
| **Addon developer mode**                                    |                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      |                                                                                                                                                                                                                                                                                                                                                                             |
| <small>(v0.21)</small>                                           |                                                                                                                                                                                                                                                                                                                                                                             |
+++

## Import-Export 

The Import-Export preferences affect how files are imported and exported. They are described on the [Import Export Preferences](Import_Export_Preferences.md) page.

## Measure


<small>(v1.0)</small> 

This preferences group has a single page: Appearance.

### Appearance

<img alt="" src=images/Preferences_Measure_Page_Appearance.png  style="width:400px;">

On this page you can specify the following:

+++
| Name                             | Description                                                                             |
+==================================+=========================================================================================+
|                   | Specifies the size of the text in pixels.                                               |
| **Text size**        |                                                                                         |
|                               |                                                                                         |
+++
|                   | Specifies the color of the text.                                                        |
| **Text color**       |                                                                                         |
|                               |                                                                                         |
+++
|                   | Specifies the color of the line connecting the text label with the measured element(s). |
| **Line color**       |                                                                                         |
|                               |                                                                                         |
+++
|                   | Specifies the background color of the text label.                                       |
| **Background color** |                                                                                         |
|                               |                                                                                         |
+++




<div class="mw-translate-fuzzy">

## 工作台首选项

下列为常用工作台的首选项。部分工作台并没有对应的首选项。其他可选工作台可能也未列入其中。


</div>

Preferences for the built-in workbenches are linked below. These links are also listed in [:Category:Preferences](:Category_Preferences.md). Some workbenches have no preferences.


<div class="mw-translate-fuzzy">

[Arch工作台首选项](Arch_Preferences.md)


</div>

## Scripting

See [Std DlgParameter](Std_DlgParameter#Scripting.md).

## Related

-   [Parameter editor](Std_DlgParameter.md)
-   [Fine-tuning](Fine-tuning.md)



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > Preferences Editor/zh-cn
