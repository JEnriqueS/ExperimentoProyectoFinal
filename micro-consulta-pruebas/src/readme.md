<!-- inside src folder -->

<!-- env creation -->
python -m venv venv
<!-- activate -->
venv\Scripts\Activate.ps1
<!-- deactivate -->
deactivate
<!-- install package -->
python -m pip install <package>
<!-- run -->
python -m flask run

<!-- json body with random variables for postman test -->

{
    "numid_nacional":"{{$guid}}",
    "nombres":"{{$randomFirstName}} {{$randomFirstName}}",
    "apellidos":"{{$randomLastName}} {{$randomLastName}}",
    "telefono":"{{$randomPhoneNumber}}",
    "direccional":"{{$randomStreetAddress}}",
    "edad":{{$randomInt}},
    "ubicacion_geografica":"{{$randomCountry}}",
    "idiomas":"{{$randomLocale}}",
    "id_estado":1
}

<!-- Docker commands -->
docker build -t consulta:v1 .
docker run --env-file .env -d -p 5000:5000 consulta:v1