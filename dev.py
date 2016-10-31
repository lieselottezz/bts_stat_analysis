"""Import csv file with pandas"""
import pandas as pd
btsstat_55 = {}
btsstat_56 = {}
btsstat_57 = {}
btsstat_58 = {}
csvfile = pd.read_csv('btsstat58csv.csv')

# Create Dictionary to store data from BTS Stat 2555
for i in csvfile['Mo Chit'][0:12]:
    btsstat_55.setdefault('Mo Chit', [])
    btsstat_55['Mo Chit'].append(i)

for i in csvfile['Saphan Khwai'][0:12]:
    btsstat_55.setdefault('Saphan Khwai', [])
    btsstat_55['Saphan Khwai'].append(i)
    
for i in csvfile['Ari'][0:12]:
    btsstat_55.setdefault('Ari', [])
    btsstat_55['Ari'].append(i)
    
for i in csvfile['Sanam Pao'][0:12]:
    btsstat_55.setdefault('Sanam Pao', [])
    btsstat_55['Sanam Pao'].append(i)
    
for i in csvfile['Victory Monument'][0:12]:
    btsstat_55.setdefault('Victory Monument', [])
    btsstat_55['Victory Monument'].append(i)

for i in csvfile['Phaya Thai'][0:12]:
    btsstat_55.setdefault('Phaya Thai', [])
    btsstat_55['Phaya Thai'].append(i)

for i in csvfile['Ratchathewi'][0:12]:
    btsstat_55.setdefault('Ratchathewi', [])
    btsstat_55['Ratchathewi'].append(i)

for i in csvfile['Siam'][0:12]:
    btsstat_55.setdefault('Siam', [])
    btsstat_55['Siam'].append(i)

for i in csvfile['Chit Lom'][0:12]:
    btsstat_55.setdefault('Chit Lom', [])
    btsstat_55['Chit Lom'].append(i)

for i in csvfile['Phloen Chit'][0:12]:
    btsstat_55.setdefault('Phloen Chit', [])
    btsstat_55['Phloen Chit'].append(i)

for i in csvfile['Nana'][0:12]:
    btsstat_55.setdefault('Nana', [])
    btsstat_55['Nana'].append(i)

for i in csvfile['Asok'][0:12]:
    btsstat_55.setdefault('Asok', [])
    btsstat_55['Asok'].append(i)

for i in csvfile['Phrom Phong'][0:12]:
    btsstat_55.setdefault('Phrom Phong', [])
    btsstat_55['Phrom Phong'].append(i)

for i in csvfile['Thong Lo'][0:12]:
    btsstat_55.setdefault('Thong Lo', [])
    btsstat_55['Thong Lo'].append(i)

for i in csvfile['Ekkamai'][0:12]:
    btsstat_55.setdefault('Ekkamai', [])
    btsstat_55['Ekkamai'].append(i
                                     )
for i in csvfile['Phra Khanong'][0:12]:
    btsstat_55.setdefault('Phra Khanong', [])
    btsstat_55['Phra Khanong'].append(i)

for i in csvfile['On Nut'][0:12]:
    btsstat_55.setdefault('On Nut', [])
    btsstat_55['On Nut'].append(i)

for i in csvfile['Bang Chak'][0:12]:
    btsstat_55.setdefault('Bang Chak', [])
    btsstat_55['Bang Chak'].append(i)

for i in csvfile['Punnawithi'][0:12]:
    btsstat_55.setdefault('Punnawithi', [])
    btsstat_55['Punnawithi'].append(i)

for i in csvfile['Udom Suk'][0:12]:
    btsstat_55.setdefault('Udom Suk', [])
    btsstat_55['Udom Suk'].append(i)

for i in csvfile['Bang Na'][0:12]:
    btsstat_55.setdefault('Bang Na', [])
    btsstat_55['Bang Na'].append(i)

for i in csvfile['Bearing'][0:12]:
    btsstat_55.setdefault('Bearing', [])
    btsstat_55['Bearing'].append(i)

