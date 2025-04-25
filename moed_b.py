from flask import Flask, render_template, request
from more_itertools import powerset

app = Flask(__name__)


@app.route('/food_arranger', methods=['POST', 'GET'])
def food_arranger():
    if request.method == 'POST':
        food_dict = {}
        max_cal = request.form.get('max_cal')
        min_prot = request.form.get('min_prot')
        for i in range(1, 4):
            food = request.form.get(f"food{i}")
            cal = request.form.get(f"cal{i}")
            prot = request.form.get(f"prot{i}")
            food_dict[i] = (food, cal, prot)

        best_arrange = 0
        result = 0
        combinations = list(powerset([1, 2, 3]))
        for comb in combinations[1:]:
            qty = len(comb)
            if qty > best_arrange:
                foods = []
                cals = 0
                prots = 0
                for n in comb:
                    food = food_dict[n]
                    foods.append(food[0])
                    cals += food[1]
                    prots += food[2]
                if cals <= max_cal and prots >= min_prot:
                    best_arrange = qty
                    result = (foods, cals, prots)
        return render_template('show_arrange.html', best=best_arrange, result=result)

    else:
        return render_template('food_arranger.html')


if __name__ == "__main__":
    app.run(debug=True)
