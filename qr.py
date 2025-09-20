import qrcode

def make_qr(url: str, filename: str = "qrcode.png"):
    """
    Erstellt einen QR-Code für die angegebene URL und speichert ihn als PNG.

    :param url: Die Webseite-URL
    :param filename: Dateiname für den gespeicherten QR-Code
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR-Code gespeichert unter: {filename}")

# Beispiel:
if __name__ == "__main__":
    website = input("Gib eine URL ein: ")
    make_qr(website, "mein_qrcode.png")
