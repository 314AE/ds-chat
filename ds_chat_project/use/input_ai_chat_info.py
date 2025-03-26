# 输入ai chat 问题内容
from ds_chat_project.ai_make_chat._ai_chat_make_file_ import MakeAIFile
from ds_chat_project.ai_make_chat._make_ai_chat_ import MakeAIChat
from ds_chat_project.comm._comm_unit_ import nowFormattedDate, nowFormattedTime
from ds_chat_project.entity.ai_chat_info import AIChatInfo
from ds_chat_project.sqlite_conn._sqlite_conn_ import SqliteConn

def aiProblemInfo():
    print('输入问题内容：')
    problemInfo: str = input('')

    # sqlite3连接
    sqlConn = SqliteConn('..\\db\\chat_record.db')

    resCreateTime = nowFormattedDate()
    resId = nowFormattedTime()
    # ai chat
    # ai chat create
    makeAIChat = MakeAIChat(problemInfo)
    AIChatResContent = makeAIChat.createAIChat()
    print(AIChatResContent)

    # save ai chat sqlite3
    aiChatInfo = AIChatInfo(resId, str(problemInfo), str(AIChatResContent), resCreateTime)

    # 保存ai chat info
    sqlConn._insert_ai_chat_info_table_(aiChatInfo)
    aiChatListRecord = sqlConn._get_ai_chat_info_table_()
    print(aiChatListRecord)

    # 保存 ai chat info 文件
    makeAIChat = MakeAIFile(problemInfo, AIChatResContent)
    makeAIChat.writeAIChatMD()
    makeAIChat.writeAIChatTXT()