for i in csvfile['Ratchadamri'][0:12]:
    btsstat_55.setdefault('Ratchadamri', [])
    btsstat_55['Ratchadamri'].append(i)

for i in csvfile['Sala Daeng'][0:12]:
    btsstat_55.setdefault('Sala Daeng', [])
    btsstat_55['Sala Daeng'].append(i)

for i in csvfile['Chong Nonsi'][0:12]:
    btsstat_55.setdefault('Chong Nonsi', [])
    btsstat_55['Chong Nonsi'].append(i)

for i in csvfile['Surasak'][0:12]:
    btsstat_55.setdefault('Surasak', [])
    btsstat_55['Surasak'].append(i)

for i in csvfile['Saphan Taksin'][0:12]:
    btsstat_55.setdefault('Saphan Taksin', [])
    btsstat_55['Saphan Taksin'].append(i)

for i in csvfile['Krung Thon Buri'][0:12]:
    btsstat_55.setdefault('Krung Thon Buri', [])
    btsstat_55['Krung Thon Buri'].append(i)

for i in csvfile['Wongwian Yai'][0:12]:
    btsstat_55.setdefault('Wongwian Yai', [])
    btsstat_55['Wongwian Yai'].append(i)

for i in csvfile['Pho Nimit'][0:12]:
    btsstat_55.setdefault('Pho Nimit', [])
    btsstat_55['Pho Nimit'].append(i)

for i in csvfile['Talat Phlu'][0:12]:
    btsstat_55.setdefault('Talat Phlu', [])
    btsstat_55['Talat Phlu'].append(i)

for i in csvfile['Wutthakat'][0:12]:
    btsstat_55.setdefault('Wutthakat', [])
    btsstat_55['Wutthakat'].append(i)

for i in csvfile['Bang Wa'][0:12]:
    btsstat_55.setdefault('Bang Wa', [])
    btsstat_55['Bang Wa'].append(i)\

for i in csvfile['National Stadium'][0:12]:
    btsstat_55.setdefault('National Stadium', [])
    btsstat_55['National Stadium'].append(i)

# Create Dictionary to store data from BTS Stat 2556
for i in csvfile['Mo Chit'][12:24]:
    btsstat_56.setdefault('Mo Chit', [])
    btsstat_56['Mo Chit'].append(i)

for i in csvfile['Saphan Khwai'][12:24]:
    btsstat_56.setdefault('Saphan Khwai', [])
    btsstat_56['Saphan Khwai'].append(i)
    
for i in csvfile['Ari'][12:24]:
    btsstat_56.setdefault('Ari', [])
    btsstat_56['Ari'].append(i)
    
for i in csvfile['Sanam Pao'][12:24]:
    btsstat_56.setdefault('Sanam Pao', [])
    btsstat_56['Sanam Pao'].append(i)
    
for i in csvfile['Victory Monument'][12:24]:
    btsstat_56.setdefault('Victory Monument', [])
    btsstat_56['Victory Monument'].append(i)

for i in csvfile['Phaya Thai'][12:24]:
    btsstat_56.setdefault('Phaya Thai', [])
    btsstat_56['Phaya Thai'].append(i)

for i in csvfile['Ratchathewi'][12:24]:
    btsstat_56.setdefault('Ratchathewi', [])
    btsstat_56['Ratchathewi'].append(i)

for i in csvfile['Siam'][12:24]:
    btsstat_56.setdefault('Siam', [])
    btsstat_56['Siam'].append(i)

for i in csvfile['Chit Lom'][12:24]:
    btsstat_56.setdefault('Chit Lom', [])
    btsstat_56['Chit Lom'].append(i)

for i in csvfile['Phloen Chit'][12:24]:
    btsstat_56.setdefault('Phloen Chit', [])
    btsstat_56['Phloen Chit'].append(i)

for i in csvfile['Nana'][12:24]:
    btsstat_56.setdefault('Nana', [])
    btsstat_56['Nana'].append(i)

