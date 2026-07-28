from operations import sumar

def ejecutar_operacion() -> None:
    print("===Calculadora===")
    print(f"  Suma: 2 + 3 = {sumar(2, 3)}")

if __name__ == "__main__":
    ejecutar_operacion()