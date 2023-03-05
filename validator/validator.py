class Validator:
    @staticmethod
    def name_validate_for_empty_and_white_spaces(name, massage):
        if name.strip() == "":
            raise ValueError(massage)

    @staticmethod
    def value_validation(value, massage):
        if value <= 0:
            raise ValueError(massage)

    @staticmethod
    def validate_table_number(value, min_value, max_value, massage):
        if value < min_value or value > max_value:
            raise ValueError(massage)
