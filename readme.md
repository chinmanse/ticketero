# Puesta en marcha
## Contenedores
### Configuraciones
Antes de nada se debe crear los archivos de entorno, estos se encuentran en la siguiente ruta:
```
compose/envs
```
En esta carpeta se encuentan archivos de ejemplo con las variables a configurar.
### Puesta en marcha
Para la puesta en marcha de los contenedores se debe seguir el siguiente procedimiento:
- En una terminal ejecutar el siguiente comando
```bash
docker compose -f docker-compose.yml up -d
```
En caso de tener un error verificar los siguiente
- Tener instalador docker, para esto ejecutar el siguiente comando
```bash
docker --version
```
- En caso de tener instalado una version antigua de docker es probable que se tenga que hacer uso del comando con un -
```bash
docker-compose -f docker-compose.yml up -d
```
# Base de datos
En la carpeta ```compose/db``` se puede encontrar un archivo ```struct_db.sql``` el cual contiene la estructura de la base de datos.

Importar el archivo ```struct_db.sql``` al contenedor de la base de datos ```tk_db```.

# Ejecucion
El unico contenedor que requiere una accion extra es ```tk_front```. Por lo que en la carpeta front ejecutar el siguiente comando:
```bash
npm install --force
```
Y reniciar el contenedor ```tk_front```
```bash
docker restart tk_front
```
Ahora el frontend estara corriendo en el puerto 3000, el back en el puerto 8000 y la base de datos puede ser accedida desde el puesto 54331

## Ingreso
Para ingresar solo debe dirigirse a la siguiente url:
```url
http://localhost:3000
```
Lo primero que vera sera un listado de usuarios, este listado funciona como un login al que en cuanto uno ingresa puede registrar tickets a nombre del mismo, y tambien responder y terminar o rechazar los tickets.