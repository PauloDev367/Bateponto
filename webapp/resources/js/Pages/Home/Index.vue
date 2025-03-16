<template>
    <main class="home-area">
        <div class="container">
            <div class="row">
                <div class="col-12 text-center">
                    <h1>Bate ponto</h1>
                </div>

                <div class="col-12">
                    <div class="camera">
                        <video ref="video" v-show="isCameraOn" autoplay></video>
                        <canvas ref="canvas"></canvas>
                        <div v-if="isCameraOn" class="overlay">Centralize e aproxime seu rosto</div>
                    </div>

                    <div class="area-buttons">
                        <button class="btn mr-3" :class="(isCameraOn ? 'btn-danger' : 'btn-info')"
                            @click="toggleCamera">
                            {{ isCameraOn ? "Desligar Câmera" : "Ligar Câmera" }}
                        </button>

                        <button @click="captureImage" data-toggle="modal" data-target="#modalEnviarFoto"
                            class="btn btn-secondary" :disabled="!isCameraOn">
                            Capturar
                        </button>
                    </div>

                    <div v-if="capturedImage">
                        <h3>Foto Capturada:</h3>

                    </div>
                </div>
            </div>


        </div>
    </main>

    <div class="modal fade" id="modalEnviarFoto" tabindex="-1" role="dialog" aria-labelledby="modalEnviarFotoLabel"
        aria-hidden="true" data-backdrop="static" data-keyboard="false">

        <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="modalEnviarFotoLabel">Foto capturada</h5>
                    <!-- Removendo o botão de fechar (×) -->
                </div>
                <div class="modal-body">
                    <img :src="capturedImage" alt="Captura" class="w-100" />
                </div>
                <div class="modal-footer">
                    <button type="button" @click="cancelClockIn" class="btn btn-sm btn-secondary"
                        data-dismiss="modal">Cancelar</button>
                    <button type="button" class="btn btn-sm btn-info">Bater ponto</button>
                </div>
            </div>
        </div>
    </div>





</template>

<script setup>
import { ref } from "vue";

const video = ref(null);
const canvas = ref(null);
const capturedImage = ref(null);
const isCameraOn = ref(false);
let stream = null;

const startCamera = async () => {
    try {
        stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.value.srcObject = stream;
        isCameraOn.value = true;
    } catch (error) {
        console.error("Erro ao acessar a câmera:", error);
    }
};

const stopCamera = () => {
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
        isCameraOn.value = false;
    }
};

const toggleCamera = () => {
    if (isCameraOn.value) {
        stopCamera();
    } else {
        startCamera();
    }
};

const captureImage = () => {
    if (!isCameraOn.value) return;

    const ctx = canvas.value.getContext("2d");
    canvas.value.width = video.value.videoWidth;
    canvas.value.height = video.value.videoHeight;
    ctx.drawImage(video.value, 0, 0, canvas.value.width, canvas.value.height);
    capturedImage.value = canvas.value.toDataURL("image/png");
};

const cancelClockIn = () => {
    window.location.reload();
}
</script>


<style scoped></style>