for i in csvfile['Asok'][12:24]:
    btsstat_56.setdefault('Asok', [])
    btsstat_56['Asok'].append(i)

for i in csvfile['Phrom Phong'][12:24]:
    btsstat_56.setdefault('Phrom Phong', [])
    btsstat_56['Phrom Phong'].append(i)

for i in csvfile['Thong Lo'][12:24]:
    btsstat_56.setdefault('Thong Lo', [])
    btsstat_56['Thong Lo'].append(i)

for i in csvfile['Ekkamai'][12:24]:
    btsstat_56.setdefault('Ekkamai', [])
    btsstat_56['Ekkamai'].append(i
                                     )
for i in csvfile['Phra Khanong'][12:24]:
    btsstat_56.setdefault('Phra Khanong', [])
    btsstat_56['Phra Khanong'].append(i)

for i in csvfile['On Nut'][12:24]:
    btsstat_56.setdefault('On Nut', [])
    btsstat_56['On Nut'].append(i)

for i in csvfile['Bang Chak'][12:24]:
    btsstat_56.setdefault('Bang Chak', [])
    btsstat_56['Bang Chak'].append(i)

for i in csvfile['Punnawithi'][12:24]:
    btsstat_56.setdefault('Punnawithi', [])
    btsstat_56['Punnawithi'].append(i)

for i in csvfile['Udom Suk'][12:24]:
    btsstat_56.setdefault('Udom Suk', [])
    btsstat_56['Udom Suk'].append(i)

for i in csvfile['Bang Na'][12:24]:
    btsstat_56.setdefault('Bang Na', [])
    btsstat_56['Bang Na'].append(i)

for i in csvfile['Bearing'][12:24]:
    btsstat_56.setdefault('Bearing', [])
    btsstat_56['Bearing'].append(i)

for i in csvfile['Ratchadamri'][12:24]:
    btsstat_56.setdefault('Ratchadamri', [])
    btsstat_56['Ratchadamri'].append(i)

for i in csvfile['Sala Daeng'][12:24]:
    btsstat_56.setdefault('Sala Daeng', [])
    btsstat_56['Sala Daeng'].append(i)

for i in csvfile['Chong Nonsi'][12:24]:
    btsstat_56.setdefault('Chong Nonsi', [])
    btsstat_56['Chong Nonsi'].append(i)

for i in csvfile['Surasak'][12:24]:
    btsstat_56.setdefault('Surasak', [])
    btsstat_56['Surasak'].append(i)

for i in csvfile['Saphan Taksin'][12:24]:
    btsstat_56.setdefault('Saphan Taksin', [])
    btsstat_56['Saphan Taksin'].append(i)

for i in csvfile['Krung Thon Buri'][12:24]:
    btsstat_56.setdefault('Krung Thon Buri', [])
    btsstat_56['Krung Thon Buri'].append(i)

for i in csvfile['Wongwian Yai'][12:24]:
    btsstat_56.setdefault('Wongwian Yai', [])
    btsstat_56['Wongwian Yai'].append(i)

for i in csvfile['Pho Nimit'][12:24]:
    btsstat_56.setdefault('Pho Nimit', [])
    btsstat_56['Pho Nimit'].append(i)

for i in csvfile['Talat Phlu'][12:24]:
    btsstat_56.setdefault('Talat Phlu', [])
    btsstat_56['Talat Phlu'].append(i)

for i in csvfile['Wutthakat'][12:24]:
    btsstat_56.setdefault('Wutthakat', [])
    btsstat_56['Wutthakat'].append(i)

for i in csvfile['Bang Wa'][12:24]:
    btsstat_56.setdefault('Bang Wa', [])
    btsstat_56['Bang Wa'].append(i)\

for i in csvfile['National Stadium'][12:24]:
    btsstat_56.setdefault('National Stadium', [])
    btsstat_56['National Stadium'].append(i)

