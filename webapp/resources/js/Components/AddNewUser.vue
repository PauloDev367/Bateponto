<template>
    <div class="modal fade" id="addNewUser" tabindex="-1" role="dialog" aria-labelledby="addNewUserLabel"
        aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="addNewUserLabel">Adicionar novo usuário</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <form :action="route('user.register')" method="POST" @submit.prevent="submit" enctype="multipart/form-data">
                    <div class="modal-body">
                        <div class="form-group">
                            <label for="name">Nome</label>
                            <input type="text" v-model="form.name" id="name" class="form-control">
                        </div>
                        <div class="form-group">
                            <label for="email">E-mail</label>
                            <input type="text" v-model="form.email" id="email" class="form-control">
                        </div>
                        <div class="form-group">
                            <label for="name">Foto</label>
                            <input type="file" @change="handleFileUpload" id="file" class="form-control">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary btn-sm" data-dismiss="modal">
                            Cancelar
                        </button>
                        <button type="submit" class="btn btn-info btn-sm">
                            <i class="fa-regular fa-square-plus"></i> Cadastrar usuário
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useToastr } from '@/Services/toastr';
import { useForm } from '@inertiajs/vue3';

const form = useForm({
    email: '',
    name: '',
    file: null, 
});
const toastr = useToastr();

const submit = () => {
    const formData = new FormData();
    formData.append('name', form.name);
    formData.append('email', form.email);
    if (form.file) {
        formData.append('file', form.file);
    }

    form.post(route('user.register'), {
        forceFormData: true,
        onError: ()=>{
            toastr.error('Erro ao tentar cadastrar usuário. Verifique se ele já não está cadastrado no sistema.');
        },
        onSuccess: ()=>{
            toastr.success('Usuário cadastrado com sucesso');
            form.email = '';
            form.name = '';
        }
    });
};

const handleFileUpload = (event) => {
    form.file = event.target.files[0];
};
</script>
