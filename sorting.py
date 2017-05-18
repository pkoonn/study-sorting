# coding: UTF-8
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
    keep = ' '                                      # 調べている文字の1文字前がなにか補完
    color_list = {'青':0,'黄':0,'赤':0,'緑':0}       # 感情の色
    writing.write('id ')
    for color in color_list.keys():
        writing.write(color+' ')
    writing.write('\n')
    for line in data:                               # 入力ファイルを1行ずつ読む
        for c in list(line):                        # 1文字ずつ読む
            if c == '」':
                if keep == '。':
                    id = str(count)
                    out += '」\n'
                    writing.write(out)
                    count += 1
                    out = id.zfill(digit)+'\t0 0 0 0 '
                    keep = c
                elif keep == '、' or keep == '…':
                    id = str(count)
                    out += '」\n'+id.zfill(digit)+'\t0 0 0 0 '
                    count += 1
                    keep = c
                else:
                    if out[-1] != ' ':
                        id = str(count)
                        out += '」\n'+id.zfill(digit)+'\t0 0 0 0 '
                        count += 1
                    keep = c
            elif c == '。':
                out += '。'
                keep = c
            elif keep == '。':
                out += '\n'
                writing.write(out)
                id = str(count)
                out = id.zfill(digit)+'\t0 0 0 0 '+c
                count += 1
                keep = c
            elif c == '「':
                if keep != '」':
                    out += '\n'
                    if out == '':
                        out += id.zfill(digit)+'\t0 0 0 0 '
                    else:
                        out += id.zfill(digit)+'\t0 0 0 0 '
                    writing.write(out)
                    count += 1
                    id = str(count)
                    out = c
                else:
                    out += c
                keep = '「'
            else:
                keep = c
                out += c
    writing.close()                              # 出力ファイルを閉じる
analyze()