# Create Dictionary to store data from BTS Stat 2557
for i in csvfile['Mo Chit'][24:36]:
    btsstat_57.setdefault('Mo Chit', [])
    btsstat_57['Mo Chit'].append(i)

for i in csvfile['Saphan Khwai'][24:36]:
    btsstat_57.setdefault('Saphan Khwai', [])
    btsstat_57['Saphan Khwai'].append(i)
    
for i in csvfile['Ari'][24:36]:
    btsstat_57.setdefault('Ari', [])
    btsstat_57['Ari'].append(i)
    
for i in csvfile['Sanam Pao'][24:36]:
    btsstat_57.setdefault('Sanam Pao', [])
    btsstat_57['Sanam Pao'].append(i)
    
for i in csvfile['Victory Monument'][24:36]:
    btsstat_57.setdefault('Victory Monument', [])
    btsstat_57['Victory Monument'].append(i)

for i in csvfile['Phaya Thai'][24:36]:
    btsstat_57.setdefault('Phaya Thai', [])
    btsstat_57['Phaya Thai'].append(i)

for i in csvfile['Ratchathewi'][24:36]:
    btsstat_57.setdefault('Ratchathewi', [])
    btsstat_57['Ratchathewi'].append(i)

for i in csvfile['Siam'][24:36]:
    btsstat_57.setdefault('Siam', [])
    btsstat_57['Siam'].append(i)

for i in csvfile['Chit Lom'][24:36]:
    btsstat_57.setdefault('Chit Lom', [])
    btsstat_57['Chit Lom'].append(i)

for i in csvfile['Phloen Chit'][24:36]:
    btsstat_57.setdefault('Phloen Chit', [])
    btsstat_57['Phloen Chit'].append(i)

for i in csvfile['Nana'][24:36]:
    btsstat_57.setdefault('Nana', [])
    btsstat_57['Nana'].append(i)

for i in csvfile['Asok'][24:36]:
    btsstat_57.setdefault('Asok', [])
    btsstat_57['Asok'].append(i)

for i in csvfile['Phrom Phong'][24:36]:
    btsstat_57.setdefault('Phrom Phong', [])
    btsstat_57['Phrom Phong'].append(i)

for i in csvfile['Thong Lo'][24:36]:
    btsstat_57.setdefault('Thong Lo', [])
    btsstat_57['Thong Lo'].append(i)

for i in csvfile['Ekkamai'][24:36]:
    btsstat_57.setdefault('Ekkamai', [])
    btsstat_57['Ekkamai'].append(i
                                     )
for i in csvfile['Phra Khanong'][24:36]:
    btsstat_57.setdefault('Phra Khanong', [])
    btsstat_57['Phra Khanong'].append(i)

for i in csvfile['On Nut'][24:36]:
    btsstat_57.setdefault('On Nut', [])
    btsstat_57['On Nut'].append(i)

for i in csvfile['Bang Chak'][24:36]:
    btsstat_57.setdefault('Bang Chak', [])
    btsstat_57['Bang Chak'].append(i)

for i in csvfile['Punnawithi'][24:36]:
    btsstat_57.setdefault('Punnawithi', [])
    btsstat_57['Punnawithi'].append(i)

for i in csvfile['Udom Suk'][24:36]:
    btsstat_57.setdefault('Udom Suk', [])
    btsstat_57['Udom Suk'].append(i)

for i in csvfile['Bang Na'][24:36]:
    btsstat_57.setdefault('Bang Na', [])
    btsstat_57['Bang Na'].append(i)

for i in csvfile['Bearing'][24:36]:
    btsstat_57.setdefault('Bearing', [])
    btsstat_57['Bearing'].append(i)

for i in csvfile['Ratchadamri'][24:36]:
    btsstat_57.setdefault('Ratchadamri', [])
    btsstat_57['Ratchadamri'].append(i)

for i in csvfile['Sala Daeng'][24:36]:
    btsstat_57.setdefault('Sala Daeng', [])
    btsstat_57['Sala Daeng'].append(i)

