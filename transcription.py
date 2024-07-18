import os
import whisper
import argparse
import json

def main():
    data_path = args.data_path
    json_path = args.json_path
    result = {}
    
    model = whisper.load_model("base")
    
    lg_list = os.listdir(data_path)
    for lg in lg_list:
        lg_path = data_path + '/' + lg
        
        result_file_name = f'{lg}_result.json'
        json_loc = json_path + result_file_name
        
        with open(json_loc, "w") as f:
                
            ad_list = os.listdir(lg_path)
            for ad in ad_list:
                ad_path = lg_path + '/' + ad
                
                fl_list = os.listdir(ad_path)
                json_object = {}
                for fl in fl_list:
                    fl_path = ad_path + '/' + fl
                    if fl.endswith('mp3'):
                        result = model.transcribe(fl_path)
                        result["au_path"] = fl_path
                        result["vi_path"] = fl_path[:-4] + ".mp4"
                    json_object[fl] = result
                    json.dump(json_object, f, indent=2)
        f.close()




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", default="/home/nas4/DB/AVSpeech/AVSpeechDownloader/train", dest="data_path", action="store", type=str, help="Enter data path to transcribe")
    parser.add_argument("--json_path", default="/home/nas4/DB/AVSpeech/AVSpeechDownloader/", dest="json_path", action="store", type=str, help="Enter json path to store")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.data_path):
        print("data path does not exist!")
        sys.exit()
    
    main()