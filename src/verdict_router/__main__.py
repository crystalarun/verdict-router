from __future__ import annotations

import json
import sys

from verdict_router.route import route


def main(argv: list[str] | None = None) -> int:
    question = " ".join(argv if argv is not None else sys.argv[1:]).strip()
    if not question:
        print("Pass a question.")
        return 2
    result = route(question)
    json.dump({"question": question, **result.__dict__}, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
