from yaml_function import *
import wave
import glob
from utils import *
import os
import librosa
from scipy.io.wavfile import read as wavread
import soundfile


# In[]
params = HParam('config.yaml')

# In[functions]
def downsampleWav(src, dst, outrate):
    if not os.path.exists(src):
        print('Source not found!')
        return False

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    try:
        src_signal, org_sr = librosa.load(src, sr=None)

    except:
        print('Failed to open file!')
        return False

    resampled_y = librosa.resample(src_signal, org_sr, outrate, res_type='fft')
    resampled_y = librosa.resample(resampled_y, outrate, org_sr, res_type='fft')

    try:
        soundfile.write(dst, resampled_y, org_sr, 'PCM_16')
    except:
        print('Failed to write wav')
        return False

    return True

def create_data(scr_root, dst_root, sr):
    dst_root = os.path.join(dst_root, str(sr//1000)+'kHz')
    os.makedirs(dst_root,exist_ok=True)
    downsample_file=0
    downsample_with_error = 0
    for filename in glob.glob(os.path.join(scr_root, '**/*.wav'), recursive=True):
        if os.path.isfile(filename):

            filename = os.path.normpath(filename)
            e = filename.split(os.sep)
            dst = os.path.join(dst_root,'_'.join(e[-3:]))

            if not downsampleWav(filename, dst, sr):
                downsample_with_error+=1
                print(downsample_with_error)
            else:
                downsample_file+=1
            if downsample_file%20==0:
                print(downsample_file)
# for filename in glob.glob(os.path.join(dst_root, '**/*.wav'), recursive=True):


#read all wave file and list it in txt file
def make_text_file_from_data(dst_root, sr, text_file_name):
    dst_root = os.path.join(dst_root, str(sr//1000)+'kHz')
    with open(dst_root + '/'+ text_file_name + '.txt', 'w') as f:
        for file_basename in glob.glob(os.path.join(dst_root, '*.wav')):
            set_name = os.path.basename(file_basename).split('.')[0]
            f.writelines([set_name, '\n'])


# In[]
if __name__ == '__main__':
    for sr in params.prepare_data.sample_rates:
        # create_data(params.prepare_data.raw_input_wavs, params.prepare_data.save_root, sr)
        make_text_file_from_data(params.prepare_data.save_root, sr, 'train_set')



"""
 # sample_wave= '/home/iman/storage/code/project/PERSONAL/military/BWE/data/SampleDeepMine/wav/R000457/S005747/P000001.wav'
samplerate, x = wavread(m)
samplerate2, y = wavread('16demo2.wav')
print(x.dtype)
print(y.dtype)
"""