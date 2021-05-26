if __name__ == "__main__":
    from src.load_data import words as API, data_path
    from src.App import App
    from pathlib import Path

    root_path = Path(__file__).parent.absolute()
    analysis_parameters = {
        "points": {
            "define_strong": 3,
            "define_weak": -5,
            "define_mastered": 5,
            "increase_rate": 1,
            "decrease_rate": 2,  #
        },
        "API": {
            "data_copy": API.copy(),
            "path": data_path,  #
        },
    }

    App(
        words=API,
        root_path=root_path,
        analysis_parameters=analysis_parameters,  #
    ).create_gameplay()
