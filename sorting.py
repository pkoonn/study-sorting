# coding: UTF-8

def analyze():
    readfile = "input.txt"                          # 銀河鉄道の夜が記載
    outfile = "output.txt"                          # 出力結果
    read = open(readfile,'r',encoding="UTF-8")
    data = read.readlines()                         # ファイル終端まで全て読んだデータを返す
    read.close()                                    # 入力ファイルを閉じる

    writing = open(outfile,'w',encoding="UTF-8")    # "output.txt"が無ければ新規作成=>主力、あれば上書き保存

    out = ''                                        # 1文章のデータを補完
    keep = '　'                                     # 調べている文字の1文字前がなにか補完
    for line in data:                               # 入力ファイルを1行ずつ読む
        for c in list(line):                        # 1文字ずつ読む
            if c == '」':
                out += "」\n"
                writing.write(out)
                keep = '　'
                out = ''
            elif c == '。':
                out += '。'
                keep = c
            elif keep == '。':
                out += '\n'
                writing.write(out)
                keep = c
                out = c
            elif c == '「':
                if keep == '」':
                    keep = c
                    out += c
                else:
                    out += '\n「'
                    writing.write(out)
                    out = ''
                    keep = c
            else:
                keep = c
                out += c
    # 出力ファイ+;ルを閉じる
    writing.close()
analyze()

# memo
# ファイル全てから1行ずつ読み込んでいるため、その1行の中に"。"が入っていなくても改行されてしまう
