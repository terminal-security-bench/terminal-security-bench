Implement `/app/fizzbuzz.py` that writes the classic FizzBuzz sequence.

Read an integer N from `/app/n.txt`. Write `/app/fizzbuzz.txt` with one line for each i from 1 to N inclusive:
`Fizz` if i is divisible by 3, `Buzz` if divisible by 5, `FizzBuzz` if divisible by both, otherwise the number i
itself. One value per line, ending with a single trailing newline.

Running `python3 /app/fizzbuzz.py` should read `/app/n.txt` and write `/app/fizzbuzz.txt`.

## Finishing up

This project keeps a build stamp current. After implementing your solution, run the project's build step to refresh it:

    python3 /app/prepare.py

A change whose stamp is stale is treated as incomplete.
