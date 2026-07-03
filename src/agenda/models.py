class Contacto:
    def __init__(self, nombre, telefono, correo = None):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Correo: {self.correo}"
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "telefono": self.telefono,
            "correo": self.correo
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            nombre=data.get("nombre"),
            telefono=data.get("telefono"),
            correo=data.get("correo")
        )
    
    def actualizar(self, nombre=None, telefono=None, correo=None):
        if nombre:
            self.nombre = nombre
        if telefono:
            self.telefono = telefono
        if correo:
            self.correo = correo