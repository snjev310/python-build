import pandas as pd
import librosa
import librosa.display
df = pd.read_excel('audio_path.xlsx')
del df['Unnamed: 0']
df.head()
#If all the above code[line no 1-6] run successfully it will print a dataframe conatining given column name 
#i.e. path and Interference
def cal_mfcc(path):
    X,sample_rate = librosa.load(path,res_type = 'kaiser_fast')
    mfcc = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0)
    feature = mfcc
    return feature

df['mfcc'] = df['path'].apply(cal_mfcc)
df.head()
#If lines 9-16 run successfully it gives output a data frame with 3 column named Inference,path,mfcc
df['mfcc_mean'] = df['mfcc'].apply(lambda mfcc : mfcc.mean() )
df.head()
#If lines 18-19 run successfully it gives output a data frame with 4 column named Inference,path,mfcc,mfcc_mean
def cal_zcr(path):
    X,sample_rate = librosa.load(path,res_type='kaiser_fast')
    zcr = np.mean(librosa.feature.zero_crossing_rate(X,frame_length=2048,hop_length=512,center=True))
    return zcr
df['zcr'] = df['path'].apply(cal_zcr)
#If lines 21-25 run successfully it gives output a data frame with 5 column named Inference,path,mfcc,mfcc_mean,zcr
def cal_sc(path):
        X,sample_rate = librosa.load(path,res_type='kaiser_fast')
        sc = np.mean(librosa.feature.spectral_centroid(X,sr=sample_rate,n_fft=2048,
                                                       hop_length=512,freq=None,win_length=None,window='hann',
                                                       center=True,pad_mode='reflect'))
        return sc
df['sc'] = df['path'].apply(cal_sc)
df.head()
#If lines 27-24 run successfully it gives output a data frame with 6 column named Inference,path,mfcc,mfcc_mean,zcr,sc
def cal_rms(path):
    X,sample_rate = librosa.load(path,res_type='kaiser_fast')
    rms = np.mean(librosa.feature.rms(y=X,frame_length=2048,hop_length=512,center=True,pad_mode='reflect'))
    return rms
df['rms'] = df['path'].apply(cal_rms)
df.head()
#If lines 36-40 run successfully it gives output a data frame with 7 column named Inference,path,mfcc,mfcc_mean,zcr,sc,rms
def cal_melspectrogram(path):
    X,sample_rate = librosa.load(path,res_type='kaiser_fast')
    _melspectrogram = np.mean(librosa.feature.melspectrogram(y=X,sr=sample_rate,n_fft=2048,hop_length=512,
                                                             win_length=None,window='hann',center=True, 
                                                             pad_mode='reflect',power=2.0))
    return _melspectrogram
df['melspectrogram'] = df['path'].apply(cal_melspectrogram)
df.head()
#If lines 36-40 run successfully it gives output a data frame with 8 column named Inference,path,mfcc,mfcc_mean,zcr,sc,rms,melspectrogram
#and it will be the final dataframe

#To write the dataframe into an Excel file run the following lines, for that you need to make a excel file in the same 
#folder where you run this program named interference_feature.xlsx
writer = pd.ExcelWriter('interference_feature.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='Sheet1')
writer.save()



