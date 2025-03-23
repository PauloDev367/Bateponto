<?php

use Inertia\Inertia;
use Illuminate\Support\Facades\Route;
use Illuminate\Foundation\Application;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\ClockInController;
use App\Http\Controllers\ProfileController;
use App\Http\Controllers\RegisterUserController;

// Route::get('/', function () {
//     return Inertia::render('Welcome', [
//         'canLogin' => Route::has('login'),
//         'canRegister' => Route::has('register'),
//         'laravelVersion' => Application::VERSION,
//         'phpVersion' => PHP_VERSION,
//     ]);
// });

Route::get('/', [HomeController::class, 'index'])
    ->name('home');

Route::get('/users', [ClockInController::class, 'users'])
    ->name('users');
    
Route::get('/users/{id}', [ClockInController::class, 'usersHistory'])
    ->name('users.history');

Route::get('/dashboard', function () {
    return Inertia::render('Dashboard');
})->middleware(['auth', 'verified'])->name('dashboard');

Route::post('/clock-in', [ClockInController::class, 'checkUserImage'])->name('clockin');

Route::middleware('auth')->group(function () {
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');

    Route::post('/users/register', [RegisterUserController::class, 'register'])->name('user.register');
});

require __DIR__.'/auth.php';
