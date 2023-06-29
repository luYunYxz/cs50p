# import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parents[1]))  # 将父级目录加入执行目录列表
# from hello2 import hello

from ..hello2 import hello


def test_argyuments():
    assert hello("david") == "hello, david"

def test_default():
    assert hello() == "hello, world"


    import sys

