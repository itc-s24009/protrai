import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy
#画像を数値リストに変換
def imageToData(filename):
    #画像を8x8のグレースケールに変更
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8,8),PIL.Image.Resampling.LANCZOS)
    #数値リストに変換
    numImage = numpy.asarray(grayImage,dtype = float)
    numImage = 16 - numpy.floor(17 * numImage / 256)
    numImage = numImage. flatten()

    print(numImage)
    return numImage
#数字を予想する
def predictDigits(data):
    #データを読み込む
    digits = sklearn.datasets.load_digits()
    #機械学習
    clf = sklearn.svm.SVC(gamma = 0.001)
    clf.fit(digits.data,digits.target)
    n = clf.predict([data])
    #予想結果を表示する
    print("予測=",n)

data = imageToData("tmp/2.png")
predictDigits(data)
