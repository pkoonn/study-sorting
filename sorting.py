# coding: UTF-8
# import string                                       # 特定のグループの文字列をまとめて取得
def analyze():
    readfile = "input.txt"                          # 銀河鉄道の夜が記載
    outfile = "output.txt"                          # 出力結果
    read = open(readfile,'r',encoding="UTF-8")
    data = read.readlines()                         # ファイル終端まで全て読んだデータを返す
    read.close()                                    # 入力ファイルを閉じる

    writing = open(outfile,'w',encoding="UTF-8")    # "output.txt"が無ければ新規作成=>主力、あれば上書き保存

    id = ''                                         # 1文章に最大7桁のidを付けるための初期値
    count = 0                                       # idの管理
    digit = 7                                       # idの桁数

    out = ''                                        # 1文章のデータを補完
    keep = '　'                                     # 調べている文字の1文字前がなにか補完
    for line in data:                               # 入力ファイルを1行ずつ読む
        for c in list(line):                        # 1文字ずつ読む
            if c == '」':
                if keep == '。':
                    id = str(count)
                    out += "」"
                    # out += '」\n'+id.zfill(digit)
                elif '、' and '…':
                    id = str(count)
                    out += '」\n'+id.zfill(digit)
                    count += 1
                else:
                    if out[-1].isdigit() == True:
                        id = str(count)
                        out += keep+'」'
                    else:
                        out += id.zfill(digit)+keep+'」\n'
                        count += 1
                    keep = c
            elif c == '。':
                out += '。'
                keep = c
            elif keep == '。':
                out += '\n'
                writing.write(out)
                id = str(count)
                out = id.zfill(digit)+'\t'+c
                count += 1
                keep = c
            elif c == '「':
                if keep == '」':
                    id = str(count)
                    # if out[-1].isalnum() == True:
                    out += '\n'+id.zfill(digit)+'\t「'
                    writing.write(out)
                    out = ''
                    count += 1
                else:
                    out += '\n'
                    writing.write(out)
                    id = str(count)
                    out = id.zfill(digit)+'\t「'
                    count += 1
                keep = '「'
            else:
                keep = c
                out += c
    # 出力ファイルを閉じる
    writing.close()
analyze()
