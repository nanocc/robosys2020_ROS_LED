# 2020年度 ロボットシステム学 課題2

## 内容
端末またはweb上から特定のコマンドを入力することで，LEDが点灯または消灯する  
- 入力したコマンドはその説明文と共にweb上で確認可能  
- 使用可能なコマンドは'0'～'9'，'a'～'f'，'l'，'p'  
- 実験器具や配線などについての詳細はこちらを参照 https://github.com/nanocc/robosys2020_LED (課題1)  

## 動作環境
- Raspberry Pi 4 Model B  
- Ubuntu 20.04  
- ROS noetic  

## 実行方法

- パッケージのインストール
```
$ sudo apt install ros-noetic-rosbridge-suite
```

- 以下のコマンドを順に実行
```
$ git clone https://github.com/nanocc/robosys2020_LED.git
$ cd robosys2020_LED
$ make
$ sudo insmod myled.ko
$ sudo chmod 666 /dev/myled0
$ cd ..
$ git clone https://github.com/nanocc/robosys2020_ROS.git
$ cd robosys2020_ROS
$ roslaunch mypkg mypkg.launch
```

## 操作方法

- roslaunchを実行した端末からコマンドを入力
<img src="./images/terminal.png" width="300">

- http:// [Raspberry Pi のIPアドレス] :8000/pub.html にアクセスしコマンドを入力，sendボタンをクリック
<img src="./images/pub.png" width= "300">

- http:// [Raspberry Pi のIPアドレス] :8000/sub.html にアクセスしコマンドとその説明文を確認
<img src="./images/sub.png" width="300">

## アンインストール

- 以下のコマンドを実行
```
$ sudo rmmod myled
$ make clean
```

## デモムービー
https://www.youtube.com/watch?v=CtdgQqRCb1Y

## 参考資料
- HTML，Javascriptの記述を参考にさせて頂きました [https://github.com/ryuichiueda/robosys2019/blob/master/md/13_ros.md]

## ライセンス
[GNU General Public License v3.0](https://github.com/nanocc/robosys2020_ROS/blob/main/COPYING)
