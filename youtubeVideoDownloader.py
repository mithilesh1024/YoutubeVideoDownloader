from pytube import YouTube

link = input("Enter link :")
yt = YouTube(link)

# Title of video
print("Title: ", yt.title)
# Number of views of video
print("Number of views: ", yt.views)
# Length of the video
print("Length of video: ", yt.length, "seconds")
# Description of video
#print("Description: ",yt.description)
# Rating
print("Ratings: ", yt.rating)

video = yt.streams.filter(progressive=True).first()
print(video)

# yt = yt.streams.get_by_itag('18')
print("Download...")
video.download()
print("\nDownload Completed!!")
