# クラスの定義テンプレート
# クラスの定義
class ClassName:
    # コンストラクタ：インスタンス生成時の初期化
    def __init__(self, attribute1, attribute2):  # 必要な属性を引数として追加
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        # 必要に応じて他の属性を追加

    # メソッドの例
    def method_name(self):
        # 何かの処理
        pass

# インスタンスの作成
instance_name = ClassName(value_for_attribute1, value_for_attribute2)

# メソッドの呼び出しの例
instance_name.method_name()



# Bookというクラスを例にして、上記のテンプレートを使った入力見本
# クラスの定義
class Book:
    # コンストラクタ：インスタンス生成時の初期化
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    # 本の情報を表示するメソッド
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")

# インスタンスの作成
harry_potter = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997)
lord_of_the_rings = Book("The Lord of the Rings", "J.R.R. Tolkien", 1954)

# メソッドの呼び出し
harry_potter.display_info()
# 出力:
# Title: Harry Potter and the Sorcerer's Stone
# Author: J.K. Rowling
# Year Published: 1997

lord_of_the_rings.display_info()
# 出力:
# Title: The Lord of the Rings
# Author: J.R.R. Tolkien
# Year Published: 1954
