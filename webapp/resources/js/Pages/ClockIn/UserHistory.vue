<script setup>
import AddNewClockIn from '@/Components/AddNewClockIn.vue';
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
                        <div class="row align-items-center">
                            <div class="col-12 col-md-4">
                                <img src="https://julianafonte.com.br/wp-content/uploads/2018/02/dermato-estetica-macas-do-rosto-750x500.jpg"
                                    class="user-page-image" alt="Foto do usuário">
                            </div>

                            <div class="col-12 col-md-8">
                                <div class="form-group">
                                    <label>Nome:</label>
                                    <input type="text" class="form-control" readonly value="Nome da Silva">
                                </div>
                                <div class="form-group">
                                    <label>E-mail:</label>
                                    <input type="text" class="form-control" readonly value="email@email.com">
                                </div>
                                <div class="form-group">
                                    <label>Data de Cadastrado:</label>
                                    <input type="text" class="form-control" readonly value="Cadastrado: 01/02/2023">
                                </div>
                                <div class="form-group">
                                    <label class="mr-2">Status da conta:</label>
                                    <span class="badge badge-success">Ativada</span>
                                </div>

                                <div class="mt-3 text-right">
                                    <button class="btn btn-sm btn-danger">
                                        <i class="fa-solid fa-ban"></i> Desativar conta
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="overflow-hidden bg-white shadow-sm sm:rounded-lg">
                    <div class="p-6 text-gray-900">
                        <h5>Filtros</h5>
                        <form action="" class="mb-3">
                            <div class="row">
                                <div class="col-12 col-md-4">
                                    <div class="form-group">
                                        <label>Dentro do horário</label>
                                        <select name="" id="" class="form-control">
                                            <option selected disabled>Selecionar</option>
                                            <option value="">Dentro do horário</option>
                                            <option value="">Fora do horário</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="col-12 col-md-4">
                                    <div class="form-group">
                                        <label>Status</label>
                                        <select name="" id="" class="form-control">
                                            <option selected disabled>Selecionar</option>
                                            <option value="">Confirmado</option>
                                            <option value="">Confirmado por um admin</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="col-12 col-md-4">
                                    <div class="form-group">
                                        <label>Método de registro</label>
                                        <select name="" id="" class="form-control">
                                            <option selected disabled>Selecionar</option>
                                            <option value="">Foto</option>
                                            <option value="">Manual</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="col-12 text-right">
                                    <button class="btn btn-sm btn-secondary">
                                        <i class="fa-solid fa-filter"></i> Filtrar
                                    </button>
                                </div>
                            </div>
                        </form>


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
                                <tr>
                                    <td><span class="badge badge-success"> Confirmado </span></td>
                                    <td>01/02/2024 09:00:00</td>
                                    <td>
                                        <span class="badge badge-success">
                                            Dentro do horário
                                        </span>
                                    </td>
                                    <td>
                                        <span class="badge badge-secondary">
                                            Foto
                                        </span>
                                    </td>

                                    <td>
                                        <a href="#" class="btn btn-sm btn-outline-info">
                                            <i class="fa-solid fa-eye"></i>
                                        </a>
                                    </td>
                                </tr>

                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        <AddNewClockIn />
    </AuthenticatedLayout>
</template>
