![header](https://capsule-render.vercel.app/api?type=soft&text=Text&nbsp;to&nbsp;Speech&nbsp;(TTS)&nbsp;for&nbsp;Jejueo&fontSize=45&color=439A97&fontColor=ffff)

## Glow-TTS와 HiFi-GAN을 사용한 제주어 음성 합성 프로젝트

Jejueo TTS (제주어 음성합성) using [🐸Coqui TTS](https://github.com/coqui-ai/TTS) Model - Glow-TTS & HiFi-GAN 
- Train models with [Jejueo Single Speaker Speech](https://www.kaggle.com/datasets/bryanpark/jejueo-single-speaker-speech-dataset) Dataset for 1K Step

### You can check the TTS result examples on [here](https://watchstep.me/glow-tts-jejueo-demo/)!

## Project Structure
```
glow-tts-dialect
├─ korean # for preprocessing jejueo
│  ├─ __init__.py
│  ├─ ko_dictionary.py
│  ├─ ko_normalize.py
│  ├─ ko_cleaner.py
├─ model # for saving model .pth file
│  ├─ glow-tts
│  └─ hifigan
├─ audio # for saving .wav file
├─ prepare-data.ipynb
├─ glow-tts.ipynb 
├─ inference.ipynb
└─ hifi-gan.ipynb
```
## Requirements

```
!pip install librosa
!pip install TTS==0.10.0
!pip install jamo==0.4.1
!pip install kaggle
```

## Reference
- [Jejueo Datasets for Machine Translation and Speech Synthesis](https://arxiv.org/pdf/1911.12071.pdf)
- [A Generative Flow for Text-to-Speech via Monotonic Alignment Search](https://github.com/jaywalnut310/glow-tts)
- [SCE-TTS: 내 목소리로 TTS 만들기
](https://sce-tts.github.io/#/)
- [Korean TTS using coqui TTS (glowtts and multiband melgan) - 한국어 TTS](https://github.com/ttop32/coqui_tts_korea)
-[KSS데이터를 활용한 Text to speech service (glow_tts, hifi_gan)](https://github.com/ljh468/Imf_TTS)
