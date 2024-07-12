import argparse
import os
import whisper
import shutil
import sys

def main():
    src_path = args.src_path
    dest_path = args.dest_path
    mp4 = args.mp4
    
    
    '''
    ex) path of data : /home/DB/dataset_name/data/A/A_1.mp3
                    /home/DB/dataset_name/data/A/A_2.mp3
                    .
                    .
                    .
                    /home/DB/dataset_name/data/B/B_1.mp3
                    
        src_path = "/home/DB/AVSpeech/data"
        linkList = ['A', ...]
    ''' 
    
    linkList = os.listdir(src_path)

    model = whisper.load_model("base")

    for link in linkList:
        
        link_path = src_path + '/' + link
        fileList = os.listdir(link_path)
        
        mp3List = [f for f in fileList if f.endswith('.mp3')]
        
        # Using whisper, get information from mp3
        for mp3 in mp3List:
            audio_path = link_path + '/' + mp3
            result = model.transcribe(audio_path)
            
            lang_path = dest_path + '/' + result["language"]
            
            if not os.path.isdir(lang_path):
                os.makedirs(lang_path)
            if not os.path.isdir(os.path.join(lang_path, link)):
                os.makedirs(os.path.join(lang_path, link))
                
            shutil.move(audio_path, os.path.join(lang_path, link, mp3))
            print(mp3)
            if mp4:
                mp4name = mp3.replace('mp3', 'mp4')
                shutil.move(os.path.join(link_path, mp4name), os.path.join(lang_path, link, mp4name))
            print(mp4name)
            
        



if __name__ == '__main__':
    # "/home/nas4/DB/AVSpeech/AVSpeechDownloader/data"
    # "/home/nas4/DB/AVSpeech/AVSpeechDownloader/test_data/data"
    # "/home/nas4/DB/AVSpeech/AVSpeechDownloader/train"
    # "/home/nas4/DB/AVSpeech/AVSpeechDownloader/test"

    parser = argparse.ArgumentParser()
    parser.add_argument("--src", default="/home/nas4/DB/AVSpeech/AVSpeechDownloader/data", dest="src_path", action="store", type=str, help='original path where data stored')
    parser.add_argument("--dest", default="/home/nas4/DB/AVSpeech/AVSpeechDownloader/train", dest="dest_path", action="store", type=str, help='destination path where classified data stored')
    parser.add_argument("--mp4", default=True, dest="mp4", type=bool, help="If you move both mp4 and mp3 that has same name, set True, or only for just mp3, set False")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.src_path):
        print("src path does not exist!")
        sys.exit()
        
    if not os.path.isdir(args.dest_path):
        print("dest path does not exist!")
        sys.exit()
    
    main()