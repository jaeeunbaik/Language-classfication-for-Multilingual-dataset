# Language-classfication-and-transcription-for-Multilingual-dataset


#### This code is for classification and transcription of multi-lingual dataset using [OpenAI/Whisper](https://github.com/openai/whisper?tab=readme-ov-file). Originally for AVSpeech dataset!


#### 다언어 데이터셋에 대해서 [whisper](https://github.com/openai/whisper?tab=readme-ov-file)를 이용해서 언어별로 데이터셋을 분류하고, 
#### whisper를 이용해서 전사하는 데이터셋입니다.



```
ex) path of data : /home/DB/dataset_name/data/A/A_1.mp3
              /home/DB/dataset_name/data/A/A_2.mp3
              .
              .
              .
              /home/DB/dataset_name/data/B/B_1.mp3
              
    src_path = "/home/DB/AVSpeech/data"
    linkList = ['A', ...]
```

```
--src : 'Enter the path where the MP3 is stored, grandparent folders'
--dest : 'Enter the path wher the MP3 will be classfied, the subfolders (ex. .../fr/A/A_1.mp3, .../en/B/B_1.mp3, ...)
```
