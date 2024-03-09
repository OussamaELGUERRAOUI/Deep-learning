import requests
from bs4 import BeautifulSoup
import os

def download_images_from_url(url, output_directory):
    # Créer le répertoire de sortie s'il n'existe pas déjà
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Faire la requête GET à l'URL
    response = requests.get(url)
    
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Créer un objet BeautifulSoup pour analyser le HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Trouver toutes les balises <img> qui contiennent des images
        img_tags = soup.find_all('img')
        
        # Télécharger chaque image trouvée
        for img_tag in img_tags:
            # Récupérer l'URL de l'image
            img_url = img_tag.get('src')
            
            # Télécharger l'image
            if img_url:
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    # Extraire le nom du fichier de l'URL de l'image
                    img_filename = os.path.join(output_directory, os.path.basename(img_url))
                    
                    # Enregistrer l'image dans le répertoire de sortie
                    with open(img_filename, 'wb') as img_file:
                        img_file.write(img_response.content)
                    print(f"Image téléchargée : {img_filename}")
                else:
                    print(f"Impossible de télécharger l'image depuis l'URL : {img_url}")
    else:
        print(f"La requête GET a échoué avec le code d'état : {response.status_code}")

# Exemple d'utilisation
url = "https://www.gettyimages.fr/photos/homme-qui-pleure"
output_directory = "images_logo_getty"
download_images_from_url(url, output_directory)
