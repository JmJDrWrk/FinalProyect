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
>     appsArray = win10.toRunnableApp(appsStringArray)
> File "c:\Users\Jaime\3D Objects\ProyectoFinDeCiclo\RunnableProgram.py", line 145, in
> ```
>
> toRunnableApp
> runnableApps.append(RunnableApp(app_properties[3]))
> File "c:\Users\Jaime\3D Objects\ProyectoFinDeCiclo\RunnableProgram.py", line 45, in __init__
> state_value = values[3]
> IndexError: list index out of range

# En funcionamiento

> ```
> main.py
> WindowsInteractuable.py -- Clase importada en main.py
> RunnableApp.py  -- Clase importada en main.py
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


# Autoría	

MOai

# Coolaboradores

ninguno.
