from django.shortcuts import render


# Create your views here.

def calculate(request):
    query = request.GET.getlist("name", "rrrrrrrrrr")
    print(query)
    context = {"name": query, "test": "lalala"}
    return render(request, "calculate.html", context)


def calculate_operation(request):
    if request.method == "GET":
        return render(request, "calculate.html")
    else:
        numbers = request.POST.get("numbers")


secret_numbers = [1, 2, 3, 4]


def calculation_operational(request):
    if request.method == "GET":
        return render(request, "calculate.html")
    else:
        if len(secret_numbers) != 4:
            return "The amount of integers should be equal to 4"
        if len(secret_numbers) != 4:
            return "The amount of integers should be equal to 4"
        if len(secret_numbers) != len(set(secret_numbers)):
            return "The value should be unique"
        for i in secret_numbers:
            if i > 9 or i < 1:
                return "Numbers must be greater than 1 and less than 10"

        return render(request, "calculate.html")


def get_result(request):
    bulls = 0
    cows = 0
    for i in range(len(secret_numbers)):
        if secret_numbers[i] == secret_numbers[i]:
            bulls += 1
        elif secret_numbers[i] in secret_numbers:
            cows += 1
        if bulls == 4:
            return "Winner"
        elif bulls or cows:
            return f"You got{bulls} bulls and {cows} cows"
        else:
            return "No identical numbers"

