from enum import Enum


class Element(int, Enum):
    PYRO = 0
    HYDRO = 1
    ANEMO = 2
    ELECTRO = 3
    DENDRO = 4
    CYRO = 5
    GEO = 6


class Region(int, Enum):
    MONDSTADT = 0
    LIYUE = 1
    INAZUMA = 2
    SUMERU = 3
    FONTAINE = 4
    NATLAN = 5
    SNEZHNAYA = 6
    KHAENRIAH = 99
    COLABO = 100


class WeaponType(int, Enum):
    SWORD = 0
    CLAYMORE = 1
    POLEARM = 2
    CATALYST = 3
    BOW = 4


class Item():
    def __init__(self, name: str, rarity: int):
        self.name = name
        self.rarity = rarity


class Weapon(Item):
    pass


class Charactor(Item):
    def __init__(self, name: str, rarity: int, weapon: WeaponType, elem: Element, region: Region) -> None:
        super().__init__(name, rarity)
        self.weapon = weapon
        self.elem = elem
        self.region = region


# 5stars
Venti =                 Charactor('ウェンティ',     5, WeaponType.BOW,      Element.ANEMO,      Region.MONDSTADT)
Klee =                  Charactor('クレー',         5, WeaponType.CATALYST, Element.PYRO,       Region.MONDSTADT)
Tartaglia =             Charactor('タルタリヤ',     5, WeaponType.BOW,      Element.HYDRO,      Region.SNEZHNAYA)
Zhongli =               Charactor('鍾離',           5, WeaponType.POLEARM,  Element.GEO,        Region.LIYUE)
Albedo =                Charactor('アルベド',       5, WeaponType.SWORD,    Element.GEO,        Region.MONDSTADT)
Ganyu =                 Charactor('甘雨',           5, WeaponType.BOW,      Element.CYRO,       Region.LIYUE)
Xiao =                  Charactor('魈',             5, WeaponType.POLEARM,  Element.ANEMO,      Region.LIYUE)
Hu_Tao =                Charactor('胡桃',           5, WeaponType.POLEARM,  Element.PYRO,       Region.LIYUE)
Eula =                  Charactor('エウルア',       5, WeaponType.CLAYMORE, Element.CYRO,       Region.MONDSTADT)
Kaedehara_Kazuha =      Charactor('楓原万葉',       5, WeaponType.SWORD,    Element.ANEMO,      Region.INAZUMA)
Kamisato_Ayaka =        Charactor('神里綾華',       5, WeaponType.SWORD,    Element.CYRO,       Region.INAZUMA)
Yoimiya =               Charactor('宵宮',           5, WeaponType.BOW,      Element.PYRO,       Region.INAZUMA)
Raiden_Shogun =         Charactor('雷電将軍',       5, WeaponType.POLEARM,  Element.ELECTRO,    Region.INAZUMA)
Sangonomiya_Kokomi =    Charactor('珊瑚宮心海',     5, WeaponType.CATALYST, Element.HYDRO,      Region.INAZUMA)
Arataki_Itto =          Charactor('荒瀧一斗',       5, WeaponType.CLAYMORE, Element.GEO,        Region.INAZUMA)
Shenhe =                Charactor('申鶴',           5, WeaponType.POLEARM,  Element.CYRO,       Region.LIYUE)
Yae_Miko =              Charactor('八重神子',       5, WeaponType.CATALYST, Element.ELECTRO,    Region.INAZUMA)
Kamisato_Ayato =        Charactor('神里綾人',       5, WeaponType.SWORD,    Element.HYDRO,      Region.INAZUMA)
Yelan =                 Charactor('夜蘭',           5, WeaponType.BOW,      Element.HYDRO,      Region.LIYUE)
Cyno =                  Charactor('セノ',           5, WeaponType.CLAYMORE, Element.ELECTRO,    Region.SUMERU)
Nilou =                 Charactor('ニイロウ',       5, WeaponType.SWORD,    Element.HYDRO,      Region.SUMERU)
Nahida =                Charactor('ナヒーダ',       5, WeaponType.CATALYST, Element.DENDRO,     Region.SUMERU)
Wanderer =              Charactor('放浪者',         5, WeaponType.CATALYST, Element.ANEMO,      Region.SUMERU)
Alhaitham =             Charactor('アルハイゼン',   5, WeaponType.SWORD,    Element.DENDRO,     Region.SUMERU)

