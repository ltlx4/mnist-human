from django.shortcuts import render 
import csv
# Create your views here.


def index(request):
    return render(request, 'website/index.html')

def test(request):
    file = open('static/csv/mnist_test.csv')
    csvreader = csv.reader(file)
    # header = next(csvreader)
    # print(header)
    # rows = []
    # for row in csvreader:
    #     rows.append(row)
    # return print(rows)
    return render(request, 'website/index.html')