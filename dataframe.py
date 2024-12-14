import pandas as pd

#1
data_list = [ 
    ['Kota Sukabumi',275040,2017],
    ['Kota Sukabumi',168336,2018],
    ['Kota Sukabumi',47509,2020],
    ['Kabupaten Pangandaran',68760,2017],
    ['Kabupaten Pangandaran',39996,2018],
    ['Kabupaten Pangandaran',66106,2020],
    ['Kota Bandung',2031840,2017],
    ['Kota Bandung',2541600,2018],
    ['Kota Bandung',55211,2020],
]
df_list = pd.DataFrame(data_list, columns=['Kabupaten/kota','Jumlah Sampah','Tahun'])
print(df_list)

# 2 Jumlah sampah tahun 2017
data_pertahun = df_list.loc[0,'Jumlah Sampah'] + df_list.loc[3,'Jumlah Sampah'] + df_list.loc[6,'Jumlah Sampah']
print(data_pertahun)

# 3 Jumlah data pertahun
sampah_2017 = df_list.loc[0,'Jumlah Sampah'] + df_list.loc[3,'Jumlah Sampah'] + df_list.loc[6,'Jumlah Sampah']
sampah_2018 = df_list.loc[1,'Jumlah Sampah'] + df_list.loc[4,'Jumlah Sampah'] + df_list.loc[7,'Jumlah Sampah']
sampah_2020 = df_list.loc[2,'Jumlah Sampah'] + df_list.loc[5,'Jumlah Sampah'] + df_list.loc[8,'Jumlah Sampah']

print("\nJumlah sampah per tahun")
print("2017:", sampah_2017)
print("2018:", sampah_2018)
print("2020:", sampah_2020)

# 4 Jumlah data per kota
sampah_sukabumi = df_list.loc[0,'Jumlah Sampah'] + df_list.loc[1,'Jumlah Sampah'] + df_list.loc[2,'Jumlah Sampah']
sampah_pangandaran = df_list.loc[3,'Jumlah Sampah'] + df_list.loc[4,'Jumlah Sampah'] + df_list.loc[5,'Jumlah Sampah']
sampah_bandung = df_list.loc[6,'Jumlah Sampah'] + df_list.loc[7,'Jumlah Sampah'] + df_list.loc[8,'Jumlah Sampah']
print("\nJumlah sampah per Kota/Kabupaten:")
print("Kota Sukabumi:", sampah_sukabumi)
print("Kabupaten Pangandaran:", sampah_pangandaran)
print("Kota Bandung:", sampah_bandung)