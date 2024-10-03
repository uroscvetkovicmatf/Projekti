import sqlite3

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

conn = sqlite3.connect("baza.db") # conn ( connection ) - promenljiva koja nam omogućava konekciju između Python - a i SQL - a ( BAZE )
c = conn.cursor()                 # c ( cursor ) - promenljiva koja nam omogućava upravljanje bazom

                                  # execute( ) - sluzi za izvrsavanje nekog UPIT - a
c.execute( """                    

    CREATE TABLE knjige(

        barkod text,
        autor text,
        naziv text,
        izdavac text,
        godina_izdanja int,
        mesto_izdanja text

    	)

	""")

conn.close()                      # close( ) - zatvaranje konekcije za BAZOM
