if __name__ == "__main__":
    
    print("========= DEMOSTRACIÓN POO EN PYTHON =========\n")
    
    print("--- 🔧 Creando Motores ---")
    motor_v8 = Motor(tipo="V8 Gasolina", potencia=450)
    motor_electrico = Motor(tipo="Eléctrico Dual", potencia=670)
    motor_boxer = Motor(tipo="Bóxer 2 cilindros", potencia=110)
    motor_monocilindrico = Motor(tipo="Monocilíndrico 4T", potencia=30)
    
    print(motor_v8)
    print(motor_electrico)
    
    print("\n--- 🚗 Creando Automóviles ---")
    mi_mustang = Automovil(
        marca="Ford", 
        modelo="Mustang GT", 
        anio=2024, 
        motor=motor_v8,
        numero_puertas=2
    )
    
    mi_tesla = Automovil(
        marca="Tesla", 
        modelo="Model S Plaid", 
        anio=2025, 
        motor=motor_electrico,
        numero_puertas=4
    )
    
    print("\n--- 🏍️ Creando Motocicletas ---")
    mi_bmw_gs = Motocicleta(
        marca="BMW",
        modelo="R1250GS",
        anio=2023,
        motor=motor_boxer,
        cilindraje=1250
    )
    
    mi_honda = Motocicleta(
        marca="Honda",
        modelo="CRF 300L",
        anio=2024,
        motor=motor_monocilindrico,
        cilindraje=300
    )
    
    print("\n--- 🏁 Ejecutando Métodos del Mustang ---")
    print(mi_mustang)
    mi_mustang.encender()
    mi_mustang.tocar_claxon()
    mi_mustang.apagar()
    
    print("\n--- 🏁 Ejecutando Métodos del Tesla ---")
    print(mi_tesla)
    mi_tesla.encender()
    mi_tesla.abrir_maletero()
    mi_tesla.apagar()
    
    print("\n--- 🏁 Ejecutando Métodos de la BMW ---")
    print(mi_bmw_gs)
    mi_bmw_gs.encender()
    mi_bmw_gs.hacer_caballito()
    mi_bmw_gs.apagar()
    
    print("\n--- 🏁 Ejecutando Métodos de la Honda ---")
    print(mi_honda)
    mi_honda.encender()
    mi_honda.usar_patada_arranque()
    mi_honda.apagar()
    
    print("\n--- 🔄 Demostrando @setters ---")
    print(f"Potencia original del Mustang: {mi_mustang.motor.potencia} HP")
    mi_mustang.motor.potencia = 500
    print(f"Potencia modificada del Mustang: {mi_mustang.motor.potencia} HP")
    
    print(f"\nAño original del Tesla: {mi_tesla.anio}")
    mi_tesla.anio = 2026
    print(f"Año modificado del Tesla: {mi_tesla.anio}")
    
    print(f"\nCilindraje original Honda: {mi_honda.cilindraje}")
    mi_honda.cilindraje = 350
    print(f"Cilindraje modificado Honda: {mi_honda.cilindraje}")
    
    print("\n========= FIN DE LA DEMOSTRACIÓN =========\n")
