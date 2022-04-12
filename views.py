from django.shortcuts import render
from rest_framework import generics, status
import io, csv, pandas as pd
from rest_framework.response import Response
from .models import File
from .serializers import FileUploadSerializer
import mysql.connector as mysql

class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    queryset = File.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)

        conn = mysql.connect(host='localhost', database='csv_upload', user='root', )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            # loop through the data frame
            for i, row in reader.iterrows():
                # pass in string values using %s
                sql = "INSERT INTO csv_upload.upload_file VALUES (%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, tuple(row))
                # commit connection to save our changes because the connection is not auto committed by default
                conn.commit()

        return Response({"status": "success"}, status=status.HTTP_201_CREATED)

class UploadFileList(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    queryset = File.objects.all()

    def get(self, request, format=None):
            connection = mysql.connect(host='localhost', database='csv_upload',user='root',)
            sql_select_Query = "SELECT * FROM upload_file"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            # get all records
            records = cursor.fetchall()
            print("\nPrinting each row")
            for row in records:
                print("date_time = ", row[0], )
                print("close = ", row[1])
                print("high  = ", row[2])
                print("low  = ", row[3])
                print("open  = ", row[4])
                print("volume  = ", row[5])
                print("instrument  = ", row[6], "\n")

            return Response(records)