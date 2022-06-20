from django.shortcuts import render

# Create your views here.

def handle(request):
    query = request.GET.getlist("name", "rrrrrrrrrr")
    print(query)
    context = {"name": query, "test": "lalala"}
    return render(request, "calculate.html", context)


    response_body = '''
    <p>Guess 4 numbers. Enter them separated with spaces:</p>
    <form method="POST" action="/">
        <input type="text" name="numbers"/>
        <input type="submit" value="Send"/>
    </form>
    '''
    if request.method == "POST":
        request.body = request.body.decode()
        request_body = parse_qs(request.body)
        if request_body.get("numbers"):
            numbers_str = request_body["numbers"][0].split()
            print(numbers_str)
            # проверки
            response_body += ", ".join(numbers_str)
        else:
            response_body += "Error"

    response_body_length = len(response_body.encode())
    response = [
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        f'Content-Length: {response_body_length}',
        'Connection: close',
        '',
        response_body
    ]
    self.wfile.write('\r\n'.join(response).encode())
    # self.request.sendall("\r\n".join(response).encode())