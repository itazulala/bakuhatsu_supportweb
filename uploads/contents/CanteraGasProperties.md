---
title: "Canteraでガスの状態を確認する"
date: 2022-05-20T07:53:24+09:00
draft: false
katex: true
tags: [cantera]
categories: [Tutorials]
---

## Canteraでのガスの状態の確認

　このページでは常温常圧の水素-空気の化学量論比気体のを例としてCanteraでのガスの状態の確認方法を紹介します。

　この例では水素と酸素のモル比が２：１になるように水素と空気が混合した気体を例とします。化学反応機構データベースにはGRIMech3.0（データベースファイル名：gri30.yaml）を使用します[^1]。以下の例ではインスタンス'gas'を作成し、状態として常温常圧の水素-空気混合気体を設定します。
[^1]: http://combustion.berkeley.edu/gri-mech/version30/text30.html

 
## Pythonスクリプト例1

```python
import cantera as ct

gas = ct.Solution('gri30.yaml')

T = 298
P = 100000
X = 'H2:2 O2:1 N2:3.77'

gas.TPX = T, P, X
gas()
print('''Temperature:{0:10.2f} 
Pressure:{1:10.2f} 
Density:{2:10.5f} 
mean_molecular_weight{3:10.5f} '''
.format(gas.T, gas.P, gas.density, gas.mean_molecular_weight))
```

　`gas()` でインスタンスの状態の概要を標準出力します。そのあとの`print`関数で個別に温度、圧力、密度、平均分子量を出力します。それぞれの状態量はメンバ変数  
T：温度  
P：圧力  
density：密度  
mean\_molecular\_weight：平均分子量  
で呼び出しています。インスタンスが持つ状態にアクセスする変数は様々用意されています[^2]。プログラムの出力は次のようになります。
[^2]: https://cantera.org/documentation/docs-2.6/sphinx/html/cython/thermo.html#thermophase

```text
  gri30:

       temperature   298 K
          pressure   1e+05 Pa
           density   0.84441 kg/m^3
  mean mol. weight   20.922 kg/kmol
   phase of matter   gas

                                     1 kg              1 kmol     
                                    ---------------   ---------------
               enthalpy       -170.19          -3560.7  J
     internal energy       -1.186e+05    -2.4813e+06  J
                 entropy       8780.4           1.837e+05  J/K
     Gibbs function        -2.6167e+06  -5.4748e+07  J
 heat capacity c_p      1388.3            29046  J/K
 heat capacity c_v       990.91            20732  J/K

                      mass frac. Y      mole frac. X     chem. pot. / RT
                     ---------------   ---------------   ---------------
                H2          0.028466           0.29542            -16.95
                O2           0.22591           0.14771           -26.599
                N2           0.74563           0.55687           -23.632
     [  +50 minor]                 0                 0  

Temperature:    298.00 
Pressure: 100000.00 
Density:   0.84441 
mean_molecular_weight  20.92212
```

　`Temperature` の行以下がprint文によって出力された部分です。`gas()`で出力された温度、圧力、密度、平均分子量と一致していることが確認できます。さらにその下のエンタルピーなども出力してみましょう。各状態量を表す変数名は以下の通りです。  
h：エンタルピー  
u：内部エネルギー  
s：エントロピー  
g：ギブス自由エネルギー  
cp：定圧比熱  
cv：定容積比熱  

　Pythonスクリプトは次のようになります。
　
## Pythonスクリプト例2

```python
import cantera as ct

gas = ct.Solution('gri30.yaml')

T = 298
P = 100000
X = 'H2:2 O2:1 N2:3.77'

gas.TPX = T, P, X
gas()
print('''Enthalpy:{0:10.2f} 
Internal energy:{1:10.4e} 
Entropy:{2:10.2f} 
Gibbs function:{3:10.4e} 
Heat capacity cp:{4:10.2f} 
Heat capacity cv:{5:10.2f} '''
.format(gas.h, gas.u, gas.s, gas.g, gas.cp, gas.cv))
```
　
プログラムの出力は次のようになります。

