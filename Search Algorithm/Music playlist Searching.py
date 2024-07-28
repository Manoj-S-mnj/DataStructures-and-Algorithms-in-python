playlist =[
    {'songName':"usure nee thane","artist":"A.R.Rahman"},
    {"songName":"alagiya laila","artist":"A.R.Rahman"},
    {"songName":"oru naalil vaalkai","artist":"U1"},
    {'songName':'Kadharalz',"artist":"Anirudh"}
]

def searchBysongname(PL,TV):
    for song in PL:
        if song['songName'] == TV:
            return song
    return "Song in not found in the play List"

def searchByArtist(PL,TV):
    for song in PL:
        if song['artist'] == TV:
            return song
    return "Song in not found in the play List"


target = int(input("Search By : 1. Song Name 2.Artist \n Enter 1 or 2...."))
if target == 1:
    targetValue = input("Enter song Name : ")
    result = searchBysongname(playlist,targetValue)
elif target == 2:
    targetValue = input("Enter Artist Name : ")
    result = searchByArtist(playlist,targetValue)
else:
    print("Wrong Option")
print(result)
     


          

