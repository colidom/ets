## Tarea: Instalación del IDE Netbeans 12
Alumno: Carlos Javier Oliva Domínguez
N. Lista: 26

**Índice**

1. [Prerrequisitos](#id1)
2. [Instalación](#id2)
3. [Ejecutando Netbeans 15](#id3)
4. [Eliminar Netbeans](#id4)
5. [Instalación a través wget (Cualquier distribución Linux)](#id5)

---

##### Prerrequisitos <a name="id1"></a>
Primeramente comprobaremos que tenemos correctamente instalado Java en nuestro sistema:

![img](img/1_java-version.png)

##### Instalación <a name="id2"></a>
Ahora instalaremos Netbeans mediante el siguiente comando:
```
sudo snap install netbeans --classic
```

![img](img/2_install_netbeans.png)

##### Ejecutando Netbeans 15<a name="id3"></a>
Una vez instaldo podremos abrir el IDE y comprobamos su interfaz de bienvenida

![img](img/4_netbeans.png)


##### Eliminar Netbeans <a name="id4"></a>
Aunque no haremos este pasi, en caos de querer eliminar Netbeans usaremos el comando:

```
sudo snap remove netbeans
```

##### Instalación a través wget (Cualquier distribución Linux) <a name="id5"></a>

Ahora vamos a  realizar la instalación de `Netbeans 12.5` a través del comando `wget`.
![img](img/3_netbeans_12.png)

Otorgamos permisos de ejecución y lo ejecutamos
![img](img/4_chmod_install.png)

Ahora nos aparecerá el Asistente de instalación que tendrá el siguiente aspecto:

Haremos click en `Next`

![img](img/5_wizard_welc.png)

Dejaremos por defecto la ruta donde se instalará Netbeans y haremos click en `Next`
![img](img/6_install_path.png)

Nos aparecerá la siguiente pantalla y tendremos que esperar a que finalize el proceso.
![img](img/7_installing.png)

Finalmente podremos comprobar que la instalación ha finalizado correctamente.
![img](img/8_success_install.png)
