<?php

namespace App\Services;

use App\Http\Requests\CreateUserRequest;
use App\Models\User;
use App\Services\FacecheckerService;

class UserService
{
    public function __construct(
        private readonly FacecheckerService $facecheckerService
    ) {}

    public function registerNewUser(CreateUserRequest $request)
    {
        $this->facecheckerService->registerUser($request);
        $user = new User();
        $user->name = $request->name;
        $user->email = $request->email;
        $user->password = bcrypt(uniqid() . uniqid() . uniqid());
        $user->save();
    }
}
