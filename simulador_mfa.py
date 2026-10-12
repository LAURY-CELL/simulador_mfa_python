def iniciar_sesion_mfa(password_intento, codigo_mfa_intento): 
    password_real = "Uc3m2026"
    codigo_mfa_real = "458912"
    if password_intento != password_real:
        print("Error de Identidad: Contraseña incorrecta. Acceso denegado.")
    else:
        print("Contraseña correcta. Pasando al segundo factor de seguridad...")
        
        if codigo_mfa_intento == codigo_mfa_real:
            print("MFA Verificado. ¡Acceso concedido al sistema seguro!")
        else:
            print("Alerta: Codigo MFA incorrecto. Intento de hackeo bloqueado.")
print("--- PRUEBA 1: El atacante no se sabe la contraseña ---")
iniciar_sesion_mfa("clave_falsa", "458912")
print("\n--- PRUEBA 2: Robaron la contraseña pero No tienen tu móvil ---")
iniciar_sesion_mfa("Uc3m2026", "000000")
print("\n--- PRUEBA 3: Acceso legitimo del usuario ( Contraseña + MFA) ---")
iniciar_sesion_mfa("Uc3m2026", "458912")

