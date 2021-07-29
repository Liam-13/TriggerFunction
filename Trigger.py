HitArray = ev.photons_end.t[DetectionFlag]
distance = ev.photons_end.pos[DetectionFlag]
YamlPMTs = 2
YamlTime = 500
YamlOccur = 3
pmtsize = 202


trigger = 0
#for hitTime1 in HitArray:
hitTime1 = HitArray[0]
pos = -1
PMTs = []
NumOfPMT = 0
Count = 0

for hitTime2 in HitArray:
  temp = HitArray[HitArray != hitTime2]
  distanceTemp = distance[HitArray != hitTime2]# removes its own time
  TimeDif = np.abs(temp - hitTime2) < YamlTime  #boolean of all the times that are close enough for the specific time
  PMTs = distanceTemp[TimeDif]  #boolean used to find the end positions of relevant Photons

  for IsolatedPMT in PMTs:
    print(np.sum(np.square(IsolatedPMT-PMTs)), axis=1)
    distanceBool = np.abs(np.sqrt(np.sum(np.square(IsolatedPMT-PMTs)))) < pmtsize
    print(PMTs[distanceBool])
    break
    if len(PMTs[distanceBool])-1 >= YamlOccur:
      NumOfPMT += 1
  if NumOfPMT >= YamlPMTs:
    Count += 1
  break
break
print(Count)
