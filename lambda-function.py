import json
import boto3
import os
import sys
import datetime


def send_s3_file(data):
  dt = datetime.datetime.now()
  s3 = boto3.resource('s3')
  bucket = s3.Bucket('site-data-challenge')
  key = f'{dt}.txt'
  with open('/tmp/file.txt', 'w', encoding='UTF8', newline='') as file:
    for k,v in data.items():
      file.write(f'{k}: {len(v)}\n')
    file.close()
  bucket.upload_file('/tmp/file.txt', key)
  
def delete_messages(messages, queue):
  try:
    entries = [
      {"Id": str(ind), "ReceiptHandle": msg.receipt_handle}
      for ind, msg in enumerate(messages)  
    ]
    response = queue.delete_messages(Entries=entries)
  except:
    print("error deleting messages")

def lambda_handler(event, context):
  
  # Obter o bucket S3
  s3 = boto3.resource('s3', region_name='us-east-1')
  bucket = s3.Bucket('site-data-challenge')

  # Ler as mensagens da fila SQS
  sqs = boto3.resource('sqs')
  queue = sqs.Queue('count_files_queue')
  
  arquivos_por_extensao = {}

  # Ler as mensagens da fila
  while True:
    messages = queue.receive_messages(MaxNumberOfMessages=10)
    # Verificar se existem mensagens
    if messages:
      # Processar cada mensagem
      for message in messages:
        # Obter o conteúdo da mensagem
        body = json.loads(message.body)
        for object in body['Records']:
          extensao = ((object['s3']['object']['key']).split('.')[-1]).lower()
          if extensao in arquivos_por_extensao:
            arquivos_por_extensao[extensao].append(object['s3']['object']['key'])
          else:
            arquivos_por_extensao[extensao] = [object['s3']['object']['key']]
      delete_messages(messages, queue)
    else:
      break
  if arquivos_por_extensao:
    print("Sending file to S3")
    send_s3_file(arquivos_por_extensao)
