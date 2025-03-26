class Assertions:
    @staticmethod
    def assert_equal(actual, expected, message=""):
        assert actual == expected, f"{message} Diharapkan: {expected}, Ditemukan: {actual}"

    @staticmethod
    def assert_in(substring, string, message=""):
        assert substring in string, f"{message} '{substring}' tidak ditemukan dalam '{string}'"
