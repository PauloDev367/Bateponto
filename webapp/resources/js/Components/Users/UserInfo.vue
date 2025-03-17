<template>
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
</template>