# Sorting
卒業研究（自然言語処理）で利用するプログラムです。

# Overview
input.txtに記述している文章をsorting.pyで整理して1行に1文章されたデータがoutput.txtに出力されます。
今回、input.txtには青空文庫の銀河鉄道の夜を記載しています。
あまり大きなデータでなければinput.txtに好きな文書を使用してみて下さい。

## 実行環境
- Python 3.5.2
- MacOS バージョン　10.12.3

# Installation

## 1.python3をインストール

### Windowsの場合
1. [公式](https://www.python.org/)からインストーラーをダウンロード
2. 順序に従ってダウンロード
3. バージョン確認
```
> python --version
```
バージョンが表示されるとインストール完了です。

### MacOSの場合
1. pyenvのインストール

macにはデフォルトでpython2がインストールされている。

pythonのバージョン切り替えを管理するために、まずpyenvをHomeBrewでインストール。

```
$ brew install pyenv
```

2. パスの設定

```
$ export PYENV_ROOT="$HOME/.pyenv"
$ export PATH="$PYENV_ROOT/bin:$PATH"
$ eval "$(pyenv init -)"
```
3. Pythonのインストール

インストールしたpyenvでインストールバージョンを確認。

```
$ pyenv install --list
```
好きなバージョンをインストール。

```
$ pyenv install 3.5.0
```
インストールしたバージョンの確認。

```
$ pyenv versions
* system (set by /Users/[ユーザ名]/.pyenv/version)
  3.5.2
```

4. 入力バージョンを3.5.2に切り替える。

```
$ pyenv global 3.5.2
$ pyenv rehash
```

5. 切り替わっているか確認してみる。
```
$ pyenv versions
  system
* 3.5.2 (set by /Users/[ユーザ名]/.pyenv/version)
$ python --version
python 3.5.2
```
これで完了。

## git clone

githubからローカルにダウンロード
```
$ git clone https://github.com/pkoonn/study-sorting.git
```

# Usage

```
> python3 sorting.py
```
