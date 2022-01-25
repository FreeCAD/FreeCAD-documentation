# Installing on Windows/ja
<div class="mw-translate-fuzzy">

Windows上でのFreeCADのインストールのもっとも簡単なやり方は下記のインストーラーをダウンロードすることです。


</div>


{{DownloadWindowsStable}}


<div class="mw-translate-fuzzy">

.msi (Microsoftインストーラー)ファイルをダウンロードし、それをダブルクリックするだけでインストール処理が開始します。


</div>


<div class="mw-translate-fuzzy">

以下には技術的なオプションのより詳しい情報が記載されています。よくわからなくても心配は無用です！ほとんどのWindowsユーザーはインストール用.msiで行うこと以上のことは必要ありません。**[ さあ始めましょう](Getting_started/jp.md)**！


</div>

### シンプルなMicrosoftインストーラーでのインストール

**Windows上でのFreeCADのインストール**のもっとも簡単なやり方は上記のインストーラーを使う方法です。このページでは追加のインストールオプションを使った*Microsoftインストーラー*の機能とその使い方を説明します。

The easiest way to **install FreeCAD on Windows** is by using the downloadable installer bundle above. This page describes the usage and features of the *NSIS Installer* for more installation options.

もし64ビット版や不安定開発版をダウンロードしたければ[ダウンロードページを見てください](Download.md)。

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

### コマンドラインでのインストール

*msiexec.exe*コマンドラインユーティリティーを使用すると非対話的なインストールや管理者用インストールといった追加機能を使用することができます。

With the *msiexec.exe* command line utility, additional features such as non-interactive installation and administrative installation are available. See examples below.

#### 非対話的なインストール

With the command line


```python
msiexec /i FreeCAD<version>.msi
```

以下のコマンドを使用するとインストールをプログラム的に開始させることが可能です。

追加パラメーターは以下のようにコマンドラインの末尾で設定できます。


```python
msiexec /i FreeCAD-2.5.msi TARGETDIR=R:\FreeCAD25
```

#### 制限付きユーザーインターフェイス

/qオプションを使うことでインストーラーが表示するインターフェイスの量をコントロールできます。具体的には以下の通りです：

The amount of user control permitted by the installer can be controlled with /q options:


<div class="mw-translate-fuzzy">

-   /qn - インターフェイス無し
-   /qb - 簡易インターフェイス - 小さなプログレスダイアログだけです
-   /qb! - /qbと同じですがキャンセルボタンを非表示にします
-   /qr - 省略インターフェイス - 全てのダイアログを表示しますがユーザー操作は必要とされません（モーダルダイアログは全てスキップされます）
-   /qn+ - /qnと同じですが、最後に\"Completed\"ダイアログが表示されます
-   /qb+ - /qbと同じですが、最後に\"Completed\"ダイアログが表示されます


</div>

#### ターゲットディレクトリ

TARGETDIRプロパティによってFreeCADインストール先のルートディレクトリを設定できます。例えば以下のようにすると異なるインストールドライブを指定できます。

The property TARGETDIR determines the root directory of the FreeCAD installation. For example, a different installation drive can be specified with


```python
TARGETDIR=R:\FreeCAD25
```

デフォルトのTARGETDIRは\[WindowsVolume\\Programm Files\\\]FreeCADです。

#### 全てのユーザーにインストール

Adding


```python
ALLUSERS=1
```

を追加すると全てのユーザーにインストールを行います。非対話的なインストールはデフォルトではカレントユーザーにのみパッケージをインストールします。また対話的なインストールはユーザーが必要な権限を持っている場合にデフォルトが\"all users\"のダイアログを表示します。

#### 機能の選択

複数のプロパティを使用してインストールされる機能、再インストールされる機能、削除される機能を選択することができます。FreeCADでの機能のセットは以下の通りです。

A number of properties allow selection of features to be installed, reinstalled, or removed. The set of features for the FreeCAD installer is

-   DefaultFeature - ソフトウェア一式とコアライブラリーをインストールします
-   Documentation - ドキュメントをインストールします
-   Source code - ソースコードをインストールします
-   \... ToDo

さらにALLで全ての機能を指定できます。全ての機能はDefaultFeatureに依存するのでどれか一つでも機能を自動でインストールするとはDefaultFeatureでインストールされる機能もインストールされます。以下のプロパティを使うとインストールされる機能、削除される機能をコントロールできます。

