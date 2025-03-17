<script setup>
import AddNewClockIn from '@/Components/AddNewClockIn.vue';
import UserActivities from '@/Components/Users/UserActivities.vue';
import UserActivityFilter from '@/Components/Users/UserActivityFilter.vue';
import UserInfo from '@/Components/Users/UserInfo.vue';
import AuthenticatedLayout from '@/Layouts/AuthenticatedLayout.vue';

</script>

<template>
    <AuthenticatedLayout>
        <div class="py-12">
            <div class="mx-auto max-w-7xl sm:px-6 lg:px-8">
                <div class="text-right mb-3">
                    <button class="btn btn-sm btn-info" data-toggle="modal" data-target="#addNewClockIn">
                        <i class="fa-regular fa-square-plus"></i> Cadastrar ponto manualmente
                    </button>
                </div>

                <div class="overflow-hidden bg-white shadow-sm sm:rounded-lg mb-3">
                    <div class="p-6 text-gray-900">
                        <h5 class="mb-4">Atividades registradas</h5>
                        <UserInfo />
                    </div>
                </div>

                <div class="overflow-hidden bg-white shadow-sm sm:rounded-lg">
                    <div class="p-6 text-gray-900">
                        <h5>Filtros</h5>
                        <UserActivityFilter />

                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Status</th>
                                    <th>Horário</th>
                                    <th>Dentro do horário</th>
                                    <th>Método de registro</th>
                                    <th>Ver foto</th>
                                </tr>
                            </thead>
                            <tbody>
                                <UserActivities/>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        <AddNewClockIn />
    </AuthenticatedLayout>
</template>
