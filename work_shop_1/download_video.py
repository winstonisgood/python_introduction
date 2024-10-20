from pytube import YouTube

# Step 1: Specify the YouTube video URL
url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

# Step 2: Create a YouTube object
yt = YouTube(url)

# Step 3: Display video details
print(f'Title: {yt.title}')
print(f'Views: {yt.views}')
print(f'Duration: {yt.length} seconds')

# Step 4: Get the highest resolution stream available
stream = yt.streams.get_highest_resolution()

# Step 5: Download the video
stream.download('/path/to/download/directory')  # Replace with your path
print("Download completed!")
