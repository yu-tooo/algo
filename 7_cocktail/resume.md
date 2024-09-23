# Cocktail Sortとは
1. Bubbleソートのように前から順に入れ替えを行う。右端には一番大きい数が右端に来る。
2. limitを左にずらし、後から入れ替えを行う。左端には一番小さな数が左端に来る
3. 1,2を繰り返しながら、一度も入れ替えが行われなくなったタイミングで終了する

# 練習手順
1. Cocktail Sortを実装する

# ヒント
- for i in range(start, end)とすると、start以上、end未満（endまではいかないので注意）までループする
- for i in range(end, start, -1)とすると、end以上、start未満までループする