for i in csvfile['Chong Nonsi'][24:36]:
    btsstat_57.setdefault('Chong Nonsi', [])
    btsstat_57['Chong Nonsi'].append(i)

for i in csvfile['Surasak'][24:36]:
    btsstat_57.setdefault('Surasak', [])
    btsstat_57['Surasak'].append(i)

for i in csvfile['Saphan Taksin'][24:36]:
    btsstat_57.setdefault('Saphan Taksin', [])
    btsstat_57['Saphan Taksin'].append(i)

for i in csvfile['Krung Thon Buri'][24:36]:
    btsstat_57.setdefault('Krung Thon Buri', [])
    btsstat_57['Krung Thon Buri'].append(i)

for i in csvfile['Wongwian Yai'][24:36]:
    btsstat_57.setdefault('Wongwian Yai', [])
    btsstat_57['Wongwian Yai'].append(i)

for i in csvfile['Pho Nimit'][24:36]:
    btsstat_57.setdefault('Pho Nimit', [])
    btsstat_57['Pho Nimit'].append(i)

for i in csvfile['Talat Phlu'][24:36]:
    btsstat_57.setdefault('Talat Phlu', [])
    btsstat_57['Talat Phlu'].append(i)

for i in csvfile['Wutthakat'][24:36]:
    btsstat_57.setdefault('Wutthakat', [])
    btsstat_57['Wutthakat'].append(i)

for i in csvfile['Bang Wa'][24:36]:
    btsstat_57.setdefault('Bang Wa', [])
    btsstat_57['Bang Wa'].append(i)\

for i in csvfile['National Stadium'][24:36]:
    btsstat_57.setdefault('National Stadium', [])
    btsstat_57['National Stadium'].append(i)

# Create Dictionary to store data from BTS Stat 2558
for i in csvfile['Mo Chit'][36:48]:
    btsstat_58.setdefault('Mo Chit', [])
    btsstat_58['Mo Chit'].append(i)

for i in csvfile['Saphan Khwai'][36:48]:
    btsstat_58.setdefault('Saphan Khwai', [])
    btsstat_58['Saphan Khwai'].append(i)
    
for i in csvfile['Ari'][36:48]:
    btsstat_58.setdefault('Ari', [])
    btsstat_58['Ari'].append(i)
    
for i in csvfile['Sanam Pao'][36:48]:
    btsstat_58.setdefault('Sanam Pao', [])
    btsstat_58['Sanam Pao'].append(i)
    
for i in csvfile['Victory Monument'][36:48]:
    btsstat_58.setdefault('Victory Monument', [])
    btsstat_58['Victory Monument'].append(i)

for i in csvfile['Phaya Thai'][36:48]:
    btsstat_58.setdefault('Phaya Thai', [])
    btsstat_58['Phaya Thai'].append(i)

for i in csvfile['Ratchathewi'][36:48]:
    btsstat_58.setdefault('Ratchathewi', [])
    btsstat_58['Ratchathewi'].append(i)

for i in csvfile['Siam'][36:48]:
    btsstat_58.setdefault('Siam', [])
    btsstat_58['Siam'].append(i)

for i in csvfile['Chit Lom'][36:48]:
    btsstat_58.setdefault('Chit Lom', [])
    btsstat_58['Chit Lom'].append(i)

for i in csvfile['Phloen Chit'][36:48]:
    btsstat_58.setdefault('Phloen Chit', [])
    btsstat_58['Phloen Chit'].append(i)

for i in csvfile['Nana'][36:48]:
    btsstat_58.setdefault('Nana', [])
    btsstat_58['Nana'].append(i)

for i in csvfile['Asok'][36:48]:
    btsstat_58.setdefault('Asok', [])
    btsstat_58['Asok'].append(i)

for i in csvfile['Phrom Phong'][36:48]:
    btsstat_58.setdefault('Phrom Phong', [])
    btsstat_58['Phrom Phong'].append(i)

