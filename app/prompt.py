
from app.model import RecipeBase


def make_prompt(recipe_base: RecipeBase, day: int, days: int, policy: str):

    family_members = ", ".join(
        f"{member.age}歳の{member.gender}" for member in recipe_base.family_members)
    dislike_food = ", ".join(recipe_base.dislike_food)

    user_input = f'''
    {days}日間うちの{day}日目のレシピを提案してください。
    
    ## 考案するレシピに関する条件
    ・家族構成は、{family_members}です。年齢と性別にあった栄養バランスの良い、分量の適切なレシピを提案してください。
    ・苦手な食べ物は{dislike_food}なので、これはレシピに含めないようにしてください。
    ・他の日とのレシピ被りはあまりないようにしてください。
    ・レシピのポリシーとしては{policy}に従ったレシピを提案してください。
    
    ## レシピ




    ## 主食・主菜・副菜の定義
    主食は、食事の基盤となるエネルギー源です。主に炭水化物を多く含み、米、パン、麺類などがこれに当たります。日本の伝統的な食事では、ご飯が主食の典型的な例です。
    具体例： ご飯、パン、うどん、そば、パスタ
    
    主菜は、食事におけるたんぱく質の主要な供給源です。肉、魚、卵、大豆製品などが含まれ、これらを使った料理が主菜に該当します。主菜は、栄養バランスを考える上で重要な役割を持ち、食事の中心となる料理です。
    具体例： 魚の塩焼き、肉の照り焼き、豆腐の味噌汁、卵焼き
    
    副菜は、ビタミンやミネラル、食物繊維を補うための料理で、野菜や海藻、きのこなどを主材料としています。色々な種類の副菜を取り入れることで、栄養バランスが向上します。副菜は、主食や主菜と合わせて食事のバリエーションや彩りを豊かにします。
    具体例： 野菜のサラダ、ひじきの煮物、きのこの炒め物、浅漬け
    
    
    ## レシピの作り方についての表示形式
    1. 玉ねぎ、にんじん、セロリをみじん切りにします。野菜のサイズは均一にすることで、調理時に均等に火が通ります。\n
    2. フライパンにオリーブオイルを中火で熱し、みじん切りにした野菜を加え、透明になるまで炒めます。この時、塩少々を振り、野菜から水分を引き出しやすくします。\n
    3. 野菜が透明になったら、ひき肉を加え、色が変わり、パリッとするまで中火で炒めます。ひき肉がダマにならないように、木べらなどでしっかりとほぐしながら炒めます。\n
    4. ホールトマト、赤ワイン、牛乳を加えます。ホールトマトは手で粗くつぶしながら加えると、ソースに深みが出ます。塩、黒こしょうで味を調え、弱火で30分から1時間程度、時々かき混ぜながら煮込みます。ソースが煮詰まってきたら、味を見て、必要に応じて調味料を調整します。\n
    5. ソースが煮込んでいる間に、大きな鍋でたっぷりの湯を沸かし、塩を加えてパスタを茹でます。パスタの茹で時間はパッケージの指示に従いますが、アルデンテ（少し固め）に茹でるのがおすすめです。\n
    6. パスタが茹で上がったら、水を切り、煮込んだソースとよく絡めます。この時、ソースがパスタによく絡むように、少しのパスタの茹で汁を加えると良いでしょう。\n
    7. 皿に盛り付けた後、お好みでパルメザンチーズをたっぷりと振りかけます。\n

    上記のように、詳しく工程を書くようにしてください。
 
    ## 必要な食材の分量についての表示形式
    以下のように指定してください。
    Step1 - 食材名を表示
    Step2 - 食材名の後ろに半角スペース1つ分空ける
    Step3 - 食材の必要な分量を表示
    Step4 - レシピとレシピの間に「,」を入れる
    
    具体的な表示例
    ブロッコリー 2個,鶏胸肉 300g, そば 200g

    '''

    return user_input


system_prompt = f'''
あなたは管理栄養士です。
バランスの取れた食事プランを考案し、提供することができます。



'''





json_schema = {
    "type": "object",
    "properties": {
        "morning": {
            "type": "object",
            "properties": {
                "staple_food": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "主食のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "主食のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "main_dish": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "主菜のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "主菜のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "side_dish": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "副菜のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "副菜のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "ingredients": {"type": "string"}
            },
            "required": ["staple_food", "main_dish", "side_dish", "ingredients"]
        },
        "lunch": {
            "type": "object",
            "properties": {
                "staple_food": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "主食のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "主食のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "main_dish": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "主菜のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "主菜のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "side_dish": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "副菜のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "副菜のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "ingredients": {"type": "string"}
            },
            "required": ["staple_food", "main_dish", "side_dish", "ingredients"]
        },
        "dinner": {
            "type": "object",
            "properties": {
                "staple_food": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "主食のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "主食のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "main_dish": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "主菜のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "主菜のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "side_dish": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "副菜のレシピ名を入力してください"
                        },
                        "how_to_cook": {
                            "type": "string",
                            "description": "副菜のレシピの作り方を細かく入力してください。"
                        }
                    },
                    "required": ["name", "how_to_cook"]
                },
                "ingredients": {"type": "string"}
            },
            "required": ["staple_food", "main_dish", "side_dish", "ingredients"]
        }
    },
    "required": ["morning", "lunch", "dinner"]
}
