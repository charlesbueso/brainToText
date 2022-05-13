import pandas as pd
import mne

link = "EEG_recording_2022-04-26-18.58.23.csv"
#opening data with pandas
df = pd.read_csv(link)

df.drop("timestamps", axis =1, inplace=True)
df.drop("Secondary Timestamp (Base)", axis =1, inplace=True)
df.drop("Secondary Timestamp (Remainder)", axis =1, inplace=True)

sfreq = 250
#ch_types = ["eeg"]*df.shape[1]
ch_types = ["eeg","eeg", "eeg", "eeg"]
ch_names = ["TP9","AF7", "AF8","TP10"]
montage = mne.channels.make_standard_montage("standard_1020")
info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)
samples = df.T*1e-6
loadedRaw = mne.io.RawArray(samples, info)
loadedRaw.set_montage(montage = montage)

loadedRaw.info

loadedRaw.plot()
loadedRaw.plot_sensors(show_names=True)
loadedRaw.plot_psd()
loadedRaw.plot_psd(tmin=0,tmax=60, fmin=2, fmax=120, average=True)