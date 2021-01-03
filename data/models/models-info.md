# modelsフォルダ　Infomation

modelsフォルダには学習モデルを配置し、ipynbファイルと別にすることでmodelの使い回しを考慮する。

- input

    入力情報として扱うのはpandas.DataFrame,paramや、DLの場合はtensor化されたものを扱う。画像などはtransformしたものを扱う。

- output
  
    出力結果として扱うのは予測結果である。argmaxに変換するべきか、one-hot-labelにしたものを出力するのかは検討中
