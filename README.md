# IPM
### 交通事故專題

## Reference
1. IPM公式&代碼參考
    * https://blog.csdn.net/monk1992/article/details/83780999
    * https://blog.csdn.net/yeyang911/article/details/51915348
    * https://sites.google.com/site/yorkyuhuang/home/research/computer-vision-augmented-reality/ipm
5. 逢圖工具AutoStitch64
    http://matthewalunbrown.com/autostitch/autostitch.html

## IPM使用
1. GetIPMImage.py
    * 主要跑程式的檔案
    * 目前需要手動調整參數的地方(需要相機參數，目前還沒能自動產生)
        * Focal Length焦距 (單位：pixel)(感覺可以先試試看跟解析度差不多的數字)
        * Camera Height相機高度
        * Pitch俯仰角
        * Yaw航向角
        * Roll橫滾角
        * left、right、top、bottom(照片中需要用來做IPM的道路範圍)
    ![](https://i.imgur.com/DtMI4rl.png)
    * OutImage目前解析度暫定640*640，若俯視圖長寬比例有錯可以將輸出的image手動調整長寬，以後希望可以轉自動。
2. GetVanishingPoint.py
    * 是用來找道路消失點(較適用於有道路盡頭的照片)，用意是可以自動找出top的位置，但目前覺得計算出來的結果不好，正在嘗試新的方法。
3. TransformImage2Ground.py
    * 是用來找出left、right、top、bottom在世界座標的相對位置
4. TransformGround2Image.py
    * 是用來找即將轉成俯視圖的各個點在原圖的哪個位置，以用來填色。
5. GetAndSetGPS.py
    * 用來將原圖的GPS座標輸入給OutImage
    * 目前先不用理他
6. Example
    * road1
    ![](https://i.imgur.com/LdMTRGC.jpg)
    ![](https://i.imgur.com/l9qXDfG.png)
    ![](https://i.imgur.com/keOZYuY.png)
    * road2 
    ![](https://i.imgur.com/v2gTZ2Q.jpg)
    ![](https://i.imgur.com/nsHP6xo.png)
    ![](https://i.imgur.com/MMzzuOz.png)
    * road3
    ![](https://i.imgur.com/5lmKS2Q.jpg)
    ![](https://i.imgur.com/PE3705Q.png)
    ![](https://i.imgur.com/fXyihaJ.png)



