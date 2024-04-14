import secrets


def enc(file_name: str):
    file_size = 0
    with open(file_name, 'rb') as f:
        with open(file_name + '.load', 'ab+') as mirror:
            with open(file_name + '.key', 'ab+') as key:
                mirror.seek(2)
                key.seek(2)

                while bys := f.read(1024):
                    file_size += len(bys)
                    rdm_bytes = secrets.token_bytes(len(bys))
                    enc_bytes = bytes(a ^ b for a, b in zip(bys, rdm_bytes))
                    mirror.write(enc_bytes)
                    key.write(rdm_bytes)
    print(f"One-time Padding Encryption Finished! File Size: {file_size / 1024.0 / 1024.0} MB")


def dec(enc_file_name: str, key_file_name: str, out_file_name: str):
    file_size = 0
    with open(enc_file_name, 'rb') as f:
        with open(key_file_name, 'rb') as key:
            with open(out_file_name, 'ab+') as out:
                while bys := f.read(1024):
                    file_size += len(bys)
                    key_bytes = key.read(len(bys))
                    dec_bytes = bytes(a ^ b for a, b in zip(bys, key_bytes))
                    out.write(dec_bytes)
    print(f"One-time Padding Decryption Finished! File Size: {file_size / 1024.0 / 1024.0}")


if __name__ == '__main__':
    encryption_input_file_name = "xxx.xxx"
    enc_file_name = encryption_input_file_name + ".load"
    key_file_name = encryption_input_file_name + ".key"
    out_file_name = "otd_" + encryption_input_file_name
    enc(encryption_input_file_name)
    dec(enc_file_name, key_file_name, out_file_name)