-   ADDLOCAL - ローカルマシン上にインストールされる機能のリスト
-   REMOVE - 削除する機能のリスト
-   ADDDEFAULT - デフォルト設定に追加される機能のリスト（FreeCADの全機能の一部）
-   REINSTALL - 再インストール/修復される機能のリスト
-   ADVERTISE - アド表示インストールが行われる機能のリスト

さらにいくつかのプロパティが利用可能です。詳細についてはMSDNのドキュメントを見てください。

これらのオプションに加えて


```python
ADDLOCAL=Extensions
```

を追加した場合、インタープリター自体のインストールと拡張子の登録が行われ、他には何もインストールされません。

### アンインストール

With


```python
msiexec /x FreeCAD<version>.msi
```

とするとFreeCADをアンインストールできます。パッケージまたはプロダクトコードを代わりに指定すればアンインストール用のMSIファイルは必要ありません。プロダクトコードはFreeCADがスタートメニューにインストールするアンインストール用ショートカットのプロパティで確認できます。

### 管理者用インストール

With


```python
msiexec /a FreeCAD<version>.msi
```

とすると\"管理者用\"（ネットワーク）インストールを開始できます。ファイルがターゲットディレクトリ（ネットワークディレクトリである必要があります）に展開されますがローカルマシンに対してはそれ以外の変更は行われません。また別の（小さな）msiファイルがターゲットディレクトリに生成され、クライアントはそれを使ってローカルへのインストールを行うことができます（将来的なバージョンではいくつかの機能を完全にネットワークドライブ上に置くことができるようになる予定です）。

今のところ、管理者用インストールにはユーザーインターフェイスが無いのでターゲットディレクトリはコマンドラインで渡す必要があります。

管理者用インストールには特にアンインストール手順はありません - クライアントが使用しなくなった場合はターゲットディレクトリを削除するだけで問題ありません。

### アドバタイズのインストール

With


```python
msiexec /jm FreeCAD<version>.msi
```

とするとFreeCADをマシンに\"アドバタイズ\"することができます（/juでユーザーにアドバタイズできます）。これを行うと実際にソフトウェアをインストールすることなくスタートメニューにアイコンを表示し、拡張子を登録することができます。機能の実際のインストールはその機能を初めて使用する時になって行われます。

FreeCADインストーラーでは今のところスタートメニューでのアドバタイズのみサポートし、ショートカットでのアドバタイズはサポートしていません。

### マシングループへの自動インストール

Windowsグループポリシーを使うとマシングループに自動でFreeCADをインストールすることが可能です。実行には以下のステップを行なってください。

1.  ドメインのコントローラーにログオンします
2.  全てのターゲットマシンからアクセスできる共有フォルダにMSIファイルをコピーします
3.  MMCスナップインの\"Active Directory ユーザーとコンピュータ\"をを開きます
4.  FreeCADをインストールするコンピューターグループに移動します
5.  プロパティを開きます
6.  グループポリシーを開きます
7.  新しいポリシーを追加し、編集します
8.  コンピュータの構成/ソフトウェアインストールで新規作成/パッケージを選択します
9.  ネットワークパスからMSIファイルを選択します
10. オプションでコンピューターがポリシーの範囲を外れた場合にFreeCADがアンインストールされるようにすることができます

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

グループポリシーが伝達されるまでには普通、多少の時間がかかります - 確実にパッケージを配置するには全てのマシンを再起動する必要があります。

### CrossoverOfficeを使用したLinuxへのインストール

*CXOffice 5.0.1*を使うとWindows版のFreeCADをLinuxシステム上にインストールできます。CXOfficeのコマンドラインから*msiexec*を実行してください。インストールパッケージはドライブレター\"Y:\"にマップされた\"software\"ディレクトリに配置されます：

.msi

FreeCADは実行されますがOpenGL表示が動作しないことが報告されています。これはGoogle [SketchUpなど](wikipedia_SketchUp.md)[Wine上で動作するプログラム全般に言えることです](wikipedia:Wine_(software).md)。


```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

FreeCAD is running, but it has been reported that the OpenGL display does not work, like with other programs running under [Wine](wikipedia:Wine_(software).md) i.e. Google [SketchUp](wikipedia_SketchUp.md).


<div class="mw-translate-fuzzy">


{{docnav/ja|Feature list/ja|Install on Unix/ja}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Installing on Windows/ja
