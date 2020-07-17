from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, nome, idade):
    return HttpResponse("<h1>Hello World, {} ({} anos)</h1>".format(nome, idade))

def calc(request, op1, operacao, op2):
        if operacao=="+":
            return HttpResponse("{} {} {} = {}".format(op1, operacao, op2, op1+op2))
        elif operacao=="-":
            return HttpResponse("{} {} {} = {}".format(op1, operacao, op2, op1-op2))
        elif operacao=="*":
            return HttpResponse("{} {} {} = {}".format(op1, operacao, op2, op1*op2))
        elif operacao==":":
            try:
                return HttpResponse("{} {} {} = {}".format(op1, operacao, op2, op1/op2))
            except:
                return HttpResponse("Erro: Divisão por zero.")
