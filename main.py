from TikTokApi import TikTokApi

# Thanks for downloading this repo

print("TikTok Downloader")
print("=================")
print("")
video_url = input("Video URL: ")
video_name = input("Video Name (file_name): ")
# get the video id from the url
video_id = video_url.split("/")[-1]
video_id = video_id.split("?")[0]
video_id = video_id.split("#")[0]

print("Downloading video...")

with TikTokApi() as api:
    video = api.video(id=f"{video_id}")
    video_data = video.bytes()
    with open(f"./videos/{video_name}.mp4", "wb") as out_file:
        out_file.write(video_data)
        print(f"Video saved to /videos/{video_name}.mp4")

print("Done!")
print("")
print("Press enter to exit...")
input()
exit()
# end of main.py
