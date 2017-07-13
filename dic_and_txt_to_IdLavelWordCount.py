# coding: UTF-8
from collections import OrderedDict                     # 辞書型の代入順序を維持するためのライブラリ

read_features = "features.txt"
read_label = "output_w_label.txt"
dic = "dic.txt"
outfile = "word_matrix.txt"                             # 出力結果
read_features = open(read_features,'r',encoding="UTF-8")
read_label = open(read_label,'r',encoding="UTF-8")
read_dic = open(dic,'r',encoding="UTF-8")
f_data = read_features.readlines()                      # ファイル終端まで全て読んだデータを返す
l_data = read_label.readlines()
d_data = read_dic.readlines()
read_features.close()                                   # 入力ファイルを閉じる
read_label.close()                                      # 入力ファイルを閉じる
read_dic.close()                                        # 入力ファイルを閉じる

line = len(open('dic.txt').readlines())                 # dic.txtの総行数
dic_Allword_list = [[0 for i in range(3)] for j in range(line)]                    # 1つの要素にdic_word_listが入ってるlist

row_1_list = [[]]                                       # 1行の単語をlistに格納
dic_hash = OrderedDict()                                # {'ジョパンニ':1,'人':2}



def dic():
    dic_word_list = []                          # 1単語分の情報 list[0]:単語のID、list[1]:単語の出現回数、list[2]:単語
    line = len(open('dic.txt').readlines())     # dic.txtの総行数
    dic_row = []                                # dic.txtの1行毎list
    # dic_Allword_list = [[id1,cnt,word1],[id2,cnt,word2],[],[]....]

    for dic_word in d_data:
        dic_row.append(dic_word)

    for element in range(0,line):
        dic_word_list = dic_row[element].split(' ')                     # dic_word_list=[id,cnt,word]
        for cnt in range(0,3):
            dic_Allword_list[element][cnt] = dic_word_list[cnt]

    cnt = 1                                                             # dicのIDが1から振られているから1

dic()
def access_word(word):                                                  # wordが入っているdicの単語idを返す
    for l in range(0,line):
        try:
            dic_Allword_list[l].index(word)
            return l    # 上の行でwordが見つからない場合はこのprint文は実行されない
        except ValueError:
            continue

def lavel():
    lavel_num = 7                               # lavelの数
    out = ""
    row_pre = []                                # 出力の1行文をlistに格納
    row = []
    for lavel_line in l_data:                   # ID+lavelをrow_listに格納
        for c in lavel_line:
            if c.isdigit():
                out += c
            elif c == ' ':
                out += c
        row_pre.append(out)
        out = ""
    cnt = 0
    for features_line in f_data:
        for c in features_line:
            if not c.isdigit():
                out += c
        row.append(row_pre[cnt]+out)
        out = ""
        cnt += 1
    out_list = [[]]
    cnt = 0
    id_row1_list = [[]]
    out = ""
    for row_sentence in row:
        num_flag = 0
        row_1_list.append(row_sentence.split(' '))
        cnt += 1

    cnt = 1
    for word in dic_Allword_list:                                       # 辞書を作成{'ジョパンニ':1,'云う':2}
        dic_hash[word[2].strip("\n")] = cnt
        cnt += 1

    cnt = 0
    id_row1_list = row_1_list
    for word_list in row_1_list:
        for j in range(0,len(word_list)):
            word_list[j].strip("\n")                                 # 引数があれば、その文字列を削除
        for i in range(9,len(word_list)):
            if word_list[i] in dic_hash:
                id_row1_list[cnt][i] = dic_hash[word_list[i]]
            # else:
            #     print(word_list[i])
        cnt += 1
    print(id_row1_list)
lavel()
