class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        numbers = self._handle_custom_delimiters(numbers)
        self._check_for_negatives(numbers)
        numbers = self._ignore_numbers_grater_1000(numbers)

        return sum(self._to_int_list(numbers))

    def _to_int_list(self, numbers: str) -> list:
        cleaned_numbers = numbers.replace("\n", ",")
        parts = cleaned_numbers.split(",")
        return [int(part) for part in parts]

    def _handle_custom_delimiters(self, numbers: str) -> str:
        if numbers.startswith("//") and "\n" in numbers:
            header, numbers = numbers.split("\n")
            delimiter = header[2:]
            numbers = numbers.replace(delimiter, ",")
        return numbers

    def _check_for_negatives(self, numbers:str) -> str:
        for number in self._to_int_list(numbers):
            if number < 0:
                raise ValueError(f"negatives not allowed {number}")

    def _ignore_numbers_grater_1000(self, numbers: str) -> str:
        no_large_numbers = []
        for number in self._to_int_list(numbers):
            if number >= 1000:
                continue
            no_large_numbers.append(str(number))
        numbers = ",".join(no_large_numbers)
        return numbers

c = StringCalculator()
print(c.add("2, 1001"))
