meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "Tanggapan terhadap lelucon",
            "SHEESH": "Sedikit ketidaksetujuan",
            "CREEPY": "Menakutkan, tidak menyenangkan",
            "AGGRO": "Untuk menjadi agresif/marah",
            "EW": "Menjijikkan dan jelek",
            }
            

for i in range(5):
    word = input("Ketik kata yang tidak kamu mengerti! (gunakan huruf kapital semua!): ")
    word = word.upper()

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Not in dictionary!")