Jean =                  Charactor('ジン',           5, WeaponType.SWORD,    Element.ANEMO,      Region.MONDSTADT)
Diluc =                 Charactor('ディルック',     5, WeaponType.CLAYMORE, Element.PYRO,       Region.MONDSTADT)
Mona =                  Charactor('モナ',           5, WeaponType.CATALYST, Element.HYDRO,      Region.MONDSTADT)
Qiqi =                  Charactor('七七',           5, WeaponType.SWORD,    Element.CYRO,       Region.LIYUE)
Keqing =                Charactor('刻晴',           5, WeaponType.SWORD,    Element.ELECTRO,    Region.LIYUE)
Aloy =                  Charactor('アーロイ',       5, WeaponType.BOW,      Element.CYRO,       Region.COLABO)
Tighnari =              Charactor('ティナリ',       5, WeaponType.BOW,      Element.DENDRO,     Region.SUMERU)

# 4starts
Fischl =                Charactor('フィッシュル',   4, WeaponType.BOW,      Element.ELECTRO,    Region.MONDSTADT)
Barbara =               Charactor('バーバラ',       4, WeaponType.CATALYST, Element.HYDRO,      Region.MONDSTADT)
Xiangling =             Charactor('香菱',           4, WeaponType.POLEARM,  Element.PYRO,       Region.LIYUE)
Xingqiu =               Charactor('行秋',           4, WeaponType.SWORD,    Element.HYDRO,      Region.LIYUE)
Sucrose =               Charactor('スクロース',     4, WeaponType.CATALYST, Element.ANEMO,      Region.MONDSTADT)
Noelle =                Charactor('ノエル',         4, WeaponType.CLAYMORE, Element.GEO,        Region.MONDSTADT)
Ningguang =             Charactor('凝光',           4, WeaponType.CATALYST, Element.GEO,        Region.LIYUE)
Diona =                 Charactor('ディオナ',       4, WeaponType.BOW,      Element.CYRO,       Region.MONDSTADT)
Beidou =                Charactor('北斗',           4, WeaponType.CLAYMORE, Element.ELECTRO,    Region.LIYUE)
Chongyun =              Charactor('重雲',           4, WeaponType.CLAYMORE, Element.CYRO,       Region.LIYUE)
Xinyan =                Charactor('辛炎',           4, WeaponType.CLAYMORE, Element.PYRO,       Region.LIYUE)
Razor =                 Charactor('レザー',         4, WeaponType.CLAYMORE, Element.ELECTRO,    Region.MONDSTADT)
Bennett =               Charactor('ベネット',       4, WeaponType.SWORD,    Element.PYRO,       Region.MONDSTADT)
Rosaria =               Charactor('ロサリア',       4, WeaponType.POLEARM,  Element.CYRO,       Region.MONDSTADT)
Yanfei =                Charactor('煙緋',           4, WeaponType.CATALYST, Element.PYRO,       Region.LIYUE)
Sayu =                  Charactor('早柚',           4, WeaponType.CLAYMORE, Element.ANEMO,      Region.INAZUMA)
Kujou_Sara =            Charactor('九条裟羅',       4, WeaponType.BOW,      Element.ELECTRO,    Region.INAZUMA)
Thoma =                 Charactor('トーマ',         4, WeaponType.POLEARM,  Element.PYRO,       Region.INAZUMA)
Gorou =                 Charactor('ゴロー',         4, WeaponType.BOW,      Element.GEO,        Region.INAZUMA)
Yun_Jin =               Charactor('雲菫',           4, WeaponType.POLEARM,  Element.GEO,        Region.LIYUE)
Kuki_Shinobu =          Charactor('久岐忍',         4, WeaponType.SWORD,    Element.ELECTRO,    Region.INAZUMA)
Shikanoin_Heizou =      Charactor('鹿野院平蔵',     4, WeaponType.CATALYST, Element.ANEMO,      Region.INAZUMA)
Collei =                Charactor('コレイ',         4, WeaponType.BOW,      Element.DENDRO,     Region.SUMERU)
Dori =                  Charactor('ドリー',         4, WeaponType.CLAYMORE, Element.ELECTRO,    Region.SUMERU)
Candace =               Charactor('キャンディス',   4, WeaponType.POLEARM,  Element.HYDRO,      Region.SUMERU)
Layla =                 Charactor('レイラ',         4, WeaponType.SWORD,    Element.CYRO,       Region.SUMERU)
Faruzan =               Charactor('ファルザン',     4, WeaponType.BOW,      Element.ANEMO,      Region.SUMERU)

Amber =                 Charactor('アンバー',       4, WeaponType.BOW,      Element.PYRO,       Region.MONDSTADT)
Kaeya =                 Charactor('ガイア',         4, WeaponType.SWORD,    Element.CYRO,       Region.MONDSTADT)
Lisa =                  Charactor('リサ',           4, WeaponType.CATALYST, Element.ELECTRO,    Region.MONDSTADT)
