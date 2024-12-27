def nyetak(*args, **kwargs):
    """print() diganti nyetak()."""
    print(*args, **kwargs)


def dowo(objek):
    """len() diganti dowo()."""
    count = 0
    for _ in objek:
        count += 1
    return count


def jenis(objek):
    """type() diganti jenis()."""
    return objek.__class__


class Pemisah:
    def __init__(self, teks):
        self.teks = teks

    def misah(self, sep=None, maxsplit=-1):
        """split() diganti misah()."""
        if sep is None:
            # Split on any whitespace and discard empty strings
            hasil = []
            bagian = ""
            hitung = 0

            for karakter in self.teks:
                if karakter.isspace():
                    if bagian:  # Only add non-empty parts
                        hasil.append(bagian)
                        bagian = ""
                    if maxsplit != -1 and hitung >= maxsplit:
                        break
                else:
                    bagian += karakter

            # Add the last part if not empty
            if bagian:
                hasil.append(bagian)

            return hasil
        else:
            # Split using the specified separator
            hasil = []
            bagian = ""
            hitung = 0
            sep_len = len(sep)

            for i in range(len(self.teks)):
                if self.teks.startswith(sep, i):
                    if bagian:
                        hasil.append(bagian)
                        bagian = ""
                        hitung += 1
                        if maxsplit != -1 and hitung >= maxsplit:
                            break
                    i += sep_len - 1  # Skip the separator length
                else:
                    bagian += self.teks[i]

            # Add the last part if not empty
            if bagian:
                hasil.append(bagian)

            return hasil


def main():
    teks1 = "woi jawa lu sok asix"
    pemisah = Pemisah(teks1)

    nyetak("Hasil pemisahan:", pemisah.misah())
    nyetak("Jumlah kata:", dowo(pemisah.misah()))
    nyetak("Tipe objek:", jenis(pemisah))


if __name__ == "__main__":
    main()
