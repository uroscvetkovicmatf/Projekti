import sqlite3

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def izmeni_podatak_u_bazi(podatak_koji_menjamo, novi_podatak):

	upit = f"""

			UPDATE knjige
			SET {podatak_koji_menjamo} = "{novi_podatak}"
			WHERE barkod = {bar_kod_3}

		"""

	c.execute(upit)
	conn.commit()

	conn.close()

	print("Izmena je uspešno izvrešena.")

while True:

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

	conn = sqlite3.connect("baza.db")          					  # ostvarivanje konekcije za BAZOM PODATAKA
	c = conn.cursor()                          					  # da bismo manipulisali BAZOM, potreban nam je CURSOR / KURSOR ( promenljiva c )

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

	pitanje = input("Izaberite jednu od sledećih opcija\n\t1. Dodaj novu knjigu\n\t2. Pretraži knjigu ( na osnovu bar-koda )\n\t3. Izmeni podatke o knjizi\n\t4. Obriši knjigu\n\t5. Prikaži sve knjige\n")

	while pitanje not in ['1', '2', '3', '4', '5']:
		pitanje = input("Uneli ste nedozvoljenu vrednost ( pogrešan karakter ), pokušajte ponovo: ")

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

	if pitanje == '1':
	    
	    bar_kod = input("Unesite bar-kod knjige: ")
	    autor = input("Unesite ime i prezime autora: ")
	    naziv = input("Unesite naziv: ")
	    izdavac = input("Unesite ime izdavača: ")
	    godina_izdanja = input("Unesite godinu kada je knjiga izdata: ")
	    mesto_izdanja = input("Unesite mesto gde je knjiga izdata: ")
	    
	    upit = f"""

	    	INSERT INTO knjige
	    	VALUES ( "{bar_kod}", "{autor}", "{naziv}", "{izdavac}", {godina_izdanja}, "{mesto_izdanja}" )	

	    """

	    c.execute(upit)                       					  # metodi execute prosleđujemo zadati UPIT kojim se dodaju podaci vezani za novu knjigu
	    conn.commit()                         					  # da bi ova promena bila vidljiva, potrebno je navesti i ovu komandu ( commit() )

	    conn.close()
	     
	    print("Knjiga je uspešno dodata u bazu.") 

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -    

	elif pitanje == '2':

		bar_kod = input("Unesite bar-kod knjige koju želite da pretražite: ")

		upit = f"""

	    	SELECT *
	    	FROM knjige
	    	WHERE barkod = {bar_kod}

		"""
		
		c.execute(upit)
		rezultat_upita = c.fetchall()             				  # prihvatanje rezultata upita ( fetchall() )
	    
		conn.close()

		if len(rezultat_upita) == 0:                              # rezultat_upita je LISTA TORKI ( u svakoj TORKI su podaci vezani za jednu knjigu )
			print("Tražena knjiga se ne nalazi u bazi podataka.")

		else:
			print(" - " * 13)
			print(f"Autor: {rezultat_upita[0][1]}")                
			print(f"Naziv: {rezultat_upita[0][2]}")
			print(f"Izdavač: {rezultat_upita[0][3]}")
			print(f"Godina izdavača: {rezultat_upita[0][4]}.")
			print(f"Mesto izdavača: {rezultat_upita[0][5]}")

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -		
	    
	elif pitanje == '3':
		
		bar_kod_3 = input("Unesite bar-kod knjige koju želite da izmenite: ")

		pitanje = input("\nIzaberite ono što želite da izmenite kod odabrane knjige:\n\t1. Bar-kod\n\t2. Autor\n\t3. Naziv\n\t4. Izdavač\n\t5. Godina izdanja\n\t6. Mesto izdanja\n")

		while pitanje not in ['1', '2', '3', '4', '5', '6']:
			pitanje = input("Uneli ste nedozvoljenu vrednost ( pogrešan karakter ), pokušajte ponovo: ")

		if pitanje == '1':

			nova_vrednost = input("Unesite novu vrednost za bar-kod: ")

			izmeni_podatak_u_bazi("barkod", nova_vrednost)

		elif pitanje == '2':

			nova_vrednost = input("Unesite novu vrednost za autora knjige: ")

			izmeni_podatak_u_bazi("autor", nova_vrednost)

		elif pitanje == '3':

			nova_vrednost = input("Unesite novu vrednost za naziv knjige: ")

			izmeni_podatak_u_bazi("naziv", nova_vrednost)

		elif pitanje == '4':

			nova_vrednost = input("Unesite novu vrednost za izdavača: ")

			izmeni_podatak_u_bazi("izdavac", nova_vrednost)

		elif pitanje == '5':

			nova_vrednost = int(input("Unesite novu vrednost za godinu: "))

			izmeni_podatak_u_bazi("godina_izdanja", nova_vrednost)

		elif pitanje == '6':

			nova_vrednost = input("Unesite novu vrednost za mesto: ")

			izmeni_podatak_u_bazi("mesto_izdanja", nova_vrednost)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

	elif pitanje == '4':

		bar_kod = input("Unesite bar-kod knjige koju želite da obrišete iz baze podataka: ")

		upit = f"""

	    	SELECT *
	    	FROM knjige
	    	WHERE barkod = {bar_kod}

		"""
		
		c.execute(upit)
		rezultat_upita = c.fetchall()             				  

		if len(rezultat_upita) == 0:                              
			print("Tražena knjiga se ne nalazi u bazi podataka.")

			conn.close()

		else:

			upit = f"""

				DELETE FROM knjige
				WHERE barkod = {bar_kod}

			"""		

			c.execute(upit)
			conn.commit()
	 
			conn.close()

			print("Knjiga je uspešno uklonjena / izbrisana iz baze podataka.")

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

	elif pitanje == '5':

		upit = """

			SELECT *
			FROM knjige

		"""

		c.execute(upit)
		rezultat_upita = c.fetchall()

		conn.close()

		if len(rezultat_upita) == 0:
			print("U bazi podataka se ne nalazi nijedna knjiga.")

		else:

			for i in rezultat_upita:
				print("- " * 13)
				print(f"Bar-kod: {i[0]}")
				print(f"Autor: {i[1]}")
				print(f"Naziv: {i[2]}")
				print(f"izdavač: {i[3]}")
				print(f"Godina: {i[4]}.")
				print(f"Mesto: {i[5]}")

	ponovo = input("Da li želite da odaberete još neku opciju?\n\t\tDa / Ne\n")

	while ponovo not in ["Da", "Ne"]:
		ponovo = input("Uneli ste nedozvoljenu vrednost, pokušajte ponovo:\n( Unesite Da / Ne )\n")
    
	if ponovo == "Ne":
		break
