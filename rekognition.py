import boto3

def detect_text(photo, bucket,lista):
    #llamada a rekognition
    client=boto3.client('rekognition')
    #respuesta
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    listaPalabras=[]        
    textDetections=response['TextDetections']
    #for para recorrer todas las palabras detectadas
    for text in textDetections:
            # si se cumple que es mayor que 95 la confidence entra
            if(text['Confidence']>=0.95):
                for i in range(lista.lenght):
                    #si hay match se guarda en el array 
                    if(lista[i]==text['DetectedText']):
                        listaPalabras.append(text['DetectedText'])
            
    return listaPalabras

def main():
    #Generamos la lista de palabras
    lista =[""]
    bucket='bucket'
    photo='photo'
    #llamamos a la funcion encargada de buscar las palabras que estan en la lista y que tienen minimo un 95 de confidence
    listaPalabras=detect_text(photo,bucket,lista)
    #print aquellas palabras que han cumplido las dos condiciones
    for i in listaPalabras:
        print(i)


if __name__ == "__main__":
    main()