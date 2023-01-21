"""
 Citește din input-ul consolei numele, prenumele și numărul de telefon al utilizatorului și generează
 un cod QR corespunzător transpunerii informațiilor în formatul vCard

 Pentru a rula codul:
 1) Clonează acest repository
 2) Din directorul `pyqrcode` rulează comanda `pipenv install`
 3) Apoi rulează comanda  `pipenv shell`
 4) Din acest shell rulează `python3 main.py`
"""
import pyqrcode
from subprocess import run


def generateVcard(fname, lname="", tel=""):
    """
    Generează vCard din informațiile trimise

    :param str fname: primul nume
    :param str lname: al doilea nume
    :param str tel: telefon
    :return: str
    """
    return "\n".join([
        "BEGIN:VCARD",
        f"FN:{fname} {lname}",
        f"TEL;TYPE=cell:{tel}",
        "END:VCARD"
    ])


def generateQrCode(content, filename='qrcode.png', encoding='utf-8'):
    """
    Generează un cod QR din conținut și îl salvează pe disc ca fișier png.
    Pentru compatibilitate include extensia. Returnează numele fișierului salvat.

    :param str content: conținut
    :param str filename: nume de fișier
    :param str encoding: codarea specifică caracterelor din conținut (implicit utf-8)
    :return: str
    """
    qrcode = pyqrcode.create(content, encoding=encoding)
    qrcode.png(file=filename)

    return filename


if __name__ == '__main__':

    # Tuplu cu lista de întrebări (input)
    questions = ("Nume: ", "Prenume: ", "Tel: ")
    # Listă cu răspunsuri (input)
    answers = []

    for q in questions:
        reply = input(q)
        answers.append(q + " " + reply)

    # Generază vCard pe baza răspunsurilor primite
    vcard = generateVcard(answers[1], answers[0], answers[2])

    # Generează și salvează codul QR sub forma unui fișier
    qrcodePath = generateQrCode(vcard, filename='./qrcode.png', encoding='ISO-8859-16')

    # Deschide fișierul folosind utilitarul "open" (specific MacOS)
    run(["open", qrcodePath])
