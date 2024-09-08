##Para correr el programa se debe tener la librería "pyswip" instalada además de "swipl" en las variables de entorno de Windows

from pyswip import Prolog

options = [];
prolog = Prolog();
prolog.consult("vulnerabilities.pl");


devices = list(prolog.query("dispositivo(X, Y)"));

for value in devices:
    options.append({
        "type_id": value['X'],
        "name": value['Y']
    });
    
if(len(options) > 0):
    while 0 == 0:
        print("\nLista de dispositivos:");
        print("0. Detener programa");
        for value in options:
            print("{0}. {1}".format(value["type_id"], value["name"]));
        user = input("\nEscoge el número del dispositivo:\n");
        if(user == "0"):
            print("Bye");
            break
        vulnerabilities = list(prolog.query("vulnerabilidad("+user+", Y)"));
        if(len(vulnerabilities) > 0):
            print("*********************");
            print("VULNERABILIDADES:\n");
            for value in vulnerabilities:
                print("-", value["Y"]);
            print("\n*********************");

    




