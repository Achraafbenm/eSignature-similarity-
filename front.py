import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os
import cv2
from numpy import result_type
from back import match


Seuil_de_tolerance = 80

def browsefunc(ent):
    filename = askopenfilename(filetypes=([
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
    ]))
    ent.delete(0, tk.END)
    ent.insert(tk.END, filename)  




def checkSimilarity(window, path1, path2):
    result = match(path1=path1, path2=path2)
    if(result <= Seuil_de_tolerance):
        messagebox.showerror("Échec : Signatures Do Not Match",
                             "Signatures sont à "+str(result)+f" % similaires!")
        pass
    else:
        messagebox.showinfo("Succés: Signatures Match",
                            "Signatures sont à "+str(result)+f" % similaires!")
    return True


root = tk.Tk()
root.title("Vérification de la similarité des signatures")
root.geometry("800x800")  
uname_label = tk.Label(root, text="Comparaison: Insérez SVP les deux signatures", font=10)
uname_label.place(x=90, y=50)

img1_message = tk.Label(root, text="Signature Numéro 1", font=10)
img1_message.place(x=10, y=120)

image1_path_entry = tk.Entry(root, font=10)
image1_path_entry.place(x=180, y=120)


img1_browse_button = tk.Button(
    root, text="Parcourir", font=10, command=lambda: browsefunc(ent=image1_path_entry))
img1_browse_button.place(x=400, y=120)

image2_path_entry = tk.Entry(root, font=10)
image2_path_entry.place(x=180, y=240)

img2_message = tk.Label(root, text="Signature Numéro 2", font=10)
img2_message.place(x=10, y=240)


img2_browse_button = tk.Button(
    root, text="Parcourir", font=10, command=lambda: browsefunc(ent=image2_path_entry))
img2_browse_button.place(x=400, y=240)

compare_button = tk.Button(
    root, text="Comparer", font=10, command=lambda: checkSimilarity(window=root,
                                                                   path1=image1_path_entry.get(),
                                                                   path2=image2_path_entry.get(),))

compare_button.place(x=200, y=320)
root.mainloop()
