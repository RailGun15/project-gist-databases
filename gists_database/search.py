from .models import Gist
from datetime import *

def search_gists(db_connection, **kwargs):
    list_gists = []
    if kwargs == {}:
        cursor = db_connection.execute("""SELECT * FROM gists;""")
        for row in cursor:
            gist = Gist(row)
            list_gists.append(gist)
        return list_gists
    else:
        search = [(key,val) for (key,val) in kwargs.items()]
        for arg in search:
            if isinstance(arg[1], datetime):
                cursor = db_connection.execute("SELECT * FROM gists WHERE datetime(created_at) == datetime(:created_at);",(arg[1],))
            else: 
                cursor = db_connection.execute("SELECT * FROM gists WHERE {} = ?;".format(arg[0]),(arg[1],))
            for row in cursor:
                gist = Gist(row)
                list_gists.append(gist)
    return list_gists

        
