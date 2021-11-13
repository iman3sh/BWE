from scipy.io.wavfile import read
import matplotlib
# matplotlib.use("Agg")
import matplotlib.pylab as plt
import librosa

def plot_spectrogram(spectrogram):
    fig, ax = plt.subplots(figsize=(10, 2))
    im = ax.imshow(spectrogram, aspect="auto", origin="lower",
                   interpolation='none')
    plt.colorbar(im, ax=ax)

    fig.canvas.draw()
    plt.show()
    plt.close()

    return fig

def load_wav(full_path):
    sampling_rate, data = read(full_path)
    return data, sampling_rate
kHz4_F = '/home/iman/storage/code/project/PERSONAL/military/BWE/utils/kHz4_F.wav'
kHz4_R = '/home/iman/storage/code/project/PERSONAL/military/BWE/utils/kHz4_R.wav'
kHz8_R = '/home/iman/storage/code/project/PERSONAL/military/BWE/utils/kHz8_R.wav'
kHz16_R = '/home/iman/storage/code/project/PERSONAL/military/BWE/utils/kHz16_R.wav'
x, sr = librosa.load(kHz4_F, sr=None)
X = librosa.stft(x, n_fft=512)
plot_spectrogram(librosa.amplitude_to_db(abs(X)))


x, sr = librosa.load(kHz4_R, sr=None)
print(sr)
X = librosa.stft(x, n_fft=512)
plot_spectrogram(librosa.amplitude_to_db(abs(X)))



x, sr = librosa.load(kHz8_R, sr=None)
X = librosa.stft(x, n_fft=512)
plot_spectrogram(librosa.amplitude_to_db(abs(X)))


x, sr = librosa.load(kHz16_R, sr=None)
X = librosa.stft(x, n_fft=512)
plot_spectrogram(librosa.amplitude_to_db(abs(X)))