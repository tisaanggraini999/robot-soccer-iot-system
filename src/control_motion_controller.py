from control.decision_logic import compute_velocity

def process_vision(vision):
    return compute_velocity(
        vision["angle"],
        vision["distance"]
    )
