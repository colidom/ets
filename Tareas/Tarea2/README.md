# Tarea 2: Manipulación de repositorios en Git
##### Alumno: Carlos Javier Oliva Domínguez 
##### N. Lista: 26

### Descripción de la tarea
*La siguiente tarea tiene como objetivo que el alumno se familiarice con la creación y manipulación de repositorios en GIT. Para conseguirlo se irán describiendo los pasos necesarios para la realización de cada una de las acciones necesarias.*



**Índice**

0. [Preparando la máquina](#id0)
1. [Configuración](#id1)
2. [Creación de un repositorio](#id2)
3. [Comprobar el estado del repositorio](#id3)
4. [Realizando Commit´s](#id4)
5. [Modificación de ficheros](#id5)
6. [Historial](#id6)

---
### Tareas

## 0. Preparando la máquina<a name="id1"></a>
Primeramente vamos a preparar la máquina para actualizar los paquetes y crear el arbol de dependencias de Linux. 
![sudo apt update](./img/1_update.png)

Posteriormente instalaremos git en la misma ya que no viene por defecto.
![sudo apt install](./img/2_apt_install.png)

Podremos comprobar que se ha instalado correctamente mediante el comando `git --version`.
![git version](./img/3_version.png)

## Configuración<a name="id1"></a>
Acto seguido configuraremos Git definiendo el nombre del usuario, el correo electrónico y activando el coloreado de la salida.
![git config](./img/4_config.png)


## Creación de un repositorio<a name="id2"></a>
Ahora crearemos un repositorio nuevo con el nombre dpl.
![git init](./img/5_init.png)


## Comprobar el estado del repositorio<a name="id3"></a>
Vamos a comprobar el estado del repositorio y como lo hemos creado hace apenas unos instantes comprobaremos que el control de versiones nos alerta de que `No hay commits todavía`, lo cual es correcto porque aún no hemos añadido ningún cambio.
![git status](./img/6_status.png)

Eso está a punto de cambiar, crearemos un fichero llamado indice.txt y añadiremos contenido al mismo.
![touch](./img/7_touch.png)

Mediante el comando `git status` comprobaremos el estado del repositorio en local y comprobaremos que hay cambios nuevos pero que aún no se han añadido al *STAGE*(mostrando el nombre del fichero en <span style="color:red">color rojo</span>).

>El STAGE es donde añadiremos los ficheros que han sido modificados para posteriormente añadir un commit que haga referencia a los cambios del mismo.

![git status](./img/8_status.png)

El comando `git add` nos permite añadir al STAGE los ficheros que han sido modificados. Como se puede ver, una vez añadidos están en el STAGE(mostrando el nombre del fichero en <span style="color:green">color verde</span>).
![git add](./img/9_add_status.png)


## Realizando Commit´s<a name="id4"></a>
Añadiremos un commit descriptivo que explique brevemente los cambios que hemos hecho en el fichero y mostramos el estado del mismo.
![git commit](./img/10_commit.png)


## Modificación de ficheros<a name="id5"></a>
Lo siguiente será añadir nuevas líneas a nuestro fichero, haremos uso del comando `git status` y veremos que pasa...
Git nos dice que el fichero ha sido modificado y lo representa en <span style="color:red">color rojo</span>. Además de informarnos que hagamos un `git add` y/o `git commit -a` que añade todos los ficheros modificados al STAGE.
> El parámetro * al añadir los ficheros(git add) indica que queremos añadir todos los ficheros modificados que hay en nuestro local.

![git add again](./img/11_add_again.png)

Ejecutamos los comandos y veremos que 
![git commit again](./img/12_commit_again.png)

## Historial<a name="id5"></a>
Mostraremos los cambios de la última versión del repositorio con respecto a la anterior con el comando `git show`.
![git show](./img/13_show.png)

Dado el caso de equivocarnos, podemos corregir el mensaje del commit si aún no lo hemos subido al origen(servidor), para ello haremos uso del comando `git --amend` y cambiaremos el commit.
![git amend](./img/14_amend.png)
Una vez hayamos añadido el nuevo mensaje vamos a mostrar nuevamente el último cambio realizado.
![git amend](./img/15_show_again.png)
