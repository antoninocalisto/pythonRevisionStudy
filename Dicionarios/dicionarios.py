usuarios = []
print(usuarios)

usuarios = {"chaves": ["chaves do 8", "24/12/2017", "Recep_01"],
            "quico": ["Quico das flores", "20/12/2019", "Raio_x_03"]
            }
print(usuarios)

usuarios["dona florinda"] = ["Dona FLorianda", "23/05/2018", "Raio_x_01"]
print(usuarios.get("quico"))