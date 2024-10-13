import os
import hashlib
import subprocess

def getImgRoute():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, 'irudia')

def computeMD5Hash(image_path):
    with open(image_path, 'rb') as f:
        img_data = f.read()
    return hashlib.md5(img_data).hexdigest()

def hash_images_in_directory(directory, known_hash):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(directory, filename)
            image_hash = computeMD5Hash(image_path)
            print(f"Image: {filename}, MD5 Hash: {image_hash}")
            if image_hash == known_hash:
                print(f"Match found: {filename}")
                return image_path


def main():
    img_directory = getImgRoute()
    known_md5_hash = "e5ed313192776744b9b93b1320b5e268"
    secret_img_path = hash_images_in_directory(img_directory, known_md5_hash)
    print(f"Secret image path: {secret_img_path}")

    # SECRET MESSAGE:
    # "Al Fascismo no se le discute, se le destruye." Buenaventura Durruti
    # Received by using the following command on the following directory:
    # /usr/share/stegosuite
    # java --add-exports java.base/sun.security.provider=ALL-UNNAMED -jar stegosuite-0.8.0.jar

if __name__ == "__main__":
    main()