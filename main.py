import segno


def main():
    qrcode = segno.make_qr("Hello Hello Bandung, ibu kota Jawa Barat, sudah lama beta")
    qrcode.save(
        "qr_pertamaku.png",
        scale=10,
        border=5,
        data_light="lightyellow",
        data_dark="darkgreen",
    )


if __name__ == "__main__":
    main()
