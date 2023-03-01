from . import context_objective


def add_objective_json(id, array):
    text = str(id)
    data = context_objective.get_json_data()
    objective = get_single_objective(id)
    if objective == None:
        current_data = {
            "id": id,
            "array": array
        }
    else:
        for item in array:
            objective['array'].append(item)
        current_data = objective

    data[text] = current_data
    context_objective.store_json_data(data)


def remove_objective(id, item):
    text = str(id)
    data = context_objective.get_json_data()

    objective = get_single_objective(id)
    objective['array'].remove(item)
    data[text] = objective
    context_objective.store_json_data(data)


def get_single_objective(id):
    data = context_objective.get_json_data()
    text = str(id)
    return data[text]
