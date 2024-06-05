import asyncio

#función asíncrona para imprimir los números primos.
async def print_prime_numbers():
    print("Generando los primeros 100 números primos...")

    # Espera 2 segundos para simular un proceso de generación.
    await asyncio.sleep(2)

    #función interna para generar los números primos.
    async def generate_primes():
        # Función para verificar si un número es primo.
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        count = 0  # Contador de números primos encontrados.
        num = 2    # Número actual a verificar si es primo.
        while count < 100:  # Generar 100 números primos.
            if is_prime(num):  
                yield num  
                count += 1  #
            num += 1 

    #Bucle asíncrono para obtener los números primos generados.
    async for prime in generate_primes():
        print(prime)  # Imprime el número primo.


asyncio.run(print_prime_numbers())
