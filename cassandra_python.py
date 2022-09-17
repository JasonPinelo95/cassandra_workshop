from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra import ConsistencyLevel

if __name__ == "__main__":
    cluster = Cluster(['172.23.0.2'],port=9042)
    #session = cluster.connect('store',wait_for_all_pools=True)
    #session.execute('USE store')
    #rows = session.execute('SELECT * FROM shopping_cart')
    #for row in rows:
    #    print(row)

    session = cluster.connect()

    # Create a keyspace
    session.execute("CREATE KEYSPACE IF NOT EXISTS university WITH REPLICATION \
            = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };")

	 # Create table
    session.execute("CREATE TABLE IF NOT EXISTS university.students (\
            studentid text PRIMARY KEY,\
            name text,\
            last_name text,\
            program text,\
            semester int\
            );")

    # Insert data
    query = SimpleStatement("INSERT INTO university.students\
            (studentid, name, last_name, program, semester)\
            VALUES\
            (%s, %s, %s, %s, %s)", consistency_level = ConsistencyLevel.QUORUM)

    session.execute(query, ('1', 'Jason', 'Pinelo', 'Data Engineering', 9))
    session.execute(query, ('2', 'Adrian', 'Carmona', 'Data Engineering', 9))
    session.execute(query, ('3', 'Emmanuel', 'Hurtado', 'Data Engineering', 9))
    session.execute(query, ('4', 'Pedro', 'Uicab', 'Data Engineering', 9))
    session.execute(query, ('5', 'Karla', 'Valdez', 'Data Engineering', 9))


    #session.execute("SELECT * FROM university.students;")
