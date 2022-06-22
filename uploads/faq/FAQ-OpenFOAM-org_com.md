---
title: "2種類の OpenFOAM"
date: 2022-04-19T09:20:20+09:00
draft: false
katex: true
tags: [OpenFOAM]
categories: [FAQ]
css: "style.css"
---

## Q. なぜ、OpenFOAMには2種類（Foundation版とESI版)のバージョンがあるのですか︖

## A. OpenFOAMの開発の歴史的な背景によるものです。以下で詳しく説明します。
OpenFOAMは、英国のImperical Colleage LondonのHenry Weller博士によって1980年代から開発が始
まりました。
始めは、FOAM(Field Operation And Manupulation)という商用コードであったのですが、2004年にな
り、商用コードからオープンソース化が図られ、現在のOpenFOAM(Open-source Field Operation
And Manupulation)という名前になります(OpenCFD社がGnu Public License(GPL)のもとで、オープ
ンソースとして配布を始める)。
2011年にSGI(Silicon Graphics International)社とOpenCFD社の間で、OpenFOAM Foundationが創設
されました(SGI社がOpenCFD社を買収する)。その後、OpenFOAM Foundationがバージョン管理と
アップデートを行っておりました。その間に、OpenCFD社が、ESI(Engineering System
International)社に買収されております。2015年に、OpenFOAM foundationとESI社との間で、ライセ
ンス契約上の問題が発生し(the CEO of ESI did not sign the Agreement, without explanation)、その結
果として、ESI版とFoundation版が別々にバージョンをリリースすることになりました。Foundation
版は、バージョン番号をそのまま引継ぎ、現在のOpenFOAM-9になっております。一方で、ESI版
は、リリースの年月をバージョン番号につけております（現在は、v2112）。OpenFOAM foundation
の活動基盤は英国にあるのに対し、ESI社の活動基盤は米国です。
二つのバージョンにおいて、基本的な機能、使い勝手、プログラムの構造などはほとんど変わりませ
んが、 ESI版の方が、チュートリアルプログラムがより充実しております。Foudationバージョンは、
重なり格子点(オーバーセットメッシュ)の取り扱いがESIバージョンよりも優れている違いがありま
す。
