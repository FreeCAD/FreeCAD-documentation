# Installing on Windows/zh-cn
<div class="mw-translate-fuzzy">

最简单的把 FreeCAD 安装到 Windows的方式是下面的安装器：


</div>


{{DownloadWindowsStable}}


<div class="mw-translate-fuzzy">

下载完 .msi (微软安装文件格式) 文件，只需要双击它以启动安装过程。


</div>


<div class="mw-translate-fuzzy">

下面是更多关于技术选项的信息。 如果它看起来很吓人，不要紧张！绝大部分 Windows 用户只需要使用 .msi 安装 FreeCAD 和 阅读 **[入门](Getting_started/zh-cn.md)**!


</div>

### 简单微软安装器安装过程

**在 Windows 上安装 FreeCAD**的最简单方式是使用上面的安装器。此节描述了**微软安装器**更多安装选项的使用和特性。

The easiest way to **install FreeCAD on Windows** is by using the downloadable installer bundle above. This page describes the usage and features of the *NSIS Installer* for more installation options.

如果你想下载一个 64 位或者不稳定的开发版本，请参考 [下载](Download/zh-cn.md) 页。

## Chocolatey

However, it is highly recommended that you use a package manager such as Chocolatey to keep your software updated. You can installed Chocolatey following [these instructions](https://chocolatey.org/install) and then open a PowerShell terminal as admin and run:


```python
choco install freecad
```

every once in a while you can update your software with


```python
choco upgrade freecad
```

to get the latest version available on Chocolatey repository. If there are any issues with the chocolatey package, you may contact maintainers on [this page](https://chocolatey.org/packages/freecad).

### 命令行安装

通过 *msiexec.exe* 命令行工具，可以获得额外的特性，例如非交互模式安装和管理员模式安装。

With the *msiexec.exe* command line utility, additional features such as non-interactive installation and administrative installation are available. See examples below.

#### 非交互模式安装

通过命令

With the command line


```python
msiexec /i FreeCAD<version>.msi
```

安装过程能够被程序化发起。额外的参数附加到这个命令行的尾部，就像


```python
msiexec /i FreeCAD-2.5.msi TARGETDIR=R:\FreeCAD25
```

#### 有限的用户交互

安装器可以通过 /q 参数控制能显示的用户界面，特别地：

The amount of user control permitted by the installer can be controlled with /q options:


<div class="mw-translate-fuzzy">

-   /qn - 无用户交互
-   /qb - 基本用户交互------只显示一个过程对话框。
-   /qb! - 像 /qb，但是隐藏撤销按钮。
-   /qr - 减少接口 - 显示所有不需要用户交互的对话框(跳过所有强制回应对话框)。
-   /qn+ - 像 /qn，但是最后显示"安装完成"对话框。
-   /qb+ - 像 /qb，但是最后显示"安装完成"对话框。


</div>

#### 安装目录

属性 TARGETDIR 决定 FreeCAD 安装的根目录。例如，可以指定不同的安装分区：

The property TARGETDIR determines the root directory of the FreeCAD installation. For example, a different installation drive can be specified with


```python
TARGETDIR=R:\FreeCAD25
```

默认 TARGETDIR 是 \[WindowsVolume\\Programm Files\\\]FreeCAD.

#### 为所有用户安装

添加参数

Adding


```python
ALLUSERS=1
```

为所有用户安装。默认非交互式安装仅当前用户，如果用户是管理员权限那么交互式安装会提供"所有用户"的选项。

#### 功能选择

FreeCAD 安装器提供了安装，重装，卸载选项：

A number of properties allow selection of features to be installed, reinstalled, or removed. The set of features for the FreeCAD installer is

-   DefaultFeature - 安装适当的软件，再加上核心库。
-   Documentation - 安装文档。
-   Source code - 安装源码
-   \... ToDo

此外，ALL 指定的所有功能。所有的特性依赖于默认功能 DefaultFeature，所以安装任何功能都会安装 DefaultFeature，下面的参数为指定重装或者卸载

-   ADDLOCAL - 指定需要安装的功能
-   REMOVE - 指定需要卸载的功能
-   ADDDEFAULT - list of features added in their default configuration (which is local for all FreeCAD features)
-   REINSTALL - 指定需要重装／修复的功能
-   ADVERTISE - 指定需要广告方式安装的功能

其他属性参见 MSDN 文档。

添加


```python
ADDLOCAL=Extensions
```

安装解释器和和仅注册扩展，但是不安装扩展(扩展使用时安装)。

### 卸载

使用

With


```python
msiexec /x FreeCAD<version>.msi
```

来卸载 FreeCAD。卸载并不需要 MSI 文件; 你可以在开始菜单中找到卸载 FreeCAD 的快捷方式。

### 管理员权限安装

使用

With


```python
msiexec /a FreeCAD<version>.msi
```

启动管理员(网络)安装。文件解压缩到一个(网络)路径，但对本地系统没有改动。另外在目标文件夹生成了一个小 msi 文件，客户机可以使用它本地安装(未来版本将提供网络启动分区共享功能)。

暂时没有管理员权限的用户交互模式卸载，所以目标路径必须要在命令行中设定。

没有为管理员权限安装的卸载方式------如果没有用户使用了，直接删除即可。

### 广告方式

使用

With


```python
msiexec /jm FreeCAD<version>.msi
```

原则上，(使用 /ju)可以把 FreeCAD "广告"到一台机器。这样 FreeCAD 的图标将显示在开始菜单中，扩展登记但未安装。当首次使用某功能时使该功能安装。

FreeCAD 安装器现在提供了"广告" 开始菜单项，还不能"广告"快捷方式。

### 自动向机群安装

使用 Windows 组策略，可以自动安装 FreeCAD 到一组机器。要做到这一点，请执行以下步骤： 登录到网域控制站

1.  把MSI文件复制到一个所有目标机器都夹授予访问权限的共享文件夹。

＃打开MMC管理单元的"Active Directory 用户和计算机" ＃浏览到需要 FreeCAD的计算机组 ＃打开属性 ＃打开"组策略" ＃添加一个新的组策略，并对其进行编辑 ＃在计算机配置/软件安装，选择"新建/包"，通过网络的路径选择MSI文件 ＃(可选)如果要有不安装 FreeCAD 的计算机，使其离开组策略范围。

With Windows Group Policy, it is possible to automatically install FreeCAD on a group of machines. To do so, perform the following steps:

1.  Log on to the domain controller
2.  Copy the MSI file into a folder that is shared with access granted to all target machines.
3.  Open the MMC snapin \"Active Directory users and computers\"
4.  Navigate to the group of computers that need FreeCAD
5.  Open Properties
6.  Open Group Policies
7.  Add a new policy, and edit it
8.  In Computer Configuration/Software Installation, choose New/Package
9.  Select the MSI file through the network path
10. Optionally, select that you want FreeCAD to be de-installed if the computer leaves the scope of the policy.

组策略传播通常需要一段时间 - 可靠地部署包后，所有机器重新启动。

### 使用 Crossover Office 把 Windows 版本的 FreeCAD 安装到 Linux 

（译者注：实际上，完全没有这样做的必要，因为有原生的 Linux 版本的 FreeCAD。）

你可以通过 \"CXOffice 5.0.1\"\" 安装 Windows 版本的 FreeCAD 到 Linux 系统。在 CXOffice 的命令行中运行 \"msiexec\" ，假设安装包已经被放置到映射盘 \"Y\" 的 \"software\" 目录下:


```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

FreeCAD 已经运行中，但它报告 OpenGL 无法正常显示，就像其它的程序运行在 _ 一样，例如 Google _.


```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

FreeCAD is running, but it has been reported that the OpenGL display does not work, like with other programs running under _ i.e. Google _.


<div class="mw-translate-fuzzy">


{{docnav|Feature list/zh-cn|Install on Unix/zh-cn}}


</div>

---
[documentation index](../README.md) > Installing on Windows/zh-cn
