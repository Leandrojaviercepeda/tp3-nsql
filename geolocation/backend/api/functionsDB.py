from connectionDB import client

def generate_points():
    con = client()
    con.flushdb()
    con.geoadd('breweries',-58.2361143,-32.480575,'Drakkar',-58.2504781,-32.4773196,'Lagash',-58.2401659,-32.4812371,'Tractor')
    con.geoadd('universities',-58.2355213,-32.479067,'UADER FCyT',-58.2305606,-32.4846711,'UADER FHAyCS',-58.2318001,-32.4958,'UTN FRCU')
    con.geoadd('pharmacy',-58.2351599,-32.4862249,'Alberdi',-58.2331543,-32.486659,'Suarez',-58.2366414,-32.485827,'Argentina')
    con.geoadd('emergencies',-58.2369422,-32.4842218,'Alerta',-58.2331737,-32.483037,'Vida',-58.2389064,-32.479766,'Cooperativa Medica')
    con.geoadd('supermarkets',-58.232506,-32.4892655,'Gran Rex',-58.2439911,-32.4885239,'Dia',-58.246514,-32.4744789,'Impulso')
    return 'OK'

def add_point(point,longitude,latitude,name):
    con = client()
    con.geoadd(point,longitude,latitude,name)
    return "Se agrego el local {0} al punto {1}".format(name,point)

def user_radio(point,longitude,latitude):
    con = client()
    points = []
    points = con.georadius(point,longitude,latitude,5,unit='km',withdist=True)
    return points