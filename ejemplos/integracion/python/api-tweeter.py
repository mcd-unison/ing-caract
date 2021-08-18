# Obtención de datos provenientes de twitter

# Vamos aver como se una una RestAPI con librería especializada, ya que
# es muy común encontrarse en estos casos. 

#%% Vamos a cargar las librerías necesarias

# Primero hay que instalar teepy con
# conda install -c conda-forge tweepy 

# Siempre tener a la mano la documentación
# http://docs.tweepy.org/en/latest/

import tweepy
import json
import pandas as pd

#%% Información para acceder a la API de Twetter

# En muchas APIs la información es privada y se firma un convenio de uso
# de datos que deslindan a la compañía del mal uso que le pueda uno dar
# a los datos.

# Para poder utilizar la interface de Twetter es necesario:
# 1. Contar con cuenta de Twitter y tener registrado el telefono 
#    (para la autentificación de dos tiempos).
#
# 2. Ir a la página de desarrolladores (estando registrado en Twetter) 
#    y crear una nueva App. https://developer.twitter.com/en/apps
#
# 3. En la página generada de tu App, puedes recuperar en el apartado 
#    Keys and Access Tokens la información necesaria para poder 
#    recuperar información.
#
# 4. En esta misma página debes de crear tu Access Token para que tu App 
#    pueda acceder a la información (Una clave por desarrollador y una 
#    clave por aplicación).

# Ya no podemos usarlos mios, porque me sacaron del tuiter

consumer_key = 'PN2ri0UvsLYawitO8Hako1PvM'
consumer_secret = 'fud3LXwVza6PQMAIRmA9Y9mJ6Gc2Y1uNkV3f8G2okPZHXrCdTK'
access_token = '43091680-zO6sw8j0VxjN2df1L3fUqMCFoRr78iNfq4eNtirqh'
access_token_secret = 'dt3eeJgi6fzFHzalwrH7oq2B624THUTEjhiqzrqpL9BzH'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#%% Leyendo tuits fuera de linea

mcd_tweets = api.user_timeline('@McdUnison', count=20)
for tweet in mcd_tweets:
    print(tweet.author.name + ': ')
    print(tweet.text)
    print("\n" + 20*'=')

#%% Obteniendo la lista de amigos de alguien
amigos_mcd = api.friends("@McdUnison", count=200)
print("Doscientos amigos de @McdUnison\n")
print("Id".center(20) + "|" + "user id".center(20) + "|" + "nombre".center(15))
print(20 * "-" + "+" + 20 * "-" + "+" + 15 * "-")
for amigo in amigos_mcd:
    print("{}|{}|{}".format(str(amigo.id).ljust(20), amigo.screen_name.ljust(20), amigo.name))

# %% Obteniendo TTs geolocalizados (usando WOEID)
# Revisar en https://www.findmecity.com

mx_trends = api.trends_place(23424900)
print("TTs en México:")
for trend in mx_trends[0]['trends'][:10]:
    print('\t{} ({})'.format(trend["name"], trend["url"]))

hillo_trends = api.trends_place(124785)
print("TTs en Hermosillo:")
for trend in hillo_trends[0]['trends'][:10]:
    print('\t{} ({})'.format(trend["name"], trend["url"]))

# %% Como ejecutar un script que se encuentre recolectando y guardando información

archivo = '../data/tweets_ejemplo.csv'

class Listener(tweepy.streaming.StreamListener):

    def on_data(self, data):
        try:
            tweet = json.loads(data)
        except Exception as e:
            print(e) 
            return True

        texto = tweet['text'].replace('\n', ' ').replace(',', '<coma>')
        usuario = '@' + tweet.get('user').get('screen_name')
        fecha = tweet.get('created_at')
        tweet = u'{},{},{}\n'.format(texto, usuario, fecha)
        
        self.archivo.write(tweet)
        return True

    def on_error(self, status):
        print(status)

with open(archivo, 'w', encoding='utf-8') as fp:
    fp.write('Texto, Usuario, Fecha_creacion\n')

with  open(archivo, 'a', encoding='utf-8') as fp:    
    listner = Listener()
    listner.archivo = fp
    twitterStream = tweepy.Stream(auth, listner)
    
    twitterStream.filter(track=['COVID', 'Salud', 'Sonora'])    

#%% Y ahora como lo vemos
df = pd.read_csv(archivo)
df.header()
