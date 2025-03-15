<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Inertia\Inertia;

class ClockInController extends Controller
{
    public function users()
    {
        return Inertia::render('ClockIn/Users');
    }
}
