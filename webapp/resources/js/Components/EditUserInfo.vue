<template>
    <div class="modal fade" id="editUserInfo" tabindex="-1" role="dialog" aria-labelledby="editUserInfoLabel"
        aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="editUserInfoLabel">Atualizar dados do usuário</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <form action="" enctype="multipart/form-data">
                        <div class="form-group">
                            <label for="name">Nome</label>
                            <input type="text" class="form-control">
                        </div>
                        <div class="form-group">
                            <label for="name">E-mail</label>
                            <input type="text" class="form-control">
                        </div>
                        <div class="form-group">
                            <label for="name">Foto</label>
                            <input type="file" class="form-control">
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary btn-sm" data-dismiss="modal">
                        Cancelar
                    </button>
                    <button type="button" class="btn btn-warning btn-sm">
                        <i class="fa-solid fa-pen-to-square"></i> Atualizar usuário
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>