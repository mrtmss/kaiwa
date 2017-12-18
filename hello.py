import MeCab

print('村田不動産:村田不動産です。質問を入力してください。終わりたいときは、「終了」と入力してください。')
num1=0
while num1==0:
    text1=input("顧客:")
    if text1=='こんにちは' or text1=='やあ':
        print('村田不動産:こんにちは')
        continue
    text3=[]
    for text2 in MeCab.Tagger().parse(text1).splitlines()[:-1]:
          (w1,h1) = text2.split('\t')
          if h1.startswith('名詞'):
             text3.append(w1)
    s="".join(text3)
    if s=='村田AA10-1号室':
        print("村田不動産:空いています。家賃は7万円です。")
    elif  s=='終了' or s=='end':
        num1=1
    else:
        print("村田不動産:空いていません。")
