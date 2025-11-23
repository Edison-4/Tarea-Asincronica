# Actividad Asincronica: POO en Python con Herencia, Composición, Encapsulamiento y Métodos de Comportamiento

Este programa modela un sistema de transporte utilizando conceptos clave de Programación Orientada a Objetos (POO):

Herencia: Las clases Automovil y Motocicleta son hijas de la clase padre Vehiculo. Heredan atributos básicos (marca, modelo, año) y métodos comunes (encender/apagar).

Composición: Los vehículos tienen un Motor. En lugar de heredar de Motor, se pasa una instancia de la clase Motor al constructor del automóvil o la motocicleta, permitiendo que cada vehículo tenga su propia fuente de potencia.

Encapsulamiento: Se usan decoradores (@property) para proteger y gestionar el acceso a los atributos internos de las clases.

En resumen: El script ejecucion.py crea motores independientes, los instala dentro de coches y motos, y finalmente demuestra cómo interactúan todas las partes imprimiendo sus estados y acciones.

<img width="1920" height="1080" alt="Captura de pantalla 2025-11-14 134250" src="https://github.com/user-attachments/assets/5289f938-fece-4cef-bd3a-1be64d46f76d" />
