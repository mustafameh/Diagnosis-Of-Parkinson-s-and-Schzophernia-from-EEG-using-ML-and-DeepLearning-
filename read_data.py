import mne
#fuction that can read data from path
def read_data(file_path):
    data= mne.io.read_raw_edf(file_path,preload=True)
    data.set_eeg_reference() #sets refrence as average
    data.filter(l_freq=0.5,h_freq=50)#basic filter to the data again
    #split data into segments
    epochs=mne.make_fixed_length_epochs(data,duration=4, overlap=1)
    data=epochs.get_data() # converts data from mne object to numpy array
    return data
