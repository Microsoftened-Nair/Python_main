def download_video():
    def progress(stream=None, chunk=None, remaining=None):
        file_size = stream.filesize
        p1 = (100 * (file_size - remaining)) / file_size

        for i in range(1, int(p1+1)):
            progressbar['value'] = p1
            l4.configure(text= 'Downloaded ' + str(round(p1,1)) + "%")
            root.update_idletasks()
            time.sleep(0.01)
            if p1 == 100:
                l4.configure(text='Done')

    link = entry.get()
    yt = YouTube(link, on_progress_callback=progress)

    if clicked.get() == '360p':
        stream = yt.streams.get_by_itag(18)
        stream.download(path)

    if clicked.get() == '720p':
        stream = yt.streams.get_by_itag(22)
        stream.download(path)

    if clicked.get() == 'Audio only':
        stream = yt.streams.get_by_itag(136)
        stream.download(path)
        wb.open_new_tab("https://convertio.co/mp4-mp3/")

    if clicked.get() == '360p video-only':
        stream = yt.streams.get_by_itag(243)
        stream.download(path)

    if clicked.get() == '720p video-only':
        stream = yt.streams.get_by_itag(247)
        stream.download(path)

    if clicked.get() == '1080p video-only':
        stream = yt.streams.get_by_itag(248)
        stream.download(path)