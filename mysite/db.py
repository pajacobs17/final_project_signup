import MySQLdb

#DB class lifted from: https://help.pythonanywhere.com/pages/ManagingDatabaseConnections
#acts as an ORM (object relation manager) whiches helps to maintain various common
#issues with connecting to a database
class DB:
    conn = None;

    def connect(self):
        self.conn = MySQLdb.connect(
        host='pajacobs.mysql.pythonanywhere-services.com',
        user='pajacobs',
        passwd='zjg26107',
        db='pajacobs$signUp');

    def query(self, sql, escaped = []):
        try:
            cursor = self.conn.cursor();
            if not escaped:
                cursor.execute(sql);
            else:
                cursor.execute(sql, escaped);
        except (AttributeError, MySQLdb.OperationalError):
            self.connect()
            cursor = self.conn.cursor();
            if not escaped:
                cursor.execute(sql);
            else:
                cursor.execute(sql, escaped);
        return cursor