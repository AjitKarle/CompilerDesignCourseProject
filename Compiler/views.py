from django.shortcuts import render
from . import utils
# Create your views here.

def home(request): 
    return render(request, 'home.html')
def example1(request): 
    output = ""
    output = utils.mainCompiler("example1") 
    print("Output is: ", output)
    args = {}
    args['output'] = output
    return render(request, 'output.html', args)
def example2(request): 
    output = ""
    output = utils.mainCompiler("example2") 
    print("Output is: ", output)
    args = {}
    args['output'] = output
    return render(request, 'output.html', args)
def example3(request): 
    output = ""
    output = utils.mainCompiler("example3") 
    print("Output is: ", output)
    args = {}
    args['output'] = output
    return render(request, 'output.html', args)
def example4(request): 
    output = ""
    output = utils.mainCompiler("example4") 
    print("Output is: ", output)
    args = {}
    args['output'] = output
    return render(request, 'output.html', args)
def example5(request): 
    output = ""
    output = utils.mainCompiler("example5") 
    print("Output is: ", output)
    args = {}
    args['output'] = output
    return render(request, 'output.html', args)
def example6(request): 
    output = ""
    output = utils.mainCompiler("example6") 
    print("Output is: ", output)
    args = {}
    args['output'] = output
    return render(request, 'output.html', args)
def example7(request): 
    output = ""
    output = utils.mainCompiler("example7") 
    print("Output is: ", output)
    args = {}
    args['output'] = output
    return render(request, 'output.html', args)
def example8(request): 
    output = ""
    output = utils.mainCompiler("example8") 
    print("Output is: ", output)
    args = {}
    args['output'] = output
    return render(request, 'output.html', args)
def example9(request): 
    output = ""
    output = utils.mainCompiler("example9") 
    print("Output is: ", output)
    args = {}
    args['output'] = output
    return render(request, 'output.html', args)