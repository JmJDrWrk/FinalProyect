
  

- YOU are in editor mode, to switch to view mode press `Cntrl + Shift + V`

  
  

# Estado de desarrollo

  

- Actualmente estoy desarrollando en paralelo La clase Runnable
Program, con la idea de substituir a su predecesora RunnableApp,
estoy trabajando en la propia clase.

- Especificamente estoy trabajando en el modiclo ToRunnableAoo de la
clase WindowsInteractuable implmentada en la misma, que debería de
dar el siguiente errore la clase*

  

> ```
> Traceback (most recent call last):
> File "c:\Users\Jaime\3D Objects\ProyectoFinDeCiclo\RunnableProgram.py", line 172, in module
> appsArray = win10.toRunnableApp(appsStringArray)
> File "c:\Users\Jaime\3D Objects\ProyectoFinDeCiclo\RunnableProgram.py", line 145, in
> toRunnableApp
> runnableApps.append(RunnableApp(app_properties[3]))
> File "c:\Users\Jaime\3D Objects\ProyectoFinDeCiclo\RunnableProgram.py", line 45, in __init__
> state_value = values[3]
> IndexError: list index out of range
> ```
  

# En funcionamiento

  

> ```
> main.py
> WindowsInteractuable.py -- Clase importada en main.py
> RunnableApp.py -- Clase importada en main.py
> HTML.py -- Clase importada en main.py
> JavaScript.py -- Clase importada en main.py
> ```
>
> index.html -- Generado por codigo index.css -- Preescrito a mano
> index.js -- Generado por codigo

  
  
  

# Otros Errores Y Posibles Correcciones

  

La clase LoadHtml deberia implementar un método más fiable de ejecución de servidor no apropiativo. El hilo de ejecución

  

parece ser bloqueado por bucle

  

```

python -m http.server port

```

  

# Big Bang Problems

    Skipping due to being a null line
    --------------------------------------------------
    Failed to obtain values[3] from: C:/Program Files (x86)/Steam/steam.exe
    Failed to obtain values[3] from: C:/Users/Jaime/AppData/Local/Gaijin/Program Files (x86)/NetAgent/gjagent.exe
    Failed to obtain values[3] from: C:/Users/Jaime/AppData/Roaming/Spotify/Spotify.exe
    Failed to obtain values[3] from: C:/Users/Jaime/AppData/Local/Discord/Update.exe
    Failed to obtain values[3] from: C:/Windows/system32/cmd.exe /c parameter1 parameter2 parameter3 ...
    Failed to obtain values[3] from: C:/Program Files/AMD/CNext/CNext/RadeonSoftware.exe
    Failed to obtain values[3] from: C:/Program Files/LGHUB/lghub.exe
    Failed to obtain values[3] from: C:/Users/Jaime/AppData/Local/Programs/Opera GX/assistant/browser_assistant.exe
    Failed to obtain values[3] from: C:/Users/Jaime/Desktop/Pruebas/GoogIe.exe
    Failed to obtain values[3] from: C:/Users/Jaime/Desktop/Pruebas/display_Image_comp_a.exe
    Failed to obtain values[3] from: C:/Users/Jaime/AppData/Local/Gaijin/Program Files (x86)/NetAgent/gjagent.exe
    Failed to obtain values[3] from: C:/Users/Jaime/AppData/Local/Programs/Opera/assistant/browser_assistant.exe

Probablemente sea un error de Ruta en la consulta REG QUERY {ruta}, quizá esta sea variable según el equipo en el que se esté trabajando

En cuyo caso es importante que la ruta sea una variable que se pueda calcular previamente a la ejecución del la consulta

--------------------------------------------------
# Autoría

  

MOai

  

# Coolaboradores

  

ninguno.