import string

def preprocess_text(text):
# I.S terdefinisi string teks panjang inputan
# F.S mengembalikan array kata yang dipisahkan berdasarkan spasi yang sudah diubah menjadi huruf kecil dan tanda baca dihapus
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()

def count_keywords_iterative(words, keywords):
# I.S terdefinisi array kata words yang sudah melalui pra-proses dan array kata kunci keywords yang akan dihitung banyaknya
# F.S mengembalikan bilangan bulat yang menyatakan total kemunculan seluruh kata kunci dalam keywords dengan pendekatan iteratif
    total = 0
    i = 0

    while i < len(words):
        j = 0
        while j < len(keywords):
            if words[i] == keywords[j]:
                total += 1
            j += 1
        i += 1

    return total


def count_keywords_recursive(words, keywords, i):
# I.S terdefinisi array kata words yang sudah melalui pra-proses, array kata kunci keywords yang akan dihitung banyaknya, dan indeks i sebagai penunjuk posisi kata yang sedang diproses
# F.S mengembalikan bilangan bulat yang menyatakan total kemunculan seluruh kata kunci dalam keywords dengan pendekatan rekursif
    if i == len(words):
        return 0

    j = 0
    total = 0
    while j < len(keywords):
        if words[i] == keywords[j]:
            total = 1
        j += 1

    return total + count_keywords_recursive(words, keywords, i + 1)

