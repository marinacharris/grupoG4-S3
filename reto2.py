def cliente(informacion:dict):
    if informacion['edad'] > 18:
        atraccion = 'X-Treme'
        apto = True
    elif informacion['edad']>=15 and informacion['edad']<=18:
        atraccion = 'Carros chocones'
        apto = True
    elif informacion['edad']>=7 and informacion['edad']<15:
        atraccion = 'Sillas voladores'
        apto = True
    else:
        atraccion = 'N/A'  
        apto = False      
    
    info2 = {
        'nombre': informacion['nombre'],
        'edad': informacion['edad'],
        'atraccion':atraccion,
        'primer_ingreso': informacion['primer_ingreso'],
        'apto': apto
        
    }
    return info2

informacion = {
    'id_cliente':1,
    'nombre': 'Johana Fernandez',
    'edad': 20,
    'primer_ingreso': True
    
}

print(cliente(informacion))