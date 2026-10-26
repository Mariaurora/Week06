import mysql.connector
from mysql.connector import errorcode


def main():
    print("Il mio primo programma con MySql")

    try:
        # Stabilisco la connessione con il database
        conn = mysql.connector.connect(user='root',
                                      password='',
                                      host='localhost',
                                      port='3306',
                                      database='products_suppliers')

        print("Se sono arrivato qui mi sono collegato al database")

        # Mi faccio dare dalla connessione conn un cursore
        # cursore = conn.cursor()
        cursore_dizionario = conn.cursor(dictionary=True)

        # Scrivo la query in SQL
        #query = "SELECT * FROM S"

        # Come creare una query parametrica/parametrizzata
        citta = input("Per quale citta' vuoi estrarre i fornitori? ")

        #query = f"""SELECT `S#`, `STATUS`
        #           FROM S
        #           WHERE CITY = '{citta}'"""

        query = f"""SELECT `S#`, `STATUS`
                   FROM S
                   WHERE CITY = %s"""


        # La eseguo attraverso il cursore
        #cursore.execute(query)
        #cursore_dizionario.execute(query)
        cursore_dizionario.execute(query, (citta, ))

        # Il cursore è un container di Python ...
        # ... quindi posso iterare su di esso con for
        #for riga in cursore:
        #    print(riga[1])

        for riga in cursore_dizionario:
            #print(riga["SNAME"])
            print(riga)


    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ERRORE: Qualcosa è andato storto con username o password!");
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("ERRORE: Lo schema di database non esiste")
        else:
            print(err)
    else:
        conn.close()



main()
pass

