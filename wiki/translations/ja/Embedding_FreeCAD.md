# Embedding FreeCAD/ja
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

他のプログラムやスタンドアローンのPythonコンソールにFreeCADをPythonモジュールとしてインポートするための機能は驚くほど充実しています。FreeCADのモジュールとコンポーネントの全てをまとめてインポートできるのです。FreeCADのGUIをPythonモジュールとしてインポートすることさえできます・・多少の制約はありますが。


</div>


<div class="mw-translate-fuzzy">

### GUIなしでFreeCADを使用


</div>


<div class="mw-translate-fuzzy">

まずはじめに思いつく直接的で簡単で便利な応用はFreeCADドキュメントをあなたのプログラムにインポートすることです。次の例ではFreeCADドキュメントのPartジオメトリーを[blender](http://www.blender.org)にインポートしています。スクリプトはこれで全てです。このシンプルさにあなたが感動してくれるといいのですが：


</div>


{{Code|lang=python|code=
<nowiki>
FREECADPATH = '/usr/lib/freecad-python3/lib/' # path to your FreeCAD.so or FreeCAD.pyd file,
# for Windows you must either use \\ or / in the path, using a single \ is problematic
# FREECADPATH = 'C:\\FreeCAD\\bin'
import Blender, sys
sys.path.append(FREECADPATH)
 
def import_fcstd(filename):
   try:
       import FreeCAD
   except ValueError:
       Blender.Draw.PupMenu('Error%t|FreeCAD library not found. Please check the FREECADPATH variable in the import script is correct')
   else:
       scene = Blender.Scene.GetCurrent()
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()

def main():
   Blender.Window.FileSelector(import_fcstd, 'IMPORT FCSTD', 
                        Blender.sys.makename(ext='.fcstd'))    
 
# This lets you import the script without running it
if __name__=='__main__':
   main()
</nowiki>
}}


<div class="mw-translate-fuzzy">

まず重要なのはPythonがちゃんとFreeCADライブラリを見つけ出しているかの確認です。それが済めば私たちが使っているPartなどFreeCADモジュール全てを自動的に利用できるようになります。そこでまずPythonがモジュールを検索する位置を示すsys.path変数を取り、そこにFreeCADのlibのパスを追加しています。ここで行った変更は一時的なものでPythonインタプリタの終了時に消えます。これとは別にFreeCADライブラリをPythonの検索パスの一つにリンクさせることもできます。今回のスクリプトではパスを定数（FREECADPATH）に入れています。こうしておけば他のユーザーが自分のシステム用にスクリプトを調整するのが簡単になるでしょう。


</div>


{{Code|lang=python|code=
FREECADPATH = 'C:\\FreeCAD\\bin' # path to your FreeCAD.so or FreeCAD.pyd file
import sys
sys.path.append(FREECADPATH)
}}


<div class="mw-translate-fuzzy">

いったんライブラリのロード（try/except部分）が行われれば、いよいよFreeCADを使って作業を行うことができます。やり方はFreeCAD独自の内部Pythonインタプリタの時と同じです。main()関数を使って渡されたFreeCADドキュメントを開き、そのオブジェクトのリストを作成しています。それから関心のあるPartジオメトリーだけを選び出すために各オブジェクトのTypeプロパティに \"Part\"が入っているかどうか確認し、それをモザイク構造（tessellate）に変換します。


</div>


{{Code|lang=python|code=
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
}}

このモザイク構造から頂点のリストと頂点をインデックスとして定義された面のリストが作成されます。これで完璧です。何しろblenderがメッシュを定義するのと全く同じ方法なのですから。やっていることは馬鹿馬鹿しいほど単純です。ただ両方のリストの内容をblenderのmeshのvertsとfacesに追加するだけです。全て終わったら画面を再描画して終わりです！


{{Code|lang=python|code=
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()
}}


<div class="mw-translate-fuzzy">

もちろんこのスクリプトは非常に簡単なものなので（実を言うともっと応用的なものも[作ってあります](http://yorik.orgfree.com/scripts/import_freecad.py)）、あなたはこれを拡張したくなるでしょう。例えばメッシュオブジェクトのインポート、面の無いPartジオメトリーのインポート、FreeCADで読める他のファイルフォーマットのインポートといったものが考えられます。またジオメトリーをFreeCADドキュメントとしてエクスポートしたいと思うかもしれません。同じようにしてできます。あるいはダイアログを使ってユーザーが何をインポートするか選べるようにしたいと思うかも。他にもあるでしょう。実際の所、これら全てに共通して言える利点はあなたが選んだプログラムの結果出力用にFreeCADに基礎となる作業をさせることができる、ということなのです。


</div>


**Note:**

checkout [Headless FreeCAD](Headless_FreeCAD.md) for running FreeCAD without the GUI.


<div class="mw-translate-fuzzy">

### GUIありでFreeCADを使用


</div>

バージョン4.2からQtには興味深い機能が追加されました。Qt-GUI依存のプラグインを非Qtなホストアプリケーションに埋め込み、ホスト側のイベントループを共有できるようになったのです。

特にFreeCADについて言えば、これは別のアプリケーション内から全体のユーザーインターフェイスごとFreeCADをインポートでき、ホストアプリケーションがFreeCADを完全に制御できるということを意味します。

これを行うためのPythonコードは全部でたったのニ行です。


```python
import FreeCADGui 
FreeCADGui.showMainWindow()
```

もしホストアプリケーションがQtベースであればこの方法はQtがサポートされている全てのプラットフォームで動作します。ただしホスト側はFreeCADと同じバージョンのQtとリンクされている必要があります。さもないと予期しない実行時エラーが起きる可能性があります。

非Qtなアプリケーションでも知っておく必要のある制約はごくわずかです。この方法は恐らく他のツールキットと一緒に使っても動作しません。 Windowsの場合、ホストアプリケーションはWin32を直接使用しているかwxWidgets、MFC、WinFormなど内部でWin32APIを使用しているツールキットを使用していなければなりません。X11下で動作するためにはホストアプリケーションは\"glib\"ライブラリをリンクしている必要があります。

またコンソールアプリケーションではこの方法は使えないことに注意してください。なぜならイベントループ実行が存在しないからです。

## Caveats

Although it is possible to import FreeCAD to an external Python interpreter, this is not a common usage scenario and requires some care. Generally, it is better to use the Python included with FreeCAD, run FreeCAD via command line, or as a subprocess. See [Start up and Configuration](Start_up_and_Configuration.md) for more on the last two options.

Since the FreeCAD Python module is compiled from C++ (rather than being a pure Python module), it can only be imported from a compatible Python interpreter. Generally this means that the Python interpreter must be compiled with the same C compiler as was used to build FreeCAD. Information about the compiler used to build a Python interpreter (including the one built with FreeCAD) can be found as follows: 
```python
>>> import sys
>>> sys.version
'2.7.13 (default, Dec 17 2016, 23:03:43) \n[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)]'
```

## Related

-   [Headless FreeCAD](Headless_FreeCAD.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Embedding FreeCAD/ja
