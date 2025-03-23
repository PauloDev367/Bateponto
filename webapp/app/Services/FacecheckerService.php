<?php

namespace App\Services;

use App\Http\Requests\CreateUserRequest;
use CURLFile;
use Illuminate\Container\Attributes\Cache;
use Illuminate\Support\Facades\Cache as FacadesCache;
use Symfony\Component\HttpFoundation\Exception\BadRequestException;
use Symfony\Component\HttpKernel\Exception\BadRequestHttpException;
use Symfony\Component\HttpKernel\Exception\NotFoundHttpException;

class FacecheckerService
{
    private string $baseUrl;
    private string $accessToken;

    public function __construct()
    {
        $this->baseUrl = env('FACECHECKER_API_BASE_URL');
        $this->login();
    }

    private function login()
    {
        $this->accessToken = FacadesCache::remember('facechecker_api_token', now()->addMinutes(10), function () {
            $email = env('FACECHECKER_API_EMAIL');
            $pass = env('FACECHECKER_API_PASS');

            $data = [
                'email' => $email,
                'password' => $pass,
            ];

            $curl = curl_init();

            curl_setopt_array($curl, array(
                CURLOPT_URL => $this->baseUrl . '/auth/login/',
                CURLOPT_RETURNTRANSFER => true,
                CURLOPT_ENCODING => '',
                CURLOPT_MAXREDIRS => 10,
                CURLOPT_TIMEOUT => 0,
                CURLOPT_FOLLOWLOCATION => true,
                CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
                CURLOPT_CUSTOMREQUEST => 'POST',
                CURLOPT_POSTFIELDS => json_encode($data),
                CURLOPT_HTTPHEADER => array(
                    'Content-Type: application/json'
                ),
            ));

            $response = curl_exec($curl);

            curl_close($curl);
            $data = json_decode($response, true);
            if (!isset($data['access_token'])) {
                throw new NotFoundHttpException('Erro ao tentar fazer login');
            }

            return $data['access_token'];
        });
    }

    public function registerUser(CreateUserRequest $request)
    {
        $profilePicture = $request->file('file');

        $data = [
            'email' => $request->email,
            'name' => $request->name,
            'password' => uniqid() . uniqid(),
            'profile_picture' => new CURLFile($profilePicture->getPathname(), $profilePicture->getMimeType(), $profilePicture->getClientOriginalName())
        ];

        $curl = curl_init();

        curl_setopt_array($curl, [
            CURLOPT_URL => $this->baseUrl . '/auth/register/',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $data,
            CURLOPT_HTTPHEADER => [
                'Content-Type: multipart/form-data',
                'Authorization: Bearer ' . $this->accessToken
            ],
        ]);

        $response = curl_exec($curl);

        curl_close($curl);

        $data = json_decode($response, true);
        if (!isset($data['message'])) {
            throw new BadRequestHttpException('Dados inválidos! Verifique se o usuário está cadastrado no sistema');
        }
    }


    public function checkImage() {}
}
