<script setup>
import AddNewUser from '@/Components/AddNewUser.vue';
import LastActivitiesTr from '@/Components/Dashboard/LastActivitiesTr.vue';
import AuthenticatedLayout from '@/Layouts/AuthenticatedLayout.vue';

import { Head } from '@inertiajs/vue3';
</script>

<template>

    <Head title="Dashboard" />

    <AuthenticatedLayout>
        <template #header>
            <h2 class="text-xl font-semibold leading-tight text-gray-800">
                Dashboard
            </h2>
        </template>

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
                                    <th>Status</th>
                                    <th>Horário</th>
                                    <th>Dentro do horário</th>
                                    <th>Método de registro</th>
                                    <th>Ver foto</th>
                                </tr>
                            </thead>
                            <tbody>



                                <LastActivitiesTr/>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <AddNewUser />
        </div>
    </AuthenticatedLayout>
</template>
