n, m = map(int, input().split())


def center(string: str, width: int = m, char: str = "-") -> str:

    return string.center(width, char)


print(
    "\n".join(
        (top_half := [center(".|." * i) for i in range(1, n, 2)])
        + [center("WELCOME")]
        + top_half[::-1]
    )
)