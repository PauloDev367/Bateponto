import face_recognition
import numpy as np
from faceverifier.models import ApplicationUser
from urllib.request import urlopen
from io import BytesIO

class FaceCheck:
    def __init__(self):
        self.users = ApplicationUser.objects.all()
        self.registered_faces, self.registered_names = self.__load_registered_faces()
    
    def __load_registered_faces(self):
        registered_faces = []
        nomes = []

        for usuario in self.users:
            if usuario.profile_picture:
                url_imagem = usuario.profile_picture.url
                
                with urlopen(url_imagem) as response:
                    imagem_bytes = response.read()
                    imagem_stream = BytesIO(imagem_bytes)
                
                imagem = face_recognition.load_image_file(imagem_stream)
                
                codificacoes = face_recognition.face_encodings(imagem)
                
                if codificacoes:
                    registered_faces.append(codificacoes[0])
                    nomes.append(usuario.username)

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
