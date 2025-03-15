import face_recognition
import numpy as np

class FaceCheck:
    def __init__(self, users):
        """Inicializa a classe com um banco de dados simulado."""
        self.users = users
        self.registered_faces, self.registered_names = self.__load_registered_faces()
    
    def __load_registered_faces(self):
        """Carrega e codifica todas as imagens cadastradas no banco de dados."""
        registered_faces = []
        nomes = []
        
        for usuario in self.users:
            caminho_imagem = usuario["foto_cadastrada"]
            imagem = face_recognition.load_image_file(caminho_imagem)
            codificacoes = face_recognition.face_encodings(imagem)
            
            if codificacoes:
                registered_faces.append(codificacoes[0])
                nomes.append(usuario["nome"])
        
        return registered_faces, nomes
    
    def verificar_rosto(self, imagem_teste):
        """Verifica se o rosto na imagem de teste corresponde a algum do sistema."""
        imagem = face_recognition.load_image_file(imagem_teste)
        codificacoes_teste = face_recognition.face_encodings(imagem)
        
        if not codificacoes_teste:
            print("Nenhum rosto encontrado na imagem de teste.")
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

# Exemplo de uso:
# if __name__ == "__main__":
#     exemplo_users = [
#         {"id": 1, "nome": "Paulo Silva", "foto_cadastrada": "fotos/1.jpeg"},
#         {"id": 2, "nome": "Antonio Calabresa", "foto_cadastrada": "fotos/2.jpg"}
#     ]
    
#     face_checker = FaceCheck(exemplo_users)
#     imagem_teste = "verificar/2.jpg"
#     nome_encontrado = face_checker.verificar_rosto(imagem_teste)
    
#     if nome_encontrado:
#         print(f"Rosto identificado: {nome_encontrado}")
#     else:
#         print("Rosto não cadastrado no sistema.")
