# てもて言語

## 概要
有り余る深夜テンションで開発したネタ言語です。  
brainf*ckを元にしています。

## 使い方
interpreter.pyのコマンドライン引数に.temファイルを指定して実行してください。  
bf_to_temote.pyの第一引数に.temファイル、第二引数にbrainf\*ckのコードを直接渡すことでbrainf\*ckからこの言語に変換できます。  

## てもて言語の仕様
brainf*ckの命令に一対一対応しています。  
### 命令一覧
| 命令     | 実行される内容                                                  | 
| -------- | --------------------------------------------------------------- | 
| てもて   | ポインタをインクリメント                                        | 
| てもてっ | ポインタをデクリメント                                          | 
| てもて〜 | ポインタの値をインクリメント                                    | 
| てもてー | ポインタの値をデクリメント                                      | 
| てもて！ | ポインタの値を出力                                              | 
| てもて？ | 入力から1バイト読み込んでポインタが指す値に代入                 | 
| あっぷっ | ポインタが指す値が0なら、あとの「ぷぇ！」までジャンプする       | 
| ぷぇ！   | ポインタが指す値が0でなければ、前の「あっぷっ」までジャンプする | 

## 参考にさせていただいたサイト様
https://emoson.hateblo.jp/entry/2014/10/14/193825
