## Tarea3: Manipulación Avanzada en Git
Alumno: Carlos Javier Oliva Domínguez
N. Lista: 26

###Ejercicio 1:
#### Descripción de la tarea
- Mostrar el historial de cambios del repositorio.
- Crear la carpeta capítulos y crear dentro de ella el fichero capitulo1.txt con el siguiente texto.
    ```
    - Git es un sistema de control de versiones ideado por Linus Torvalds.
    ```
- Añadir los cambios a la zona de intercambio temporal.
- Hacer un commit de los cambios con el mensaje Añadido capítulo 1.
- Volver a mostrar el historial de cambios del repositorio.

###Resultado:
El primer paso para realizar la tarea será el clonado el repositorio propuesto por el profesor, posteriormente haremos un `git log` para comprobar el historial de cambios del repositorio.

![img](img/1_clone.png)

Salida comando `git log`
![img](img/2_git-log.png)

Lo siguiente será crear la carpeta capítulos y crear dentro de ella el fichero capitulo1.txt con el siguiente texto:
    ```
    - Git es un sistema de control de versiones ideado por Linus Torvalds.
    ```
![img](img/3_mk_and_echo.png)
- El comando `mkdir` crea una carpeta en la localización en la que nos encontramos.
- El comando `echo` recoge una cadena de texto y con los operadores >> lo metemos en un fichero llamado a nuestra elección, en este caso `capítulo1.txt` tal y como se pide en la tarea.

El siguiente paso será añadirlos a la zona de intercambio temporal `stage` y hacer un commit además de añadir un mensaje descriptivo al mismo, por ejemplo `Añadido capítulo 1.`.
![img](img/4_commit.png)

Una vez hecho esto, volveremos a emplear el comando `git.log` para comprobar los nuevos cambios que hemos añadido sobre nuestro repo.
![img](img/5_git_log.png)


Algo que es interesante destacar es que si nos fijamos en la ruta de la terminal `\Tareas\Tarea3`, estamos trabajando en un repositorio git dentro de otro repositorio git `\ets`(A elección propia con fines organizativos solamente). Lo curioso es ver como git sabe que esto es así y nos detecta cambios en ramas distintas...
Por un lado `origin/main` y por otro lado `HEAD -> main` que aunque no es una rama en si, me parece muy curioso como Git mueve ese Head al repo en el que estamos trabajando actualmente, donde hemos hecho el commit `Añadido capítulo 1`.
