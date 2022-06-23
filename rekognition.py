import boto3

def detect_text(photo, bucket,lista):

    client=boto3.client('rekognition')

    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    listaPalabras=[]        
    textDetections=response['TextDetections']
    print ('Detected text\n----------')
    for text in textDetections:
            if(text['Confidence']>=0.95):
                for i in range(lista.lenght):
                    if(lista[i]==text['DetectedText']):
                        listaPalabras.append(text['DetectedText'])
            
    return listaPalabras

def main():
    lista =[""]
    bucket='bucket'
    photo='photo'
    listaPalabras=detect_text(photo,bucket,lista)
    for i in listaPalabras:
        print(i)


if __name__ == "__main__":
    main()