from pytube import YouTube


class Video:
    def __init__(self, url):
        self.url = url

        print("Initialisation de l'objet YouTube")
        self.yt = YouTube(url)

        self.streams = self.yt.streams.filter()

        hr = self.get_highest_resolution()
        print(f"hr = {hr}")

        print("Séléction du nombre de fps max")
        self.video = self.streams.filter(resolution=hr).order_by('fps').last()

        self.download()

    def get_highest_resolution(self):
        print("Séléction de la meilleur qualité de la vidéo")
        return self.streams.order_by("resolution").last().resolution

    def download(self):
        print("Début du téléchargement")
        self.video.download()
        print("Fin du téléchargement")
