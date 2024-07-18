from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllCromosomi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct Chromosome c
                    from genes g
                    where Chromosome <> 0"""

        cursor.execute(query, ())

        for row in cursor:
            result.append(row['c'])

        cursor.close()
        conn.close()
        return result