```text
  gri30:

       temperature   298 K
          pressure   1e+05 Pa
           density   0.84441 kg/m^3
  mean mol. weight   20.922 kg/kmol
   phase of matter   gas

                          1 kg             1 kmol     
                     ---------------   ---------------
          enthalpy           -170.19           -3560.7  J
   internal energy        -1.186e+05       -2.4813e+06  J
           entropy            8780.4         1.837e+05  J/K
    Gibbs function       -2.6167e+06       -5.4748e+07  J
 heat capacity c_p            1388.3             29046  J/K
 heat capacity c_v            990.91             20732  J/K

                      mass frac. Y      mole frac. X     chem. pot. / RT
                     ---------------   ---------------   ---------------
                H2          0.028466           0.29542            -16.95
                O2           0.22591           0.14771           -26.599
                N2           0.74563           0.55687           -23.632
     [  +50 minor]                 0                 0  

Enthalpy:   -170.19 
Internal energy:-1.1860e+05 
Entropy:   8780.40 
Gibbs function-2.6167e+06 
Heat capacity cp   1388.31 
Heat capacity cv    990.91 
```
 こちらも`Enthalpy` の行以下がprint文によって出力された部分です。`gas()`で出力された「1 kgあたりの」状態量と一致していることが確認できます。このように一部の状態量はデフォルトでは1kgあたりの値で出力されます。この1kg基準の出力は`basis`という変数で変更することができます、デフォルトでは質量基準の'mass'になっていますが'molar'に変更すると1kmolあたりの状態量を出力します（**1molあたりでないことに注意！**）
 
## Pythonスクリプト例3

```python
import cantera as ct

gas = ct.Solution('gri30.yaml')

T = 298
P = 100000
X = 'H2:2 O2:1 N2:3.77'

gas.TPX = T, P, X

gas.basis='molar' # 出力単位を1kgから1kmolに変更

gas()
print('''Enthalpy:{0:10.2f} 
Internal energy:{1:10.4e} 
Entropy:{2:10.2f} 
Gibbs function:{3:10.4e} 
Heat capacity cp:{4:10.2f} 
Heat capacity cv:{5:10.2f} '''
.format(gas.h, gas.u, gas.s, gas.g, gas.cp, gas.cv))
```
　「Pythonスクリプト例2」からの変更点は`gas.basis='molar'`が入っていることだけです。これでプログラムの出力は次のように変わります。
```text
  gri30:

       temperature   298 K
          pressure   1e+05 Pa
           density   0.84441 kg/m^3
  mean mol. weight   20.922 kg/kmol
   phase of matter   gas

                          1 kg             1 kmol     
                     ---------------   ---------------
          enthalpy           -170.19           -3560.7  J
   internal energy        -1.186e+05       -2.4813e+06  J
           entropy            8780.4         1.837e+05  J/K
    Gibbs function       -2.6167e+06       -5.4748e+07  J
 heat capacity c_p            1388.3             29046  J/K
 heat capacity c_v            990.91             20732  J/K

                      mass frac. Y      mole frac. X     chem. pot. / RT
                     ---------------   ---------------   ---------------
                H2          0.028466           0.29542            -16.95
                O2           0.22591           0.14771           -26.599
                N2           0.74563           0.55687           -23.632
     [  +50 minor]                 0                 0  

Enthalpy:  -3560.73 
Internal energy:-2.4813e+06 
Entropy: 183704.64 
Gibbs function:-5.4748e+07 
Heat capacity cp:  29046.35 
Heat capacity cv:  20731.88 
```
　数値が1kgあたりのものから1kmolあたりのものに変わったことが分かります。このようにbasisによって数値が変わってしまう変数はリファレンス[^2]で  
on <span style="color: blue; ">basis</span>  
 と表記があります（図1）。例えば定圧比熱`cp`はbasisに依存しますが`cp_mass`および`cp_molar`はbasisに依存せずそれぞれ1kg、1kmolあたりの状態量が出力されます。
![basisの表示](/img/cantera_cp_basis.png "図1. Cantera公式ページのcp（定圧熱容量）に関する記述")

