def converter(metros):
    conversoes = {
    	    "kilometros (km)": metros / 1000,
         "hectometro (hm)" : metros / 100,
         "decametro (dam)" : metros / 10,
         "decimetro (dm)" : metros * 10,
         "centimetro (cm)" : metros * 100,
         "milimetro (mm)" : metros * 1000
    	}
    	
    for unidade, valor  in conversoes.items():
        	print(f"{metros} m = {valor}{unidade}")

 
metros = float(input("Uma distancia em metros: "))
print(f"A medida de {metros}m corresponde a: ")
converter(metros)