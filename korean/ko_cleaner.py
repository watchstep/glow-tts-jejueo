#https://github.com/coqui-ai/TTS/tree/dev/TTS/tts/utils/text/korean
# https://github.com/Deepest-Project/MelNet/blob/master/text/korean.py

import re
from korean.ko_normalize import normalize
from jamo import hangul_to_jamo, h2j, j2h, hcj_to_jamo, is_hcj
from jamo.jamo import _jamo_char_to_hcj

PAD = '_'
EOS = '~'
PUNC = '!\'(),-.:;? '

'''
한국어 초성, 중성, 종성 구분해 유니코드로 변경
제주 방언에는 아래아, 쌍아래아 사용됨
ᆞ (아래아) 0x119E
ᆢ (쌍아래아) 0x11A2
ᅌ (옛이응) 0x114C
'''

LEADS = [chr(_) for _ in range(0x1100, 0x1113)]
JAMO_LEADS = "".join(LEADS)

VOWELS = [chr(_) for _ in range(0x1161, 0x1176)]
VOWELS.extend([chr(_) for _ in [0x119E, 0x11A2, 0x114C]])
JAMO_VOWELS = "".join(VOWELS)

TAILS = [chr(_) for _ in range(0x11A8, 0x11C3)]
JAMO_TAILS = "".join(TAILS)

VALID_CHARS = JAMO_LEADS + JAMO_VOWELS + JAMO_TAILS
ALL_SYMBOLS = PAD + PUNC + VALID_CHARS + EOS

char_to_id = {c: i for i, c in enumerate(ALL_SYMBOLS)}
id_to_char = {i: c for i, c in enumerate(ALL_SYMBOLS)}


def is_lead(char):
    return char in JAMO_LEADS

def is_vowel(char):
    return char in JAMO_VOWELS

def is_tail(char):
    return char in JAMO_TAILS

def get_mode(char):
    if is_lead(char):
        return 0
    elif is_vowel(char):
        return 1
    elif is_tail(char):
        return 2
    else:
        return -1

def _get_text_from_candidates(candidates):
    if len(candidates) == 0:
        return ""
    elif len(candidates) == 1:
        return _jamo_char_to_hcj(candidates[0])
    else:
        return j2h(**dict(zip(["lead", "vowel", "tail"], candidates)))

def jamo_to_korean(text):
    text = h2j(text)

    idx = 0
    new_text = ""
    candidates = []

    while True:
        if idx >= len(text):
            new_text += _get_text_from_candidates(candidates)
            break

        char = text[idx]
        mode = get_mode(char)

        if mode == 0:
            new_text += _get_text_from_candidates(candidates)
            candidates = [char]
        elif mode == -1:
            new_text += _get_text_from_candidates(candidates)
            new_text += char
            candidates = []
        else:
            candidates.append(char)

        idx += 1
    return new_text
  
def compare_sentence_with_jamo(text1, text2):
    return h2j(text1) != h2j(text2)

def tokenize(text, as_id=False):
    # "jamo" package의 hangul_to_jamo를 이용하여 한글 string을 초성/중성/종성으로 분리
    text = normalize(text)
    tokens = list(hangul_to_jamo(text)) # '존경하는'  --> ['ᄌ', 'ᅩ', 'ᆫ', 'ᄀ', 'ᅧ', 'ᆼ', 'ᄒ', 'ᅡ', 'ᄂ', 'ᅳ', 'ᆫ', '~']

    if as_id:
        return [char_to_id[token] for token in tokens] + [char_to_id[EOS]]
    else:
        return [token for token in tokens] + [EOS]

def tokenize_fn(iterator):
    return (token for x in iterator for token in tokenize(x, as_id=False))