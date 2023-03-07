from Video import Video
import tkinter as tk

qualities = ['2160p', '1440p', '1080p', '720p', '480p', '360p', '240p', '144p']


def on_submit():
    # Récupère les valeurs saisies dans les entrées
    Video(entry.get())
    root.quit()


if __name__ == '__main__':
    # Crée une fenêtre de base
    root = tk.Tk()
    root.title("Download yt video")
    root.geometry("300x150")

    question = "Url : "
    entry = tk.Entry(root)

    label = tk.Label(root, text=question)
    label.pack()
    entry.pack()

    # Crée un bouton de soumission
    submit = tk.Button(root, text="Soumettre", command=on_submit)
    submit.pack()

    # Affiche la fenêtre
    root.mainloop()
