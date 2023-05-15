from pytube import Youtube

link = input("Enter a link to download: ")
yt = Youtube(link)

print("Searching audio track.")

downloader = yt.streams.filter(only_audio=True).get_audio_only()
print("DOwnloading...")
downloader.download()
print("Finished downloading.")

