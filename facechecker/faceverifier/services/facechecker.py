import os
import face_recognition
import numpy as np
from faceverifier.models import ApplicationUser
from urllib.request import urlopen
from io import BytesIO
import time


CACHE_DIR = "/tmp/faces_cache"
CACHE_TIME = 1 * 60 * 60

class FaceCheck:
    def __init__(self):
        self.users = ApplicationUser.objects.all()
        self.__limpar_cache_expirado()
        self.registered_faces, self.registered_names = self.__load_registered_faces()

    def __limpar_cache_expirado(self):
        if not os.path.exists(CACHE_DIR):
            os.makedirs(CACHE_DIR)
            return

        now = time.time()
        for filename in os.listdir(CACHE_DIR):
            filepath = os.path.join(CACHE_DIR, filename)
            if os.path.isfile(filepath) and (now - os.path.getmtime(filepath)) > CACHE_TIME:
                os.remove(filepath)

    def __load_registered_faces(self):
        registered_faces = []
        nomes = []

        for usuario in self.users:
            if usuario.profile_picture:
                image_filename = f"{CACHE_DIR}/{usuario.username}.jpg"

                if not os.path.exists(image_filename):
                    url_imagem = usuario.profile_picture.url
                    with urlopen(url_imagem) as response:
                        with open(image_filename, "wb") as f:
                            f.write(response.read())

                imagem = face_recognition.load_image_file(image_filename)
                codificacoes = face_recognition.face_encodings(imagem)

                if codificacoes:
                    registered_faces.append(codificacoes[0])
                    nomes.append(usuario.name)

        return registered_faces, nomes

    def verificar_rosto(self, imagem_teste):
        imagem = face_recognition.load_image_file(imagem_teste)
        codificacoes_teste = face_recognition.face_encodings(imagem)

        if not codificacoes_teste:
            return None

        rosto_teste = codificacoes_teste[0]
        resultados = face_recognition.compare_faces(self.registered_faces, rosto_teste)
        distancias = face_recognition.face_distance(self.registered_faces, rosto_teste)

        if True in resultados:
            indice = np.argmin(distancias)
            limite_distancia = 0.6
            if distancias[indice] < limite_distancia:
                return self.registered_names[indice]

        return None
