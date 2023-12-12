#!/bin/bash

# Bucket de destino
BUCKET_NAME="poc-data-sic"

# Loop para criar arquivos .txt
for i in {1..5}; do
  FILE_NAME="file${i}.txt"
  touch $FILE_NAME
  # Envia o arquivo .txt para o bucket
  s3cmd put $FILE_NAME s3://$BUCKET_NAME
done

# Loop para criar arquivos .jpg
for i in {1..5}; do
  FILE_NAME="image${i}.jpg"
  touch $FILE_NAME
  # Envia o arquivo .jpg para o bucket
  s3cmd put $FILE_NAME s3://$BUCKET_NAME
done

# Loop para criar arquivos .pdf
for i in {1..5}; do
  FILE_NAME="document${i}.pdf"
  touch $FILE_NAME
  # Envia o arquivo .pdf para o bucket
  s3cmd put $FILE_NAME s3://$BUCKET_NAME
done

# Loop para criar arquivos .csv
for i in {1..3}; do
  FILE_NAME="document${i}.csv"
  touch $FILE_NAME
  # Envia o arquivo .pdf para o bucket
  s3cmd put $FILE_NAME s3://$BUCKET_NAME
done

# Loop para criar arquivos .png
for i in {1..2}; do
  FILE_NAME="document${i}.png"
  touch $FILE_NAME
  # Envia o arquivo .pdf para o bucket
  s3cmd put $FILE_NAME s3://$BUCKET_NAME
done