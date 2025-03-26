# 数据内容
from pathlib import Path
from ds_chat_project.comm._comm_unit_ import *


class MakeAIFile(object):
    def __init__(self,title=None,content=None):
        self.__title = title
        self.__content = content

    def writeAIChatMD(self):
        # 格式化为 Markdown
        markdown_content = f"# {self.__title}\n\n{self.__content}"
        aiChatAITitleMD = str(self.__title)+'.md'
        # 构造文件路径
        file_path = Path("..") / "docs" / nowYear() / nowMonth() / nowDay() /  aiChatAITitleMD

        # 获取目录路径
        dir_path = file_path.parent

        # 如果目录不存在，则创建目录
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)

        # 写入 .md 文件
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(markdown_content)

        print(f"Markdown 文件已保存到 {file_path.resolve()}")

    def writeAIChatTXT(self):
        # 格式化为 Markdown
        markdown_content = f"# {self.__title}\n\n{self.__content}"
        aiChatAITitleTXT = str(self.__title) + '.txt'
        # 构造文件路径
        file_path = Path("..") / "docs" / nowYear() / nowMonth() / nowDay() / aiChatAITitleTXT

        # 获取目录路径
        dir_path = file_path.parent

        # 如果目录不存在，则创建目录
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)

        # 写入 .md 文件
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(markdown_content)

        print(f"Markdown 文件已保存到 {file_path.resolve()}")