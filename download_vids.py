from pytube import Channel
import os

def  download_vids(channel: Channel) -> None:
    save_path = os.getcwd() + channel.channel_name
    i = 0
    print(len(channel.videos))
    for video in channel.videos:
        print(f'video name: {video.title}')
        if i == 2:
            break
        video.streams.first().download()
        i += 1

def main():
    c = Channel('https://www.youtube.com/c/joerogan')
    download_vids(c)
    # print(f"Videos_url: {len(c.video_urls)}")

    # print(f"Downloading videos by: {c.channel_name}")
    # print(len(c.video_urls))
    # for url in c.video_urls[:3]:
    #     print(url)

if __name__ == "__main__":
    main()