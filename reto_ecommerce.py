productos = [
    {"id": 1, "nombre": "Laptop Pro 14", "categoria": "Computo", "precio": 25000, "descuento": 0.10, "stock": 5},
    {"id": 2, "nombre": "Mouse Gamer X", "categoria": "Accesorios", "precio": 1200, "descuento": 0.15, "stock": 20},
    {"id": 3, "nombre": "Teclado Mecánico K1", "categoria": "Accesorios", "precio": 2200, "descuento": 0.05, "stock": 10},
    {"id": 4, "nombre": "Monitor 27'' 4K", "categoria": "Computo", "precio": 8000, "descuento": 0.20, "stock": 7},
    {"id": 5, "nombre": "Audífonos Bluetooth Z", "categoria": "Audio", "precio": 1500, "descuento": 0.0, "stock": 15},
]

ventas = [
    {"venta_id": 101, "producto_id": 1, "cantidad": 1, "cliente": "Ana"},
    {"venta_id": 102, "producto_id": 2, "cantidad": 2, "cliente": "Luis"},
    {"venta_id": 103, "producto_id": 4, "cantidad": 1, "cliente": "Sofía"},
    {"venta_id": 104, "producto_id": 2, "cantidad": 1, "cliente": "Carlos"},
    {"venta_id": 105, "producto_id": 5, "cantidad": 3, "cliente": "Ana"},
]

tienda_info = ("TechieStore", "Santiago", 2025)


# print("Bienvenidos a " + tienda_info[0] +" en " + tienda_info[1] + " Año " + tienda_info[2].__str__())
print(f"Bienvenidos a {tienda_info[0]} en {tienda_info[1]} Año {tienda_info[2]}")

print("-----------------------------------------------------------")

total_productos = len(productos)

print(f"Total de productos disponibles: {total_productos}")

producto_final1 = productos[0]
producto_final2 = productos[1]
producto_final3 = productos[2]
producto_final4 = productos[3]
producto_final5 = productos[4]
precio_final1 = producto_final1["precio"] - (producto_final1["precio"] * producto_final1["descuento"])
precio_final2 = producto_final2["precio"] - (producto_final2["precio"] * producto_final2["descuento"])
precio_final3 = producto_final3["precio"] - (producto_final3["precio"] * producto_final3["descuento"])
precio_final4 = producto_final4["precio"] - (producto_final5["precio"] * producto_final4["descuento"])
precio_final5 = producto_final5["precio"] - (producto_final4["precio"] * producto_final5["descuento"])

print(f"producto: {producto_final1['nombre']}, precio final con descuento: ${precio_final1}")
print(f"producto: {producto_final2['nombre']}, precio final con descuento: ${precio_final2}")
print(f"producto: {producto_final3['nombre']}, precio final con descuento: ${precio_final3}")
print(f"producto: {producto_final4['nombre']}, precio final con descuento: ${precio_final4}")
print(f"producto: {producto_final5['nombre']}, precio final con descuento: ${precio_final5}")

print("-----------------------------------------------------------")


venta1 = ventas[0]
venta2 = ventas[1]  
venta3 = ventas[2]
venta4 = ventas[3]
venta5 = ventas[4]

print(f"Venta ID: {venta1['venta_id']}, {venta1['cliente']} compro {venta1['cantidad']} unidad(es) {producto_final1['nombre']} y pago ${precio_final1 * venta1['cantidad']}")
print(f"Venta ID: {venta2['venta_id']}, {venta2['cliente']} compro {venta2['cantidad']} unidad(es) {producto_final2['nombre']} y y pago ${precio_final2 * venta2['cantidad']}")
print(f"Venta ID: {venta3['venta_id']}, {venta3['cliente']} compro {venta3['cantidad']} unidad(es) {producto_final4['nombre']} y pago ${precio_final4 * venta3['cantidad']}")
print(f"Venta ID: {venta4['venta_id']}, {venta4['cliente']} compro {venta4['cantidad']} unidad(es) {producto_final2['nombre']} y y pago ${precio_final2 * venta4['cantidad']}")
print(f"Venta ID: {venta5['venta_id']}, {venta5['cliente']} compro {venta5['cantidad']} unidad(es) {producto_final5['nombre']} y y pago ${precio_final5 * venta5['cantidad']}")


print("-----------------------------------------------------------")

total_ingresos = (precio_final1 * venta1['cantidad'] + precio_final2 * venta2['cantidad'] + precio_final3 * venta3['cantidad'] + precio_final4 * venta4['cantidad'] + precio_final5 * venta5['cantidad'])   


print(f"Ingreso total del día: ${total_ingresos}")