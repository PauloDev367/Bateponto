<script setup>
import AuthenticatedLayout from '@/Layouts/AuthenticatedLayout.vue';
import AddNewUser from '@/Components/AddNewUser.vue';
import EditUserInfo from '@/Components/EditUserInfo.vue';
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
                        <h5 class="mb-4">Últimas atividades registradas</h5>

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
                                <tr>
                                    <td>
                                        <a href="#" class="text-info">
                                            <i class="fa-solid fa-magnifying-glass"></i>
                                            José
                                        </a>
                                    </td>
                                    <td>jose@email.com</td>
                                    <td>01/02/2024 00:00:00</td>
                                    <td>
                                        <a href="#" class="btn btn-sm btn-outline-success">
                                            <i class="fa-solid fa-image"></i>
                                        </a>
                                    </td>
                                    <td>
                                        <a href="#" class="btn btn-sm btn-outline-warning mr-2"
                                        data-toggle="modal" data-target="#editUserInfo">
                                            <i class="fa-solid fa-pen-to-square"></i>
                                        </a>
                                        <a href="#" class="btn btn-sm btn-outline-danger">
                                            <i class="fa-solid fa-trash-can"></i>
                                        </a>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <a href="#" class="text-info">
                                            <i class="fa-solid fa-magnifying-glass"></i>
                                            José
                                        </a>
                                    </td>
                                    <td>jose@email.com</td>
                                    <td>01/02/2024 00:00:00</td>
                                    <td>
                                        <a href="#" class="btn btn-sm btn-outline-success">
                                            <i class="fa-solid fa-image"></i>
                                        </a>
                                    </td>
                                    <td>
                                        <a href="#" class="btn btn-sm btn-outline-warning mr-2"
                                        data-toggle="modal" data-target="#editUserInfo">
                                            <i class="fa-solid fa-pen-to-square"></i>
                                        </a>
                                        <a href="#" class="btn btn-sm btn-outline-danger">
                                            <i class="fa-solid fa-trash-can"></i>
                                        </a>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <a href="#" class="text-info">
                                            <i class="fa-solid fa-magnifying-glass"></i>
                                            José
                                        </a>
                                    </td>
                                    <td>jose@email.com</td>
                                    <td>01/02/2024 00:00:00</td>
                                    <td>
                                        <a href="#" class="btn btn-sm btn-outline-success">
                                            <i class="fa-solid fa-image"></i>
                                        </a>
                                    </td>
                                    <td>
                                        <a href="#" class="btn btn-sm btn-outline-warning mr-2"
                                        data-toggle="modal" data-target="#editUserInfo">
                                            <i class="fa-solid fa-pen-to-square"></i>
                                        </a>
                                        <a href="#" class="btn btn-sm btn-outline-danger">
                                            <i class="fa-solid fa-trash-can"></i>
                                        </a>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <a href="#" class="text-info">
                                            <i class="fa-solid fa-magnifying-glass"></i>
                                            José
                                        </a>
                                    </td>
                                    <td>jose@email.com</td>
                                    <td>01/02/2024 00:00:00</td>
                                    <td>
                                        <a href="#" class="btn btn-sm btn-outline-success">
                                            <i class="fa-solid fa-image"></i>
                                        </a>
                                    </td>
                                    <td>
                                        <a href="#" class="btn btn-sm btn-outline-warning mr-2"
                                        data-toggle="modal" data-target="#editUserInfo">
                                            <i class="fa-solid fa-pen-to-square"></i>
                                        </a>
                                        <a href="#" class="btn btn-sm btn-outline-danger">
                                            <i class="fa-solid fa-trash-can"></i>
                                        </a>
                                    </td>
                                </tr>
                                
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
