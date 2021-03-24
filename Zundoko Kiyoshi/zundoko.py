import random

def zundoko_gen():
    zun_count = 0
    word_list = ('ズン', 'ドコ')

    while True:
        word = random.choice(word_list)
        yield word

        if word == 'ズン':
            zun_count += 1
        else:
            if word == 'ドコ' and  zun_count >= 4:
                return
            zun_count = 0


for word in zundoko_gen():
    print(word);

print('キ・ヨ・シ！')
