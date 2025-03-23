<?php

namespace App\Http\Controllers;

use App\Http\Requests\CreateUserRequest;
use App\Services\UserService;

class RegisterUserController
{
    public function __construct(
        private readonly UserService $userService
    ) {}

    public function register(CreateUserRequest $request)
    {
        try {
            $this->userService->registerNewUser($request);
            return back();
        } catch (\Throwable $th) {
            return back()->withErrors(['error' => 'Erro ao tentar cadastrar usuário']);
        }
    }
}
