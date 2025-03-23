<?php

namespace App\Http\Controllers;

use App\Http\Requests\CheckUserImageRequest;
use App\Services\FacecheckerService;
use Illuminate\Http\Request;
use Inertia\Inertia;

class ClockInController extends Controller
{
    public function __construct(
        private readonly FacecheckerService $service
    ) {}

    public function users()
    {
        return Inertia::render('ClockIn/Users');
    }

    public function usersHistory(int $id)
    {
        return Inertia::render('ClockIn/UserHistory');
    }

    public function checkUserImage(CheckUserImageRequest $request)
    {
        $user = $this->service->checkImage($request);
        return response()->json(['message' => $user]);
    }
}
