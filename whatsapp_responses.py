# Custom respon bot sesuai keinginan mu

new_message = []

def response(input_message):
    message = input_message.lower()
    # ini hanya contoh dari saya :v
    if message == 'help' :
        return "Berikut beberapa kata yg dimengerti bot : \nhelp, hai, mang, dimas, p, test, we, salam kenal.\nMaaf jika kata yang anda butuhkan tidak ada. Kirim 'saran' untuk menambahkan kata baru utk bot dan output nya anda sendiri yg atur."
    elif message == 'hai':
        return 'bot : haii jugaa'
    elif message == 'dimas':
        return 'bot : Apa?'
    elif message == 'mang':
        return 'bot : Apee?'
    elif message == 'p' :
        return 'bot : Pa pe pa pe, y.'
    elif message == 'test':
        return 'bot : bot aktif!'
    elif message == 'we' or  message=='wee' or message=='weee':
        return 'bot : oit?'
    elif message == 'salam kenal':
        return 'bot : salam kenal juga, pemilik nomor ini namanya Dimas.\nDuduk di bangku SMP.'
    elif message == 'gpp' or message=='hm':
        return 'bot : y'
    elif message == 'hah' or message == 'y':
        return 'bot : hm'
    elif message == 'ok' or message=='sip' or message=='oh' or message=='ae':
        return 'bot : OK'
    elif message == 'besok coba lagi' or message=='coba lagi' or message=='coba' or message=='besok coba':
        return 'bot : sip, akan dicoba lagi'
    
    elif message == 'saran': #perbaikan
        return "bot : maaf, belum bisa menggunakan fitur ini karena masih dalam perbaikan."
    else:
        return "bot : tidak ngerti cuy, ketik 'help' untuk menampilkan kata apa saja yg dimengerti."
