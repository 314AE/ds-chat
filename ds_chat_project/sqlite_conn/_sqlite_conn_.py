import sqlite3


class SqliteConn(object):

    def __init__(self, connPath):
        self.__connPath = connPath
        print(self.__connPath)
        self.__sqliteConn = sqlite3.connect(self.__connPath)
        self.__cursor = self.__sqliteConn.cursor()
        print('数据库连接成功！')

    def _insert_response_res_table_(self, res_record):
        try:
            self.__cursor.execute(
                'INSERT INTO res_record (id, status_code, headers, res_text, create_time) VALUES (?, ?, ?, ?, ?)',
                (res_record.getId(), res_record.getStatusCode(), res_record.getHeaders(), res_record.getRes_text(), res_record.getCreateTime())
            )
            self.__sqliteConn.commit()
            print("数据插入成功")
        except sqlite3.Error as e:
            print(f"插入数据时发生错误: {e}")

    def _get_res_table_(self):
        try:
            self.__cursor.execute('select * from res_record')
            self.__sqliteConn.commit()
            return self.__cursor.fetchall()
        except ValueError as ve:
            print(ve, '读取res_record表的记录')

    def _insert_ai_chat_info_table_(self, aiChatInfoRecord):
        try:
            self.__cursor.execute(
                'INSERT INTO ai_chat_info (id, problem_info, res_info, create_time) VALUES (?, ?, ?, ?)',
                (aiChatInfoRecord.getId(), aiChatInfoRecord.getProblemInfo(),  aiChatInfoRecord.getResInfo(), aiChatInfoRecord.getCreateTime())
            )
            self.__sqliteConn.commit()
            print("数据插入成功")
        except sqlite3.Error as e:
            print(f"插入数据时发生错误: {e}")

    def _get_ai_chat_info_table_(self):
        try:
            self.__cursor.execute('select * from ai_chat_info')
            self.__sqliteConn.commit()
            return self.__cursor.fetchall()
        except ValueError as ve:
            print(ve, '读取res_record表的记录')

    def close(self):
        self.__sqliteConn.close()
        self.__cursor.close()
        print("数据库连接已关闭")