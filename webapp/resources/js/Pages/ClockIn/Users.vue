<script setup>
import AuthenticatedLayout from '@/Layouts/AuthenticatedLayout.vue';
import AddNewUser from '@/Components/AddNewUser.vue';
import EditUserInfo from '@/Components/EditUserInfo.vue';
import UserTr from '@/Components/Users/UserTr.vue';
</script>

<template>
    <AuthenticatedLayout>
        <div class="py-12">
            <div class="mx-auto max-w-7xl sm:px-6 lg:px-8">
                <div class="text-right mb-3">
                    <button class="btn btn-sm btn-info" data-toggle="modal" data-target="#addNewUser">
                        <i class="fa-regular fa-square-plus"></i> Cadastrar usuário
                    </button>
                </div>
                <div class="overflow-hidden bg-white shadow-sm sm:rounded-lg">
                    <div class="p-6 text-gray-900">
                        <h5 class="mb-4">Usuários registrados</h5>

                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Nome</th>
                                    <th>E-mail</th>
                                    <th>Data de cadastro</th>
                                    <th>Foto de perfil</th>
                                    <th>Ações</th>
                                </tr>
                            </thead>
                            <tbody>
                                <UserTr />
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>


            <AddNewUser />
            <EditUserInfo />

        </div>
    </AuthenticatedLayout>
</template>