for i in csvfile['Thong Lo'][36:48]:
    btsstat_58.setdefault('Thong Lo', [])
    btsstat_58['Thong Lo'].append(i)

for i in csvfile['Ekkamai'][36:48]:
    btsstat_58.setdefault('Ekkamai', [])
    btsstat_58['Ekkamai'].append(i
                                     )
for i in csvfile['Phra Khanong'][36:48]:
    btsstat_58.setdefault('Phra Khanong', [])
    btsstat_58['Phra Khanong'].append(i)

for i in csvfile['On Nut'][36:48]:
    btsstat_58.setdefault('On Nut', [])
    btsstat_58['On Nut'].append(i)

for i in csvfile['Bang Chak'][36:48]:
    btsstat_58.setdefault('Bang Chak', [])
    btsstat_58['Bang Chak'].append(i)

for i in csvfile['Punnawithi'][36:48]:
    btsstat_58.setdefault('Punnawithi', [])
    btsstat_58['Punnawithi'].append(i)

for i in csvfile['Udom Suk'][36:48]:
    btsstat_58.setdefault('Udom Suk', [])
    btsstat_58['Udom Suk'].append(i)

for i in csvfile['Bang Na'][36:48]:
    btsstat_58.setdefault('Bang Na', [])
    btsstat_58['Bang Na'].append(i)

for i in csvfile['Bearing'][36:48]:
    btsstat_58.setdefault('Bearing', [])
    btsstat_58['Bearing'].append(i)

for i in csvfile['Ratchadamri'][36:48]:
    btsstat_58.setdefault('Ratchadamri', [])
    btsstat_58['Ratchadamri'].append(i)

for i in csvfile['Sala Daeng'][36:48]:
    btsstat_58.setdefault('Sala Daeng', [])
    btsstat_58['Sala Daeng'].append(i)

for i in csvfile['Chong Nonsi'][36:48]:
    btsstat_58.setdefault('Chong Nonsi', [])
    btsstat_58['Chong Nonsi'].append(i)

for i in csvfile['Surasak'][36:48]:
    btsstat_58.setdefault('Surasak', [])
    btsstat_58['Surasak'].append(i)

for i in csvfile['Saphan Taksin'][36:48]:
    btsstat_58.setdefault('Saphan Taksin', [])
    btsstat_58['Saphan Taksin'].append(i)

for i in csvfile['Krung Thon Buri'][36:48]:
    btsstat_58.setdefault('Krung Thon Buri', [])
    btsstat_58['Krung Thon Buri'].append(i)

for i in csvfile['Wongwian Yai'][36:48]:
    btsstat_58.setdefault('Wongwian Yai', [])
    btsstat_58['Wongwian Yai'].append(i)

for i in csvfile['Pho Nimit'][36:48]:
    btsstat_58.setdefault('Pho Nimit', [])
    btsstat_58['Pho Nimit'].append(i)

for i in csvfile['Talat Phlu'][36:48]:
    btsstat_58.setdefault('Talat Phlu', [])
    btsstat_58['Talat Phlu'].append(i)

for i in csvfile['Wutthakat'][36:48]:
    btsstat_58.setdefault('Wutthakat', [])
    btsstat_58['Wutthakat'].append(i)

for i in csvfile['Bang Wa'][36:48]:
    btsstat_58.setdefault('Bang Wa', [])
    btsstat_58['Bang Wa'].append(i)\

for i in csvfile['National Stadium'][36:48]:
    btsstat_58.setdefault('National Stadium', [])
    btsstat_58['National Stadium'].append(i)
print("2555")
for i in btsstat_55:
    print(i, btsstat_55[i])
print()
print("2556")
for i in btsstat_56:
    print(i, btsstat_56[i])
print()
print("2557")
for i in btsstat_57:
    print(i, btsstat_57[i])
print()
print("2558")
for i in btsstat_58:
    print(i, btsstat_58[i])
