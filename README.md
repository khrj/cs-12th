# CS Answers

_This repository is not intended to be used standalone without the given classroom resource._

**None of the one-liners given here are idiomatic. Please do
not write production code using this as an example.**

**Table of contents:**

-   [Question Bank Solutions](#question-bank-solutions)
-   [Assignment Solutions](#assignment-solutions)
-   [Test Solutions](#test-solutions)
-   [Difference between one-liners and one-liners<sup>[strict]</sup>](#difference-between-one-liners-and-one-linersstrict)
-   [Contributing](#contributing)

## Question Bank Solutions

| Topic                                          | Idiomatic | One-liners | One-liners<sup>[strict]</sup> |
| ---------------------------------------------- | --------- | ---------- | ----------------------------- |
| [Fundamentals and data handling][fundamentals] |           | ✔          |                               |
| [Data handling libraries][handling]            |           |            |                               |
| [Control flow and iterative statements][flow]  | ✔         |            |                               |
| [Strings][strings]                             |           | ✔          |                               |
| [Lists][lists]                                 |           | ✔          |                               |
| [Tuples][tuples]                               |           | ✔          |                               |
| [Dictionaries][dictionaries]                   |           | ✔          |                               |
| [Functions][functions]                         |           | ✔          |                               |

[fundamentals]: https://github.com/khrj/cs-answers/tree/main/qbs/1-fundamentals-handling
[handling]: https://github.com/khrj/cs-answers/tree/main/qbs/2-data-handling-libraries
[flow]: https://github.com/khrj/cs-answers/tree/main/qbs/3-flow-conditional-iterative
[strings]: https://github.com/khrj/cs-answers/tree/main/qbs/4-strings
[lists]: https://github.com/khrj/cs-answers/tree/main/qbs/5-lists
[tuples]: https://github.com/khrj/cs-answers/tree/main/qbs/6-tuples
[dictionaries]: https://github.com/khrj/cs-answers/tree/main/qbs/7-dictionaries
[functions]: https://github.com/khrj/cs-answers/tree/main/qbs/8-functions

## Assignment Solutions

| Topic                            | Idiomatic | One-liners | One-liners<sup>[strict]</sup> |
| -------------------------------- | --------- | ---------- | ----------------------------- |
| [Flow of control][a-flow]        |           |            | ✔                             |
| [String manipulation][a-strings] |           |            | ✔                             |
| [SA1 practice][sa1-practice]     |           |            | ✔                             |
| [Lists][a-lists]                 |           |            | ✔                             |
| [Practice 1][practice-1]         |           |            | ✔                             |
| [Dictionaries][a-dict]           |           |            | ✔                             |
| [Practice 2][practice-2]         |           | ✔          |                               |
| [Practice 3][practice-3]         | ✔         |            |                               |
| [Functions 1][functions-1]       | ✔         |            |                               |
| [Functions 2][functions-2]       | ✔         |            |                               |

[a-flow]: https://github.com/khrj/cs-answers/tree/main/assignments/flow-of-control
[a-strings]: https://github.com/khrj/cs-answers/tree/main/assignments/string-manipulation
[sa1-practice]: https://github.com/khrj/cs-answers/tree/main/assignments/sa1-practice
[a-lists]: https://github.com/khrj/cs-answers/tree/main/assignments/lists
[practice-1]: https://github.com/khrj/cs-answers/tree/main/assignments/practice-1
[a-dict]: https://github.com/khrj/cs-answers/tree/main/assignments/dictionaries
[practice-2]: https://github.com/khrj/cs-answers/tree/main/assignments/practice-2
[practice-3]: https://github.com/khrj/cs-answers/tree/main/assignments/practice-3
[functions-1]: https://github.com/khrj/cs-answers/tree/main/assignments/functions-1
[functions-2]: https://github.com/khrj/cs-answers/tree/main/assignments/functions-2

## Test Solutions

| Topic       | Idiomatic | One-liners | One-liners<sup>[strict]</sup> |
| ----------- | --------- | ---------- | ----------------------------- |
| [FA2][fa-2] |           | ✔          |                               |

[fa-2]: https://github.com/khrj/cs-answers/tree/main/tests/FA2

## Difference between one-liners and one-liners<sup>[strict]</sup>

-   **One-liners**: Code written in a single line, using a single statement.
    **Statements separated by semi-colons in a single line are prohibited**.
    Exceptions (non-exhaustive):
    -   Import statements
    -   Guidelines imposed by the question ("define a function to-")
    -   Misc reasons which make code longer by a few lines
-   **One-liners<sup>[strict]</sup>**: Same as One-liners, except there are no
    exceptions. If an answer requires multiple lines, it is categorized into
    one-liners instead of one-liners<sup>[strict]</sup>.

## Contributing

Found a better solution to an answer? Perhaps one that reduces the number of
statements in an answer? Excellent! Please open a [pull request][pull-request]
or otherwise send your changes to me, while adhering to the following:

-   Don't reduce a one-liners<sup>[strict]</sup> rating to a one-liners rating
    (see [difference](#difference-between-one-liners-and-one-linersstrict))
-   In idiomatic files, name variables well

[pull-request]:
    https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request