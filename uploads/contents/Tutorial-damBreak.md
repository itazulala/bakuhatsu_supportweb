---
title: "はじめてのOpenFOAM並列計算: damBreak"
date: 2022-04-20
draft: false
katex: true
tags: [OpenFOAM]
categories: [Tutorials]
---

## 前提条件:
並列計算環境下(openmpiなどがインストールされている)で、OpenFOAMがインストールされて
いることを念頭に置いております。
Linux/Unixのコマンドをある程度習熟していることも念頭に置いております。

## 例題︓damBreak
ダムの決壊過程のシミュレーションを気液二層流のモデルを用いて行っているテスト問題です。
利用するOpenFOAMソルバーは、interFoamです。
気体ー液体の境界はVOF(Volume Of Fluid)法を用いて数値計算を行っております。
まずは、なにも考えずに実行してみます
(注意︓ % はシェルのプロンプトのことです。)

### 手順︓
#### 1. OpenFOAMのコマンドが実行できるようにパスを通してください。
```
% source $OpenFOAM/etc/bashrc
```
$OpenFOAMはOpenFOAMがインストールされているディレクトリです。

#### 2. ケースを実行するディレクトリに移動してください。
```
% cd $FOAM_RUN
```

#### 3. チュートリアル集のディレクトリからdamBreakをコピーしてきます。
```
% cp -r $FOAM_TUTORIALS/multiphase/interFoam/laminar/damBreak .
```

#### 4. 該当ディレクトリに行きます。
```
cd dambreak
```

#### 5. lsコマンドで、Allrun.shがあることを確認してみます。このAllrun.shが計算実行に必要なすべて
のコマンドを実行するためのシェルスクリプトです。

#### 6. 確認したら、以下のコマンドをタイプし、計算を実行してみましょう。
```
% ./Allrun.sh
```

#### 7. 可視化ツール（paraview）を使うために、空ファイル（.foamを拡張子としたファイル ）を以下
のように、touchコマンドで作ります。
```
% touch vis.foam
```
.foamという拡張子であれば、自身で適当にファイル名を決定できます。
このファイルは、Allrun.sh実行後にできているdamBreakFine上で行ってください。

#### 8. paraviewで可視化。 vis.foamを読み込みます。
paraviewを立ち上げる。
ツールバーのFile (またはフォルダのアイコン）をクリックする。
Linuxシステムをネットワークマウントしているドライブを探します(ZまたはYドライブ)。
damBreakシミュレーションを実行したディレクトリを探します(damBreakFine)。
vis.foamまたは各自で作成した.foamファイルをクリックし、読み込み
