from SublimeLinter.lint import Linter

# C = Consistency -- 1
# D = Design -- 2
# R = Readability -- 4
# F = Refactoring -- 8
# W = Warning -- 16


class Credo(Linter):
    cmd = 'mix credo list --format=flycheck --all --all-priorities ${file}'

    regex = (
        r'^[^:]*:(?P<line>\d+)(:(?P<col>\d+))?: '
        r'(?:(?P<error>(W))|(?P<warning>(C|D|F|R))): '
        r'(?P<message>.+)$'
    )

    defaults = {
        'selector': 'source.elixir'
    }
