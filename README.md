# blur-script

画像複数枚に対して同じくらいのサイズに拡大してぼかしをかけるためのもの  
デスクトップ壁紙のリサイズにおすすめです

極端にアスペクト比の違う画像 (16:9と9:21のようなもの) を同時に処理するとすごいことになる気がします (試していません)

## Execute

```bash
uv run blur-script
```

`img/0-preprocessed/` 内に存在する画像ファイルすべてに対して拡大縮小・ぼかし処理が適用され `img/1-postprocessed` 内に保存されます  
`img/1-postprocessed/` 内の既存ファイルは上書きされます

開発用の環境に付随するファイルも載せているので使用用途であれば `src/blur_script/__init__.py` のみで動作します  
その場合は [pillow](https://pypi.org/project/pillow/) ライブラリのインストールが必要です

```bash
pip install pillow
```

リサイズ先の画像サイズおよびぼかしの強度は `src/blur_script/__init__.py` の `main` 関数冒頭に記述がある各変数を書き換えて設定してください (気が向いたら引数で処理できるようにします)
