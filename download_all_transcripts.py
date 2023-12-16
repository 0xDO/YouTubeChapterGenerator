import scrapetube
from youtube_transcript_api import YouTubeTranscriptApi
from pprint import pprint


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


def clean_title(title):
    contraband = [':','/','\\','?','"']
    for c in contraband:
        title = title.replace(c,'')
    return title

# AI UCvKRFNawVcuz4b9ihUTApCg
# Neurospicy UCHDvy-B0O0zFHaD36gF90TQ
channel_id = 'UCHDvy-B0O0zFHaD36gF90TQ'
videos = scrapetube.get_channel(channel_id)
print(videos)


for video in videos:
    try:
        #print(video['title'])
        #print(video)
        transcript = YouTubeTranscriptApi.get_transcript(video['videoId'])
        text = [i['text'] for i in transcript]
        block = ' '.join(text)
        title = clean_title(video['title']['runs'][0]['text'])
        print(title)
        save_file('transcripts/%s.txt' % title, block)
    except Exception as oops:
        print(video['title'], oops)